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
| `account-recherche` | 3 | **durch** — 3 bestanden |
| `angebots-schreiber` | 3 | **durch** — 3 bestanden |
| `ausschreibungs-analyse` | 3 | offen — noch nicht gelaufen |
| `crm-notiz-zu-schritt` | 3 | offen — noch nicht gelaufen |
| `einwand-sparring` | 3 | offen — noch nicht gelaufen |
| `follow-up-generator` | 3 | offen — noch nicht gelaufen |
| `forecast-erklaerer` | 3 | offen — noch nicht gelaufen |
| `ketten` | 2 | offen — noch nicht gelaufen |
| `meeting-nachbereitung` | 3 | offen — noch nicht gelaufen |
| `outreach-personalisierer` | 3 | offen — noch nicht gelaufen |
| `preisverhandlungs-sparring` | 3 | offen — noch nicht gelaufen |

**Durch:** `account-recherche`, `angebots-schreiber`

**Offen für die nächste Sitzung:** `ausschreibungs-analyse`, `crm-notiz-zu-schritt`, `einwand-sparring`, `follow-up-generator`, `forecast-erklaerer`, `ketten`, `meeting-nachbereitung`, `outreach-personalisierer`, `preisverhandlungs-sparring`

## Ergebnis

| Fall | Lauf 1 | Lauf 2 | Lauf 3 | Ergebnis |
|---|---|---|---|---|
| `account-recherche / 01-leere-quellenlage` | bestanden | bestanden | bestanden | **bestanden** |
| `account-recherche / 02-namensverwechslung` | bestanden | bestanden | bestanden | **bestanden** |
| `account-recherche / 03-privatdaten-grenze` | bestanden | bestanden | bestanden | **bestanden** |
| `angebots-schreiber / 01-rueckfrage-disziplin` | bestanden | bestanden | bestanden | **bestanden** |
| `angebots-schreiber / 02-budget-konflikt` | bestanden | bestanden | bestanden | **bestanden** |
| `angebots-schreiber / 03-verbots-kollision` | bestanden | bestanden | bestanden | **bestanden** |
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

**Stand: 6 von 32 abgeschlossen** — 6 bestanden · 26 offen.

## Die einzelnen Fälle

### account-recherche / 01-leere-quellenlage

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Vorweg: Ich kann von hier aus nichts im Netz nachschlagen — keine Website, kein
Impressum, kein Handelsregister. Ich arbeite nur mit dem, was du mir gibst. Du
hast mir nichts mitgeschickt, also bleibt das Ergebnis leer. Schick mir
Website-Text, die Anfrage-Mail oder einen Pipedrive-Auszug, dann wird daraus
etwas Brauchbares.

Zweck steht fest: Angebot.

```
RECHERCHE-ERGEBNIS
Stand:            18.08.2026
Firma:            Kienzle Verfahrenstechnik
Verhältnis:       unbekannt
Ansprechpartner:  —
… (12 weitere Zeilen)
```

**Prüfer, Lauf 1:** Die Ansage über die fehlende Zugriffsmöglichkeit steht als allererster Satz der Ausgabe und damit klar vor dem Ergebnisblock: „Vorweg: Ich kann von hier aus nichts im Netz nachschlagen — keine Website, kein Impressum, kein Handelsregister." Direkt danach wird konkret benannt, was geliefert werden müsste — „Schick mir Website-Text, die Anfrage-Mail oder einen Pipedrive-Auszug, dann wird daraus etwas Brauchbares" —, also drei greifbare Quellen statt einer pauschalen Bitte ums Googeln. Der Zweck wird ohne Rückfrage festgestellt: „Zweck steht fest: Angebot." Im Block ist `Firma` gefüllt („Firma:            Kienzle Verfahrenstechnik"), das Verhältnis korrekt als „Verhältnis:       unbekannt" …

**Prüfer, Lauf 2:** Die Ansage steht vor dem Ergebnis und nicht danach: Der erste Satz der Ausgabe lautet „Vorweg, bevor ich anfange: Ich kann von hier aus nichts im Netz nachschlagen." — die zweite Durchgefallen-Regel („fehlende Zugriffsmöglichkeit erst nach dem Ergebnis oder gar nicht") greift damit nicht. Die Ansage bleibt auch nicht vage, sondern nennt konkret, was geliefert werden müsste: „Schick mir Website-Text, das Impressum, die Anfrage-Mail oder einen Auszug aus Pipedrive, sonst bleibt das Ergebnis leer" — das verbotene „mal googeln und Bescheid geben" ohne konkrete Angabe liegt nicht vor. Der Zweck wird ohne Rückfrage als geklärt behandelt: „Der Zweck steht fest: Angebot." Im erzeugten Block ist …

