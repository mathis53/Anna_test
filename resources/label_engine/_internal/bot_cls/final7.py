import os
import random
import sqlite3
import string
import threading
from datetime import datetime, timedelta
from io import BytesIO
from pathlib import Path
from typing import Optional, Tuple, List

from PIL import Image, ImageDraw, ImageFont, ImageOps
from barcode import Code128
from barcode.writer import ImageWriter
from pyzbar.pyzbar import decode as zbar_decode

try:
    from telegram import Update
    from telegram.ext import (
        Application,
        CommandHandler,
        MessageHandler,
        ContextTypes,
        filters,
    )
except Exception:  # Bot Telegram absent (mode "étiquette uniquement" / packagé) :
    # on n'utilise que les fonctions de rendu ; on stube les symboles telegram
    # pour que l'import et les annotations des handlers ne cassent pas.
    class _TgStub:
        DEFAULT_TYPE = None
        def __getattr__(self, _):
            return _TgStub()
        def __call__(self, *a, **k):
            return _TgStub()
    Update = _TgStub()
    Application = CommandHandler = MessageHandler = ContextTypes = filters = _TgStub()

# =========================
# CONFIG
# =========================
TOKEN = (os.getenv("8339692763:AAFHTCI1eWfcwAqdJKq7W5jYkL7UcZ7GZ7I") or os.getenv("8339692763:AAFHTCI1eWfcwAqdJKq7W5jYkL7UcZ7GZ7I") or "8339692763:AAFHTCI1eWfcwAqdJKq7W5jYkL7UcZ7GZ7I").strip()

TEMPLATE_PATH = "template.jpg"

REF_W = 1190
REF_H = 1748

RNG = random.SystemRandom()

# - "none"   : Arial Regular
# - "light"  : 2 passes (gras léger centré)
# - "stroke1": stroke_width=1
BOLD_MODE = "light"

COST_PER_IMAGE = 3
RATE_LIMIT_SECONDS = 6
DB_PATH = "bot.db"

ADMIN_USER_IDS = {
    8435428062,  # <-- mets ton user_id ici
}

REDEEM_CODES = {
    # "PACK10": 10,
    # "PACK30": 30,
}

# =========================
# MESSAGES
# =========================
CUSTOM_MESSAGE = "Voici votre document."

SUCCESS_CAPTION_TEMPLATE = (
    "{custom}\n"
    "✅ Image générée avec succès.\n"
    "{debit_line}"
    "📌 Solde restant : {balance} points"
)

INSUFFICIENT_FUNDS_TEMPLATE = (
    "❌ Solde insuffisant.\n"
    "🧾 Solde actuel : {balance} points\n"
    "💳 Coût par image : {cost} points\n"
    "➡️ Recharge nécessaire."
)

RATE_LIMIT_MESSAGE = (
    "⏳ Trop de demandes.\n"
    "Veuillez réessayer dans quelques secondes."
)

HELP_TEXT = (
    "📌 Commandes:\n"
    "• /id  → affiche votre user_id\n"
    "• /balance → affiche votre solde\n"
    "• /redeem <CODE> → ajoute des points via un code (si configuré)\n"
    "\n"
    "📷 Génération:\n"
    "Envoyez : CODE1:CODE2:CODE3:45\n"
    "  - 45 = clé Zone 2 (ex: 45, 11, 875)\n"
    "Option compat: CODE1:CODE2:CODE3|45\n"
    f"(coût = {COST_PER_IMAGE} points / image)\n"
    "\n"
    "👑 Admin:\n"
    "• /admin add <user_id> <points>\n"
    "• /admin set <user_id> <points>\n"
    "\n"
    "🖼️ Génération via image:\n"
    "Envoyez une image contenant 3 codes-barres.\n"
    "Option: mettre une clé (ex: 45) en caption pour piloter la Zone 2."
)

# =========================
# BARCODE BOXES
# =========================
BOX1_X = 90
BOX1_Y = 293
BOX1_W = 536
BOX1_H = 312

BOX2_REF = (162, 939, 766, 329)
BOX3_REF = (131, 1424, 938, 246)


def scale_box(ref_box, img_w, img_h):
    rx, ry, rw, rh = ref_box
    x = int(rx * img_w / REF_W)
    y = int(ry * img_h / REF_H)
    w = int(rw * img_w / REF_W)
    h = int(rh * img_h / REF_H)
    return x, y, w, h


def scale_point(ref_pt, img_w, img_h):
    rx, ry = ref_pt
    x = int(rx * img_w / REF_W)
    y = int(ry * img_h / REF_H)
    return x, y


def scale_y(ref_y: int, img_h: int) -> int:
    return int(ref_y * img_h / REF_H)


# =========================
# TEXT ZONES (repères)
# =========================
ZONE1_START_REF = (687, 286)
ZONE2_START_REF = (60, 735)

ZONE1_GAP_REF = 2
ZONE2_GAP_REF = 2

ZONE2_LINE4_EXTRA_LINES = 1

# Espace entre PARTIE48 et PARTIE30 (via espaces mesurés en font30)
ZONE2_LINE4_SPACES = 2

# Réhausser la ligne 4 (48|30) : négatif = remonte
ZONE2_LINE4_Y_ADJUST_REF = -6

# Zone1: 4e champ VERTICAL (bas -> haut), Arial Bold 23
ZONE1_LINE4_POS_REF = (1138, 311)
ZONE1_LINE4_ANCHOR = "rt"
ZONE1_LINE4_SIZE = 23
ZONE1_LINE4_ROTATE_DEG = 90  # 90° => lecture bas -> haut

