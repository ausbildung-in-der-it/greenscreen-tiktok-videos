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

## Provider

**Immer Gemini.** Schneller als OpenAI (5 bis 10 Sekunden statt 30 Sekunden bei `quality=high`), rendert deutsche Umlaute und Tabellen-Layouts zuverlässig, ausreichend gute Qualität bei wissenschaftlicher Diagramm-Optik. Img2img-Korrekturen funktionieren nur mit Gemini.

OpenAI nur als **Fallback** in einem Spezialfall: wenn Gemini bei einem konkreten Schaubild nach zwei Iterationen die gleiche spezifische Schwäche zeigt (z.B. extrem text-heavy Vergleichstabelle mit mehr als 20 Zellen, bei der Gemini wiederholt Labels vertauscht). Standardmäßig nicht nötig.

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

## Vier getestete Diagramm-Typen

| Typ | Template |
|---|---|
| Hub-Spoke (Komponenten) | `templates/schaubild-prompts/hub-spoke.md` |
| Vergleichstabelle | `templates/schaubild-prompts/vergleichstabelle.md` |
| Kreislauf | `templates/schaubild-prompts/kreislauf.md` |
| 3-Schritt-Prozess | `templates/schaubild-prompts/prozess-3-schritt.md` |

Custom-Layouts (z.B. 2x2-Matrix, Decision-Tree, Zeitstrahl, Hook-Bild mit Statistik): Prompt freihändig schreiben, Style-Block aus `templates/style-suffix-wissenschaft.md` unten anhängen.

## Label-Präzision: keine zu breiten Begriffe

Wenn du in einer Vergleichs-Visualisierung (Matrix, Decision-Tree, Vergleichstabelle) Berufen, Konzepten oder Tools je ein Verb oder Stichwort zuordnest, prüfe vorher: ist das zugeordnete Stichwort wirklich das ganze Label, oder steckt da ein Sammelbegriff drin?

Beispiel aus Video 02: Der Fachinformatiker hat vier Fachrichtungen (Anwendungsentwicklung, Systemintegration, Daten- und Prozessanalyse, Digitale Vernetzung). "Programmieren" trifft nur eine davon. Wer "Fachinformatiker = programmieren" suggeriert, lügt didaktisch.

Drei Lösungen, wenn das Label zu breit ist:

1. **Splitten**: zeige die zwei oder drei dominanten Sub-Typen separat, statt den Sammelbegriff. In der 2x2-Matrix von Video 02 wurde der Fachinformatiker-Quadrant in zwei Sub-Boxen geteilt: Anwendungsentwicklung und Systemintegration.
2. **Breiter umformulieren**: statt eines konkreten Verbs ein generischeres Label nehmen, das mehrere Sub-Typen einschließt. Aus "programmieren" wird "Software und Systeme".
3. **Mündlich auflösen**: im Skript explizit benennen, dass das Label ein Sammelbegriff ist und das gezeigte Verb nur einen Sub-Typ trifft. Bevorzugt die schwächste der drei Lösungen, weil der Zuschauer das Schaubild ohne den Sprechtext nicht versteht.

Faustregel: bei jeder Vergleichs-Visualisierung einmal in jede Box schauen und fragen "ist das wirklich ein Begriff auf gleicher Ebene wie die anderen Boxen?" Wenn nein, splitten oder umformulieren, bevor du generierst.

## Schaubild-Sequenz pro Video

Anzahl und Funktion der Schaubilder pro Video richtet sich nach dem Storytelling-Bogen (`docs/storytelling.md`), mindestens drei pro Video. Typische Sektionstypen und passende Diagramm-Typen:

| Sektionstyp | Typischer Diagramm-Typ |
|---|---|
| Hook | Custom-Bild mit der Schlüssel-Statistik oder dem Kontrast des Videos |
| Abgrenzung / Verwirrung erklären | Vergleichstabelle oder Genealogie-Bild |
| Hauptdefinition | Hub-Spoke, Matrix, Kreislauf |
| Mechanismus / Detail | Kreislauf oder Zoom-in auf das Hauptbild |
| Beispiel / Praxis-Anker | 3-Schritt-Prozess oder Beispiel-Custom |
| Entscheidungsregel | Decision-Tree oder Hauptbild mit Hervorhebung |
| CTA / Outro | Schlichtes Custom-Bild mit der Schlussfrage |

Wiederverwendung erlaubt: Hauptbild über zwei Sektionen sichtbar lassen, wenn die zweite Sektion eine Vertiefung der ersten ist.

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
