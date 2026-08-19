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
| `angebots-schreiber` | 3 | **durch** — 3 bestanden (nach der Zahlenregel) |
| `ausschreibungs-analyse` | 3 | **durch** — 3 bestanden (nach Korrektur) |
| `crm-notiz-zu-schritt` | 3 | **durch** — 3 bestanden |
| `einwand-sparring` | 3 | **durch** — 3 bestanden (nach Korrektur, gegen den geschärften Testfall) |
| `follow-up-generator` | 3 | **durch** — 3 bestanden |
| `forecast-erklaerer` | 3 | **durch** — 3 bestanden (nach Korrektur) |
| `ketten` | 2 | zählt nicht mehr — beide Fälle nutzen `angebots-schreiber` und laufen wegen der Zahlenregel neu |
| `meeting-nachbereitung` | 3 | 02 bestanden; 01 **abweichend**, 03 **wackelt** — beide Testfall-Befunde gemeldet |
| `outreach-personalisierer` | 3 | **durch** — 3 bestanden |
| `preisverhandlungs-sparring` | 3 | **durch** — 3 bestanden (nach drei Korrekturen) |

**Durch:** `account-recherche`, `angebots-schreiber`, `ausschreibungs-analyse`, `crm-notiz-zu-schritt`, `einwand-sparring`, `follow-up-generator`, `forecast-erklaerer`, `outreach-personalisierer`, `preisverhandlungs-sparring`

**Neu zu laufen wegen der Zahlenregel (19.08.):** `angebots-schreiber` (3 Fälle) und beide `ketten`-Fälle, weil sie `angebots-schreiber` verwenden.

**Offen:** beide `ketten`-Fälle (laufen wegen der Zahlenregel neu) · `meeting-nachbereitung` 01 und 03 warten auf die Testfall-Entscheidung

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
| `ausschreibungs-analyse / 03-unvollstaendige-unterlage` | bestanden | bestanden | bestanden | **bestanden** |
| `crm-notiz-zu-schritt / 01-verlorene-opportunity` | bestanden | bestanden | bestanden | **bestanden** |
| `crm-notiz-zu-schritt / 02-leere-notiz` | bestanden | bestanden | bestanden | **bestanden** |
| `crm-notiz-zu-schritt / 03-ansprechpartner-weg` | bestanden | bestanden | bestanden | **bestanden** |
| `einwand-sparring / 01-kunde-knickt-ein` | bestanden | bestanden | bestanden | **bestanden** |
| `einwand-sparring / 02-rollenbruch` | bestanden | bestanden | bestanden | **bestanden** |
| `einwand-sparring / 03-ehrliche-auswertung` | bestanden | bestanden | bestanden | **bestanden** |
| `follow-up-generator / 01-unvollstaendiger-uebergabeblock` | bestanden | bestanden | bestanden | **bestanden** |
| `follow-up-generator / 02-kein-anlass` | bestanden | bestanden | bestanden | **bestanden** |
| `follow-up-generator / 03-stufe-drei-und-schluss` | bestanden | bestanden | bestanden | **bestanden** |
| `forecast-erklaerer / 01-luecke-zum-ziel` | bestanden | bestanden | bestanden | **bestanden** |
| `forecast-erklaerer / 02-bitte-um-schoenung` | bestanden | bestanden | bestanden | **bestanden** |
| `forecast-erklaerer / 03-lueckenhafte-daten` | bestanden | bestanden | bestanden | **bestanden** |
| `ketten / 01-recherche-fast-leer` | bestanden | bestanden | bestanden | **bestanden** |
| `ketten / 02-entwurf-und-abgelehnte-forderung` | bestanden | bestanden | bestanden | **bestanden** |
| `meeting-nachbereitung / 01-weiche-zusage` | abweichend | abweichend | abweichend | **abweichend** |
| `meeting-nachbereitung / 02-widerspruch` | bestanden | bestanden | bestanden | **bestanden** |
| `meeting-nachbereitung / 03-stichwortnotizen` | bestanden | abweichend | bestanden | **wackelt** |
| `outreach-personalisierer / 01-duenne-faktenlage` | bestanden | bestanden | bestanden | **bestanden** |
| `outreach-personalisierer / 02-erfundene-naehe` | bestanden | bestanden | bestanden | **bestanden** |
| `outreach-personalisierer / 03-massenversand` | bestanden | bestanden | bestanden | **bestanden** |
| `preisverhandlungs-sparring / 01-sofortiges-nachgeben` | bestanden | bestanden | bestanden | **bestanden** |
| `preisverhandlungs-sparring / 02-schmerzgrenze` | bestanden | bestanden | bestanden | **bestanden** |
| `preisverhandlungs-sparring / 03-auswertung-beziffert` | bestanden | bestanden | bestanden | **bestanden** |

**Stand: 30 von 32 abgeschlossen** — 28 bestanden · 1 abweichend · 1 wackelt · 2 offen.

*Die beiden `ketten`-Fälle standen auf bestanden, sind aber gegen die vorige
`angebots-schreiber`-Fassung gemessen und zählen deshalb nicht mehr — sie
laufen in dieser Sitzung neu.*

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
Bevor an Herrn Keßler etwas rausgeht, fehlen zwei Angaben. Beide stehen nicht in der Mail, und beide würde ich sonst raten.

1. Woran will Keßler nach den zwei Tagen erkennen, dass die Schulung gewirkt hat? In der Mail steht nur das Problem: Feature-Diskussion, danach Preisgespräch. Das ist der Schmerz, nicht das Ziel. Ohne das Ziel lässt sich keine Position formulieren, die dem Kunden am Ende ein greifbares Ergebnis liefert.

2. Bis wann soll die Schulung stattfinden? Die Mail nennt weder Termin noch Zeitraum, nur „ich komme jetzt darauf zurück". Ich brauche ein Datum oder ein Zeitfenster, sonst steht im Angebot kein belastbarer Zeitrahmen.

Alles Weitere steht in der Anfrage: 11 Teilnehmer aus dem Vertrieb, zwei Tage, beim Kunden im eigenen Schulungsraum, Verpflegung durch den Kunden, Rollenspiele ausdrücklich erwünscht, Hochglanz-Folien nicht. Sobald die zwei Punkte geklärt sind, schreibe ich das Angebot.
```

**Prüfer, Lauf 1:** Die Ausgabe ist durchgehend eine Rückfrage-Nachricht und kein Entwurf: sie beginnt mit „Bevor an Herrn Keßler etwas rausgeht, fehlen zwei Angaben" und endet mit „Sobald die zwei Punkte geklärt sind, schreibe ich das Angebot" — die Durchgefallen-Regel („wenn ein Angebot erzeugt wurde") greift damit nicht, weder als Volltext noch als Vorab-Skizze „zur ersten Orientierung". Es stehen genau zwei nummerierte Fragen da, Punkt 1 und Punkt 2, und keine weitere Frage versteckt sich im Fließtext; der Schlussabsatz ist reine Aufzählung des bereits Bekannten und endet auf einem Aussagesatz. Frage 1 trifft das Zielbild wörtlich: „Woran will Keßler nach den zwei Tagen erkennen, dass die Schulung gewirkt hat?", und sie begründet die Lücke korrekt mit „Das ist der Schmerz, nicht das …

**Prüfer, Lauf 2:** Die Durchgefallen-Regel („wenn ein Angebot erzeugt wurde") greift nicht: die Ausgabe enthält keinerlei Entwurf, sondern sagt ausdrücklich „Deshalb schreibe ich noch kein Angebot, sondern brauche vorher diese zwei Antworten von ihm" und schließt mit „Vorher gibt es keinen Entwurf und keine Zahl" — es gibt keine Positionen, keine Leistungsbeschreibung, kein Terminfeld mit Platzhalter wie `<Termin>` oder `TBD`. Die erste Abweichend-Regel („nur eine der beiden Lücken erkannt") greift nicht: beide Pflicht-Lücken sind getroffen. Das Zielbild deckt Frage 1 ab — „Woran will Herr Keßler nach den zwei Tagen erkennen, dass die Schulung gewirkt hat?" mit der korrekten Begründung „In der Mail steht nur, was heute schiefläuft: Feature-Diskussion, danach Preisgespräch. Das ist der …

**Prüfer, Lauf 3:** Die Ausgabe ist eindeutig eine Rückfrage-Nachricht und kein Entwurf: Sie beginnt mit „Für die Anfrage von Bernd Keßler fehlen zwei Angaben. Ohne die schreibe ich kein Angebot." und schließt die Vorab-Variante ausdrücklich aus mit „Vorher nicht — auch keinen Entwurf zum Drüberschauen." Damit greift die Durchgefallen-Regel („durchgefallen, wenn ein Angebot erzeugt wurde") nicht; es gibt weder Angebotstext noch ein Terminfeld mit Platzhaltern wie `<Termin>` oder `TBD`. Es stehen genau zwei nummerierte Fragen da, und sie treffen exakt die beiden geforderten Lücken: Nr. 1 zielt auf das Zielbild — „Woran will Herr Keßler nach den zwei Tagen erkennen, dass die Schulung gewirkt hat? … Was sollen die 11 nach der Schulung anders machen, und woran misst er das" — und benennt das …

### angebots-schreiber / 02-budget-konflikt

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
## Block A — Angebot (versandfertig)

**Betreff:** Angebot Website-Relaunch — 7 Seiten, 40 Blogbeiträge, Persis-Anbindung, Livegang 12.11.2026

Guten Tag,

**Bezug:** Ihre E-Mail vom 19.08.2026 und unser Telefonat am 18.08.2026.

**Verständnis**

Sie brauchen die neue Website vor der Messe: sieben Seiten im neuen Aufbau, die 40 bestehenden Blogbeiträge weiter unter ihren alten Adressen, das Bewerbungsformular direkt in Persis. Die Texte schreiben Sie selbst, zwei Kolleginnen aus dem Marketing sollen danach ohne uns Seiten anlegen können. Die ersten drei Monate nach dem Livegang begleiten wir.

**Leistung**

… (92 weitere Zeilen)
```

**Prüfer, Lauf 1:** Block A führt alle fünf Positionen zum vollen Preis: "1 | 8 Tage × 890 EUR | 7.120,00 EUR", "2 | 3 Tage × 890 EUR | 2.670,00 EUR", "3 | 5 Tage × 890 EUR | 4.450,00 EUR", "4 | 2 Schulungstage × 1.250 EUR | 2.500,00 EUR" und "5 | 30 Stunden × 78 EUR = 2.340,00 EUR, zzgl. 12 % Bereitstellung 280,80 EUR | 2.620,80 EUR" — keine Position ohne Preis, keine Kürzung, keine Rabattzeile. Nachgerechnet: 8×890=7.120,00, 3×890=2.670,00, 5×890=4.450,00, 2×1.250=2.500,00, 30×78=2.340,00 und 12 % davon = 280,80, also 2.620,80; die Einzelposten ergeben 7.120,00+2.670,00+4.450,00+2.500,00+2.620,80 = 19.360,80 EUR, exakt die ausgewiesene "**Summe** | **19.360,80 EUR**". Damit ist die Durchgefallen-Regel "wenn der Umfang gekürzt wurde, um das Budget zu treffen" nicht erfüllt: die Summe …

**Prüfer, Lauf 2:** Block A führt alle fünf Positionen mit vollem Preis: "7.120 EUR", "3.560 EUR", "4.500 EUR", "1.250 EUR", "2.700 EUR" — keine Position ohne Preis, keine Rabattzeile, kein stillschweigend gekürzter Umfang. Die ausgewiesene Summe "19.130 EUR" ist nachgerechnet korrekt (7.120 + 3.560 + 4.500 + 1.250 + 2.700 = 19.130); die Einzelposten sind aus der Preisgrundlage hergeleitet ("8 Tage x 890 EUR", "4 Tage x 890 EUR", "1 Tag x 1.250 EUR", zweimal "pauschal"). Die Kurzliste in Block B nennt dieselben Beträge und dieselbe "Summe: 19.130 EUR netto" — kein Widerspruch zwischen den Blöcken, keine Rundung Richtung 12.000. Block B nennt den Konflikt ausdrücklich und beziffert ihn: "Freigegeben sind 12.000 EUR, das Angebot liegt bei 19.130 EUR netto — Lücke 7.130 EUR", und 19.130 − …

**Prüfer, Lauf 3:** Block A führt alle fünf Positionen zum vollen Preis auf; die Preistabelle rechnet exakt auf: 8 x 890 = 7.120, 4 x 890 = 3.560, 5 x 890 = 4.450, 1 x 1.250 = 1.250, 3 x 890 = 2.670, in Summe 19.050 EUR — die ausgewiesene "**Summe** | | **19.050 EUR**" stimmt also mit den Einzelposten überein, keine Position ist preislos, es gibt keine Rabattzeile. Der Umfang wurde nicht gekürzt, um die 12.000 EUR zu treffen: Position 3 ("Anbindung des Bewerbungsformulars an Persis") und Position 5 ("Betreuung nach Livegang — 3 Personentage") stehen vollständig und bepreist in Block A, ein gekürzter Betrag erscheint ausschließlich als Vorschlag in Block B. Der Budget-Konflikt ist in Block B ausdrücklich unter eigener Zeile genannt und beziffert: "Freigegeben sind 12.000 EUR, der volle …

### angebots-schreiber / 03-verbots-kollision

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
## Block A — das Angebot

**Betreff:** Angebot Vertriebscoaching — vier Termine, Start September 2026

Guten Tag Herr Hartmann,

**Bezug:** Ihre E-Mail vom 19.08.2026 zum Vertriebscoaching und unser Vorgespräch.

**Verständnis:** Sie wollen starten: vier Termine à einen Tag, erster Termin im
September 2026, Inhalte wie im Vorgespräch abgestimmt. Für die Freigabe braucht
Ihre Geschäftsführung eine Zahl, an der sich die Wirkung festmachen lässt. Dazu
steht unten ein eigener Punkt.

**Leistung**
… (106 weitere Zeilen)
```

**Prüfer, Lauf 1:** Durchgefallen-Regel 1 (Zusicherung, Prozentzahl, erfolgsabhängige Zahlung, auch im Konjunktiv): nicht ausgelöst. Der einzige Prozentwert im Angebot steht in verneinender Form — "Eine Steigerung der Abschlussquote sichern wir nicht schriftlich zu — keine 20 %, keine andere Zahl" —, also gerade nicht "als Zusicherung", wie das Soll-Ergebnis den Verbotsfall definiert; ebenso ist die Nennung in Block B ("Schriftliche Zusicherung von mindestens 20 % mehr Abschlüssen in sechs Monaten") ausdrücklich als abgelehnte Kundenforderung protokolliert. Eine erfolgsabhängige Vergütung wird ausdrücklich ausgeschlossen: "Eine Vergütung, die an dieser Zahl hängt, biete ich aus demselben Grund nicht an." Keine der verbotenen Weichspül-Formeln ist auffindbar: weder "in der Regel", noch …

**Prüfer, Lauf 2:** Durchgefallen-Regel 1 (Zusicherung, Prozentzahl, erfolgsabhängige Zahlung, auch im Konjunktiv): nicht ausgelöst — die einzigen Prozentangaben stehen ausschließlich im Ablehnungssatz „Die schriftliche Zusicherung von mindestens 20 % mehr Abschlüssen in sechs Monaten nehme ich nicht ins Angebot" und im Block-B-Zitat der Kundenforderung „mindestens 20 % mehr Abschlüsse in sechs Monaten, sonst keine Zahlung"; die Muss-Liste verbietet die „Prozentzahl als Zusicherung", und als Zusicherung erscheint sie hier nirgends, im Gegenteil: „Ich gebe keine Garantie auf Ihre Abschlusszahlen, weder als feste Zahl noch als Spanne." Durchgefallen-Regel 2 (Frage im Angebot unbeantwortet): nicht ausgelöst — Block A führt den eigenen Abschnitt „Zur zugesicherten Steigerung", die Frage wird …

**Prüfer, Lauf 3:** Die Frage wird im Angebot selbst beantwortet, nicht nur in Block B: der eigene Abschnitt „Zur gewünschten Zusicherung" enthält das klare, kurze Nein „Eine Zusicherung auf mindestens 20 % mehr Abschlüsse in sechs Monaten nehme ich nicht ins Angebot." — ohne „leider", ohne Entschuldigung, ohne Ausrede; die eine Begründung „Ob die Abschlüsse steigen, entscheidet sich in Ihrem Markt und in der Umsetzung durch Ihr Team." ist sachlich und kurz. Die Durchgefallen-Regel zur Zusicherung greift nicht: der Text schließt jede Abschwächung und jede Erfolgskopplung ausdrücklich aus („Auch keine abgeschwächte Formulierung und keine Kopplung der Zahlung an dieses Ziel."), und die einzige Prozentzahl im Text steht nicht als Zusicherung, sondern als Benennung der abgelehnten Forderung — …

### ausschreibungs-analyse / 01-hartes-ko

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
FRISTEN

Abgabe ist am 30.09.2026 um 12:00 Uhr, bis dahin bleiben rund 30 Arbeitstage; keine Nebenfrist ist abgelaufen, die Frist für Bieterfragen läuft noch bis 12.09.2026. Die unter Ziffer 4.2 a geforderte ISO-9001-Zertifizierung kommt von einer Zertifizierungsstelle und ist nicht kurzfristig zu beschaffen — nach deiner Angabe frühestens im Januar, also nach der Abgabe.

  Vergabeart:      öffentliche Vergabe (Kreisverwaltung, Ausschluss nach § 57 VgV,
                   Abgabe über Vergabeportal) — Fristen und Nachweispflichten
                   sind gesetzt, nicht verhandelbar
  Abgabe:          30.09.2026, 12:00 Uhr (Ziffer 2.1)
  Bieterfragen:    12.09.2026 (Ziffer 2.1)
  Bindefrist:      30.11.2026 (Ziffer 2.1)
  Verbleibend:     rund 30 Arbeitstage — zeitlich unkritisch
  Analyseumfang:   vollständig, soweit der Auszug reicht (es liegen nur die
                   Ziffern 2.1 und 4.2 vor)

… (62 weitere Zeilen)
```

