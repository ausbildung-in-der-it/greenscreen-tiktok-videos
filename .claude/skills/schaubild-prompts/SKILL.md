---
name: schaubild-prompts
description: Generiert einen Schaubild-Prompt aus einem der 4 Diagramm-Typ-Templates (Hub-Spoke, Vergleichstabelle, Kreislauf, 3-Schritt-Prozess) und führt durch die Bildgenerierung. Triggert bei "schaubild erstellen", "diagramm prompt", "schaubild generieren".
---

# Schaubild-Prompt erstellen und Bild generieren

Du hilfst dem User, ein Schaubild für ein TikTok-Video zu bauen.

## Schritte

### 1. Diagramm-Typ wählen

Frag den User (oder erkenne aus dem Kontext), welcher Typ passt:

| Typ | Template | Beste für |
|---|---|---|
| Hub-Spoke | `templates/schaubild-prompts/hub-spoke.md` | "Was sind die Bausteine von X?" |
| Vergleichstabelle | `templates/schaubild-prompts/vergleichstabelle.md` | "Was ist der Unterschied zwischen X und Y?" |
| Kreislauf | `templates/schaubild-prompts/kreislauf.md` | "Wie funktioniert X als Prozess?" |
| 3-Schritt-Prozess | `templates/schaubild-prompts/prozess-3-schritt.md` | "Beispiel: so läuft das ab" |

### 2. Variablen sammeln

Lies das passende Template. Frag den User die Variablen ab (z.B. HEADLINE, INNER_BOXES, etc.).

### 3. Prompt zusammenbauen

Füll die Variablen ein. Hänge den Style-Block aus `templates/style-suffix-wissenschaft.md` unten an.

### 4. Provider wählen

Default: Gemini. Bei Vergleichstabelle oder vielen Labels: OpenAI gpt-image-2 high.

Begründung kurz dem User mitteilen.

### 5. Generieren

```bash
tools image generate "$(cat ./videos/NN/prompts/X.txt)" \
  --provider=<gemini|openai> \
  --aspect-ratio=1:1 \
  --image-size=2K \
  --quality=high \
  -o ./videos/NN/schaubilder/X-roh.png
```

### 6. Flach kopieren

Die CLI legt den Output in einem Unterordner ab. Hol das echte File raus:

```bash
src=$(find ./videos/NN/schaubilder/X-roh.png -name 'image-*' -type f | head -1)
cp "$src" ./videos/NN/schaubilder/X.${src##*.}
```

### 7. Visuelle Prüfung

Öffne das Bild im Finder. Prüfe:

- Sind alle Umlaute korrekt?
- Keine Sub-Texte unter Box-Labels?
- Farbpalette diszipliniert?
- Bei Daumennagel-Größe noch lesbar?

### 8. Bei Fehlern: Img2img-Korrektur

```bash
tools image generate "fix German typography: change Xae to Xä, keep all other elements identical" \
  --provider=gemini \
  --aspect-ratio=1:1 \
  --image-size=2K \
  --input1=./videos/NN/schaubilder/X.jpeg \
  -o ./videos/NN/schaubilder/X-fix.png
```

## Wichtig

- Stil-Regeln aus `docs/stil-regeln.md` befolgen
- Prompt-Datei im Video-Ordner unter `prompts/` speichern, nicht nur ad-hoc generieren
- Bei jedem Fehlversuch: Variante mit Suffix speichern, damit Lerneffekt erhalten bleibt
