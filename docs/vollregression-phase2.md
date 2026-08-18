# Vollregression Phase 2 — alle 32 Fälle, je drei Läufe

Stand: 18.08.2026. Diese Datei wird **nach jedem einzelnen Fall** fortgeschrieben,
committet und gepusht. Bricht die Sitzung ab, steht der Stand hier — nicht im Kopf
einer Sitzung (Bauprinzip 2). Die nächste Sitzung liest den Abschnitt
„Fortschritt" und macht bei den offenen Skills weiter.

## Warum dieser Lauf

Die Bauregel-Gegenprobe (`docs/gegenprobe-bauregel.md`, Commit `b4e9c21`) hat
**alle zehn Skill-Dateien** geändert. Damit sind sämtliche 32 Testfälle gegen eine
Fassung gemessen, die es nicht mehr gibt — auch die 13, die in
`docs/testlauf-phase2-regression.md` gerade bestanden haben. Die Gegenprobe war
eine **Struktur-**, keine Verhaltensprüfung: Sie belegt, dass die Regeln dort
stehen, wo sie halten, nicht dass die Skills sich daran halten. Genau das misst
dieser Lauf.

Er ist zugleich die Definition of Done aus Phase 2.

## Portioniert, in mehreren Sitzungen

Der Lauf wird in Portionen gefahren, um Nutzungskontingent nicht in einem Stück zu
verbrennen. Jede Sitzung nimmt sich einige Skills vor und führt deren Fälle
vollständig zu Ende — dreimal erzeugt, dreimal bewertet. Ein Skill gilt erst als
**durch**, wenn alle seine Fälle abgeschlossen sind. Angefangene Skills stehen im
Fortschritt ausdrücklich als angefangen.

## Bestanden heißt 3 von 3

Jeder Fall läuft dreimal. Bestanden nur, wenn alle drei Läufe `bestanden` ergeben.
Weichen die drei Urteile voneinander ab, lautet das Ergebnis **wackelt** — ein
eigenes Ergebnis, kein „im Zweifel bestanden".

## Methode

Unverändert übernommen aus `docs/testlauf-phase2.md` und
`docs/testlauf-phase2-regression.md`, damit die Zahlen vergleichbar bleiben:

1. **Zerlegung.** Jeder Testfall maschinell geschnitten in `## Eingabe` und
   Kriterienteil. Der Eingabeteil enthält nie Sollkriterien, Bewertungsregeln oder
   die Prüfabsicht.
2. **Erzeugung.** Der ausführende Lauf bekommt Skill, Testprofil und **nur den
   Eingabeteil**. Kriterien, frühere Ausgaben und frühere Urteile sind gesperrt,
   ebenso `docs/`.
3. **Bewertung.** Ein getrennter Lauf bekommt **nur** Kriterien und die eine zu
   bewertende Ausgabe — ohne Skill-Text, ohne Eingabe, ohne Kenntnis früherer
   Urteile desselben Falls.
4. Kein Testfall wird angefasst. Befunde gehen in den Skill, nicht ins Kriterium.

