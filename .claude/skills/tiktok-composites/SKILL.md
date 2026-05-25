---
description: Konvertiert die 1:1-Schaubilder eines Videos in 1080x1920 TikTok-Composites mit Padding und Greenscreen-Raum unten.
when_to_use: Triggert bei "tiktok composite", "9:16 vorbereiten", "tiktok bilder".
argument-hint: [video-ordner]
disable-model-invocation: true
allowed-tools: Bash
---

# TikTok-Composites generieren

Video-Ordner: $ARGUMENTS (z.B. `videos/01-was-ist-ein-ki-agent`). Bei leerem Argument: nachfragen.

Padding-Werte und Greenscreen-Höhe stehen als Konstanten am Anfang von `scripts/make-tiktok-composites.py`. Bei abweichendem Wunsch dort anpassen, nicht hier.

## 1. Voraussetzungen prüfen

- `videos/NN-thema/schaubilder/` existiert und enthält mindestens ein `.jpeg`, `.jpg` oder `.png`
- PIL/Pillow ist installiert: `python3 -c "from PIL import Image"`

## 2. Skript ausführen

```bash
python3 scripts/make-tiktok-composites.py videos/NN-thema/
```

## 3. Output verifizieren

```bash
ls -lh videos/NN-thema/tiktok-1080x1920/
open videos/NN-thema/tiktok-1080x1920/
```

## 4. Greenscreen-Raum kontrollieren

Das Skript loggt pro Bild den freien Raum unten. Unterschreitet er die im Skript dokumentierte Mindest-Höhe, das Padding im Skript reduzieren oder das Schaubild kleiner skalieren.
