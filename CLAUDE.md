# CLAUDE.md

Projekt-Anweisungen für Claude Code in diesem Repository.

## Worum es geht

Dieses Repo enthält Material für deutsche TikTok-Erklär-Videos im Greenscreen-Format. Pro Video gibt es einen Ordner unter `videos/NN-thema/` mit Recherche, Schaubildern, Skript und Composites.

Zielgruppe der Videos: deutschsprachige Unternehmer, Selbständige, Dienstleister, KI-Einsteiger. Keine Tech-Insider, kein Fachjargon ohne Erklärung.

## Stil und Sprache

Diese Regeln sind nicht verhandelbar und gelten überall, wo Text produziert wird (Schaubilder, Skript, Recherche, Commits).

### Umlaute

- **Immer echte Umlaute verwenden**: ä, ö, ü, ß. Nie "ae", "oe", "ue", "ss".
- Im Bild-Generierungs-Prompt zusätzlich explizit fordern: `render German umlauts correctly: ä, ö, ü, ß. Do not transliterate to ae, oe, ue, ss.`
- Wenn ein generiertes Bild Umlaute falsch rendert: Img2img-Korrektur mit `--input1=./schaubild.png` und Prompt "fix German typography, change Xae to Xä, keep everything else identical".

### Typografie

- Keine Em-Dashes (`—`) im Fließtext. Stattdessen Kommas, Doppelpunkte oder neuer Satz.
- En-Dash (`–`) nur für Zahlenbereiche.
- Hyphen (`-`) für Wortverbindungen.
- Keine redundanten `---` Horizontal-Rules, wenn Heading-Struktur reicht.

### Satzbau

- Du-Anrede.
- Aktive Verben vor Nominalstil.
- Kurze Hauptsätze. Wenn ein Satz mehr als zwei Nebensätze hat, aufteilen.
- Keine Füllphrasen wie "im Wesentlichen", "grundsätzlich".

## Fact-Checking

Alles, was in ein Video oder Skript geht, muss stimmen.

- Jedes Zitat muss aus einer geprüften Primärquelle kommen, mit URL.
- Bei Behauptungen über Anbieter (Anthropic, OpenAI, Google): zur offiziellen Doku oder zum offiziellen Blog verlinken, nicht zu Drittquellen.
- Versions-Angaben und Daten gegen die echte Doku abgleichen, nicht aus dem Training-Cache.
- Vor jeder Skript-Finalisierung den Selbst-Check aus `docs/recherche.md` durchgehen.

## Schaubild-Generierung

- Provider: Gemini als Default (günstig, ruhige Optik). OpenAI mit hoher Qualitätsstufe, wenn Text-Treue kritisch ist (z.B. bei Tabellen mit vielen Labels).
- Style-Block aus `templates/style-suffix-wissenschaft.md` an jeden Prompt anhängen.
- **Keine Sub-Texte in Boxen.** Pro Box nur ein Haupt-Label. Erklärungen kommen ins gesprochene Wort, nicht ins Schaubild.
- Heller Hintergrund (#FFFFFF), Farbpalette: dunkelblau #1E3A8A mit weißem Text, hellblau #DBEAFE mit dunklem Text. Keine Gradients, kein Glow.
- Aspect-Ratio 1:1, Image-Size 2K.

## HTML-Skript

- Basiert auf `templates/skript.html.template`.
- Stichpunkte, nicht ausformulierte Sätze (Aufnahme erfolgt ohne Teleprompter).
- Nuance-Boxen pro Sektion für Rückfragen aus Kommentaren.
- Quellen am Ende, klickbar.
- Prämisse-Box oben.

## TikTok-Composite

- Format 1080x1920 (vertikal, 9:16).
- Schaubild oben mit Padding (Default: 130px seitlich, 180px oben).
- Unten bleibt Platz für den Greenscreen-Cutout (Default: 920px).
- Skript: `scripts/make-tiktok-composites.py`. Padding-Werte sind Variablen.

## Recherche

- Primärquellen-Pflicht: Anthropic Engineering-Blog, OpenAI Docs, Google Research, Papers (arXiv), OECD, NN/G, klassische Lehrbücher (Russell & Norvig).
- Konflikte zwischen Quellen explizit benennen, nicht überdecken.
- Für Tiefen-Recherche: Opus-Subagent (general-purpose, model: opus) mit klarem Briefing nutzen.
- Parallel: WebSearch + exa AI MCP.

## Ein neues Video anlegen

Slash-Command: `/neues-video <thema>` (siehe `.claude/skills/neues-video/SKILL.md`).

Erzeugt: `videos/NN-thema/` mit Unterordnern und README-Stub.

## Commits

- Conventional Commits Format: `type(scope): description`
- Types: feat, fix, docs, refactor, chore, content
- Beispiele:
  - `content(video-01): finalisiere skript`
  - `feat(skills): neues-video skill erstellt`
  - `fix(scripts): korrigiere padding in composite`

Nicht commiten ohne Aufforderung des Users.
