# Diagramm-Typ: Kreislauf

Mehrere nummerierte Stationen auf einem Kreis, mit Pfeilen im Uhrzeigersinn verbunden.

## Wann nutzen

- "Wie funktioniert X als Schleife?"
- Iterative Loops (ReAct, OODA, Plan-Do-Check-Act)
- "Endlos-Schleifen" als Konzept

## Variablen

- **Headline**: z.B. "Der Arbeitszyklus eines KI-Agenten"
- **Stationen**: drei bis sechs nummerierte Schritte, je ein kurzes Label (max. zwei Wörter). Vier passt am saubersten auf den Kreis (Uhrzeiten 12, 3, 6, 9). Bei fünf oder sechs wird das Layout enger.

## Visueller Rahmen

Headline oben zentriert. Darunter gleich große rounded Rectangles, gleichmäßig auf einem gedachten Kreis verteilt, mit Primärblau-Fill und weißem Bold-Text. Jede Box trägt eine Nummer plus Label.

Gebogene dunkelgraue Pfeile mit triangularen Spitzen verbinden die Stationen im Uhrzeigersinn zu einer geschlossenen Schleife. Mittelpunkt des Kreises bleibt leer.

Style-Suffix aus `templates/style-suffix-wissenschaft.md` immer unten anhängen.

## Beispiel-Inhalt

- Headline: "Der Arbeitszyklus eines KI-Agenten"
- Stationen: 1. Ziel, 2. Denken, 3. Handeln, 4. Beobachten

## Tipp

Bei mehr als vier Stationen: vor dem Generieren prüfen, ob ein linearer Prozess-Block (siehe `prozess-3-schritt.md`, mit mehr Schritten) didaktisch nicht klarer wäre als ein gedrängter Kreis.

## Provider

Siehe `docs/schaubild-prompting.md`. Default: Gemini.
