# Schaubild-Prompting

Wie du saubere wissenschaftliche Schaubilder erzeugst, ohne KI-Slop-Optik. Diese Datei besitzt: Bildregeln, Provider, Label-Präzision, Diagramm-Typen-Liste. Sie besitzt nicht: CLI-Befehle (siehe `.claude/skills/schaubild-prompts/SKILL.md`), Schaubild-Sequenz pro Video (siehe `docs/storytelling.md`).

## Grundregeln

1. Echte Umlaute im Prompt verwenden. Direkt ä ö ü ß tippen, keine Transliteration.
2. Sonderzeichen-Constraint anhängen, falls Modell sonst transliteriert.
3. Keine Sub-Texte in Boxen. Pro Box nur ein kurzes Haupt-Label. Erklärung kommt ins gesprochene Wort.
4. Heller Hintergrund (#FFFFFF), nicht dunkel-neon.
5. Disziplinierte Farbpalette: dunkelblau #1E3A8A, hellblau #DBEAFE, dunkelgrau #1F2937. Drei Farben reichen.
6. Sans-serif bold (Inter, Helvetica, Arial). Keine Script- oder Serif-Schriften.
7. Flat fills, keine Gradients, kein Glow, kein Drop-Shadow.

## Style-Block

Liegt in `templates/style-suffix-wissenschaft.md`. An jeden Bild-Prompt unten anhängen.

## Provider

Immer Gemini. Schneller als OpenAI (rund 5 bis 10 Sekunden statt 30), rendert deutsche Umlaute und Tabellen-Layouts zuverlässig, ausreichend gute Qualität. Img2img-Korrekturen funktionieren nur mit Gemini.

OpenAI nur als Fallback in einem Spezialfall. Bedingung: Gemini zeigt bei einem konkreten Schaubild nach zwei Iterationen dieselbe spezifische Schwäche (z.B. extrem text-heavy Vergleichstabelle mit über 20 Zellen, bei der Gemini wiederholt Labels vertauscht).

## Label-Präzision: keine zu breiten Begriffe

Wenn du Berufen, Konzepten oder Tools je ein Verb oder Stichwort zuordnest, prüfe vorher: ist das zugeordnete Stichwort wirklich das ganze Label, oder steckt da ein Sammelbegriff drin?

Beispiel: Der Fachinformatiker hat vier Fachrichtungen. "Programmieren" trifft nur eine davon. Wer "Fachinformatiker = programmieren" suggeriert, lügt didaktisch.

Drei Lösungen, wenn das Label zu breit ist:

1. **Splitten**: zeige die dominanten Sub-Typen separat.
2. **Breiter umformulieren**: aus "programmieren" wird "Software und Systeme".
3. **Mündlich auflösen**: im Skript explizit benennen, dass das Label ein Sammelbegriff ist. Schwächste der drei Lösungen, weil das Schaubild ohne Sprechtext irreführend bleibt.

Faustregel: bei jeder Vergleichs-Visualisierung in jede Box schauen und fragen, ob das wirklich ein Begriff auf gleicher Ebene wie die anderen Boxen ist. Falls nein: splitten oder umformulieren, bevor du generierst.

## Diagramm-Typen

Templates unter `templates/schaubild-prompts/`:

| Template | Beste für |
|---|---|
| `hub-spoke.md` | "Was sind die Bausteine von X?" |
| `vergleichstabelle.md` | "Was ist der Unterschied zwischen X und Y?" |
| `kreislauf.md` | "Wie funktioniert X als Schleife?" |
| `prozess-3-schritt.md` | "So läuft das in mehreren Schritten ab" |

Custom-Layouts (2x2-Matrix, Decision-Tree, Zeitstrahl, Hook-Bild mit Statistik, Outro-Bild) schreibst du freihändig. Style-Block anhängen, sonst gilt das gleiche Vorgehen.

## Bekannte Anti-Muster

- **Excalidraw-Preset**: zu sketchy für seriöse Zielgruppe.
- **Dunkler Hintergrund mit Neon**: wirkt nach AI-Slop.
- **Komplexe Sub-Texte unter Box-Labels**: werden bei Mobile-Größe unlesbar und Modelle rendern sie unzuverlässig.
- **Englische Clickbait-Headlines** wie "NICHT DASSELBE": passt nicht zum wissenschaftlichen Stil.
- **Programmatische Generierung mit Satori**: lohnt sich erst, wenn dieselben Templates dutzendfach mit variierenden Inhalten gebraucht werden. Für 4 bis 6 Schaubilder pro Video ist KI-Generierung schneller.

## Selbst-Check vor Verwendung

1. Alle Umlaute korrekt? (Strg+F nach "ae" "oe" "ue" "ss" im erwarteten Wort)
2. Keine ungewollten Sub-Texte unter Box-Labels?
3. Farbpalette diszipliniert (max. 3 bis 4 Farben)?
4. Bei 200x350 px Daumennagel-Größe noch lesbar?
5. Kontrast Text gegen Hintergrund ausreichend (WCAG mindestens 4.5:1)?
