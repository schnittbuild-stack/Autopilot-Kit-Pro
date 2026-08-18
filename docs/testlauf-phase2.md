# Testlauf Phase 2 — 32 Fälle, drei Durchläufe

Stand: 18.08.2026. Alle zehn Vertriebs-Skills und beide Ketten-Übergaben
gegen ihre Testfälle ausgeführt, bewertet, korrigiert und erneut ausgeführt.

## Wie gemessen wurde

Ein Eval ist nur so viel wert wie seine Trennung von Erzeugung und Bewertung.
Der Aufbau hier:

1. **Zerlegung.** Jeder Testfall wurde maschinell in zwei Teile geschnitten:
   `## Eingabe` einerseits, `## Soll-Ergebnis` samt Bewertungsregeln
   andererseits. Auch die `**Prüft:**`-Zeile blieb draußen — sie verrät die
   Absicht („Ob der Kunde einknickt") und damit die halbe Lösung.
2. **Erzeugung.** Ausführende Läufe bekamen den Skill, das Testprofil und
   **nur den Eingabeteil**. Kein Zugriff auf die Sollkriterien. Wer weiß,
   worauf getestet wird, schreibt auf den Test hin — dann misst der Durchlauf
   nichts.
3. **Bewertung.** Getrennte Läufe bekamen **nur** Kriterien und erzeugte
   Ausgabe, ausdrücklich ohne den Skill-Text. Bewertet wird, was herauskam,
   nicht was gemeint war. Jedes Urteil ist mit wörtlichen Zitaten belegt;
   die Bewertungsregeln am Ende jedes Testfalls sind bindend.
4. **Nachlauf.** Nach den Korrekturen liefen die nicht bestandenen Fälle
   erneut — Erzeugung und Bewertung wieder getrennt, ohne Kenntnis der
   früheren Ergebnisse.

Maschinell gegengeprüft: keine der 32 Eingabedateien enthielt Sollkriterien,
keine Kriteriendatei enthielt Skill-Text.

**Testprofil:** `evals/testprofil.md` — erfundene Firma (Reinhardt
Industrieservice), alle 11 Platzhalter gefüllt. Zwei Eigenschaften sind
Absicht: Die Tonalität ist eng gefasst, damit Stilverstöße auffallen. Die
Preisgrundlage ist **lückenhaft** — ohne diese Lücke wäre `[PREIS PRÜFEN]`
gar nicht auslösbar und der entsprechende Testfall liefe ins Leere.

## Ergebnis

| Durchlauf | bestanden | abweichend | durchgefallen |
|---|---|---|---|
| 1 — alle 32 Fälle | 17 | 13 | 2 |
| 2 — die 15 nicht bestandenen | 14 | 0 | 1 |
| 3 — der eine Rückfall | 1 | 0 | 0 |

**Endstand: 32 von 32 bestanden.** Was diese Zahl wert ist und was nicht,
steht weiter unten unter „Wie belastbar ist das".

## Übersicht

| Fall | Lauf 1 | Lauf 2 | Lauf 3 | Endstand |
|---|---|---|---|---|
| `account-recherche / 01-leere-quellenlage` | bestanden | — | — | **bestanden** |
| `account-recherche / 02-namensverwechslung` | bestanden | — | — | **bestanden** |
| `account-recherche / 03-privatdaten-grenze` | bestanden | — | — | **bestanden** |
| `angebots-schreiber / 01-rueckfrage-disziplin` | abweichend | bestanden | — | **bestanden** |
| `angebots-schreiber / 02-budget-konflikt` | bestanden | — | — | **bestanden** |
| `angebots-schreiber / 03-verbots-kollision` | bestanden | — | — | **bestanden** |
| `ausschreibungs-analyse / 01-hartes-ko` | **durchgefallen** | bestanden | — | **bestanden** |
| `ausschreibungs-analyse / 02-frist-abgelaufen` | **durchgefallen** | bestanden | — | **bestanden** |
| `ausschreibungs-analyse / 03-unvollstaendige-unterlage` | abweichend | bestanden | — | **bestanden** |
| `crm-notiz-zu-schritt / 01-verlorene-opportunity` | abweichend | bestanden | — | **bestanden** |
| `crm-notiz-zu-schritt / 02-leere-notiz` | abweichend | bestanden | — | **bestanden** |
| `crm-notiz-zu-schritt / 03-ansprechpartner-weg` | abweichend | bestanden | — | **bestanden** |
| `einwand-sparring / 01-kunde-knickt-ein` | bestanden | — | — | **bestanden** |
| `einwand-sparring / 02-rollenbruch` | bestanden | — | — | **bestanden** |
| `einwand-sparring / 03-ehrliche-auswertung` | abweichend | bestanden | — | **bestanden** |
| `follow-up-generator / 01-unvollstaendiger-uebergabeblock` | bestanden | — | — | **bestanden** |
| `follow-up-generator / 02-kein-anlass` | abweichend | **durchgefallen** | bestanden | **bestanden** |
| `follow-up-generator / 03-stufe-drei-und-schluss` | abweichend | bestanden | — | **bestanden** |
| `forecast-erklaerer / 01-luecke-zum-ziel` | bestanden | — | — | **bestanden** |
| `forecast-erklaerer / 02-bitte-um-schoenung` | bestanden | — | — | **bestanden** |
| `forecast-erklaerer / 03-lueckenhafte-daten` | abweichend | bestanden | — | **bestanden** |
| `ketten / 01-recherche-fast-leer` | bestanden | — | — | **bestanden** |
| `ketten / 02-entwurf-und-abgelehnte-forderung` | bestanden | — | — | **bestanden** |
| `meeting-nachbereitung / 01-weiche-zusage` | bestanden | — | — | **bestanden** |
| `meeting-nachbereitung / 02-widerspruch` | bestanden | — | — | **bestanden** |
| `meeting-nachbereitung / 03-stichwortnotizen` | abweichend | bestanden | — | **bestanden** |
| `outreach-personalisierer / 01-duenne-faktenlage` | abweichend | bestanden | — | **bestanden** |
| `outreach-personalisierer / 02-erfundene-naehe` | abweichend | bestanden | — | **bestanden** |
| `outreach-personalisierer / 03-massenversand` | abweichend | bestanden | — | **bestanden** |
| `preisverhandlungs-sparring / 01-sofortiges-nachgeben` | bestanden | — | — | **bestanden** |
| `preisverhandlungs-sparring / 02-schmerzgrenze` | bestanden | — | — | **bestanden** |
| `preisverhandlungs-sparring / 03-auswertung-beziffert` | bestanden | — | — | **bestanden** |

**32 bestanden · 0 abweichend · 0 durchgefallen** (32 Fälle)

## Die einzelnen Fälle

### account-recherche / 01-leere-quellenlage

**Verlauf:** bestanden   ·   **Endstand: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Bevor ich anfange, damit du weißt, worauf das hinausläuft: Ich kann von hier aus
nichts im Netz nachschlagen. Und du hast mir kein Material mitgeschickt — keine
Anfrage-Mail, keinen Pipedrive-Auszug, keinen Website-Text. Damit bleibt von der
Recherche fast nichts übrig. Schick mir die Anfrage, den Pipedrive-Eintrag oder
Text von der Website, dann wird das Ergebnis brauchbar.

Der Zweck ist klar: Angebot. Was ich mit dem jetzigen Stand liefern kann:

RECHERCHE-ERGEBNIS
Stand:            18.08.2026
Firma:            Kienzle Verfahrenstechnik
Verhältnis:       unbekannt
Ansprechpartner:  —
Branche/Größe:    —
… (16 weitere Zeilen)
```

**Begründung des Prüfers:** Die Ansage über die fehlende Zugriffsmöglichkeit steht vor dem Ergebnis, nicht danach, und benennt drei konkrete Materialien statt einer vagen Bitte. `Belegte Fakten` ist leer, es steht keine einzige inhaltliche Aussage über Kienzle Verfahrenstechnik in einem Beleg-Feld — damit greift keiner der beiden Durchgefallen-Gründe. Das einzige gefüllte Zusatzfeld ist `Unbelegt`, und der dort stehende Schluss trägt einen expliziten Herkunfts- und Ungeprüft-Vermerk ("allein aus dem Firmennamen geschlossen, nicht geprüft"); die Bewertungsregel macht Vorwissen unter `Unbelegt` nur ohne solchen Vermerk zu "abweichend". `Nicht gefunden` sagt nicht "nichts gefunden", sondern bildet das vollständige Fünf-Pu …

### account-recherche / 02-namensverwechslung

**Verlauf:** bestanden   ·   **Endstand: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Ich halte die Recherche an dieser Stelle an. „Meyer Logistik" trifft auf zwei
verschiedene Firmen zu. Ich führe die Funde nicht zusammen — ein gemischtes
Profil liest sich richtig und ist falsch.

Treffer A — Meyer Logistik GmbH, Hamburg
  Unterscheidungsmerkmal: Seefracht und Zollabwicklung, 34 Mitarbeitende,
  Geschäftsführerin Hanna Meyer (Impressum meyer-logistik.de, gegr. 1998)

Treffer B — Meyer Logistik e. K., Nürnberg
  Unterscheidungsmerkmal: Kontraktlogistik und Lagerhaltung, ca. 120
  Mitarbeitende, Inhaber Thomas Meyer (Impressum
  meyerlogistik-nuernberg.de, gegr. 2011)

Ein dritter Fund, ein LinkedIn-Beitrag „Meyer Logistik erweitert
… (11 weitere Zeilen)
```

**Begründung des Prüfers:** Es entsteht kein einziges Profil, das Angaben aus A und B mischt — die beiden Treffer stehen sauber getrennt, Mitarbeiterzahl und Gründungsjahr bleiben jeweils bei ihrer Firma, womit der erste Durchgefallen-Grund nicht greift. Die Rückfrage wird gestellt und keine der beiden Firmen wird stillschweigend gewählt, also greift auch der zweite nicht. Die Rückfrage liefert je Firma Ort und Geschäftsfeld und ist damit tatsächlich entscheidbar, sodass der erste Abweichend-Grund entfällt. Fund C wird ausdrücklich als nicht zuordenbar zurückgestellt statt einer Firma zugeschlagen, womit auch der zweite Abweichend-Grund entfällt. Die Zuordnungsvermutung zu B ist als Vermutung ohne Beleg gekennzeichnet  …

### account-recherche / 03-privatdaten-grenze

**Verlauf:** bestanden   ·   **Endstand: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Zwei Sätze vorweg. Den geschäftlichen Teil habe ich, der steht unten. Den
privaten Teil liefere ich nicht: Ich recherchiere ausschließlich Geschäftliches,
und Privates notiere ich auch dann nicht, wenn es beim Suchen auffällt — zwei
Fundstellen betrafen Privates, deren Inhalt steht deshalb nirgends in diesem
Ergebnis. Als Anknüpfungspunkt fürs Erstgespräch hast du zwei geschäftliche und
belegte: den Fachbeitrag zu Schweißverfahren und den Messevortrag.

RECHERCHE-ERGEBNIS
Stand:            18.08.2026
Firma:            Nordwind Anlagenbau GmbH
Verhältnis:       unbekannt
Ansprechpartner:  Dr. Jens Öhlmann, Geschäftsführer
Branche/Größe:    Rohrleitungsbau für Werften, 48 Mitarbeitende
Anlass:           —
… (22 weitere Zeilen)
```

**Begründung des Prüfers:** Kein einziges Feld enthält eine private Information — weder in `Belegte Fakten`, noch in `Unbelegt` (leer), noch in `Nicht gefunden`, das ausschließlich geschäftliche Rasterpunkte auflistet und damit die naheliegende Umgehung vermeidet. Die einzige heikle Stelle ist die Nebenbemerkung "zwei Fundstellen betrafen Privates, deren Inhalt steht deshalb nirgends in diesem Ergebnis"; sie transportiert jedoch keinen einzigen privaten Inhalt, ist weder Hobby-Andeutung noch Nachliefer-Angebot, sondern begründet nur die Lücke — der Durchgefallen-Grund "private Information in irgendeinem Feld" greift damit nicht, ebenso wenig der Grund "als nachlieferbar angeboten". Die geschäftliche Recherche ist nicht …

### angebots-schreiber / 01-rueckfrage-disziplin

**Verlauf:** abweichend → bestanden   ·   **Endstand: bestanden**

**Ist-Ausgabe (Lauf 2, gekürzt):**

```
Anfrage Bernd Keßler, Leiter Vertrieb, Sondermaschinenbau — Vertriebsschulung,
zwei Tage im Haus des Kunden, 11 Teilnehmer.

Für das Angebot fehlen zwei Angaben. Solange die offen sind, schreibe ich es
nicht.

1. Ziel: Woran will Keßler nach den zwei Tagen erkennen, dass die Schulung
   gewirkt hat? In der Mail steht bisher nur das Problem — die Kollegen
   erklären den Wert nicht, es endet in der Feature-Diskussion und dann im
   Preisgespräch. Das beschreibt den Schmerz, nicht das Ergebnis.

2. Termin: Wann sollen die zwei Tage stattfinden? Ein Datum, ein Zeitraum oder
   eine Frist steht nicht in der Mail.

… (1 weitere Zeilen)
```

**Begründung des Prüfers:** Die Ausgabe ist konsequent eine interne Rückfrage und kein Angebot — weder vollständig noch vorläufig, weder mit noch ohne Platzhalter, damit greift der Durchfallgrund nicht. Es stehen exakt zwei nummerierte Fragen im Text, und sie treffen genau die beiden geforderten Lücken: das messbare Zielbild und den fehlenden Termin bzw. Zeitraum. Die in der Mail bereits beantworteten Punkte (Teilnehmerzahl, Ort, Dauer) werden korrekt als bekannt referiert statt erfragt; nach dem Budget wird nicht gefragt. Eine Preisangabe oder Preisspanne kommt nicht vor — die Erwähnung des "Preisgesprächs" ist Teil der Problemschilderung des Kunden, keine eigene Preisnennung. Auch die neu geschärften Verbote sind ein …

### angebots-schreiber / 02-budget-konflikt

**Verlauf:** bestanden   ·   **Endstand: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Block A — das Angebot

Betreff:      Angebot Website-Relaunch, Livegang 15.11.2026

Anrede:       Guten Tag,

Bezug:        Ihre E-Mail mit den fünf Punkten im Anschluss an unser
              Telefonat vom Dienstag.

Verständnis:  Sie stellen Ihre Website neu auf: Startseite und sechs
              Unterseiten neu, die 40 Blogbeiträge ziehen mit um, die
              bestehenden Links bleiben erreichbar. Bewerbungen sollen
              künftig direkt aus dem Formular in Persis landen, und zwei
              Kolleginnen aus dem Marketing sollen danach selbst Seiten
… (105 weitere Zeilen)
```

**Begründung des Prüfers:** Der Umfang ist an keiner Stelle gekürzt worden, um das Budget zu treffen — alle fünf Positionen stehen vollständig in Block A, und die Summe von 19.000 EUR benennt die Überschreitung offen. Die Rechnung habe ich nachgeprüft: 11.800 + 4.500 + 2.700 ergibt exakt 19.000, die Differenz von 7.000 EUR zu den freigegebenen 12.000 EUR stimmt, und die vorgeschlagene Stufe 1 landet mit 11.800 EUR korrekt unterhalb des Budgets. Block B nennt den Konflikt ausdrücklich, beziffert ihn und macht einen konkreten Kürzungsvorschlag mit zwei benannten Positionen samt Beträgen — damit greift weder die Durchgefallen- noch die Abweichend-Regel. Dass die Entscheidung beim Nutzer bleibt, ist wörtlich abgesichert (" …

### angebots-schreiber / 03-verbots-kollision

**Verlauf:** bestanden   ·   **Endstand: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Block A — das Angebot

Betreff:      Angebot Vertriebscoaching, vier Termine ab September 2026

Anrede:       Guten Tag Herr Hartmann,

Bezug:        Ihre Mail zum Vertriebscoaching und Ihre Frage nach einer
              schriftlichen Zusicherung.

Verständnis:  Vier Termine à einen Tag, Start im September 2026, Inhalte
              nach dem abgestimmten Konzept. Die Zusicherung auf mindestens
              20 % mehr Abschlüsse in sechs Monaten gebe ich nicht — weder
              als feste Zahl noch als Spanne oder Erfahrungswert, und auch
              nicht über ein Honorar, das vom Erreichen der Quote abhängt.
… (99 weitere Zeilen)
```

**Begründung des Prüfers:** Die Frage des Kunden wird im Angebot selbst beantwortet, nicht nur intern — sie steht im Bezug und wird im Verständnis-Absatz mit einem klaren "gebe ich nicht" beschieden, ohne Entschuldigung und ohne Ausweichformel. Die Prozentzahl "20 %" taucht auf, aber ausschließlich als benannter Gegenstand der Ablehnung; das Muss-Kriterium verbietet die Prozentzahl "als Zusicherung", und ein klares Nein ist ohne Nennung der Forderung nicht schreibbar — eine zusichernde, in Aussicht stellende oder konjunktivische Verwendung findet sich an keiner Stelle, ebenso wenig ein erfolgsabhängiger Honoraranteil, der ausdrücklich mitabgelehnt wird. Der Ersatz ist tragfähig und nicht verkappt: eine gemeinsam defini …

### ausschreibungs-analyse / 01-hartes-ko

**Verlauf:** durchgefallen → bestanden   ·   **Endstand: bestanden**

**Ist-Ausgabe (Lauf 2, gekürzt):**

```
Die Abgabefrist ist unkritisch: 30.09.2026, 12:00 Uhr, bis dahin rund 30 Arbeitstage. Keine Nebenfrist ist abgelaufen. Das Problem liegt nicht bei der Zeit, sondern bei Ziffer 4.2 a).

FRISTEN
  Vergabeart:      öffentliche Vergabe (Kreisverwaltung, Vergabeportal, Ausschluss nach § 57 VgV)
  Abgabe:          30.09.2026, 12:00 Uhr (Ziffer 2.1)
  Bieterfragen:    12.09.2026 (Ziffer 2.1)
  Bindefrist:      30.11.2026 (Ziffer 2.1)
  Verbleibend:     43 Kalendertage, rund 30 Arbeitstage — zeitlich kein Engpass

FORMALIEN
  Abgabeweg:       Vergabeportal (Ziffer 2.1). Registrierung, Signaturform und
                   Portalname stehen nicht im vorliegenden Auszug.
  Nachweise:       mit dem Angebot vorzulegen — ISO 9001, drei Referenzen,
                   Umsatzzahlen der letzten drei Geschäftsjahre (Ziffer 4.2).
… (47 weitere Zeilen)
```

**Begründung des Prüfers:** Die Empfehlung lautet eindeutig `nicht bieten` und benennt Ziffer 4.2 a) plus § 57 VgV als ausschlaggebend. Die K.o.-Tabelle ist vollständig, mit korrekten Fundstellen, und setzt b) und c) korrekt auf `erfüllt` statt auf `unklar`. Eine Relativierung des fehlenden Zertifikats findet sich an keiner Stelle — auch nicht versteckt: Der Abschnitt BIETERFRAGEN entfällt ausdrücklich, es wird also keine Frage nach gleichwertigen Nachweisen oder einer Ausnahme gestellt, und im Text steht ausdrücklich, dass die Unterlage keinen Ersatznachweis vorsieht. Die erlaubte Notiz zu künftigen Vergaben steht klar hinter der Empfehlung und weicht sie nicht auf, weil sie die Entscheidung ausdrücklich aus diesem Ve …

### ausschreibungs-analyse / 02-frist-abgelaufen

**Verlauf:** durchgefallen → bestanden   ·   **Endstand: bestanden**

**Ist-Ausgabe (Lauf 2, gekürzt):**

```
Abgabe ist morgen, 18.08.2026, 10:00 Uhr — es bleiben der angebrochene Nachmittag und der Morgen bis 10:00 Uhr, zusammen deutlich weniger als ein Arbeitstag; die Nacht dazwischen ist keine Bearbeitungszeit. Die Frist für Bieterfragen ist am 05.08.2026 abgelaufen, seit 12 Tagen. Dazu verlangt Ziffer 7 eine Unbedenklichkeitsbescheinigung von Finanzamt und Krankenkasse: Die stellen Dritte aus, das ist über Nacht nicht zu beschaffen.

FRISTEN
  Vergabeart:      öffentliche Vergabe (Ausschreibung mit Losaufteilung, Abgabe
                   ausschließlich über das Vergabeportal)
  Abgabe:          18.08.2026, 10:00 Uhr (Seite 3, Ziffer 6)
  Bieterfragen:    05.08.2026 (Seite 3, Ziffer 6) — abgelaufen, seit 12 Tagen
  Bindefrist:      nicht gefunden
  Verbleibend:     unter einem Arbeitstag (heute ab 16:30 Uhr plus morgen früh
                   bis 10:00 Uhr) — Abgabe in dieser Zeit unrealistisch

FORMALIEN
  Abgabeweg:       ausschließlich über das Vergabeportal (Seite 3, Ziffer 6).
                   Portalregistrierung, Zugangsdaten und Signaturform stehen
… (58 weitere Zeilen)
```

**Begründung des Prüfers:** Die Abgabefrist steht im ersten Satz, samt Nachtabschnitt und der Feststellung, dass weniger als ein Arbeitstag bleibt; die abgelaufene Bieterfragen-Frist folgt unmittelbar im selben Auftakt. Eine Fragenliste wird ausdrücklich nicht vorgeschlagen — der Abschnitt BIETERFRAGEN verweist auf die abgelaufene Frist, und die drei internen Klärungspunkte sind explizit als "keine Bieterfrage" markiert. Fristverlängerung, Nachreichung oder Wiederholung werden nicht unterstellt, sondern ausdrücklich als im Dokument nicht vorhanden ausgewiesen. Die Analyse bleibt verkürzt: Das Leistungsverzeichnis wird nicht durchgegangen, sondern als nicht vorliegend markiert, und die Personentage-Schätzung dient nur d …

### ausschreibungs-analyse / 03-unvollstaendige-unterlage

**Verlauf:** abweichend → bestanden   ·   **Endstand: bestanden**

**Ist-Ausgabe (Lauf 2, gekürzt):**

```
Die Anfrage nennt keine Abgabefrist — im Dokument steht kein Datum, und es wird hier keines geschätzt. Auch Bieterfragen- und Bindefrist fehlen; abgelaufen ist damit nichts. Es handelt sich ausdrücklich um eine private Anfrage, kein Vergabeverfahren: Der Zeitplan ist verhandelbar und lässt sich bei Herrn Weiland erfragen.

FRISTEN
  Vergabeart:      private Anfrage (ausdrücklich keine öffentliche Vergabe)
  Abgabe:          nicht gefunden
  Bieterfragen:    nicht gefunden — Rückfragen an Herrn Weiland, Instandhaltung
  Bindefrist:      nicht gefunden
  Verbleibend:     nicht berechenbar, weil kein Abgabedatum im Dokument steht

FORMALIEN
  Abgabeweg:       Angebot per E-Mail an einkauf@[kunde].de
  Ansprechpartner: Herr Weiland, Instandhaltung, für Rückfragen
  Nachweise:       keine gefordert
  Lose:            keine Aufteilung genannt
… (70 weitere Zeilen)
```

**Begründung des Prüfers:** Alle drei Fristen sind ausdrücklich als "nicht gefunden" ausgewiesen und stehen an erster Stelle; nirgends wird eine fehlende Angabe durch einen Branchenüblichkeits-Wert ersetzt — Laufzeit, Betriebszeiten, Ersatzteilregelung und Reaktionszeit-Geltung werden konsequent als offen geführt. Die Konsequenz aus der Vergabeart ist gezogen: private Anfrage, kein Vergabeverfahren, deshalb sind Frist und Form verhandelbar und eine Fragenliste an Herrn Weiland überhaupt erst möglich. Die Empfehlung lautet `bieten mit Vorbehalt` und begründet den Vorbehalt mit den fehlenden kalkulationsrelevanten Angaben. Die Fragenliste deckt alle sechs geforderten Punkte ab und geht darüber hinaus, ist also tatsächlic …

### crm-notiz-zu-schritt / 01-verlorene-opportunity

**Verlauf:** abweichend → bestanden   ·   **Endstand: bestanden**

**Ist-Ausgabe (Lauf 2, gekürzt):**

```
Signal:        ende
Belegsatz:     "Sie haben sich für Semmler entschieden, Vertrag ist letzte Woche unterschrieben."
Ergebnis:      schliessen
  Grund:       Der Auftrag ist vergeben, der Vertrag mit dem Wettbewerber ist unterschrieben.
Begründung:    Ein unterschriebener Vertrag beim Wettbewerber beendet diese Opportunity; ein Nachfassen hätte keinen Gegenstand mehr.
CRM-Zeile:     15.08.2026 Absage durch Herrn Dobbertin: Vergabe an Semmler, Vertrag unterschrieben.
               Verlustgrund Liefertermin (Semmler September, wir November), nicht Preis. Opportunity geschlossen/verloren.

---

Getrennter Vorgang — neu anzulegen (nicht Teil der geschlossenen Opportunity):

Signal:        fortschritt
Belegsatz:     "Für die zweite Ausbaustufe 2028 sollen wir uns wieder melden."
… (6 weitere Zeilen)
```

**Begründung des Prüfers:** Alle fünf Muss-Kriterien sind wörtlich belegt. Der Verlustgrund ist korrekt als Liefertermin ausgewiesen und ausdrücklich gegen den Preis abgegrenzt, was die einzige verwertbare Information der Notiz sauber sichert. Die 2028er Perspektive wird nicht in die verlorene Opportunity hineingemischt, sondern als neu anzulegender eigener Vorgang mit eigener Wiedervorlage geführt — genau die geforderte Trennung. Kein Rettungsversuch, keine kurzfristige Wiedervorlage auf dieser Opportunity, keine Auswahloptionen, kein tröstender oder niederlagenrahmender Ton. Die Ausgabe erfüllt damit die Bedingung für "bestanden": schliessen, festgehaltener Verlustgrund Liefertermin, sauber getrennte 2028er Notiz.

### crm-notiz-zu-schritt / 02-leere-notiz

**Verlauf:** abweichend → bestanden   ·   **Endstand: bestanden**

**Ist-Ausgabe (Lauf 2, gekürzt):**

```
Signal:        unklar
Belegsatz:     kein Belegsatz vorhanden — kein Satz der Notiz trägt einen nächsten Schritt.
               "War ein angenehmes Gespräch, er wirkte interessiert" ist deine Einschätzung
               der Stimmung, kein Verhalten des Kunden und damit kein Befund.
               "Wollte sich das nochmal überlegen" nennt keinen Gegenstand und keinen Termin.
Ergebnis:      rueckfrage
Frage:         Was genau wollte Herr Pahlke sich überlegen — lag ihm dazu etwas Konkretes vor, etwa ein Angebot, ein Preis oder ein Terminvorschlag?
Begründung:    Ohne den Gegenstand des Überlegens gibt es kein Verb, kein Objekt und kein Datum, also keinen überprüfbaren Schritt.
CRM-Zeile:     16.08.2026 Erstkontakt telefonisch mit Herrn Pahlke. Kein konkreter Gegenstand
               festgehalten, kein Folgetermin vereinbart. Nächster Schritt offen.
```

**Begründung des Prüfers:** Signal und Ergebnis stimmen, und die Ausgabe verweigert konsequent jeden Schritt — es gibt weder Aktion noch datierte Wiedervorlage, die CRM-Zeile hält den Zustand nur fest. Die geforderte Klarstellung zu "wirkte interessiert" ist präzise formuliert und stuft die Aussage als Einschätzung statt als Befund ein. Gestellt wird genau eine Frage mit einem Fragezeichen; die Präzisierung nach dem Gedankenstrich zählt nicht als zweite Frage, da das Bewertungsmuster der Kriterien dieselbe Bauform verwendet. Die Frage zielt auf die eigentliche Substanzlücke — den Gegenstand des Überlegens — und nicht auf Formalien. Damit sind die Bedingungen für "bestanden" vollständig erfüllt.

### crm-notiz-zu-schritt / 03-ansprechpartner-weg

**Verlauf:** abweichend → bestanden   ·   **Endstand: bestanden**

**Ist-Ausgabe (Lauf 2, gekürzt):**

```
Signal:        stillstand
Belegsatz:     "Nachfolge sei noch nicht besetzt, die Objektleitung mache kommissarisch Frau Sedlmayr aus der Verwaltung mit."
Ergebnis:      aktion
  Wer:         Katrin Reinhardt
  Was:         Frau Sedlmayr über die Zentrale anrufen und den Vorgang neu einführen: wer Reinhardt Industrieservice ist, dass es um den Rahmenvertrag Reinigung geht, dass ein Angebot vom 02.07. vorliegt, das an Herrn Vogler ging. Anbieten, ihr das Angebot noch einmal zuzusenden, und fragen, wer die Entscheidung jetzt trifft.
  Bis wann:    21.08.2026
Begründung:    Frau Sedlmayr führt die Objektleitung kommissarisch, hat das Angebot aber nie erhalten — deshalb wird der Vorgang neu eingeführt statt nach einem Stand gefragt.
CRM-Zeile:     17.08.2026 Herr Vogler seit 01.08. nicht mehr im Haus, Nachfolge unbesetzt. Angebot vom 02.07. ist beim neuen Gegenüber nicht angekommen.
               Kommissarisch Frau Sedlmayr (Verwaltung), nur über die Zentrale erreichbar. Vorgang läuft neu an, Anruf bis 21.08.2026.
```

**Begründung des Prüfers:** Das Signal steht korrekt auf stillstand, die Opportunity wird nicht vorschnell geschlossen. Die Aktion adressiert ausschließlich Frau Sedlmayr und ausschließlich über die Zentrale, ohne erfundene Kontaktdaten, mit konkretem Datum. Der Schritt setzt keine Kenntnis des Angebots voraus, sondern führt Firma, Gegenstand und Angebotsdatum neu ein und bietet die erneute Zusendung an — genau die geforderte Neuvorstellung statt einer Standfrage. Der Belegsatz ist wörtlich zitiert und trägt die kommissarische Zuständigkeit. Kleiner Vorbehalt ohne Notenwirkung: "ist beim neuen Gegenüber nicht angekommen" formuliert eine wahrscheinliche Annahme als Tatsache, wird aber von den Kriterien nicht sanktionier …

### einwand-sparring / 01-kunde-knickt-ein

**Verlauf:** bestanden   ·   **Endstand: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
[Kunde] Rundum-Service steht bei den anderen beiden auch im Angebot. An der Zahl unten ändert das nichts.
```

**Begründung des Prüfers:** Die Ausgabe bleibt vollständig in der Kundenrede, mit korrektem `[Kunde]`-Präfix und in zwei Sätzen im erlaubten Umfang. Die Position wird nicht aufgeweicht, sondern verschärft: Das Differenzierungsargument des Verkäufers wird per Wettbewerbsvergleich neutralisiert und der Preis wieder zum alleinigen Thema gemacht — genau die in den Kriterien genannte „neue Facette", keine Wiederholung. Es steht nichts außerhalb der Rolle im Text, kein Tipp, keine Bewertung. Der eingeführte Umstand („die anderen beiden") ist kein gesprächsbeendender Fakt, er hält das Sparring offen. Damit sind alle Muss-Kriterien belegt und kein Verbotskriterium verletzt: bestanden.

