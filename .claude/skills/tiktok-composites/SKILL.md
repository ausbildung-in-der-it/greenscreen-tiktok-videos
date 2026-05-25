---
name: tiktok-composites
description: Konvertiert die 1:1-Schaubilder eines Videos in 1080x1920 TikTok-Composites mit Padding und Greenscreen-Raum unten. Triggert bei "tiktok composite", "9:16 vorbereiten", "tiktok bilder".
---

# TikTok-Composites generieren

Du nimmst die 1:1-Schaubilder eines Video-Ordners und erzeugst 1080x1920-Versionen mit Padding.

## Schritte

### 1. Video-Ordner bestimmen

Frag den User, welches Video (z.B. `01-was-ist-ein-ki-agent`), wenn nicht aus Kontext klar.

### 2. Voraussetzungen prüfen

- `videos/NN/schaubilder/` existiert
- enthält mindestens ein .jpeg, .jpg oder .png
- PIL/Pillow ist installiert (`python3 -c "from PIL import Image"`)

### 3. Padding-Werte (optional anpassen)

Defaults im Skript:

- `PAD_TOP = 180`
- `PAD_SIDE = 130`

Wenn der User andere Werte will, im Skript anpassen oder als CLI-Argument übergeben (Feature-Erweiterung).

### 4. Skript ausführen

```bash
python3 scripts/make-tiktok-composites.py videos/NN-thema/
```

### 5. Output verifizieren

Liste die generierten Dateien:

```bash
ls -lh videos/NN-thema/tiktok-1080x1920/
```

Öffne den Ordner im Finder:

```bash
open videos/NN-thema/tiktok-1080x1920/
```

### 6. Greenscreen-Raum kontrollieren

Das Skript loggt pro Bild, wie viele Pixel unten frei bleiben. Default sollte 920px sein (= 48% der Höhe). Wenn weniger als 800px: Padding reduzieren oder Schaubild kleiner skalieren.

## Wichtig

- Padding-Werte im Skript dokumentieren wenn geändert (Kommentar oben)
- Bei mehreren Videos parallel: nicht versehentlich den falschen Ordner targeten
- Output-Format JPG bewusst gewählt: TikTok komprimiert beim Upload sowieso, JPG ist kleiner als PNG