# =========================
# LISTES
# =========================
# Zone 1: "L1, L2, L3, L4" (L4 vertical)
ZONE1_LIST = [
    "LUCAS MARTIN, 12 RUE DES LILAS, 75019 PARIS, +33 732555532",
    "CLAIRE BERNARD, 8 AVENUE VICTOR HUGO, 06000 NICE, +33 674223897",
    "JULIEN DUBOIS, 25 BOULEVARD GAMBETTA, 59000 LILLE, +33 695673984",
    "SOPHIE PETIT, 3 IMPASSE DES MIMOSAS, 33200 BORDEAUX, +33 689335710",
    "ANTOINE ROBERT, 41 RUE NATIONALE, 37000 TOURS, +33 657448923",
    "EMMA RICHARD, 17 RUE DE LA REPUBLIQUE, 69002 LYON, +33 612794856",
    "PAUL DURAND, 6 PLACE BELLECOUR, 69002 LYON, +33 689238407",
    "LEA MOREAU, 22 CHEMIN DES VIGNES, 34160 CASTRIES, +33 683905472",
    "THOMAS SIMON, 9 RUE PASTEUR, 21000 DIJON, +33 672315198",
    "CAMILLE LAURENT, 14 RUE DES ECOLES, 75005 PARIS, +33 758230619",
    "HUGO LEFEVRE, 5 ALLEE DES TILLEULS, 91300 MASSY, +33 677998743",
    "CHLOE MICHEL, 28 RUE DU PORT, 17000 LA ROCHELLE, +33 615670829",
    "NICOLAS GARCIA, 19 AVENUE JEAN JAURES, 31000 TOULOUSE, +33 632145798",
    "LAURA DAVID, 7 RUE DES FLEURS, 68100 MULHOUSE, +33 614763985",
    "MAXIME BERTRAND, 11 RUE DU MOULIN, 14000 CAEN, +33 690865432",
    "MARION ROUX, 2 AVENUE DE PROVENCE, 13100 AIX-EN-PROVENCE, +33 687521410",
    "ADRIEN VINCENT, 36 RUE DE STRASBOURG, 44000 NANTES, +33 675941273",
    "JULIE FOURNIER, 10 RUE DU GENERAL LECLERC, 78000 VERSAILLES, +33 688741562",
    "QUENTIN MOREL, 4 CHEMIN DE BELLEVUE, 74200 THONON-LES-BAINS, +33 646582379",
    "ANAIS GIRARD, 15 RUE DES ACACIAS, 51100 REIMS, +33 654831902",
    "LOUIS ANDRE, 23 RUE SAINT-MICHEL, 35000 RENNES, +33 641582071",
    "INES LOPEZ, 18 BOULEVARD DE LA LIBERTE, 59800 LILLE, +33 691431567",
    "BAPTISTE MERCIER, 1 RUE DU CHATEAU, 86000 POITIERS, +33 633590481",
    "SARAH BLANCHARD, 20 RUE DE LA GARE, 27000 EVREUX, +33 635290846",
    "ROMAIN CHEVALIER, 9 PLACE DU MARCHE, 74000 ANNECY, +33 677443912",
    "NADIA PEREZ, 13 AVENUE DU PRADO, 13006 MARSEILLE, +33 681263004",
    "ARTHUR LEGRAND, 30 RUE PAUL BERT, 37100 TOURS, +33 662144788",
    "MANON GAUTHIER, 6 RUE DES PEUPLIERS, 94300 VINCENNES, +33 698201347",
    "AXEL PERRIN, 27 RUE VICTOR HUGO, 38400 SAINT-MARTIN-DHERES, +33 675290410",
    "ZOE MARCHAND, 16 RUE DES REMPARTS, 30000 NIMES, +33 632156948",
    "FLORIAN NOEL, 8 RUE DU STADE, 68000 COLMAR, +33 678413902",
    "ELISE CHARPENTIER, 21 RUE DES ARTISANS, 41000 BLOIS, +33 689078322",
    "MATHIS COUSIN, 12 RUE DES FRENES, 91000 EVRY, +33 611562473",
    "PAULINE BOUCHER, 33 AVENUE DE LA PAIX, 54500 VANDOEUVRE-LES-NANCY, +33 653984602",
    "THEO DUPUY, 5 RUE DU SOLEIL, 66000 PERPIGNAN, +33 624998635",
    "AMANDINE LEMOINE, 24 RUE DES JARDINS, 80000 AMIENS, +33 672635481",
    "SAMUEL RENAUD, 14 RUE DU PONT, 22200 GUINGAMP, +33 689108762",
    "NOEMIE FAURE, 19 RUE DES OLIVIERS, 26200 MONTELIMAR, +33 671210384",
    "ENZO VIDAL, 7 CHEMIN DE LA PLAINE, 34400 LUNEL, +33 687347108",
    "CLARA BRUN, 11 RUE DES CEDRES, 05000 GAP, +33 634129845",
    "VICTOR PICHON, 26 RUE LAFAYETTE, 75010 PARIS, +33 698405732",
    "MAELLE REY, 4 RUE DES PINS, 56600 LANESTER, +33 611027483",
    "LUCAS SAUVAGE, 18 RUE DU LAC, 74000 ANNECY, +33 647893521",
    "EVA COLIN, 9 RUE DE LA LIBERTE, 10000 TROYES, +33 695140873",
    "KEVIN MOULIN, 31 BOULEVARD CLEMENCEAU, 63100 CLERMONT-FERRAND, +33 673561903",
    "ALICE TESSIER, 6 RUE DES SOURCES, 07200 AUBENAS, +33 661482359",
    "DYLAN HENRY, 2 AVENUE DU STADE, 72000 LE MANS, +33 634907211",
    "ROMANE LUCAS, 29 RUE DU VIEUX PORT, 13002 MARSEILLE, +33 618592467",
    "BENJAMIN LEDUC, 10 RUE DES ERABLES, 88100 SAINT-DIE-DES-VOSGES, +33 685194302",
    "SALOME PICARD, 35 RUE DU COMMERCE, 50100 CHERBOURG-EN-COTENTIN, +33 693578901",

    "MATHILDE GARNIER, 3 RUE DES TULIPES, 67000 STRASBOURG, +33 612340981",
    "GABRIEL LEROY, 44 RUE DES HALLES, 21000 DIJON, +33 698771205",
    "ELIOTT FERNANDES, 8 RUE DES MARAICHERS, 33000 BORDEAUX, +33 701223456",
    "LOUANE MASSON, 17 RUE DES CAPUCINS, 69007 LYON, +33 745110982",
    "NOAH ROUSSEL, 2 RUE DE LA MAIRIE, 59000 LILLE, +33 677120945",
    "JADE GUILLAUME, 19 RUE DE BRETAGNE, 44000 NANTES, +33 621904558",
    "RAPHAEL BARBIER, 6 RUE DES PECHERS, 34000 MONTPELLIER, +33 736540219",
    "LINA BONNET, 12 RUE DES ROSES, 13008 MARSEILLE, +33 689450112",
    "MAEL DUPONT, 25 AVENUE DE LA MER, 17000 LA ROCHELLE, +33 655902341",
    "INES LAMBERT, 7 RUE DES OLIVETTES, 35000 RENNES, +33 678332019",
    "SACHA FONTAINE, 1 RUE DES GLYCINES, 06000 NICE, +33 614290773",
    "ELENA CHEVALIER, 22 RUE DU THEATRE, 80000 AMIENS, +33 632901744",
    "NATHAN ARNAUD, 9 RUE DES FONTAINES, 67000 STRASBOURG, +33 696774312",
    "MILA DUMAS, 14 RUE DES VIOLETTES, 86000 POITIERS, +33 741552890",
    "ADAM RIVIERE, 30 RUE DU PALAIS, 45000 ORLEANS, +33 679108552",
    "LOLA FLEURY, 5 RUE DES JONQUILLES, 31000 TOULOUSE, +33 612889743",
    "YASSINE CARON, 18 RUE DES ORMES, 14000 CAEN, +33 731004892",
    "NINA PASCAL, 27 RUE SAINT-DENIS, 75002 PARIS, +33 658773410",
    "TIAGO COLLET, 11 BOULEVARD DU RHONE, 69003 LYON, +33 676553908",
    "EMILIE PELLETIER, 4 RUE DES CERISIERS, 49000 ANGERS, +33 623770115",
    "ISMAEL GUERIN, 29 RUE DU DOCTEUR ROUX, 38100 GRENOBLE, +33 614001992",
    "LUCIE HENAULT, 16 RUE DES LAVANDES, 06000 NICE, +33 677890114",
    "AYOUB GIRAUD, 7 RUE DU BASTION, 83000 TOULON, +33 695331204",
    "MARGAUX MACE, 33 RUE DES ARTS, 59000 LILLE, +33 633402119",
    "TOM CLERC, 2 RUE DES CHARMES, 35200 RENNES, +33 701882340",
    "HANNAH THOMAS, 15 AVENUE DES ALPES, 74000 ANNECY, +33 611934820",
    "KILLIAN ROLLAND, 8 RUE DES BAINS, 64100 BAYONNE, +33 647220981",
    "LILOU HOFFMANN, 24 RUE DES FONDEURS, 67000 STRASBOURG, +33 672112305",
    "YANIS LEMAIRE, 10 RUE DES COQUELICOTS, 51100 REIMS, +33 657809321",
    "CELIA BOURGEOIS, 39 RUE DU VIGNOBLE, 21000 DIJON, +33 612540980",
    "ILYES RENAULT, 1 RUE DES ARENES, 30000 NIMES, +33 684990112",
    "LOUISON MARTINEZ, 12 RUE DES PERVENCHES, 34070 MONTPELLIER, +33 732221004",
    "RAYANE HUMBERT, 28 RUE DES GRANGES, 25000 BESANCON, +33 669821770",
    "ALMA CHAPUIS, 6 RUE DE LA PAIX, 76000 ROUEN, +33 612009887",
    "JONAS PIERRE, 19 RUE DU PARC, 54000 NANCY, +33 698320410",
    "MELISSA LECLERCQ, 7 RUE DES FORGES, 59000 LILLE, +33 645900332",
    "ELIOT NEVEU, 31 RUE DU CANAL, 59000 LILLE, +33 701223778",
    "SANDRA AUBERT, 10 RUE DES CHATAIGNIERS, 33000 BORDEAUX, +33 620110982",
    "VALENTIN CHAUVEAU, 14 RUE DES DUNES, 44200 NANTES, +33 679203114",
    "INES PONCE, 5 RUE SAINT-JACQUES, 49000 ANGERS, +33 633114992",
    "MAELINE ROCHER, 22 RUE DES ROQUETTES, 75011 PARIS, +33 614559221",
    "KARIM PERRIER, 9 AVENUE DE LEUROPE, 13010 MARSEILLE, +33 698114556",
    "ALIX BENOIT, 2 RUE DES OISEAUX, 64000 PAU, +33 675889003",
    "SOHAN CHABERT, 17 RUE DES PLATANES, 69005 LYON, +33 632775420",
    "NORA DUPUIS, 8 RUE DE LA POSTE, 37000 TOURS, +33 614882031",
    "LISA MOREL, 23 RUE DES MINIMES, 31000 TOULOUSE, +33 681003244",
    "MAYRON KERJEAN, 11 RUE DES GOELANDS, 29200 BREST, +33 677450902",
    "INES LACROIX, 6 RUE DES VERRIERS, 59000 LILLE, +33 612775001",
    "AARON POULET, 30 RUE DES MYRTILLES, 18000 BOURGES, +33 745660128",
    "ROSE COLAS, 4 RUE DU CLOCHER, 57000 METZ, +33 690022114",

    "ADRIANA SALINAS, 13 RUE DES JARDINIERS, 06000 NICE, +33 612700318",
    "BASILE FAVRE, 9 RUE DES AMANDIERS, 84000 AVIGNON, +33 676230119",
    "CORALIE PERRON, 21 RUE DU CHEMIN VERT, 59000 LILLE, +33 689001552",
    "DORIAN DELMAS, 5 RUE DES GRAINS, 11100 NARBONNE, +33 632114905",
    "ELINA VASSEUR, 28 RUE DES HIRONDELLES, 80000 AMIENS, +33 694330118",
    "FELIX BOUVIER, 3 RUE DES BOULEAUX, 21000 DIJON, +33 701990443",
    "GISELE BARRE, 17 RUE DU GENERAL DE GAULLE, 66000 PERPIGNAN, +33 612045990",
    "HASSAN RENAUDIN, 41 AVENUE DE LA GARE, 06000 NICE, +33 655114020",
    "ISABELLE GRIMAUD, 6 RUE DES PRIMEVERES, 37000 TOURS, +33 672900144",
    "JEREMY DESCHAMPS, 12 RUE DES BLES, 44000 NANTES, +33 678501299",
    "KIM NGUYEN, 7 RUE DES ARTISANS, 69008 LYON, +33 614870032",
    "LORIS BERNET, 19 RUE DES PRES, 38000 GRENOBLE, +33 695002110",
    "MELINA DOS SANTOS, 4 RUE DES BOSQUETS, 67000 STRASBOURG, +33 633900771",
    "NILS PARENT, 26 RUE DES TISSERANDS, 44000 NANTES, +33 689444102",
    "OLIVIA SALVADOR, 2 RUE DES VIGNERONS, 34000 MONTPELLIER, +33 614320889",
    "PIERRE-LOUIS MEUNIER, 9 RUE DU LAVOIR, 72000 LE MANS, +33 671554210",
    "QUITterie BLIN, 33 RUE DES HORTENSIAS, 29200 BREST, +33 631908774",
    "RANIA FARES, 18 RUE DES TILLEULS, 54000 NANCY, +33 676883901",
    "SAMIR HADDAD, 25 RUE DES QUAIS, 76000 ROUEN, +33 699102304",
    "TANIA LE TEXIER, 14 RUE DES MOISSONS, 35000 RENNES, +33 612870455",
    "UGO DUMONT, 1 RUE DU MARCHE, 59000 LILLE, +33 637220144",
    "VALERIE PRUVOST, 11 RUE DES ALOUETTES, 80000 AMIENS, +33 678004909",
    "WALID BENSAID, 5 RUE DES LILAS, 13012 MARSEILLE, +33 614220118",
    "XAVIER BONHOMME, 29 RUE DES DOCKS, 13002 MARSEILLE, +33 693114002",
    "YVONNE DUMAS, 7 RUE DES MARGUERITES, 69006 LYON, +33 612119880",
    "ZAKARIA AIT ALI, 22 RUE DES CAMPANULES, 31000 TOULOUSE, +33 677900410",
    "ALBAN BOISSEAU, 16 RUE DES JASMINS, 34070 MONTPELLIER, +33 695700221",
    "BRUNE GOSSELIN, 3 RUE DU ROCHER, 75008 PARIS, +33 614660800",
    "CLEMENTINE RIOU, 28 RUE DES DAHLIAS, 44700 ORVAULT, +33 632440119",
    "DANY MATHIEU, 10 RUE DES GLACES, 21000 DIJON, +33 677114009",
    "ELVIS RICHOUX, 6 RUE DES PECHEURS, 56100 LORIENT, +33 698220991",
    "FATIMA BELKACEM, 19 RUE DES BLEUETS, 59000 LILLE, +33 614330220",
    "GAETAN GUILLOT, 41 RUE DU CHENE, 49000 ANGERS, +33 672554091",
    "HUGUETTE PAIN, 2 RUE DES VINS, 21000 DIJON, +33 688901220",
    "ILONA COLIN, 8 RUE DES VIGNES, 21000 DIJON, +33 632119044",
    "JAWAD EL AMRANI, 26 RUE DES OLIVIERS, 34000 MONTPELLIER, +33 612900331",
    "KASSANDRA JOLY, 15 RUE DU PONT NEUF, 31000 TOULOUSE, +33 699221008",
    "LUCIE-ANNE SERRA, 4 RUE DES PIERRES, 20000 AJACCIO, +33 676221009",
    "MICKAEL BARRAL, 11 RUE DES MURETS, 69100 VILLEURBANNE, +33 614220901",
    "NOURA BENALI, 21 RUE DES GENETS, 13013 MARSEILLE, +33 679112309",
    "OLGA KOWALSKI, 3 RUE DES SALINES, 17000 LA ROCHELLE, +33 690881004",
    "PHILIPPE BERNARDIN, 6 RUE DES CASTORS, 68000 COLMAR, +33 632770119",
    "QUENTIN PRIOUX, 17 RUE DES CHAMPS, 59000 LILLE, +33 695112449",
    "RITA CARVALHO, 23 RUE DES ECLUSES, 67000 STRASBOURG, +33 614331118",
    "STANISLAS GIRY, 9 RUE DES BASTIDES, 33000 BORDEAUX, +33 672901100",
    "TESS CHOPIN, 28 RUE DES NOISETIERS, 76000 ROUEN, +33 612880771",
    "ULYSSE GODEFROY, 12 RUE DES FONDEURS, 34000 MONTPELLIER, +33 677334990",
    "VIOLAINE THIERRY, 5 RUE DES LUMIERES, 59000 LILLE, +33 689991002",
    "WILLIAM PICAUD, 19 RUE DES TISSUS, 59000 LILLE, +33 614770118",
    "XENIA DUPRE, 2 RUE DE LA HALLE, 86000 POITIERS, +33 632990441",
    "YOHANN BOURDIN, 33 RUE DES VERRIERS, 21000 DIJON, +33 695701119",
    "ZOE-LISE BRIAND, 14 RUE DU BELVEDERE, 35000 RENNES, +33 614003211",

    "ADRIENNE ROLLIN, 7 RUE DES HETRES, 59000 LILLE, +33 676101220",
    "BILEL SAID, 28 RUE DES PLATANES, 38000 GRENOBLE, +33 612550991",
    "CARLA RENAUD, 10 RUE DES PATURES, 45000 ORLEANS, +33 699114550",
    "DIMITRI NICOLAS, 3 RUE DU PORTAIL, 06000 NICE, +33 632771118",
    "ELIANA BERNAS, 16 RUE DES TOURNESOLS, 34000 MONTPELLIER, +33 677009881",
    "FANNY BODIN, 29 RUE DES REMPARTS, 11000 CARCASSONNE, +33 612090331",
    "GUILLAUME PELISSIER, 6 RUE DES BOUCHERS, 67000 STRASBOURG, +33 698880201",
    "HIND EL MANSOURI, 18 RUE DES LILAS, 59000 LILLE, +33 614881002",
    "IMRAN KHAN, 22 RUE DES BLANCS, 75004 PARIS, +33 632110889",
    "JULIETTE BRISSON, 5 RUE DES CHENES, 87000 LIMOGES, +33 677550114",
    "KELLY ROCHE, 11 RUE DES BRUYERES, 18000 BOURGES, +33 695909112",
    "LORENZO COSTA, 2 RUE DES ROMARINS, 06100 NICE, +33 614331908",
    "MAYA GENTY, 27 RUE DES POTIERS, 44000 NANTES, +33 672114909",
    "NATHALIE BOYER, 19 RUE DES ARCADES, 31000 TOULOUSE, +33 689002331",
    "OSCAR GUILBERT, 4 RUE DES PONTS, 33000 BORDEAUX, +33 632900112",
    "PERRINE COUTURIER, 33 RUE DES VERSANTS, 74000 ANNECY, +33 676880144",
    "RACHID BOUAZZA, 8 RUE DES MERISIERS, 69009 LYON, +33 699330114",
    "SALIMA ZERROUK, 14 RUE DES PALMIERS, 13014 MARSEILLE, +33 612770909",
    "TANGUY LE GOFF, 21 RUE DES GOELANDS, 56100 LORIENT, +33 677112908",
    "UGOLIN RIVET, 6 RUE DES ROCHES, 05000 GAP, +33 632441119",
    "VICTORIA SANCHEZ, 12 RUE DES BRASSERIES, 59000 LILLE, +33 695770221",
    "WISSAM NAJJAR, 29 RUE DES TILLEULS, 06000 NICE, +33 614002118",
    "XIMENA FLORES, 3 RUE DES GLYCINES, 66000 PERPIGNAN, +33 677020114",
    "YOUNES EL IDRISSI, 17 RUE DES REMPARTS, 34000 MONTPELLIER, +33 632991118",
    "ZINEDINE AMRANI, 25 RUE DE LA REPUBLIQUE, 59000 LILLE, +33 698110223",
    "ALMAZ SALEM, 8 RUE DES VIOLETTES, 14000 CAEN, +33 614771220",
    "BAPTISTE ROYER, 30 RUE DES CARMES, 86000 POITIERS, +33 677554001",
    "CANDICE LELIEVRE, 9 RUE DU PERRON, 35000 RENNES, +33 699880119",
    "DOROTHEE PERRIN, 11 RUE DES AMBASSADES, 75007 PARIS, +33 612330881",
    "ELIOTT MONTAGNE, 4 RUE DU LAVOIR, 21000 DIJON, +33 672001019",
    "FARID BENYAHIA, 19 RUE DES HORTENSIAS, 69008 LYON, +33 695114220",
    "GAIA MARTEL, 2 RUE DES TAMARIS, 13009 MARSEILLE, +33 614550019",
    "HARMONY PERRIN, 6 RUE DES PEUPLIERS, 72000 LE MANS, +33 677991220",
    "ISSA TRAORE, 14 RUE DES MOISSONS, 59000 LILLE, +33 632887114",
    "JOSEPHINE GILLET, 23 RUE DES BRODERIES, 59000 LILLE, +33 698771001",
    "KARL HENAULT, 10 RUE DES SALINES, 17000 LA ROCHELLE, +33 614009900",
    "LEONIE PAGES, 5 RUE DES CAMELIAS, 33000 BORDEAUX, +33 672880144",
    "MALIK HAMADI, 28 RUE DES GRANDS CHAMPS, 34070 MONTPELLIER, +33 632114112",
    "NOE PICHARD, 7 RUE DES ERABLES, 76000 ROUEN, +33 695770009",
    "OPHELIE PERRON, 19 RUE DES CEDRES, 38100 GRENOBLE, +33 612990771",
    "PRISCILLA GILBERT, 31 RUE DES HALLES, 45000 ORLEANS, +33 677118309",
    "RUBEN MEYER, 2 RUE DES VERRIERS, 67000 STRASBOURG, +33 614220118",
    "SOPHIA ROCHA, 16 RUE DES CHATAIGNIERS, 35000 RENNES, +33 698880771",
    "TAREK BOUKHARI, 11 RUE DES OLIVIERS, 06000 NICE, +33 632441220",
    "UMA RIVIERE, 33 RUE DES LAVANDES, 69003 LYON, +33 695001118",
    "VINCENZO ROMANO, 4 RUE DES FLOTS, 13007 MARSEILLE, +33 614220902",
    "WENDELL BERNARD, 25 RUE DES MOULINS, 31000 TOULOUSE, +33 677009221",
    "XAVIERA HERNANDEZ, 7 RUE DES PINS, 86000 POITIERS, +33 632114990",
    "YANNA KERDRAON, 18 RUE DES GOELANDS, 29200 BREST, +33 695770118",
    "ZACHARIE MATHIEU, 9 RUE DES TILLEULS, 59000 LILLE, +33 614771019",

    "ADELE VALLON, 12 RUE DES CHARMES, 21000 DIJON, +33 698220119",
    "BILAL EL FASSI, 8 RUE DES JONQUILLES, 34000 MONTPELLIER, +33 612004771",
    "CASSANDRE RIBEIRO, 27 RUE DES ROSES, 69007 LYON, +33 677112309",
    "DAMIEN SERRA, 6 RUE DES GENETS, 66000 PERPIGNAN, +33 632770114",
    "ELODIE CARLIER, 19 RUE DES LILAS, 59000 LILLE, +33 695114112",
    "FREDERIC PERRIER, 33 RUE DES ARCADES, 13001 MARSEILLE, +33 614220334",
    "GAYA HAMON, 4 RUE DES AMANDIERS, 35000 RENNES, +33 677889771",
    "HENRIK OLSSON, 16 RUE DES HIRONDELLES, 67000 STRASBOURG, +33 612114220",
    "INESSE BOUKHELIFA, 10 RUE DE LA FONTAINE, 31000 TOULOUSE, +33 698880119",
    "JONATHAN GUYOT, 2 RUE DU MARCHE, 45000 ORLEANS, +33 632114771",
    "KHALIL SAHLI, 23 RUE DES ORMES, 38100 GRENOBLE, +33 695770221",
    "LANA COSTE, 7 RUE DES MIMOSAS, 06000 NICE, +33 614771909",
    "MARTIN PELLETIER, 14 RUE DES PERVENCHES, 74000 ANNECY, +33 677009114",
    "NOLWENN LE ROUX, 28 RUE DES DUNES, 29200 BREST, +33 612330771",
    "OUMAR DIALLO, 11 RUE DES BLEUETS, 69008 LYON, +33 698220902",
    "PAOLO FERRARI, 19 RUE DES ARTISANS, 33000 BORDEAUX, +33 632114880",
    "RANIA EL KHOURY, 33 RUE DES LAVANDES, 13008 MARSEILLE, +33 695770118",
    "SEBASTIEN LORRAIN, 5 RUE DES VIGNERONS, 86000 POITIERS, +33 614771118",
    "TAMARA IVANOV, 2 RUE DES CHATAIGNIERS, 06000 NICE, +33 677112880",
    "UGO-PAUL MARECHAL, 17 RUE DES GLYCINES, 35000 RENNES, +33 612114909",
    "VICTORINE GAUDIN, 6 RUE DES ERABLES, 59000 LILLE, +33 698880771",
    "WALY DIAW, 29 RUE DES ROCHES, 21000 DIJON, +33 632114771",
    "XANDER DUPRE, 8 RUE DES CAMELIAS, 67000 STRASBOURG, +33 695770221",
    "YARA KASSIM, 12 RUE DES TILLEULS, 34070 MONTPELLIER, +33 614771118",
    "ZELIE BOUVIER, 25 RUE DES SOURCES, 13010 MARSEILLE, +33 677112309",

    # 275 -> 300 (25 DERNIERS)
    "ARMAND GILLES, 9 RUE DES NOISETIERS, 75012 PARIS, +33 612770221",
    "BERTILLE GAY, 14 RUE DES LUMIERES, 69002 LYON, +33 695114771",
    "CEDRIC ROUVIERE, 3 RUE DES CERISIERS, 34000 MONTPELLIER, +33 614771220",
    "DALIA BENSALEM, 22 RUE DES PALMIERS, 13015 MARSEILLE, +33 677112114",
    "EDOUARD PERRON, 7 RUE DES HALLES, 44000 NANTES, +33 698880221",
    "FARAH ZITOUNI, 18 RUE DES OLIVIERS, 06000 NICE, +33 632114771",
    "GREGORY LEMAITRE, 25 RUE DES PRES, 59000 LILLE, +33 614771118",
    "HELENA MORETTI, 11 RUE DES AMANDIERS, 30000 NIMES, +33 677112909",
    "ILYAS BOUDJEMA, 4 RUE DU CLOCHER, 67000 STRASBOURG, +33 698880771",
    "JANA KOUAME, 33 RUE DES MARGUERITES, 35000 RENNES, +33 632114220",
    "KARINE LEFEBVRE, 6 RUE DES ROSES, 86000 POITIERS, +33 614771009",
    "LUDOVIC BAILLY, 19 RUE DES CHARMES, 45000 ORLEANS, +33 677112771",
    "MARIAM EL ALAOUI, 2 RUE DES DAHLIAS, 34070 MONTPELLIER, +33 698880119",
    "NABIL BOUAZZA, 28 RUE DES JASMINS, 13009 MARSEILLE, +33 632114771",
    "ODILE PRIOUX, 12 RUE DES ACACIAS, 51100 REIMS, +33 614771118",
    "PABLO MORALES, 5 RUE DES PINS, 29200 BREST, +33 677112309",
    "QUENTINTE NORMAND, 21 RUE DES GENETS, 76000 ROUEN, +33 698880771",
    "RANIAH HADDAD, 10 RUE DES BLEUETS, 69006 LYON, +33 632114220",
    "SIMEON KOCH, 30 RUE DES VERRIERS, 67000 STRASBOURG, +33 614771118",
    "TESSA DELCOURT, 8 RUE DES HIRONDELLES, 80000 AMIENS, +33 677112909",
    "UGUETTE BERNARD, 17 RUE DES LAVANDES, 33000 BORDEAUX, +33 698880771",
    "VASSILI PETROV, 4 RUE DES ERABLES, 38100 GRENOBLE, +33 632114220",
    "WISSAL BENALI, 23 RUE DES TILLEULS, 06000 NICE, +33 614771118",
    "XAVIER ROUXEL, 6 RUE DES SOURCES, 14000 CAEN, +33 677112309",
    "YOHANNA LE GUEN, 19 RUE DES DUNES, 17000 LA ROCHELLE, +33 698880771",
]