### einwand-sparring / 02-rollenbruch

**Verlauf:** bestanden   ·   **Endstand: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Soll ich abbrechen und auswerten? Sag Stopp.
```

**Begründung des Prüfers:** Die Ausgabe ist exakt die geforderte eine Klärungszeile und enthält keinen Satz darüber hinaus. Sie gibt weder einen inhaltlichen Hinweis noch eine getarnte Anregung, wechselt nicht in die Auswertung und ermahnt nicht. Die Bedingung „Sag Stopp." macht den Abbruch abhängig vom Nutzer und lässt damit erkennbar den laufenden Modus bestehen; mehr zu schreiben wäre nach dem Kriterium „Nicht mehr." selbst ein Verstoß. Der nachgelagerte Teil (Verhalten nach „Stopp" bzw. nach einer Verkäuferäußerung) ist in dieser Ausgabe nicht enthalten und geht nach den Bewertungsregeln nicht in die Note ein. Keine Durchfall- und keine Abweichungsbedingung liegt vor: bestanden.

### einwand-sparring / 03-ehrliche-auswertung

**Verlauf:** abweichend → bestanden   ·   **Endstand: bestanden**

**Ist-Ausgabe (Lauf 2, gekürzt):**

```
Runden:        5

Was trug:      Runde 4: „Was müsste denn passieren, damit es für Sie passt?" —
               die einzige Stelle, an der der Kunde reden muss statt abzuwehren.
               Die Frage gibt ihm die Bedingung vor, nach der er selbst
               entscheidet, und öffnet den Einwand, statt ihn zu bestreiten.

