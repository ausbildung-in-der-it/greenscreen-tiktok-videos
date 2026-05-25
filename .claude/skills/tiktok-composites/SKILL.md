---
description: Konvertiert die 1:1-Schaubilder eines Videos in 1080x1920 TikTok-Composites mit Padding und Greenscreen-Raum unten.
when_to_use: Triggert bei "tiktok composite", "9:16 vorbereiten", "tiktok bilder".
argument-hint: [video-ordner]
disable-model-invocation: true
allowed-tools: Bash
---

# TikTok-Composites generieren

Video-Ordner: $ARGUMENTS (z.B. `videos/01-was-ist-ein-ki-agent`)

Wenn $ARGUMENTS leer ist: frag nach.

## 1. Voraussetzungen prüfen

- `videos/NN/schaubilder/` existiert und enthält mindestens ein `.jpeg`, `.jpg` oder `.png`
- PIL/Pillow ist installiert: `python3 -c "from PIL import Image"`

## 2. Padding-Werte (optional)

Defaults im Skript: `PAD_TOP = 180`, `PAD_SIDE = 130`. Bei abweichendem Wunsch im Skript anpassen.

## 3. Skript ausführen

```bash
python3 scripts/make-tiktok-composites.py videos/NN-thema/
```

## 4. Output verifizieren

```bash
ls -lh videos/NN-thema/tiktok-1080x1920/
open videos/NN-thema/tiktok-1080x1920/
```

## 5. Greenscreen-Raum kontrollieren

Das Skript loggt pro Bild den freien Raum unten. Default 920px (48% der Höhe). Bei weniger als 800px: Padding reduzieren oder Schaubild kleiner skalieren.

Bei Padding-Anpassung den Wert im Skript dokumentieren (Kommentar oben).