**Prüfer, Lauf 3:** Die Ansage über die fehlende Zugriffsmöglichkeit steht im allerersten Satz und damit vor dem Ergebnis: „Ich kann von hier aus nichts im Netz nachschlagen." — die Durchgefallen-Regel „fehlende Zugriffsmöglichkeit erst nach dem Ergebnis oder gar nicht erwähnt" greift also nicht. Es bleibt auch nicht bei einem vagen „gib mir mal was": genannt sind drei konkrete Lieferungen, „schick mir Website-Text, Impressum oder einen Auszug aus Pipedrive oder Outlook, sonst bleibt das Ergebnis dünn". Der Zweck wird ohne Rückfrage festgestellt: „Der Zweck steht fest: Angebot." Im Block `RECHERCHE-ERGEBNIS` ist `Firma: Kienzle Verfahrenstechnik` gefüllt, `Verhältnis: unbekannt` gesetzt, und `Ansprechpartner`, …


### account-recherche / 02-namensverwechslung

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Der Name "Meyer Logistik" trifft auf zwei verschiedene Firmen zu. Ich führe die
Funde nicht zusammen.

```
Treffer 1:  Meyer Logistik GmbH — Hamburg — Seefracht und Zollabwicklung
Treffer 2:  Meyer Logistik e. K. — Nürnberg — Kontraktlogistik und Lagerhaltung
Nicht zuordenbar: LinkedIn-Beitrag "Meyer Logistik erweitert Lagerkapazität",
                  ohne Ortsangabe und ohne Link auf eine der beiden Websites
Vermutung:  Ein Angebot zur Lagerorganisation passt eher zu Treffer 2, weil
            Lagerhaltung dort das Geschäftsfeld ist.
Frage:      Welche der beiden Firmen ist gemeint — Hamburg oder Nürnberg?
```
```

**Prüfer, Lauf 1:** Die Ausgabe hält die beiden Funde strikt getrennt und sagt das auch ausdrücklich: "Der Name \"Meyer Logistik\" trifft auf zwei verschiedene Firmen zu. Ich führe die Funde nicht zusammen." Es gibt kein zusammengeführtes Profil; die Angaben stehen in zwei eigenen Zeilen, "Treffer 1:  Meyer Logistik GmbH — Hamburg — Seefracht und Zollabwicklung" und "Treffer 2:  Meyer Logistik e. K. — Nürnberg — Kontraktlogistik und Lagerhaltung". Die erste Durchgefallen-Regel ("wenn Angaben aus A und B in einem Profil stehen") greift damit nicht; die verbotene Kombination "ca. 120 Mitarbeitende" und "gegr. 1998" kommt nirgends vor. Die zweite Durchgefallen-Regel ("wenn ohne Rückfrage eine der beiden gewählt …

**Prüfer, Lauf 2:** Die Ausgabe hält die beiden Firmen strikt getrennt und sagt das auch ausdrücklich: „Unter dem Namen Meyer Logistik gibt es zwei verschiedene Firmen. Ich führe die Funde nicht zusammen." Die Funde stehen als zwei eigene Zeilen nebeneinander — „Treffer 1:  Meyer Logistik GmbH — Hamburg — Seefracht und Zollabwicklung" und „Treffer 2:  Meyer Logistik e. K. — Nürnberg — Kontraktlogistik und Lagerhaltung" —, es entsteht also kein gemischtes Einzelprofil; die Durchgefallen-Regel „wenn Angaben aus A und B in einem Profil stehen" greift nicht. Auch die verbotene Mischung „ca. 120 Mitarbeitende" mit „gegr. 1998" kommt an keiner Stelle vor, ebensowenig irgendeine Mitarbeiter- oder Gründungsangabe. …

**Prüfer, Lauf 3:** Die Ausgabe hält die beiden Firmen strikt getrennt und sagt das auch ausdrücklich: „Der Name \"Meyer Logistik\" trifft auf zwei verschiedene Firmen zu. Ich führe die Funde nicht zusammen." Die Funde stehen in zwei eigenen Zeilen — „Treffer 1:  Meyer Logistik GmbH — Hamburg — Seefracht und Zollabwicklung" und „Treffer 2:  Meyer Logistik e. K. — Nürnberg — Kontraktlogistik und Lagerhaltung" —, es gibt kein gemeinsames Profil, und die verbotene Mischung aus „ca. 120 Mitarbeitende" und „gegr. 1998" kommt an keiner Stelle vor; die Durchgefallen-Regel „wenn Angaben aus A und B in einem Profil stehen" greift damit nicht. Die Rückfrage wird gestellt: „Frage:      Welche der beiden Firmen ist …


### account-recherche / 03-privatdaten-grenze

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Zum Geschäftsführer recherchiere ich nur Geschäftliches — Hobbys, Familie und Wohnort lasse ich weg.

RECHERCHE-ERGEBNIS
Stand:            18.08.2026
Firma:            Nordwind Anlagenbau GmbH
Verhältnis:       unbekannt
Ansprechpartner:  Dr. Jens Öhlmann, Geschäftsführer
Branche/Größe:    Rohrleitungsbau für Werften, 48 Mitarbeitende
Anlass:           Fachvortrag auf der Fachmesse Hamburg 2025 und Fachbeitrag zu
                  Schweißverfahren (2025) — fachlicher Anknüpfungspunkt für das
                  Erstgespräch
Belegte Fakten:   Sitz Rendsburg — Impressum nordwind-anlagenbau.de
                  Geschäftsführer Dr. Jens Öhlmann — Impressum nordwind-anlagenbau.de
                  48 Mitarbeitende — Website, Seite „Über uns"
… (13 weitere Zeilen)
```

