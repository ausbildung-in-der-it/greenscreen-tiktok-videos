---
name: recherche-tiefe
description: Startet eine Tiefen-Recherche zu einem Thema mit einem Opus-Subagent. Nutzt WebSearch und exa AI MCP parallel, liefert Markdown-Report mit Primärquellen, Wendepunkten, Storytelling-Hooks. Triggert bei "tiefen recherche", "video recherche starten", "opus subagent recherche".
---

# Tiefen-Recherche per Opus-Subagent

Du startest eine fundierte Recherche zu einem Thema, das Recherche-Tiefe verdient (Begriffsgeschichte, konkurrierende Definitionen, historische Wendepunkte).

## Wann diesen Skill nutzen

- Bei historischen Themen (über Jahrzehnte)
- Wenn der User explizit "tiefer recherchieren" sagt
- Wenn die Quellenlage komplex ist und mehrere Anbieter widersprüchlich sind
- Wenn das Ergebnis ein eigenes Video oder eine Video-Sektion werden soll

Für Schnell-Checks reicht WebSearch + exa direkt, kein Subagent.

## Schritte

### 1. Briefing vorbereiten

Vorlage:

```
Du bist ein Recherche-Agent. Ich brauche eine fundierte, quellengestützte
Recherche zu [THEMA].

# Kontext
[Was wurde schon erforscht? Welches Video, welche Sektion?]

# Auftrag
Recherchiere die wichtigsten Stationen / Definitionen / Wendepunkte zu [THEMA].
Mindestens diese Aspekte abdecken:
1. [Aspekt 1]
2. [Aspekt 2]
...

Für jede Station: kurze Beschreibung, Datum, Primärquelle als URL, optional ein
direktes Zitat.

# Zusätzlich
- Wendepunkt-Analyse: wann hat sich die Bedeutung am stärksten verschoben?
- Begriffsverschiebung: wo bedeutet X heute etwas anderes als früher?
- 3 Storytelling-Hooks für ein Video, mit Bezug auf die Recherche-Funde
- Empfohlener Skript-Bogen (60-90s)

# Deliverable
Markdown-Dokument unter `videos/NN-thema/recherche.md` mit:
- H1 Titel
- H2 pro Epoche / Station (chronologisch)
- Pro Station: 2-4 Bullets, Datum, Quelle als Hyperlink, optional Zitat
- H2 "Wendepunkte und Begriffsverschiebung"
- H2 "Storytelling-Hooks fürs Video"
- H2 "Empfohlener Skript-Bogen"

Quellen-Strenge: nur Primärquellen (Papers, offizielle Anbieter-Blogs, OECD, NN/G).
Keine zufälligen Blog-Posts. Bei Unsicherheit markieren statt raten.

Stilregeln: keine Em-Dashes, echte Umlaute, du-Anrede, kurze Sätze.

Länge: 600 bis 1200 Wörter.

WebSearch und exa AI MCP parallel nutzen.
```

### 2. Subagent starten

```
Agent({
  description: "Tiefen-Recherche [THEMA]",
  subagent_type: "general-purpose",
  model: "opus",
  prompt: "[Briefing oben]",
  run_in_background: true
})
```

### 3. Während der Subagent läuft

Erzähle dem User kurz, was der Subagent macht. Erwartungs-Management: Subagenten brauchen 2 bis 5 Minuten für eine Tiefen-Recherche.

### 4. Nach Abschluss

Lies das Markdown-Dokument unter `videos/NN-thema/recherche.md`. Fasse die wichtigsten 3 bis 5 Erkenntnisse zusammen, mit besonderem Fokus auf:

- Überraschende Daten oder Personen
- Klare Wendepunkte (für den Hook)
- Konflikte zwischen Quellen (für die Glaubwürdigkeit)

### 5. Übergabe ans Skript

Schlage dem User vor, welche Erkenntnisse ins Skript wandern und welche nur als Backup-Material in der Nuance-Box landen.

## Wichtig

- Opus statt Sonnet, weil mehr Reasoning bei komplexen Quellenkonflikten nötig
- Run in background, damit der Hauptkonversation nicht blockiert wird
- Stilregeln im Briefing explizit nennen, sonst kommt der Output mit Em-Dashes zurück
