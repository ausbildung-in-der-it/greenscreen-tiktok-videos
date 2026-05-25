# End-to-End-Workflow für ein Video

Schritt-für-Schritt-Ablauf, vom Themen-Brief bis zum fertigen Material zum Aufnehmen.

## Schritt 1: Thema und Prämisse

Bevor du irgendwas baust, formuliere die Prämisse in einem Satz:

> "Ein KI-Agent ist kein besserer Chatbot, sondern ein anderes Werkzeug."

Die Prämisse muss

- **klar abgegrenzt** sein (was sagst du, was sagst du nicht?)
- **kontrovers oder überraschend** für die Zielgruppe (sonst kein Hook)
- **belegbar** mit Primärquellen

Ohne saubere Prämisse kein Video.

## Schritt 2: Recherche

Siehe `docs/recherche.md`. Output: ein `recherche.md` im Video-Ordner mit Quellen und Schlüssel-Befunden. Bei Tiefen-Recherche zusätzlich `recherche-tiefe.md`.

## Schritt 3: Storytelling-Bogen

Wähle einen Bogen aus `docs/storytelling.md`. Default ist der **Aufklärungs-Bogen** (Bogen A). Bei Berufswahl- oder Abgrenzungs-Themen meist Bogen C (Vergleichs-Pattern).

## Schritt 4: Schaubild-Sequenz planen

Anzahl Schaubilder pro Video richtet sich nach dem Bogen, **mindestens drei**. Der Sprecher steht in jedem Moment vor einem Schaubild, es gibt keine Vollbild-Sektionen.

Tabellen pro Bogen siehe `docs/storytelling.md`. Beispiele:

- Bogen A (Aufklärung, 60s): typischerweise 4 bis 5 Schaubilder
- Bogen B (Historie, 90s): 5 bis 6 Schaubilder
- Bogen C (Vergleich, 60s): 3 bis 5 Schaubilder
- Bogen D (How-to, 120s): 5 bis 7 Schaubilder

Vor dem Generieren: pro Sektion einen Schaubild-Typ benennen (Hub-Spoke, Vergleichstabelle, Kreislauf, Matrix, Zeitstrahl, Beispiel-Bild, Hook-Bild, Outro-Bild). Wiederverwendung des Hauptbildes über zwei Sektionen ist erlaubt, wenn die zweite Sektion eine Vertiefung der ersten ist.

## Schritt 5: Schaubilder generieren

Siehe `docs/schaubild-prompting.md` für Provider, Style-Block, Mechanik. Pro Schaubild:

1. Diagramm-Typ wählen, Prompt aus `templates/schaubild-prompts/` als Basis
2. Style-Block aus `templates/style-suffix-wissenschaft.md` anhängen
3. Generieren, flach kopieren, visuell prüfen
4. Bei Fehlern: Img2img-Korrektur

## Schritt 6: HTML-Skript

Auf Basis von `templates/skript.html.template`:

- Prämisse-Box oben
- Pro Sektion: Timing, Schaubild-Referenz, **ausformulierte Sprechsätze** (siehe `docs/storytelling.md`), Nuance-Box
- Quellen am Ende, klickbar

Sprechsätze sind keine Stichpunkte und kein Teleprompter-Text. Sie enthalten Substanz: konkrete Beispiele, Zahlen, Arbeitgeber-Namen, Bilder im Kopf. Du liest sie vor der Aufnahme einmal und sprichst dann frei.

Nuance-Boxen enthalten Detail-Antworten für Kommentar-Rückfragen. Wichtig: was wurde **bewusst weggelassen**, und warum.

## Schritt 7: TikTok-Composites

```bash
python3 scripts/make-tiktok-composites.py videos/NN-thema/
```

Erzeugt unter `videos/NN-thema/tiktok-1080x1920/`:

- 1080x1920 Canvas, weiß
- Schaubild oben mit Padding (Default 130/180)
- Greenscreen-Raum unten (Default 920px)

## Schritt 8: Aufnehmen

- Greenscreen vor dem Composite-Bild positioniert
- Pro Sektion das jeweilige Schaubild als Hintergrund einblenden
- Du sprichst frei nach den Sprechsätzen aus dem HTML
- Pausen zwischen Sektionen einplanen, damit der Zuschauer Schaubilder lesen kann

## Selbst-Check vor dem Upload

1. Jedes Schaubild auf Umlaute geprüft?
2. Jede Quelle im Skript prüfbar (URL funktioniert)?
3. Keine Em-Dashes im sichtbaren Text?
4. Hook in den ersten 3 Sekunden?
5. CTA klar und einladend?
6. Wirklich kein Vollbild-Moment ohne Schaubild?

Wenn alle 6 Punkte erfüllt sind: hochladen.
