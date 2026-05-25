# Schaubild-Prompting

Wie du saubere wissenschaftliche Schaubilder mit Bildgenerierung erzeugst, ohne KI-Slop-Optik.

## Grundregeln

1. **Echte Umlaute** im Prompt verwenden. Direkt `ä ö ü ß` tippen, nicht "ae oe ue ss".
2. **Sonderzeichen-Constraint** anhängen: `render German umlauts correctly: ä, ö, ü, ß. Do not transliterate.`
3. **Keine Sub-Texte** in Boxen. Pro Box nur ein kurzes Haupt-Label.
4. **Heller Hintergrund** (#FFFFFF), nicht dunkel-neon.
5. **Disziplinierte Farbpalette**: dunkelblau #1E3A8A, hellblau #DBEAFE, dunkelgrau #1F2937. Drei Farben reichen.
6. **Sans-serif bold** (Inter, Helvetica, Arial). Keine Script- oder Serif-Schriften.
7. **Flat fills**, keine Gradients, kein Glow, kein Drop-Shadow.

## Style-Block

Liegt in `templates/style-suffix-wissenschaft.md`. An jeden Bild-Prompt unten anhängen.

## Provider-Wahl

| Anforderung | Provider | Begründung |
|---|---|---|
| Schaubild mit wenig Text | Gemini | Günstiger, ruhigere Farbwirkung |
| Schaubild mit vielen Labels (Tabelle, Diagramm) | OpenAI gpt-image-2 high | Bessere Text-Treue, sauberere Kanten |
| Img2img-Korrektur | Gemini | OpenAI gpt-image-2 hat kein Img2img |
| Illustrative Szenen | Gemini | Ausreichend, OpenAI ist teurer |

## Befehl

```bash
tools image generate "$(cat ./prompts/A.txt)" \
  --provider=gemini \
  --aspect-ratio=1:1 \
  --image-size=2K \
  -o ./schaubilder/A-roh.png
```

Die CLI legt den Output in einem **Unterordner** ab, mit timestamped Dateinamen. Danach flach kopieren:

```bash
src=$(find ./schaubilder/A-roh.png -name 'image-*' -type f | head -1)
cp "$src" ./schaubilder/A.${src##*.}
```

## Img2img-Korrektur

Wenn der Output Umlaute oder Sub-Texte falsch hat:

```bash
tools image generate "fix German typography: change 'Gedaechtnis' to 'Gedächtnis', \
keep all other elements identical, do not change layout, colors, or arrows" \
  --provider=gemini \
  --aspect-ratio=1:1 \
  --image-size=2K \
  --input1=./schaubilder/A.jpeg \
  -o ./schaubilder/A-fix.png
```

## Vier Diagramm-Typen, die ich bereits getestet habe

| Typ | Template | Beste Provider-Wahl |
|---|---|---|
| Hub-Spoke (Komponenten) | `templates/schaubild-prompts/hub-spoke.md` | Gemini |
| Vergleichstabelle | `templates/schaubild-prompts/vergleichstabelle.md` | OpenAI gpt-image-2 high |
| Kreislauf | `templates/schaubild-prompts/kreislauf.md` | Gemini |
| 3-Schritt-Prozess | `templates/schaubild-prompts/prozess-3-schritt.md` | Gemini |

## Was nicht geht (gelernt aus Versuchen)

- **Excalidraw-Preset**: zu sketchy für seriöse Zielgruppe (Unternehmer)
- **Dunkler Hintergrund mit Neon**: wirkt nach AI-Slop, nicht professionell
- **Komplexe Sub-Texte unter Box-Labels**: werden bei Mobile-Größe unlesbar und Modelle rendern sie unzuverlässig
- **Englische Headlines wie "NICHT DASSELBE"**: zu Clickbait, passt nicht zum wissenschaftlichen Stil
- **Programmatische Generierung mit Satori (getestet)**: lohnt sich erst, wenn man dieselben Templates dutzendfach mit variierenden Inhalten braucht. Für 4 bis 6 Schaubilder pro Video ist KI-Generierung schneller.

## Selbst-Check vor Verwendung

1. Alle Umlaute korrekt? (Strg+F nach "ae" "oe" "ue" "ss" im erwarteten Wort)
2. Keine ungewollten Sub-Texte unter Box-Labels?
3. Farbpalette diszipliniert (max. 3 bis 4 Farben)?
4. Bei 200x350 px Daumennagel-Größe noch lesbar?
5. Kontrast Text/Hintergrund ausreichend (WCAG ≥4.5:1)?