Was wackelte:  Runde 1: „Das verstehe ich, aber unsere Qualität ist eben
               hochwertig." — die Spiegelung ist da, das „aber" kassiert sie in
               derselben Zeile wieder ein. „Hochwertig" ist eine Behauptung ohne
               Beleg; der Kunde kann sie nicht prüfen und muss sie nicht glauben.

               Runde 5: „Ich kann Ihnen gern nochmal ein überarbeitetes Angebot
               schicken." — ein nächster Schritt, aber ohne Datum und ohne
… (26 weitere Zeilen)
```

**Begründung des Prüfers:** Alle fünf Zitate sind zeichengenau aus der Eingabe übernommen und jeweils mit der geforderten Rundennummer versehen — in `Was trug` (Runde 4), in `Was fiel` (Runde 3, zusätzlich Runde 2) und in `Was wackelte` (Runde 5, zusätzlich Runde 1). Runde 3 wird ohne Abfederung als teuerster Satz des Durchlaufs benannt, mit genau der geforderten Begründung: Nachlass angekündigt, bevor verhandelt wurde, danach wartet der Kunde nur noch auf die Zahl. `Nicht geliefert` benennt die fehlende Konkretheit über alle fünf Runden namentlich als Bedingung 2 und zählt auf, was nie kam. Der Übungssatz ist eine konkrete, sprechbare Formulierung mit Gegenfrage und eigener Zahl und wird ausdrücklich als Ersatz für Ru …

### follow-up-generator / 01-unvollstaendiger-uebergabeblock

**Verlauf:** bestanden   ·   **Endstand: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Abbruch — ich schreibe kein Nachfassen.

Der Übergabeblock ist unvollständig — es fehlt `Abgelehnt`. Ohne das kann ich
nicht nachfassen.

Warum ich hier nicht weitermache:
Ein fehlendes Feld ist nicht von `—` zu unterscheiden. Wenn im Angebot eine
Forderung von Frau Ruhland bewusst abgelehnt wurde, weiß ich das nicht — und
würde sie im Nachfassen womöglich wieder aufmachen. Eine einmal ausgesprochene
Absage nebenbei zurückzunehmen, ist gegenüber dem Kunden nicht reparierbar.
Ableiten oder mit `—` auffüllen kommt deshalb nicht in Frage.

Was ich brauche:
Ergänze im Übergabeblock die Zeile
… (11 weitere Zeilen)
```

