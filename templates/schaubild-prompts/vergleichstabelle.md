# Schaubild-Prompt: Vergleichstabelle

Zwei-Spalten-Tabelle mit Attribut-Spalte links, zwei Vergleichs-Spalten rechts.

## Wann nutzen

- "Was ist der Unterschied zwischen X und Y?"
- "Wann nutzt du X, wann Y?"
- Abgrenzungs-Diagramme

## Variablen

- `HEADLINE`: z.B. "X vs. Y"
- `LEFT_HEADER`, `RIGHT_HEADER`: Spalten-Überschriften
- `ROWS`: 3 bis 5 Zeilen, jede mit `attr`, `left`, `right` (jeweils kurz, max. 4 Wörter)

## Prompt-Template

```
Two-column comparison table in German for a clean infographic.

Top center headline in bold mixed case: "{{HEADLINE}}"

Below the headline, a clean two-column table with thin dark gray borders. The
leftmost column contains attribute labels in regular gray text. Two main columns
to its right have dark blue (#1E3A8A) header cells with white bold text. Body
cells alternate between light blue (#DBEAFE) and white fills with dark text.
Every cell contains only a short label, NO sub-text, NO explanations.

Column headers:
- (leftmost): empty
- middle: "{{LEFT_HEADER}}"
- right: "{{RIGHT_HEADER}}"

Rows below the header row, with attribute label on far left and one short label per cell:

Row 1 attribute label "{{ATTR_1}}":
- middle cell: "{{LEFT_1}}"
- right cell: "{{RIGHT_1}}"

Row 2 attribute label "{{ATTR_2}}":
- middle cell: "{{LEFT_2}}"
- right cell: "{{RIGHT_2}}"

[weitere Zeilen analog]

[STYLE-SUFFIX VON style-suffix-wissenschaft.md HIER ANHÄNGEN]
```

## Beispiel-Inhalt

| Attribut | Chatbot | KI-Agent |
|---|---|---|
| Steuerung | Mensch tippt | Entscheidet selbst |
| Werkzeuge | keine | Browser, Code, Datenbank |
| Ablauf | Frage → Antwort | Schleife |
| Ziel | wartet | verfolgt Ziel |

## Tipp

Bei Tabellen ist Text-Treue wichtig. **OpenAI mit hoher Qualitätsstufe** liefert hier oft sauberer als Gemini.