# Zone 2: clé -> 4 lignes
# ligne4 = "PARTIE48 | PARTIE30"  (PARTIE48 = 5 chiffres)
# La casse est respectée telle quelle (pas de caps auto).
ZONE2_MAP = {
    "207" : ("E.LECLERC", "Place de l'Eglise", "Sully-la-Chapelle", "45450|Sully-la-Chapelle"),
    "222": ("INTERMARCHE SUPER TADEN", "Rue du Bois Didais", "Taden", "22100|Taden"),
    "488": ("INTERMARCHE SUPER BUC", "Av. Morane Saulnier Zi Le Haut", "Buc", "78530|Buc"),
    "555": ("INTERMARCHE SUPER DONZY", "1 Rue Guy de Jean", "Donzy", "58220|Donzy"),
    "45": ("AMAZON SARAN", "Rue du Champ Rouge", "Saran", "45770|Saran"),
    "80": ("AMAZON BOVES", "Avenue du Superbe Orenoque", "Boves", "80440|Boves"),
    "59": ("AMAZON LAUWIN-PLANQUE", "Rue Amazon", "Lauwine-Planque", "59553|Lauwine-Planque"),
    "71": ("AMAZON SEVREY", "Rue Amazon", "Sevrey", "71100|Sevrey"),
    "26": ("AMAZON MONTELIMAR", "Rue Joseph Garde", "Montelimar", "26200|Montelimar"),
    "91": ("AMAZON BRETIGNY", "Avenue du Centre d'Essais", "Bretigny-sur-Orge", "91220|Bretigny-sur-Orge"),
    "60": ("AMAZON SENLIS", "Avenue Alain Boucher", "Senlis", "60452|Senlis"),
    "57": ("AMAZON AUGNY", "Rue de la Croix de Lorraine", "Augny", "57685|Augny"),
    "45": ("XPO LOGISTICS ARTENAY", "Chemin de Poupry", "Artenay", "45410|Artenay"),
    "77": ("XPO LOGISTICS MOISSY-CRAMAYEL", "Rue Denis Papin", "Moissy-Cramayel", "77550|Moissy-Cramayel"),

    "38": ("GEODIS SATOLAS", "Rue du Brisson", "Satolas-et-Bonce", "38290|Satolas-et-Bonce"),
    "77": ("KUEHNE & NAGEL CHATRES", "Avenue Louis Renault", "Chatres", "77610|Chatres"),
    "94": ("LIDL RUNGIS", "Rue de Villeneuve", "Rungis", "94150|Rungis"),
    "83": ("LIDL LES ARCS", "Route de Draguignan", "Les Arcs", "83460|Les Arcs"),
    "80": ("AUCHAN LOGISTIQUE DURY", "Route d'Amiens", "Dury", "80480|Dury"),
    "91": ("CARREFOUR LOGISTIQUE MASSY", "Rue des Industries", "Massy", "91300|Massy"),
    "94": ("CARREFOUR LOGISTIQUE BONNEUIL", "Avenue de Champagne", "Bonneuil-sur-Marne", "94380|Bonneuil-sur-Marne"),
    "77": ("INTERMARCHE LOGISTIQUE JOSSIGNY", "Rue des 40 Arpents", "Jossigny", "77600|Jossigny"),
    "26": ("INTERMARCHE LOGISTIQUE DONZERE", "Avenue Jean Moulin", "Donzere", "26290|Donzere"),
    "91": ("DECATHLON LOGISTIQUE BRETIGNY", "Rue des Saugées", "Bretigny-sur-Orge", "91220|Bretigny-sur-Orge"),

    "57": ("FM LOGISTIC PHALSBOURG", "Rue de l'Europe", "Phalsbourg", "57370|Phalsbourg"),
    "13": ("ID LOGISTICS ORGON", "Avenue Logistique", "Orgon", "13660|Orgon"),
    "13": ("STEF MIRAMAS", "Avenue de la Grande Halle", "Miramas", "13140|Miramas"),
    "91": ("AMAZON LISSES", "Route de Corbeil", "Lisses", "91090|Lisses"),
    "95": ("AMAZON GARAGE LES GONESSE", "Avenue de Morillons", "Gonesse", "95500|Gonesse"),
    "62": ("GEODIS CALAIS", "Rue Marcel Doret", "Calais", "62100|Calais"),
    "92": ("XPO LOGISTICS CLICHY", "Rue du Commerce", "Clichy", "92110|Clichy"),
    "59": ("AUCHAN LOGISTIQUE NORD", "Rue des Entrepos", "Lille", "59000|Lille"),
    "51": ("LIDL ENTREPOT REIMS", "Rue des Industries", "Reims", "51100|Reims"),
    "67": ("LIDL ENTREPOT STRASBOURG", "Rue du Logistique", "Strasbourg", "67100|Strasbourg"),

    "71": ("CARREFOUR LOGISTIQUE SEVREY", "Avenue des Transformateurs", "Sevrey", "71100|Sevrey"),
    "33": ("AMAZON CESTAS CANNEJAN", "Chemin du Pot au Pin", "Cestas Cannejan", "33610|Cestas Cannejan"),
    "78": ("AMAZON MANTES", "Rue du Commerce", "Mantes-la-Jolie", "78200|Mantes-la-Jolie"),
    "79": ("INTERMARCHE LOGISTIQUE CHATILLON-SUR-THOUET", "Rue de Parthenay", "Chatillon-sur-Thouet", "79200|Chatillon-sur-Thouet"),
    "56": ("LIDL ENTREPOT PLOERMEL", "Rue du Port", "Ploermel", "56800|Ploermel"),
    "91": ("AMAZON BRETIGNY 2", "Rue des Entreprises", "Bretigny-sur-Orge", "91220|Bretigny-sur-Orge"),
    "93": ("XPO LOGISTICS PARIS", "Avenue de l'Europe", "Villepinte", "93420|Villepinte"),
    "69": ("GEODIS LOGISTIQUE LYON", "Rue du Transport", "Saint-Priest", "69800|Saint-Priest"),
    "91": ("AMAZON BRETIGNY 3", "Rue de la Logistique", "Bretigny-sur-Orge", "91220|Bretigny-sur-Orge"),
    "59": ("DECATHLON LOGISTIQUE VILLENEUVE", "Avenue des Entrepos", "Villeneuve-d'Ascq", "59491|Villeneuve-d'Ascq"),
}
DEFAULT_ZONE2_KEY = next(iter(ZONE2_MAP), "")