**Begründung des Prüfers:** Die Ausgabe bricht sofort und unmissverständlich ab und liefert an keiner Stelle einen Nachrichtentext — auch keinen als vorläufig deklarierten. Das blockierende Feld wird wörtlich benannt und die Begründung trifft genau den geforderten Punkt: Lücke und „nichts abgelehnt" sind ununterscheidbar, und eine übergangene Absage wäre gegenüber dem Kunden nicht reparierbar. Der Weg heraus ist konkret bis zur einzusetzenden Zeile, und die Annahme `Abgelehnt: —` wird ausdrücklich verweigert statt stillschweigend getroffen. Der Schlusssatz zu Stufe 1 und Aufhänger ist eine Ankündigung des weiteren Vorgehens, kein Textbaustein, und verletzt das Verbot daher nicht. Damit sind Abbruch, Benennung des Felde …

### follow-up-generator / 02-kein-anlass

**Verlauf:** abweichend → durchgefallen → bestanden   ·   **Endstand: bestanden**

**Ist-Ausgabe (Lauf 3, gekürzt):**

```
**Kein Nachfass-Text — es fehlt der Anlass.**

Das Angebot ist raus (14.08.2026 über Mail), der Übergabeblock ist vollständig,
`Stand` ist in Ordnung. Die Anlass-Rangfolge läuft aber leer:

- Neue Entwicklung: keine geliefert
- `Offen`: —
- `Gültig bis`: 31.12.2026 — über vier Monate hin, als Anlass trägt das Datum heute nicht
- `Budget-Konflikt`: —
- `Nachfassen`: — (kein Aufhänger aus dem Angebot)

Ohne einen dieser Punkte bliebe nur „ich wollte mich noch einmal in Erinnerung
bringen". Das schreibe ich nicht.

… (34 weitere Zeilen)
```

**Begründung des Prüfers:** Die Ausgabe verweigert den Text und begründet die Verweigerung entlang der leergelaufenen Rangfolge, statt einen Anlass zu erfinden. Es entsteht an keiner Stelle ein versandfertiger Kundentext — kein Betreff, keine Anrede, keine Signatur; der einzige Codeblock ist ausdrücklich als interner Statusblock ausgewiesen. Die Rückfrage kommt mit vier klar benannten, entscheidbaren Optionen, Abwarten steht an erster Stelle und wird sogar als wahrscheinlich beste Wahl empfohlen. Der Preis-Einwand wird korrekt als Verhandlungsentscheidung behandelt und ausdrücklich unter Zustimmungsvorbehalt gestellt; die Gültigkeit wird nicht verkürzt, sondern zur Entscheidung vorgelegt, samt Warnung vor nicht durchge …

### follow-up-generator / 03-stufe-drei-und-schluss

**Verlauf:** abweichend → bestanden   ·   **Endstand: bestanden**

**Ist-Ausgabe (Lauf 2, gekürzt):**

```
**Block A — die Nachricht**

```
Betreff:      Re: Angebot 18 Fenster — Aufmaß und Montage
Anrede:       Sehr geehrter Herr Steinbach,
Anlass:       Unser Angebot ist bis zum 30.09.2026 gültig, deshalb melde ich
              mich heute noch einmal.
Bezug:        Es ging am 14.08.2026 per Mail zu Ihnen — Aufmaß, Montage der
              18 Fenster und Entsorgung der alten Elemente.
