# CLAUDE.md

Projekt-Anweisungen für Claude Code in diesem Repository.

## Worum es geht

Dieses Repo enthält Material für deutsche TikTok-Erklär-Videos im Greenscreen-Format. Pro Video gibt es einen Ordner unter `videos/NN-thema/` mit Recherche, Schaubildern, Skript und Composites.

Zielgruppe: deutschsprachige Unternehmer, Selbständige, Dienstleister, KI-Einsteiger. Keine Tech-Insider, kein Fachjargon ohne Erklärung.

## Wo steht was

Kanonische Quellen, jede genau einmal. Bei Konflikt gilt die jeweilige Doc, nicht diese Datei.

| Thema | Quelle |
|---|---|
| End-to-End-Workflow für ein Video | `docs/workflow.md` |
| Storytelling-Bögen, Schaubild-Sequenz, ausformulierte Sprechsätze | `docs/storytelling.md` |
| Schaubild-Generierung, Provider, Style-Block | `docs/schaubild-prompting.md` |
| Recherche, Quellen, Subagents, Fact-Checking | `docs/recherche.md` |
| Schreibstil, Umlaute, Typografie, Du-Anrede | `docs/stil-regeln.md` |
| Orchestrator-Verhalten (wann fragen, wann handeln) | `.claude/skills/neues-video/SKILL.md` |
| Schaubild-Generierung-Mechanik (CLI-Aufrufe) | `.claude/skills/schaubild-prompts/SKILL.md` |

## Nicht verhandelbar (Eckpunkte)

Diese drei Punkte sind so zentral, dass sie hier nochmal stehen, als Backstop für den Fall, dass die docs übersehen werden. Detail-Regeln in den verlinkten Dateien.

1. **Fact-Checking-Pflicht.** Nichts, was im Video oder Skript steht, darf "vermutlich stimmen". Jeder Fakt mit Primärquelle. Details: `docs/recherche.md`.
2. **Echte Umlaute überall.** Im Text, im Skript, im Bild-Prompt. Nie "ae", "oe", "ue", "ss" als Ersatz. Details: `docs/stil-regeln.md`.
3. **Greenscreen-Setup heißt: immer Schaubild.** Es gibt keine Vollbild-Sektion ohne visuellen Anker. Jede Sektion braucht ein Schaubild, mindestens drei pro Video. Details: `docs/storytelling.md`.

## Ein neues Video anlegen

Slash-Command: `/neues-video <thema>`. Erzeugt Ordner und orchestriert den Workflow aus `docs/workflow.md`.

## Commits

Conventional Commits Format: `type(scope): description`.

Types: feat, fix, docs, refactor, chore, content.

Beispiele:

- `content(video-01): finalisiere skript`
- `feat(skills): neues-video skill erstellt`
- `fix(scripts): korrigiere padding in composite`

Nicht commiten ohne Aufforderung des Users.
