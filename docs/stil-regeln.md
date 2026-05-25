# Stil-Regeln

Zusammengefasst aus der globalen CLAUDE.md des Users plus projekt-spezifischer Erkenntnisse.

## Typografie

### Keine Em-Dashes (`—`) im Fließtext

Em-Dash wirkt künstlich und nach KI-generiertem Text. Stattdessen, je nach Funktion:

| Funktion | Ersatz | Beispiel |
|---|---|---|
| Einschub | Kommas | "Claude, der KI-Assistent von Anthropic, kann..." |
| Starker Einschub | Klammern | "Die API (genauer: der Endpoint) antwortet..." |
| Dramatische Pause | Punkt, neuer Satz | "Claude erklärt nicht nur. Er handelt." |
| Definition | Doppelpunkt | "Harness: das Regelwerk, was er darf." |
| Aufzählung | Doppelpunkt | "Drei Bausteine: A, B, C." |

### En-Dash (`–`)

Nur für Zahlenbereiche: "3–4 Tage", "1–2 Wochen". Nicht als Gedankenstrich in Prosa.

### Hyphen (`-`)

Für Wortverbindungen: "Claude-Code-Session", "API-Key".

### Keine standalone `---`

Wenn H1/H2 Struktur geben, sind zusätzliche Horizontal-Rules überflüssig.

## Umlaute

- Immer echte Umlaute: **ä, ö, ü, ß**
- Nie "ae", "oe", "ue", "ss" als Ersatz
- Gilt auch in Code-Beispielen, Prompts, Dateinamen wenn möglich

## Satzbau und Ton

- **Du-Anrede** überall
- **Aktive Verben** vor Nominalstil: "Wir bauen das Tool" > "Die Erstellung des Tools erfolgt"
- **Kurze Hauptsätze**: wenn ein Satz mehr als 2 Nebensätze hat, aufteilen
- **Keine Füllphrasen**: "im Wesentlichen", "grundsätzlich", "letztendlich"
- **Fachbegriffe beim ersten Auftritt erklären**: Abkürzung ausschreiben, dann konsistent kurz verwenden
- **Absätze kurz**: 2 bis 4 Sätze pro Absatz, ein Gedanke pro Absatz

## Didaktik (für Erklär-Inhalte)

Annahme: die Zuschauerin hört den Fachbegriff zum ersten Mal.

1. Abkürzungen beim ersten Auftritt ausschreiben
2. Nach Einführung konsistent eine Form benutzen
3. Kurzdefinition direkt dahinter, nicht "erkläre ich später"
4. Analogien nie mit unbekanntem Zweitbegriff
5. Das "Warum" mitliefern, nicht nur "was"
6. Beispiel vor Abstraktion, nie umgekehrt

## Selbst-Check vor Abgabe

1. Grep auf `—` (em-dash), muss 0 ergeben
2. Grep auf `^---$` (standalone HR), muss 0 ergeben außer begründete Ausnahme
3. Jeden Satz laut lesen: klingt natürlich? Keine KI-Typik?
4. Umlaute überall korrekt?
5. Du-Anrede konsequent?
