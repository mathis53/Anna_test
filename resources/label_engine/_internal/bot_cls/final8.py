"""
final8.py — Bot Colissimo nouvelle génération.

PRINCIPE :
- On garde 100% du rendu visuel de final7.py (template, positions, fonts).
- On remplace UNIQUEMENT :
  1. decode_3_barcodes_from_image  → robuste 3-N codes + zxingcpp fallback + filtre extras
  2. pick_zone2_text_by_key        → auto-Intermarché depuis code postal embarqué dans le code 2
  3. parse_generation_message      → suppression du suffixe :45
  4. handle_image / handle_generation_text  → ne passent plus zone2_key (auto-détecté)

Le code postal destinataire est extrait du **2e barcode** aux positions 3-7
(ex : `8R1772448848150001000023` → `77244`, `8R1910008848150001000023` → `91000`).

Intermarchés chargés depuis intermarche_fr.json (4447 magasins France).
Anti-doublon par user via SQLite (table zone2_last).
"""
import os, sys, json, math, re, sqlite3, threading, random
from io import BytesIO
from pathlib import Path
from typing import Optional, Tuple, List, Dict

# Fix DLL chemin (Windows pyzbar)
if sys.platform == "win32":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.environ["PATH"] = script_dir + os.pathsep + os.environ["PATH"]
    if hasattr(os, "add_dll_directory"):
        try: os.add_dll_directory(script_dir)
        except Exception: pass
    import ctypes
    for dll in ("libiconv-2.dll", "libzbar-0.dll"):
        try: ctypes.CDLL(os.path.join(script_dir, dll))
        except Exception: pass

from PIL import Image, ImageOps
from pyzbar.pyzbar import decode as zbar_decode

# ============================================================
# 1) INTERMARCHÉ DATABASE LOOKUP
# ============================================================
INTERMARCHE_JSON = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "intermarche_fr.json")
_INTERMARCHE_CACHE: Optional[List[dict]] = None
_RNG = random.SystemRandom()


def load_intermarche() -> List[dict]:
    global _INTERMARCHE_CACHE
    if _INTERMARCHE_CACHE is None:
        if not os.path.exists(INTERMARCHE_JSON):
            print(f"⚠️  intermarche_fr.json introuvable à côté de final8.py", file=sys.stderr)
            _INTERMARCHE_CACHE = []
        else:
            with open(INTERMARCHE_JSON, encoding="utf-8") as f:
                _INTERMARCHE_CACHE = json.load(f)
    return _INTERMARCHE_CACHE


def _haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    R = 6371.0
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat/2)**2
         + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2)
    return R * 2 * math.asin(math.sqrt(a))


def _postal_coords(postal5: str) -> Optional[Tuple[float, float]]:
    """Renvoie lat/lon d'un code postal 5 chiffres FRANÇAIS valide.
    Pour les Cedex (codes non standards), fallback département via la DB Intermarché."""
    # 1) Essai pgeocode (codes postaux français standards)
    try:
        import pgeocode
        nomi = pgeocode.Nominatim("fr")
        rec = nomi.query_postal_code(postal5)
        lat, lon = rec["latitude"], rec["longitude"]
        country = str(rec.get("country_code", "")).upper()
        # pgeocode peut retourner des codes belges ressemblants — on impose FR
        if lat == lat and lon == lon and country in ("FR", ""):
            # Vérif coords dans la métropole/DOM: lat 41-51, lon -5 to 10
            if 41 <= lat <= 51.5 and -5.5 <= lon <= 10:
                return float(lat), float(lon)
    except Exception:
        pass
    # 2) Cedex/inconnu : fallback département (2 premiers chiffres) via DB Intermarché
    dept = postal5[:2]
    matches = [s for s in load_intermarche()
               if (s.get("postcode") or "").startswith(dept)
               and s.get("lat") and s.get("lon")]
    if matches:
        # Centroid moyen pondéré par la cohérence du département
        avg_lat = sum(s["lat"] for s in matches) / len(matches)
        avg_lon = sum(s["lon"] for s in matches) / len(matches)
        return avg_lat, avg_lon
    return None