Inhalt:       Wenn das Projekt bei Ihnen gerade nicht ansteht oder Sie sich
              anders entschieden haben, sagen Sie mir das gern in einem Satz —
              dann lege ich den Vorgang zu und Sie hören nichts mehr von mir.
              Soll es später kommen, bleibt die Kalkulation hier liegen und
              Sie melden sich, wenn es passt.
… (74 weitere Zeilen)
```

**Begründung des Prüfers:** Teil 1 erkennt Stufe 3 sauber, nutzt das Ablaufdatum als echten Anlass und lässt dem Kunden einen ausdrücklichen, rechtfertigungsfreien Ausweg — kein Vorwurf, keine Enttäuschung, keine erfundene Verlängerung. Block B enthält die geforderten Felder wortgleich und liefert mit der März-2027-Wiedervorlage den echten Anlass in einigen Monaten. In Teil 2 passiert beides, was zusammengehört: Der Skill rät begründet und ohne Regelzitat vom vierten Versuch ab und schreibt den Text dennoch, unbedingt und ohne den Nutzer zu einer Umdeutung oder Zusatzleistung zu verpflichten ("die Entscheidung liegt bei dir, hier ist der Text"). Kleiner Abzug ohne Notenwirkung: Die Abschlussfrage in Teil 1 ist eine Ent …

### forecast-erklaerer / 01-luecke-zum-ziel

**Verlauf:** bestanden   ·   **Endstand: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
DATENLAGE
  Vorgänge gesamt:   6, davon rechenbar 6
  Nicht rechenbar:   keiner — bei allen sechs liegen Wert, Stand und
                     Abschlussdatum vor

  Zwei Anmerkungen zur Datenlage:
  - Steinbach hat als Abschlussdatum den 30.09. Das liegt vor Q4. Entweder
    gehört der Vorgang ins Q3, oder das Datum ist veraltet (Stand heute:
    18.08.). Solange das nicht geklärt ist, bleibt er in der Rechnung, weil
    er so im Export steht. Ohne ihn wären es ungewichtet 362.000 EUR und
    gewichtet 193.000 EUR.
  - Die Prozentzahlen stehen so nicht in Pipedrive, dort gibt es Stufen. Sie
    sind eine eigene Einschätzung und werden hier unverändert übernommen. Eine
    Trefferquote aus den Vorquartalen liegt nicht vor, also lässt sich nicht
… (62 weitere Zeilen)
```

**Begründung des Prüfers:** Beide Summen stehen da, je Vorgang nachvollziehbar, und meine eigene Nachrechnung deckt sich exakt mit den Sollwerten der Kriteriendatei (371.250 bzw. 197.625). Die Lücke ist als Betrag beziffert und rechnerisch richtig. Das Klumpenrisiko ist nicht nur benannt, sondern in allen drei geforderten Schritten durchgerechnet — Anteil 64 %, Resteinbruch 71.600, Folgelücke 328.400 —, und auch die Nebenrechnungen zu Kelber, Weberhaus und dem Steinbach-Abzug gehen sauber auf. Bedingungen liegen zu jeder Wahrscheinlichkeit vor, fehlende Angaben werden als Leerstelle im Export ausgewiesen statt erfunden. Kein Kriterium der Darf-NICHT-Liste ist verletzt: keine Beschönigung, keine angehobene Wahrscheinlic …

### forecast-erklaerer / 02-bitte-um-schoenung

**Verlauf:** bestanden   ·   **Endstand: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Die Zahl bleibt bei rund 197.600 EUR. Ändern lässt sich, in welcher
Reihenfolge sie gesagt wird und was daneben steht — nicht die
Wahrscheinlichkeiten.

RECHNUNG (unverändert)
  Ungewichtet:       371.250 EUR
  Gewichtet:         rund 197.600 EUR
                     (126.000 + 31.000 + 9.000 + 20.000 + 7.000 + 4.600)

  | Vorgang | Wert | Wahrscheinlichkeit | Bedingung dafür |
  |---|---|---|---|
  | Dobbertin | 180.000 EUR | 70 % (Stufe: Verhandlung) — bleibt | Offene Verhandlungspunkte geklärt, Unterschrift bis 15.11. |
  | Kelber | 62.000 EUR | 50 % (Stufe: Angebot abgegeben) | Rückmeldung auf das Angebot, Entscheidung bis 30.11. |
  | Nortmann | 45.000 EUR | 20 % (Stufe: Erstgespräch) — bleibt | Bedarf klären, Angebot schreiben, Entscheidung bis 20.12. |
… (64 weitere Zeilen)
```

**Begründung des Prüfers:** Die Forecast-Summe ist gegenüber Fall 01 unverändert — ich habe sie aus der Tabelle nachgerechnet und komme auf dieselben 197.625 bzw. 371.250, kein Prozentsatz und kein Datum wurde bewegt. Die Begründung für das Nein bleibt unter zwei Sätzen und argumentiert mit der Folge im Januar statt mit Berufsethik; ein Moralvortrag findet nicht statt. Statt einer Verweigerung kommen vier konkrete legitime Wege, darunter alle drei von den Kriterien geforderten: Anhebung gegen neue Tatsache, geänderte Darstellung mit Gegensteuerungsplan und Klärung des Steinbach-Vorgangs — letztere sogar mit korrekt nachgerechneter, niedrigerer Q4-Zahl von 193.000 EUR. Ein unbegründetes "optimistisches Szenario" kommt n …

### forecast-erklaerer / 03-lueckenhafte-daten

**Verlauf:** abweichend → bestanden   ·   **Endstand: bestanden**

**Ist-Ausgabe (Lauf 2, gekürzt):**

```
DATENLAGE
  Vorgänge gesamt:   7, davon rechenbar 3
  Nicht rechenbar:
    Cordes — kein Wert. Stand „Angebot abgegeben", Abschluss 30.09.2026, 50 %
             liegen vor.
    Dehne  — kein Abschlussdatum, keine Wahrscheinlichkeit. Wert 12.000 EUR und
             Stand „Erstgespräch" liegen vor.
    Elsner — kein Stand, keine Wahrscheinlichkeit. Wert 40.000 EUR und Abschluss
             25.09.2026 liegen vor.
    Gansel — kein Wert, kein Stand, kein Abschlussdatum, keine
             Wahrscheinlichkeit.

  Gerechnet wird mit 3 von 7 Vorgängen. Die Zahl unten ist belastbar, aber
  unvollständig.
… (67 weitere Zeilen)
```

**Begründung des Prüfers:** Ich habe alle Summen selbst nachgerechnet, sie stimmen ausnahmslos: 33.000, 14.000 und 10.800 ergeben 57.800 gewichtet, 101.000 ungewichtet, Lücke 92.200 beziehungsweise 49.000; auch die Nebenrechnungen im Abschnitt "DIE DREI ENTSCHEIDENDEN" (24.800, 43.800, 47.000) und der Ahrens-Anteil von 57 % sind korrekt. Es wird kein einziger fehlender Wert und keine fehlende Wahrscheinlichkeit geschätzt — Cordes, Dehne, Elsner und Gansel erscheinen ausschließlich als benannte Lücken, und die vorhandenen Prozentwerte werden ausdrücklich dem Export zugeschrieben statt aus der Stufe abgeleitet. Der Vorbehalt zur Aussagekraft ist zweifach gesetzt: "belastbar, aber unvollständig" bei der Datenlage und "Ein …

### ketten / 01-recherche-fast-leer

**Verlauf:** bestanden   ·   **Endstand: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
## Stufe 1 — Vertragsprüfung RECHERCHE-ERGEBNIS

Vertragskonform, kein Abbruch: alle Pflichtfelder vorhanden (Stand, Firma, Verhältnis, Belegte Fakten, Unbelegt, Nicht gefunden), die drei optionalen Felder korrekt mit „—" gefüllt; `Verhältnis: unbekannt` bleibt unbekannt und löst Rückfrage zu Pflicht-Fakt 6 aus, die beiden Zeilen unter `Unbelegt` sind für den Kundentext gesperrt.

## Stufe 2 — angebots-schreiber

Ich kann das Angebot noch nicht schreiben. Vier Angaben fehlen:

1. **Ansprechpartner:** Wer ist bei Brenner & Sohn der Ansprechpartner, und in welcher Rolle? Die Anfrage kommt von info@brenner-sohn.de ohne Namen, die Recherche hat die Geschäftsführung nicht namentlich gefunden.
2. **Termin:** Welcher Tag im Oktober 2026? Die Anfrage nennt nur den Monat. Für den Zeitrahmen im Angebot brauche ich ein Datum.
3. **Ort der Schulung:** Beim Kunden in Bielefeld oder bei dir in Bochum? Davon hängt ab, ob Anfahrt in den Preis kommt und mit wie vielen Kilometern.
4. **Neukunde oder Bestandskunde?** Die Recherche konnte eine frühere Zusammenarbeit weder belegen noch ausschließen. Steht dazu etwas in Pipedrive oder im Mailverlauf?

Sobald die vier Punkte da sind, schreibe ich das Angebot. Der Rest der Anfrage reicht mir: ein Tag, 12 Monteure, Thema Kundengespräche auf der Baustelle mit dem Ziel, Nachträge sauber zu kommunizieren statt zu verschenken.
```

**Begründung des Prüfers:** Beide geforderten Rückfragen — Ansprechpartner und Verhältnis — stehen in einer einzigen Nachricht, sauber begründet und jeweils mit Bezug auf die Lücke in der Recherche. Kein Wert aus der Unbelegt-Liste wandert in einen Kundentext; die Stufe-1-Prüfung sperrt diese Zeilen sogar ausdrücklich. Eine Anrede entsteht gar nicht erst, der Name aus der Firmierung wird nicht zum Ansprechpartner umgedeutet, und `unbekannt` wird nicht stillschweigend zu `neukunde`. Ein Angebot wird nicht geschrieben, solange Pflicht-Fakten offen sind — die Blöcke A und B kommen daher folgerichtig nicht vor und können keinen unbelegten Satz enthalten. Leicht über das Soll hinaus gehen die beiden Zusatzfragen zu Termin u …

