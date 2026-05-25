# Schaubild-Prompt: Hub-Spoke (Komponenten-Diagramm)

Zentraler Container mit Sub-Komponenten innen, optional externe Boxen außen mit Pfeilen.

## Wann nutzen

- "Was sind die Bausteine von X?"
- "Wie ist X aufgebaut?"
- Architektur-Diagramme

## Variablen, die du anpasst

- `HEADLINE`: Bold-Titel oben, z.B. "Komponenten eines KI-Agenten"
- `CONTAINER_LABEL`: zentraler Block, z.B. "KI-Agent"
- `INNER_BOXES`: 3 oder 4 Sub-Komponenten als kurze Labels
- `OUTER_LABEL`: optional, externe Box, z.B. "Umgebung"
- `INFLOW_LABEL`: Pfeil-Beschriftung Eingang, z.B. "Eingaben"
- `OUTFLOW_LABEL`: Pfeil-Beschriftung Ausgang, z.B. "Aktionen"

## Prompt-Template

```
Technical architecture diagram of {{TOPIC}} for a German-language audience.

Top center headline in bold mixed case: "{{HEADLINE}}"

Central large rounded rectangle filled with dark blue (#1E3A8A) labeled
"{{CONTAINER_LABEL}}" in white bold text at the top. Inside this central container,
{{N}} equally sized sub-component boxes arranged horizontally in a single row,
with light blue (#DBEAFE) fill and dark text. Each box contains ONLY one short
label, nothing else, NO sub-text:

- Box 1: "{{INNER_BOX_1}}"
- Box 2: "{{INNER_BOX_2}}"
- Box 3: "{{INNER_BOX_3}}"

Outside and below the central container, a separate light gray (#E5E7EB) rounded
rectangle spanning a similar width, labeled "{{OUTER_LABEL}}" in dark text.

Two thin dark gray arrows connect the central container with the outer box:
- one arrow from {{OUTER_LABEL}} upward into the leftmost inner box, with a small
  label "{{INFLOW_LABEL}}" next to it
- one arrow from the rightmost inner box downward into {{OUTER_LABEL}}, with a
  small label "{{OUTFLOW_LABEL}}" next to it

[STYLE-SUFFIX VON style-suffix-wissenschaft.md HIER ANHÄNGEN]
```

## Beispiel-Inhalt

- HEADLINE: "Komponenten eines KI-Agenten"
- CONTAINER_LABEL: "KI-Agent"
- INNER_BOXES: ["Sprachmodell", "Harness", "Werkzeuge"]
- OUTER_LABEL: "Umgebung"
- INFLOW_LABEL: "Eingaben"
- OUTFLOW_LABEL: "Aktionen"