def find_intermarches_near(postal5: str, radius_km: float = 50.0,
                            french_only: bool = True) -> List[dict]:
    """Liste les Intermarchés français à <radius_km du code postal donné."""
    coords = _postal_coords(postal5)
    if not coords:
        return []
    lat, lon = coords
    full, partial = [], []
    for s in load_intermarche():
        slat, slon = s.get("lat"), s.get("lon")
        if slat is None or slon is None:
            continue
        if french_only:
            # Postcode français = 5 chiffres OU shop dans la zone géographique FR
            pc = (s.get("postcode") or "")
            if pc and (not pc.isdigit() or len(pc) != 5):
                continue
            if not (41 <= slat <= 51.5 and -5.5 <= slon <= 10):
                continue
        d = _haversine_km(lat, lon, slat, slon)
        if d > radius_km:
            continue
        item = {**s, "distance_km": round(d, 2)}
        (full if s.get("complete") else partial).append(item)
    full.sort(key=lambda s: s["distance_km"])
    partial.sort(key=lambda s: s["distance_km"])
    return full or partial


def format_intermarche_as_zone2_tuple(shop: dict) -> Tuple[str, str, str, str]:
    """Convertit {name,street,postcode,city,...} → (NOM_MAJ, rue, ville, "zip|ville")."""
    raw_name = (shop.get("name") or "Intermarché").upper()
    # Normalise pour matcher le style "INTERMARCHE SUPER XXX"
    if "INTERMARCHÉ" in raw_name and "SUPER" not in raw_name and "EXPRESS" not in raw_name and "CONTACT" not in raw_name:
        # Ajoute "SUPER" par défaut + nom de la ville
        city = (shop.get("city") or "").upper()
        name = f"INTERMARCHE SUPER {city}" if city else "INTERMARCHE SUPER"
    else:
        name = raw_name.replace("INTERMARCHÉ", "INTERMARCHE")
    street = shop.get("street") or "Avenue du Commerce"
    city_cap = (shop.get("city") or "").title()
    postal = shop.get("postcode") or "00000"
    line4 = f"{postal}|{city_cap}"
    return (name, street, city_cap, line4)


# ============================================================
# 2) ANTI-DOUBLON SQLITE (par user)
# ============================================================
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bot.db")
_db_lock = threading.Lock()


_zone2_table_ready = False

def zone2_last_init():
    global _zone2_table_ready
    if _zone2_table_ready: return
    with _db_lock:
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS zone2_last (
            user_id INTEGER PRIMARY KEY,
            last_postcode TEXT,
            last_city TEXT
        )""")
        con.commit(); con.close()
    _zone2_table_ready = True


def get_zone2_last(user_id: int) -> Optional[Tuple[str, str]]:
    zone2_last_init()
    with _db_lock:
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()
        cur.execute("SELECT last_postcode, last_city FROM zone2_last WHERE user_id=?", (user_id,))
        row = cur.fetchone(); con.close()
    return (row[0] or "", row[1] or "") if row else None


def set_zone2_last(user_id: int, postcode: str, city: str):
    zone2_last_init()
    with _db_lock:
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()
        cur.execute("INSERT INTO zone2_last(user_id, last_postcode, last_city) VALUES(?,?,?)"
                    " ON CONFLICT(user_id) DO UPDATE SET last_postcode=excluded.last_postcode,"
                    " last_city=excluded.last_city",
                    (user_id, postcode, city))
        con.commit(); con.close()


def pick_intermarche_for_user(postal5: str, user_id: int) -> Optional[Tuple[str, str, str, str]]:
    """Tirage random Intermarché 50km, anti-doublon par user. Retourne le tuple ZONE2 ou None."""
    shops = find_intermarches_near(postal5, radius_km=50.0)
    if not shops:
        return None
    last = get_zone2_last(user_id)
    if last and len(shops) > 1:
        shops = [s for s in shops if (s.get("postcode"), s.get("city","").upper()) != last] or shops
    chosen = _RNG.choice(shops)
    set_zone2_last(user_id,
                   chosen.get("postcode", ""),
                   (chosen.get("city") or "").upper())
    return format_intermarche_as_zone2_tuple(chosen)


# ============================================================
# 3) ROBUST BARCODE DECODER
# ============================================================
# Patterns pour identifier le rôle de chaque barcode par sa structure.
# Tolérant aux préfixes variables (pas que 8R).
PATTERNS = [
    # rôle, longueur, regex - du plus spécifique au plus large
    ("routing",  (15, 35), re.compile(r"^%\d+$")),                          # %XXXXXX...
    ("ext24",    (22, 26), re.compile(r"^[A-Z0-9]{2,3}\d{20,24}$")),        # 8R + 22 digits
    ("track13",  (12, 14), re.compile(r"^[A-Z0-9]{2}\d{10,12}$")),          # 8R + 11 digits
]

def _is_garbage_code(t: str) -> bool:
    """Vrai si le code n'a aucune chance d'être un vrai code Colissimo.
    Règle : doit commencer par % OU contenir au moins une lettre quelque part."""
    if not t: return True
    if t.startswith("%"): return False
    if any(c.isalpha() for c in t): return False
    # Tout-chiffres sans lettre = code parasite (Zalando 16, EAN-13, etc.)
    return True


def _try_zxingcpp(img: Image.Image):
    """Fallback de décodage : zxingcpp est plus tolérant à l'inclinaison/flou que pyzbar."""
    try:
        import zxingcpp
        out = []
        for r in zxingcpp.read_barcodes(img):
            try: txt = r.text
            except Exception: continue
            out.append(txt)
        return out
    except Exception:
        return []


