---
description: Generiert einen Schaubild-Prompt aus einem Diagramm-Typ-Template oder Custom-Layout und führt durch die Bildgenerierung.
when_to_use: Triggert bei "schaubild erstellen", "diagramm prompt", "schaubild generieren".
argument-hint: [diagramm-typ] [video-ordner]
disable-model-invocation: true
allowed-tools: Bash Read Write
---

# Schaubild-Prompt erstellen und Bild generieren

Argumente: $ARGUMENTS (optional Diagramm-Typ und/oder Video-Ordner).

Kanonische Regeln zu Provider, Style-Block, Diagramm-Typen und Schaubild-Sequenz: `docs/schaubild-prompting.md`. Diese Datei beschreibt nur die ausführende Mechanik.

## 1. Diagramm-Typ wählen

Templates unter `templates/schaubild-prompts/`:

- `hub-spoke.md` für "Was sind die Bausteine von X?"
- `vergleichstabelle.md` für "Was ist der Unterschied zwischen X und Y?"
- `kreislauf.md` für "Wie funktioniert X als Prozess?"
- `prozess-3-schritt.md` für "Beispiel: so läuft das ab"

Custom-Layouts (2x2-Matrix, Decision-Tree, Zeitstrahl, Hook-Bild, Outro-Bild) schreibst du freihändig.

Wenn nicht aus $ARGUMENTS klar: frag den User nach dem Typ.

## 2. Prompt schreiben

Lies das passende Template (bei Custom-Layout: schreib direkt). Füll Variablen ein. Hänge den Style-Block aus `templates/style-suffix-wissenschaft.md` unten an. Speichere unter `videos/NN/prompts/<X>.txt`.

## 3. Generieren

```bash
tools image generate "$(cat ./videos/NN/prompts/X.txt)" \
  --provider=gemini \
  --aspect-ratio=1:1 \
  --image-size=2K \
  -o ./videos/NN/schaubilder/X-roh.png
```

## 4. Flach kopieren

Die CLI legt den Output in einem Unterordner ab:

```bash
src=$(find ./videos/NN/schaubilder/X-roh.png -name 'image-*' -type f | head -1)
cp "$src" ./videos/NN/schaubilder/X.${src##*.}
rm -rf ./videos/NN/schaubilder/X-roh.png
```

## 5. Visuell prüfen

Lies die Bilddatei. Prüfe: Umlaute korrekt, kein Sub-Text, Farben diszipliniert, lesbar bei Daumennagel.

## 6. Bei Fehlern: Img2img-Korrektur

```bash
tools image generate "fix German typography: change Xae to Xä, keep all other elements identical, do not change layout, colors, or arrows" \
  --provider=gemini \
  --aspect-ratio=1:1 \
  --image-size=2K \
  --input1=./videos/NN/schaubilder/X.jpeg \
  -o ./videos/NN/schaubilder/X-fix.png
```

Nach zwei gescheiterten Iterationen: dem User zeigen, was vorliegt, und kurz fragen wie weiter (anderer Prompt, Text reduzieren, Layout anpassen).