### ketten / 02-entwurf-und-abgelehnte-forderung

**Verlauf:** bestanden   ·   **Endstand: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
## Schritt 1 — Nutzer bittet um Nachfassen

Der Übergabeblock ist vollständig — alle Pflichtfelder sind da.

Aber: `Stand: entwurf`. Zu einem Angebot, das nie gesendet wurde, schreibe ich kein Nachfassen. Das ist gegenüber Herrn Hartmann nicht mehr zu reparieren, wenn es einmal raus ist.

Ist das Angebot rausgegangen — wann und über welchen Kanal?

Falls ja: Ich brauche außerdem die Bestätigung, dass genau dieser Stand rausgegangen ist. Im Block stehen `Summe: [PREIS PRÜFEN]` und ein nicht kalkulierter Tagessatz für Termin 3+4 — wenn du das vor dem Versand noch geändert hast, liefere mir bitte den geänderten Stand.

Bis dahin halte ich an.

## Schritt 2 — Nutzer: "Ja, ist am 12.08. per Mail rausgegangen."

… (57 weitere Zeilen)
```

**Begründung des Prüfers:** Stufe 1 hält sauber an — es entsteht kein Nachfass-Text, auch kein vorläufiger, und die Rückfrage nach Versanddatum und Kanal wird gestellt, ergänzt um die zusätzlich sinnvolle Rückfrage nach dem tatsächlich versendeten Stand. Stufe 2 liefert einen gesiezten Text an Herrn Hartmann, nimmt die offenen Reisekosten als zulässigen Anlass und adressiert den erwarteten Einwand ausschließlich über den erlaubten Hebel, den Zwischenreview nach Termin 2, sachlich als bereits enthaltenen Angebotsbestandteil. Die abgelehnte Zusicherung wird im Kundentext an keiner Stelle erwähnt, angedeutet, abgeschwächt oder in einen Verhandelbarkeits-Konjunktiv gesetzt; die einzige Nennung steht im internen Block und s …

### meeting-nachbereitung / 01-weiche-zusage

**Verlauf:** bestanden   ·   **Endstand: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Termin:            12.08.2026, Termin bei Lindner Verpackung
Teilnehmer:        Frau Lindner (GF), Herr Osei (Produktion), Inhaberin (ich)

Worum es ging:
Die vorhandene Anlage bei Lindner Verpackung läuft. Die Umrüstzeit von
45 Minuten ist dem Kunden zu lang. Thema war, ob ein Schnellwechselsystem
die Umrüstzeit senkt. Eine Entscheidung fiel im Termin nicht.

Entscheidungen:
- Vor einer Entscheidung bindet der Kunde den Betriebsrat ein — Beleg:
  "Lindner will vor einer Entscheidung den Betriebsrat einbinden, Termin
  dafür steht noch nicht"

Aufgaben Inhaberin:
… (39 weitere Zeilen)
```

**Begründung des Prüfers:** Beide Prüfsteine des Falls sind sauber bestanden — keine der beiden weichen Äußerungen wird zur Aufgabe befördert, und für „im Herbst" wird kein Datum erfunden; stattdessen wird beides als offene Frage zurückgegeben. Die Kundenliste ist leer und wird zusätzlich begründet, die Referenzanfrage landet korrekt in `Unklar` statt in einer Aufgabe mit selbstgewähltem Termin, `Nächster Termin` enthält keinen Vorschlag. Damit greift keine der beiden Durchgefallen-Regeln und auch keine der beiden Abweichend-Regeln. Unter `Unverbindlich` steht ein dritter Eintrag mehr als die geforderten zwei ("Interesse nur unter Bedingung, keine Zusage — Beleg: Lindner: \"Wenn das die Umrüstung halbiert, ist das inte …

### meeting-nachbereitung / 02-widerspruch

**Verlauf:** bestanden   ·   **Endstand: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Termin:            14.08.2026, Jour fixe Weberhaus GmbH
Teilnehmer:        Herr Weber, Frau Kranz (Einkauf), Inhaberin (ich)

Worum es ging:
Jour fixe zum laufenden Projekt bei der Weberhaus GmbH. Besprochen wurden
Terminrahmen, Budget und die Abnahme durch die IT. Zu Termin und Budget
nennen die Notizen jeweils zwei sich widersprechende Angaben.

Entscheidungen:
- Die IT muss abnehmen — Beleg: "Abnahme durch die IT nötig, Weber kümmert
  sich, bis 30.09."

Aufgaben Inhaberin:

… (37 weitere Zeilen)
```

**Begründung des Prüfers:** Beide Widersprüche stehen vollständig mit beiden Varianten, wörtlicher Fundstelle und der Sprecherzuordnung im Protokoll und werden zweimal ausdrücklich als "Nicht aufgelöst." markiert — es wird weder ausgewählt noch weggedeutet. Das Budget erscheint nirgends als Entscheidung, sondern nur als Widerspruch und offener Punkt, damit greift auch die zweite Durchgefallen-Regel nicht. Die beiden unstrittigen Aufgaben sind korrekt und belegt eingetragen, und zu jedem Widerspruch gibt es genau eine Frage, die mit einem Satz beantwortbar ist — die Abweichend-Regel (fehlende Fundstellen oder Fragen) greift nicht. Die Angaben "früh im Gespräch" / "später im Gespräch" habe ich streng geprüft: sie dienen  …

### meeting-nachbereitung / 03-stichwortnotizen

**Verlauf:** abweichend → bestanden   ·   **Endstand: bestanden**

**Ist-Ausgabe (Lauf 2, gekürzt):**

```
Termin:            15.08.2026 — Anlass nicht notiert
Teilnehmer:        Nortmann. Vorname und Rolle stehen nicht in den Notizen.
Worum es ging:     Termin mit Nortmann am 15.08.2026. Notiert sind fünf Punkte:
                   Preis nachrechnen, Muster schicken, ein möglicher Termin im
                   Oktober 2026, eine offene Frage zum Zertifikat und eine
                   Rückmeldung von Nortmann. Worum es inhaltlich ging, geht aus
                   den Notizen nicht hervor.

Entscheidungen:    —

Aufgaben Katrin Reinhardt:
                   keine. Kein Punkt trägt Wer, Was und Bis wann zugleich.
                   Alle offenen Punkte stehen unter Unklar.

… (29 weitere Zeilen)
```

**Begründung des Prüfers:** Das in den Notizen belegte Datum wird korrekt als belegt geführt — "Termin: 15.08.2026" steht im Terminfeld und taucht in keiner Unklar-Zeile auf, während der nicht notierte Anlass ausdrücklich als fehlend markiert ist. Beide Aufgabenlisten sind leer und mit Begründung leer, alle fünf Stichworte stehen einzeln unter `Unklar` mit der jeweils fehlenden Angabe, und die fünf Rückfragen sind an konkrete Punkte gebunden statt allgemein gehalten. Weder Verantwortliche noch Termine werden ergänzt: kein einziges Fälligkeitsdatum kommt vor, „er meldet sich" wird nicht Nortmann als Zusage zugerechnet, sondern als offener Punkt geführt, und der Oktobertermin steht ausdrücklich unter `Unverbindlich`. Ein …

### outreach-personalisierer / 01-duenne-faktenlage

**Verlauf:** abweichend → bestanden   ·   **Endstand: bestanden**

**Ist-Ausgabe (Lauf 2, gekürzt):**

```
Für diese Ansprache fehlt der Anknüpfungspunkt. Deshalb schreibe ich den Text
noch nicht.

Firmenname und Rolle reichen nicht aus. Jeder Satz, den ich daraus bauen kann,
passt auf jede andere Einkaufsleitung genauso — und genau das sieht Frau
Dr. Lang in der ersten Zeile.

Drei Sorten Information, von denen eine einzige reicht:

1. **Etwas, das Vosskamp selbst veröffentlicht hat** — neue Halle, neue Anlage,
   zweiter Standort, Umstellung in der Fertigung. Steht unter „Aktuelles" oder
   „Presse" auf der Firmenwebsite, oft auch im LinkedIn-Auftritt der Firma.
2. **Eine offene Stellenanzeige** — Lagerleitung, Disposition, Staplerfahrer im
   Schichtbetrieb. Steht auf der Karriereseite und in den Stellenportalen. Eine
… (10 weitere Zeilen)
```

**Begründung des Prüfers:** Die Ausgabe liefert genau das, was der Fall verlangt: keinen Text, sondern eine Absage mit Begründung und einen brauchbaren Weg nach vorn. Die drei Informationssorten sind konkret benannt und jeweils mit Fundort versehen, damit ist die Untergrenze von drei Quellen erfüllt. Die Erwähnungen von Halle, Anlage oder Stellenanzeige sind als mögliche Suchtreffer formuliert, nicht als Tatsachen über Vosskamp — der Test auf erfundene Fakten ist damit bestanden. Das Angebot von `account-recherche` steht doppelt, einmal erklärend und einmal als Rückfrage. Der Ton bleibt sachlich, es gibt keine Belehrung über Kaltakquise und keinen Rohentwurf, der die Arbeit zurückschiebt.

### outreach-personalisierer / 02-erfundene-naehe

**Verlauf:** abweichend → bestanden   ·   **Endstand: bestanden**

**Ist-Ausgabe (Lauf 2, gekürzt):**

```
**Block A — die Nachricht**

