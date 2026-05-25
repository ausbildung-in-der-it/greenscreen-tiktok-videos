---
description: Legt einen neuen TikTok-Video-Ordner unter videos/NN-thema/ an und führt durch Prämisse, Recherche, Storytelling-Bogen, drei Schaubild-Ansätze.
when_to_use: Triggert bei "neues video", "tiktok video starten", "neuer erklärfilm".
argument-hint: [thema]
disable-model-invocation: true
allowed-tools: Bash Glob Read Write
---

# Neues TikTok-Video starten

Arbeitstitel: $ARGUMENTS

Folge `docs/workflow.md`. Befolge die Stil-Regeln aus `docs/stil-regeln.md` (echte Umlaute, keine Em-Dashes, Du-Anrede).

## 1. Ordner anlegen

Finde die nächste laufende Nummer:

```bash
ls videos/ 2>/dev/null | grep -E '^[0-9]{2}-' | sort | tail -1
```

Lege an: `videos/NN-thema-slug/` mit Unterordnern `prompts/`, `schaubilder/`, `tiktok-1080x1920/`. Erstelle `README.md` mit Arbeitstitel und Status "in Arbeit".

## 2. Prämisse formulieren

Frag: "Was soll die Zuschauerin am Ende verstanden haben? Ein Satz."

Speichere die Prämisse oben im README mit Datum.

## 3. Recherche

Schlag vor: Schnell-Check (WebSearch + exa parallel, 5 bis 10 Minuten) oder Tiefen-Recherche per Opus-Subagent (`/recherche-tiefe`).

Bei Schnell-Check: Ergebnisse direkt in `videos/NN/recherche.md` ablegen.

## 4. Storytelling-Bogen wählen

Zeig die vier Bögen aus `docs/storytelling.md`. Schlag den passendsten vor. Bei Unsicherheit: AskUserQuestion.

## 5. Drei Schaubild-Ansätze

Skizziere drei konkurrierende visuelle Ansätze mit Stärken und Schwächen. Lass den User wählen.

## 6. Weiter mit Schaubild-Prompting

Nach Bestätigung: `/schaubild-prompts` verwenden.
