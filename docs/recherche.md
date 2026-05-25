# Recherche-Workflow

Wie du Quellen findest, prüfst und in Videos einbaust.

## Grundregel

> "Alles, was in ein Video geht, muss stimmen. 'Dürfte stimmen' ist kein Prüfen."

Diese Regel stammt aus deiner CLAUDE.md und ist im Repo nicht verhandelbar.

## Quell-Hierarchie

Von oben nach unten: stärker zu schwächer.

1. **Primäre Anbieter-Doku**: Anthropic Engineering-Blog, OpenAI Docs, Google Research, Vercel Docs
2. **Wissenschaftliche Papers**: arXiv, peer-reviewed Journals
3. **Standardisierungs-Bodies**: OECD, NIST, IEEE, W3C
4. **Lehrbücher**: Russell & Norvig, Sutton & Barto, etc.
5. **Hoch zitierte Sekundärquellen**: NN/G, Springer Surveys
6. **Reputable Blogs**: nur als Ergänzung, nicht als Hauptquelle
7. **Random Web-Posts**: keine Hauptquelle

Wenn du auf Ebene 6 oder 7 landest, frag dich: gibt es das auf einer höheren Ebene auch?

## Tooling

### WebSearch und exa AI MCP parallel

Beide haben unterschiedliche Stärken. WebSearch ist gut bei tagesaktuellen News, exa bei semantischer Recherche und Paper-Findung.

Parallel-Aufruf spart Zeit:

```
WebSearch("OpenAI definition AI agent 2026 official documentation")
mcp__exa__web_search_exa("Anthropic blog post building effective agents Claude definition components 2025 2026")
```

### Tiefen-Recherche per Opus-Subagent

Bei komplexen Themen mit vielen Stationen (z.B. Begriffsgeschichte über Jahrzehnte) lohnt sich ein dedizierter Subagent.

Beispiel-Briefing-Struktur:

- Kontext (was wurde schon erforscht?)
- Auftrag (welche Epochen, Quellen, Datum-Stand?)
- Wendepunkte (welche Hypothesen prüfen?)
- Deliverable (Markdown unter videos/NN/recherche.md, mit H2 pro Station)
- Stilregeln (Umlaute, keine Em-Dashes)

Aufruf:

```
Agent({
  subagent_type: "general-purpose",
  model: "opus",
  prompt: "...",
  run_in_background: true
})
```

## Datum-Check: gibt es eine neuere Quelle?

Bevor du eine Statistik, einen Bericht oder einen Datenstand im Skript zitierst, prüfe immer, ob inzwischen eine neuere Erhebung verfügbar ist. Quellen mit jährlichem oder periodischem Rhythmus altern schnell.

Faustregel: wenn die zitierte Quelle älter als 12 Monate ist, suche aktiv nach der nächsten Version.

Bekannte Periodika, die regelmäßig erneuert werden:

| Quelle | Rhythmus | Veröffentlichung typischerweise |
|---|---|---|
| BIBB-Erhebung Tab67 (Neuabschlüsse) | jährlich, Stichtag 30.09. | Dezember des laufenden Jahres |
| BIBB-Datenreport zum Berufsbildungsbericht | jährlich | Frühjahr |
| Statistisches Bundesamt, Auszubildende | jährlich | März und August |
| BERUFENET-Steckbriefe | laufend, Stand-Datum im PDF | mehrmals pro Jahr |
| Anthropic Model-Releases | unregelmäßig | mehrmals pro Jahr |

Vorgehen, wenn du eine BIBB-Tabelle einbauen willst:

1. Suche nach "Tabelle 67 [aktuelles Jahr]" auf bibb.de
2. Wenn vorhanden: nimm die neueste Version
3. Wenn nicht vorhanden: nimm die letzte verfügbare und markiere im Skript explizit den Stand-Datum

Den gleichen Check machst du für jede einzelne Behauptung mit Datum oder Versionsnummer im Skript.

## Selbst-Check vor Skript-Finalisierung

Grep-Liste, die du vor jedem Video einmal durchgehst:

- Jede URL im Skript: funktioniert sie (HTTP 200, nicht Redirect)?
- Jede Versions-Angabe: aus welcher Quelle?
- Jedes Datum: stimmt es mit Pressemitteilung oder Release Notes überein?
- Jedes wörtliche Zitat: exakt aus der Quelle übernommen, mit Original-Wortlaut?
- Jede Behauptung über einen Anbieter: zur offiziellen Doku verlinkt, nicht zu Drittquellen?
- Jede Statistik: gibt es eine neuere Erhebung (siehe Datum-Check oben)?

Bei Unsicherheit: lieber recherchieren als raten. Bei Nicht-Verifizierbarkeit: explizit als "nicht verifiziert" markieren, nicht weglassen.

## Konflikte zwischen Quellen

Wenn zwei Quellen widersprechen: **benennen, nicht überdecken.**

Beispiel: Russell & Norvig AIMA 1995 (1. Auflage) sagt "effectors". Spätere Auflagen sagen "actuators". Im Video kannst du das nutzen:

> "Im Original-Lehrbuch von 1995 stand sogar noch 'effectors' statt 'actuators'. Das wurde erst später modernisiert."

Das ist Fact-Check-Tiefe, die Glaubwürdigkeit gibt.

## Quellen-Format im Skript

Im HTML-Skript ans Ende, gruppiert nach Anbieter:

```html
<p class="anbieter">Anthropic, Hersteller von Claude</p>
<ul>
  <li><a href="https://...">Titel</a>, Datum, kurzes Zitat oder Beschreibung</li>
</ul>
```

Nicht nur die URL, sondern auch was die Quelle sagt. Wer das Skript später nochmal liest, soll ohne Klicken den Kontext haben.
