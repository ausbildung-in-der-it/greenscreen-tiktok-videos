# Style-Suffix: Wissenschaftliches Schaubild

Dieser Block wird an jeden Schaubild-Prompt **unten angehängt**, damit der Output wie ein Lehrbuch- oder draw.io-Diagramm aussieht, nicht wie KI-Slop.

## Verwendung

```bash
cat templates/style-suffix-wissenschaft.md  # die Block-Region kopieren
# oder direkt im Prompt einfügen
```

## Style-Block

```
Render as a clean technical infographic in the style of a scientific paper or
textbook diagram (like draw.io, Lucidchart, IEEE figures):
- White background (#FFFFFF)
- Crisp geometric shapes only: rectangles with rounded corners (4 to 6 pixel radius)
- Solid flat fills, NO gradients, NO glow, NO neon, NO drop shadows, NO blur
- Color palette: dark blue (#1E3A8A) primary with white text, light blue (#DBEAFE)
  secondary with dark text, light gray (#E5E7EB) tertiary, dark gray (#1F2937) text
- Thin dark gray connecting lines (1.5 to 2 pixel) with simple triangular arrowheads
- Sans-serif typography only (Inter / Helvetica / Arial), bold for headings
- Each box contains ONLY a short main label, absolutely NO sub-text, NO descriptive sub-lines
- Generous white space, perfectly grid-aligned, symmetric composition
- Render German umlauts correctly: ä, ö, ü, ß. Do not transliterate to ae, oe, ue, ss.
- Mobile-readable: every label large enough at thumbnail size
- NO hand-drawn or sketch aesthetic, NO whiteboard, NO 3D, NO illustrations of robots
  or characters, NO photorealistic elements
- Aesthetic: looks like a figure from a computer science textbook or a Notion/Linear product diagram
```

## Warum jeder Punkt

| Regel | Grund |
|---|---|
| Weißer Hintergrund | Dunkel-neon wirkt KI-typisch und unprofessionell |
| Flat Fills | Gradients und Glow sind KI-Slop-Marker |
| Drei Farben | Disziplin schafft seriösen Eindruck, mehr Farben wirken billig |
| Sans-serif bold | Lesbar bei Mobile-Daumennagel-Größe |
| Keine Sub-Texte | Modelle rendern sie unzuverlässig, machen Mobile unlesbar |
| Echte Umlaute | Transliterationen sind sofort sichtbar als Fehler |
| Keine Roboter-Illustrationen | Wirken kindlich, passen nicht zu Unternehmer-Zielgruppe |
