---
description: Generiert einen Schaubild-Prompt aus einem der vier Diagramm-Typ-Templates (Hub-Spoke, Vergleichstabelle, Kreislauf, 3-Schritt-Prozess) und führt durch die Bildgenerierung.
when_to_use: Triggert bei "schaubild erstellen", "diagramm prompt", "schaubild generieren".
argument-hint: [diagramm-typ] [video-ordner]
disable-model-invocation: true
allowed-tools: Bash Read Write
---

# Schaubild-Prompt erstellen und Bild generieren

Argumente: $ARGUMENTS (optional Diagramm-Typ und/oder Video-Ordner)

## 1. Diagramm-Typ wählen

| Typ | Template | Beste für |
|---|---|---|
| `hub-spoke` | `templates/schaubild-prompts/hub-spoke.md` | "Was sind die Bausteine von X?" |
| `vergleichstabelle` | `templates/schaubild-prompts/vergleichstabelle.md` | "Was ist der Unterschied zwischen X und Y?" |
| `kreislauf` | `templates/schaubild-prompts/kreislauf.md` | "Wie funktioniert X als Prozess?" |
| `prozess-3-schritt` | `templates/schaubild-prompts/prozess-3-schritt.md` | "Beispiel: so läuft das ab" |

Wenn nicht aus $ARGUMENTS klar: frag nach.

## 2. Variablen sammeln

Lies das passende Template. Frag die Variablen ab.

## 3. Prompt zusammenbauen

Füll die Variablen ein. Hänge den Style-Block aus `templates/style-suffix-wissenschaft.md` unten an. Speichere den fertigen Prompt unter `videos/NN/prompts/<TYP>.txt`.

## 4. Provider wählen

Default: Gemini. Bei Vergleichstabelle oder vielen Labels: OpenAI mit hoher Qualitätsstufe. Begründung kurz dem User mitteilen.

## 5. Generieren

```bash
tools image generate "$(cat ./videos/NN/prompts/X.txt)" \
  --provider=<gemini|openai> \
  --aspect-ratio=1:1 \
  --image-size=2K \
  --quality=high \
  -o ./videos/NN/schaubilder/X-roh.png
```

## 6. Flach kopieren

Die CLI legt den Output in einem Unterordner ab. Extrahiere die echte Datei:

```bash
src=$(find ./videos/NN/schaubilder/X-roh.png -name 'image-*' -type f | head -1)
cp "$src" ./videos/NN/schaubilder/X.${src##*.}
```

## 7. Visuell prüfen

Öffne im Finder. Prüfe Umlaute, keine Sub-Texte, disziplinierte Farben, lesbar bei Daumennagel.

## 8. Bei Fehlern: Img2img-Korrektur

```bash
tools image generate "fix German typography: change Xae to Xä, keep all other elements identical" \
  --provider=gemini \
  --aspect-ratio=1:1 \
  --image-size=2K \
  --input1=./videos/NN/schaubilder/X.jpeg \
  -o ./videos/NN/schaubilder/X-fix.png
```

Befolge `docs/schaubild-prompting.md` und `docs/stil-regeln.md`.