Zwei Fälle laufen in zwei Zügen, weil der Nutzer zwischendurch antwortet:
`ketten / 02` (Stufe 1 → „Ja, ist am 12.08. per Mail rausgegangen." → Stufe 2).
Der zweite Zug sieht nur seine eigene erste Antwort, nie die Kriterien.

## Fortschritt — welche Skills sind durch

| Skill | Fälle | Stand |
|---|---|---|
| `account-recherche` | 3 | offen — noch nicht gelaufen |
| `angebots-schreiber` | 3 | offen — noch nicht gelaufen |
| `ausschreibungs-analyse` | 3 | offen — noch nicht gelaufen |
| `crm-notiz-zu-schritt` | 3 | offen — noch nicht gelaufen |
| `einwand-sparring` | 3 | offen — noch nicht gelaufen |
| `follow-up-generator` | 3 | offen — noch nicht gelaufen |
| `forecast-erklaerer` | 3 | offen — noch nicht gelaufen |
| `ketten` | 2 | offen — noch nicht gelaufen |
| `meeting-nachbereitung` | 3 | offen — noch nicht gelaufen |
| `outreach-personalisierer` | 3 | offen — noch nicht gelaufen |
| `preisverhandlungs-sparring` | 3 | offen — noch nicht gelaufen |

**Durch:** — noch keiner

**Offen für die nächste Sitzung:** `account-recherche`, `angebots-schreiber`, `ausschreibungs-analyse`, `crm-notiz-zu-schritt`, `einwand-sparring`, `follow-up-generator`, `forecast-erklaerer`, `ketten`, `meeting-nachbereitung`, `outreach-personalisierer`, `preisverhandlungs-sparring`

## Ergebnis

| Fall | Lauf 1 | Lauf 2 | Lauf 3 | Ergebnis |
|---|---|---|---|---|
| `account-recherche / 01-leere-quellenlage` | — | — | — | offen |
| `account-recherche / 02-namensverwechslung` | — | — | — | offen |
| `account-recherche / 03-privatdaten-grenze` | — | — | — | offen |
| `angebots-schreiber / 01-rueckfrage-disziplin` | — | — | — | offen |
| `angebots-schreiber / 02-budget-konflikt` | — | — | — | offen |
| `angebots-schreiber / 03-verbots-kollision` | — | — | — | offen |
| `ausschreibungs-analyse / 01-hartes-ko` | — | — | — | offen |
| `ausschreibungs-analyse / 02-frist-abgelaufen` | — | — | — | offen |
| `ausschreibungs-analyse / 03-unvollstaendige-unterlage` | — | — | — | offen |
| `crm-notiz-zu-schritt / 01-verlorene-opportunity` | — | — | — | offen |
| `crm-notiz-zu-schritt / 02-leere-notiz` | — | — | — | offen |
| `crm-notiz-zu-schritt / 03-ansprechpartner-weg` | — | — | — | offen |
| `einwand-sparring / 01-kunde-knickt-ein` | — | — | — | offen |
| `einwand-sparring / 02-rollenbruch` | — | — | — | offen |
| `einwand-sparring / 03-ehrliche-auswertung` | — | — | — | offen |
| `follow-up-generator / 01-unvollstaendiger-uebergabeblock` | — | — | — | offen |
| `follow-up-generator / 02-kein-anlass` | — | — | — | offen |
| `follow-up-generator / 03-stufe-drei-und-schluss` | — | — | — | offen |
| `forecast-erklaerer / 01-luecke-zum-ziel` | — | — | — | offen |
| `forecast-erklaerer / 02-bitte-um-schoenung` | — | — | — | offen |
| `forecast-erklaerer / 03-lueckenhafte-daten` | — | — | — | offen |
| `ketten / 01-recherche-fast-leer` | — | — | — | offen |
| `ketten / 02-entwurf-und-abgelehnte-forderung` | — | — | — | offen |
| `meeting-nachbereitung / 01-weiche-zusage` | — | — | — | offen |
| `meeting-nachbereitung / 02-widerspruch` | — | — | — | offen |
| `meeting-nachbereitung / 03-stichwortnotizen` | — | — | — | offen |
| `outreach-personalisierer / 01-duenne-faktenlage` | — | — | — | offen |
| `outreach-personalisierer / 02-erfundene-naehe` | — | — | — | offen |
| `outreach-personalisierer / 03-massenversand` | — | — | — | offen |
| `preisverhandlungs-sparring / 01-sofortiges-nachgeben` | — | — | — | offen |
| `preisverhandlungs-sparring / 02-schmerzgrenze` | — | — | — | offen |
| `preisverhandlungs-sparring / 03-auswertung-beziffert` | — | — | — | offen |

**Stand: 0 von 32 abgeschlossen** — 32 offen.

## Die einzelnen Fälle



## Was dieser Lauf nicht zeigt

- **Die Fälle sind konstruiert, nicht aus der Praxis.** Sie sind hart, aber
  erfunden. Eine Erfolgsquote aus konstruierten Fällen ist eine Aussage über die
  Regeltreue der Skills, keine über den Alltag eines Käufers. Vor der Beta gegen
  anonymisierte Realfälle tauschen (siehe `docs/STATUS-BAU.md`, offene Punkte).
- **Drei Läufe sind drei Läufe.** Sie zeigen, dass ein Verhalten nicht zufällig
  war. Sie zeigen nicht, dass es in jedem denkbaren Lauf auftritt. `wackelt` ist
  deshalb ein eigenes Ergebnis und wird nicht zu „bestanden" gerundet.
- **Ein Prüfer je Lauf.** Die Bewertung ist streng an die Kriteriendatei gebunden
  und mit wörtlichen Zitaten belegt, aber sie bleibt ein Modellurteil. Sie ersetzt
  keinen Menschen, der den Text an einen echten Kunden schicken würde.
- **Gemessen wird ein Skill, keine Kette aus zehn.** Die beiden Ketten-Fälle
  prüfen je eine Schnittstelle, nicht den Gesamtdurchlauf des Pakets.

## Was bei einem Befund passiert

Abweichungen werden **im Skill** behoben, nie im Testfall — das ist die Regel gegen
Weichspülen aus `CLAUDE.md`. Erscheint ein Kriterium selbst sachlich falsch, gilt
das Verfahren aus `docs/STATUS-BAU.md`, Abschnitt „Änderungsregel für Testfälle":
melden, entscheiden lassen, mit Änderungsvermerk ändern, neu bewerten. Nach jeder
Skill-Korrektur laufen die betroffenen Fälle **komplett neu**, dreimal — Läufe
gegen die alte Fassung zählen nicht mehr.