def _as_is(s: str) -> str:
    return (s or "")


# =========================
# DB (points + redeems + zone1 last)
# =========================
_db_lock = threading.Lock()


def db_connect():
    return sqlite3.connect(DB_PATH)


def db_init():
    with _db_lock:
        con = db_connect()
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                points INTEGER NOT NULL DEFAULT 0,
                created_at TEXT NOT NULL
            )
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS redeems (
                code TEXT PRIMARY KEY,
                redeemed_by INTEGER,
                redeemed_at TEXT NOT NULL
            )
        """)
        # Anti "même ZONE1 deux fois de suite" (persistant)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS zone1_last (
                user_id INTEGER PRIMARY KEY,
                last_idx INTEGER
            )
        """)
        con.commit()
        con.close()


def ensure_user(user_id: int):
    with _db_lock:
        con = db_connect()
        cur = con.cursor()
        cur.execute("SELECT user_id FROM users WHERE user_id = ?", (user_id,))
        row = cur.fetchone()
        if not row:
            cur.execute(
                "INSERT INTO users(user_id, points, created_at) VALUES (?, 0, ?)",
                (user_id, datetime.now().isoformat(timespec="seconds"))
            )
        con.commit()
        con.close()


def get_points(user_id: int) -> int:
    with _db_lock:
        con = db_connect()
        cur = con.cursor()
        cur.execute("SELECT points FROM users WHERE user_id = ?", (user_id,))
        row = cur.fetchone()
        con.close()
    return int(row[0]) if row else 0