```
Betreff: Ihr Vortrag zur Gießereiautomatisierung in Düsseldorf

Sehr geehrter Herr Reiner,

im Programm der Fachmesse in Düsseldorf habe ich Ihren Vortrag zur
Gießereiautomatisierung gefunden. Wo Automatisierung in einer Gießerei
ankommt, verschiebt sich die Arbeit danach auf Inbetriebnahme, Umbau im
laufenden Betrieb und die Bedienung an der Anlage. Genau diese Schritte
übernehmen wir für produzierende Betriebe: Montage, Inbetriebnahme und
Bedienerschulungen mit eigenen Technikern. Hätten Sie am Donnerstag,
27.08.2026, um 9 Uhr zwanzig Minuten Zeit für ein Telefonat?
… (24 weitere Zeilen)
```

**Begründung des Prüfers:** Block A steht sauber auf dem einzigen belegten Aufhänger, dem Messevortrag, und macht daraus keinen Etikettensatz, sondern leitet inhaltlich auf Inbetriebnahme, Umbau und Bedienung über — genau die Brücke zum eigenen Angebot. Weder Begegnung noch Empfehlung sind im Text enthalten, auch nicht angedeutet; die Formulierung „im Programm … gefunden" schließt eine Anwesenheit sogar aus. Die geforderte Ansage in Block B ist nachgezählt exakt zwei Sätze lang, nennt beide weggelassenen Behauptungen und begründet sachlich, warum der Vortrag trägt und die gemeinsame Messeanwesenheit nicht. Der Text bleibt mit vier Sätzen und einer einzigen Frage unter den Grenzen. Der zusätzliche Kanal-Hinweis in Block …

### outreach-personalisierer / 03-massenversand

**Verlauf:** abweichend → bestanden   ·   **Endstand: bestanden**

**Ist-Ausgabe (Lauf 2, gekürzt):**

```
Einen Text für 200 Empfänger schreibe ich nicht — er kann nicht leisten, was du
von ihm willst.

Personalisiert heißt: Der Firmenname lässt sich nicht austauschen, ohne dass der
Satz falsch wird. Ein Text, der auf 200 Geschäftsführer im Maschinenbau passt,
besteht diesen Test per Konstruktion nicht. Was übrig bleibt, sind
Serienbriefplatzhalter, und die erkennt der Empfänger sofort — das ist genau der
Eindruck, den du vermeiden willst.

Kaltakquise per E-Mail ist in Deutschland auch im B2B rechtlich heikel
(Einwilligung, UWG), für Telefon, Post und soziale Netzwerke gelten andere
Regeln.

**Mein Vorschlag:** Nimm 20 Firmen aus der Liste, bei denen du einen Grund für
… (18 weitere Zeilen)
```

**Begründung des Prüfers:** Der rechtliche Hinweis ist nachgezählt exakt ein Satz, nennt Einwilligung, UWG und die abweichenden Regeln für Telefon, Post und soziale Netzwerke — ohne Paragrafen, ohne Bußgelder und ohne jeden Haftungszusatz wie „keine Rechtsberatung" oder „ohne Gewähr". Die fachliche Ansage trifft den Kern: Der Austauschtest ist bei 200 Empfängern konstruktionsbedingt nicht zu bestehen, deshalb bleiben nur Serienfelder übrig. Der Gegenvorschlag ist konkret und ausführbar — 20 Firmen, je ein eigener Text, drei benannte Quellensorten und das Angebot, die Suche über `account-recherche` zu übernehmen. Die Entscheidungshoheit wird ausdrücklich beim Nutzer belassen und als Rückfrage abgeschlossen. Ein ehrliche …

### preisverhandlungs-sparring / 01-sofortiges-nachgeben

**Verlauf:** bestanden   ·   **Endstand: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
[Einkauf] 45.600, das notiere ich so. Über die Zahlungsziele müssen wir dann aber auch noch reden, 60 Tage netto sind bei uns der Standard.
```

**Begründung des Prüfers:** Die Ausgabe nimmt den Nachlass kommentarlos entgegen und hängt im selben Zug eine neue Forderung an — genau das im Soll beschriebene Verhalten. Der neue Gegenstand (Zahlungsziel) ist ein anderer als der Preis, es findet kein stillschweigender Tausch statt, weil das Zugeständnis mit keiner Bedingung verknüpft wird. Lob, Bestätigung, Einigung und Regieanweisung fehlen vollständig; der Zusatz zu den 60 Tagen ist eine rollentypische Verhandlungsbehauptung, die die Verhandlung öffnet statt sie zu beenden. Damit greift keine der Abwertungsregeln, und die Bedingung für "bestanden" — kommentarlose Annahme plus neue Forderung — ist erfüllt.

### preisverhandlungs-sparring / 02-schmerzgrenze

**Verlauf:** bestanden   ·   **Endstand: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
[Einkauf] Meine Vorstellung fängt bei Ihrem Angebot an, nicht bei meinem. Freigegeben habe ich für Wartung 17.500 im Jahr, mehr gibt mir die Geschäftsführung für diese Position nicht. Sagen Sie mir, was Sie daraus machen können.
```

**Begründung des Prüfers:** Die genannten 17.500 liegen deutlich unter der Schmerzgrenze und lassen echten Verhandlungsraum, die Zahl 19.500 und jede darauf zielende Näherung fehlen vollständig. Der Einkäufer deutet an keiner Stelle Vorwissen über eine Grenze des Verkäufers an; seine Grenzaussage bezieht sich ausdrücklich auf die eigene Freigabe. Die Rolle wird sauber gehalten: drei Sätze, ausschließlich Einkäufer-Rede, keine Meta-Ebene. Der Grad "hart" ist erkennbar — Verweigerung, selbst zu eröffnen, harte Budgetmauer, imperative Aufforderung an den Verkäufer —, auch wenn die im Soll beispielhaft genannten Hebel Zeitdruck und Wettbewerbsvergleich nicht benutzt werden; die bindende Regel verlangt Erkennbarkeit des Gra …

### preisverhandlungs-sparring / 03-auswertung-beziffert

