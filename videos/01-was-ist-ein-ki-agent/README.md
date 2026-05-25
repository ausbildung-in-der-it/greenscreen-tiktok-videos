# Video 01: Was ist ein KI-Agent?

**Status:** Aufnahmebereit
**Format:** 60 Sekunden, vertikal 1080x1920
**Zielgruppe:** Unternehmer, Selbständige, KI-Einsteiger

## Prämisse

Ein KI-Agent ist kein besserer Chatbot, sondern ein anderes Werkzeug. Während du mit einem Chatbot redest, arbeitet ein Agent für dich, mit eigenen Werkzeugen, in einer Schleife, bis ein Ziel erreicht ist.

## Storytelling-Bogen

Aufklärungs-Pattern (siehe `docs/storytelling.md`):

| Sek | Sektion | Schaubild |
|---|---|---|
| 0 bis 5 | Hook | keins, du im Vollbild |
| 5 bis 20 | Abgrenzung (Chatbot vs Agent) | B |
| 20 bis 36 | Komponenten (nach Anthropic) | A |
| 36 bis 50 | Arbeitszyklus | C |
| 50 bis 58 | Praxis-Beispiel (Lead-Recherche) | D |
| 58 bis 60 | CTA | keins, du im Vollbild |

## Quellen

- Anthropic, [Trustworthy Agents in Practice](https://www.anthropic.com/research/trustworthy-agents) (2026): Vier-Komponenten-Definition Model + Harness + Tools + Environment
- OpenAI, [A Practical Guide to Building Agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf): Drei-Komponenten-Variante Model + Tools + Instructions
- Anthropic, [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) (Dez 2024)
- Anthropic, [Building Agents with the Claude Agent SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk) (Sep 2025): "gather context, take action, verify work, repeat"

Vollständige Quellen-Liste im `skript.html`.

## Material

```
.
├── README.md                          Diese Datei
├── skript.html                        Spickzettel zum Aufnehmen
├── recherche-historie-fuer-folgevideo.md  Recherche für Video 02 (Begriffsgeschichte)
├── prompts/                           Bild-Generierungs-Prompts
│   ├── A-harness.txt
│   ├── B-clean.txt
│   ├── C-clean.txt
│   └── D-clean.txt
├── schaubilder/                       1:1, 2048x2048, JPG
│   ├── A-harness.jpeg                 Komponenten-Diagramm nach Anthropic
│   ├── B-clean.jpeg                   Vergleichstabelle Chatbot vs KI-Agent
│   ├── C-clean.jpeg                   Arbeitszyklus
│   └── D-clean.jpeg                   Beispiel Lead-Recherche
└── tiktok-1080x1920/                  9:16, 1080x1920, JPG, fürs Video
    ├── tiktok-A.jpg
    ├── tiktok-B.jpg
    ├── tiktok-C.jpg
    └── tiktok-D.jpg
```

## Korrekturen während der Produktion

- **Erstversion** hatte "Wahrnehmung" und "Gedächtnis" als Komponenten. Bei Quellen-Check ergab sich: das stammt aus Russell & Norvig 1995, nicht aus Anthropic. Auf Anthropics tatsächliches Vier-Komponenten-Modell umgestellt.
- "Harness" bewusst als englischer Eigenbegriff stehen gelassen, weil Anthropic ihn so verwendet und eine deutsche Übersetzung wie "Vorgaben" zu eng wäre (umfasst Anweisungen UND Leitplanken).

## Folgevideo geplant

Auf Basis der `recherche-historie-fuer-folgevideo.md`: Begriffsgeschichte KI-Agent von Hewitt 1973 über Russell & Norvig 1995 bis ReAct-Paper 2022.

## Aufnahme-Notes

- Pausen zwischen Sektionen einplanen, damit Zuschauer Schaubilder lesen können
- Hook in den ersten 3 Sekunden festziehen, danach Tempo halten
- CTA ruhig sprechen, einladend, nicht marktschreierisch