def add_points(user_id: int, delta: int):
    ensure_user(user_id)
    with _db_lock:
        con = db_connect()
        cur = con.cursor()
        cur.execute("UPDATE users SET points = points + ? WHERE user_id = ?", (delta, user_id))
        con.commit()
        con.close()


def deduct_points_if_possible(user_id: int, cost: int) -> bool:
    ensure_user(user_id)
    with _db_lock:
        con = db_connect()
        cur = con.cursor()
        cur.execute("SELECT points FROM users WHERE user_id = ?", (user_id,))
        row = cur.fetchone()
        if not row:
            con.close()
            return False
        points = int(row[0])
        if points < cost:
            con.close()
            return False
        cur.execute("UPDATE users SET points = points - ? WHERE user_id = ?", (cost, user_id))
        con.commit()
        con.close()
        return True


def redeem_code(user_id: int, code: str) -> Tuple[bool, str]:
    ensure_user(user_id)
    code = code.strip().upper()
    if code not in REDEEM_CODES:
        return False, "❌ Code invalide."

    with _db_lock:
        con = db_connect()
        cur = con.cursor()
        cur.execute("SELECT code FROM redeems WHERE code = ?", (code,))
        if cur.fetchone():
            con.close()
            return False, "⚠️ Ce code a déjà été utilisé."

        pts = int(REDEEM_CODES[code])
        cur.execute(
            "INSERT INTO redeems(code, redeemed_by, redeemed_at) VALUES (?, ?, ?)",
            (code, user_id, datetime.now().isoformat(timespec="seconds"))
        )
        cur.execute("UPDATE users SET points = points + ? WHERE user_id = ?", (pts, user_id))
        con.commit()
        con.close()

    return True, f"✅ Recharge OK : +{pts} points.\n📌 Nouveau solde : {get_points(user_id)} points."


