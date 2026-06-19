# Tor Expert Bundle — installation manuelle

Ce dossier doit contenir le binaire `tor.exe` et ses DLLs pour que le module
`src-tauri/src/tor.rs` puisse le lancer comme sidecar.

## Où télécharger

Site officiel Tor Project (jamais ailleurs) :
**https://www.torproject.org/download/tor/**

Choisir : **Windows Expert Bundle x86_64** (ou ARM64 si Windows ARM).

Exemple de nom de fichier au moment de l'écriture :
`tor-expert-bundle-windows-x86_64-14.5.x.tar.gz`

## Installation

1. Décompresser l'archive téléchargée.
2. Copier le contenu du sous-dossier `tor/` (et **pas** `data/`) dans ce dossier
   (`src-tauri/resources/tor/`).
3. Le dossier final doit contenir au minimum :
   - `tor.exe`
   - `libcrypto-*.dll`
   - `libssl-*.dll`
   - `libevent-*.dll`
   - `zlib1.dll`
   - autres DLLs livrées par le bundle

## Vérification

Depuis ce dossier, lancer :

```powershell
.\tor.exe --version
```

Doit afficher quelque chose comme `Tor version 0.4.x.x`.

## Vérification de l'intégrité (recommandé)

Tor publie des signatures GPG des releases. Vérifier la signature
`.tar.gz.asc` avec la clé GPG des développeurs Tor avant d'extraire si tu veux
être paranoïaque (recommandé pour cet usage).

Clés des dévs Tor : https://support.torproject.org/tbb/how-to-verify-signature/

## Notes

- Taille approximative du bundle : ~30-50 Mo (impact bundle final de l'app).
- Le binaire est tout ce dont on a besoin : on génère le `torrc` à la volée
  côté Rust dans `tor::write_torrc()` et on le pointe vers un dossier de
  données dans `app_local_data_dir/tor/` (wipe automatiquement par
  `security::wipe_traces`).
- **Ne pas commit** `tor.exe` dans git : la licence Tor est BSD-friendly mais
  la binary va alourdir le repo. Ajouter à `.gitignore` :

  ```
  src-tauri/resources/tor/*.exe
  src-tauri/resources/tor/*.dll
  ```
