# Drei Verstöße gegen Bauprinzip 4 (31.08.2026)

Bauprinzip 4 lautet: *„Alles in `core/` ist plattformneutrales Markdown ohne
Claude-Spezifika. Plattformwissen lebt nur in `adapter-claude/`."*

Beim Beantworten der Frage, ob das Kit für Codex bereit ist, fielen **drei
Stellen** auf, die dagegen verstoßen:

| Stelle | Was dort stand |
|---|---|
| `core/waechter/wochencheck.md` | „die Zuordnungstabelle in `CLAUDE.md`" |
| `core/interview/mapping.md` | ein Pfad in `adapter-claude/vorlagen/` |
| `notfall/05-es-geht-nicht-weiter.md` | „gibt es `CLAUDE.md`?" |

**Heute harmlos, weil es nur einen Adapter gibt.** Bei zwei Adaptern wird jede
davon zu einer falschen Anweisung für die Hälfte der Kunden — und der Wächter
beim Codex-Nutzer sucht eine Datei, die es bei ihm nicht gibt.

## Wie sie behoben sind

Nicht durch ein zweites Beispiel („`CLAUDE.md` oder `AGENTS.md`"), sondern
durch einen **Verweis auf die Quelle**, die den Namen kennt:

> Wie diese Datei heißt, hängt von der Plattform ab — die Anleitung dazu liegt
> in `system/adapter-*/INSTALLER.md`, und `START.md` nennt sie dem Nutzer beim
> Namen. Hier steht sie bewusst nicht, damit dieser Text auf jeder Plattform
> stimmt.

Dasselbe Verfahren wie bei den Ketten-Zugehörigkeiten am 28.08.: **eine Quelle,
alles andere verweist.** Eine Aufzählung beider Plattformen wäre beim dritten
Adapter wieder falsch.

## Nachlauf

Die Änderung an Prüfpunkt 4 ist verhaltensrelevant — der Wächter muss die
Zuordnungstabelle weiterhin finden, obwohl der Dateiname nicht mehr dasteht.
**Dreimal geprüft auf einem eingerichteten Kundenbaum: 3 von 3.**

Alle drei Läufe fanden `CLAUDE.md` und benannten den Weg dorthin. Einer sagte
ihn ausdrücklich: *„`START.md` nennt der Nutzerin ihr Gedächtnis beim Namen"* —
also genau die Kette, die der neue Wortlaut vorsieht.

Der Umweg kostet den Agenten einen Blick in `START.md`. Das ist der Preis dafür,
dass derselbe Satz auf beiden Plattformen stimmt.

## Was ausdrücklich offen bleibt

`START_HIER.md` ist weiterhin Claude-spezifisch — sie verlangt wörtlich die
Claude-App und sagt „Öffne Claude Code". Das ist **kein Verstoß**: Die Datei
liegt im Wurzelverzeichnis, nicht in `core/`, und sie ist der Einstiegspunkt,
der sich mit dem zweiten Adapter ohnehin gabeln muss. Sie wird dort behandelt,
nicht hier.

Ebenso offen: der Codex-Adapter selbst. Er wartet auf die Messung der
Gedächtnis-Mechanik durch den Auftraggeber — vier Fragen, fünf Minuten, auf
seinem Rechner, weil dort ein eingerichtetes Codex liegt und hier nicht.
**Erst messen, dann bauen.**
