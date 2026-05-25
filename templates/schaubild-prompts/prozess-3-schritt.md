# Schaubild-Prompt: 3-Schritt-Prozess

Drei nebeneinander liegende Boxen, mit Pfeilen verbunden, mittlere Box optional hervorgehoben.

## Wann nutzen

- "So funktioniert das in 3 Schritten"
- Beispiele und Workflows
- Input → Verarbeitung → Output

## Variablen

- `HEADLINE`: z.B. "Beispiel: Lead-Recherche"
- `STEPS`: genau 3 Labels (je 1 bis 3 Wörter)
- `ICONS`: 3 einfache Symbole pro Box

## Prompt-Template

```
Three-step process diagram in German showing {{TOPIC}}.

Top center headline in bold mixed case: "{{HEADLINE}}"

Below the headline, three equally sized rounded rectangles arranged horizontally
left to right, connected by simple dark gray directional arrows pointing right
between them. Each box contains ONLY a short main label and a single small icon,
NO sub-text, NO explanation sentences.

Step 1 box (light blue #DBEAFE fill, dark text):
- Label at top: "{{STEP_1}}"
- One small dark icon below the label: {{ICON_1}}

Step 2 box in the middle (dark blue #1E3A8A fill, white text):
- Label at top: "{{STEP_2}}"
- {{N_ICONS}} small white line-art icons arranged in a horizontal row below the label: {{ICON_2}}

Step 3 box (light blue #DBEAFE fill, dark text):
- Label at top: "{{STEP_3}}"
- One small dark icon below the label: {{ICON_3}}

[STYLE-SUFFIX VON style-suffix-wissenschaft.md HIER ANHÄNGEN]
```

## Beispiel (aus Video 01)

- HEADLINE: "Beispiel: Lead-Recherche"
- STEP_1: "Auftrag", ICON_1: speech bubble
- STEP_2: "Agent arbeitet" (primary blue), ICONS: browser, search, contact card
- STEP_3: "Ergebnis", ICON_3: list/table

Vollständiger Prompt in `videos/01-was-ist-ein-ki-agent/prompts/D-clean.txt`.

## Tipp

Mittlere Box mit dunkelblauem Fill hervorheben (statt alle drei hellblau), damit der Workflow-Höhepunkt visuell stark wirkt.
