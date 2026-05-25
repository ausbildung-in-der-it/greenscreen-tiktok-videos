# Diagramm-Typ: Hub-Spoke

Ein zentraler Container mit Sub-Komponenten innen, optional externe Boxen außen mit Pfeilen.

## Wann nutzen

- "Was sind die Bausteine von X?"
- "Wie ist X aufgebaut?"
- Architektur-Diagramme

## Variablen, die du beim Prompt-Schreiben brauchst

- **Headline**: Bold-Titel oben
- **Container-Label**: zentraler Block mit dem Oberbegriff
- **Innere Boxen**: drei bis fünf Sub-Komponenten als kurze Labels. Mehr als fünf wird auf 1:1 schnell unlesbar.
- **Externe Box** (optional): eine Box außerhalb des Containers
- **Pfeil-Beschriftungen** (optional): Eingang, Ausgang

## Visueller Rahmen

Zentraler großer Rounded-Rectangle, gefüllt mit Primärblau (#1E3A8A), Headline-Label in weißer Bold-Schrift oben. Innerhalb des Containers liegen die Sub-Komponenten gleich groß nebeneinander oder im Grid, mit hellblauem Fill (#DBEAFE) und dunklem Text. Bei externer Box: hellgraue Box außerhalb, mit dünnen dunkelgrauen Pfeilen verbunden.

Style-Suffix aus `templates/style-suffix-wissenschaft.md` immer unten anhängen.

## Beispiel-Inhalt

- Headline: "Komponenten eines KI-Agenten"
- Container-Label: "KI-Agent"
- Innere Boxen: Sprachmodell, Harness, Werkzeuge
- Externe Box: "Umgebung"
- Pfeile: "Eingaben" rein, "Aktionen" raus

## Provider

Siehe `docs/schaubild-prompting.md`. Default: Gemini.
