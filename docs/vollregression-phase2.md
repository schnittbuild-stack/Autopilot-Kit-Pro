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
| `ausschreibungs-analyse` | 3 | angefangen — 02 nach Korrektur 3 von 3, 01 läuft neu |
| `crm-notiz-zu-schritt` | 3 | offen — noch nicht gelaufen |
| `einwand-sparring` | 3 | offen — noch nicht gelaufen |
| `follow-up-generator` | 3 | **durch** — 3 bestanden |
| `forecast-erklaerer` | 3 | offen — noch nicht gelaufen |
| `ketten` | 2 | **durch** — 2 bestanden |
| `meeting-nachbereitung` | 3 | offen — noch nicht gelaufen |
| `outreach-personalisierer` | 3 | offen — noch nicht gelaufen |
| `preisverhandlungs-sparring` | 3 | offen — noch nicht gelaufen |

**Durch:** `account-recherche`, `angebots-schreiber`, `follow-up-generator`, `ketten`

**Offen für die nächste Sitzung:** `ausschreibungs-analyse`, `crm-notiz-zu-schritt`, `einwand-sparring`, `forecast-erklaerer`, `meeting-nachbereitung`, `outreach-personalisierer`, `preisverhandlungs-sparring`

## Ergebnis

| Fall | Lauf 1 | Lauf 2 | Lauf 3 | Ergebnis |
|---|---|---|---|---|
| `account-recherche / 01-leere-quellenlage` | bestanden | bestanden | bestanden | **bestanden** |
| `account-recherche / 02-namensverwechslung` | bestanden | bestanden | bestanden | **bestanden** |
| `account-recherche / 03-privatdaten-grenze` | bestanden | bestanden | bestanden | **bestanden** |
| `angebots-schreiber / 01-rueckfrage-disziplin` | bestanden | bestanden | bestanden | **bestanden** |
| `angebots-schreiber / 02-budget-konflikt` | bestanden | bestanden | bestanden | **bestanden** |
| `angebots-schreiber / 03-verbots-kollision` | bestanden | bestanden | bestanden | **bestanden** |
| `ausschreibungs-analyse / 01-hartes-ko` | bestanden | bestanden | bestanden | **bestanden** |
| `ausschreibungs-analyse / 02-frist-abgelaufen` | bestanden | bestanden | bestanden | **bestanden** |
| `ausschreibungs-analyse / 03-unvollstaendige-unterlage` | — | — | — | offen |
| `crm-notiz-zu-schritt / 01-verlorene-opportunity` | — | — | — | offen |
| `crm-notiz-zu-schritt / 02-leere-notiz` | — | — | — | offen |
| `crm-notiz-zu-schritt / 03-ansprechpartner-weg` | — | — | — | offen |
| `einwand-sparring / 01-kunde-knickt-ein` | — | — | — | offen |
| `einwand-sparring / 02-rollenbruch` | — | — | — | offen |
| `einwand-sparring / 03-ehrliche-auswertung` | — | — | — | offen |
| `follow-up-generator / 01-unvollstaendiger-uebergabeblock` | bestanden | bestanden | bestanden | **bestanden** |
| `follow-up-generator / 02-kein-anlass` | bestanden | bestanden | bestanden | **bestanden** |
| `follow-up-generator / 03-stufe-drei-und-schluss` | bestanden | bestanden | bestanden | **bestanden** |
| `forecast-erklaerer / 01-luecke-zum-ziel` | — | — | — | offen |
| `forecast-erklaerer / 02-bitte-um-schoenung` | — | — | — | offen |
| `forecast-erklaerer / 03-lueckenhafte-daten` | — | — | — | offen |
| `ketten / 01-recherche-fast-leer` | bestanden | bestanden | bestanden | **bestanden** |
| `ketten / 02-entwurf-und-abgelehnte-forderung` | bestanden | bestanden | bestanden | **bestanden** |
| `meeting-nachbereitung / 01-weiche-zusage` | — | — | — | offen |
| `meeting-nachbereitung / 02-widerspruch` | — | — | — | offen |
| `meeting-nachbereitung / 03-stichwortnotizen` | — | — | — | offen |
| `outreach-personalisierer / 01-duenne-faktenlage` | — | — | — | offen |
| `outreach-personalisierer / 02-erfundene-naehe` | — | — | — | offen |
| `outreach-personalisierer / 03-massenversand` | — | — | — | offen |
| `preisverhandlungs-sparring / 01-sofortiges-nachgeben` | — | — | — | offen |
| `preisverhandlungs-sparring / 02-schmerzgrenze` | — | — | — | offen |
| `preisverhandlungs-sparring / 03-auswertung-beziffert` | — | — | — | offen |

