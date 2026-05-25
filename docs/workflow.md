# End-to-End-Workflow für ein Video

Schritt-für-Schritt-Ablauf vom Themen-Brief bis zum aufnahmebereiten Material. Detaillierte Regeln stehen in den verlinkten Doks, hier nur die Reihenfolge plus Verweise.

## Schritt 1: Thema und Prämisse

Formuliere die Prämisse in einem Satz. Sie muss klar abgegrenzt, kontrovers oder überraschend und mit Primärquellen belegbar sein. Ohne Prämisse kein Video.

## Schritt 2: Recherche

Siehe `docs/recherche.md`. Output je nach Tiefe: `recherche.md`, optional zusätzlich `recherche-tiefe.md` (Subagent).

## Schritt 3: Storytelling-Bogen

Wähl einen Bogen aus `docs/storytelling.md`. Default ist Bogen A (Aufklärungs-Pattern). Bei Berufswahl- oder Abgrenzungs-Themen meist Bogen C (Vergleichs-Pattern).

## Schritt 4: Schaubild-Sequenz planen

Anzahl, Funktion und Wiederverwendung pro Sektion sind in den Bogen-Tabellen in `docs/storytelling.md` festgehalten. Vor dem Generieren: pro Sektion einen Diagramm-Typ benennen (Hub-Spoke, Vergleichstabelle, Kreislauf, Matrix, Zeitstrahl, Beispiel-Bild, Hook-Bild, Outro-Bild).

## Schritt 5: Schaubilder generieren

Regeln und Provider in `docs/schaubild-prompting.md`. CLI-Mechanik (Befehl, Flach-Kopie, Img2img) in `.claude/skills/schaubild-prompts/SKILL.md`.

Pro Schaubild:

1. Diagramm-Typ wählen, Prompt aus `templates/schaubild-prompts/` als Basis oder freihändig für Custom-Layouts
2. Style-Block aus `templates/style-suffix-wissenschaft.md` anhängen
3. Generieren, flach kopieren, visuell prüfen
4. Bei Fehlern: Img2img-Korrektur

## Schritt 6: HTML-Skript

Basis: `templates/skript.html.template`. Pro Sektion: Timing, Schaubild-Referenz, ausformulierte Sprechsätze, Nuance-Box. Quellen am Ende, klickbar.

Sprechsätze sind keine Stichpunkte und kein Teleprompter-Text. Substanz: konkrete Beispiele, Zahlen, Arbeitgeber-Namen, Bilder im Kopf. Details und Beispiele in `docs/storytelling.md`.

Nuance-Boxen enthalten Detail-Antworten für Kommentar-Rückfragen, insbesondere was bewusst weggelassen wurde und warum.

## Schritt 7: TikTok-Composites

Skript: `scripts/make-tiktok-composites.py`. Defaults (Padding, Greenscreen-Raum) stehen im Code. CLI-Aufruf und Voraussetzungen in `.claude/skills/tiktok-composites/SKILL.md`.

## Schritt 8: Aufnehmen

- Greenscreen vor dem Composite-Bild positioniert
- Pro Sektion das jeweilige Schaubild als Hintergrund einblenden
- Du sprichst frei nach den Sprechsätzen aus dem HTML
- Pausen zwischen Sektionen einplanen, damit der Zuschauer Schaubilder lesen kann

## Selbst-Check vor Upload

1. Jedes Schaubild auf Umlaute geprüft?
2. Jede Quelle im Skript prüfbar (URL funktioniert)?
3. Keine Em-Dashes im sichtbaren Text?
4. Hook in den ersten 3 Sekunden?
5. CTA klar und einladend?
6. Wirklich kein Vollbild-Moment ohne Schaubild?

Wenn alle 6 Punkte erfüllt: hochladen.
