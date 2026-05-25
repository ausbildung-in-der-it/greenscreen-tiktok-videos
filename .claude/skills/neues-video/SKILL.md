---
description: Legt einen neuen TikTok-Video-Ordner unter videos/NN-thema/ an und orchestriert den kompletten Workflow von der Prämisse bis zum aufnahmefertigen Material.
when_to_use: Triggert bei "neues video", "tiktok video starten", "neuer erklärfilm".
argument-hint: [thema]
disable-model-invocation: true
allowed-tools: Bash Glob Read Write Edit Agent AskUserQuestion TaskCreate TaskUpdate WebSearch mcp__exa__web_search_exa mcp__exa__web_fetch_exa
---

# Neues TikTok-Video starten

Arbeitstitel: $ARGUMENTS

Folge die kanonischen Anleitungen:

- `docs/workflow.md`: End-to-End-Workflow
- `docs/storytelling.md`: Bögen, Schaubild-Sequenz, ausformulierte Sprechsätze
- `docs/schaubild-prompting.md`: Provider, Style-Block, Mechanik
- `docs/recherche.md`: Quellen, Subagents, Fact-Checking
- `docs/stil-regeln.md`: Umlaute, keine Em-Dashes, Du-Anrede

Diese Datei ergänzt den Workflow nur um **orchestrator-spezifische Regeln**. Sie wiederholt nichts, was in den docs steht.

## Deine Rolle: Orchestrator

Du **führst aus**, du schlägst nicht nur vor.

- Du legst den Ordner an, schreibst README, Recherche, Prompts, Skript und generierst die Schaubilder selbst.
- Du delegierst an Subagents (`Agent` Tool, model im Briefing setzen), wenn es um Tiefen-Recherche geht. Briefe wie einen Kollegen: was geprüft wurde, welche Lücken zu schließen sind, welche Primärquellen erlaubt sind, welche nicht. Output direkt nach `videos/NN/recherche-tiefe.md`.
- Du iterierst Schaubilder selbst: bei Umlaut-Fehlern Img2img-Korrektur. Wenn ein Layout nicht trägt, neu generieren mit angepasstem Prompt.
- Du nutzt `TaskCreate` und `TaskUpdate`, um Fortschritt sichtbar zu halten, sobald drei oder mehr Schritte offen sind.

Du fragst, wenn eine Entscheidung wirklich offen ist. Du fragst **nicht** "soll ich jetzt weitermachen?". Du machst weiter.

## Feedback-Punkte

Stell genau diese Fragen, mehr nicht:

1. **Prämisse:** Welche der zwei bis drei vorgeschlagenen Formulierungen passt?
2. **Recherche-Tiefe:** Schnell-Check oder Tiefen-Recherche per Subagent?
3. **Storytelling-Bogen:** Nur bei echter Unsicherheit zwischen zwei Bögen.
4. **Schaubild-Sequenz:** Welche Schaubild-Ansätze (drei Optionen pro Schlüsselbild) oder welche Variante pro Sektion?
5. **Schaubild-Iteration:** Nur wenn nach zwei Versuchen kein Treffer.
6. **Skript-Approval:** Nach komplett geschriebenem Skript.

Dazwischen führst du aus.

## Subagent-Briefing (Tiefen-Recherche)

Wenn du einen Recherche-Subagent spawnst (`Agent` Tool, `subagent_type: general-purpose`, `model: opus` für maximale Tiefe oder `sonnet` für mittlere), brief ihn mit:

- Kontext: was schon in `videos/NN/recherche.md` steht
- Lücken: welche konkreten Fragen er beantworten soll
- Erlaubte Primärquellen: BIBB, BMWK, IHK-Bund, BERUFENET, gesetze-im-internet.de, BGBl., destatis, Anthropic-Eng-Blog, OpenAI-Docs, Google Research, arXiv, OECD, NN/G, klassische Lehrbücher
- Verboten: Drittseiten-Listicles, KI-Karriere-Blogs, Werbeseiten
- Deliverable: Markdown-Datei nach `videos/NN/recherche-tiefe.md`, ein H2 pro Frage, Quellen inline, am Ende "Konflikte und Unschärfen"
- Stilregeln: echte Umlaute, keine Em-Dashes, keine erfundenen Fakten

## Workflow-Übersicht

Detaillierte Schritte siehe `docs/workflow.md`. Hier nur die Reihenfolge zum schnellen Überblick:

1. Ordner anlegen (`videos/NN-thema-slug/` mit Unterordnern)
2. Prämisse formulieren (zwei bis drei Vorschläge zur Wahl)
3. Recherche (Schnell-Check oder Subagent-Tiefe)
4. Storytelling-Bogen wählen (siehe `docs/storytelling.md`)
5. Schaubild-Sequenz planen (Anzahl + Diagramm-Typ pro Sektion)
6. Schaubilder generieren und iterieren
7. HTML-Skript schreiben (ausformulierte Sprechsätze, keine Schlagwort-Bullets)
8. TikTok-Composites generieren
9. Selbst-Check, dann Status "Aufnahmebereit"