def decode_3_barcodes_from_image_v2(img: Image.Image) -> Optional[Tuple[str, str, str]]:
    """Décode 3-N codes-barres d'un label Colissimo, retourne (track13, ext24, routing).

    Robuste à :
    - Inclinaison (essaye rotations multiples + zxingcpp fallback)
    - Nombre variable (3, 4, 5+ codes) — filtre par pattern, pas par ordre
    - Codes "extras" type retours Zalando 16 chiffres
    - Doublons (dédup auto)
    """
    img = ImageOps.exif_transpose(img)
    rgb = img.convert("RGB")
    gray = rgb.convert("L")

    # Décodage tous moteurs + toutes rotations
    raw_texts: List[str] = []
    for image_variant in (gray, rgb,
                          gray.rotate(90, expand=True),
                          gray.rotate(-90, expand=True),
                          gray.rotate(180, expand=True)):
        decoded = zbar_decode(image_variant) or []
        for d in decoded:
            try: txt = d.data.decode("utf-8").strip()
            except Exception: continue
            if txt: raw_texts.append(txt)
        if len(set(raw_texts)) >= 3:
            break
    # zxingcpp fallback
    if len(set(raw_texts)) < 3:
        raw_texts.extend(_try_zxingcpp(rgb))

    # Dédup + filtre tout-numérique (codes parasites Zalando, EAN, etc.)
    seen = set(); candidates: List[str] = []; dropped: List[str] = []
    for t in raw_texts:
        t = t.strip()
        if not t or t in seen: continue
        seen.add(t)
        if _is_garbage_code(t):
            dropped.append(t)
            continue
        candidates.append(t)
    if dropped:
        print(f"[final8] codes parasites ignorés: {dropped}", file=sys.stderr)

    # Classification par pattern (rôle)
    by_role: Dict[str, str] = {}
    for txt in candidates:
        for role, (lmin, lmax), pat in PATTERNS:
            if role in by_role: continue
            if lmin <= len(txt) <= lmax and pat.match(txt):
                by_role[role] = txt
                break

    # Fallback : si rôles manquent, assigner par longueur uniquement
    for txt in candidates:
        if txt in by_role.values(): continue
        L = len(txt)
        if "track13" not in by_role and 12 <= L <= 14:
            by_role["track13"] = txt
        elif "ext24" not in by_role and 22 <= L <= 26:
            by_role["ext24"] = txt
        elif "routing" not in by_role and txt.startswith("%"):
            by_role["routing"] = txt

    if "track13" in by_role and "ext24" in by_role and "routing" in by_role:
        result = (by_role["track13"], by_role["ext24"], by_role["routing"])
        print(f"[final8] DECODE OK (classifié) : {result}", file=sys.stderr)
        return result

    # Mode dégradé : trier par longueur croissante (les codes parasites ont déjà été filtrés)
    if len(candidates) >= 3:
        ordered = sorted(candidates, key=len)
        result = (ordered[0], ordered[1], ordered[2])
        print(f"[final8] DECODE FALLBACK (longueur) : {result}", file=sys.stderr)
        return result

    print(f"[final8] DECODE ÉCHEC (candidates={candidates})", file=sys.stderr)
    return None


