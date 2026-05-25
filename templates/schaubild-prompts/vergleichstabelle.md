# Diagramm-Typ: Vergleichstabelle

Zwei- oder Drei-Spalten-Tabelle mit Attribut-Spalte links und Vergleichs-Spalten rechts.

## Wann nutzen

- "Was ist der Unterschied zwischen X und Y?"
- "Wann nutzt du X, wann Y?"
- Abgrenzungs-Diagramme

## Variablen

- **Headline**: z.B. "X vs. Y"
- **Spalten-Header**: Namen der verglichenen Konzepte
- **Zeilen**: drei bis fünf, jede mit Attribut-Label und je einem Zell-Label pro Spalte. Pro Zelle maximal vier Wörter, sonst geht Lesbarkeit am Daumennagel verloren.

## Visueller Rahmen

Headline oben zentriert, bold. Darunter eine Tabelle mit dünnen dunkelgrauen Border-Linien. Spalten-Header-Zellen in Primärblau (#1E3A8A) mit weißem Bold-Text. Body-Zellen alternieren zwischen Hellblau (#DBEAFE) und Weiß mit dunklem Text. Attribut-Spalte links in dezentem Grau-Ton.

Jede Zelle enthält nur ein kurzes Label. Keine Sub-Texte, keine Erklärungssätze.

Style-Suffix aus `templates/style-suffix-wissenschaft.md` immer unten anhängen.

## Beispiel-Inhalt

| Attribut | Chatbot | KI-Agent |
|---|---|---|
| Steuerung | Mensch tippt | Entscheidet selbst |
| Werkzeuge | keine | Browser, Code, Datenbank |
| Ablauf | Frage, Antwort | Schleife |
| Ziel | wartet | verfolgt Ziel |

## Provider

Siehe `docs/schaubild-prompting.md`. Default: Gemini.