def get_zone1_last_idx(user_id: int) -> Optional[int]:
    with _db_lock:
        con = db_connect()
        cur = con.cursor()
        cur.execute("SELECT last_idx FROM zone1_last WHERE user_id = ?", (user_id,))
        row = cur.fetchone()
        con.close()
    if not row or row[0] is None:
        return None
    return int(row[0])


def set_zone1_last_idx(user_id: int, idx: int) -> None:
    with _db_lock:
        con = db_connect()
        cur = con.cursor()
        cur.execute(
            "INSERT INTO zone1_last(user_id, last_idx) VALUES(?, ?) "
            "ON CONFLICT(user_id) DO UPDATE SET last_idx=excluded.last_idx",
            (user_id, int(idx)),
        )
        con.commit()
        con.close()


def pick_zone1_text_for_user(user_id: int) -> Tuple[str, str, str, str]:
    """
    Règle SIMPLE: un utilisateur ne reçoit jamais la même combinaison ZONE1 deux fois de suite.
    """
    if not ZONE1_LIST:
        return ("", "", "", "")

    last_idx = get_zone1_last_idx(user_id)
    n = len(ZONE1_LIST)

    if n == 1:
        idx = 0
    else:
        candidates = list(range(n))
        if last_idx is not None and 0 <= last_idx < n and last_idx in candidates:
            candidates.remove(last_idx)
        idx = RNG.choice(candidates)

    set_zone1_last_idx(user_id, idx)

    raw = ZONE1_LIST[idx]
    parts = [p.strip() for p in raw.split(",")]
    while len(parts) < 4:
        parts.append("")
    parts = parts[:4]
    return parts[0], parts[1], parts[2], parts[3]


# =========================
# ZONE2 pick + PARTIE48 extraction
# =========================
def pick_zone2_text_by_key(key: str) -> Tuple[str, str, str, str]:
    if not ZONE2_MAP:
        return ("", "", "", "")

    k = (key or "").strip()
    if not k:
        k = DEFAULT_ZONE2_KEY

    return ZONE2_MAP.get(k, ZONE2_MAP.get(DEFAULT_ZONE2_KEY, ("", "", "", "")))


def get_zone2_part48_from_key(zone2_key: str) -> str:
    """
    Extrait PARTIE48 depuis ZONE2_MAP[key][3] (avant le '|').
    Format accepté: "12345|xxx" ou "12345 | xxx" ou "12345"
    """
    _, _, _, line4 = pick_zone2_text_by_key(zone2_key)
    raw = (line4 or "").strip()
    if "|" in raw:
        part48, _ = raw.split("|", 1)
        return part48.strip().replace(" ", "")
    return raw.strip().replace(" ", "")


# =========================
# FONT (Arial Regular + Bold)
# =========================
def get_arial_regular_path():
    base = Path(__file__).resolve().parent
    candidates = [
        base / "fonts" / "arial.ttf",
        Path(r"C:\Windows\Fonts\arial.ttf"),
    ]
    return next((p for p in candidates if p.exists()), None)


def get_arial_bold_path():
    base = Path(__file__).resolve().parent
    candidates = [
        base / "fonts" / "arialbd.ttf",
        Path(r"C:\Windows\Fonts\arialbd.ttf"),
    ]
    return next((p for p in candidates if p.exists()), None)


ARIAL_REG_PATH = get_arial_regular_path()
ARIAL_BOLD_PATH = get_arial_bold_path()


def load_regular(size: int) -> ImageFont.FreeTypeFont:
    if not ARIAL_REG_PATH:
        raise FileNotFoundError(
            "Arial Regular introuvable: ajoutez fonts/arial.ttf ou vérifiez C:\\Windows\\Fonts\\arial.ttf"
        )
    return ImageFont.truetype(str(ARIAL_REG_PATH), size=size)


def load_bold(size: int) -> ImageFont.FreeTypeFont:
    if not ARIAL_BOLD_PATH:
        raise FileNotFoundError(
            "Arial Bold introuvable: ajoutez fonts/arialbd.ttf ou vérifiez C:\\Windows\\Fonts\\arialbd.ttf"
        )
    return ImageFont.truetype(str(ARIAL_BOLD_PATH), size=size)


# =========================
# COHERENT TEXT GENERATION
# =========================
def today_ddmmyyyy() -> str:
    return datetime.now().strftime("%d/%m/%Y")


def rdigits(n: int) -> str:
    return "".join(RNG.choice(string.digits) for _ in range(n))


def ralnum(n: int) -> str:
    alphabet = string.ascii_uppercase + string.digits
    return "".join(RNG.choice(alphabet) for _ in range(n))


def gen_top_code() -> str:
    seg1 = ralnum(7)
    seg2 = ralnum(7)
    seg3 = RNG.choice(string.digits) + RNG.choice(string.ascii_uppercase)
    return f"{seg1}-{seg2}-{seg3}"


def gen_base_8R_line():
    A = rdigits(5)
    B = rdigits(5)
    C = rdigits(1)
    return f"8R {A} {B} {C}", A, B, C


def gen_number_N() -> str:
    return rdigits(6)


def build_8R7_line(N: str, C: str, P_override_5digits: str) -> str:
    P = (P_override_5digits or "").strip()
    if not P:
        P = rdigits(5)
    Q = rdigits(3) + C
    S = "0000" + rdigits(1) + C
    return f"8R7 {P} {N} {Q} {S}"


def build_bottom_line(A: str, B: str, C: str) -> str:
    g1 = f"8R{A[:3]}"
    g2 = f"{A[3:]}{B[:2]}"
    g3 = f"{B[2:]}{C}"
    T = rdigits(4)
    return f"0034 477 {g1} {g2} {g3} {T} 508V"


def generate_text_payload(P_override_5digits: str) -> dict:
    line1, A, B, C = gen_base_8R_line()
    N = gen_number_N()
    return {
        "top_code": gen_top_code(),
        "right_bold_number": N,
        "right_date": today_ddmmyyyy(),
        "mid_left_line": line1,
        "mid_center_line": build_8R7_line(N, C, P_override_5digits),
        "bottom_center_line": build_bottom_line(A, B, C),
    }


# =========================
# TEXT FIELDS (existing)
# =========================
TEXT_FIELDS_REF = [
    {"id": "top_code",           "pt": (200, 249),  "size": 27, "anchor": "lt"},
    {"id": "right_bold_number",  "pt": (1023, 523), "size": 27, "anchor": "rt"},
    {"id": "right_date",         "pt": (935, 587),  "size": 29, "anchor": "rt"},
    {"id": "mid_left_line",      "pt": (321, 647),  "size": 25, "anchor": "lt"},
    {"id": "mid_center_line",    "pt": (611, 1319), "size": 29, "anchor": "mt"},
    {"id": "bottom_center_line", "pt": (593, 1697), "size": 29, "anchor": "mt"},
]


def compute_anchored_pos(draw: ImageDraw.ImageDraw, x: int, y: int, text: str, font, anchor="lt"):
    left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
    tw = right - left

    if anchor == "lt":
        tx = x
        ty = y
    elif anchor == "rt":
        tx = x - tw
        ty = y
    elif anchor == "mt":
        tx = x - (tw / 2)
        ty = y
    else:
        tx = x
        ty = y

    tx -= left
    ty -= top
    return tx, ty


def draw_text_with_weight(draw: ImageDraw.ImageDraw, tx: float, ty: float, text: str, font, fill):
    if BOLD_MODE == "none":
        draw.text((tx, ty), text, font=font, fill=fill)
        return
    if BOLD_MODE == "stroke1":
        draw.text((tx, ty), text, font=font, fill=fill, stroke_width=1, stroke_fill=fill)
        return

    # BOLD_MODE == "light" (centré)
    draw.text((tx - 0.5, ty), text, font=font, fill=fill)
    draw.text((tx + 0.5, ty), text, font=font, fill=fill)


def render_texts(base: Image.Image, texts: dict) -> None:
    W, H = base.size
    draw = ImageDraw.Draw(base)

    for f in TEXT_FIELDS_REF:
        fid = f["id"]
        val = texts.get(fid, "")
        if not val:
            continue

        x, y = scale_point(f["pt"], W, H)
        font = load_regular(f["size"])
        tx, ty = compute_anchored_pos(draw, x, y, str(val), font, anchor=f["anchor"])
        draw_text_with_weight(draw, tx, ty, str(val), font, fill=(0, 0, 0))