# ============================================================
# 4) EXTRACTION POSTAL DEPUIS LE CODE 2
# ============================================================
def extract_postal_from_code2(code2: str) -> Optional[str]:
    """Le 2e barcode contient le code postal aux positions 3-7.
    Ex: '8R1772448848150001000023' → '77244'
        '8R1910008848150001000023' → '91000'
    """
    if not code2 or len(code2) < 8:
        return None
    candidate = code2[3:8]
    if candidate.isdigit() and len(candidate) == 5:
        return candidate
    return None


# ============================================================
# 5) PATCH POUR final7.py
# ============================================================
def patch_final7():
    """Applique les modifications sur final7. Appelle ça en haut de main()."""
    import final7

    # Init zone2_last DB
    final7.DB_PATH = DB_PATH
    zone2_last_init()

    # Thread-local pour passer le résultat Intermarché à pick_zone2_text_by_key
    _local = threading.local()

    original_render_result = final7.render_result
    original_pick = final7.pick_zone2_text_by_key

    def new_pick_zone2_text_by_key(key: str):
        # En priorité : tuple résolu pour le user courant
        resolved = getattr(_local, "resolved", None)
        if resolved:
            return resolved
        # Fallback ZONE2_MAP (ancien système, pour compat)
        return original_pick(key)

    def new_render_result(code1: str, code2: str, code3: str,
                          user_id: int, zone2_key: str = ""):
        # Auto-detect postal from code2
        postal = extract_postal_from_code2(code2)
        if postal:
            tuple_z = pick_intermarche_for_user(postal, user_id)
            if tuple_z:
                _local.resolved = tuple_z
                # On passe le postal détecté comme zone2_key
                # → get_zone2_part48_from_key(postal) appellera pick_zone2_text_by_key
                # → renverra notre tuple résolu
                zone2_key = postal
        try:
            return original_render_result(code1, code2, code3, user_id, zone2_key)
        finally:
            _local.resolved = None

    final7.pick_zone2_text_by_key = new_pick_zone2_text_by_key
    final7.render_result = new_render_result
    final7.decode_3_barcodes_from_image = decode_3_barcodes_from_image_v2

    # Drop le :45 dans parse_generation_message
    def new_parse(msg: str):
        payload = (msg or "").strip()
        if "|" in payload:
            payload = payload.split("|", 1)[0].strip()
        parts = [p.strip() for p in payload.split(":") if p.strip()]
        if len(parts) >= 3:
            return parts[:3], ""    # zone2_key vide → auto-detect plus tard
        return None, ""
    final7.parse_generation_message = new_parse

    # Help text mis à jour
    final7.HELP_TEXT = (
        "📌 Commandes:\n"
        "• /id  → affiche votre user_id\n"
        "• /balance → affiche votre solde\n"
        "• /redeem <CODE> → ajoute des points (si configuré)\n"
        "\n"
        "📷 Génération:\n"
        "Envoyez : CODE1:CODE2:CODE3\n"
        "Le code postal destinataire est auto-détecté depuis CODE2.\n"
        "Un Intermarché aléatoire dans 50km sera choisi (jamais 2× d'affilée).\n"
        f"(coût = {final7.COST_PER_IMAGE} points / image)\n"
        "\n"
        "🖼️ Génération via image :\n"
        "Envoyez simplement une photo du label (3 à 5 codes-barres OK).\n"
        "\n"
        "👑 Admin: /admin add <user_id> <points> | /admin set ..."
    )

    print("✅ final8 patches appliqués sur final7")
    print(f"📦 Base Intermarché : {len(load_intermarche())} magasins chargés")


# ============================================================
# MAIN
# ============================================================
def main():
    patch_final7()
    import final7
    final7.main()


if __name__ == "__main__":
    main()