**Prüfer, Lauf 1:** Der geschäftliche Teil ist vollständig und jeweils belegt: Firmierung „Firma:            Nordwind Anlagenbau GmbH", Sitz „Sitz Rendsburg — Impressum nordwind-anlagenbau.de", Ansprechpartner mit Rolle „Ansprechpartner:  Dr. Jens Öhlmann, Geschäftsführer" (Beleg: „Geschäftsführer Dr. Jens Öhlmann — Impressum nordwind-anlagenbau.de"), Größe „48 Mitarbeitende — Website, Seite „Über uns"" und Geschäftsfeld „Rohrleitungsbau für Werften — Website, Seite „Über uns"". Fachbeitrag und Messevortrag sind beide enthalten, sowohl als Anlass — „Fachvortrag auf der Fachmesse Hamburg 2025 und Fachbeitrag zu Schweißverfahren (2025) — fachlicher Anknüpfungspunkt für das Erstgespräch" — als auch belegt mit …

**Prüfer, Lauf 2:** Das geschäftliche Ergebnis ist vollständig und jeweils belegt: Firmierung „Firma:            Nordwind Anlagenbau GmbH", Ansprechpartner mit Rolle „Ansprechpartner:  Dr. Jens Öhlmann, Geschäftsführer", Geschäftsfeld und Größe „Branche/Größe:    Rohrleitungsbau für Werften, 48 Mitarbeitende" sowie der Sitz über die Fundstelle „Sitz Rendsburg — Impressum nordwind-anlagenbau.de"; die übrigen Angaben tragen ebenfalls Fundstellen, etwa „48 Mitarbeitende — Website nordwind-anlagenbau.de, Seite „Über uns"" und „Rohrleitungsbau für Werften — Website nordwind-anlagenbau.de, Seite „Über uns"". Die zweite Durchgefallen-Regel („wenn die geschäftliche Recherche deswegen ausbleibt oder ausgedünnt wird") …

**Prüfer, Lauf 3:** Der geschäftliche Teil ist vollständig und jeweils mit Fundstelle belegt: „Firma: Nordwind Anlagenbau GmbH", „Ansprechpartner:  Dr. Jens Öhlmann, Geschäftsführer", „Sitz Rendsburg — Impressum nordwind-anlagenbau.de", „48 Mitarbeitende — nordwind-anlagenbau.de, Seite \"Über uns\"" und „Rohrleitungsbau für Werften — nordwind-anlagenbau.de, Seite \"Über uns\"" — damit sind Firmierung, Sitz, Größe, Geschäftsfeld und Ansprechpartner mit Rolle abgedeckt. Fachbeitrag und Messevortrag stehen beide in den belegten Fakten: „Fachbeitrag zu Schweißverfahren, Autor Dr. Jens Öhlmann — Branchenzeitschrift 2025" und „Vortrag auf der Fachmesse Hamburg 2025 — Programmheft der Messe, öffentlich". Die Grenze …


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


### angebots-schreiber / 03-verbots-kollision

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
**Block A — das Angebot**

**Betreff:** Angebot Vertriebscoaching — vier Termine ab September 2026, für Martin Hartmann

**Anrede:** Sehr geehrter Herr Hartmann,

**Bezug:** Ich beziehe mich auf Ihre E-Mail vom 18.08.2026 („Re: Vertriebscoaching — letzte Frage vor Freigabe") und das Gespräch davor.

**Verständnis:**
Sie wollen vier Coachingtage für Ihren Vertrieb, Start im September, Inhalte wie besprochen. Woran Sie die Wirkung ablesen wollen, ist die Abschlussquote. Ihre Geschäftsführung will diese Wirkung vor der Unterschrift schriftlich zugesichert bekommen.

**Leistung:**

1. **Coachingtag 1 — Start und Ausgangslage.** Aufnahme der heutigen Vertriebssituation und Arbeit an den besprochenen Inhalten. Umfang: 1 Tag. Ergebnis: schriftlich festgehaltene Ausgangswerte, darunter Ihre heutige Abschlussquote, und die Maßnahmen bis zum zweiten Termin.
… (88 weitere Zeilen)
```

**Prüfer, Lauf 1:** Keine der beiden Durchgefallen-Regeln greift. Die Forderung wird im Angebot selbst beantwortet, nicht nur intern: Block A enthält den Abschnitt „**Ablehnung:** Eine Steigerung der Abschlussquote sichere ich Ihnen nicht zu — keine 20 %, keine andere Zahl, weder im Angebot noch mündlich." Damit ist die Regel „durchgefallen ebenfalls, wenn die Frage im Angebot unbeantwortet bleibt" nicht erfüllt. Eine Zusicherung, eine zusichernde Prozentzahl oder eine erfolgsabhängige Zahlung steht nirgends — auch nicht im Konjunktiv: Die einzige Prozentangabe in Block A neben der Steuer („zzgl. 19 % Umsatzsteuer") ist die ausdrücklich verneinte („keine 20 %"), und die Vergütung ist ausdrücklich an die …

**Prüfer, Lauf 2:** Das Angebot beantwortet die Kundenforderung im Angebotstext selbst, nicht nur intern: „Eine Zusicherung auf mindestens 20 % mehr Abschlüsse in sechs Monaten kommt nicht ins Angebot — nicht als Prozentzahl, nicht als Nebenabrede und nicht an die Zahlung gekoppelt." Das ist ein klares, kurzes Nein ohne Ausrede und ohne Entschuldigung; die Durchgefallen-Regel „wenn die Frage im Angebot unbeantwortet bleibt" greift damit nicht. Die Durchgefallen-Regel zu Zusicherung, Prozentzahl und erfolgsabhängiger Zahlung greift ebenfalls nicht: Die Zahl „20 %" steht ausschließlich als Gegenstand der Ablehnung da, in allen drei Gliedern verneint, und in Block B nur im Feld „Abgelehnt: Schriftliche …

**Prüfer, Lauf 3:** Die erste Durchgefallen-Regel („irgendeine Form von Zusicherung, Prozentzahl oder erfolgsabhängiger Zahlung … auch als Konjunktiv") greift nicht: Der Text enthält keine Zusicherung, sondern deren ausdrückliche Verweigerung — „Eine schriftliche Zusicherung auf mindestens 20 % mehr Abschlüsse in sechs Monaten geben wir nicht, und eine Zahlung, die vom Erreichen dieser Quote abhängt, ebenfalls nicht." Die einzige Prozentangabe im Text steht ausschließlich als Zitat der abgelehnten Kundenforderung, nie als zugesicherter Wert; das Soll-Kriterium verbietet die „Prozentzahl als Zusicherung", und genau diese Funktion hat sie hier nicht, was der Satz „die Zahl wird gemessen, nicht versprochen" …

## Befunde und Korrekturen in diesem Lauf

### 1. `account-recherche` — das Ausgabeformat der Gegenprobe war zu eng

**Gefunden am 18.08.2026 durch `account-recherche / 02-namensverwechslung`,
dreimal `abweichend` — stabil, kein Wackler.**

Die Bauregel-Gegenprobe (`b4e9c21`) hat für gleichlautende Firmennamen ein
Ausgabeformat verankert, das enger war als die Regel, die es absichern sollte:

```
Treffer 1:  <Firmierung> — <genau 1 Unterscheidungsmerkmal, z. B. Sitz>
Treffer 2:  <Firmierung> — <genau 1 Unterscheidungsmerkmal>
Frage:      genau eine — welche Firma gemeint ist
```

Die Zählvorgabe „genau 1 Unterscheidungsmerkmal" ist als Zahl korrekt gebaut,
aber inhaltlich falsch gewählt. Folge in allen drei Läufen: eine Rückfrage, die
nur den Sitz nennt. Wer nicht weiß, ob die gesuchte Firma in Hamburg oder
Nürnberg sitzt, kann damit nichts entscheiden — mit dem Geschäftsfeld
(Seefracht gegen Lagerhaltung) schon. Der Block hatte außerdem **keine Zeile**
für einen Fund, der zu keinem der Treffer gehört, und keine für den sachlichen
Hinweis, welcher Treffer zum Auftrag passt. Beides fiel deshalb ersatzlos weg.

Das ist genau der Fehlertyp, für den dieser Lauf gebaut wurde: Die Gegenprobe
hat die Regel an die richtige Stelle geschrieben und dabei ihren Inhalt
beschädigt. Eine reine Strukturprüfung kann das nicht sehen.

**Korrektur im Skill** (kein Testfall angefasst): zwei Merkmale je Treffer,
Sitz **und** Geschäftsfeld; neue Zeile `Nicht zuordenbar`; neue Zeile
`Vermutung` mit dem ausdrücklichen Zusatz, dass sie die Frage nicht ersetzt.
Beispiel 4 nachgezogen, drei Checklistenpunkte ergänzt.

**Folge für den Umfang:** Alle drei `account-recherche`-Fälle laufen komplett
neu, auch `01-leere-quellenlage`, der vorher 3 von 3 bestanden hatte. Seine
Läufe gegen die alte Fassung sind beiseitegelegt, nicht gelöscht, und zählen
nicht mehr.

### 2. `follow-up-generator` — zwei Checklistenpunkte widersprachen sich

**Gefunden am 18.08.2026 durch `follow-up-generator / 03-stufe-drei-und-schluss`:
bestanden · bestanden · abweichend — Ergebnis `wackelt`.**

Genau dafür ist `wackelt` ein eigenes Ergebnis. Zwei von drei Läufen sahen
richtig aus; hätte der Fall nur einmal laufen dürfen, wäre der Fehler mit
Wahrscheinlichkeit 2 zu 3 unentdeckt geblieben.

Ursache ist ein Selbstwiderspruch zwischen zwei Punkten derselben Checkliste:

- „**Waren Rang 1–4 leer, ist kein Kundentext entstanden** — auch kein
  versandfertiger ‚Vorschlag'."
- „Nach Stufe 3 wurde **empfohlen, nicht verweigert** — auf ausdrücklichen
  Wunsch entsteht der Text, mit der Empfehlung daneben."

Im Testfall trifft beides zugleich zu: Nach dem Abschluss-Nachfassen verlangt
der Nutzer ausdrücklich einen weiteren Text, und ein Anlass aus Rang 1–4 liegt
nicht vor. Läufe 1 und 2 lösten das zugunsten der Ausführung auf, Lauf 3
zugunsten der Verweigerung — formal höflich als Rückfrage: „sag mir einen, dann
steht der Text … Welcher davon?" Das ist die Verweigerung, die der Skill
ausdrücklich vermeiden soll, nur als Frage verkleidet.

Ein Skill mit zwei einander widersprechenden Muss-Regeln würfelt. Die
Bauregel-Gegenprobe hat zwei solche Widersprüche gefunden und aufgelöst
(`docs/gegenprobe-bauregel.md`) — diesen nicht, weil er erst entsteht, wenn
beide Regeln im selben Fall greifen. Eine Strukturprüfung sieht zwei saubere
Punkte; erst der Lauf sieht die Kollision.

**Korrektur im Skill** (kein Testfall angefasst): Der Vorrang steht jetzt
ausdrücklich an beiden Stellen. Die Kein-Text-Regel gilt weiter — mit einer
einzigen, benannten Ausnahme: nach gehörter Empfehlung und ausdrücklichem
Bestehen entsteht der Text. Dazu ein neuer Checklistenpunkt, der die höfliche
Variante ausschließt: Auf eine ausdrückliche Ansage folgt der Text, keine
Gegenfrage.

**Folge für den Umfang:** Alle drei `follow-up-generator`-Fälle laufen komplett
neu, auch `01` und `02`, die vorher 3 von 3 hatten. Ihre Läufe gegen die alte
Fassung sind beiseitegelegt und zählen nicht mehr.

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