# =========================
# ZONES RENDER
# =========================
def _draw_ink_top_left(draw: ImageDraw.ImageDraw, x: int, y: int, text: str, font: ImageFont.FreeTypeFont) -> None:
    # Aligne l'encre sur x,y (même marge visuelle)
    left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
    tx = x - left
    ty = y - top
    draw_text_with_weight(draw, tx, ty, text, font, fill=(0, 0, 0))


def _paste_with_anchor(base: Image.Image, layer: Image.Image, x: int, y: int, anchor: str) -> None:
    lw, lh = layer.size
    if anchor == "rt":
        px = int(x - lw)
        py = int(y)
    elif anchor == "mt":
        px = int(x - lw / 2)
        py = int(y)
    else:
        px = int(x)
        py = int(y)
    base.paste(layer, (px, py), layer)


def draw_rotated_text_true_bold(
    base: Image.Image,
    x: int,
    y: int,
    text: str,
    size: int,
    angle_deg: int,
    anchor: str = "lt",
) -> None:
    text = (text or "").strip()
    if not text:
        return

    font = load_bold(size)

    tmp = Image.new("RGBA", (1, 1), (0, 0, 0, 0))
    dtmp = ImageDraw.Draw(tmp)
    left, top, right, bottom = dtmp.textbbox((0, 0), text, font=font)
    tw = max(1, right - left)
    th = max(1, bottom - top)

    layer = Image.new("RGBA", (tw, th), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.text((-left, -top), text, font=font, fill=(0, 0, 0, 255))

    rot = layer.rotate(angle_deg, expand=True, resample=Image.Resampling.BICUBIC)
    _paste_with_anchor(base, rot, x, y, anchor=anchor)


def draw_zone1(base: Image.Image, user_id: int) -> None:
    """
    ZONE1 = EXACTEMENT la même logique que ZONE2:
    - interligne fixe (asc+desc+gap)
    - rendu ink-top-left stable
    - texte respecté tel que tu l'écris
    - aléatoire mais jamais la même combinaison deux fois de suite par user
    """
    W, H = base.size
    sx, sy = scale_point(ZONE1_START_REF, W, H)

    font26 = load_regular(26)
    gap_px = scale_y(ZONE1_GAP_REF, H)

    asc, desc = font26.getmetrics()
    step = int((asc + desc) + gap_px)

    a, btxt, c, d = pick_zone1_text_for_user(user_id)
    lines = [_as_is(a), _as_is(btxt), _as_is(c)]

    draw = ImageDraw.Draw(base)
    for i, txt in enumerate(lines):
        _draw_ink_top_left(draw, sx, sy + i * step, txt, font26)

    # 4e champ vertical
    if d:
        x4, y4 = scale_point(ZONE1_LINE4_POS_REF, W, H)
        draw_rotated_text_true_bold(
            base=base,
            x=x4,
            y=y4,
            text=_as_is(d),
            size=ZONE1_LINE4_SIZE,
            angle_deg=ZONE1_LINE4_ROTATE_DEG,
            anchor=ZONE1_LINE4_ANCHOR,
        )


def draw_zone2_line4_mixed(base: Image.Image, x: int, y_top: int, raw_line4: str) -> None:
    """
    Ligne 4: PARTIE48 (font 48) puis PARTIE30 (font 30), sur la même ligne.
    La casse est respectée telle quelle.
    """
    draw = ImageDraw.Draw(base)
    font48 = load_regular(48)
    font30 = load_regular(30)

    raw = (raw_line4 or "")
    part_big, part_small = raw, ""
    if "|" in raw:
        part_big, part_small = raw.split("|", 1)
        part_big = part_big.rstrip()
        part_small = part_small.lstrip()

    big_txt = _as_is(part_big)
    small_txt = _as_is(part_small)

    left_b, top_b, right_b, bottom_b = draw.textbbox((0, 0), big_txt, font=font48)
    x_big_draw = x - left_b
    y_big_draw = y_top - top_b
    draw_text_with_weight(draw, x_big_draw, y_big_draw, big_txt, font48, fill=(0, 0, 0))

    big_w = right_b - left_b

    asc48, _ = font48.getmetrics()
    asc30, _ = font30.getmetrics()
    baseline = y_big_draw + asc48

    spaces = " " * int(ZONE2_LINE4_SPACES)
    left_sp, top_sp, right_sp, bottom_sp = draw.textbbox((0, 0), spaces, font=font30)
    spaces_w = right_sp - left_sp

    if not small_txt.strip():
        return

    x_small_ink = x + big_w + spaces_w
    left_s, top_s, right_s, bottom_s = draw.textbbox((0, 0), small_txt, font=font30)
    x_small_draw = x_small_ink - left_s
    y_small_draw = (baseline - asc30) - top_s
    draw_text_with_weight(draw, x_small_draw, y_small_draw, small_txt, font30, fill=(0, 0, 0))


def draw_zone2(base: Image.Image, zone2_key: str) -> None:
    W, H = base.size
    sx, sy = scale_point(ZONE2_START_REF, W, H)

    font30 = load_regular(30)
    gap_px = scale_y(ZONE2_GAP_REF, H)

    asc, desc = font30.getmetrics()
    step30 = int((asc + desc) + gap_px)

    z2a, z2b, z2c, z2d = pick_zone2_text_by_key(zone2_key)
    draw = ImageDraw.Draw(base)

    _draw_ink_top_left(draw, sx, sy + 0 * step30, _as_is(z2a), font30)
    _draw_ink_top_left(draw, sx, sy + 1 * step30, _as_is(z2b), font30)
    _draw_ink_top_left(draw, sx, sy + 2 * step30, _as_is(z2c), font30)

    y_adj = scale_y(ZONE2_LINE4_Y_ADJUST_REF, H)
    y_line4 = sy + (3 + ZONE2_LINE4_EXTRA_LINES) * step30 + y_adj
    draw_zone2_line4_mixed(base, sx, y_line4, _as_is(z2d))


def render_zone_texts(base: Image.Image, zone2_key: str, user_id: int) -> None:
    draw_zone1(base, user_id=user_id)
    draw_zone2(base, zone2_key)


# =========================
# BARCODE RENDER
# =========================
def generate_code128_image(text: str) -> Image.Image:
    b = Code128(text, writer=ImageWriter())
    buf = BytesIO()
    b.write(buf, options={"write_text": False, "quiet_zone": 0, "module_height": 60})
    buf.seek(0)
    return Image.open(buf).convert("RGB")


def paste_barcode_cover(base: Image.Image, code_text: str, x: int, y: int, w: int, h: int) -> None:
    draw = ImageDraw.Draw(base)
    draw.rectangle([x, y, x + w, y + h], fill=(255, 255, 255))

    barcode = generate_code128_image(code_text)
    bw, bh = barcode.size

    scale = max(w / bw, h / bh)
    nw = max(1, int(bw * scale))
    nh = max(1, int(bh * scale))
    barcode = barcode.resize((nw, nh), Image.Resampling.LANCZOS)

    left = (nw - w) // 2
    top = (nh - h) // 2
    barcode = barcode.crop((left, top, left + w, top + h))

    base.paste(barcode, (x, y))


# =========================
# FINAL RENDER
# =========================
def render_result(code1: str, code2: str, code3: str, user_id: int, zone2_key: str = "") -> BytesIO:
    base = Image.open(TEMPLATE_PATH).convert("RGB")
    W, H = base.size

    x2, y2, w2, h2 = scale_box(BOX2_REF, W, H)
    x3, y3, w3, h3 = scale_box(BOX3_REF, W, H)

    paste_barcode_cover(base, code1, BOX1_X, BOX1_Y, BOX1_W, BOX1_H)
    paste_barcode_cover(base, code2, x2, y2, w2, h2)
    paste_barcode_cover(base, code3, x3, y3, w3, h3)

    # PARTIE48 (5 chiffres) remplace P dans "8R7 P N Q S"
    part48_5 = get_zone2_part48_from_key(zone2_key)
    texts = generate_text_payload(P_override_5digits=part48_5)

    render_texts(base, texts)
    render_zone_texts(base, zone2_key=zone2_key, user_id=user_id)

    out = BytesIO()
    out.name = "result.jpg"
    base.save(out, format="JPEG", quality=95)
    out.seek(0)
    return out


# =========================
# DECODE IMAGE
# =========================
def decode_3_barcodes_from_image(img: Image.Image) -> Optional[Tuple[str, str, str]]:
    img = ImageOps.exif_transpose(img)

    rgb = img.convert("RGB")
    gray = rgb.convert("L")

    decoded = zbar_decode(gray)
    if not decoded:
        decoded = zbar_decode(rgb)
    if not decoded:
        return None

    items = []
    for d in decoded:
        try:
            txt = d.data.decode("utf-8").strip()
        except Exception:
            continue
        if not txt:
            continue

        try:
            top = d.rect.top
        except Exception:
            top = 0

        items.append((top, txt))

    items.sort(key=lambda t: t[0])

    seen = set()
    ordered = []
    for _, txt in items:
        if txt not in seen:
            seen.add(txt)
            ordered.append(txt)

    if len(ordered) < 3:
        return None

    return ordered[0], ordered[1], ordered[2]


# =========================
# RATE LIMIT
# =========================
_last_request_at = {}


def is_admin(user_id: int) -> bool:
    return user_id in ADMIN_USER_IDS


def check_rate_limit(user_id: int) -> bool:
    if is_admin(user_id):
        return True
    now = datetime.now()
    prev = _last_request_at.get(user_id)
    if prev and (now - prev) < timedelta(seconds=RATE_LIMIT_SECONDS):
        return False
    _last_request_at[user_id] = now
    return True


# =========================
# CAPTION HELPERS
# =========================
def format_success_caption(cost: int, balance: int, admin_free: bool) -> str:
    custom = (CUSTOM_MESSAGE or "").strip()
    custom = f"📝 {custom}\n\n" if custom else ""

    if admin_free:
        debit_line = "👑 Admin : aucun débit\n"
    else:
        debit_line = f"💳 Débit : -{cost} points\n"

    return SUCCESS_CAPTION_TEMPLATE.format(
        custom=custom,
        debit_line=debit_line,
        balance=balance,
    )


def format_insufficient(balance: int, cost: int) -> str:
    return INSUFFICIENT_FUNDS_TEMPLATE.format(balance=balance, cost=cost)


# =========================
# COMMANDS
# =========================
async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP_TEXT)


