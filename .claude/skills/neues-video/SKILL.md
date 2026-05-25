---
name: neues-video
description: Legt einen neuen TikTok-Video-Ordner unter videos/NN-thema/ an und führt durch Prämisse, Recherche, Storytelling-Bogen, 3 Schaubild-Ansätze. Triggert bei "neues video", "tiktok video starten", "neuer erklärfilm".
---

# Neues TikTok-Video starten

Du hilfst dem User, ein neues Video von Null aufzubauen. Strukturiert nach dem Workflow in `docs/workflow.md`.

## Argumente

Wenn der User ein Thema mitgegeben hat (z.B. `/neues-video MCP-Protokoll erklärt`), nutze es als Arbeitstitel. Wenn nicht, frag nach dem Thema.

## Schritte

### 1. Ordner anlegen

Finde die nächste laufende Nummer:

```bash
ls videos/ | grep -E '^[0-9]{2}-' | sort | tail -1
```

Lege an: `videos/NN-thema-slug/` mit Unterordnern `prompts/`, `schaubilder/`, `tiktok-1080x1920/`.

Erstelle ein `README.md` mit Arbeitstitel und Status "in Arbeit".

### 2. Prämisse formulieren

Frag den User: "Was soll die Zuschauerin am Ende verstanden haben? Ein Satz."

Speicher die Prämisse oben im README, plus Stand und Datum.

### 3. Recherche starten

Schlage vor, ob

- ein **Schnell-Check** reicht (WebSearch + exa parallel, 5 bis 10 Minuten)
- oder eine **Tiefen-Recherche per Opus-Subagent** sinnvoll ist (bei historischen Themen, Begriffsgeschichte, vielen Stationen)

Bei Schnell-Check: führe selbst durch, lege Ergebnisse in `videos/NN/recherche.md` ab.
Bei Tiefen-Recherche: starte einen Opus-Subagent mit Brief gemäß `docs/recherche.md`.

### 4. Storytelling-Bogen wählen

Zeige die 4 Bögen aus `docs/storytelling.md` (Aufklärung, Historie, Vergleich, How-to) und schlage den passendsten vor. Bei Unsicherheit: AskUserQuestion.

### 5. Drei Schaubild-Ansätze

Skizziere 3 konkurrierende visuelle Ansätze für das Hauptkonzept des Videos. Jeder Ansatz mit Stärke und Schwäche. Lass den User wählen.

### 6. Mit nächster Phase weitermachen

Nach Bestätigung: gehe zu Schaubild-Prompting (siehe `.claude/skills/schaubild-prompts/SKILL.md`).

## Wichtig

- Folge den Stil-Regeln aus `docs/stil-regeln.md` (Umlaute, keine Em-Dashes, Du-Anrede)
- Bei jedem User-Input: bestätigen, nicht raten
- Quellen-Pflicht von Anfang an (siehe `docs/recherche.md`)