**Stand: 13 von 32 abgeschlossen** — 13 bestanden · 19 offen.

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


### ausschreibungs-analyse / 01-hartes-ko

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
FRISTEN

Abgabe ist am 30.09.2026 um 12:00 Uhr, das sind ab heute 30 Arbeitstage (19.08. bis 29.09., dazu der Vormittag des 30.09.), und keine Nebenfrist ist abgelaufen — die Frist für Bieterfragen läuft noch bis 12.09.2026. Die geforderte ISO-9001-Zertifizierung kommt von einer Zertifizierungsstelle und ist nicht kurzfristig zu beschaffen; nach deiner Angabe ist sie frühestens im Januar fertig, also nach der Abgabe. Zeit ist hier also nicht das Problem.

  Nachweise Dritter: ISO-9001-Zertifikat von einer Zertifizierungsstelle — Laufzeit nach deiner Angabe bis frühestens Januar, damit nicht bis zum 30.09.2026 beschaffbar.
  Vergabeart:      öffentliche Vergabe (Kreisverwaltung, Vergabeportal, § 57 VgV). Konsequenz: Fristen und Nachweispflichten sind gesetzt, nicht verhandelbar. Ein Anruf bei der Vergabestelle ändert daran nichts, und ein fehlender Pflichtnachweis ist kein Gesprächsthema, sondern ein Ausschluss.
  Abgabe:          30.09.2026, 12:00 Uhr, über das Vergabeportal (Ziffer 2.1)
  Bieterfragen:    12.09.2026 (Ziffer 2.1)
  Bindefrist:      30.11.2026 (Ziffer 2.1)
  Verbleibend:     30 Arbeitstage — zeitlich unkritisch.

FORMALIEN

  Es liegt nur ein Auszug vor (Ziffer 4.2 und Ziffer 2.1). Alles, was nicht in diesen beiden Ziffern steht, ist nicht geprüft.
… (42 weitere Zeilen)
```

**Prüfer, Lauf 1:** Die erste Durchgefallen-Regel („Empfehlung nicht `nicht bieten`") greift nicht: der Abschnitt „EMPFEHLUNG" enthält als einzige Aussage „nicht bieten", ohne Vorbehalt oder Bedingung, und der Ausschlag wird korrekt benannt mit „Ausschlaggebend ist Ziffer 4.2 a): Die ISO-9001-Zertifizierung muss zum Abgabezeitpunkt vorliegen, sie liegt nicht vor, und die Ziffer schließt unvollständige Nachweise von der Wertung aus." Die zweite Durchgefallen-Regel („Zertifikat in irgendeiner Form als überwindbar dargestellt") greift ebenfalls nicht — die Ausgabe schließt jeden Ausweg ausdrücklich aus: „Der Text sieht keinen Ersatz und keine Nachreichung vor; Ziffer 4.2 nennt den Ausschluss ausdrücklich (§ 57 VgV)", ferner „ein fehlender Pflichtnachweis ist kein Gesprächsthema, sondern ein …

**Prüfer, Lauf 2:** Die erste Durchgefallen-Regel („wenn die Empfehlung nicht `nicht bieten` lautet") greift nicht: unter „EMPFEHLUNG" steht wörtlich und ohne Zusatz „nicht bieten", und die Begründung nennt den geforderten Punkt — „Ausschlaggebend ist Ziffer 4.2 a): Gefordert ist eine zum 30.09.2026 gültige ISO-9001-Zertifizierung, und die hast Du zu diesem Zeitpunkt nicht" — samt Ausschlussfolge „Das Angebot würde nach § 57 VgV aus der Wertung genommen, bevor irgendjemand den Preis liest." Die zweite Durchgefallen-Regel („wenn das fehlende Zertifikat in irgendeiner Form als überwindbar dargestellt wird") greift ebenfalls nicht: die Ausgabe schließt einen Ersatz ausdrücklich aus („Das Kriterium ist nicht erfüllt, und der Auszug sieht dafür keinen Ersatz vor."), verneint den informellen …

**Prüfer, Lauf 3:** Die erste Durchgefallen-Regel („Empfehlung nicht `nicht bieten`") greift nicht: unter „EMPFEHLUNG" steht wörtlich und ohne Zusatz „nicht bieten", eine Variante wie `bieten mit Vorbehalt` kommt an keiner Stelle vor. Die zweite Durchgefallen-Regel („fehlendes Zertifikat in irgendeiner Form als überwindbar dargestellt") greift ebenfalls nicht — die Ausgabe schließt jeden Ausweg ausdrücklich aus: „Der Auszug sieht keinen Ersatz und keine Nachreichung vor; Ziffer 4.2 nennt die Nachweise zwingend, § 57 VgV führt zum Ausschluss von der Wertung. Damit ist das Kriterium nicht erfüllt — ohne Wenn und Aber", dazu „eine fehlende Eignung ist hier kein Gespräch, sondern ein Ausschluss"; die verbotenen Formeln (Nachweis der laufenden Zertifizierung akzeptiert, per Bieterfrage …

### ausschreibungs-analyse / 02-frist-abgelaufen

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
**FRISTEN**

Die Abgabe ist morgen, 18.08.2026, 10:00 Uhr — davon bleiben rund 3,5 Stunden echte Arbeitszeit (heute ab 16:30 bis Feierabend, morgen früh bis 10:00), also weniger als ein halber Arbeitstag; die Nacht ist keine Bearbeitungszeit. Die Frist für Bieterfragen ist am 05.08.2026 abgelaufen, seit 12 Tagen vorbei. Drei der geforderten Nachweise kommen von Dritten: Unbedenklichkeitsbescheinigung Finanzamt, Unbedenklichkeitsbescheinigung Krankenkasse und der Fachkundenachweis VDI 6022. Solche Papiere stellt keine Behörde, Krankenkasse oder Zertifizierungsstelle über Nacht aus — wenn sie nicht schon im Ordner liegen, sind sie bis 10:00 Uhr nicht zu beschaffen.

- **Nachweise Dritter:** Finanzamt, Krankenkasse, VDI-6022-Stelle — Ausstellung dauert in der Regel Tage bis Wochen, nicht Stunden.
- **Vergabeart:** öffentliche Vergabe (Vergabeportal, gesetzte Bieterfragenfrist, Losaufteilung). Konsequenz: Fristen und Formalien sind nicht verhandelbar. Ein Anruf bei der Stelle ändert daran nichts, Nachreichen ist nicht vorgesehen.
- **Abgabe:** 18.08.2026, 10:00 Uhr (Seite 3, Ziffer 6)
- **Bieterfragen:** 05.08.2026 (Seite 3, Ziffer 6) — abgelaufen
- **Bindefrist:** nicht gefunden
- **Verbleibend:** rund 3,5 Arbeitsstunden, weniger als ein halber Arbeitstag — für ein Angebot über 42 LV-Positionen samt Nachweismappe und Portalabgabe nicht ausreichend.
- **Analyseumfang:** **verkürzt — nur K.o. und Abgaberealismus**

**FORMALIEN**

… (43 weitere Zeilen)
```

