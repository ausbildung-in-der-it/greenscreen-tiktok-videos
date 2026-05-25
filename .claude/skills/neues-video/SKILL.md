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
- `docs/schaubild-prompting.md`: Provider, Style-Block, Bildregeln
- `docs/recherche.md`: Quellen, Artefakte, Datum-Check
- `docs/stil-regeln.md`: Umlaute, keine Em-Dashes, Du-Anrede

Diese Datei ergänzt den Workflow nur um orchestrator-spezifische Regeln. Sie wiederholt nichts, was in den docs steht.

## Deine Rolle: Orchestrator

Du führst aus, du schlägst nicht nur vor.

- Du legst den Ordner an, schreibst README, Recherche, Prompts, Skript und generierst die Schaubilder selbst.
- Du delegierst Tiefen-Recherche an Subagents (siehe `.claude/skills/recherche-tiefe/SKILL.md`).
- Du iterierst Schaubilder selbst. Bei Umlaut-Fehlern: Img2img-Korrektur. Bei nicht tragendem Layout: neu generieren.
- Du nutzt `TaskCreate` und `TaskUpdate`, sobald drei oder mehr Schritte offen sind.

Du fragst, wenn eine Entscheidung wirklich offen ist. Du fragst nicht "soll ich jetzt weitermachen?". Du machst weiter.

## Feedback-Punkte

Stell genau diese Fragen, mehr nicht:

1. **Prämisse**: welche der zwei bis drei vorgeschlagenen Formulierungen passt?
2. **Recherche-Tiefe**: Schnell-Check oder Tiefen-Recherche per Subagent?
3. **Storytelling-Bogen**: nur bei echter Unsicherheit zwischen zwei Bögen.
4. **Schaubild-Sequenz**: welcher Schaubild-Ansatz pro Schlüsselbild?
5. **Schaubild-Iteration**: nur wenn nach zwei Versuchen kein Treffer.
6. **Skript-Approval**: nach komplett geschriebenem Skript.

Dazwischen führst du aus.

## Workflow-Übersicht

Detaillierte Schritte: `docs/workflow.md`. Hier nur die Reihenfolge:

1. Ordner anlegen unter `videos/NN-thema/` mit Unterordnern
2. Prämisse formulieren (zwei bis drei Vorschläge zur Wahl)
3. Recherche (Schnell-Check in `recherche.md`, optional Subagent in `recherche-tiefe.md`)
4. Storytelling-Bogen wählen
5. Schaubild-Sequenz planen (Anzahl und Diagramm-Typ pro Sektion)
6. Schaubilder generieren und iterieren
7. HTML-Skript schreiben (ausformulierte Sprechsätze)
8. TikTok-Composites generieren
9. Selbst-Check, dann Status "Aufnahmebereit"
