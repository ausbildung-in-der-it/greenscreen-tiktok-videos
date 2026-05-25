---
description: Startet eine Tiefen-Recherche zu einem Thema mit einem Opus- oder Sonnet-Subagent. Output landet in videos/NN-thema/recherche-tiefe.md.
when_to_use: Triggert bei "tiefen recherche", "video recherche starten", "opus subagent recherche".
argument-hint: [thema] [optional: video-ordner]
disable-model-invocation: true
---

# Tiefen-Recherche per Subagent

Thema: $ARGUMENTS

Kanonische Recherche-Regeln (Quellenhierarchie, Datum-Check, Artefakte): `docs/recherche.md`. Diese Datei beschreibt nur das ausführende Vorgehen.

## Wann diesen Skill nutzen

- Historische Themen über Jahrzehnte
- User sagt explizit "tiefer recherchieren"
- Komplexe Quellenlage mit widersprüchlichen Anbietern
- Lücken aus der Schnell-Recherche (`recherche.md`), die mit fünf bis zehn Minuten Web-Suche nicht schließbar sind

Für Schnell-Checks reichen WebSearch und exa direkt, kein Subagent nötig.

## 1. Briefing zusammenbauen

Nimm die Briefing-Vorlage unten und füll Thema, Kontext, Aspekte, Output-Pfad ein. Output ist immer `videos/NN-thema/recherche-tiefe.md` (siehe `docs/recherche.md`, Abschnitt "Artefakte").

## 2. Subagent starten

```
Agent({
  description: "Tiefen-Recherche [THEMA]",
  subagent_type: "general-purpose",
  model: "opus",   // oder "sonnet" für mittlere Tiefe
  prompt: "[Briefing]",
  run_in_background: true
})
```

## 3. Während der Subagent läuft

Erklär dem User kurz, was passiert. Erwartung: zwei bis fünf Minuten Laufzeit.

## 4. Nach Abschluss

Lies das Markdown unter `videos/NN-thema/recherche-tiefe.md`. Fasse drei bis fünf Erkenntnisse zusammen, Fokus auf:

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
[Was wurde schon erforscht, was steht in videos/NN-thema/recherche.md?]

# Auftrag
Recherchiere die wichtigsten Stationen, Definitionen, Wendepunkte zu [THEMA].
Pro Station: kurze Beschreibung, Datum, Primärquelle als URL, optional Zitat.

# Zusätzlich
- Wendepunkt-Analyse
- Begriffsverschiebung
- Drei Storytelling-Hooks
- Empfohlener Skript-Bogen (60 bis 90 Sekunden)

# Deliverable
Markdown unter videos/NN-thema/recherche-tiefe.md, 600 bis 1200 Wörter.

Quellen-Strenge: nur Primärquellen. Stilregeln: keine Em-Dashes, echte Umlaute,
Du-Anrede, kurze Sätze.

WebSearch und exa AI MCP parallel nutzen.
```