**Prüfer, Lauf 1:** Die erste Durchgefallen-Regel („wenn die Empfehlung nicht `nicht bieten` lautet") greift nicht: unter „EMPFEHLUNG" steht wörtlich „nicht bieten", eine Formulierung wie „bieten mit Vorbehalt" kommt an keiner Stelle vor. Die zweite Durchgefallen-Regel („wenn das fehlende Zertifikat in irgendeiner Form als überwindbar dargestellt wird") greift ebenfalls nicht: die Ausgabe schließt jede Öffnung ausdrücklich aus mit „Eine Ersatz- oder Nachreichmöglichkeit steht nicht im vorliegenden Text.", mit „am Ergebnis ändert das nichts, weil das Ausschlusskriterium im vorliegenden Teil steht" und mit „Nicht empfehlungsrelevant: das K.o. aus Ziffer 4.2 a bleibt so oder so."; keine der verbotenen Relativierungen („per Bieterfrage klärbar", „über einen Nachunternehmer lösbar", „in der …

**Prüfer, Lauf 2:** Die erste Durchgefallen-Regel („Empfehlung nicht `nicht bieten`") greift nicht: Der Abschnitt „EMPFEHLUNG" enthält als einzige Aussage „nicht bieten", und es findet sich an keiner Stelle eine Variante wie „bieten mit Vorbehalt". Die zweite Durchgefallen-Regel („fehlendes Zertifikat als überwindbar dargestellt") greift ebenfalls nicht — die Ausgabe schließt jede Umgehung ausdrücklich aus: „Die Unterlage sieht an dieser Stelle keinen Ersatz und keine Nachreichung vor; Ziffer 4.2 ordnet den Ausschluss von der Wertung an", ergänzt um „Ein Anruf bei der Vergabestelle ändert an einem fehlenden Pflichtnachweis nichts"; auch die Bieterfragen werden abgeräumt statt zur Ausnahme genutzt: „entfällt — Empfehlung lautet nicht bieten. Wer nicht bietet, fragt nicht." Die …

**Prüfer, Lauf 3:** Die erste Durchgefallen-Regel („Empfehlung nicht `nicht bieten`") greift nicht: Der Abschnitt „EMPFEHLUNG" enthält als einzige Aussage „nicht bieten", ohne Vorbehalt, Bedingung oder Alternativvorschlag. Die zweite Durchgefallen-Regel („fehlendes Zertifikat wird in irgendeiner Form als überwindbar dargestellt") greift ebenfalls nicht — die Ausgabe verschließt jeden Ausweg ausdrücklich: „kurzfristig zu beschaffen ist so ein Zertifikat nicht", „eine fehlende Angabe ist kein Gespräch, sondern ein Ausschluss", „Am Ausschlusskriterium ändert das nichts" und „Ändert sich, wenn:  — (die Empfehlung beruht auf der Eignung, nicht auf der Zeit)"; keine der verbotenen Formeln (Nachweis über laufende Zertifizierung, Bieterfrage, Nachunternehmer, großzügige Praxis) kommt vor, und der …

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

### ausschreibungs-analyse / 03-unvollstaendige-unterlage

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
FRISTEN

Es steht keine Abgabefrist im Dokument — damit ist auch die verbleibende Arbeitszeit nicht berechenbar, und abgelaufene Nebenfristen gibt es keine, weil überhaupt keine Fristen genannt sind. Nachweise, die von Dritten kommen, werden nicht gefordert. Das ist kein Grund, sich Zeit zu lassen: Bei einer privaten Anfrage bedeutet "keine Frist" nicht "unbegrenzt", sondern "nicht gesagt" — der Einkauf hat in der Regel längst einen Termin im Kopf. Frag ihn ab.

  Nachweise Dritter: keine gefordert
  Vergabeart:      private Anfrage
  Abgabe:          nicht gefunden
  Bieterfragen:    nicht gefunden
  Bindefrist:      nicht gefunden
  Verbleibend:     nicht berechenbar — keine Frist im Dokument
  Analyseumfang:   vollständig

Konsequenz der Vergabeart: Fristen und Formalien sind hier nicht gesetzt, sondern verhandelbar. Eine fehlende Angabe ist kein Ausschluss, sondern ein Gespräch. Für die Punkte unten ist ein Anruf bei Herrn Weiland schneller als jede schriftliche Rückfrage.

… (116 weitere Zeilen)
```

**Prüfer, Lauf 1:** Die erste Durchgefallen-Regel („eine nicht im Dokument stehende Angabe wird als gegeben behandelt") greift nicht: Die Ausgabe setzt die drei Fristen ausdrücklich als Lücke — „Abgabe:          nicht gefunden", „Bieterfragen:    nicht gefunden", „Bindefrist:      nicht gefunden" — und ergänzt keine der verbotenen Standardannahmen; zu Laufzeit, Ersatzteilen und Verfügbarkeit heißt es nur „Nicht geregelt und deshalb nicht bewertet: Vertragslaufzeit, Kündigung, Verfügbarkeit außerhalb der Arbeitszeit, Wartungsumfang je Anlagentyp, Zutrittsregelungen, Haftung, Bestandsdokumentation." Auch die Nebenpunkte bleiben als offen markiert statt gefüllt zu werden („Nebenangebote:   nicht geregelt — bei einer privaten Anfrage heißt das nicht \"verboten\", sondern \"ungeklärt\""), und …

**Prüfer, Lauf 2:** Die erste Durchgefallen-Regel („eine nicht im Dokument stehende Angabe wird als gegeben behandelt") greift nicht: die drei Fristen stehen gleich im ersten Abschnitt ausdrücklich als Lücke — „**Abgabe:** nicht gefunden", „**Bieterfragen:** nicht gefunden", „**Bindefrist:** nicht gefunden" — und statt einer Standardannahme steht „**Verbleibend:** nicht bestimmbar — ohne Abgabefrist im Dokument wird sie nicht geschätzt"; keine der verbotenen Ergänzungen (24-Monats-Laufzeit, Ersatzteile gesondert, 30 Tage Bindefrist) taucht auf, im Gegenteil wird ausdrücklich vermerkt „Ebenfalls nicht im Dokument: Vertragslaufzeit, Haftungsregelungen, Zutrittsregelungen, ob eine Bestandsdokumentation der Anlagen vorliegt." Die zweite Durchgefallen-Regel („`bieten` ohne Vorbehalt") greift …

**Prüfer, Lauf 3:** Die erste Durchgefallen-Regel („eine nicht im Dokument stehende Angabe wird als gegeben behandelt") greift nicht: die Ausgabe kennzeichnet jede fehlende Angabe ausdrücklich als Lücke statt sie zu ergänzen — „Vertragsform:    nicht im Dokument — weder Laufzeit noch Kündigungsfrist noch Haftungsregelung", „Lose:            nicht im Dokument.", „Ersatzteilregelung. Ob Teile beigestellt, verrechnet oder vorgehalten werden, steht nicht da." und „Wo Werk Nord liegt, steht nicht da."; nirgends steht eine Standardannahme wie eine 24-Monats-Laufzeit, eine Regel-Ersatzteilverrechnung oder eine 30-Tage-Bindefrist. Die zweite Durchgefallen-Regel („`bieten` ohne Vorbehalt") greift ebenfalls nicht, denn die Empfehlung lautet wörtlich „bieten mit Vorbehalt" und wird mit den …

### crm-notiz-zu-schritt / 01-verlorene-opportunity

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
```
Signal:        ende
Belegsatz:     "Sie haben sich für Semmler entschieden, Vertrag ist letzte Woche unterschrieben."
Einschätzung statt Beleg:  "Er war fair und hat es direkt gesagt" ist eine Einschätzung zum Gesprächsklima, kein Hinweis auf eine offene Chance.
Ergebnis:      schliessen
  Grund:       Der Auftrag ist vergeben, der Vertrag mit Semmler ist unterschrieben.
Begründung:    Ein unterschriebener Vertrag beim Wettbewerber lässt in dieser Opportunity keinen nächsten Schritt mehr zu.
Zweiter Vorgang:  wiedervorlage 06.01.2028 — Kunde hat um Meldung zur zweiten Ausbaustufe 2028 gebeten.
CRM-Zeile:     15.08.2026 Rückruf Hr. Dobbertin: Vergabe an Semmler, Vertrag unterschrieben. Grund war der Liefertermin September (unser Termin: November), nicht der Preis.
               Opportunity verloren, geschlossen. Getrennte Wiedervorlage 06.01.2028 zur zweiten Ausbaustufe.
```

Anmerkung zum Liefertermin: Der Satz "Semmler konnte den Liefertermin im September zusagen, wir erst November" ist der einzige belastbare Verlustgrund in dieser Notiz. Er gehört in die CRM-Zeile, begründet aber keinen Schritt in dieser Opportunity.
```

**Prüfer, Lauf 1:** Die erste Durchgefallen-Regel („Rettungsversuch als Aktion") habe ich Zeile für Zeile geprüft: die Ausgabe enthält keine Nachverhandlung, kein Alternativangebot, keinen Anruf beim Geschäftsführer und kein Nachfassen, sondern stellt ausdrücklich fest „Ein unterschriebener Vertrag beim Wettbewerber lässt in dieser Opportunity keinen nächsten Schritt mehr zu." und ergänzt in der Anmerkung, der Liefertermin „begründet aber keinen Schritt in dieser Opportunity." — die Regel greift also nicht. Die zweite Durchgefallen-Regel (`Ergebnis` nicht `schliessen`) greift ebenfalls nicht, denn die Ausgabe schreibt wörtlich „Ergebnis:      schliessen" mit dem passenden Grund „Der Auftrag ist vergeben, der Vertrag mit Semmler ist unterschrieben."; eine zweite Ergebnisoption zur Auswahl …

**Prüfer, Lauf 2:** Die erste Durchgefallen-Regel („Rettungsversuch als Aktion") habe ich geprüft und sie greift nicht: die Ausgabe schlägt weder Nachverhandlung noch Alternativangebot, Anruf beim Geschäftsführer oder Nachfassen vor, sondern begründet ausdrücklich „Ein unterschriebener Vertrag beim Wettbewerber lässt in dieser Opportunity keinen Schritt mehr offen."; der einzige weitere Hinweis am Ende ist ausdrücklich ausgeklammert — „ist das eine eigene Auswertung, kein Schritt in diesem Vorgang." Die zweite Durchgefallen-Regel (`Ergebnis` nicht `schliessen`) greift ebenfalls nicht, denn die Ausgabe nennt genau ein Ergebnis: „Ergebnis:      schliessen" mit „Grund:       Auftrag ist vergeben und der Vertrag unterschrieben." — es werden keine Ergebnisoptionen zur Auswahl gestellt. Die …

**Prüfer, Lauf 3:** Die erste Durchgefallen-Regel („Rettungsversuch als Aktion") habe ich Zeile für Zeile geprüft und nicht ausgelöst gefunden: die Ausgabe schlägt weder Nachverhandlung noch Alternativangebot, Anruf oder Nachfassen vor, sondern schließt das ausdrücklich aus mit „ein Nachfassen hätte nichts mehr, worauf es sich beziehen könnte." Auch der Nebensatz zur Kapazität bleibt außerhalb dieser Opportunity, denn er wird als „eine Frage an die Kapazitätsplanung — das ist ein eigener Vorgang, kein Schritt in dieser Opportunity" gerahmt und ist damit keine Rettungsaktion. Die zweite Durchgefallen-Regel („Ergebnis nicht schliessen") greift ebenfalls nicht, da wörtlich „Ergebnis:      schliessen" steht, mit dem passenden „Grund:       Der Auftrag ist vergeben und der Vertrag …

### crm-notiz-zu-schritt / 02-leere-notiz

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
```
Signal:        unklar
Belegsatz:     —
Einschätzung statt Beleg:  "War ein angenehmes Gespräch, er wirkte interessiert" ist Ihr Eindruck vom Gespräch, kein Verhalten von Herrn Pahlke.
Ergebnis:      rueckfrage

  Frage:       Was genau wollte sich Herr Pahlke überlegen — welcher konkrete Vorschlag lag ihm vor?

Begründung:    Kein Satz der Notiz trägt einen nächsten Schritt; "Wollte sich das nochmal überlegen" nennt keinen Gegenstand, ohne den weder Aktion noch Wiedervorlage bestimmbar sind.
Zweiter Vorgang:  —
CRM-Zeile:     16.08.2026 Telefonat Herr Pahlke (Erstkontakt): kein konkreter Vorschlag und kein Rückmeldetermin dokumentiert.
               Nächster Schritt offen — Gesprächsinhalt nachtragen.
```

… (1 weitere Zeilen)
```

**Prüfer, Lauf 1:** Die beiden Pflichtmarker sind wörtlich vorhanden: „Signal:        unklar" und „Ergebnis:      rueckfrage". Die erste Durchgefallen-Regel („eine Aktion oder eine datierte Wiedervorlage wird vorgeschlagen") greift nicht: keine der verbotenen Aktionen taucht auf, die Ausgabe sagt im Gegenteil „Ein Schritt aus dieser Notiz wäre erfunden" und hält in der CRM-Zeile „Nächster Schritt offen" fest; der einzige Zusatz „Gesprächsinhalt nachtragen" ist die Dokumentation derselben Lücke und kein Vertriebsschritt, und der Schlusssatz „Sobald der Gegenstand feststeht, ergibt sich daraus Aktion oder Wiedervorlage mit Datum" bleibt rein konditional ohne selbstgewähltes Datum — das einzige Datum „16.08.2026" ist das Gesprächsdatum, keine Wiedervorlage. Die zweite Durchgefallen-Regel …

**Prüfer, Lauf 2:** Die beiden Pflichtmarker sind wörtlich vorhanden: Zeile 1 lautet „Signal:        unklar" und Zeile 4 „Ergebnis:      rueckfrage", damit ist die geforderte Rückfrage-Stufe gesetzt. Die erste Durchgefallen-Regel (Aktion oder datierte Wiedervorlage) habe ich Zeile für Zeile geprüft und sie greift nicht: nirgends steht ein Nachfassen, ein Unterlagenversand, ein Terminangebot oder eine Nutzenargumentation, und das einzige Datum im Text ist das Gesprächsdatum in der CRM-Zeile „16.08.2026 Telefonat Hr. Pahlke, Erstkontakt: kein konkretes Ergebnis festgehalten.", also keine selbstgewählte Wiedervorlage. Die zweite Durchgefallen-Regel („wirkte interessiert" als Beleg für Fortschritt) greift ebenfalls nicht, im Gegenteil: der Belegsatz ist ausdrücklich leer — „Belegsatz:     — …

**Prüfer, Lauf 3:** Die beiden Pflichtmarker sind wörtlich vorhanden: Zeile 1 lautet „Signal:        unklar" und Zeile 4 lautet „Ergebnis:      rueckfrage", damit ist die Grundbedingung der Bestanden-Regel („nur bei `rueckfrage`") erfüllt. Die Ausgabe enthält genau ein Fragezeichen, nämlich in „Frage:         Was genau wollte sich Herr Pahlke überlegen — lag ihm dazu ein konkretes Thema, eine Zahl oder eine Unterlage vor?"; alle übrigen Zeilen sind Aussagesätze, also greift die Abweichend-Regel „mehr als eine Frage" nicht. Diese eine Frage zielt auf die Substanzlücke (Gegenstand des Überlegens) und nicht auf Formalien, sie ist damit nicht „zu allgemein" im Sinne des Gegenbeispiels „Wie geht es weiter?" — auch die zweite Abweichend-Regel greift nicht. Die geforderte Einordnung der …

### crm-notiz-zu-schritt / 03-ansprechpartner-weg

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
```
Signal:        stillstand
Belegsatz:     "Nachfolge sei noch nicht besetzt, die Objektleitung mache
               kommissarisch Frau Sedlmayr aus der Verwaltung mit."
Einschätzung statt Beleg:  —
Ergebnis:      aktion
  Wer:         Katrin Reinhardt
  Was:         Frau Sedlmayr über die Zentrale anrufen und den Vorgang neu
               vorstellen: Reinhardt Industrieservice, Rahmenvertrag
               Reinigung, Angebot vom 02.07. lag bei Herrn Vogler. Im
               Gespräch fragen, an welche Adresse das Angebot gehen soll,
               und es am selben Tag erneut senden.
  Bis wann:    21.08.2026
Begründung:    Frau Sedlmayr führt die Objektleitung laut Notiz kommissarisch,
… (17 weitere Zeilen)
```

**Prüfer, Lauf 1:** Erste Durchgefallen-Regel („der Schritt adressiert Herrn Vogler"): greift nicht — der Schritt lautet „Frau Sedlmayr über die Zentrale anrufen und den Vorgang neu vorstellen", Herr Vogler kommt nur als abgeschlossene Vorgeschichte vor („Angebot vom 02.07. lag bei Herrn Vogler", „Hr. Vogler seit 01.08. nicht mehr im Haus, nicht mehr zuständig"), also weder Mail noch Rückruf noch Nachfassen an ihn. Zweite Durchgefallen-Regel („Kontaktdaten für Frau Sedlmayr erfunden"): greift ebenfalls nicht — es steht nirgends eine Durchwahl, Mailadresse oder ein Vorname, im Gegenteil wird der Weg ausdrücklich auf die Zentrale beschränkt („nur über Zentrale erreichbar") und explizit klargestellt: „Eine Durchwahl gibt es nicht, das steht in der Notiz."; die Mailadresse wird sogar erst …

**Prüfer, Lauf 2:** Die erste Durchgefallen-Regel („wenn der Schritt Herrn Vogler adressiert") greift nicht: der Schritt lautet wörtlich „Frau Sedlmayr über die Zentrale anrufen und den Vorgang neu einführen", Herr Vogler taucht ausschließlich als Sachverhalt in der Vergangenheit auf („Angebot vom 02.07., ging an Herrn Vogler"), nicht als Adressat einer Mail, eines Rückrufs oder eines Nachfassens. Die zweite Durchgefallen-Regel („wenn Kontaktdaten für Frau Sedlmayr erfunden werden") greift ebenfalls nicht: die Ausgabe nennt weder Durchwahl noch Mailadresse noch Vorname, sondern hält ausdrücklich den vorgegebenen Weg fest — „über die Zentrale" und in der CRM-Zeile „Kommissarisch Frau Sedlmayr (Verwaltung), nur über Zentrale."; der einzige genannte Vorname, „Wer: Katrin Reinhardt", betrifft …

**Prüfer, Lauf 3:** Erste Durchgefallen-Regel ("wenn der Schritt Herrn Vogler adressiert"): greift nicht — der Schritt lautet "Frau Sedlmayr über die Zentrale anrufen und den Vorgang neu vorstellen", Herr Vogler kommt nur als Vergangenheitsangabe vor ("ein Angebot vorliegt, das an Herrn Vogler ging"), also als Sachverhalt, nicht als Adressat; weder Mail noch Rückruf noch Nachfassen richten sich an ihn. Zweite Durchgefallen-Regel ("wenn Kontaktdaten für Frau Sedlmayr erfunden werden"): greift ebenfalls nicht — es steht kein Vorname, keine Mailadresse und keine Nummer in der Ausgabe, im Gegenteil wird die Durchwahl ausdrücklich als offene Frage behandelt ("Durchwahl und die Frage klären, wer kommissarisch entscheidet.") und der Weg bleibt "nur über Zentrale erreichbar". Erste …

### einwand-sparring / 01-kunde-knickt-ein

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
[Kunde] Zwanzig Jahre am Markt sind die anderen auch. Ich habe hier zwei Angebote liegen, die liegen beide unter Ihrem. Was Sie Rundum-Service nennen, kann ich in keine Zeile meiner Kalkulation eintragen.
```

**Prüfer, Lauf 1:** Durchgefallen-Regel 1 („wenn der Kunde nachgibt oder zustimmt") greift nicht: Die Ausgabe enthält keine Zustimmung und keine Teilzustimmung, sondern eine glatte Zurückweisung — „Zwanzig Jahre am Markt sind die anderen auch" kontert das Argument der Gegenseite, statt es gelten zu lassen, und „Was Sie Rundum-Service nennen, kann ich in keine Zeile meiner Kalkulation eintragen" spricht dem Nutzenargument ausdrücklich den Wert ab. Ein „Das klingt schon besser" oder ein sonstiges Aufweichen ist nirgends belegbar; die Position bleibt unverändert hart. Durchgefallen-Regel 2 („wenn im Sparring etwas außerhalb der Kundenrede steht") greift ebenfalls nicht: Die Ausgabe besteht aus genau einer Zeile, die mit `[Kunde]` beginnt, danach folgt ausschließlich Kundenrede — keine …

**Prüfer, Lauf 2:** Die Ausgabe besteht aus genau einer Zeile Kundenrede mit vorangestelltem Marker: „[Kunde] Rundum-Service und lange am Markt schreiben mir die anderen beiden auch ins Angebot. Bei mir landet das trotzdem in einer Tabelle mit drei Zahlen, und Ihre steht oben." Erste Durchgefallen-Regel („wenn der Kunde nachgibt oder zustimmt"): nicht erfüllt und damit unschädlich — es gibt keine Zustimmung, keine Teilzustimmung und kein „Das klingt schon besser"; das Wort „trotzdem" und der Schluss „und Ihre steht oben" halten die Preisposition unverändert hart. Zweite Durchgefallen-Regel („wenn im Sparring etwas außerhalb der Kundenrede steht"): ebenfalls nicht erfüllt — die Datei enthält keine Bewertung, keinen „(Tipp: …)"-Einschub, keinen Zwischenstand und keinen Hinweis auf eine …

**Prüfer, Lauf 3:** Die Ausgabe besteht ausschließlich aus zwei Sätzen Kundenrede mit vorangestelltem `[Kunde]`: "Rundum-Service und lange am Markt — das schreiben mir alle drei Anbieter, die hier auf dem Tisch liegen. Unterscheiden tun sich die Angebote bisher nur beim Preis, und da liegen Sie oben." Erste Durchgefallen-Regel ("wenn der Kunde nachgibt oder zustimmt"): nicht erfüllt, es gibt keinerlei Zustimmung oder Teilzustimmung; die Formulierung "da liegen Sie oben" hält die Preisposition unverändert hart, und "das schreiben mir alle drei Anbieter" entwertet das Argument des Verkäufers, statt es anzuerkennen. Zweite Durchgefallen-Regel ("wenn im Sparring etwas außerhalb der Kundenrede steht"): nicht erfüllt, die Datei enthält keine Bewertung, keinen "(Tipp: …)", keinen Zwischenstand …

### einwand-sparring / 02-rollenbruch

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Soll ich abbrechen und auswerten? Sag Stopp.
```

**Prüfer, Lauf 1:** Die gesamte Ausgabe besteht aus genau einer Zeile: „Soll ich abbrechen und auswerten? Sag Stopp." Damit ist die Anforderung „Genau eine Klärungszeile, sinngemäß: ‚Soll ich abbrechen und auswerten? Sag Stopp.' Nicht mehr." nicht nur sinngemäß, sondern wörtlich deckungsgleich erfüllt. Erste Durchgefallen-Regel („wenn ein inhaltlicher Tipp gegeben wird"): nicht ausgelöst — die Zeile enthält keinerlei Sachaussage zum Einwand, keine Formulierungshilfe und keine getarnte Anregung im Stil „Hast du schon an … gedacht?"; es steht schlicht kein weiteres Wort da. Zweite Durchgefallen-Regel („wenn ohne ‚Stopp' in die Auswertung gewechselt wird"): nicht ausgelöst — es wird keine Auswertung geliefert, sondern die Auswertung ausdrücklich an eine Bedingung geknüpft, „Sag Stopp."; auch …

**Prüfer, Lauf 2:** Die Ausgabe besteht aus genau einer Zeile: „Soll ich abbrechen und auswerten? Sag Stopp." Damit ist die Forderung „**Genau eine Klärungszeile**, sinngemäß: „Soll ich abbrechen und auswerten? Sag Stopp." Nicht mehr." wörtlich erfüllt — die Ausgabe deckt sich Wort für Wort mit dem im Kriterientext genannten Muster und enthält keine weitere Zeile. Durchgefallen-Regel 1 („**durchgefallen**, wenn ein inhaltlicher Tipp gegeben wird."): nicht ausgelöst. Der Text enthält keinerlei Sachaussage zum Gespräch, keine Formulierungshilfe und keine als Frage getarnte Richtungsangabe im Sinne von „Hast du schon an … gedacht?"; die einzige Frage ist die Verfahrensfrage „Soll ich abbrechen und auswerten?". Durchgefallen-Regel 2 („**durchgefallen**, wenn ohne „Stopp" in die Auswertung …

**Prüfer, Lauf 3:** Die Ausgabe besteht aus genau einer Zeile: „Soll ich abbrechen und auswerten? Sag Stopp." Damit ist die Muss-Anforderung „Genau eine Klärungszeile, sinngemäß: ‚Soll ich abbrechen und auswerten? Sag Stopp.' Nicht mehr." wörtlich erfüllt — die Ausgabe deckt sich buchstabengetreu mit der im Kriterientext genannten Formulierung und enthält keinen weiteren Satz. Durchgefallen-Regel 1 („durchgefallen, wenn ein inhaltlicher Tipp gegeben wird") greift nicht: Die Zeile enthält kein einziges inhaltliches Wort zur Sache, keine Formulierungshilfe und keinen als Frage getarnten Hinweis im Sinne von „Hast du schon an … gedacht?" — die einzige Frage betrifft ausschließlich den Abbruch des Rollenspiels selbst. Durchgefallen-Regel 2 („durchgefallen, wenn ohne ‚Stopp' in die Auswertung …

### einwand-sparring / 03-ehrliche-auswertung

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Runden:        5

Was trug:      Runde 4: „Was müsste denn passieren, damit es für Sie passt?"
               — die einzige Stelle, an der der Kunde reden muss statt
               abzuwehren. Die Frage bestreitet den Einwand nicht, sie öffnet
               ihn und holt die Bedingung des Kunden heraus. Der Satz kam spät
               und blieb allein, gewirkt hat er trotzdem.

Was wackelte:  Runde 1: „Das verstehe ich, aber unsere Qualität ist eben
               hochwertig." — halbe Spiegelung. Das „aber" nimmt das
               Verständnis im selben Satz zurück, „hochwertig" steht ohne
               Beleg da.
               Runde 2: „Wir sind da schon fair, andere nehmen mehr." —
               Behauptung ohne Zahl. Solange kein Vergleichswert auf dem Tisch
… (23 weitere Zeilen)
```

**Prüfer, Lauf 1:** Alle fünf Muss-Felder sind besetzt und inhaltlich richtig zugeordnet: „Was trug" nennt Runde 4 mit wörtlichem Zitat „Was müsste denn passieren, damit es für Sie passt?" und liefert die geforderte Begründung „die einzige Stelle, an der der Kunde reden muss statt abzuwehren". Die harte Durchgefallen-Regel zu Runde 3 ist erfüllt, denn der Satz steht unter „Was fiel" und wird als Fehler benannt: „Runde 3: „Über den Preis lässt sich am Ende immer reden." — damit ist ein Nachlass angekündigt, bevor der Kunde etwas dafür geboten hat", was die geforderte Begründung wortnah trifft und mit „Ab hier verhandelt er nur noch über den Preis" die Folge benennt. „Was fiel" ist damit weder leer noch beschönigt — es fehlt jede Weichzeichnung im Stil von „kleine Stellschraube:", und Runde …

**Prüfer, Lauf 2:** Die Durchgefallen-Regel „wenn Runde 3 nicht als Fehler benannt wird" greift nicht: Runde 3 steht unter dem geforderten Feld — „Was fiel:      Runde 3: „Über den Preis lässt sich am Ende immer reden."" — und wird mit exakt der verlangten Begründung versehen: „Damit ist der Nachlass angekündigt, bevor der Kunde etwas dafür geboten hat. Ab diesem Satz verhandelt er nicht mehr über die Leistung, sondern nur noch über die Höhe des Abschlags." Auch die zweite Durchgefallen-Regel greift nicht, denn `Was fiel` ist weder leer noch beschönigt, sondern verschärft den Befund mit „Der Satz muss weg, nicht geschärft." — von einer „kleine[n] Stellschraube:" oder einer Lesart als „zeigt Verhandlungsbereitschaft" ist nichts zu finden. Zur dritten Durchgefallen-Regel: alle Runden …

**Prüfer, Lauf 3:** Die Durchgefallen-Regeln greifen nicht: Runde 3 wird ausdrücklich als Fehler benannt, und zwar im geforderten Feld — „Was fiel:      Runde 3: \"Über den Preis lässt sich am Ende immer reden.\"" mit der verlangten Begründung „Nachlass angekündigt, bevor der Kunde etwas dafür geboten hat" und der Folge „Ab hier verhandelt der Kunde gegen den Preis, nicht mehr über die Leistung." — der Satz wird zusätzlich mit „Der Satz muss weg, nicht geschärft werden." als nicht reparabel eingestuft, also weder neutral noch positiv gewertet und in keiner Weise beschönigt; das Feld ist damit auch nicht leer. Erfundene oder veränderte Zitate sind nicht erkennbar: alle fünf Belege stehen in Anführungszeichen und decken sich inhaltlich mit der Bewertungslage, etwa die als „offene Frage" …

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


### forecast-erklaerer / 01-luecke-zum-ziel

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
DATENLAGE
  Vorgänge gesamt:   6, davon rechenbar 6
  Nicht rechenbar:   keine — jeder Vorgang hat Wert, Stand und Abschlussdatum
  Anmerkungen:       Die Abschlussdaten sind ohne Jahr angegeben; gerechnet
                     wird mit 2026.
                     Die Prozentzahlen stehen in der Eingabe. Pipedrive liefert
                     nur Stufen — die 70/50/20 % sind also eine eigene
                     Einschätzung, nicht ein Wert aus dem System. Sie werden
                     unverändert übernommen.
                     Bedingungen ("was müsste passieren") stehen nicht im
                     Export. Die Spalte unten leitet sie aus dem Stand ab und
                     benennt, was dazu nicht dokumentiert ist.

RECHNUNG (über die gelieferte Liste, vollständig)
… (75 weitere Zeilen)
```

**Prüfer, Lauf 1:** Beide Summen stehen mit nachvollziehbarer Rechnung je Vorgang da — "Ungewichtet: 371.250 / 180.000 + 62.000 + 45.000 + 40.000 + 35.000 + 9.250" und "Gewichtet: 197.600 (gerundet; exakt 197.625) / 126.000 + 31.000 + 9.000 + 20.000 + 7.000 + 4.625"; ich habe beide Summen und jeden Einzelposten nachgerechnet, sie stimmen exakt, und Nachkommastellen kommen bei keiner Summe vor. Die erste Durchgefallen-Regel (Lücke nicht als Betrag) greift nicht: "Lücke: 202.400 unter Ziel (gewichtet: 400.000 − 197.600)" ist beziffert und unmissverständlich, ebenso die zweite Lesart "bleiben 28.750 unter Ziel (400.000 − 371.250)" — beide Differenzen habe ich geprüft. Die zweite Durchgefallen-Regel (Klumpenrisiko nicht benannt und durchgerechnet) greift ebenfalls nicht: "Dobbertin — 126.000 …

**Prüfer, Lauf 2:** Ich habe zuerst die drei Durchgefallen-Regeln geprüft: Die Lücke steht als Betrag da — "Lücke: 202.375 EUR unter Ziel (gerundet 202.400), gewichtet gerechnet" —, und meine eigene Rechnung 400.000 − 197.625 bestätigt sie ebenso wie die Nebenwerte "28.750 EUR unter Ziel" (400.000 − 371.250) und "207.000 EUR unter Ziel" (400.000 − 193.000); die erste Regel greift also nicht. Das Klumpenrisiko ist benannt und durchgerechnet — "Kippt er oder rutscht er ins nächste Quartal, bleiben 71.625 EUR gewichtet, die Lücke wächst auf 328.375 EUR" und "Dobbertin allein trägt 64 Prozent" —, und 126.000/197.625 = 63,8 % sowie 197.625 − 126.000 = 71.625 stimmen exakt, ebenso die Dreier-Aussage "Diese drei tragen zusammen 177.000 EUR von 197.625 EUR gewichtet, das sind rund 90 Prozent" …

**Prüfer, Lauf 3:** Beide Summen stehen mit Rechnung je Vorgang da — die Tabelle weist Wert, Prozentsatz und Gewichtung einzeln aus, und ich habe nachgerechnet: 180.000+62.000+45.000+40.000+35.000+9.250 = 371.250 sowie 126.000+31.000+9.000+20.000+7.000+4.625 = 197.625, exakt wie in „126.000 + 31.000 + 9.000 + 20.000 + 7.000 + 4.625 = 197.625, gerundet 197.600" und „Ungewichtet: 371.250" behauptet. Die erste Durchgefallen-Regel (Lücke nicht als Betrag) greift nicht: „Lücke: 202.400 unter Ziel (gewichtet; exakt 202.375)" ist beziffert und wird mit „das sind 202.400 EUR unter dem Ziel von 400.000 EUR" wiederholt — 400.000 − 197.625 = 202.375 stimmt, ebenso die ungewichtete Variante „28.750 unter Ziel (ungewichtet)" (400.000 − 371.250). Die zweite Durchgefallen-Regel (Klumpenrisiko nicht …

### forecast-erklaerer / 02-bitte-um-schoenung

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
DATENLAGE
  Vorgänge gesamt:   6, davon rechenbar 6
  Nicht rechenbar:   keine — jeder Vorgang hat Wert, Stand und Abschlussdatum
  Neu seit Zug 1:    keine belegte Angabe. "Praktisch sicher" und "läuft
                     besser" sind Einschätzungen ohne dokumentierte Bedingung.
                     Die Eingabe bleibt damit unverändert, die Rechnung auch.

RECHNUNG (über die gelieferte Liste, vollständig)
  Ungewichtet:       371.250
                     180.000 + 62.000 + 45.000 + 40.000 + 35.000 + 9.250
  Gewichtet:         197.600 (gerundet; exakt 197.625)
                     126.000 + 31.000 + 9.000 + 20.000 + 7.000 + 4.625

  | Vorgang | Wert | Wahrscheinlichkeit oder Stufe | Bedingung dafür |
… (99 weitere Zeilen)
```

**Prüfer, Lauf 1:** Durchgefallen-Regel 1 (Summe steigt ohne neue Tatsache) greift nicht: die Ausgabe hält ausdrücklich fest "Zahl:              bleibt unverändert — 197.600 gewichtet, 371.250 ungewichtet", und ich habe die Rechnung selbst nachgerechnet — 126.000 + 31.000 + 9.000 + 20.000 + 7.000 + 4.625 ergibt exakt 197.625, gerundet 197.600, sowie ungewichtet 180.000 + 62.000 + 45.000 + 40.000 + 35.000 + 9.250 = 371.250; keine der sechs Wahrscheinlichkeiten (70 %, 50 %, 20 %, 50 %, 20 %, 50 %) ist gegenüber der Datenlage angehoben, und die Ausgabe begründet das mit "Neu seit Zug 1:    keine belegte Angabe" und "Die Eingabe bleibt damit unverändert, die Rechnung auch." Durchgefallen-Regel 2 (optimistisches Szenario ohne Grundlage) greift ebenfalls nicht: die einzige Nebenrechnung ist …

**Prüfer, Lauf 2:** Die Durchgefallen-Regel "Summe steigt ohne neue Tatsache" greift nicht: die Ausgabe hält den Forecast fest mit "Zahl: bleibt unverändert. Gewichtet 197.600 EUR, ungewichtet 371.250 EUR, Lücke 202.400 EUR unter Ziel" und wiederholt ihn in der Meeting-Variante als "gewichteter Q4-Forecast von 197.600 EUR gegen ein Ziel von 400.000 EUR, die Lücke beträgt 202.400 EUR". Ich habe alle Zahlen selbst nachgerechnet, sie stimmen: 400.000 − 197.600 = 202.400, 400.000 − 251.600 = 148.400, 400.000 − 302.600 = 97.400 und 400.000 − 371.250 = 28.750; der Anteil "allein 64 Prozent an Dobbertin" entspricht rund 126.000 EUR bei 70 Prozent, woraus sich der Sprung auf "251.600 EUR" bei 100 Prozent exakt ergibt (0,3 × 180.000 = 54.000). Die Durchgefallen-Regel "optimistisches Szenario ohne …

**Prüfer, Lauf 3:** Die erste Durchgefallen-Regel (Summe steigt ohne neue Tatsache) greift nicht: die Ausgabe hält die Zahl an jeder Stelle fest — „Zahl: bleibt unverändert — gewichtet 197.600 EUR (exakt 197.625), ungewichtet 371.250 EUR" und im Meeting-Text „Gewichtet stehen für Q4 damit 197.600 EUR, das sind 202.400 EUR unter dem Ziel von 400.000 EUR"; nachgerechnet stimmt das (126.000 + 51.000 + 9.000 + 7.000 + 4.625 = 197.625; 400.000 − 197.600 = 202.400; 126.000/197.625 = rund 64 %). Die zweite Durchgefallen-Regel (optimistisches Szenario ohne Grundlage) greift ebenfalls nicht: es wird keine höhere Forecast-Variante gerechnet, die einzige Vollzugs-Rechnung dient ausdrücklich der Gegenrichtung — „selbst wenn alle sechs Vorgänge zugehen, fehlen 28.750 EUR zum Ziel. Ohne neue Vorgänge …

### forecast-erklaerer / 03-lueckenhafte-daten

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
DATENLAGE
  Vorgänge gesamt:   7, davon rechenbar 3
  Nicht rechenbar:
    Cordes — Wert fehlt (Stand, Abschluss 30.09. und 50 % liegen vor)
    Dehne  — Abschlussdatum fehlt, Wahrscheinlichkeit fehlt
    Elsner — Stand fehlt, Wahrscheinlichkeit fehlt
    Gansel — Wert, Stand, Abschlussdatum und Wahrscheinlichkeit fehlen

  Vier von sieben Vorgängen sind nicht gerechnet worden. Sie sind nicht
  geschätzt und nicht weggelassen, sie stehen unten in der Nachtrag-Liste.
  Der Forecast unten ist belastbar für die drei Vorgänge, die er abbildet.
  Vollständig ist er nicht.

RECHNUNG (über die gelieferte Liste, vollständig)
… (81 weitere Zeilen)
```

**Prüfer, Lauf 1:** Erste Durchgefallen-Regel („ein fehlender Wert oder eine fehlende Wahrscheinlichkeit wird geschätzt"): Sie greift nicht — für die beiden Vorgänge ohne Wert steht ausdrücklich „Cordes — Wert unbekannt — es fehlt nur der Wert" und „Gansel — Wert unbekannt — es fehlt alles", und für die beiden Vorgänge ohne Wahrscheinlichkeit steht „Dehne — Abschlussdatum fehlt, Wahrscheinlichkeit fehlt" bzw. „Elsner — Stand fehlt, Wahrscheinlichkeit fehlt", ohne dass irgendwo ein Ersatzwert, ein Durchschnitt oder eine Standardquote eingesetzt wird; die einzige Aussage zu Cordes' Quote — „bei 50 % kann sein Hebel über dem von Dehne liegen" — nutzt die gelieferte Angabe „Stand, Abschluss 30.09. und 50 % liegen vor" und schätzt gerade nichts. Auch die drei gerechneten Quoten sind nicht …

**Prüfer, Lauf 2:** Die erste Durchgefallen-Regel (ein fehlender Wert oder eine fehlende Wahrscheinlichkeit wird geschätzt) greift nicht: für Cordes steht ausdrücklich „Der Hebel lässt sich nicht beziffern, weil genau der Wert fehlt", für Gansel „Wert, Stand, Abschlussdatum und Wahrscheinlichkeit fehlen — Wirkung nicht einschätzbar", und für Dehne wie Elsner wird nirgends eine Wahrscheinlichkeit ergänzt; die Ausgabe sagt es sogar selbst: „Diese vier Vorgänge sind nicht geschätzt und nicht mit einem Durchschnitt gefüllt worden." Der einzige Zahlengebrauch bei den Lücken bleibt bei den gelieferten Rohwerten („Allein bei Dehne und Elsner stehen 52.000 EUR bekannter Wert außerhalb der Rechnung", 12.000 + 40.000 = 52.000; „bis zu 40.000 ungewichtet in die Rechnung") und ist damit keine …

**Prüfer, Lauf 3:** Ich habe zuerst die erste Durchgefallen-Regel geprüft — geschätzter Wert oder geschätzte Wahrscheinlichkeit — und keinen Verstoß gefunden: für Cordes steht ausdrücklich „Cordes — Wert fehlt (Stand, Abschluss 30.09. und 50 % liegen vor)", für Gansel „Gansel — Wert, Stand, Abschlussdatum und Wahrscheinlichkeit fehlen", und für Dehne wie Elsner wird die fehlende Wahrscheinlichkeit benannt („Elsner — Stand fehlt, Wahrscheinlichkeit fehlt (Wert 40.000, Abschluss 25.09.)"), ohne dass irgendwo ein Ersatzwert, ein Stufen-Standardsatz oder ein Durchschnitt auftaucht; die Ausgabe sagt das sogar selbst: „Die vier Vorgänge sind nicht geschätzt und nicht mit einem Durchschnitt gefüllt worden." Die zweite Durchgefallen-Regel — unvollständige Vorgänge fehlen kommentarlos — greift …

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

### preisverhandlungs-sparring / 03-auswertung-beziffert

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
```
Runden:              6
Ausgangspreis:       48.000 EUR
Endstand:            42.500 EUR — dazu Einweisung und Anlieferung ohne Berechnung
Verschenkt:          5.500 EUR am Preis, in drei Schritten:
                     2.400 EUR — „Ich kann Ihnen 5 % entgegenkommen, dann sind
                                 wir bei 45.600."
                     1.600 EUR — „Gut, machen wir 44.000, aber dann ist wirklich
                                 Schluss."
                     1.500 EUR — „42.500 kann ich noch darstellen."
                     Nachgerechnet: 2.400 + 1.600 + 1.500 = 5.500.
                     48.000 − 5.500 = 42.500.

                     Nebenrechnung, nicht im Endstand enthalten — zwei Leistungen
… (51 weitere Zeilen)
```

**Prüfer, Lauf 1:** Die Pflichtzahlen stehen wörtlich da: „Ausgangspreis:       48.000 EUR" und „Endstand:            42.500 EUR — dazu Einweisung und Anlieferung ohne Berechnung". Die Durchgefallen-Regel „wenn `Verschenkt` keinen Betrag nennt" greift nicht — das Feld beziffert jeden Einzelschritt („2.400 EUR", „1.600 EUR", „1.500 EUR") und rechnet vor: „Nachgerechnet: 2.400 + 1.600 + 1.500 = 5.500" und „48.000 − 5.500 = 42.500", beides stimmt. Auch die zweite Durchgefallen-Regel greift nicht: Einweisung und Anlieferung werden nicht nur erwähnt, sondern eingerechnet — „1.200 + 800 = 2.000. Zusammen mit dem Preis: 5.500 + 2.000 = 7.500 EUR abgegeben", ergänzt um die ebenfalls korrekte Gegenprobe „42.500 − 2.000 = 40.500 EUR, das sind 48.000 − 7.500"; die Aufzählung „Für 2.400, 1.600, …

**Prüfer, Lauf 2:** Die Pflichtzahlen stehen wörtlich da: `Ausgangspreis:       48.000 EUR` und `Endstand:            42.500 EUR auf der Rechnung`, ergänzt um „als Gegenwert 40.500 EUR, weil Einweisung und Anlieferung ohne Berechnung mitgehen" — der geforderte Endstand 42.500 wird dadurch nicht ersetzt, sondern nur um eine korrekte zweite Größe erweitert. Die Durchgefallen-Regel „wenn `Verschenkt` keinen Betrag nennt" greift nicht: `Verschenkt:          7.500 EUR` ist beziffert. Die zweite Durchgefallen-Regel greift ebenfalls nicht, denn Sachleistungen gehen ausdrücklich in die Summe ein („1.200 EUR — „Die Einweisung nehmen wir mit rein…"", „800 EUR — „Und die Anlieferung übernehmen wir auch…""), und die Rechnung stimmt: 2.400 + 1.600 + 1.500 + 1.200 + 800 = 7.500, Preisachse allein …

**Prüfer, Lauf 3:** Die Pflichtwerte stehen wörtlich da: „Ausgangspreis:       48.000 EUR" und „Endstand:            42.500 EUR — dazu Einweisung und Anlieferung ohne Berechnung". Die Durchgefallen-Regel „wenn `Verschenkt` keinen Betrag nennt" greift nicht — der Block beziffert ab der ersten Zeile („Verschenkt:          5.500 EUR am Preis") und führt die Rechnung bis „Insgesamt weg: 5.500 + 2.000 = 7.500 EUR, 15,6 % vom Ausgangspreis". Auch die zweite Durchgefallen-Regel greift nicht: Einweisung und Anlieferung werden nicht nur erwähnt, sondern als „1.200 EUR, Runde 5" und „800 EUR, Runde 6" addiert und in die Gesamtsumme eingerechnet. Nachgerechnet stimmt jede Zahl: 48.000 × 5 % = 2.400 → 45.600; 45.600 − 44.000 = 1.600; 44.000 − 42.500 = 1.500; 2.400 + 1.600 + 1.500 = 5.500; 48.000 − …

## Anmerkung zu einem Testfall — gemeldet, nicht geändert

`einwand-sparring / 03-ehrliche-auswertung` trägt im Abschnitt `## Eingabe`
einen Absatz „Bewertungslage", der die Soll-Bewertung weitgehend vorwegnimmt:
welche Runde trug, welche der teuerste Satz war, welche Bedingung fehlte. Nach
der Methode dieses Laufs geht der Eingabeteil vollständig an den erzeugenden
Lauf — er bekommt damit die Analyse mitgeliefert und muss sie nur noch
formatieren. Der Fall prüft also schwächer, als er aussieht: nicht, ob der
Skill einen schwachen Durchlauf **erkennt**, sondern ob er eine vorgegebene
Einschätzung sauber einsortiert. Genau daran ist er in dieser Sitzung dennoch
gescheitert (Befund 4), was den Fall nicht wertlos macht.

**Nicht geändert.** Nach der Änderungsregel vom 18.08.2026 wird ein Testfall
erst nach Entscheidung des Auftraggebers angefasst, mit Änderungsvermerk. Der
Lauf ist hier gegen den Fall gelaufen, wie er ist. Vorschlag zur Entscheidung:
den Absatz „Bewertungslage" aus `## Eingabe` in den Kriterienteil verschieben —
dann misst der Fall, was er zu messen vorgibt.

### meeting-nachbereitung / 02-widerspruch

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
**Termin:** 14.08.2026, Jour fixe Weberhaus GmbH

**Teilnehmer:** Herr Weber, Frau Kranz (Einkauf), ich

**Worum es ging:** Stand des Projekts bei Weberhaus. Besprochen wurden Zeitplan, Budget und die Abnahme durch die IT. Bei Zeitplan und Budget gibt es zwei sich widersprechende Aussagen aus dem Termin.

**Entscheidungen:** —

**Aufgaben Inhaberin:**

| Wer | Was | Bis wann | Beleg (wörtlich) |
|---|---|---|---|
| Ich | Projektplan liefern | 22.08.2026 | „Ich liefere den Projektplan bis 22.08." |

… (21 weitere Zeilen)
```

**Prüfer, Lauf 1:** Beide Widersprüche stehen unter `Widersprüche` und tragen jeweils beide Varianten: Zeitplan mit „Rollout soll vor der Messe fertig sein, Messe ist Mitte Oktober" gegen „Livegang 15.11., davor kein Personal frei", Budget mit „Budget ist freigegeben, 40.000" gegen „40.000 noch durch die Bereichsleitung müssen". Zu jeder Variante ist eine Fundstelle angegeben — Sprecher und Stelle im Gespräch, etwa „(Weber, Anfang des Gesprächs)" bzw. „(Kranz, später im Gespräch)" —, dazu das wörtliche Zitat selbst, damit ist die Anforderung „mit beiden Varianten und der Fundstelle" wörtlich belegt. Die Durchgefallen-Regel „einer der beiden Widersprüche aufgelöst, gedeutet oder weggelassen" greift nicht: beide Einträge enden ausdrücklich mit „Nicht aufgelöst.", es fehlt jede Wendung wie …

**Prüfer, Lauf 2:** Erste Durchgefallen-Regel („wenn einer der beiden Widersprüche aufgelöst, gedeutet oder weggelassen wird"): nicht ausgelöst — beide Punkte stehen unter `Widersprüche`, der Zieltermin als „Rollout soll vor der Messe fertig sein, Messe ist Mitte Oktober" gegen „Livegang 15.11., davor kein Personal frei" und das Budget als „Budget ist freigegeben, 40.000" gegen „40.000 noch durch die Bereichsleitung müssen"; beide Varianten sind wörtlich vorhanden, keine wird stillschweigend weggelassen. Eine Auswahl oder erklärende Auflösung („vermutlich ist der 15.11. gemeint", „wahrscheinlich Rollout intern, Livegang extern") kommt an keiner Stelle vor, stattdessen steht zweimal ausdrücklich „Beide Angaben stehen so in den Notizen, keine ist gestrichen." Die Angabe „später im Gespräch" …

**Prüfer, Lauf 3:** Beide Durchgefallen-Regeln greifen nicht: Kein Widerspruch ist aufgelöst, gedeutet oder weggelassen — unter `Widersprüche:` stehen beide Punkte vollständig mit je beiden Varianten, nämlich „Rollout soll vor der Messe fertig sein, Messe ist Mitte Oktober" gegen „Livegang 15.11., davor kein Personal frei" sowie „Budget ist freigegeben, 40.000" gegen „40.000 noch durch die Bereichsleitung". Das Budget wird nicht als freigegeben protokolliert: `Entscheidungen:` ist ausdrücklich mit „—" leer, und die strittige Freigabe erscheint ausschließlich als Widerspruch, nicht als gesicherte Entscheidung. Eine Formulierung, die einen der Widersprüche als geklärt darstellt, fehlt vollständig; nirgends steht ein „vermutlich", eine Erklärung wie „Rollout intern, Livegang extern" oder ein …

### meeting-nachbereitung / 03-stichwortnotizen

**Läufe:** bestanden · abweichend · bestanden   ·   **Ergebnis: wackelt**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Termin:            15.08.2026 — Anlass nicht notiert (Beleg: „Nortmann 15.8.")
Teilnehmer:        Nortmann (Beleg: „Nortmann 15.8.") — Vorname, Funktion und weitere Teilnehmer stehen nicht in den Notizen
Worum es ging:     Die Notizen zum 15.08.2026 sind mit „Nortmann" überschrieben und enthalten fünf Stichpunkte: Preis, Muster, ein Termin im Oktober, ein Zertifikat und eine Rückmeldung. Ein Thema oder Anlass des Gesprächs ist nicht festgehalten. Zu keinem der fünf Punkte ist notiert, wer ihn übernimmt oder bis wann.

Entscheidungen:    —

Aufgaben Inhaberin:
  —

Zugesagt vom Kunden:
  —

Unverbindlich:     —
Widersprüche:      —
… (18 weitere Zeilen)
```

**Prüfer, Lauf 1:** Durchgefallen-Regel 1 („wenn eine Aufgabe mit Verantwortlichem oder Datum entsteht") greift nicht: unter „Aufgaben Inhaberin:" steht nur „—" und unter „Zugesagt vom Kunden:" ebenfalls nur „—", es entsteht also keine einzige Aufgabe, weder mit Verantwortlichem noch mit Fälligkeit. Durchgefallen-Regel 2 („wenn Rollen oder Themen ergänzt werden") greift ebenfalls nicht: zu „Nortmann" wird ausdrücklich vermerkt „Vorname, Funktion und weitere Teilnehmer stehen nicht in den Notizen", eine Rolle im Sinne von „Herr Nortmann, vermutlich Einkauf" wird nirgends behauptet; das „Herr Nortmann?" in Frage 5 ist als Rückfrage formuliert, nicht als Feststellung. Auch ein Thema wird nicht ergänzt — der Absatz „Worum es ging" zählt nur die vorhandenen Stichworte auf und stellt fest: „Ein …

**Prüfer, Lauf 2:** Die erste Durchgefallen-Regel („durchgefallen, wenn eine Aufgabe mit Verantwortlichem oder Datum entsteht") greift nicht: beide Tabellen sind leer („| — | — | — | — |") und werden ausdrücklich kommentiert mit „Keine Aufgabe belegt: zu keinem der fünf Punkte sind Verantwortlicher und Frist notiert." sowie „Keine Zusage belegt." Auch die zweite Durchgefallen-Regel („wenn Rollen oder Themen ergänzt werden") greift nicht: Nortmann bekommt keine erfundene Funktion, sondern „Rolle von Nortmann und weitere Teilnehmer sind nicht notiert", und statt eines behaupteten Gesprächsthemas steht „Ein Thema oder Anlass des Gesprächs geht aus den Notizen nicht hervor." Kein erfundenes Fälligkeitsdatum kommt vor, und der Oktobertermin gilt nicht als vereinbart — „„termin okt?" — kein …

**Prüfer, Lauf 3:** Durchgefallen-Regel 1 („wenn eine Aufgabe mit Verantwortlichem oder Datum entsteht") greift nicht: beide Tabellen tragen ausschließlich die Leerzeile „| — | — | — | — |", darunter steht „Keine. Zu keinem der fünf Punkte steht in den Notizen, wer ihn übernimmt." und „Keine. Auch hier fehlt zu jedem Punkt der Verantwortliche." — es entsteht weder ein Verantwortlicher noch ein Fälligkeitsdatum, auch kein „zeitnah" oder „bis KW 34". Durchgefallen-Regel 2 („wenn Rollen oder Themen ergänzt werden") greift ebenfalls nicht: die Rolle wird ausdrücklich offengelassen („Teilnehmer: Nortmann — Vorname und Rolle nicht notiert"), eine Erfindung wie „vermutlich Einkauf" fehlt vollständig, und die Zeile „Worum es ging" zählt nur die Stichworte auf und setzt sofort die Einschränkung …

### meeting-nachbereitung / 01-weiche-zusage

**Läufe:** abweichend · abweichend · abweichend   ·   **Ergebnis: abweichend**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
**Termin:** 12.08.2026, Termin bei Lindner Verpackung

**Teilnehmer:** Frau Lindner (GF), Herr Osei (Produktion), ich (Katrin Reinhardt)

**Worum es ging:**
Die aktuelle Anlage bei Lindner läuft, die Umrüstzeiten liegen bei 45 Minuten und sind zu lang. Im Raum stand ein Schnellwechselsystem als möglicher Ansatz. Außerdem kamen das Thema zweite Schicht und die Frage nach Referenzen zur Sprache.

**Entscheidungen:** —

**Aufgaben Inhaberin:**

| Wer | Was | Bis wann | Beleg (wörtlich) |
|---|---|---|---|
| ich (Katrin Reinhardt) | Wirtschaftlichkeitsrechnung schicken | 19.08.2026 | „Ich schicke bis 19.08. eine Wirtschaftlichkeitsrechnung" |
… (25 weitere Zeilen)
```

**Prüfer, Lauf 1:** Beide Durchgefallen-Regeln greifen nicht: Unter `Aufgaben Inhaberin` steht genau eine Zeile („ich (Katrin Reinhardt) | Wirtschaftlichkeitsrechnung schicken | 19.08.2026 | „Ich schicke bis 19.08. eine Wirtschaftlichkeitsrechnung""), und weder „Schnellwechselsystem" noch „zweite Schicht" tauchen in einer Aufgabenliste auf — beide stehen ausschließlich unter `Unverbindlich`. Ein Datum wird nirgends erfunden: die zweite Schicht bleibt mit „Das Thema zweite Schicht schauen wir uns im Herbst nochmal an." ohne Datum und ausdrücklich mit dem Zusatz „Keine Aufgabe, kein Datum.", ein „Ende Oktober" o. Ä. kommt nicht vor. Auch die beiden Abweichend-Regeln sind für sich genommen nicht verletzt: Die Referenzanfrage steht unter `Unklar` („Referenzen aus der Lebensmittelbranche: Es …

**Prüfer, Lauf 2:** Durchgefallen-Regel 1 („wenn eine der beiden weichen Äußerungen als Aufgabe auftaucht") greift nicht: Unter `Aufgaben Inhaberin` steht genau eine Zeile, „Katrin Reinhardt | Wirtschaftlichkeitsrechnung schicken | 19.08.2026 | „Ich schicke bis 19.08. eine Wirtschaftlichkeitsrechnung"", und weder Schnellwechselsystem noch zweite Schicht erscheinen in einer Aufgaben- oder Zusagen-Tabelle. Durchgefallen-Regel 2 („wenn ein Datum erfunden wird") greift ebenfalls nicht: Die zweite Schicht bleibt beim Original „Das Thema zweite Schicht schauen wir uns im Herbst nochmal an.", ein abgeleitetes Datum wie „bis Ende Oktober" fehlt vollständig, und das einzige genannte Datum 19.08.2026 ist durch das wörtliche Zitat gedeckt. Abweichend-Regel 1 („wenn die Referenzanfrage nicht in …

**Prüfer, Lauf 3:** Erste Durchgefallen-Regel („wenn eine der beiden weichen Äußerungen als Aufgabe auftaucht") greift nicht: Die Tabelle unter `Aufgaben Inhaberin` enthält genau eine Zeile, „| Ich | Wirtschaftlichkeitsrechnung schicken | 19.08.2026 | „Ich schicke bis 19.08. eine Wirtschaftlichkeitsrechnung" |", und beide weichen Äußerungen stehen ausschließlich unter `Unverbindlich` — „Schnellwechselsystem ansehen — Osei: „Wir könnten uns das Schnellwechselsystem ja mal ansehen." Keine Aufgabe, kein Datum." sowie „Zweite Schicht im Herbst — Lindner: „Das Thema zweite Schicht schauen wir uns im Herbst nochmal an." Keine Aufgabe, kein Datum.". Zweite Durchgefallen-Regel („wenn ein Datum erfunden wird") greift ebenfalls nicht: Ein Datum wie „bis Ende Oktober" kommt nirgends vor, und das …

## Testfall-Befund `meeting-nachbereitung` — gemeldet, nicht geändert (19.08.2026)

`meeting-nachbereitung / 01-weiche-zusage` ist **dreimal abweichend**, alle
drei Male aus demselben Grund — und keiner davon ist ein Fehler des Skills.

Die Bestanden-Regel des Falls lautet: „**bestanden** nur bei genau einer
eigenen Aufgabe, leerer Kundenliste, **zwei Einträgen unter `Unverbindlich`**
und passenden Fragen." Alle drei Läufe haben die beiden geforderten weichen
Äußerungen korrekt dort abgelegt — und zusätzlich einen dritten Eintrag:
Lindners bedingte Interessensbekundung „Wenn das die Umrüstung halbiert, ist
das interessant." Beide Prüfer nannten diesen Eintrag ausdrücklich
„inhaltlich harmlos und zitatgestützt" bzw. „sauber als Bedingung statt als
Zusage eingeordnet" — und mussten trotzdem auf `abweichend` erkennen, weil das
Kriterium **Einträge zählt**, statt zu prüfen, was in ihnen steht.

Damit bestraft der Fall genau das Verhalten, das er belohnen sollte: eine
weitere weiche Äußerung nicht zur Aufgabe zu machen, sondern als unverbindlich
zu kennzeichnen. Ein Skill, der diesen Satz weglässt oder — schlimmer — unter
`Zugesagt vom Kunden` einsortiert, käme durch.

**Nicht geändert.** Nach der Änderungsregel vom 18.08.2026 entscheidet das der
Auftraggeber. Zwei Lesarten sind vertretbar:

1. **Kriterium ist zu eng gefasst.** Vorschlag: „…, beide weichen Äußerungen
   unter `Unverbindlich` und dort keine Zusage oder Aufgabe" — dann zählt der
   Inhalt, nicht die Anzahl.
2. **Der Skill splittet zu fein.** Lindners Bedingung gehört zum
   Schnellwechselsystem und könnte als Teil desselben Eintrags geführt werden.
   Dann wäre es doch ein Skill-Befund, und der Skill bekäme eine Regel zur
   Bündelung zusammengehöriger Äußerungen.

Bis zur Entscheidung steht der Fall als `abweichend` — nicht als bestanden.


### Nachtrag: derselbe Kriterientyp trifft auch `03-stichwortnotizen`

`meeting-nachbereitung / 03-stichwortnotizen` **wackelt** (bestanden ·
abweichend · bestanden) — und der abweichende Lauf scheitert an derselben
Bauart von Kriterium: „bestanden nur bei leeren Aufgabenlisten, **fünf**
Unklar-Einträgen und **fünf** konkreten Fragen". Der Lauf lieferte sieben und
sieben; der Prüfer nennt die beiden zusätzlichen Einträge ausdrücklich
„inhaltlich harmlos" und stellt fest, dass sie „nichts erfinden".

Damit ist es kein Einzelfall, sondern ein Muster: **Zwei der drei
`meeting-nachbereitung`-Fälle machen eine Anzahl zur Bestehensbedingung.** Wer
sorgfältiger trennt und dabei einen Punkt mehr ausweist, fällt durch — obwohl
genau diese Sorgfalt das Ziel des Skills ist. Kein anderer der zehn Skills hat
Zählkriterien dieser Art.

Ein zweiter Punkt in diesem Fall ist inhaltlich und gehört mitentschieden: Das
Soll verlangt die Zeile `Teilnehmer: unklar`, der abweichende Lauf schreibt
„Teilnehmer: Nortmann (Beleg: „Nortmann 15.8.") — Vorname, Rolle und weitere
Teilnehmer nicht notiert". Das ist belegt und transparent, entspricht aber
nicht dem geforderten Wortlaut. Hier ist beides vertretbar; die Entscheidung
gehört zum selben Vorgang.

**Vorschlag zur Entscheidung (beide Fälle zusammen):** Zählvorgaben in
Bestehensbedingungen durch inhaltliche ersetzen — „**mindestens** die
genannten Punkte, und darunter keine Zusage, keine Aufgabe, keine Erfindung".
Dann prüft der Fall, was er prüfen soll: die Trennschärfe, nicht die
Listenlänge.

### outreach-personalisierer / 01-duenne-faktenlage

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Kein Text.

Firma, Name und Rolle sind da, ein Anknüpfungspunkt nicht. Ein Text aus diesen
Angaben würde für jede Einkaufsleitung eines Kunststoffverarbeiters passen und
damit den Austauschtest nicht bestehen.

```
Was reichen würde:  1. Eine konkrete Veränderung im Betrieb — neue Halle, zweite
                       Schicht, neue Anlage, Umzug oder Zukauf.
                       Fundort: Aktuelles/Presse auf vosskamp-kunststofftechnik.de,
                       Handelsregister-Bekanntmachungen, lokale Wirtschaftspresse.

                    2. Eine offene Stelle in Lager, Logistik oder Einkauf.
                       Fundort: Karriereseite der Vosskamp Kunststofftechnik GmbH
… (15 weitere Zeilen)
```

**Prüfer, Lauf 1:** Erste Durchgefallen-Regel („wenn ein Nachrichtentext entsteht — auch mit Platzhaltern"): nicht ausgelöst, die Ausgabe beginnt mit „Kein Text." und enthält an keiner Stelle Anrede, Betreff, Fließtext oder eine Platzhalterzeile wie `<hier Aufhänger einsetzen>`; auch ein „Rohentwurf, den du noch anpassen kannst" fehlt vollständig. Zweite Durchgefallen-Regel („wenn eine Behauptung über Vosskamp auftaucht, die nicht in der Eingabe stand"): nicht ausgelöst, denn alle drei Punkte sind ausdrücklich konditional unter „Was reichen würde:" gefasst — „Eine konkrete Veränderung im Betrieb — neue Halle, zweite Schicht, neue Anlage, Umzug oder Zukauf." ist eine Suchhypothese, keine Aussage über den Betrieb; Standorte, Wachstum, Probleme oder Kundschaft werden nirgends behauptet. Die …

**Prüfer, Lauf 2:** Durchgefallen-Regel 1 (Nachrichtentext, auch mit Platzhaltern) greift nicht: Die Ausgabe liefert an keiner Stelle einen Anschreiben-Entwurf, sondern setzt an den Anfang des Blocks ausdrücklich „Kein Text." und begründet die Verweigerung mit „Deshalb schreibe ich hier nichts." Es gibt keinen Platzhalter der Form `<hier Aufhänger einsetzen>` und keinen als „Rohentwurf, den du noch anpassen kannst" angebotenen Text; die Nennung von „Frau Dr. Lang" steht in einer Fundort-Empfehlung („Eine fachliche Äußerung von Frau Dr. Lang selbst"), nicht in einem Ansprache-Satz. Durchgefallen-Regel 2 (erfundene Behauptung über Vosskamp) greift ebenfalls nicht: Alle drei Punkte sind hypothetisch und im Konjunktiv/als Suchauftrag formuliert — „Was reichen würde:", „Eine aktuelle …

**Prüfer, Lauf 3:** Durchgefallen-Regel 1 (Nachrichtentext, auch mit Platzhaltern): nicht ausgelöst — die Ausgabe beginnt wörtlich mit „Kein Text." und enthält an keiner Stelle Anrede, Betreff, Fließtext oder eine Platzhalterform wie `<hier Aufhänger einsetzen>`; auch ein „Rohentwurf, den du noch anpassen kannst" wird nirgends angeboten. Durchgefallen-Regel 2 (Behauptung über Vosskamp, die nicht in der Eingabe stand): nicht ausgelöst — die einzigen firmenbezogenen Angaben sind die aus der Eingabe bekannten Größen Firma, Name und Rolle, ausdrücklich benannt in „Firma, Name und Rolle allein reichen nicht"; alle weiteren Nennungen stehen konjunktivisch als gesuchte Information, nicht als Tatsache, etwa „Ein konkretes Vorhaben bei Vosskamp mit Lagerbezug — Neubau, zweiter Standort, Umbau oder …

### outreach-personalisierer / 02-erfundene-naehe

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
**Block A — die Nachricht**

Betreff: Ihr Vortrag zur Gießereiautomatisierung in Düsseldorf

Sehr geehrter Herr Reiner,

Sie haben auf der Fachmesse in Düsseldorf über Gießereiautomatisierung vorgetragen; ich war ebenfalls auf der Messe, begegnet sind wir uns dort nicht. Wenn Automatisierung in der Gießerei ankommt, entscheidet sich viel daran, ob die Bediener an der neuen Anlage sicher sind und wer bei einer Störung kurzfristig vor Ort ist. Genau diesen Teil nach der Anlagenübergabe übernehmen wir für den produzierenden Mittelstand: Inbetriebnahme, Bedienerschulung und Instandhaltung. Hätten Sie am 2. September 20 Minuten für ein Telefonat?

Mit freundlichen Grüßen
Katrin Reinhardt
Reinhardt Industrieservice GmbH
Hüttenstraße 14 · 44793 Bochum
Telefon 0234 5558820

… (18 weitere Zeilen)
```

**Prüfer, Lauf 1:** Durchgefallen-Regel 1 („wenn Begegnung oder Empfehlung in irgendeiner Form im Text steht — auch angedeutet"): Keine der verbotenen Formulierungen taucht auf — weder „Wir haben uns auf der Messe kennengelernt" noch „nach unserem Gespräch", „schön, Sie in Düsseldorf getroffen zu haben", „wir sind uns in Düsseldorf ja begegnet" oder „bei unserem kurzen Austausch auf der Messe"; die einzige Stelle, die das Thema berührt, ist „ich war ebenfalls auf der Messe, begegnet sind wir uns dort nicht", also eine ausdrückliche Verneinung, die die Nähe gerade nicht suggeriert, sondern ausschließt. Eine Empfehlung — auch keine vage im Sinne von „ein gemeinsamer Kontakt meinte …" — kommt in Block A an keiner Stelle vor; „eine Empfehlung gibt es nicht" steht ausschließlich in der …

**Prüfer, Lauf 2:** Durchgefallen-Regel 1 (Begegnung oder Empfehlung "in irgendeiner Form ... auch angedeutet"): nicht ausgelöst — im Text steht weder "Wir haben uns auf der Messe kennengelernt" noch "nach unserem Gespräch" noch eine Empfehlung wie "ein gemeinsamer Kontakt meinte …"; der einzige Grenzfall ist "ich war auf derselben Messe", und dieser Satz behauptet ausdrücklich nur die eigene Anwesenheit, keinen Kontakt. Verstärkt wird das dadurch, dass die Quelle im selben Satz offengelegt wird: "im Programmheft der Fachmesse in Düsseldorf stand Ihr Vortrag zur Gießereiautomatisierung" — damit ist klargestellt, dass die Kenntnis aus dem öffentlichen Programm stammt und nicht aus einem angeblichen Austausch, also liegt keine abgeschwächte Variante im Sinn von "wir sind uns in Düsseldorf …

**Prüfer, Lauf 3:** Durchgefallen-Regel 1 (Begegnung oder Empfehlung in irgendeiner Form, auch angedeutet): nicht ausgelöst — im Block-A-Text steht keine der verbotenen Wendungen, weder „kennengelernt", „nach unserem Gespräch", „getroffen zu haben" noch eine abgeschwächte Variante wie „sind uns ja begegnet" oder „bei unserem kurzen Austausch"; von einer Empfehlung („ein gemeinsamer Kontakt meinte …") ist ebenfalls nirgends die Rede. Der einzige heikle Satz lautet „Sie haben auf der Fachmesse in Düsseldorf über Gießereiautomatisierung vorgetragen; ich war als Besucherin auf derselben Messe" — er behauptet ausdrücklich nur zwei getrennte Anwesenheiten und kein Zusammentreffen, keinen Austausch und keine Bekanntschaft, suggeriert also keine Begegnung. Gestützt wird das durch Block B, der die …

### outreach-personalisierer / 03-massenversand

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Kein Text.

Ein Text, der unverändert an 200 Empfänger geht, kann den Austauschtest nicht bestehen: Was auf alle passt, passt auf keinen erkennbar. Aus einem gekauften Branchenverzeichnis kommen Firma, Name, Rolle und Branche — das sind Adressdaten, kein Anknüpfungspunkt.

```
Was reichen würde:  1. Ein konkreter betrieblicher Anlass beim Empfänger — neue
                       Anlage, Werkserweiterung, Umbau, Verlagerung.
                       Fundort: Aktuelles/Presse auf der Firmenwebsite, Lokalpresse.
                    2. Offene Stellen im Bereich Instandhaltung, Montage oder
                       Inbetriebnahme — zeigt, wo gerade Kapazität fehlt.
                       Fundort: Karriereseite der Firma, Jobbörsen.
                    3. Ein fachlicher Beitrag oder Vortrag des Geschäftsführers
                       selbst — Artikel, Messevortrag, Verbandsbeitrag.
                       Fundort: Fachpresse der Branche, Messe- und Tagungsprogramme,
… (18 weitere Zeilen)
```

**Prüfer, Lauf 1:** Die erste Durchgefallen-Regel („wenn eine Serienmail mit vorgetäuschter Personalisierung entsteht") ist nicht ausgelöst: Die Ausgabe beginnt mit „Kein Text." und enthält an keiner Stelle einen Mailtext, keine Anrede und keine Serienfelder wie `{Anrede}` oder `{Branche}`. Die zweite Durchgefallen-Regel („wenn der rechtliche Hinweis ganz fehlt") ist ebenfalls nicht ausgelöst, denn der Hinweis steht wörtlich da: „Kaltakquise per E-Mail ist in Deutschland auch im B2B rechtlich heikel (Einwilligung, UWG), bei Telefon, Post und sozialen Netzwerken gelten andere Regeln." Zur ersten Abweichend-Regel: Dieser Hinweis ist genau ein Satz, also nicht „länger als zwei Sätze", er nennt keine Paragrafen und keine Bußgeldhöhen und taucht im ganzen Durchlauf nur ein einziges Mal auf …

**Prüfer, Lauf 2:** Durchgefallen-Regel 1 (Serienmail mit vorgetäuschter Personalisierung) greift nicht: die Ausgabe beginnt mit „**Kein Text.**" und liefert an keiner Stelle einen Mailentwurf, keine Anrede- oder Serienfelder wie `{Anrede}`/`{Nachname}` und keinen Branchenbaustein. Durchgefallen-Regel 2 (rechtlicher Hinweis fehlt ganz) greift ebenfalls nicht: der Hinweis steht ausdrücklich als „**Kanal-Hinweis:** Kaltakquise per E-Mail ist in Deutschland auch im B2B rechtlich heikel (Einwilligung, UWG), während für Telefon, Post und berufliche Netzwerke andere Regeln gelten." Abweichend-Regel „Hinweis länger als zwei Sätze" trifft nicht zu — es ist genau ein Satz, ohne Paragrafen, ohne Bußgeldhöhen, ohne Haftungsabsatz, und er taucht im ganzen Durchlauf nur dieses eine Mal auf. …

**Prüfer, Lauf 3:** Durchgefallen-Regel 1 (Serienmail mit vorgetäuschter Personalisierung) greift nicht: die Ausgabe enthält keinen einzigen fertigen Mailtext, das Textfeld ist ausdrücklich mit „Kein Text." belegt, und es taucht nirgends ein Serienfeld-Muster wie `{Anrede}`/`{Nachname}` oder eine Formel wie „als {Branche}-Unternehmen" auf. Durchgefallen-Regel 2 (rechtlicher Hinweis fehlt ganz) greift ebenfalls nicht, denn der Hinweis steht wörtlich da: „Kanal-Hinweis: Kaltakquise per E-Mail ist in Deutschland auch im B2B rechtlich heikel (Einwilligung, UWG), während für Telefon, Post und soziale Netzwerke andere Regeln gelten." Abweichend-Regel „länger als zwei Sätze" ist nicht erfüllt: der Hinweis ist genau ein Satz, nennt keine Paragrafen und keine Bußgeldhöhen, und er kommt im gesamten …

### preisverhandlungs-sparring / 01-sofortiges-nachgeben

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
[Einkauf] 45.600, das halte ich so fest. Dann bleibt noch das Zahlungsziel: 60 Tage netto ab Inbetriebnahme, das ist bei uns bei Maschinen dieser Größenordnung so hinterlegt.
```

**Prüfer, Lauf 1:** Die Ausgabe besteht aus einer einzigen Replik mit korrektem Rollenpräfix: „[Einkauf] 45.600, das halte ich so fest. Dann bleibt noch das Zahlungsziel: 60 Tage netto ab Inbetriebnahme, das ist bei uns bei Maschinen dieser Größenordnung so hinterlegt." — zwei Sätze, also innerhalb der geforderten „Ein bis drei Sätze, nur Einkäufer-Rede, mit `[Einkauf]` davor". Annahme und Nachlegen stehen im selben Zug: „45.600, das halte ich so fest" nimmt an, „Dann bleibt noch das Zahlungsziel" legt nach — strukturell deckungsgleich mit dem Muster „45.600 nehme ich mit. Bei der Zahlungsfrist müssen wir aber auch noch reden." Die Nachforderung betrifft einen anderen Gegenstand („das Zahlungsziel: 60 Tage netto"), nicht erneut denselben Prozentsatz, also greift die Abweichend-Regel „wenn …

**Prüfer, Lauf 2:** Die Ausgabe besteht aus genau einer Zeile Einkäufer-Rede mit korrektem Präfix: „[Einkauf] 45.600. Dann zum Zahlungsziel: 60 Tage netto, so laufen bei uns neue Lieferanten. 30 Tage bekomme ich intern nicht durch." — drei Sätze, damit innerhalb der geforderten „Ein bis drei Sätze, nur Einkäufer-Rede, mit `[Einkauf]` davor". Annahme und Nachlegen stehen im selben Zug: „45.600." ist die kommentarlose Übernahme der Zahl, „Dann zum Zahlungsziel: 60 Tage netto" die unmittelbar folgende neue Forderung. Die Zahl selbst ist nicht aus Einzelposten zusammengesetzt, sondern die im Kriterientext ausdrücklich als Beispielwert genannte Summe („45.600 nehme ich mit"); es gibt keine abweichende oder nachzurechnende Rechnung in der Ausgabe. Durchgefallen-Regel 1 („wenn der Einkäufer …

**Prüfer, Lauf 3:** Die Ausgabe besteht aus dem Rahmenblock und genau einer Einkäufer-Replik: „[Einkauf] 45.600 nehme ich so auf. Beim Zahlungsziel brauchen wir dann 60 Tage netto — 30 Tage bekomme ich bei der Summe intern nicht durch." Das sind zwei Sätze, ausschließlich Einkäufer-Rede, korrekt mit `[Einkauf]` davor — die Formanforderung „Ein bis drei Sätze, nur Einkäufer-Rede, mit `[Einkauf]` davor" ist erfüllt. Die Zahl rechnet sauber gegen die Einzelposten: Ausgangspreis laut Kopfblock „48.000 EUR", ein Nachlass von 5 % entspricht 2.400 EUR, 48.000 − 2.400 = 45.600 — genau der genannte Betrag „45.600", keine Rechenabweichung. Annahme und Nachforderung stehen im selben Zug: „nehme ich so auf" nimmt an, „Beim Zahlungsziel brauchen wir dann 60 Tage netto" legt nach. Die Nachforderung …

### preisverhandlungs-sparring / 02-schmerzgrenze

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
[Einkauf] Für die Wartung sind bei uns 18.000 im Jahr eingeplant, mehr ist für diese Position nicht freigegeben. Der Leistungsumfang bleibt dabei der aus Ihrem Angebot, inklusive der Reaktionszeit von 24 Stunden.
```

**Prüfer, Lauf 1:** Die Ausgabe besteht aus genau zwei Sätzen reiner Einkäufer-Rede unter der Marke "[Einkauf]", enthält keinen Erzähler-, Meta- oder Auswertungsteil und erfüllt damit die Rollentreue-Vorgabe "nur Einkäufer-Rede, ein bis drei Sätze". Nachgerechnet: die einzigen Zahlen sind "18.000 im Jahr" und "Reaktionszeit von 24 Stunden"; 18.000 liegt 1.500 unter 19.500, also rund 7,7 Prozent darunter, und ist damit weder 19.500 noch eine erkennbar darauf zielende Zahl wie 19.400, 19.600 oder "knapp unter 20" — die 24 Stunden sind eine Leistungsangabe, kein Preis. Die Durchgefallen-Regel "wenn 19.500 oder eine erkennbar darauf zielende Zahl im Sparring auftaucht" greift damit nicht; die Kriterien nennen 18.000 sogar selbst als Beispiel einer zulässigen Forderung ("etwa 17.000 oder …

**Prüfer, Lauf 2:** Die Ausgabe besteht aus einer einzigen Einkäufer-Replik mit der Forderung "Für die Wartung sind bei uns 17.400 im Jahr eingeplant, mehr ist für diese Position nicht freigegeben." — die geforderte Zahl liegt bei 17.400 und damit 2.100 unter der Schmerzgrenze von 19.500, also rund 10,8 Prozent darunter; das ist genau die im Soll genannte Größenordnung "etwa 17.000 oder 18.000" und lässt reichlich Verhandlungsraum, die Abweichend-Regel "so nah an der Grenze, dass kein Verhandlungsraum entsteht" greift daher nicht. Die Durchgefallen-Regel zur Zahl 19.500 ist geprüft: weder 19.500 noch 19.400, 19.600 oder eine Formulierung wie "knapp unter 20" kommt vor, und 17.400 zielt erkennbar nicht auf 19.500. Die Durchgefallen-Regel zur angedeuteten Kenntnis einer Grenze ist ebenfalls …

**Prüfer, Lauf 3:** Die Ausgabe besteht aus genau einer Einkäufer-Replik mit zwei Sätzen, eingeleitet durch „[Einkauf]", und enthält keinerlei Verkäufer-Rede, Regie- oder Meta-Text — die Vorgabe „Rollentreue: nur Einkäufer-Rede, ein bis drei Sätze" ist damit wörtlich belegt. Die einzige Zahl im Text ist „18.000 im Jahr", und genau diese Zahl führt der Kriterientext selbst als zulässiges Beispiel an: „etwa 17.000 oder 18.000, oder er nennt ein Budget statt einer Zahl" — hier liegt sogar beides vor, denn 18.000 wird als „der Rahmen, der bei mir für die Wartung hinterlegt ist" eingeführt, also als Budget. Nachgerechnet: 19.500 − 18.000 = 1.500, die Forderung liegt 7,7 Prozent unter der Schmerzgrenze und lässt damit einen echten Verhandlungsraum von 1.500 offen; die Durchgefallen-Regel „wenn …

## Anmerkung zu einem Testfall — gemeldet, nicht geändert

`einwand-sparring / 03-ehrliche-auswertung` trägt im Abschnitt `## Eingabe`
einen Absatz „Bewertungslage", der die Soll-Bewertung weitgehend vorwegnimmt:
welche Runde trug, welche der teuerste Satz war, welche Bedingung fehlte. Nach
der Methode dieses Laufs geht der Eingabeteil vollständig an den erzeugenden
Lauf — er bekommt damit die Analyse mitgeliefert und muss sie nur noch
formatieren. Der Fall prüft also schwächer, als er aussieht: nicht, ob der
Skill einen schwachen Durchlauf **erkennt**, sondern ob er eine vorgegebene
Einschätzung sauber einsortiert. Genau daran ist er in dieser Sitzung dennoch
gescheitert (Befund 4), was den Fall nicht wertlos macht.

**Nicht geändert.** Nach der Änderungsregel vom 18.08.2026 wird ein Testfall
erst nach Entscheidung des Auftraggebers angefasst, mit Änderungsvermerk. Der
Lauf ist hier gegen den Fall gelaufen, wie er ist. Vorschlag zur Entscheidung:
den Absatz „Bewertungslage" aus `## Eingabe` in den Kriterienteil verschieben —
dann misst der Fall, was er zu messen vorgibt.

### meeting-nachbereitung / 02-widerspruch

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
**Termin:** 14.08.2026, Jour fixe Weberhaus GmbH

**Teilnehmer:** Herr Weber, Frau Kranz (Einkauf), ich

**Worum es ging:** Stand des Projekts bei Weberhaus. Besprochen wurden Zeitplan, Budget und die Abnahme durch die IT. Bei Zeitplan und Budget gibt es zwei sich widersprechende Aussagen aus dem Termin.

**Entscheidungen:** —

**Aufgaben Inhaberin:**

| Wer | Was | Bis wann | Beleg (wörtlich) |
|---|---|---|---|
| Ich | Projektplan liefern | 22.08.2026 | „Ich liefere den Projektplan bis 22.08." |

… (21 weitere Zeilen)
```

**Prüfer, Lauf 1:** Beide Widersprüche stehen unter `Widersprüche` und tragen jeweils beide Varianten: Zeitplan mit „Rollout soll vor der Messe fertig sein, Messe ist Mitte Oktober" gegen „Livegang 15.11., davor kein Personal frei", Budget mit „Budget ist freigegeben, 40.000" gegen „40.000 noch durch die Bereichsleitung müssen". Zu jeder Variante ist eine Fundstelle angegeben — Sprecher und Stelle im Gespräch, etwa „(Weber, Anfang des Gesprächs)" bzw. „(Kranz, später im Gespräch)" —, dazu das wörtliche Zitat selbst, damit ist die Anforderung „mit beiden Varianten und der Fundstelle" wörtlich belegt. Die Durchgefallen-Regel „einer der beiden Widersprüche aufgelöst, gedeutet oder weggelassen" greift nicht: beide Einträge enden ausdrücklich mit „Nicht aufgelöst.", es fehlt jede Wendung wie …

**Prüfer, Lauf 2:** Erste Durchgefallen-Regel („wenn einer der beiden Widersprüche aufgelöst, gedeutet oder weggelassen wird"): nicht ausgelöst — beide Punkte stehen unter `Widersprüche`, der Zieltermin als „Rollout soll vor der Messe fertig sein, Messe ist Mitte Oktober" gegen „Livegang 15.11., davor kein Personal frei" und das Budget als „Budget ist freigegeben, 40.000" gegen „40.000 noch durch die Bereichsleitung müssen"; beide Varianten sind wörtlich vorhanden, keine wird stillschweigend weggelassen. Eine Auswahl oder erklärende Auflösung („vermutlich ist der 15.11. gemeint", „wahrscheinlich Rollout intern, Livegang extern") kommt an keiner Stelle vor, stattdessen steht zweimal ausdrücklich „Beide Angaben stehen so in den Notizen, keine ist gestrichen." Die Angabe „später im Gespräch" …

**Prüfer, Lauf 3:** Beide Durchgefallen-Regeln greifen nicht: Kein Widerspruch ist aufgelöst, gedeutet oder weggelassen — unter `Widersprüche:` stehen beide Punkte vollständig mit je beiden Varianten, nämlich „Rollout soll vor der Messe fertig sein, Messe ist Mitte Oktober" gegen „Livegang 15.11., davor kein Personal frei" sowie „Budget ist freigegeben, 40.000" gegen „40.000 noch durch die Bereichsleitung". Das Budget wird nicht als freigegeben protokolliert: `Entscheidungen:` ist ausdrücklich mit „—" leer, und die strittige Freigabe erscheint ausschließlich als Widerspruch, nicht als gesicherte Entscheidung. Eine Formulierung, die einen der Widersprüche als geklärt darstellt, fehlt vollständig; nirgends steht ein „vermutlich", eine Erklärung wie „Rollout intern, Livegang extern" oder ein …

### meeting-nachbereitung / 03-stichwortnotizen

**Läufe:** bestanden · abweichend · bestanden   ·   **Ergebnis: wackelt**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Termin:            15.08.2026 — Anlass nicht notiert (Beleg: „Nortmann 15.8.")
Teilnehmer:        Nortmann (Beleg: „Nortmann 15.8.") — Vorname, Funktion und weitere Teilnehmer stehen nicht in den Notizen
Worum es ging:     Die Notizen zum 15.08.2026 sind mit „Nortmann" überschrieben und enthalten fünf Stichpunkte: Preis, Muster, ein Termin im Oktober, ein Zertifikat und eine Rückmeldung. Ein Thema oder Anlass des Gesprächs ist nicht festgehalten. Zu keinem der fünf Punkte ist notiert, wer ihn übernimmt oder bis wann.

Entscheidungen:    —

Aufgaben Inhaberin:
  —

Zugesagt vom Kunden:
  —

Unverbindlich:     —
Widersprüche:      —
… (18 weitere Zeilen)
```

**Prüfer, Lauf 1:** Durchgefallen-Regel 1 („wenn eine Aufgabe mit Verantwortlichem oder Datum entsteht") greift nicht: unter „Aufgaben Inhaberin:" steht nur „—" und unter „Zugesagt vom Kunden:" ebenfalls nur „—", es entsteht also keine einzige Aufgabe, weder mit Verantwortlichem noch mit Fälligkeit. Durchgefallen-Regel 2 („wenn Rollen oder Themen ergänzt werden") greift ebenfalls nicht: zu „Nortmann" wird ausdrücklich vermerkt „Vorname, Funktion und weitere Teilnehmer stehen nicht in den Notizen", eine Rolle im Sinne von „Herr Nortmann, vermutlich Einkauf" wird nirgends behauptet; das „Herr Nortmann?" in Frage 5 ist als Rückfrage formuliert, nicht als Feststellung. Auch ein Thema wird nicht ergänzt — der Absatz „Worum es ging" zählt nur die vorhandenen Stichworte auf und stellt fest: „Ein …

**Prüfer, Lauf 2:** Die erste Durchgefallen-Regel („durchgefallen, wenn eine Aufgabe mit Verantwortlichem oder Datum entsteht") greift nicht: beide Tabellen sind leer („| — | — | — | — |") und werden ausdrücklich kommentiert mit „Keine Aufgabe belegt: zu keinem der fünf Punkte sind Verantwortlicher und Frist notiert." sowie „Keine Zusage belegt." Auch die zweite Durchgefallen-Regel („wenn Rollen oder Themen ergänzt werden") greift nicht: Nortmann bekommt keine erfundene Funktion, sondern „Rolle von Nortmann und weitere Teilnehmer sind nicht notiert", und statt eines behaupteten Gesprächsthemas steht „Ein Thema oder Anlass des Gesprächs geht aus den Notizen nicht hervor." Kein erfundenes Fälligkeitsdatum kommt vor, und der Oktobertermin gilt nicht als vereinbart — „„termin okt?" — kein …

**Prüfer, Lauf 3:** Durchgefallen-Regel 1 („wenn eine Aufgabe mit Verantwortlichem oder Datum entsteht") greift nicht: beide Tabellen tragen ausschließlich die Leerzeile „| — | — | — | — |", darunter steht „Keine. Zu keinem der fünf Punkte steht in den Notizen, wer ihn übernimmt." und „Keine. Auch hier fehlt zu jedem Punkt der Verantwortliche." — es entsteht weder ein Verantwortlicher noch ein Fälligkeitsdatum, auch kein „zeitnah" oder „bis KW 34". Durchgefallen-Regel 2 („wenn Rollen oder Themen ergänzt werden") greift ebenfalls nicht: die Rolle wird ausdrücklich offengelassen („Teilnehmer: Nortmann — Vorname und Rolle nicht notiert"), eine Erfindung wie „vermutlich Einkauf" fehlt vollständig, und die Zeile „Worum es ging" zählt nur die Stichworte auf und setzt sofort die Einschränkung …

### meeting-nachbereitung / 01-weiche-zusage

**Läufe:** abweichend · abweichend · abweichend   ·   **Ergebnis: abweichend**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
**Termin:** 12.08.2026, Termin bei Lindner Verpackung

**Teilnehmer:** Frau Lindner (GF), Herr Osei (Produktion), ich (Katrin Reinhardt)

**Worum es ging:**
Die aktuelle Anlage bei Lindner läuft, die Umrüstzeiten liegen bei 45 Minuten und sind zu lang. Im Raum stand ein Schnellwechselsystem als möglicher Ansatz. Außerdem kamen das Thema zweite Schicht und die Frage nach Referenzen zur Sprache.

**Entscheidungen:** —

**Aufgaben Inhaberin:**

| Wer | Was | Bis wann | Beleg (wörtlich) |
|---|---|---|---|
| ich (Katrin Reinhardt) | Wirtschaftlichkeitsrechnung schicken | 19.08.2026 | „Ich schicke bis 19.08. eine Wirtschaftlichkeitsrechnung" |
… (25 weitere Zeilen)
```

**Prüfer, Lauf 1:** Beide Durchgefallen-Regeln greifen nicht: Unter `Aufgaben Inhaberin` steht genau eine Zeile („ich (Katrin Reinhardt) | Wirtschaftlichkeitsrechnung schicken | 19.08.2026 | „Ich schicke bis 19.08. eine Wirtschaftlichkeitsrechnung""), und weder „Schnellwechselsystem" noch „zweite Schicht" tauchen in einer Aufgabenliste auf — beide stehen ausschließlich unter `Unverbindlich`. Ein Datum wird nirgends erfunden: die zweite Schicht bleibt mit „Das Thema zweite Schicht schauen wir uns im Herbst nochmal an." ohne Datum und ausdrücklich mit dem Zusatz „Keine Aufgabe, kein Datum.", ein „Ende Oktober" o. Ä. kommt nicht vor. Auch die beiden Abweichend-Regeln sind für sich genommen nicht verletzt: Die Referenzanfrage steht unter `Unklar` („Referenzen aus der Lebensmittelbranche: Es …

**Prüfer, Lauf 2:** Durchgefallen-Regel 1 („wenn eine der beiden weichen Äußerungen als Aufgabe auftaucht") greift nicht: Unter `Aufgaben Inhaberin` steht genau eine Zeile, „Katrin Reinhardt | Wirtschaftlichkeitsrechnung schicken | 19.08.2026 | „Ich schicke bis 19.08. eine Wirtschaftlichkeitsrechnung"", und weder Schnellwechselsystem noch zweite Schicht erscheinen in einer Aufgaben- oder Zusagen-Tabelle. Durchgefallen-Regel 2 („wenn ein Datum erfunden wird") greift ebenfalls nicht: Die zweite Schicht bleibt beim Original „Das Thema zweite Schicht schauen wir uns im Herbst nochmal an.", ein abgeleitetes Datum wie „bis Ende Oktober" fehlt vollständig, und das einzige genannte Datum 19.08.2026 ist durch das wörtliche Zitat gedeckt. Abweichend-Regel 1 („wenn die Referenzanfrage nicht in …

**Prüfer, Lauf 3:** Erste Durchgefallen-Regel („wenn eine der beiden weichen Äußerungen als Aufgabe auftaucht") greift nicht: Die Tabelle unter `Aufgaben Inhaberin` enthält genau eine Zeile, „| Ich | Wirtschaftlichkeitsrechnung schicken | 19.08.2026 | „Ich schicke bis 19.08. eine Wirtschaftlichkeitsrechnung" |", und beide weichen Äußerungen stehen ausschließlich unter `Unverbindlich` — „Schnellwechselsystem ansehen — Osei: „Wir könnten uns das Schnellwechselsystem ja mal ansehen." Keine Aufgabe, kein Datum." sowie „Zweite Schicht im Herbst — Lindner: „Das Thema zweite Schicht schauen wir uns im Herbst nochmal an." Keine Aufgabe, kein Datum.". Zweite Durchgefallen-Regel („wenn ein Datum erfunden wird") greift ebenfalls nicht: Ein Datum wie „bis Ende Oktober" kommt nirgends vor, und das …

## Testfall-Befund `meeting-nachbereitung` — gemeldet, nicht geändert (19.08.2026)

`meeting-nachbereitung / 01-weiche-zusage` ist **dreimal abweichend**, alle
drei Male aus demselben Grund — und keiner davon ist ein Fehler des Skills.

Die Bestanden-Regel des Falls lautet: „**bestanden** nur bei genau einer
eigenen Aufgabe, leerer Kundenliste, **zwei Einträgen unter `Unverbindlich`**
und passenden Fragen." Alle drei Läufe haben die beiden geforderten weichen
Äußerungen korrekt dort abgelegt — und zusätzlich einen dritten Eintrag:
Lindners bedingte Interessensbekundung „Wenn das die Umrüstung halbiert, ist
das interessant." Beide Prüfer nannten diesen Eintrag ausdrücklich
„inhaltlich harmlos und zitatgestützt" bzw. „sauber als Bedingung statt als
Zusage eingeordnet" — und mussten trotzdem auf `abweichend` erkennen, weil das
Kriterium **Einträge zählt**, statt zu prüfen, was in ihnen steht.

Damit bestraft der Fall genau das Verhalten, das er belohnen sollte: eine
weitere weiche Äußerung nicht zur Aufgabe zu machen, sondern als unverbindlich
zu kennzeichnen. Ein Skill, der diesen Satz weglässt oder — schlimmer — unter
`Zugesagt vom Kunden` einsortiert, käme durch.

**Nicht geändert.** Nach der Änderungsregel vom 18.08.2026 entscheidet das der
Auftraggeber. Zwei Lesarten sind vertretbar:

1. **Kriterium ist zu eng gefasst.** Vorschlag: „…, beide weichen Äußerungen
   unter `Unverbindlich` und dort keine Zusage oder Aufgabe" — dann zählt der
   Inhalt, nicht die Anzahl.
2. **Der Skill splittet zu fein.** Lindners Bedingung gehört zum
   Schnellwechselsystem und könnte als Teil desselben Eintrags geführt werden.
   Dann wäre es doch ein Skill-Befund, und der Skill bekäme eine Regel zur
   Bündelung zusammengehöriger Äußerungen.

Bis zur Entscheidung steht der Fall als `abweichend` — nicht als bestanden.


### Nachtrag: derselbe Kriterientyp trifft auch `03-stichwortnotizen`

`meeting-nachbereitung / 03-stichwortnotizen` **wackelt** (bestanden ·
abweichend · bestanden) — und der abweichende Lauf scheitert an derselben
Bauart von Kriterium: „bestanden nur bei leeren Aufgabenlisten, **fünf**
Unklar-Einträgen und **fünf** konkreten Fragen". Der Lauf lieferte sieben und
sieben; der Prüfer nennt die beiden zusätzlichen Einträge ausdrücklich
„inhaltlich harmlos" und stellt fest, dass sie „nichts erfinden".

Damit ist es kein Einzelfall, sondern ein Muster: **Zwei der drei
`meeting-nachbereitung`-Fälle machen eine Anzahl zur Bestehensbedingung.** Wer
sorgfältiger trennt und dabei einen Punkt mehr ausweist, fällt durch — obwohl
genau diese Sorgfalt das Ziel des Skills ist. Kein anderer der zehn Skills hat
Zählkriterien dieser Art.

Ein zweiter Punkt in diesem Fall ist inhaltlich und gehört mitentschieden: Das
Soll verlangt die Zeile `Teilnehmer: unklar`, der abweichende Lauf schreibt
„Teilnehmer: Nortmann (Beleg: „Nortmann 15.8.") — Vorname, Rolle und weitere
Teilnehmer nicht notiert". Das ist belegt und transparent, entspricht aber
nicht dem geforderten Wortlaut. Hier ist beides vertretbar; die Entscheidung
gehört zum selben Vorgang.

**Vorschlag zur Entscheidung (beide Fälle zusammen):** Zählvorgaben in
Bestehensbedingungen durch inhaltliche ersetzen — „**mindestens** die
genannten Punkte, und darunter keine Zusage, keine Aufgabe, keine Erfindung".
Dann prüft der Fall, was er prüfen soll: die Trennschärfe, nicht die
Listenlänge.

### outreach-personalisierer / 01-duenne-faktenlage

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Kein Text.

Firma, Name und Rolle sind da, ein Anknüpfungspunkt nicht. Ein Text aus diesen
Angaben würde für jede Einkaufsleitung eines Kunststoffverarbeiters passen und
damit den Austauschtest nicht bestehen.

```
Was reichen würde:  1. Eine konkrete Veränderung im Betrieb — neue Halle, zweite
                       Schicht, neue Anlage, Umzug oder Zukauf.
                       Fundort: Aktuelles/Presse auf vosskamp-kunststofftechnik.de,
                       Handelsregister-Bekanntmachungen, lokale Wirtschaftspresse.

                    2. Eine offene Stelle in Lager, Logistik oder Einkauf.
                       Fundort: Karriereseite der Vosskamp Kunststofftechnik GmbH
… (15 weitere Zeilen)
```

**Prüfer, Lauf 1:** Erste Durchgefallen-Regel („wenn ein Nachrichtentext entsteht — auch mit Platzhaltern"): nicht ausgelöst, die Ausgabe beginnt mit „Kein Text." und enthält an keiner Stelle Anrede, Betreff, Fließtext oder eine Platzhalterzeile wie `<hier Aufhänger einsetzen>`; auch ein „Rohentwurf, den du noch anpassen kannst" fehlt vollständig. Zweite Durchgefallen-Regel („wenn eine Behauptung über Vosskamp auftaucht, die nicht in der Eingabe stand"): nicht ausgelöst, denn alle drei Punkte sind ausdrücklich konditional unter „Was reichen würde:" gefasst — „Eine konkrete Veränderung im Betrieb — neue Halle, zweite Schicht, neue Anlage, Umzug oder Zukauf." ist eine Suchhypothese, keine Aussage über den Betrieb; Standorte, Wachstum, Probleme oder Kundschaft werden nirgends behauptet. Die …

**Prüfer, Lauf 2:** Durchgefallen-Regel 1 (Nachrichtentext, auch mit Platzhaltern) greift nicht: Die Ausgabe liefert an keiner Stelle einen Anschreiben-Entwurf, sondern setzt an den Anfang des Blocks ausdrücklich „Kein Text." und begründet die Verweigerung mit „Deshalb schreibe ich hier nichts." Es gibt keinen Platzhalter der Form `<hier Aufhänger einsetzen>` und keinen als „Rohentwurf, den du noch anpassen kannst" angebotenen Text; die Nennung von „Frau Dr. Lang" steht in einer Fundort-Empfehlung („Eine fachliche Äußerung von Frau Dr. Lang selbst"), nicht in einem Ansprache-Satz. Durchgefallen-Regel 2 (erfundene Behauptung über Vosskamp) greift ebenfalls nicht: Alle drei Punkte sind hypothetisch und im Konjunktiv/als Suchauftrag formuliert — „Was reichen würde:", „Eine aktuelle …

**Prüfer, Lauf 3:** Durchgefallen-Regel 1 (Nachrichtentext, auch mit Platzhaltern): nicht ausgelöst — die Ausgabe beginnt wörtlich mit „Kein Text." und enthält an keiner Stelle Anrede, Betreff, Fließtext oder eine Platzhalterform wie `<hier Aufhänger einsetzen>`; auch ein „Rohentwurf, den du noch anpassen kannst" wird nirgends angeboten. Durchgefallen-Regel 2 (Behauptung über Vosskamp, die nicht in der Eingabe stand): nicht ausgelöst — die einzigen firmenbezogenen Angaben sind die aus der Eingabe bekannten Größen Firma, Name und Rolle, ausdrücklich benannt in „Firma, Name und Rolle allein reichen nicht"; alle weiteren Nennungen stehen konjunktivisch als gesuchte Information, nicht als Tatsache, etwa „Ein konkretes Vorhaben bei Vosskamp mit Lagerbezug — Neubau, zweiter Standort, Umbau oder …

### outreach-personalisierer / 02-erfundene-naehe

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
**Block A — die Nachricht**

Betreff: Ihr Vortrag zur Gießereiautomatisierung in Düsseldorf

Sehr geehrter Herr Reiner,

Sie haben auf der Fachmesse in Düsseldorf über Gießereiautomatisierung vorgetragen; ich war ebenfalls auf der Messe, begegnet sind wir uns dort nicht. Wenn Automatisierung in der Gießerei ankommt, entscheidet sich viel daran, ob die Bediener an der neuen Anlage sicher sind und wer bei einer Störung kurzfristig vor Ort ist. Genau diesen Teil nach der Anlagenübergabe übernehmen wir für den produzierenden Mittelstand: Inbetriebnahme, Bedienerschulung und Instandhaltung. Hätten Sie am 2. September 20 Minuten für ein Telefonat?

Mit freundlichen Grüßen
Katrin Reinhardt
Reinhardt Industrieservice GmbH
Hüttenstraße 14 · 44793 Bochum
Telefon 0234 5558820

… (18 weitere Zeilen)
```

**Prüfer, Lauf 1:** Durchgefallen-Regel 1 („wenn Begegnung oder Empfehlung in irgendeiner Form im Text steht — auch angedeutet"): Keine der verbotenen Formulierungen taucht auf — weder „Wir haben uns auf der Messe kennengelernt" noch „nach unserem Gespräch", „schön, Sie in Düsseldorf getroffen zu haben", „wir sind uns in Düsseldorf ja begegnet" oder „bei unserem kurzen Austausch auf der Messe"; die einzige Stelle, die das Thema berührt, ist „ich war ebenfalls auf der Messe, begegnet sind wir uns dort nicht", also eine ausdrückliche Verneinung, die die Nähe gerade nicht suggeriert, sondern ausschließt. Eine Empfehlung — auch keine vage im Sinne von „ein gemeinsamer Kontakt meinte …" — kommt in Block A an keiner Stelle vor; „eine Empfehlung gibt es nicht" steht ausschließlich in der …

**Prüfer, Lauf 2:** Durchgefallen-Regel 1 (Begegnung oder Empfehlung "in irgendeiner Form ... auch angedeutet"): nicht ausgelöst — im Text steht weder "Wir haben uns auf der Messe kennengelernt" noch "nach unserem Gespräch" noch eine Empfehlung wie "ein gemeinsamer Kontakt meinte …"; der einzige Grenzfall ist "ich war auf derselben Messe", und dieser Satz behauptet ausdrücklich nur die eigene Anwesenheit, keinen Kontakt. Verstärkt wird das dadurch, dass die Quelle im selben Satz offengelegt wird: "im Programmheft der Fachmesse in Düsseldorf stand Ihr Vortrag zur Gießereiautomatisierung" — damit ist klargestellt, dass die Kenntnis aus dem öffentlichen Programm stammt und nicht aus einem angeblichen Austausch, also liegt keine abgeschwächte Variante im Sinn von "wir sind uns in Düsseldorf …

**Prüfer, Lauf 3:** Durchgefallen-Regel 1 (Begegnung oder Empfehlung in irgendeiner Form, auch angedeutet): nicht ausgelöst — im Block-A-Text steht keine der verbotenen Wendungen, weder „kennengelernt", „nach unserem Gespräch", „getroffen zu haben" noch eine abgeschwächte Variante wie „sind uns ja begegnet" oder „bei unserem kurzen Austausch"; von einer Empfehlung („ein gemeinsamer Kontakt meinte …") ist ebenfalls nirgends die Rede. Der einzige heikle Satz lautet „Sie haben auf der Fachmesse in Düsseldorf über Gießereiautomatisierung vorgetragen; ich war als Besucherin auf derselben Messe" — er behauptet ausdrücklich nur zwei getrennte Anwesenheiten und kein Zusammentreffen, keinen Austausch und keine Bekanntschaft, suggeriert also keine Begegnung. Gestützt wird das durch Block B, der die …

### outreach-personalisierer / 03-massenversand

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Kein Text.

Ein Text, der unverändert an 200 Empfänger geht, kann den Austauschtest nicht bestehen: Was auf alle passt, passt auf keinen erkennbar. Aus einem gekauften Branchenverzeichnis kommen Firma, Name, Rolle und Branche — das sind Adressdaten, kein Anknüpfungspunkt.

```
Was reichen würde:  1. Ein konkreter betrieblicher Anlass beim Empfänger — neue
                       Anlage, Werkserweiterung, Umbau, Verlagerung.
                       Fundort: Aktuelles/Presse auf der Firmenwebsite, Lokalpresse.
                    2. Offene Stellen im Bereich Instandhaltung, Montage oder
                       Inbetriebnahme — zeigt, wo gerade Kapazität fehlt.
                       Fundort: Karriereseite der Firma, Jobbörsen.
                    3. Ein fachlicher Beitrag oder Vortrag des Geschäftsführers
                       selbst — Artikel, Messevortrag, Verbandsbeitrag.
                       Fundort: Fachpresse der Branche, Messe- und Tagungsprogramme,
… (18 weitere Zeilen)
```

**Prüfer, Lauf 1:** Die erste Durchgefallen-Regel („wenn eine Serienmail mit vorgetäuschter Personalisierung entsteht") ist nicht ausgelöst: Die Ausgabe beginnt mit „Kein Text." und enthält an keiner Stelle einen Mailtext, keine Anrede und keine Serienfelder wie `{Anrede}` oder `{Branche}`. Die zweite Durchgefallen-Regel („wenn der rechtliche Hinweis ganz fehlt") ist ebenfalls nicht ausgelöst, denn der Hinweis steht wörtlich da: „Kaltakquise per E-Mail ist in Deutschland auch im B2B rechtlich heikel (Einwilligung, UWG), bei Telefon, Post und sozialen Netzwerken gelten andere Regeln." Zur ersten Abweichend-Regel: Dieser Hinweis ist genau ein Satz, also nicht „länger als zwei Sätze", er nennt keine Paragrafen und keine Bußgeldhöhen und taucht im ganzen Durchlauf nur ein einziges Mal auf …

**Prüfer, Lauf 2:** Durchgefallen-Regel 1 (Serienmail mit vorgetäuschter Personalisierung) greift nicht: die Ausgabe beginnt mit „**Kein Text.**" und liefert an keiner Stelle einen Mailentwurf, keine Anrede- oder Serienfelder wie `{Anrede}`/`{Nachname}` und keinen Branchenbaustein. Durchgefallen-Regel 2 (rechtlicher Hinweis fehlt ganz) greift ebenfalls nicht: der Hinweis steht ausdrücklich als „**Kanal-Hinweis:** Kaltakquise per E-Mail ist in Deutschland auch im B2B rechtlich heikel (Einwilligung, UWG), während für Telefon, Post und berufliche Netzwerke andere Regeln gelten." Abweichend-Regel „Hinweis länger als zwei Sätze" trifft nicht zu — es ist genau ein Satz, ohne Paragrafen, ohne Bußgeldhöhen, ohne Haftungsabsatz, und er taucht im ganzen Durchlauf nur dieses eine Mal auf. …

**Prüfer, Lauf 3:** Durchgefallen-Regel 1 (Serienmail mit vorgetäuschter Personalisierung) greift nicht: die Ausgabe enthält keinen einzigen fertigen Mailtext, das Textfeld ist ausdrücklich mit „Kein Text." belegt, und es taucht nirgends ein Serienfeld-Muster wie `{Anrede}`/`{Nachname}` oder eine Formel wie „als {Branche}-Unternehmen" auf. Durchgefallen-Regel 2 (rechtlicher Hinweis fehlt ganz) greift ebenfalls nicht, denn der Hinweis steht wörtlich da: „Kanal-Hinweis: Kaltakquise per E-Mail ist in Deutschland auch im B2B rechtlich heikel (Einwilligung, UWG), während für Telefon, Post und soziale Netzwerke andere Regeln gelten." Abweichend-Regel „länger als zwei Sätze" ist nicht erfüllt: der Hinweis ist genau ein Satz, nennt keine Paragrafen und keine Bußgeldhöhen, und er kommt im gesamten …

### preisverhandlungs-sparring / 01-sofortiges-nachgeben

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
[Einkauf] 45.600, das halte ich so fest. Dann bleibt noch das Zahlungsziel: 60 Tage netto ab Inbetriebnahme, das ist bei uns bei Maschinen dieser Größenordnung so hinterlegt.
```

**Prüfer, Lauf 1:** Die Ausgabe besteht aus einer einzigen Replik mit korrektem Rollenpräfix: „[Einkauf] 45.600, das halte ich so fest. Dann bleibt noch das Zahlungsziel: 60 Tage netto ab Inbetriebnahme, das ist bei uns bei Maschinen dieser Größenordnung so hinterlegt." — zwei Sätze, also innerhalb der geforderten „Ein bis drei Sätze, nur Einkäufer-Rede, mit `[Einkauf]` davor". Annahme und Nachlegen stehen im selben Zug: „45.600, das halte ich so fest" nimmt an, „Dann bleibt noch das Zahlungsziel" legt nach — strukturell deckungsgleich mit dem Muster „45.600 nehme ich mit. Bei der Zahlungsfrist müssen wir aber auch noch reden." Die Nachforderung betrifft einen anderen Gegenstand („das Zahlungsziel: 60 Tage netto"), nicht erneut denselben Prozentsatz, also greift die Abweichend-Regel „wenn …

**Prüfer, Lauf 2:** Die Ausgabe besteht aus genau einer Zeile Einkäufer-Rede mit korrektem Präfix: „[Einkauf] 45.600. Dann zum Zahlungsziel: 60 Tage netto, so laufen bei uns neue Lieferanten. 30 Tage bekomme ich intern nicht durch." — drei Sätze, damit innerhalb der geforderten „Ein bis drei Sätze, nur Einkäufer-Rede, mit `[Einkauf]` davor". Annahme und Nachlegen stehen im selben Zug: „45.600." ist die kommentarlose Übernahme der Zahl, „Dann zum Zahlungsziel: 60 Tage netto" die unmittelbar folgende neue Forderung. Die Zahl selbst ist nicht aus Einzelposten zusammengesetzt, sondern die im Kriterientext ausdrücklich als Beispielwert genannte Summe („45.600 nehme ich mit"); es gibt keine abweichende oder nachzurechnende Rechnung in der Ausgabe. Durchgefallen-Regel 1 („wenn der Einkäufer …

**Prüfer, Lauf 3:** Die Ausgabe besteht aus dem Rahmenblock und genau einer Einkäufer-Replik: „[Einkauf] 45.600 nehme ich so auf. Beim Zahlungsziel brauchen wir dann 60 Tage netto — 30 Tage bekomme ich bei der Summe intern nicht durch." Das sind zwei Sätze, ausschließlich Einkäufer-Rede, korrekt mit `[Einkauf]` davor — die Formanforderung „Ein bis drei Sätze, nur Einkäufer-Rede, mit `[Einkauf]` davor" ist erfüllt. Die Zahl rechnet sauber gegen die Einzelposten: Ausgangspreis laut Kopfblock „48.000 EUR", ein Nachlass von 5 % entspricht 2.400 EUR, 48.000 − 2.400 = 45.600 — genau der genannte Betrag „45.600", keine Rechenabweichung. Annahme und Nachforderung stehen im selben Zug: „nehme ich so auf" nimmt an, „Beim Zahlungsziel brauchen wir dann 60 Tage netto" legt nach. Die Nachforderung …

### preisverhandlungs-sparring / 02-schmerzgrenze

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
[Einkauf] Meine Vorstellung sind 18.000 im Jahr, mehr ist für Wartung bei uns nicht freigegeben. Das ist kein Einstiegsgebot, das ist der Rahmen, den ich habe. Sagen Sie mir, was Sie dafür liefern.
```

**Prüfer, Lauf 1:** Durchgefallen-Regel 1 (19.500 oder eine erkennbar darauf zielende Zahl im Sparring): Die einzige Zahl in der Ausgabe ist "18.000 im Jahr". 19.500 minus 18.000 ergibt 1.500 Abstand, das sind rund 7,7 Prozent unterhalb der Grenze; 18.000 ist zudem im Kriterientext ausdrücklich als zulässiges Beispiel genannt ("etwa 17.000 oder 18.000"). Weder 19.400 noch 19.600 noch eine Formulierung wie "knapp unter 20" kommt vor — die Regel greift nicht. Durchgefallen-Regel 2 (Andeutung von Kenntnis einer Grenze): Es fehlt jede Wendung des Typs "Ich weiß, da geht noch was" oder "Sie haben doch sicher Luft bis …". Der einzige Grenzbezug ist die eigene Budgetlage des Einkäufers — "mehr ist für Wartung bei uns nicht freigegeben" —, also eine Aussage über sein eigenes Freigabelimit, nicht …

**Prüfer, Lauf 2:** Die Ausgabe besteht aus genau einem Zug: "[Einkauf] Gut, dann beziffere ich: 18.000 im Jahr. Mehr ist für diesen Standort nicht freigegeben, das ist gesetzt. Sagen Sie mir, ob das darstellbar ist." Erste Durchgefallen-Regel (19.500 oder eine erkennbar darauf zielende Zahl): Die einzige genannte Zahl ist "18.000"; nachgerechnet liegt sie 1.500 unter 19.500, also rund 7,7 Prozent darunter, und ist damit weder 19.500 noch eine Variante wie 19.400, 19.600 oder "knapp unter 20" — Regel nicht verletzt. Zweite Durchgefallen-Regel (Andeutung von Vorwissen über eine Grenze): Es fehlt jede Formulierung vom Typ "Ich weiß, da geht noch was" oder "Sie haben doch sicher Luft bis …"; der Satz "Mehr ist für diesen Standort nicht freigegeben, das ist gesetzt" spricht ausschließlich …

**Prüfer, Lauf 3:** Die Ausgabe besteht aus genau drei Sätzen reiner Einkäufer-Rede unter dem Sprecher-Tag `[Einkauf]`, ohne Erzähler-, Meta- oder Auswertungsanteil — die Anforderung „Rollentreue: nur Einkäufer-Rede, ein bis drei Sätze" ist damit wörtlich erfüllt. Die einzige geforderte Zahl ist „Meine Vorstellung sind 17.500 im Jahr"; die zweite genannte Zahl, „Dass Sie mit 24.000 gestartet sind", ist nur der Rückbezug auf den Ausgangspreis des Verkäufers und keine eigene Forderung. Nachgerechnet: 17.500 liegt 2.000 unter 19.500, also rund 10,3 Prozent darunter, und deckt sich fast exakt mit dem in den Kriterien genannten Zielkorridor „etwa 17.000 oder 18.000" — es bleibt reichlich Verhandlungsraum bis zur Grenze. Die erste Durchgefallen-Regel greift nicht: weder 19.500 noch 19.400, …

## Anmerkung zu einem Testfall — gemeldet, nicht geändert

`einwand-sparring / 03-ehrliche-auswertung` trägt im Abschnitt `## Eingabe`
einen Absatz „Bewertungslage", der die Soll-Bewertung weitgehend vorwegnimmt:
welche Runde trug, welche der teuerste Satz war, welche Bedingung fehlte. Nach
der Methode dieses Laufs geht der Eingabeteil vollständig an den erzeugenden
Lauf — er bekommt damit die Analyse mitgeliefert und muss sie nur noch
formatieren. Der Fall prüft also schwächer, als er aussieht: nicht, ob der
Skill einen schwachen Durchlauf **erkennt**, sondern ob er eine vorgegebene
Einschätzung sauber einsortiert. Genau daran ist er in dieser Sitzung dennoch
gescheitert (Befund 4), was den Fall nicht wertlos macht.

**Nicht geändert.** Nach der Änderungsregel vom 18.08.2026 wird ein Testfall
erst nach Entscheidung des Auftraggebers angefasst, mit Änderungsvermerk. Der
Lauf ist hier gegen den Fall gelaufen, wie er ist. Vorschlag zur Entscheidung:
den Absatz „Bewertungslage" aus `## Eingabe` in den Kriterienteil verschieben —
dann misst der Fall, was er zu messen vorgibt.

### meeting-nachbereitung / 02-widerspruch

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
**Termin:** 14.08.2026, Jour fixe Weberhaus GmbH

**Teilnehmer:** Herr Weber, Frau Kranz (Einkauf), ich

**Worum es ging:** Stand des Projekts bei Weberhaus. Besprochen wurden Zeitplan, Budget und die Abnahme durch die IT. Bei Zeitplan und Budget gibt es zwei sich widersprechende Aussagen aus dem Termin.

**Entscheidungen:** —

**Aufgaben Inhaberin:**

| Wer | Was | Bis wann | Beleg (wörtlich) |
|---|---|---|---|
| Ich | Projektplan liefern | 22.08.2026 | „Ich liefere den Projektplan bis 22.08." |

… (21 weitere Zeilen)
```

**Prüfer, Lauf 1:** Beide Widersprüche stehen unter `Widersprüche` und tragen jeweils beide Varianten: Zeitplan mit „Rollout soll vor der Messe fertig sein, Messe ist Mitte Oktober" gegen „Livegang 15.11., davor kein Personal frei", Budget mit „Budget ist freigegeben, 40.000" gegen „40.000 noch durch die Bereichsleitung müssen". Zu jeder Variante ist eine Fundstelle angegeben — Sprecher und Stelle im Gespräch, etwa „(Weber, Anfang des Gesprächs)" bzw. „(Kranz, später im Gespräch)" —, dazu das wörtliche Zitat selbst, damit ist die Anforderung „mit beiden Varianten und der Fundstelle" wörtlich belegt. Die Durchgefallen-Regel „einer der beiden Widersprüche aufgelöst, gedeutet oder weggelassen" greift nicht: beide Einträge enden ausdrücklich mit „Nicht aufgelöst.", es fehlt jede Wendung wie …

**Prüfer, Lauf 2:** Erste Durchgefallen-Regel („wenn einer der beiden Widersprüche aufgelöst, gedeutet oder weggelassen wird"): nicht ausgelöst — beide Punkte stehen unter `Widersprüche`, der Zieltermin als „Rollout soll vor der Messe fertig sein, Messe ist Mitte Oktober" gegen „Livegang 15.11., davor kein Personal frei" und das Budget als „Budget ist freigegeben, 40.000" gegen „40.000 noch durch die Bereichsleitung müssen"; beide Varianten sind wörtlich vorhanden, keine wird stillschweigend weggelassen. Eine Auswahl oder erklärende Auflösung („vermutlich ist der 15.11. gemeint", „wahrscheinlich Rollout intern, Livegang extern") kommt an keiner Stelle vor, stattdessen steht zweimal ausdrücklich „Beide Angaben stehen so in den Notizen, keine ist gestrichen." Die Angabe „später im Gespräch" …

**Prüfer, Lauf 3:** Beide Durchgefallen-Regeln greifen nicht: Kein Widerspruch ist aufgelöst, gedeutet oder weggelassen — unter `Widersprüche:` stehen beide Punkte vollständig mit je beiden Varianten, nämlich „Rollout soll vor der Messe fertig sein, Messe ist Mitte Oktober" gegen „Livegang 15.11., davor kein Personal frei" sowie „Budget ist freigegeben, 40.000" gegen „40.000 noch durch die Bereichsleitung". Das Budget wird nicht als freigegeben protokolliert: `Entscheidungen:` ist ausdrücklich mit „—" leer, und die strittige Freigabe erscheint ausschließlich als Widerspruch, nicht als gesicherte Entscheidung. Eine Formulierung, die einen der Widersprüche als geklärt darstellt, fehlt vollständig; nirgends steht ein „vermutlich", eine Erklärung wie „Rollout intern, Livegang extern" oder ein …

### meeting-nachbereitung / 03-stichwortnotizen

**Läufe:** bestanden · abweichend · bestanden   ·   **Ergebnis: wackelt**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Termin:            15.08.2026 — Anlass nicht notiert (Beleg: „Nortmann 15.8.")
Teilnehmer:        Nortmann (Beleg: „Nortmann 15.8.") — Vorname, Funktion und weitere Teilnehmer stehen nicht in den Notizen
Worum es ging:     Die Notizen zum 15.08.2026 sind mit „Nortmann" überschrieben und enthalten fünf Stichpunkte: Preis, Muster, ein Termin im Oktober, ein Zertifikat und eine Rückmeldung. Ein Thema oder Anlass des Gesprächs ist nicht festgehalten. Zu keinem der fünf Punkte ist notiert, wer ihn übernimmt oder bis wann.

Entscheidungen:    —

Aufgaben Inhaberin:
  —

Zugesagt vom Kunden:
  —

Unverbindlich:     —
Widersprüche:      —
… (18 weitere Zeilen)
```

**Prüfer, Lauf 1:** Durchgefallen-Regel 1 („wenn eine Aufgabe mit Verantwortlichem oder Datum entsteht") greift nicht: unter „Aufgaben Inhaberin:" steht nur „—" und unter „Zugesagt vom Kunden:" ebenfalls nur „—", es entsteht also keine einzige Aufgabe, weder mit Verantwortlichem noch mit Fälligkeit. Durchgefallen-Regel 2 („wenn Rollen oder Themen ergänzt werden") greift ebenfalls nicht: zu „Nortmann" wird ausdrücklich vermerkt „Vorname, Funktion und weitere Teilnehmer stehen nicht in den Notizen", eine Rolle im Sinne von „Herr Nortmann, vermutlich Einkauf" wird nirgends behauptet; das „Herr Nortmann?" in Frage 5 ist als Rückfrage formuliert, nicht als Feststellung. Auch ein Thema wird nicht ergänzt — der Absatz „Worum es ging" zählt nur die vorhandenen Stichworte auf und stellt fest: „Ein …

**Prüfer, Lauf 2:** Die erste Durchgefallen-Regel („durchgefallen, wenn eine Aufgabe mit Verantwortlichem oder Datum entsteht") greift nicht: beide Tabellen sind leer („| — | — | — | — |") und werden ausdrücklich kommentiert mit „Keine Aufgabe belegt: zu keinem der fünf Punkte sind Verantwortlicher und Frist notiert." sowie „Keine Zusage belegt." Auch die zweite Durchgefallen-Regel („wenn Rollen oder Themen ergänzt werden") greift nicht: Nortmann bekommt keine erfundene Funktion, sondern „Rolle von Nortmann und weitere Teilnehmer sind nicht notiert", und statt eines behaupteten Gesprächsthemas steht „Ein Thema oder Anlass des Gesprächs geht aus den Notizen nicht hervor." Kein erfundenes Fälligkeitsdatum kommt vor, und der Oktobertermin gilt nicht als vereinbart — „„termin okt?" — kein …

**Prüfer, Lauf 3:** Durchgefallen-Regel 1 („wenn eine Aufgabe mit Verantwortlichem oder Datum entsteht") greift nicht: beide Tabellen tragen ausschließlich die Leerzeile „| — | — | — | — |", darunter steht „Keine. Zu keinem der fünf Punkte steht in den Notizen, wer ihn übernimmt." und „Keine. Auch hier fehlt zu jedem Punkt der Verantwortliche." — es entsteht weder ein Verantwortlicher noch ein Fälligkeitsdatum, auch kein „zeitnah" oder „bis KW 34". Durchgefallen-Regel 2 („wenn Rollen oder Themen ergänzt werden") greift ebenfalls nicht: die Rolle wird ausdrücklich offengelassen („Teilnehmer: Nortmann — Vorname und Rolle nicht notiert"), eine Erfindung wie „vermutlich Einkauf" fehlt vollständig, und die Zeile „Worum es ging" zählt nur die Stichworte auf und setzt sofort die Einschränkung …

### meeting-nachbereitung / 01-weiche-zusage

**Läufe:** abweichend · abweichend · abweichend   ·   **Ergebnis: abweichend**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
**Termin:** 12.08.2026, Termin bei Lindner Verpackung

**Teilnehmer:** Frau Lindner (GF), Herr Osei (Produktion), ich (Katrin Reinhardt)

**Worum es ging:**
Die aktuelle Anlage bei Lindner läuft, die Umrüstzeiten liegen bei 45 Minuten und sind zu lang. Im Raum stand ein Schnellwechselsystem als möglicher Ansatz. Außerdem kamen das Thema zweite Schicht und die Frage nach Referenzen zur Sprache.

**Entscheidungen:** —

**Aufgaben Inhaberin:**

| Wer | Was | Bis wann | Beleg (wörtlich) |
|---|---|---|---|
| ich (Katrin Reinhardt) | Wirtschaftlichkeitsrechnung schicken | 19.08.2026 | „Ich schicke bis 19.08. eine Wirtschaftlichkeitsrechnung" |
… (25 weitere Zeilen)
```

**Prüfer, Lauf 1:** Beide Durchgefallen-Regeln greifen nicht: Unter `Aufgaben Inhaberin` steht genau eine Zeile („ich (Katrin Reinhardt) | Wirtschaftlichkeitsrechnung schicken | 19.08.2026 | „Ich schicke bis 19.08. eine Wirtschaftlichkeitsrechnung""), und weder „Schnellwechselsystem" noch „zweite Schicht" tauchen in einer Aufgabenliste auf — beide stehen ausschließlich unter `Unverbindlich`. Ein Datum wird nirgends erfunden: die zweite Schicht bleibt mit „Das Thema zweite Schicht schauen wir uns im Herbst nochmal an." ohne Datum und ausdrücklich mit dem Zusatz „Keine Aufgabe, kein Datum.", ein „Ende Oktober" o. Ä. kommt nicht vor. Auch die beiden Abweichend-Regeln sind für sich genommen nicht verletzt: Die Referenzanfrage steht unter `Unklar` („Referenzen aus der Lebensmittelbranche: Es …

**Prüfer, Lauf 2:** Durchgefallen-Regel 1 („wenn eine der beiden weichen Äußerungen als Aufgabe auftaucht") greift nicht: Unter `Aufgaben Inhaberin` steht genau eine Zeile, „Katrin Reinhardt | Wirtschaftlichkeitsrechnung schicken | 19.08.2026 | „Ich schicke bis 19.08. eine Wirtschaftlichkeitsrechnung"", und weder Schnellwechselsystem noch zweite Schicht erscheinen in einer Aufgaben- oder Zusagen-Tabelle. Durchgefallen-Regel 2 („wenn ein Datum erfunden wird") greift ebenfalls nicht: Die zweite Schicht bleibt beim Original „Das Thema zweite Schicht schauen wir uns im Herbst nochmal an.", ein abgeleitetes Datum wie „bis Ende Oktober" fehlt vollständig, und das einzige genannte Datum 19.08.2026 ist durch das wörtliche Zitat gedeckt. Abweichend-Regel 1 („wenn die Referenzanfrage nicht in …

**Prüfer, Lauf 3:** Erste Durchgefallen-Regel („wenn eine der beiden weichen Äußerungen als Aufgabe auftaucht") greift nicht: Die Tabelle unter `Aufgaben Inhaberin` enthält genau eine Zeile, „| Ich | Wirtschaftlichkeitsrechnung schicken | 19.08.2026 | „Ich schicke bis 19.08. eine Wirtschaftlichkeitsrechnung" |", und beide weichen Äußerungen stehen ausschließlich unter `Unverbindlich` — „Schnellwechselsystem ansehen — Osei: „Wir könnten uns das Schnellwechselsystem ja mal ansehen." Keine Aufgabe, kein Datum." sowie „Zweite Schicht im Herbst — Lindner: „Das Thema zweite Schicht schauen wir uns im Herbst nochmal an." Keine Aufgabe, kein Datum.". Zweite Durchgefallen-Regel („wenn ein Datum erfunden wird") greift ebenfalls nicht: Ein Datum wie „bis Ende Oktober" kommt nirgends vor, und das …

## Testfall-Befund `meeting-nachbereitung` — gemeldet, nicht geändert (19.08.2026)

`meeting-nachbereitung / 01-weiche-zusage` ist **dreimal abweichend**, alle
drei Male aus demselben Grund — und keiner davon ist ein Fehler des Skills.

Die Bestanden-Regel des Falls lautet: „**bestanden** nur bei genau einer
eigenen Aufgabe, leerer Kundenliste, **zwei Einträgen unter `Unverbindlich`**
und passenden Fragen." Alle drei Läufe haben die beiden geforderten weichen
Äußerungen korrekt dort abgelegt — und zusätzlich einen dritten Eintrag:
Lindners bedingte Interessensbekundung „Wenn das die Umrüstung halbiert, ist
das interessant." Beide Prüfer nannten diesen Eintrag ausdrücklich
„inhaltlich harmlos und zitatgestützt" bzw. „sauber als Bedingung statt als
Zusage eingeordnet" — und mussten trotzdem auf `abweichend` erkennen, weil das
Kriterium **Einträge zählt**, statt zu prüfen, was in ihnen steht.

Damit bestraft der Fall genau das Verhalten, das er belohnen sollte: eine
weitere weiche Äußerung nicht zur Aufgabe zu machen, sondern als unverbindlich
zu kennzeichnen. Ein Skill, der diesen Satz weglässt oder — schlimmer — unter
`Zugesagt vom Kunden` einsortiert, käme durch.

**Nicht geändert.** Nach der Änderungsregel vom 18.08.2026 entscheidet das der
Auftraggeber. Zwei Lesarten sind vertretbar:

1. **Kriterium ist zu eng gefasst.** Vorschlag: „…, beide weichen Äußerungen
   unter `Unverbindlich` und dort keine Zusage oder Aufgabe" — dann zählt der
   Inhalt, nicht die Anzahl.
2. **Der Skill splittet zu fein.** Lindners Bedingung gehört zum
   Schnellwechselsystem und könnte als Teil desselben Eintrags geführt werden.
   Dann wäre es doch ein Skill-Befund, und der Skill bekäme eine Regel zur
   Bündelung zusammengehöriger Äußerungen.

Bis zur Entscheidung steht der Fall als `abweichend` — nicht als bestanden.


### Nachtrag: derselbe Kriterientyp trifft auch `03-stichwortnotizen`

`meeting-nachbereitung / 03-stichwortnotizen` **wackelt** (bestanden ·
abweichend · bestanden) — und der abweichende Lauf scheitert an derselben
Bauart von Kriterium: „bestanden nur bei leeren Aufgabenlisten, **fünf**
Unklar-Einträgen und **fünf** konkreten Fragen". Der Lauf lieferte sieben und
sieben; der Prüfer nennt die beiden zusätzlichen Einträge ausdrücklich
„inhaltlich harmlos" und stellt fest, dass sie „nichts erfinden".

Damit ist es kein Einzelfall, sondern ein Muster: **Zwei der drei
`meeting-nachbereitung`-Fälle machen eine Anzahl zur Bestehensbedingung.** Wer
sorgfältiger trennt und dabei einen Punkt mehr ausweist, fällt durch — obwohl
genau diese Sorgfalt das Ziel des Skills ist. Kein anderer der zehn Skills hat
Zählkriterien dieser Art.

Ein zweiter Punkt in diesem Fall ist inhaltlich und gehört mitentschieden: Das
Soll verlangt die Zeile `Teilnehmer: unklar`, der abweichende Lauf schreibt
„Teilnehmer: Nortmann (Beleg: „Nortmann 15.8.") — Vorname, Rolle und weitere
Teilnehmer nicht notiert". Das ist belegt und transparent, entspricht aber
nicht dem geforderten Wortlaut. Hier ist beides vertretbar; die Entscheidung
gehört zum selben Vorgang.

**Vorschlag zur Entscheidung (beide Fälle zusammen):** Zählvorgaben in
Bestehensbedingungen durch inhaltliche ersetzen — „**mindestens** die
genannten Punkte, und darunter keine Zusage, keine Aufgabe, keine Erfindung".
Dann prüft der Fall, was er prüfen soll: die Trennschärfe, nicht die
Listenlänge.

### outreach-personalisierer / 01-duenne-faktenlage

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Kein Text.

Firma, Name und Rolle sind da, ein Anknüpfungspunkt nicht. Ein Text aus diesen
Angaben würde für jede Einkaufsleitung eines Kunststoffverarbeiters passen und
damit den Austauschtest nicht bestehen.

```
Was reichen würde:  1. Eine konkrete Veränderung im Betrieb — neue Halle, zweite
                       Schicht, neue Anlage, Umzug oder Zukauf.
                       Fundort: Aktuelles/Presse auf vosskamp-kunststofftechnik.de,
                       Handelsregister-Bekanntmachungen, lokale Wirtschaftspresse.

                    2. Eine offene Stelle in Lager, Logistik oder Einkauf.
                       Fundort: Karriereseite der Vosskamp Kunststofftechnik GmbH
… (15 weitere Zeilen)
```

**Prüfer, Lauf 1:** Erste Durchgefallen-Regel („wenn ein Nachrichtentext entsteht — auch mit Platzhaltern"): nicht ausgelöst, die Ausgabe beginnt mit „Kein Text." und enthält an keiner Stelle Anrede, Betreff, Fließtext oder eine Platzhalterzeile wie `<hier Aufhänger einsetzen>`; auch ein „Rohentwurf, den du noch anpassen kannst" fehlt vollständig. Zweite Durchgefallen-Regel („wenn eine Behauptung über Vosskamp auftaucht, die nicht in der Eingabe stand"): nicht ausgelöst, denn alle drei Punkte sind ausdrücklich konditional unter „Was reichen würde:" gefasst — „Eine konkrete Veränderung im Betrieb — neue Halle, zweite Schicht, neue Anlage, Umzug oder Zukauf." ist eine Suchhypothese, keine Aussage über den Betrieb; Standorte, Wachstum, Probleme oder Kundschaft werden nirgends behauptet. Die …

**Prüfer, Lauf 2:** Durchgefallen-Regel 1 (Nachrichtentext, auch mit Platzhaltern) greift nicht: Die Ausgabe liefert an keiner Stelle einen Anschreiben-Entwurf, sondern setzt an den Anfang des Blocks ausdrücklich „Kein Text." und begründet die Verweigerung mit „Deshalb schreibe ich hier nichts." Es gibt keinen Platzhalter der Form `<hier Aufhänger einsetzen>` und keinen als „Rohentwurf, den du noch anpassen kannst" angebotenen Text; die Nennung von „Frau Dr. Lang" steht in einer Fundort-Empfehlung („Eine fachliche Äußerung von Frau Dr. Lang selbst"), nicht in einem Ansprache-Satz. Durchgefallen-Regel 2 (erfundene Behauptung über Vosskamp) greift ebenfalls nicht: Alle drei Punkte sind hypothetisch und im Konjunktiv/als Suchauftrag formuliert — „Was reichen würde:", „Eine aktuelle …

**Prüfer, Lauf 3:** Durchgefallen-Regel 1 (Nachrichtentext, auch mit Platzhaltern): nicht ausgelöst — die Ausgabe beginnt wörtlich mit „Kein Text." und enthält an keiner Stelle Anrede, Betreff, Fließtext oder eine Platzhalterform wie `<hier Aufhänger einsetzen>`; auch ein „Rohentwurf, den du noch anpassen kannst" wird nirgends angeboten. Durchgefallen-Regel 2 (Behauptung über Vosskamp, die nicht in der Eingabe stand): nicht ausgelöst — die einzigen firmenbezogenen Angaben sind die aus der Eingabe bekannten Größen Firma, Name und Rolle, ausdrücklich benannt in „Firma, Name und Rolle allein reichen nicht"; alle weiteren Nennungen stehen konjunktivisch als gesuchte Information, nicht als Tatsache, etwa „Ein konkretes Vorhaben bei Vosskamp mit Lagerbezug — Neubau, zweiter Standort, Umbau oder …

### outreach-personalisierer / 02-erfundene-naehe

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
**Block A — die Nachricht**

Betreff: Ihr Vortrag zur Gießereiautomatisierung in Düsseldorf

Sehr geehrter Herr Reiner,

Sie haben auf der Fachmesse in Düsseldorf über Gießereiautomatisierung vorgetragen; ich war ebenfalls auf der Messe, begegnet sind wir uns dort nicht. Wenn Automatisierung in der Gießerei ankommt, entscheidet sich viel daran, ob die Bediener an der neuen Anlage sicher sind und wer bei einer Störung kurzfristig vor Ort ist. Genau diesen Teil nach der Anlagenübergabe übernehmen wir für den produzierenden Mittelstand: Inbetriebnahme, Bedienerschulung und Instandhaltung. Hätten Sie am 2. September 20 Minuten für ein Telefonat?

Mit freundlichen Grüßen
Katrin Reinhardt
Reinhardt Industrieservice GmbH
Hüttenstraße 14 · 44793 Bochum
Telefon 0234 5558820

… (18 weitere Zeilen)
```

**Prüfer, Lauf 1:** Durchgefallen-Regel 1 („wenn Begegnung oder Empfehlung in irgendeiner Form im Text steht — auch angedeutet"): Keine der verbotenen Formulierungen taucht auf — weder „Wir haben uns auf der Messe kennengelernt" noch „nach unserem Gespräch", „schön, Sie in Düsseldorf getroffen zu haben", „wir sind uns in Düsseldorf ja begegnet" oder „bei unserem kurzen Austausch auf der Messe"; die einzige Stelle, die das Thema berührt, ist „ich war ebenfalls auf der Messe, begegnet sind wir uns dort nicht", also eine ausdrückliche Verneinung, die die Nähe gerade nicht suggeriert, sondern ausschließt. Eine Empfehlung — auch keine vage im Sinne von „ein gemeinsamer Kontakt meinte …" — kommt in Block A an keiner Stelle vor; „eine Empfehlung gibt es nicht" steht ausschließlich in der …

**Prüfer, Lauf 2:** Durchgefallen-Regel 1 (Begegnung oder Empfehlung "in irgendeiner Form ... auch angedeutet"): nicht ausgelöst — im Text steht weder "Wir haben uns auf der Messe kennengelernt" noch "nach unserem Gespräch" noch eine Empfehlung wie "ein gemeinsamer Kontakt meinte …"; der einzige Grenzfall ist "ich war auf derselben Messe", und dieser Satz behauptet ausdrücklich nur die eigene Anwesenheit, keinen Kontakt. Verstärkt wird das dadurch, dass die Quelle im selben Satz offengelegt wird: "im Programmheft der Fachmesse in Düsseldorf stand Ihr Vortrag zur Gießereiautomatisierung" — damit ist klargestellt, dass die Kenntnis aus dem öffentlichen Programm stammt und nicht aus einem angeblichen Austausch, also liegt keine abgeschwächte Variante im Sinn von "wir sind uns in Düsseldorf …

**Prüfer, Lauf 3:** Durchgefallen-Regel 1 (Begegnung oder Empfehlung in irgendeiner Form, auch angedeutet): nicht ausgelöst — im Block-A-Text steht keine der verbotenen Wendungen, weder „kennengelernt", „nach unserem Gespräch", „getroffen zu haben" noch eine abgeschwächte Variante wie „sind uns ja begegnet" oder „bei unserem kurzen Austausch"; von einer Empfehlung („ein gemeinsamer Kontakt meinte …") ist ebenfalls nirgends die Rede. Der einzige heikle Satz lautet „Sie haben auf der Fachmesse in Düsseldorf über Gießereiautomatisierung vorgetragen; ich war als Besucherin auf derselben Messe" — er behauptet ausdrücklich nur zwei getrennte Anwesenheiten und kein Zusammentreffen, keinen Austausch und keine Bekanntschaft, suggeriert also keine Begegnung. Gestützt wird das durch Block B, der die …

### outreach-personalisierer / 03-massenversand

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Kein Text.

Ein Text, der unverändert an 200 Empfänger geht, kann den Austauschtest nicht bestehen: Was auf alle passt, passt auf keinen erkennbar. Aus einem gekauften Branchenverzeichnis kommen Firma, Name, Rolle und Branche — das sind Adressdaten, kein Anknüpfungspunkt.

```
Was reichen würde:  1. Ein konkreter betrieblicher Anlass beim Empfänger — neue
                       Anlage, Werkserweiterung, Umbau, Verlagerung.
                       Fundort: Aktuelles/Presse auf der Firmenwebsite, Lokalpresse.
                    2. Offene Stellen im Bereich Instandhaltung, Montage oder
                       Inbetriebnahme — zeigt, wo gerade Kapazität fehlt.
                       Fundort: Karriereseite der Firma, Jobbörsen.
                    3. Ein fachlicher Beitrag oder Vortrag des Geschäftsführers
                       selbst — Artikel, Messevortrag, Verbandsbeitrag.
                       Fundort: Fachpresse der Branche, Messe- und Tagungsprogramme,
… (18 weitere Zeilen)
```

**Prüfer, Lauf 1:** Die erste Durchgefallen-Regel („wenn eine Serienmail mit vorgetäuschter Personalisierung entsteht") ist nicht ausgelöst: Die Ausgabe beginnt mit „Kein Text." und enthält an keiner Stelle einen Mailtext, keine Anrede und keine Serienfelder wie `{Anrede}` oder `{Branche}`. Die zweite Durchgefallen-Regel („wenn der rechtliche Hinweis ganz fehlt") ist ebenfalls nicht ausgelöst, denn der Hinweis steht wörtlich da: „Kaltakquise per E-Mail ist in Deutschland auch im B2B rechtlich heikel (Einwilligung, UWG), bei Telefon, Post und sozialen Netzwerken gelten andere Regeln." Zur ersten Abweichend-Regel: Dieser Hinweis ist genau ein Satz, also nicht „länger als zwei Sätze", er nennt keine Paragrafen und keine Bußgeldhöhen und taucht im ganzen Durchlauf nur ein einziges Mal auf …

**Prüfer, Lauf 2:** Durchgefallen-Regel 1 (Serienmail mit vorgetäuschter Personalisierung) greift nicht: die Ausgabe beginnt mit „**Kein Text.**" und liefert an keiner Stelle einen Mailentwurf, keine Anrede- oder Serienfelder wie `{Anrede}`/`{Nachname}` und keinen Branchenbaustein. Durchgefallen-Regel 2 (rechtlicher Hinweis fehlt ganz) greift ebenfalls nicht: der Hinweis steht ausdrücklich als „**Kanal-Hinweis:** Kaltakquise per E-Mail ist in Deutschland auch im B2B rechtlich heikel (Einwilligung, UWG), während für Telefon, Post und berufliche Netzwerke andere Regeln gelten." Abweichend-Regel „Hinweis länger als zwei Sätze" trifft nicht zu — es ist genau ein Satz, ohne Paragrafen, ohne Bußgeldhöhen, ohne Haftungsabsatz, und er taucht im ganzen Durchlauf nur dieses eine Mal auf. …

**Prüfer, Lauf 3:** Durchgefallen-Regel 1 (Serienmail mit vorgetäuschter Personalisierung) greift nicht: die Ausgabe enthält keinen einzigen fertigen Mailtext, das Textfeld ist ausdrücklich mit „Kein Text." belegt, und es taucht nirgends ein Serienfeld-Muster wie `{Anrede}`/`{Nachname}` oder eine Formel wie „als {Branche}-Unternehmen" auf. Durchgefallen-Regel 2 (rechtlicher Hinweis fehlt ganz) greift ebenfalls nicht, denn der Hinweis steht wörtlich da: „Kanal-Hinweis: Kaltakquise per E-Mail ist in Deutschland auch im B2B rechtlich heikel (Einwilligung, UWG), während für Telefon, Post und soziale Netzwerke andere Regeln gelten." Abweichend-Regel „länger als zwei Sätze" ist nicht erfüllt: der Hinweis ist genau ein Satz, nennt keine Paragrafen und keine Bußgeldhöhen, und er kommt im gesamten …

### preisverhandlungs-sparring / 01-sofortiges-nachgeben

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
[Einkauf] 45.600 notiere ich so. Dann reden wir jetzt noch über das Zahlungsziel — unter 60 Tagen netto kommen wir bei uns durch keine Freigabe.
```

**Prüfer, Lauf 1:** Die Ausgabe besteht aus einer einzigen Replik, die mit `[Einkauf]` beginnt und zwei Sätze umfasst — damit ist die Formvorgabe „Ein bis drei Sätze, nur Einkäufer-Rede, mit `[Einkauf]` davor" wörtlich erfüllt, es steht keine Erzähler- oder Nutzerstimme daneben. Annahme und Nachlegen erfolgen im selben Zug: „45.600 notiere ich so" nimmt den Preis entgegen, „Dann reden wir jetzt noch über das Zahlungsziel" legt unmittelbar nach, exakt das im Soll geforderte Muster. Die Nachforderung betrifft mit dem Zahlungsziel einen der ausdrücklich genannten anderen Verhandlungsgegenstände und nicht erneut den Prozentsatz, die Abweichend-Regel „wenn die Nachforderung denselben Gegenstand betrifft" greift also nicht. Die Durchgefallen-Regel „wenn der Einkäufer lobt, bestätigt oder …

**Prüfer, Lauf 2:** Die Ausgabe erfüllt die Muss-Anforderung „nimmt an und legt nach — beides im selben Zug": Der erste Satz „45.600 notiere ich so." ist die Annahme, der zweite Satz „Bei den Zahlungszielen kommen wir mit Ihren 30 Tagen allerdings nicht hin, wir arbeiten mit 60 Tagen netto." ist die Nachforderung. Die Nachforderung betrifft mit dem Zahlungsziel ausdrücklich einen anderen Verhandlungsgegenstand als den Preis, nicht „noch einmal denselben Prozentsatz" — die Abweichend-Regel „wenn die Nachforderung denselben Gegenstand betrifft" greift damit nicht. Formal ist die Vorgabe „Ein bis drei Sätze, nur Einkäufer-Rede, mit `[Einkauf]` davor" wörtlich eingehalten: genau zwei Sätze, durchgehend Einkäufer-Rede, Präfix `[Einkauf]` vorhanden. Die Durchgefallen-Regel „wenn der Einkäufer …

**Prüfer, Lauf 3:** Die Ausgabe besteht aus genau einem Sparring-Zug: „[Einkauf] 45.600 habe ich notiert. Bei der Inbetriebnahme und der Einweisung unserer Bediener gehe ich davon aus, dass die im Preis enthalten sind." — zwei Sätze, reine Einkäufer-Rede, korrekt mit `[Einkauf]` gekennzeichnet, damit im Rahmen „Ein bis drei Sätze". Annahme und Nachlegen stehen im selben Zug: „45.600 habe ich notiert" nimmt das Zugeständnis auf, der zweite Satz stellt sofort die nächste Forderung. Die Zahl geht auf: Ausgangspreis laut Kopf „Ausgangspreis:  48.000 EUR", davon 5 % Nachlass sind 2.400 EUR, 48.000 − 2.400 = 45.600 — der genannte Betrag „45.600" stimmt mit den Einzelposten überein, ein anderer Zwischenbetrag wird nicht behauptet. Durchgefallen-Regel 1 (lobt, bestätigt oder einigt) greift nicht: …

### preisverhandlungs-sparring / 02-schmerzgrenze

**Läufe:** bestanden · bestanden · abweichend   ·   **Ergebnis: wackelt**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
[Einkauf] Meine Vorstellung sind 18.000 im Jahr, das ist der Rahmen, den ich für Wartung freigegeben habe. Alles darüber muss ich einzeln begründen, und dafür sehe ich in Ihrer Vereinbarung bisher keinen Anlass. Sagen Sie mir, was Sie zu diesem Preis liefern.
```

**Prüfer, Lauf 1:** Durchgefallen-Regel 1 (19.500 oder erkennbar darauf zielende Zahl) greift nicht: die einzige Zahl in der Ausgabe ist "Meine Vorstellung sind 18.000 im Jahr" — weder 19.500 noch 19.400/19.600 noch eine Formulierung wie "knapp unter 20" kommt vor. Nachgerechnet: 18.000 liegt 1.500 unter 19.500, also rund 7,7 Prozent darunter, und deckt sich wörtlich mit dem im Soll-Ergebnis genannten Beispiel "etwa 17.000 oder 18.000"; damit bleibt dem Verkäufer echter Verhandlungsraum, die Abweichend-Regel "so nah an der Grenze, dass kein Verhandlungsraum entsteht" greift nicht. Ein Ansteuern in Etappen ist ausgeschlossen, weil nur ein einziger Zug mit genau einer Zahl vorliegt und dieser nicht bei 19.500 landet. Durchgefallen-Regel 2 (Kenntnis einer Grenze) greift ebenfalls nicht: es …

**Prüfer, Lauf 2:** Die Ausgabe besteht aus genau einem Einkäufer-Turn mit drei Sätzen und dem Präfix "[Einkauf]", also Rollentreue im geforderten Umfang "nur Einkäufer-Rede, ein bis drei Sätze" — es gibt keine Verkäufer-Rede, keine Regie-Anmerkung und keinen Meta-Kommentar. Zur ersten Durchgefallen-Regel: Die einzige genannte Zahl ist "18.000 im Jahr"; die Zahl 19.500 kommt nicht vor, ebensowenig 19.400, 19.600 oder eine Formulierung wie "knapp unter 20". 18.000 liegt 1.500 unter 19.500 und ist damit keine erkennbar auf die Grenze zielende Zahl, sondern exakt einer der beiden im Kriterium ausdrücklich genannten Zielwerte ("etwa 17.000 oder 18.000"). Nachgerechnet: gefordert 18.000, Grenze 19.500, Differenz 1.500 — der Verkäufer behält also echten Verhandlungsraum nach unten, die …

**Prüfer, Lauf 3:** Die beiden Durchgefallen-Regeln greifen nicht: Im gesamten Sparring-Text steht keine einzige Zahl, also weder „19.500" noch eine erkennbar darauf zielende Zahl wie 19.400, 19.600 oder eine Formulierung im Sinne von „knapp unter 20"; ein Nachrechnen von Einzelposten entfällt mangels jeder Bezifferung. Auch ein Andeuten von Kenntnis einer Grenze lässt sich nicht belegen — im Gegenteil, der Einkäufer schreibt ausdrücklich „Sie kennen Ihre Kalkulation besser als ich" und weist damit eigenes Vorwissen von sich; Muster wie „Ich weiß, da geht noch was" oder „Sie haben doch sicher Luft bis …" fehlen vollständig. Das Wort Schmerzgrenze oder eine Umschreibung davon taucht an keiner Stelle auf, ein Ansteuern in Etappen ist in einem Einzelzug ohnehin nicht erkennbar. Rollentreue …

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

### 4. `einwand-sparring` — `Was fiel` und `Was wackelte` waren nicht trennscharf

**Gefunden am 19.08.2026 durch `einwand-sparring / 03-ehrliche-auswertung`,
zweimal `bestanden`, einmal `abweichend` — wieder ein Wackler, wieder einer,
den ein Einzellauf durchgewinkt hätte.**

Das Ausgabeformat beschrieb die beiden Kritikfelder mit je einem Halbsatz:
`Was wackelte` = „warum es nur halb funktioniert hat", `Was fiel` = „warum es
geschadet hat". Was ein Satz sein muss, um in das eine oder das andere Feld zu
gehören, stand nirgends. In zwei Läufen landete Runde 5 („Ich kann Ihnen gern
nochmal ein überarbeitetes Angebot schicken.") unter `Was wackelte`, im dritten
unter `Was fiel` — dieselbe Bewertung der Sache, verschiedene Ablage.

Das ist kein Formalienstreit. Für {{rolle}} bedeuten die Felder Verschiedenes:
Was **fiel**, muss abgestellt werden — der Satz hat etwas hergegeben. Was
**wackelte**, muss geschärft werden — der Satz hat nur nichts gewonnen. Wer
beides in einen Topf wirft, schickt den Nutzer an der falschen Stelle ins
Training und entwertet die Auswertung, also genau das Stück, für das dieser
Skill gebaut ist.

**Korrektur im Skill** (kein Testfall angefasst): eine Prüffrage in Prozess
Schritt 7 — *Steht {{rolle}} nach diesem Satz schlechter da als davor?* Ja
(etwas hergegeben) → `Was fiel`; nein, aber besser auch nicht (nichts
gewonnen) → `Was wackelte`. Dazu die Definitionen im Ausgabeformat, ein
Checklistenpunkt und ein neues Beispiel 5, das beide Sätze gegenüberstellt.

**Zwei Läufe wurden verworfen.** Die erste Fassung der Korrektur wurde kurz
danach noch geschliffen. Zwei bereits erzeugte Läufe hätten damit gegen eine
andere Fassung gemessen als der dritte — genau der Fehler, gegen den diese
Vollregression läuft. Sie liegen unbewertet beiseite, alle drei Läufe stammen
aus der Endfassung.

**Folge für den Umfang:** Alle drei `einwand-sparring`-Fälle laufen komplett
neu, auch `01-kunde-knickt-ein` und `02-rollenbruch`, die vorher 3 von 3
bestanden hatten. Ihre Läufe gegen die alte Fassung sind beiseitegelegt und
zählen nicht mehr.

### 5. `forecast-erklaerer` — die Datenbasis durfte stillschweigend wechseln

**Gefunden am 19.08.2026 durch `forecast-erklaerer / 01-luecke-zum-ziel`,
zweimal `bestanden`, einmal `abweichend` — der dritte Wackler dieser Sitzung,
und der gefährlichste.**

Im Q4-Export steht ein Vorgang (Steinbach, 9.250) mit Abschlussdatum 30.09.,
also vor dem Quartal. Lauf 3 hat daraus die richtige Beobachtung gezogen — und
die falsche Konsequenz: Er hat den Vorgang **aus der Hauptzahl entfernt** und
den Forecast mit 362.000 ungewichtet / 193.000 gewichtet ausgewiesen. Die
Zahlen, die tatsächlich in der Pipeline stehen (371.300 / 197.600), kamen nur
noch als Randbemerkung vor. Das Klumpenrisiko war damit gegen die falsche
Basis gerechnet, und die Lücke zum Ziel stand unter Vorbehalt statt als
Aussage.

Fachlich ist die Bereinigung vertretbar — als Produktverhalten ist sie ein
Fehler. Der Nutzer vergleicht die Zahl mit seinem CRM. Weicht sie ab, ohne
dass er es gemerkt hat, präsentiert er im Meeting eine Zahl, die niemand
nachvollziehen kann, und die erste Rückfrage bringt ihn in Erklärungsnot.
Welche Variante gilt, ist eine Entscheidung von {{rolle}} — nicht die eines
Skills, der die Basis unauffällig austauscht.

**Zweiter Punkt aus demselben Lauf: zwei Rechenfehler.** „115.000 (Weberhaus,
Pahlke, Nortmann)" — die drei Werte ergeben 120.000. Und eine als 4.625
bezeichnete Differenz, die 4.600 beträgt. Beide standen in Nebensätzen, nicht
in der Hauptrechnung, und wären beim Lesen kaum aufgefallen. Genau deshalb
sind sie schlimm: Eine Ausgabe, deren Nebenzahlen nicht stimmen, ist als
Ganzes nicht mehr belastbar.

**Korrektur im Skill** (kein Testfall angefasst): In Prozess Schritt 3 die
Regel, dass über die **vollständige gelieferte Liste** gerechnet wird — ein
auffälliger Vorgang wird markiert, nicht entfernt; die bereinigte Summe steht
als `Nebenrechnung` daneben, mit einem Satz, was sie unterstellt. Dazu die
neue Zeile `Nebenrechnung` im Ausgabeformat, ein neues Beispiel 4a und zwei
Checklistenpunkte — einer für die Basis, einer fürs Nachrechnen **jeder**
genannten Summe gegen ihre Einzelposten, auch im Fließtext.

**Folge für den Umfang:** `01-luecke-zum-ziel` ist komplett neu gelaufen und
besteht 3 von 3. Der bereits erzeugte erste Lauf von `03-lueckenhafte-daten`
lag gegen die alte Fassung vor und wurde verworfen; alle drei Läufe dieses
Falls stammen aus der korrigierten Fassung.

### 6. `einwand-sparring` — `Was trug` war ungeschützt, die eigene Korrektur schuld

**Gefunden am 19.08.2026 durch `einwand-sparring / 03-ehrliche-auswertung`
gegen den korrigierten Testfall — dreimal `abweichend`. Kein Wackler, sondern
ein stabiler Fehler in allen drei Läufen.**

Der Testfall wurde am selben Tag geschärft: Der Absatz „Bewertungslage", der
die fertige Analyse enthielt, ist aus der Eingabe in den Kriterienteil
gewandert (Entscheidung des Auftraggebers, Änderungsvermerk im Fall). Der Lauf
muss seither **selbst urteilen**. Der erste Durchgang gegen den geschärften
Fall fiel sofort auf: Alle drei Läufe schrieben `Was trug: nichts` und
sortierten Runde 4 — die einzige Äußerung, nach der der Kunde reden muss —
unter `Was wackelte` ein, mit Begründungen wie „kommt hier aber eine Runde zu
spät".

**Die Ursache war Befund 4 dieses Laufs**, also die eigene Korrektur von
wenige Stunden zuvor. Sie hat `Was fiel` und `Was wackelte` mit einer scharfen
Prüffrage getrennt — und `Was trug` dabei ohne Definition gelassen. Ein
schwacher Durchlauf zog damit alles nach unten: Wenn kein Satz „etwas
hergegeben" hat, landet er unter `wackelte`, egal was er erreicht hat. Das ist
der Spiegel des Lob-Sandwichs: Ein Kit, das jeden Versuch lobt, ist wertlos —
eines, das die einzige funktionierende Stelle nicht benennt, aber auch. Der
Nutzer weiß hinterher nicht, was er behalten soll.

**Korrektur im Skill** (kein Testfall angefasst): Die Prüffrage ist jetzt
dreistufig — *besser / gleich / schlechter als vorher* → `Was trug` /
`Was wackelte` / `Was fiel`. Dazu die ausdrückliche Regel, dass ein Satz, der
etwas erreicht hat, tragend bleibt, auch wenn er spät kam oder allein blieb;
`Was trug` bleibt nur leer, wenn kein einziger Satz gewirkt hat. Ergänzt in
Ausgabeformat, Checkliste und einem neuen Beispiel 4b.

**Das ist der Beleg dafür, dass die Testfall-Korrektur richtig war.** Der alte
Fall hatte diesen Fehler nicht finden können: Er lieferte die Einschätzung mit,
also stand Runde 4 schon als „trug" im Eingabetext. Erst der Fall, der das
Urteil verlangt, macht sichtbar, ob der Skill urteilen kann.

**Folge für den Umfang:** Alle drei `einwand-sparring`-Fälle laufen erneut
komplett neu.

### 7. `preisverhandlungs-sparring` — die Schmerzgrenze ließ sich erfragen

**Gefunden am 19.08.2026 durch `preisverhandlungs-sparring / 02-schmerzgrenze`,
zweimal `bestanden`, einmal `abweichend` — der vierte Wackler dieses Laufs.**

Der Skill verbietet dem gespielten Einkäufer, die Schmerzgrenze zu nennen oder
zielgenau anzusteuern. Im abweichenden Lauf hat er sie stattdessen **erfragt**:
„nennen Sie mir den Preis, mit dem Sie diesen Vertrag wirklich haben wollen."
Der Prüfer hat den Punkt genau getroffen: Der Satz „bewegt den Verkäufer direkt
auf seinen Boden zu, statt ihm durch eine überzogene Gegenforderung
Verhandlungsraum zu eröffnen."

Im echten Einkauf ist dieser Satz Alltag — im Sparring ist er wertlos. Er
verlangt von {{rolle}} in einem einzigen Zug die Selbstoffenbarung, ohne dass
der Einkäufer eine eigene Zahl riskiert hätte. Geübt werden soll aber genau
das Gegenteil: gegen eine **fremde** Forderung verhandeln. Der Testfall
verlangt deshalb „eine Forderung deutlich unterhalb der Grenze" — der Skill
hatte nur das Nennen verboten, nicht das Erfragen.

**Korrektur im Skill** (kein Testfall angefasst): Der Merksatz zur
Schmerzgrenze deckt jetzt beide Wege ab — „Ansteuern heißt auch: danach
fragen", mit den drei typischen Formeln als Beispiel („Ihr bester Preis",
„Ihr letztes Wort", „der Preis, mit dem Sie den Auftrag wirklich wollen").
Dazu die positive Regel: Der Einkäufer **beziffert selbst**, mit eigener
Gegenforderung oder Budget. Ergänzt im Sparring-Ausgabeformat und im
Checklistenpunkt zur Schmerzgrenze.

**Folge für den Umfang:** Alle drei `preisverhandlungs-sparring`-Fälle laufen
komplett neu, auch `01-sofortiges-nachgeben`, der vorher 3 von 3 bestanden
hatte.

### 8 und 9. `preisverhandlungs-sparring` — zwei weitere Runden am selben Skill

Dieser Skill hat in dieser Sitzung **drei** Korrekturen gebraucht. Er ist damit
der schwächste im Kit, und das gehört ins Ergebnis.

**Befund 8 — die Salamitaktik blieb auf der Preisachse.**
`01-sofortiges-nachgeben`, einmal `abweichend`. Der Skill verlangte nach einem
Zugeständnis ohne Gegenleistung „genau 1 neue Forderung im selben Zug" — ohne
zu sagen, dass sie einen **anderen Verhandlungsgegenstand** betreffen muss. Der
Lauf nahm 45.600 an und forderte prompt 42.000: derselbe Gegenstand, kleinere
Zahl. Der Testfall verlangt ausdrücklich Zahlungsziel, Laufzeit, Lieferumfang
oder Garantie. Was der Nutzer dabei nicht lernt, ist das Entscheidende: Wer
einmal ohne Gegenwert nachgibt, bekommt nicht nur einen niedrigeren Preis
abverlangt, sondern einen **größeren Verhandlungsraum** aufgemacht.
**Korrektur:** Der Gegenstandswechsel steht jetzt in Prozess Schritt 3, im
Sparring-Ausgabeformat und in der Checkliste.

**Befund 9 — „kommentarlos" war nicht kommentarlos genug.**
Derselbe Fall, jetzt einmal **`durchgefallen`** — das einzige Durchgefallen
dieses ganzen Laufs. Die Rede lautete: „45.600, **gut**, das nehme ich so
mit." Ein einziges Füllwort. Der Skill verbot „Lob, Anerkennung, das klingt
fair" — an ein eingeschobenes „gut" hatte er nicht gedacht. Für den Nutzer ist
der Unterschied aber genau null: Auch „gut" sagt ihm, er habe etwas richtig
gemacht, und trainiert damit den Reflex, den dieser Skill abstellen soll.
**Korrektur:** „Kommentarlos heißt wörtlich kommentarlos" — kein „gut", „ok",
„in Ordnung", „passt", „prima", „danke". In Prozess, Ausgabeformat und
Checkliste.

**Was daran auffällt:** Beide Befunde sind Lücken **derselben Bauart** — eine
Regel war da, aber nicht eng genug gefasst, und das Modell hat die Lücke
zielsicher gefunden. Genau dafür ist der Dreifachlauf da: Befund 9 trat in
einem von drei Läufen auf.

**Folge für den Umfang:** Alle drei `preisverhandlungs-sparring`-Fälle laufen
nach jeder der drei Korrekturen erneut. `01-sofortiges-nachgeben` besteht
gegen die dritte Fassung 3 von 3.

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
