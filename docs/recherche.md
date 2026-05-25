# Recherche-Workflow

Wie du Quellen findest, prüfst und in Videos einbaust.

## Grundregel

Alles, was in ein Video geht, muss stimmen. "Dürfte stimmen" ist kein Prüfen.

## Artefakte: zwei Dateien pro Video

Im Video-Ordner (`videos/NN-thema/`) entstehen je nach Recherche-Tiefe ein oder zwei Markdown-Dateien:

| Datei | Wer schreibt | Inhalt |
|---|---|---|
| `recherche.md` | Schnell-Check (WebSearch + exa parallel, 5 bis 10 Minuten) | Schlüssel-Befunde, Quellen, am Ende "Konflikte und Unschärfen" |
| `recherche-tiefe.md` | Subagent (`general-purpose`, model opus oder sonnet) | Antworten auf konkrete Lücken aus der Schnell-Recherche, jede Frage als eigene H2, Primärquellen inline |

Wenn nur Schnell-Check stattfindet: nur `recherche.md`. Wenn vertieft wird: beide Dateien existieren, sie ersetzen einander nicht. Skripte und Schaubilder beziehen sich auf beide.

## Quell-Hierarchie

Von oben nach unten: stärker zu schwächer.

1. **Primäre Anbieter-Doku**: Anthropic Engineering-Blog, OpenAI Docs, Google Research, Vercel Docs
2. **Behörden- und Standardisierungs-Quellen**: BIBB, BMWK, IHK-Bund, BERUFENET, gesetze-im-internet.de, BGBl., destatis, OECD, NIST, IEEE, W3C
3. **Wissenschaftliche Papers**: arXiv, peer-reviewed Journals
4. **Lehrbücher**: Russell & Norvig, Sutton & Barto, vergleichbare Standardwerke
5. **Hoch zitierte Sekundärquellen**: NN/G, Springer Surveys
6. **Reputable Blogs**: nur als Ergänzung, nicht als Hauptquelle
7. **Random Web-Posts**: keine Hauptquelle

Wenn du auf Ebene 6 oder 7 landest, frag dich: gibt es das auf einer höheren Ebene auch?

## Tooling

### WebSearch und exa AI MCP parallel

Beide haben unterschiedliche Stärken. WebSearch ist gut bei tagesaktuellen News, exa bei semantischer Recherche und Paper-Findung. Parallel-Aufruf spart Zeit.

### Tiefen-Recherche per Subagent

Bei komplexen Themen mit vielen Stationen (z.B. Begriffsgeschichte über Jahrzehnte) lohnt sich ein dedizierter Subagent. Briefing-Vorlage und CLI-Aufruf siehe `.claude/skills/recherche-tiefe/SKILL.md`. Output landet in `recherche-tiefe.md` (siehe Tabelle oben).

## Datum-Check: gibt es eine neuere Quelle?

Bevor du eine Statistik, einen Bericht oder einen Datenstand im Skript zitierst, prüfe, ob inzwischen eine neuere Erhebung verfügbar ist. Quellen mit jährlichem Rhythmus altern schnell.

Faustregel: ist die zitierte Quelle älter als 12 Monate, such aktiv nach der nächsten Version.

Bekannte Periodika:

| Quelle | Rhythmus | Veröffentlichung |
|---|---|---|
| BIBB-Erhebung Tab67 (Neuabschlüsse) | jährlich, Stichtag 30.09. | Dezember des Folgejahres |
| BIBB-Datenreport zum Berufsbildungsbericht | jährlich | Frühjahr |
| Statistisches Bundesamt, Auszubildende | jährlich | März und August |
| BERUFENET-Steckbriefe | laufend, Stand-Datum im PDF | mehrmals pro Jahr |
| Anthropic Model-Releases | unregelmäßig | mehrmals pro Jahr |

Vorgehen, wenn du eine BIBB-Tabelle einbauen willst:

1. Such nach "Tabelle 67 [aktuelles Jahr]" auf bibb.de
2. Vorhanden: nimm die neueste Version
3. Nicht vorhanden: nimm die letzte verfügbare und markiere im Skript den Stand-Datum explizit

## Konflikte zwischen Quellen

Wenn zwei Quellen widersprechen: benennen, nicht überdecken.

Beispiel: Russell & Norvig AIMA 1995 sagt "effectors", spätere Auflagen sagen "actuators". Im Video kannst du das nutzen:

> "Im Original-Lehrbuch von 1995 stand sogar noch 'effectors' statt 'actuators'. Das wurde erst später modernisiert."

Das ist Fact-Check-Tiefe, die Glaubwürdigkeit gibt.

## Quellen-Format im Skript

Im HTML-Skript ans Ende, gruppiert nach Anbieter:

```html
<p class="anbieter">Anthropic, Hersteller von Claude</p>
<ul>
  <li><a href="https://...">Titel</a>, Datum, kurze Beschreibung</li>
</ul>
```

Nicht nur die URL, sondern auch was die Quelle sagt. Wer das Skript später nochmal liest, soll ohne Klicken den Kontext haben.

## Selbst-Check vor Skript-Finalisierung

Grep-Liste, die du vor jedem Video einmal durchgehst:

- Jede URL: funktioniert sie (HTTP 200, kein Redirect)?
- Jede Versions-Angabe: aus welcher Quelle?
- Jedes Datum: stimmt es mit Pressemitteilung oder Release Notes überein?
- Jedes wörtliche Zitat: exakt übernommen?
- Jede Behauptung über einen Anbieter: zur offiziellen Doku verlinkt, nicht zu Drittquellen?
- Jede Statistik: gibt es eine neuere Erhebung?

Bei Unsicherheit: lieber recherchieren als raten. Bei Nicht-Verifizierbarkeit: explizit als "nicht verifiziert" markieren, nicht weglassen.
