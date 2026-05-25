# Schaubild-Prompt: Kreislauf

Vier nummerierte Boxen auf einem Kreis, mit Pfeilen im Uhrzeigersinn.

## Wann nutzen

- "Wie funktioniert X als Prozess?"
- Iterative Loops (ReAct, OODA, Plan-Do-Check-Act)
- "Endlos-Schleifen" als Konzept

## Variablen

- `HEADLINE`: z.B. "Der Arbeitszyklus eines KI-Agenten"
- `STEPS`: 3 bis 6 nummerierte Stationen, je ein kurzes Label (max. 2 Wörter)

## Prompt-Template

```
Circular flow diagram in German showing how {{TOPIC}} works in a loop.

Top center headline in bold mixed case: "{{HEADLINE}}"

Below the headline, {{N}} equally sized rounded rectangles arranged equidistantly
on an imaginary circle (positions: top, right, bottom, left). Each box is filled
with dark blue (#1E3A8A) and contains white bold text. Each box has a number
followed by a single short label, nothing else, NO sub-text:

- Top box (12 o'clock): "1. {{STEP_1}}"
- Right box (3 o'clock): "2. {{STEP_2}}"
- Bottom box (6 o'clock): "3. {{STEP_3}}"
- Left box (9 o'clock): "4. {{STEP_4}}"

{{N}} curved dark gray arrows connect the boxes clockwise, forming a clear closed loop.
Arrows have simple triangular arrowheads.

In the center of the loop, completely empty white space, NO additional text or icon.

[STYLE-SUFFIX VON style-suffix-wissenschaft.md HIER ANHÄNGEN]
```

## Beispiel-Inhalt

- HEADLINE: "Der Arbeitszyklus eines KI-Agenten"
- STEPS: ["Ziel", "Denken", "Handeln", "Beobachten"]

## Tipp

Bei 4 Boxen klappt der Kreis sauber (12, 3, 6, 9 Uhr). Bei 5 oder 6 Boxen wird das Layout enger; teste auf Lesbarkeit am Daumennagel.
