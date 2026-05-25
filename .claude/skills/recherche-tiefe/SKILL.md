---
description: Startet eine Tiefen-Recherche zu einem Thema mit einem Opus-Subagent. Nutzt WebSearch und exa AI MCP parallel, liefert Markdown-Report mit Primärquellen, Wendepunkten, Storytelling-Hooks.
when_to_use: Triggert bei "tiefen recherche", "video recherche starten", "opus subagent recherche".
argument-hint: [thema] [optional: video-ordner]
disable-model-invocation: true
---

# Tiefen-Recherche per Opus-Subagent

Thema: $ARGUMENTS

## Wann diesen Skill nutzen

- Historische Themen (über Jahrzehnte)
- User sagt explizit "tiefer recherchieren"
- Komplexe Quellenlage mit widersprüchlichen Anbietern
- Ergebnis soll eigenes Video oder Video-Sektion werden

Für Schnell-Checks reichen WebSearch + exa direkt, kein Subagent.

## 1. Briefing vorbereiten

Verwende die Vorlage in `briefing.md` (siehe unten) und füll Thema, Kontext, Aspekte ein.

## 2. Subagent starten

```
Agent({
  description: "Tiefen-Recherche [THEMA]",
  subagent_type: "general-purpose",
  model: "opus",
  prompt: "[Briefing]",
  run_in_background: true
})
```

## 3. Während der Subagent läuft

Erklär dem User kurz, was passiert. Erwartung: 2 bis 5 Minuten Laufzeit.

## 4. Nach Abschluss

Lies das Markdown unter `videos/NN/recherche.md`. Fasse 3 bis 5 Erkenntnisse zusammen mit Fokus auf:

- Überraschende Daten oder Personen
- Klare Wendepunkte (für den Hook)
- Konflikte zwischen Quellen (für die Glaubwürdigkeit)

## 5. Übergabe ans Skript

Schlag vor, welche Erkenntnisse ins Skript wandern und welche als Backup in Nuance-Boxen landen.

## Briefing-Vorlage

```
Du bist ein Recherche-Agent. Ich brauche eine fundierte, quellengestützte
Recherche zu [THEMA].

# Kontext
[Was wurde schon erforscht?]

# Auftrag
Recherchiere die wichtigsten Stationen / Definitionen / Wendepunkte zu [THEMA].
Pro Station: kurze Beschreibung, Datum, Primärquelle als URL, optional Zitat.

# Zusätzlich
- Wendepunkt-Analyse
- Begriffsverschiebung
- 3 Storytelling-Hooks
- Empfohlener Skript-Bogen (60-90s)

# Deliverable
Markdown unter videos/NN/recherche.md, 600-1200 Wörter.

Quellen-Strenge: nur Primärquellen. Stilregeln: keine Em-Dashes, echte Umlaute,
du-Anrede, kurze Sätze.

WebSearch und exa AI MCP parallel nutzen.
```

Befolge `docs/recherche.md`.