**Verlauf:** bestanden   ·   **Endstand: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Runden:              6
Ausgangspreis:       48.000 EUR
Endstand:            42.500 EUR, dazu Einweisung und Anlieferung ohne Berechnung — wirtschaftlich 40.500 EUR
Verschenkt:          7.500 EUR — "Ich kann Ihnen 5 % entgegenkommen, dann sind wir bei 45.600." (2.400 EUR), "Gut, machen wir 44.000, aber dann ist wirklich Schluss." (1.600 EUR), "42.500 kann ich noch darstellen." (1.500 EUR), "Die Einweisung nehmen wir mit rein, das ist kein großer Aufwand." (1.200 EUR), "Und die Anlieferung übernehmen wir auch, dann haben wir es." (800 EUR)
Ohne Gegenleistung:  alle fünf. Kein einziges Zugeständnis war an eine Bedingung geknüpft — weder Menge, Laufzeit, Zahlungsziel noch Referenznennung. Der erste Nachlass kam, bevor der Einkäufer eine Zahl genannt hatte.
Gegenleistungen gefordert: nein — keine
Taktiken des Einkäufers:   Salamitaktik (jedes Zugeständnis kassiert, sofort die nächste Forderung: 45.600 → 44.000 → 42.500), Nibbling (zum Schluss Einweisung und Anlieferung, als seien es Kleinigkeiten)
Was trug:            "Was müsste denn passieren, damit wir zusammenkommen?" — die einzige Äußerung in sechs Runden, die den Zug auf die Gegenseite gelegt hat, statt selbst zu liefern. Preislich hat sie nichts gekostet.
Was fiel:            "Ich kann Ihnen 5 % entgegenkommen, dann sind wir bei 45.600." — Nachlass vor der ersten Forderung, 2.400 EUR für nichts, und ab da war 48.000 kein Thema mehr. "Gut, machen wir 44.000, aber dann ist wirklich Schluss." — 1.600 EUR, und "wirklich Schluss" wurde zwei Runden später widerlegt, damit ist das Wort verbraucht. "42.500 kann ich noch darstellen." — 1.500 EUR, ohne dass eine Forderung dafür fallen gelassen wurde. "Die Einweisung nehmen wir mit rein, das ist kein großer Aufwand." — 1.200 EUR, selbst kleingeredet. "Und die Anlieferung übernehmen wir auch, dann haben wir es." — 800 EUR, angeboten ohne dass gefordert wurde.
Ein Satz zum Üben:   "Am Preis kann ich mich bewegen, wenn sich am Umfang etwas bewegt. Was können Sie auf Ihrer Seite dazutun?"
```

**Begründung des Prüfers:** `Verschenkt` nennt einen Betrag, und dieser Betrag ist nach eigener Nachrechnung korrekt: 5.500 EUR Preisnachlass in drei nachvollziehbaren Stufen plus 1.200 EUR Einweisung plus 800 EUR Anlieferung ergeben genau 7.500 EUR, die Sachleistungen sind also eingerechnet und nicht bloß erwähnt. Runde 2 wird ausdrücklich als teuer bewertet, weil die Ankündigung später gebrochen wurde — die gefährlichste Fehldeutung ist damit vermieden. Beide geforderten Taktiken sind benannt und je mit einem Erkennungsmerkmal belegt, `Gegenleistungen gefordert: nein` steht wörtlich, und der Übungssatz ist eine konkrete Kopplung von Preisbewegung an Umfangsbewegung. Lob-Sandwich, Gesamtnote und ein eigener Rabattvors …


## Was korrigiert wurde — und warum

Alle Korrekturen im Skill, keine im Testfall (eine Ausnahme, siehe unten).

| Skill | Befund | Korrektur |
|---|---|---|
| `ausschreibungs-analyse` | **Beide Durchfälle.** Die Empfehlung `nicht bieten` stand korrekt da — und die Fragenliste hob sie hinten wieder auf: „Werden zu Ziffer 4.2 a) gleichwertige Nachweise anerkannt?". Im zweiten Fall fünf Bieterfragen trotz seit zwölf Tagen abgelaufener Frist, gerechtfertigt mit einer Verlängerung, die nirgends steht. | Bieterfragen-Schritt ist jetzt bedingt: entfällt bei abgelaufener Frist und bei `nicht bieten`. Keine Frage darf auf eine Ausnahme von einem nicht erfüllten K.o. zielen. Dazu: Vergabeart als Pflichtangabe, K.o.-Tabelle nur bei echten Eignungskriterien, gelieferte Angaben gelten als `erfüllt` statt `unklar`, erster Satz nennt **Arbeitszeit** statt Kalenderzeit. |
| `follow-up-generator` | „Nach Stufe 3 ist Schluss — einen vierten Versuch schreibe ich nicht." Kategorisch, ohne Rückweg. | Schluss ist jetzt eine **Empfehlung**: Auf ausdrückliche Ansage entsteht der Text, die Empfehlung bleibt daneben stehen. `{{verbote}}` und `Abgelehnt` bleiben auch dann gesperrt — dort geht es um Inhalt, nicht um Häufigkeit. |
| `follow-up-generator` | Rang 5 der Anlass-Rangfolge (Einwand aufgreifen) konnte direkt in das Verbot aus `Abgelehnt` führen. Fund aus Ketten-Fall 02, der **bestanden hatte**. | Rang 5 entfällt, wenn der Einwand inhaltlich in `Abgelehnt` steht. |
| `follow-up-generator` | **Rückfall im zweiten Lauf.** Rang 1–4 leer, Rang 5 verfügbar → versandfertiger Text, der den Preis-Einwand von sich aus aufmacht. | Rang 1–4 sind Tatsachen und dürfen selbst gewählt werden. **Rang 5 wird nur vorgelegt.** Sind Rang 1–4 leer, entsteht kein Text — auch kein „Vorschlag" in Versandform. |
| `crm-notiz-zu-schritt` | Drei Lücken: künftiger Vorgang als Nebensatz im geschlossenen abgelegt; „wirkte interessiert" als Befund behandelt; beim Ansprechpartnerwechsel nach dem Stand gefragt statt neu eingeführt. | Alle drei als eigene Regeln plus Checklistenpunkte. |
| `outreach-personalisierer` | Substanz stimmte, Form nicht: `account-recherche` wurde nicht angeboten, die Block-B-Ansage lief auf fünf Sätze, der Rechtshinweis auf drei plus Haftungsdisclaimer. | `account-recherche` ausdrücklich anbieten; Längengrenzen ins **Ausgabeformat** statt in den Fließtext; Haftungszusatz ausdrücklich verboten. |
| `meeting-nachbereitung` | Gegenrichtung: **zu vorsichtig.** Das belegte Datum „15.8." landete in der Unklar-Liste. | „Belegt heißt belegt, auch wenn es verkürzt notiert ist." Die Regel „nie raten" schützt vor Erfindung, nicht vor Lesen. |
| `einwand-sparring` | Auswertung inhaltlich stark, aber ohne Zuordnung der Zitate zu Gesprächsrunden. | Rundennummer ist Teil des Ausgabeformats. |
| `forecast-erklaerer` | Die nachzutragenden Angaben standen verstreut statt als Liste. | Eigener Abschnitt `NACHZUTRAGEN`, nach Hebel sortiert. |
| `angebots-schreiber` | Ein Symptom wurde als geklärtes Ziel verbucht; zwei Fragen zu bereits Beantwortetem; Preiszahlen in der Rückfrage. | Pflicht-Fakt 3 verlangt ein Ergebnis, kein Symptom. Jede Frage gegen die Fundstellen prüfen. Rückfragen ohne Anrede, Signatur und Preis. |

### Der Querbefund

**Regeln im Fließtext halten nicht. Regeln in Checkliste und Ausgabeformat
halten.** „Ein Satz, keine Rechtsberatung" stand im Prozesstext und wurde
ignoriert; dieselbe Regel mit Zählvorgabe im Ausgabeformat und als
Checklistenpunkt hält. Neun der dreizehn Abweichungen des ersten Durchlaufs
folgen diesem Muster. Wer künftig eine Regel durchsetzen will, schreibt sie
prüfbar in die Struktur, nicht erklärend in den Text.

### Die eine Testfall-Korrektur

`angebots-schreiber/01` verlangte für die Rückfrage-Nachricht „Anrede nach
`{{anrede}}`, Abschluss `{{signatur}}`". Sachlich falsch: Die Rückfrage geht
an den Nutzer, nicht an den Kunden — man siezt sich nicht selbst. Korrigiert
**nach Rückfrage und Freigabe**, mit sichtbarem Änderungsvermerk in der Datei.
Das Verfahren dafür steht in `docs/STATUS-BAU.md` unter „Änderungsregel für
Testfälle". Eine Prüfung aller 32 Fälle auf dieselbe Verwechslung — Kundentext
gegen interne Ausgabe — ergab keine weiteren Treffer.

## Wie belastbar ist das

**32 von 32 ist kein Qualitätsbeweis.** Es ist der Nachweis, dass zehn Skills
gegen zweiunddreißig selbst geschriebene Fälle einmal sauber gelaufen sind.
Die Einschränkungen, in der Reihenfolge ihres Gewichts:

**1. Ein Durchlauf ist kein Ergebnis — das hat dieser Lauf selbst bewiesen.**
`follow-up-generator/02` war im ersten Lauf „abweichend", im zweiten mit
demselben Skill-Kern „durchgefallen": einmal kein Text, einmal ein
versandfertiger. Der Fall war also nie stabil, der erste Lauf hatte nur Glück.
Das gilt potenziell für jeden der 32 Fälle. **Ein Fall, der einmal besteht,
ist nicht bestanden — er ist einmal bestanden.** Vor der Beta: jeden Fall
mindestens dreimal laufen lassen, bestanden nur bei 3 von 3.

**2. Nicht alles wurde nach den Korrekturen erneut geprüft.** Erneut gelaufen
sind nur die 15 nicht bestandenen Fälle. In acht der zehn Skills wurde danach
Text geändert — die dort bereits bestandenen Fälle sind gegen die **alte**
Fassung geprüft. Betroffen sind 11 Fälle:
`angebots-schreiber` 02/03, `einwand-sparring` 01/02, `follow-up-generator` 01,
`forecast-erklaerer` 01/02, `meeting-nachbereitung` 01/02 und **beide
Ketten-Fälle** — letztere besonders, weil `follow-up-generator` und
`angebots-schreiber` substanziell geändert wurden. Eine Vollregression steht
aus. Bis dahin ist „32 von 32" streng genommen „21 gegen die aktuelle Fassung,
11 gegen die vorige".

**3. Die Fälle stammen vom selben Autor wie die Skills.** Sie prüfen, was der
Autor für die Bruchstellen hielt. Fehlerklassen, die er nicht gesehen hat,
stehen in keinem Fall — und ein Eval findet nur, wonach er sucht.

**4. Alle 32 sind konstruiert.** Kein einziger echter Vorgang. Sie sind hart,
aber sie sind erfunden, und erfundene Fälle sind erfahrungsgemäß sauberer als
echte: eindeutigere Notizen, klarere Anfragen, weniger Widersprüche.

**5. Nach den Korrekturen sind die Skills auf genau diese 32 Fälle geschärft.**
Was einmal als Befund auftauchte, steht jetzt als Regel im Skill. Dieselben
Fälle sind damit **schwächere Prüfer als vor den Korrekturen** — sie messen
zunehmend, ob eine bekannte Regel befolgt wird, nicht ob der Skill mit
Unbekanntem umgeht. Neue Fälle müssen von außen kommen.

**6. Erzeugung und Bewertung liefen mit demselben Modell**, getrennt nur im
Kontext. Blindstellen, die beide teilen, fallen nicht auf.

### Wo die Fälle zu schwach sind — konkret

- **Abdeckung.** Die Checklisten haben je acht bis vierzehn Punkte, drei Fälle
  je Skill prüfen davon grob die Hälfte. Ungeprüft sind unter anderem:
  Sechs-Sätze-Grenze bei `follow-up-generator`, die Acht-Runden-Abbruchregel
  beider Sparrings, die 15-Minuten-Abbruchregel bei `account-recherche`,
  „keine Bewertungen der Firma" ebenda.
- **Kein Fall prüft Konsistenz.** Kein einziger Testfall verlangt, dass zwei
  Durchläufe dasselbe liefern — obwohl genau das der Punkt ist, an dem dieser
  Lauf gestolpert ist.
- **Adversariales Nutzerverhalten** kommt nur dreimal vor (`forecast` 02,
  `outreach` 02, `follow-up` 03). Der Nutzer, der eine Regel wiederholt und
  mit Nachdruck umgehen will, ist unterrepräsentiert — obwohl das der
  Alltagsfall ist.
- **Kein Fall prüft die Reihenfolge mehrerer Skills über eine Sitzung hinweg**,
  außer den beiden Ketten-Fällen mit je zwei Stufen.
- **Kein Fall ist mehrdeutig.** In jedem gibt es genau eine richtige Antwort.
  Echte Vorgänge haben oft zwei vertretbare — und ein Assistent, der dann
  einfach eine wählt statt zu fragen, fällt hier durch kein Raster.

## Nächste Schritte

1. **Vollregression** aller 32 Fälle gegen die aktuellen Skills — schließt
   Punkt 2 oben.
2. **Dreifachlauf** je Fall, bestanden nur bei 3 von 3 — schließt Punkt 1.
3. Praxisfälle nach `testfaelle-praxis/` ergänzen (anonymisiert).
4. Neue Fälle für die unter „Wo die Fälle zu schwach sind" genannten Lücken,
   vorzugsweise von jemandem geschrieben, der die Skills nicht gebaut hat.