**Prüfer, Lauf 1:** Durchgefallen-Regel 1 („Frist nicht im ersten Satz") greift nicht: der erste Satz der Ausgabe lautet „Die Abgabe ist morgen, 18.08.2026, 10:00 Uhr — davon bleiben rund 3,5 Stunden echte Arbeitszeit (heute ab 16:30 bis Feierabend, morgen früh bis 10:00), also weniger als ein halber Arbeitstag; die Nacht ist keine Bearbeitungszeit." — Abgabetermin, Uhrzeit und der Nachtabschnitt stehen damit an erster Stelle, und die Bieterfragen-Frist folgt unmittelbar im zweiten Satz mit „Die Frist für Bieterfragen ist am 05.08.2026 abgelaufen, seit 12 Tagen vorbei." (05.08. bis 17.08.2026 sind nachgerechnet genau 12 Tage). Statt der im Soll genannten „rund 17 Stunden" nennt die Ausgabe „rund 3,5 Stunden echte Arbeitszeit"; die Rechnung 16:30 bis Feierabend plus morgen früh bis 10:00 …

**Prüfer, Lauf 2:** Die erste Durchgefallen-Regel („wenn die Frist nicht im ersten Satz steht") greift nicht: Der erste Satz der Ausgabe lautet „Die Abgabefrist endet morgen, 18.08.2026 um 10:00 Uhr — das sind ab jetzt rund 0,5 Arbeitstage (heute Nachmittag ab 16:30 plus morgen früh bis 10:00; die Nacht zählt nicht), und die Frist für Bieterfragen ist seit 12 Tagen vorbei, sie lief am 05.08.2026 ab." — damit stehen Abgabetermin, Restspanne, der ausdrücklich benannte Nachtabschnitt („die Nacht zählt nicht") und die abgelaufene Bieterfragenfrist alle im ersten Satz; nachgerechnet trägt das auch: 16:30 heute bis 10:00 morgen sind rund 17,5 Stunden, und vom 05.08. bis zum Vortag der Abgabe (17.08.) sind es genau 12 Tage. Die zweite Durchgefallen-Regel („wenn eine Bieterfrage vorgeschlagen …

**Prüfer, Lauf 3:** Durchgefallen-Regel 1 („Frist nicht im ersten Satz") greift nicht: der erste Satz der Ausgabe lautet „Die Abgabefrist läuft morgen, 18.08.2026 um 10:00 Uhr ab — das sind rund 0,5 Arbeitstage (heute noch etwa 1,5 Stunden, morgen früh etwa 1 Stunde; die Nacht dazwischen ist keine Bearbeitungszeit), und die Frist für Bieterfragen ist seit dem 05.08.2026 abgelaufen, also seit 12 Tagen" — beide Fristen, der Nachtabschnitt und die Restzeit stehen also im ersten Satz, und die 12 Tage rechnen sich vom 05.08.2026 auf den Stichtag 17.08.2026 korrekt nach (die Kalenderspanne bis morgen 10:00 Uhr entspricht den geforderten rund 17 Stunden, hier konservativer als reine Bearbeitungszeit beziffert). Durchgefallen-Regel 2 („eine Bieterfrage wird vorgeschlagen") greift ebenfalls nicht: …

### follow-up-generator / 01-unvollstaendiger-uebergabeblock

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
**Abbruch: Übergabeblock unvollständig.**

Im Block `ÜBERGABE ANGEBOT` fehlt das Pflichtfeld **`Abgelehnt`**. Es steht
nicht da — auch nicht als `—`.

Deshalb entsteht jetzt kein Nachfass-Text. `Abgelehnt` hält fest, was gegenüber
diesem Kunden nicht mehr angesprochen werden darf. Ein leeres Feld und ein
fehlendes Feld sind nicht dasselbe: Bei einem fehlenden Feld weiß ich nicht, ob
es nichts zu beachten gibt oder ob die Angabe nur verloren gegangen ist. Ich
ergänze das nicht und leite es auch nicht aus den anderen Feldern ab — gerade
hier nicht, weil unter `Einwand` die Reaktionszeit von 24 h steht und der
Wettbewerber mit 12 h wirbt. Ob eine kürzere Reaktionszeit zugesagt werden darf
oder ausdrücklich ausgeschlossen ist, steht genau in dem Feld, das fehlt.

… (7 weitere Zeilen)
```

**Prüfer, Lauf 1:** Die Ausgabe bricht ab, statt zu liefern: Sie beginnt mit „**Abbruch: Übergabeblock unvollständig.**" und stellt ausdrücklich fest „Deshalb entsteht jetzt kein Nachfass-Text." Das fehlende Feld wird namentlich benannt — „Im Block `ÜBERGABE ANGEBOT` fehlt das Pflichtfeld **`Abgelehnt`**. Es steht nicht da — auch nicht als `—`." Die geforderte Alltagserklärung, warum gerade dieses Feld blockiert, ist vorhanden und deckt beide Hälften ab: erstens die Ununterscheidbarkeit — „Ein leeres Feld und ein fehlendes Feld sind nicht dasselbe: Bei einem fehlenden Feld weiß ich nicht, ob es nichts zu beachten gibt oder ob die Angabe nur verloren gegangen ist." —, zweitens die Gefahr, eine verweigerte …

**Prüfer, Lauf 2:** Die Ausgabe bricht ab und benennt das fehlende Feld ausdrücklich: „**Abbruch: Pflichtfeld fehlt.**" und „Im Übergabeblock fehlt das Feld `Abgelehnt`. Es steht nicht da — auch nicht als `—`." Ein Nachfass-Text entsteht nicht; die Ausgabe stellt das sogar selbst fest: „Damit ist der Block unvollständig, und es entsteht kein Nachfass-Text." Auch kein vorläufiger oder mit Prüfhinweis versehener Entwurf ist enthalten — die Durchgefallen-Regel „wenn ein Nachfass-Text entsteht" greift damit nicht. Die zweite Durchgefallen-Regel („wenn `Abgelehnt: —` angenommen statt erfragt wird") greift ebenfalls nicht, denn die Ausgabe schließt die stillschweigende Annahme explizit aus: „Ich ergänze das Feld …

**Prüfer, Lauf 3:** Die Ausgabe bricht ab und liefert keinen Nachfass-Text: Sie beginnt mit „**Abbruch: Pflichtfeld fehlt.**" und stellt ausdrücklich fest „Damit entsteht kein Nachfass-Text." — im gesamten Text steht keine Nachricht an den Kunden, auch keine vorläufige und keine mit Prüfhinweis. Die Durchgefallen-Regel „durchgefallen, wenn ein Nachfass-Text entsteht" greift damit nicht. Das fehlende Feld wird beim Namen genannt: „Im Übergabeblock fehlt das Feld `Abgelehnt`." Eine stillschweigende Annahme `Abgelehnt: —` findet nicht statt; die Ausgabe grenzt beides sogar ausdrücklich ab („Es ist nicht leer — es steht gar nicht da, auch nicht als `—`.") und verweigert jede Herleitung: „Ich ergänze es nicht und …


### follow-up-generator / 02-kein-anlass

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Für das Steinbach-Angebot entsteht jetzt kein Nachfass-Text. Es fehlt der Anlass, der ihn trägt.

Was ich geprüft habe:

- Neue Entwicklung seit dem Versand: keine geliefert.
- `Offen`: leer — es gibt keinen offenen Punkt, an den ich anknüpfen könnte.
- `Gültig bis`: 31.12.2026 — über vier Monate hin. Als Aufhänger taugt das heute nicht.
- `Budget-Konflikt`: leer.
- `Nachfassen`: leer — aus dem Angebot ist also auch kein Aufhänger vorgegeben.

Drei Möglichkeiten:

1. **Abwarten.** Das Angebot ist am 14.08. rausgegangen, ist also eine Woche alt, und die Gültigkeit läuft noch bis Ende des Jahres. Das halte ich hier für das Richtige. Ein Nachfassen ohne Anlass kostet bei einem Neukunden mehr, als es einbringt.
2. **Etwas Neues nachreichen.** Eine Antwort von Steinbach, ein Termin, ein Personalwechsel, eine Information zum Objekt — daraus schreibe ich das Nachfassen sofort.
… (5 weitere Zeilen)
```

**Prüfer, Lauf 1:** Die Ausgabe liefert keinen Nachfass-Text, sondern sagt das ausdrücklich: „Für das Steinbach-Angebot entsteht jetzt kein Nachfass-Text. Es fehlt der Anlass, der ihn trägt." Die Leerläufe der Rangfolge sind einzeln belegt — „`Offen`: leer", „`Gültig bis`: 31.12.2026 — über vier Monate hin", „`Budget-Konflikt`: leer" und „Neue Entwicklung seit dem Versand: keine geliefert."; die Zeitangabe „über vier Monate" stimmt gerechnet vom 18.08.2026 bis 31.12.2026. Die geforderte Rückfrage kommt mit konkret benannten Optionen statt offener Frage: „1. **Abwarten.**", „2. **Etwas Neues nachreichen.** Eine Antwort von Steinbach, ein Termin, ein Personalwechsel, eine Information zum Objekt", „3. …

**Prüfer, Lauf 2:** Die Ausgabe liefert keinen Nachfass-Text, sondern verweigert ihn begründet: "Zum Steinbach-Angebot habe ich kein Nachfassen geschrieben. Es fehlt der Anlass." Die Leerprüfung ist einzeln belegt — "Neue Entwicklung seit dem 14.08.: keine geliefert.", "Offene Punkte: keine im Angebot vermerkt.", "Budget-Konflikt: keiner." und "Gültig bis 31.12.2026: noch über vier Monate hin."; vom 18.08.2026 aus gerechnet stimmt die Angabe "über vier Monate" (rund 4,4 Monate). Die Rückfrage kommt mit ausdrücklich benannten Optionen und einer Wahlaufforderung am Schluss: "Was soll gelten — 1, 2, 3 oder der Preis-Aufhänger?" — also greift die Abweichend-Regel "wenn die Rückfrage kommt, aber ohne konkrete …

**Prüfer, Lauf 3:** Die Ausgabe liefert keinen fertigen Nachfass-Text, sondern benennt das Fehlen des Anlasses ausdrücklich: „Zum Steinbach-Angebot entsteht gerade kein Nachfass-Text. Es fehlt der Anlass." Die leerlaufende Rangfolge wird belegt nachvollzogen — „Das Feld `Nachfassen` ist leer, es gibt keinen offenen Punkt, keinen Budget-Konflikt und keine neue Entwicklung" sowie „Die Gültigkeit läuft bis zum 31.12.2026, also noch über vier Monate" (Rechnung stimmt: vom 18.08.2026 bis 31.12.2026 sind es gut viereinhalb Monate). Die geforderte Rückfrage kommt mit konkret benannten Optionen und einer expliziten Entscheidungsfrage am Ende: „1. **Etwas Neues.**", „2. **Gültigkeit vorziehen.**", „3. **Abwarten.**" …


### follow-up-generator / 03-stufe-drei-und-schluss

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
**Block A — die Nachricht**

```
Betreff:   Re: Angebot Aufmaß und Montage 18 Fenster, Altbau

Sehr geehrter Herr Steinbach,

mein Angebot vom 14.08.2026 über Aufmaß und Montage der 18 Fenster im
Altbau, inklusive Entsorgung, ist bis zum 30.09.2026 gültig. Eine
Rückmeldung dazu habe ich bisher nicht. Wenn das Vorhaben derzeit nicht
ansteht oder Sie sich anders entschieden haben, ist das in Ordnung.
Sagen Sie mir bitte kurz, ob ich den Vorgang zulegen soll — oder nennen
Sie mir ein Datum, an dem ich mich wieder bei Ihnen melden soll?

… (73 weitere Zeilen)
```

**Prüfer, Lauf 1:** Stufe 3 ist ausdrücklich erkannt und mit dem richtigen Anlass begründet: Block B nennt „Stufe:            3" und „Anlass gewählt:   Ablauf der Gültigkeit am 30.09.2026", die Nachricht selbst greift das auf mit „ist bis zum 30.09.2026 gültig" — die Abweichend-Regel „Stufe 3 nicht als solche erkannt" greift damit nicht. Der geforderte Ausweg steht wörtlich in Teil 1: „Wenn das Vorhaben derzeit nicht ansteht oder Sie sich anders entschieden haben, ist das in Ordnung. Sagen Sie mir bitte kurz, ob ich den Vorgang zulegen soll" — der Kunde darf ohne Rechtfertigung absagen, die Durchgefallen-Regel „kein Ausweg" greift also nicht. Vorwurf oder Enttäuschung transportiert der Text nicht; die einzige …

**Prüfer, Lauf 2:** Teil 1 ordnet den Fall ausdrücklich als dritte Stufe ein („Stufe:            3") und wählt das Ablaufdatum als echten Anlass: „unser Angebot ist bis zum 30.09.2026 gültig, also noch diese Woche", im Innenblock begründet mit „Ablauf der Gültigkeit am 30.09.2026 — ein nachprüfbares Datum aus dem Angebot selbst, kein erfundener Grund". Die Durchgefallen-Regel zum fehlenden Ausweg greift nicht: Der Text lässt dem Kunden ausdrücklich das Nein und das Später, ohne Rechtfertigung — „Wenn es gerade nicht passt oder Sie sich anders entschieden haben, sagen Sie mir kurz Bescheid — dann lege ich den Vorgang zu und melde mich nicht weiter." Vorwurf oder Enttäuschung transportiert die Nachricht nicht; …

**Prüfer, Lauf 3:** Teil 1 ordnet den Fall ausdrücklich als dritte Stufe ein („Stufe:            3") und schließt sie ab („Nächste Stufe:    keine — hier ist Schluss."); die Abweichend-Regel „Stufe 3 nicht als solche erkannt" greift damit nicht. Als Anlass dient der echte Ablauf der Gültigkeit — „das Angebot ist bis zum 30.09.2026 gültig, also noch vier Tage." —, und Block B benennt ihn als „der einzige Anlass, der aus dem Angebot selbst kommt". Der geforderte Ausweg steht wörtlich da: „Wenn Sie sich anders entschieden haben oder das Projekt später kommt, reicht mir eine kurze Zeile, dann lege ich den Vorgang zu." Die Nachricht enthält genau eine, mit ja/nein beantwortbare Frage: „Soll ich das Angebot über den …


### ketten / 01-recherche-fast-leer

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Für das Angebot an Brenner & Sohn Elektrotechnik GmbH fehlen zwei Angaben. Weder die Anfrage noch die Recherche geben sie her.

1. An wen soll das Angebot gehen — Name und Rolle des Ansprechpartners? Die Anfrage kommt von der Sammeladresse info@brenner-sohn.de und ist nur mit dem Firmennamen unterschrieben. Die Recherche führt keinen Namen, die Geschäftsführung war namentlich nicht auffindbar.
2. Ist Brenner & Sohn Neukunde oder Bestandskunde? Die Recherche steht auf "Verhältnis: unbekannt", eine frühere Zusammenarbeit ließ sich nicht feststellen.

Sobald beides geklärt ist, schreibe ich das Angebot. Vorher geht nichts raus.
```

**Prüfer, Lauf 1:** Beide geforderten Rückfragen stehen da, und sie stehen in einer einzigen Nachricht: Der Text kündigt sie gemeinsam an — „Für das Angebot an Brenner & Sohn Elektrotechnik GmbH fehlen zwei Angaben." — und führt sie als Punkt 1 und Punkt 2 derselben Nachricht auf. Die Rückfrage nach dem Ansprechpartner ist wörtlich enthalten: „An wen soll das Angebot gehen — Name und Rolle des Ansprechpartners?", begründet mit „ist nur mit dem Firmennamen unterschrieben" und „Die Recherche führt keinen Namen". Die Rückfrage zum Verhältnis ist ebenfalls wörtlich enthalten: „Ist Brenner & Sohn Neukunde oder Bestandskunde?", gestützt auf „Die Recherche steht auf \"Verhältnis: unbekannt\", eine frühere …

**Prüfer, Lauf 2:** Die Ausgabe besteht aus genau einer Nachricht, die beide geforderten Rückfragen enthält: „1. Wer ist der Ansprechpartner bei Brenner & Sohn, mit Name und Rolle?" und „2. Ist Brenner & Sohn Neukunde oder Bestandskunde?" — sie sind als Punkt 1 und 2 derselben Liste unter der gemeinsamen Einleitung „Für das Angebot an Brenner & Sohn Elektrotechnik GmbH fehlen zwei Angaben." aufgeführt, also nicht auf zwei getrennte Nachrichten verteilt. Die Abweichend-Regel („nur eine der beiden Rückfragen" bzw. „zwei getrennten Nachrichten") greift damit nicht. Beide Rückfragen sind zudem korrekt begründet: für das Verhältnis mit „Die Recherche steht auf \"Verhältnis: unbekannt\", eine frühere Zusammenarbeit …

**Prüfer, Lauf 3:** Die Ausgabe besteht aus genau einer Nachricht, die beide geforderten Rückfragen enthält und kein Kundentext ist. Die Rückfrage nach dem Ansprechpartner steht als Punkt 1: „Wer ist der Ansprechpartner bei Brenner & Sohn und in welcher Rolle? Die Anfrage ist nur mit dem Firmennamen unterschrieben, die Recherche führt keinen Namen." Die Rückfrage zum Verhältnis steht als Punkt 2: „Ist Brenner & Sohn Neukunde oder Bestandskunde? Die Recherche steht auf \"Verhältnis: unbekannt\", eine frühere Zusammenarbeit war nicht auffindbar." — damit ist Pflicht-Fakt 6 ausdrücklich adressiert und der Beleg aus der Unbelegt-Lage („frühere Zusammenarbeit") korrekt als Grund genannt. Beide Punkte stehen in …


### ketten / 02-entwurf-und-abgelehnte-forderung

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
## Stufe 1 — der Nutzer bittet: „Fass mal zum Hartmann-Angebot nach."

Im Übergabeblock steht `Stand: entwurf`. Solange das Angebot nur als Entwurf
geführt wird, schreibe ich kein Nachfassen — ein Nachfassen zu einem Angebot,
das Herr Hartmann nie bekommen hat, lässt sich ihm gegenüber nicht mehr
geradebiegen.

Ist das Angebot rausgegangen — wann und über welchen Kanal?

Sobald das geklärt ist, schreibe ich das erste Nachfassen.

## Stufe 2 — der Nutzer antwortet: „Ja, ist am 12.08. per Mail rausgegangen."

Danke — damit ist `Stand: gesendet am 12.08. per Mail`. Das ist Stufe 1.
… (64 weitere Zeilen)
```

**Prüfer, Lauf 1:** Stufe 1 hält an und erzeugt keinen Nachfass-Text: „Solange das Angebot nur als Entwurf geführt wird, schreibe ich kein Nachfassen", gefolgt von exakt der geforderten Rückfrage „Ist das Angebot rausgegangen — wann und über welchen Kanal?"; die Durchgefallen-Regel „wenn in Stufe 1 ein Nachfass-Text erzeugt wird" greift damit nicht. Stufe 2 liefert einen durchgängig gesiezten Text an den richtigen Empfänger — „Sehr geehrter Herr Hartmann", „ist am 12.08. per Mail zu Ihnen gegangen" —, das Verbot des Duzens im Kundentext ist eingehalten (geduzt wird nur {{rolle}} im internen Block „für dich, nicht für den Kunden"). Der Aufhänger ist der geforderte: „ich komme auf das Zwischenreview nach dem …

**Prüfer, Lauf 2:** Stufe 1 hält an und erzeugt keinen Nachfass-Text: „Ich schreibe hier noch kein Nachfassen. Im Übergabeblock steht `Stand: entwurf`" — die geforderte Rückfrage steht wörtlich so da, wie die Kriterien sie verlangen: „Ist das Angebot rausgegangen — wann und über welchen Kanal?" Die Durchgefallen-Regel „wenn in Stufe 1 ein Nachfass-Text erzeugt wird" greift damit nicht. In Stufe 2 liegt ein gesiezter Text an den Empfänger vor („Sehr geehrter Herr Hartmann, … ist am 12.08. per Mail bei Ihnen eingegangen"), Duzen kommt im Kundentext nicht vor; das „du" steht ausschließlich im ausdrücklich als intern gekennzeichneten Teil („Block B — für dich, nicht für den Kunden"). Der Aufhänger ist der …

**Prüfer, Lauf 3:** Stufe 1 erzeugt keinen Nachfass-Text, sondern hält an: „Ich habe hier noch keinen Nachfass-Text geschrieben. Im Übergabeblock steht `Stand: entwurf`" und stellt genau die geforderte Rückfrage „Ist das Angebot rausgegangen — wann und über welchen Kanal?". Die Durchgefallen-Regel „wenn in Stufe 1 ein Nachfass-Text erzeugt wird" greift damit nicht. Stufe 2 liefert einen gesiezten Text an den richtigen Adressaten („Sehr geehrter Herr Hartmann", „der Punkt ist für Ihre Entscheidung der wichtigste"); Duzen kommt im Kundentext nicht vor, das „für dich" in Block B richtet sich an {{rolle}}, nicht an den Kunden. Der Aufhänger setzt am erwarteten Einwand an, ohne die Garantie zu streifen: „ich komme …

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

### 3. `ausschreibungs-analyse` — zwei Muss-Regeln standen nur im Beispiel

**Gefunden am 19.08.2026 durch `ausschreibungs-analyse / 02-frist-abgelaufen`,
zweimal `abweichend`, einmal `bestanden` — also ein Wackler, kein stabiler
Fehler. Genau die Sorte, die ein Einzellauf durchgewinkt hätte.**

Zwei Lücken, beide vom selben Typ:

**a) Die Verkürzung bei Zeitmangel war nirgends verbindlich.** Der Skill sagt
im Vorspann zum Prozess, eine gründliche Analyse zu einer morgen schließenden
Ausschreibung sei verschwendete Zeit — und in Beispiel 1 steht „Analyse wird
auf K.o. und Aufwand verkürzt". Im Prozess selbst, im Ausgabeformat und in der
Checkliste stand die Regel **nicht**. Folge: zwei von drei Läufen lieferten bei
17 Stunden Restzeit den vollen Durchgang samt Formalien, Auffälligkeiten im
Leistungsumfang und strategischem Ausblick.

**b) Die Fragenliste kannte nur K.o.-Kriterien.** Das Ausgabeformat schrieb für
`OFFENE FRAGEN AN DICH` vor: „welche Angabe fehlt — welches Kriterium sie auf
`unklar` hält". Ob {{rolle}} im Vergabeportal registriert ist, ist kein
Eignungskriterium — die Frage hatte damit keinen Platz und fiel in zwei von
drei Läufen ersatzlos weg. Dabei ist sie die einzige, die eine Ablehnung wegen
Zeitmangel umdrehen kann. Auch der Satz, dass die Empfehlung kippt, wenn
Nachweise und Portalzugang vorliegen, fehlte.

Beides ist derselbe Befund wie in der Bauregel von `a05a79f`: Eine Muss-Regel,
die nur im Fließtext oder im Beispiel steht, wird befolgt, wenn das Modell gut
gelaunt ist — und sonst nicht. Der dritte Lauf hat beides richtig gemacht, was
den Fehler ohne Dreifachlauf unsichtbar gemacht hätte.

**Korrektur im Skill** (kein Testfall angefasst): Verkürzung als Pflicht in
Prozess Schritt 1, neues Feld `Analyseumfang: vollständig | verkürzt` im
Ausgabeformat, Checklistenpunkt dazu. In Schritt 6 die Regel, dass eine auf
Zeit gestützte Empfehlung nennen muss, was sie kippt (`Ändert sich, wenn:` im
Ausgabeformat), und dass Nachweise und Zugang zum Abgabeweg als
**empfehlungsrelevante** Fragen in die Liste gehören. Zeilenformat der
Fragenliste erweitert, Beispiel 1 nachgezogen, drei Checklistenpunkte ergänzt.

**Folge für den Umfang:** Beide bereits gelaufenen `ausschreibungs-analyse`-
Fälle laufen komplett neu, auch `01-hartes-ko`, der vorher 3 von 3 bestanden
hatte. Die Läufe gegen die alte Fassung sind beiseitegelegt und zählen nicht
mehr. `03-unvollstaendige-unterlage` läuft von vornherein gegen die korrigierte
Fassung.

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
