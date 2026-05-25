# Greenscreen TikTok Videos

Workflow und Material für deutsche TikTok-Erklär-Videos im Greenscreen-Format. Zielgruppe: Unternehmer, Selbständige, KI-Einsteiger.

## Idee

Jedes Video erklärt **ein Konzept** in 60 bis 90 Sekunden. Du sprichst frei vor Greenscreen, im Hintergrund laufen 3 bis 5 selbst gemachte Schaubilder. Format ist vertikal 1080x1920.

## Workflow auf einen Blick

1. **Thema wählen** und Prämisse formulieren. Ein Satz, was die Zuschauerin am Ende verstanden haben soll.
2. **Recherche** mit Primärquellen (siehe `docs/recherche.md`). Anthropic, OpenAI, Wissenschaft, OECD. Keine Drittquellen ohne Reputation.
3. **Storytelling-Bogen** aus dem Template wählen (`docs/storytelling.md`). Hook → Abgrenzung → Definition → Mechanismus → Praxis → CTA.
4. **3 Konzept-Ansätze** für Schaubilder skizzieren, einen wählen.
5. **Schaubilder generieren** über `tools image generate` mit den Prompt-Templates aus `templates/schaubild-prompts/`. Provider Gemini oder OpenAI, 1:1, 2K.
6. **HTML-Skript bauen** auf Basis von `templates/skript.html.template`. Bullets zum freien Sprechen, Nuance-Boxen für Rückfragen.
7. **TikTok-Composites** rendern mit `scripts/make-tiktok-composites.py`. 1:1 wird zu 1080x1920 mit Padding, Greenscreen-Raum bleibt unten.
8. **Aufnehmen, schneiden, posten.**

## Verzeichnis-Struktur

```
.
├── README.md                Diese Datei
├── CLAUDE.md                Projekt-Anweisungen für Claude Code
├── .claude/skills/          Slash-Commands für wiederkehrende Aufgaben
├── docs/                    Methodik und Best Practices
├── templates/               Wiederverwendbare Prompts, Style-Blöcke, HTML
├── scripts/                 Python-Helpers (Composite, Umlaut-Fix)
└── videos/                  Ein Ordner pro Video, alles drin
```

## Bei einem neuen Video

Verwende den Slash-Command `/neues-video <thema>`, der die Ordnerstruktur unter `videos/NN-thema/` anlegt und dich durch Recherche und Konzept führt.

## Stil

- Echte Umlaute überall (ä, ö, ü, ß), nie Transliteration
- Keine Em-Dashes im Fließtext
- Aktive Verben, kurze Sätze, Du-Anrede
- Bei Diagrammen: helle Hintergründe, disziplinierte Farbpalette, keine Sub-Texte in Boxen

Vollständige Stil-Regeln in `docs/stil-regeln.md`.
