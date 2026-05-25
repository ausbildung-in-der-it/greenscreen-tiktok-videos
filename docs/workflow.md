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

Siehe `docs/recherche.md`. Kurz:

- WebSearch und exa AI MCP parallel laufen lassen
- Nur Primärquellen zählen (Anbieter-Docs, Papers, OECD, NN/G)
- Bei Bedarf Opus-Subagent für historische Tiefe oder konkurrierende Definitionen
- Konflikte benennen, nicht überdecken

Output: ein `recherche.md` im Video-Ordner mit Quellen und Schlüssel-Befunden.

## Schritt 3: Storytelling-Bogen

Wähle eine der Strukturen aus `docs/storytelling.md`. Default ist der **Aufklärungs-Bogen**:

1. Hook (0 bis 5 s)
2. Abgrenzung (5 bis 20 s)
3. Definition (20 bis 36 s)
4. Mechanismus (36 bis 50 s)
5. Praxis-Anker (50 bis 58 s)
6. CTA (58 bis 60 s)

## Schritt 4: Drei Schaubild-Ansätze

Skizziere drei konkurrierende visuelle Ansätze. Beispiel für "Was ist ein KI-Agent":

- Ansatz A: Hub-Spoke-Komponenten
- Ansatz B: Vergleichstabelle Chatbot vs Agent
- Ansatz C: Kreislauf-Diagramm

Lass den User wählen, dann erst generieren. Spart Iterationen.

## Schritt 5: Schaubilder generieren

Pro Schaubild:

1. Prompt aus `templates/schaubild-prompts/` als Basis nehmen
2. Stil-Block aus `templates/style-suffix-wissenschaft.md` anhängen
3. Provider wählen (Gemini default, OpenAI bei Text-Heavy)
4. `tools image generate --aspect-ratio=1:1 --image-size=2K -o ./schaubilder/X.png`
5. Output flach kopieren (tools CLI legt timestamped Files in einem Unterordner ab)
6. Umlaute und Sub-Texte visuell prüfen
7. Bei Bedarf Img2img-Korrektur

## Schritt 6: HTML-Skript

Auf Basis von `templates/skript.html.template`:

- Prämisse-Box oben
- Pro Sektion: Timing, Schaubild, Stichpunkte, Nuance-Box
- Quellen am Ende, klickbar

Stichpunkte sind kurze Phrasen (max. 6 bis 8 Wörter), nicht ausformulierte Sätze. Du sprichst frei.

Nuance-Boxen enthalten Detail-Antworten für Kommentar-Rückfragen. Wichtig: was wurde **bewusst weggelassen**, und warum.

## Schritt 7: TikTok-Composites

```bash
python3 scripts/make-tiktok-composites.py videos/NN-thema/
```

Erzeugt unter `videos/NN-thema/tiktok-1080x1920/`:

- 1080x1920 Canvas, weiß
- Schaubild oben mit Padding (Default 130/180)
- Greenscreen-Raum unten

## Schritt 8: Aufnehmen

- Greenscreen vor dem Bild positioniert
- Du sprichst frei nach Bullets aus dem HTML
- Pausen zwischen Sektionen einplanen, damit der Zuschauer Schaubilder lesen kann
- Schnittprogramm: Schaubilder als Hintergrund einblenden, du als Cutout davor

## Selbst-Check vor dem Upload

1. Jedes Schaubild auf Umlaute geprüft?
2. Jede Quelle im Skript prüfbar (URL funktioniert)?
3. Keine Em-Dashes im sichtbaren Text?
4. Hook in den ersten 3 Sekunden?
5. CTA klar und einladend?

Wenn alle 5 Punkte erfüllt sind: hochladen.
