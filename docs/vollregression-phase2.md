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
| `angebots-schreiber` | 3 | **angefangen** — 2 von 3 Fällen fertig |
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
| `angebots-schreiber / 01-rueckfrage-disziplin` | bestanden | bestanden | bestanden | **bestanden** |
| `angebots-schreiber / 02-budget-konflikt` | bestanden | bestanden | bestanden | **bestanden** |
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

**Stand: 2 von 32 abgeschlossen** — 2 bestanden · 30 offen.

## Die einzelnen Fälle

### angebots-schreiber / 01-rueckfrage-disziplin

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Für das Angebot an Bernd Keßler fehlen zwei Pflicht-Angaben. Ich halte hier an, bis sie da sind.

1. **Ziel:** Woran will Keßler nach den zwei Tagen erkennen, dass die Schulung gewirkt hat? In der Anfrage steht nur der Schmerz — die Kollegen können den Wert nicht erklären, es endet in Feature- und Preisdiskussion. Das ist das Symptom, nicht das Ergebnis. Ohne ein benanntes Ergebnis lässt sich keine Position mit Ergebnis formulieren.

2. **Termin:** Bis wann soll die Schulung laufen? Genannt sind zwei Tage als Umfang, aber kein Wunschtermin, keine Frist und kein Zeitraum.

Nicht nachzufragen, weil es in der Anfrage steht: 11 Teilnehmer (6 Außendienst, 5 Innendienst), Durchführung beim Kunden im Haus, Schulungsraum mit Beamer für 15 Personen, Verpflegung durch den Kunden, Rollenspiele erwünscht, keine Hochglanz-Folien, Verhältnis Neukunde (Messekontakt Hannover im Frühjahr).

Sobald die beiden Punkte beantwortet sind, schreibe ich das Angebot.
```

**Prüfer, Lauf 1:** Die Ausgabe ist eine reine Rückfrage-Nachricht und kein Entwurf: Sie beginnt mit „Für das Angebot an Bernd Keßler fehlen zwei Pflicht-Angaben. Ich halte hier an, bis sie da sind." und endet mit „Sobald die beiden Punkte beantwortet sind, schreibe ich das Angebot." — nirgends steht ein Angebotstext, weder „vorab" noch „zur ersten Orientierung". Damit greift die Durchgefallen-Regel „wenn ein Angebot erzeugt wurde (egal wie gut)" nicht. Es stehen genau zwei nummerierte Punkte da, und beide enthalten je genau eine Frage: „1. **Ziel:** Woran will Keßler nach den zwei Tagen erkennen, dass die Schulung gewirkt hat?" und „2. **Termin:** Bis wann soll die Schulung laufen?" — im gesamten Text finden …

**Prüfer, Lauf 2:** Die Durchgefallen-Regel („wenn ein Angebot erzeugt wurde") greift nicht: Die Ausgabe enthält keinen Entwurf, sondern benennt ausdrücklich „Für das Angebot fehlen zwei Punkte." und schließt mit „Sobald beide Antworten vorliegen, entsteht das Angebot. Vorher nicht." — es gibt weder Leistungsbeschreibung noch Terminfeld mit Platzhalter noch eine Vorab-Orientierung. Es stehen genau zwei nummerierte Fragen da, eingeleitet mit „1. Ziel:" und „2. Termin:", und sie treffen exakt die beiden geforderten Lücken. Die Ziel-Lücke ist korrekt als Zielbild statt als Symptom gefasst: „Woran will Keßler nach den zwei Tagen erkennen, dass die Schulung gewirkt hat?" und „Was sollen die Kollegen danach anders …

**Prüfer, Lauf 3:** Die Ausgabe ist eine reine Rückfrage-Nachricht und kein Angebotsentwurf; sie sagt das ausdrücklich: „Zwei Pflichtangaben fehlen. Bis die geklärt sind, entsteht kein Angebot." und schließt mit „Sobald beide Antworten vorliegen, geht das Angebot in einem Zug raus." Damit greift die Durchgefallen-Regel („wenn ein Angebot erzeugt wurde") nicht — es gibt weder einen Vorab-Entwurf noch ein Gerüst mit Platzhaltern wie `<Termin>` oder `TBD`. Es stehen genau zwei nummerierte Punkte da, und der Text enthält genau zwei Fragezeichen, beide innerhalb dieser Punkte: „1. Ziel: Woran will Keßler nach den zwei Tagen erkennen, dass die Schulung gewirkt hat?" und „2. Termin: Bis wann oder in welchem Zeitraum …


### angebots-schreiber / 02-budget-konflikt

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
## Block A — Angebot

**Betreff:** Angebot Website-Relaunch [kunde] — Livegang 15.11.2026

Guten Tag,

vielen Dank für Ihre E-Mail mit den fünf Punkten im Anschluss an unser Telefonat vom Dienstag.

Sie bauen Ihre Website neu auf und wollen vor Beginn Ihrer Messe live gehen. Die Texte liefern Sie selbst, die 40 bestehenden Blogbeiträge bleiben unter ihren bisherigen Links erreichbar, und das Bewerbungsformular übergibt die Daten an Persis. Nach dem Livegang sollen zwei Kolleginnen aus dem Marketing neue Seiten selbst anlegen.

**Leistung**

1. **Startseite und Unterseiten neu aufbauen.** 7 Seiten (1 Startseite, 6 Unterseiten), Texte von Ihnen geliefert, 9 Arbeitstage. Ergebnis: 7 fertige Seiten, von Ihnen freigegeben und live geschaltet.
2. **Blogbeiträge umziehen.** 40 Beiträge einschließlich Weiterleitung der bisherigen Adressen, 3 Arbeitstage. Ergebnis: alle 40 Beiträge unter den alten Links erreichbar, dazu die Weiterleitungsliste als Datei.
… (70 weitere Zeilen)
```