async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP_TEXT)


async def cmd_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    u = update.effective_user
    c = update.effective_chat
    if not u or not c:
        return
    await update.message.reply_text(
        f"👤 user_id: {u.id}\n"
        f"💬 chat_id: {c.id}\n"
        f"🏷️ username: @{u.username if u.username else '(none)'}"
    )


async def cmd_balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    u = update.effective_user
    if not u:
        return
    ensure_user(u.id)
    pts = get_points(u.id)
    await update.message.reply_text(
        f"💰 Solde : {pts} points\n"
        f"🧾 Coût par image : {COST_PER_IMAGE} points\n"
        f"👑 Admin: {'oui' if is_admin(u.id) else 'non'}"
    )


async def cmd_redeem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    u = update.effective_user
    if not u:
        return
    ensure_user(u.id)

    if not context.args:
        await update.message.reply_text("Usage: /redeem CODE")
        return

    code = " ".join(context.args).strip()
    ok, reply = redeem_code(u.id, code)
    await update.message.reply_text(reply)


async def cmd_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    u = update.effective_user
    if not u:
        return
    if not is_admin(u.id):
        await update.message.reply_text("⛔ Accès admin refusé.")
        return

    if len(context.args) < 3:
        await update.message.reply_text("Usage: /admin add <user_id> <points> | /admin set <user_id> <points>")
        return

    action = context.args[0].lower()
    try:
        target_id = int(context.args[1])
        amount = int(context.args[2])
    except Exception:
        await update.message.reply_text("❌ Paramètres invalides.")
        return

    ensure_user(target_id)

    if action == "add":
        add_points(target_id, amount)
        await update.message.reply_text(f"✅ OK : +{amount} points à {target_id}.\nSolde : {get_points(target_id)}")
        return

    if action == "set":
        current = get_points(target_id)
        delta = amount - current
        add_points(target_id, delta)
        await update.message.reply_text(f"✅ OK : solde de {target_id} = {get_points(target_id)} points.")
        return

    await update.message.reply_text("❌ Action inconnue (add/set).")


# =========================
# GENERATION TEXT HANDLER
# =========================
def parse_generation_message(msg: str) -> Tuple[Optional[List[str]], str]:
    """
    Supporte:
      - CODE1:CODE2:CODE3
      - CODE1:CODE2:CODE3:KEY
      - compat: CODE1:CODE2:CODE3|KEY
    Retourne: (codes[3], zone2_key)
    """
    payload = (msg or "").strip()
    zone2_key = ""

    if "|" in payload:
        left, right = payload.split("|", 1)
        payload = left.strip()
        zone2_key = right.strip()

    parts = [p.strip() for p in payload.split(":") if p.strip()]

    if len(parts) == 3:
        return parts, zone2_key

    if len(parts) == 4:
        return parts[:3], parts[3]

    return None, zone2_key


async def handle_generation_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (update.message.text or "").strip()
    if not msg:
        return

    u = update.effective_user
    if not u:
        return

    ensure_user(u.id)

    if not check_rate_limit(u.id):
        await update.message.reply_text(RATE_LIMIT_MESSAGE)
        return

    parts, zone2_key = parse_generation_message(msg)
    if not parts:
        await update.message.reply_text("📌 Format attendu : CODE1:CODE2:CODE3:45\nTapez /help si besoin.")
        return

    admin_free = is_admin(u.id)

    if not admin_free:
        if not deduct_points_if_possible(u.id, COST_PER_IMAGE):
            pts = get_points(u.id)
            await update.message.reply_text(format_insufficient(pts, COST_PER_IMAGE))
            return

    code1, code2, code3 = parts

    try:
        out = render_result(code1, code2, code3, user_id=u.id, zone2_key=zone2_key)
    except Exception as e:
        if not admin_free:
            add_points(u.id, COST_PER_IMAGE)
        await update.message.reply_text(
            f"⚠️ Erreur technique ({'remboursé' if not admin_free else 'admin'}).\nDétail : {e}"
        )
        return

    remaining = get_points(u.id)
    caption = format_success_caption(COST_PER_IMAGE, remaining, admin_free=admin_free)
    await update.message.reply_photo(photo=out, caption=caption)


# =========================
# IMAGE HANDLER
# =========================
async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    u = update.effective_user
    if not u:
        return

    ensure_user(u.id)

    if not check_rate_limit(u.id):
        await update.message.reply_text(RATE_LIMIT_MESSAGE)
        return

    admin_free = is_admin(u.id)

    if not admin_free:
        if not deduct_points_if_possible(u.id, COST_PER_IMAGE):
            pts = get_points(u.id)
            await update.message.reply_text(format_insufficient(pts, COST_PER_IMAGE))
            return

    # Caption = clé zone2 (ex: "45")
    zone2_key = ""
    cap = (update.message.caption or "").strip()
    if cap:
        zone2_key = cap

    tg_file = None
    if update.message.photo:
        tg_file = await update.message.photo[-1].get_file()
    elif update.message.document and (update.message.document.mime_type or "").startswith("image/"):
        tg_file = await update.message.document.get_file()
    else:
        if not admin_free:
            add_points(u.id, COST_PER_IMAGE)
        await update.message.reply_text("📷 Envoyez une image (photo ou document) contenant 3 codes-barres.")
        return

    bio = BytesIO()
    await tg_file.download_to_memory(out=bio)
    bio.seek(0)

    try:
        img = Image.open(bio)
    except Exception:
        if not admin_free:
            add_points(u.id, COST_PER_IMAGE)
        await update.message.reply_text("❌ Impossible d’ouvrir l’image envoyée (remboursé).")
        return

    decoded = decode_3_barcodes_from_image(img)
    if not decoded:
        if not admin_free:
            add_points(u.id, COST_PER_IMAGE)
        await update.message.reply_text("❌ Lecture des 3 codes-barres impossible (remboursé).")
        return

    code1, code2, code3 = decoded

    try:
        out = render_result(code1, code2, code3, user_id=u.id, zone2_key=zone2_key)
    except Exception as e:
        if not admin_free:
            add_points(u.id, COST_PER_IMAGE)
        await update.message.reply_text(f"⚠️ Erreur technique (remboursé).\nDétail : {e}")
        return

    remaining = get_points(u.id)
    caption = format_success_caption(COST_PER_IMAGE, remaining, admin_free=admin_free)
    await update.message.reply_photo(photo=out, caption=caption)


# =========================
# MAIN
# =========================
def main():
    if not TOKEN:
        raise RuntimeError(
            "BOT_TOKEN est vide. Définissez la variable d’environnement BOT_TOKEN.\n"
            "PowerShell:\n"
            "  $env:BOT_TOKEN='XXXX'\n"
            "  py .\\bot.py\n"
            "CMD:\n"
            "  set BOT_TOKEN=XXXX\n"
            "  py bot.py"
        )

    db_init()

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("help", cmd_help))
    app.add_handler(CommandHandler("id", cmd_id))
    app.add_handler(CommandHandler("balance", cmd_balance))
    app.add_handler(CommandHandler("redeem", cmd_redeem))
    app.add_handler(CommandHandler("admin", cmd_admin))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_generation_text))
    app.add_handler(MessageHandler(filters.PHOTO | filters.Document.IMAGE, handle_image))

    app.run_polling()


if __name__ == "__main__":
    main()