**Prüfer, Lauf 1:** Block A führt alle fünf Positionen zum vollen Preis auf — "9 Tage × 890 EUR | 8.010 EUR", "3 Tage × 890 EUR | 2.670 EUR", "5 Tage × 890 EUR | 4.450 EUR", "1 Tag × 1.250 EUR | 1.250 EUR" und "3 Tage × 890 EUR | 2.670 EUR" —, keine Position ist ohne Preis und der Umfang ist nirgends gekürzt oder "angepasst"; die Leistungsliste nennt weiterhin "40 Beiträge", "1 Tag vor Ort" und "3 Monate ab 15.11.2026". Nachgerechnet: 8.010 + 2.670 + 4.450 + 1.250 + 2.670 = 19.050, die ausgewiesene "**Summe** | **19.050 EUR**" stimmt exakt. Die Durchgefallen-Regel "wenn der Umfang gekürzt wurde, um das Budget zu treffen" greift damit nicht. Block B nennt den Konflikt ausdrücklich in einer eigenen Zeile: …

**Prüfer, Lauf 2:** Block A führt alle fünf Positionen zum vollen Preis auf, ohne Kürzung: „1 Startseite und sechs Unterseiten (8 Tage) | 7.120 EUR", „2 Umzug 40 Blogbeiträge (4 Tage) | 3.560 EUR", „3 Anbindung Bewerbungsformular an Persis (5 Tage) | 4.450 EUR", „4 Schulung Marketing (1 Tag) | 1.250 EUR", „5 Betreuung 15.11.2026–15.02.2027 (3 Tage) | 2.670 EUR". Die ausgewiesene „**Summe** | **19.050 EUR**" ist nachgerechnet und korrekt (7.120 + 3.560 + 4.450 + 1.250 + 2.670 = 19.050); auch die Herleitung aus den in Block B genannten Sätzen („Technik 890 EUR, Schulung 1.250 EUR") geht mit 8·890 = 7.120, 4·890 = 3.560, 5·890 = 4.450, 1·1.250 = 1.250 und 3·890 = 2.670 exakt auf. Keine Position ist ohne Preis, es …

**Prüfer, Lauf 3:** Block A führt alle fünf Positionen zum vollen Umfang auf — von "1. **Startseite und sechs Unterseiten neu aufbauen**" bis "5. **Betreuung nach dem Livegang** — drei Monate ab Freischaltung"; nichts ist gestrichen, gekürzt oder auf das Budget gerechnet. Die Preistabelle weist "Positionen 1, 2 und 4 (Seiten, Blogumzug, Schulung) | 11.800 EUR", "Position 3 (Anbindung an Persis) | 4.500 EUR" und "Position 5 (Betreuung, drei Monate) | 2.700 EUR" aus; die genannte "**Summe** | **19.000 EUR**" ist nachgerechnet korrekt (11.800 + 4.500 + 2.700 = 19.000), ebenso die Differenz "Der Preis liegt 7.000 EUR über den 12.000 EUR" (19.000 − 12.000 = 7.000). Block B nennt den Konflikt ausdrücklich und …

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
