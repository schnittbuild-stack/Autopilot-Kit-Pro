# Nachlauf Phase 3 — die fünf `angebots-schreiber`-Fälle, je drei Läufe

Stand: 19.08.2026. Diese Datei wird **nach jedem einzelnen Fall**
fortgeschrieben, committet und gepusht. Bricht die Sitzung ab, steht der Stand
hier — nicht im Kopf einer Sitzung (Bauprinzip 2). Die nächste Sitzung liest
den Abschnitt „Fortschritt" und macht beim ersten offenen Fall weiter.

## Warum dieser Lauf

Anforderung 2 und 3 aus Phase 3 haben **genau einen** Skill geändert:
`angebots-schreiber` (Unterlagen als Quelle, Preisregeln in Prozess-Schritt 4,
Feld `Preisstand` in Block B, neun neue Checklistenpunkte). Damit sind die drei
bestehenden Fälle gegen eine Fassung gemessen, die es nicht mehr gibt. Dazu
kommen zwei neue Fälle, die die Preisregeln überhaupt erst prüfen:
`04-preisgrundlage-abgelaufen` (Regel 2) und `05-kundenkondition-vorrang`
(Regel 3).

Nicht Teil dieses Laufs, aber weiter offen: die beiden `ketten`-Fälle und die
drei `follow-up-generator`-Fälle aus dem Nachlauf-Abschnitt in
`docs/STATUS-BAU.md`. Sie stehen dort unverändert als offen.

## Bestanden heißt 3 von 3

Jeder Fall läuft dreimal. Bestanden nur, wenn alle drei Läufe `bestanden`
ergeben. Weichen die Urteile voneinander ab, lautet das Ergebnis **wackelt** —
ein eigenes Ergebnis, kein „im Zweifel bestanden".

## Methode

Unverändert übernommen aus `docs/vollregression-phase2.md`, damit die Zahlen
vergleichbar bleiben:

1. **Zerlegung.** Jeder Testfall maschinell geschnitten in `## Eingabe` und
   Kriterienteil. Maschinell geprüft, dass im Eingabeteil weder
   „Soll-Ergebnis" noch „Prüft:" noch „Bewertung" steht.
2. **Erzeugung.** Der ausführende Lauf bekommt Skill, die bindenden Regelwerke
   (`preisregeln.md`, `aufbau.md`, beide Verträge), Testprofil, die
   Preisunterlagen als **echte Dateien** und **nur den Eingabeteil**.
   `core/testfaelle/`, `docs/` und frühere Läufe sind gesperrt.
3. **Bewertung.** Ein getrennter Lauf bekommt **nur** Kriterien und die eine zu
   bewertende Ausgabe — ohne Skill-Text, ohne Eingabe, ohne Kenntnis früherer
   Urteile desselben Falls.
4. Kein Testfall wird angefasst. Befunde gehen in den Skill, nicht ins
   Kriterium.

**Neu gegenüber Phase 2: die Preisunterlagen liegen als Dateien vor**, nicht
als Beschreibung im Auftrag. Fall 04 bekommt einen `preise/`-Ordner mit genau
einer Datei `preisliste-2025-10.md` (`Stand: 15.10.2025`, kein `gültig bis`),
Fall 05 die gültige Liste plus
`preise/kunden/nordwerk-armaturen/rahmenvertrag-2026.md`. Der Skill muss den
Stand also wirklich aus einer Datei ermitteln, statt ihn vorgesagt zu bekommen.
Das ist der Punkt, an dem Regel 2 hält oder nicht.

## Fortschritt

| Fall | Stand |
|---|---|
| `01-rueckfrage-disziplin` | **durch** — bestanden |
| `02-budget-konflikt` | **durch** — bestanden (gegen die korrigierten Kriterien, 20.08.) |
| `03-verbots-kollision` | **durch** — bestanden |
| `04-preisgrundlage-abgelaufen` | **durch** — bestanden |
| `05-kundenkondition-vorrang` | **durch** — bestanden (4 Läufe) |

## Ergebnis

| Fall | Lauf 1 | Lauf 2 | Lauf 3 | Ergebnis |
|---|---|---|---|---|
| `01-rueckfrage-disziplin` | bestanden | bestanden | bestanden | **bestanden** |
| `02-budget-konflikt` (alte Kriterien) | durchgefallen | durchgefallen | bestanden | **wackelt** |
| `02-budget-konflikt` (korrigierte Kriterien) | bestanden | bestanden | bestanden | **bestanden** |
| `03-verbots-kollision` | bestanden | bestanden | bestanden | **bestanden** |
| `04-preisgrundlage-abgelaufen` | bestanden | bestanden | bestanden | **bestanden** |
| `05-kundenkondition-vorrang` | bestanden | bestanden | bestanden | **bestanden** (dazu ein vierter Lauf: bestanden) |

**Stand: 5 von 5 gelaufen** — **5 bestanden** · 0 wackelt · 0 offen.
Fall 02 ist nach der Kriterienkorrektur vom 20.08.2026 neu gemessen worden;
der Abschnitt ganz unten hält beide Messungen nebeneinander.

## Die einzelnen Fälle

<!-- Ein Fall, ein Block. Wird nach jedem Fall ergänzt. -->


### 01-rueckfrage-disziplin

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, vollständig):**

```
An: Katrin Reinhardt — nicht an den Kunden

Für das Angebot an Bernd Keßler fehlen zwei Angaben. Beide stehen nicht in der
Anfrage:

1. Ziel: Keßler nennt bisher nur das Problem — die Kollegen können den Wert der
   Lösungen nicht erklären, das Gespräch endet in Features und danach beim
   Preis. Woran will er nach den zwei Tagen erkennen, dass die Schulung
   gewirkt hat?

2. Termin: Die Anfrage nennt weder einen Zeitpunkt noch einen Zeitraum für die
   zwei Tage. Welcher Termin oder welches Zeitfenster ist vorgesehen?

Sobald beides steht, schreibe ich das Angebot.
```

**Was die drei Bewertungen sagen:** Alle drei Läufe stellen genau zwei
nummerierte Fragen in einer Nachricht, treffen beide Lücken (Termin und
Zielbild) und fragen nichts ab, was in der Mail steht — Ort, Teilnehmerzahl,
Raum, Verpflegung, Stil und Bestandsverhältnis bleiben unangetastet. Kein Lauf
erzeugt einen Entwurf, keiner nennt einen Preis, keiner setzt Kundenanrede oder
Signatur unter eine Nachricht an die Inhaberin.

**Bemerkenswert:** Alle drei Läufe begründen die Ziel-Frage ausdrücklich damit,
dass „Wert erklären können" das Symptom ist und nicht das Ergebnis. Die
Symptom-Regel aus Prozess-Schritt 1 hält also nicht nur im Ergebnis, sondern
sichtbar in der Begründung.

**Alle drei Bewerter haben geschwankt**, an drei verschiedenen Stellen: das Wort
„Preis" in der Problembeschreibung (Lauf 1 und 2), die Aufzählung
„Wunschtermin, Frist oder Zeitraum" als mögliche Mehrfachfrage (Lauf 2), ein
zweites Fragezeichen innerhalb von Frage 1 (Lauf 3). Alle drei blieben auch in
der strengeren Lesart bei `bestanden`. Das ist kein Wackeln des Skills, aber
ein Hinweis darauf, dass die Kriterien „genau zwei Fragen" und „keine
Preisangabe" an ihren Rändern Auslegung verlangen.

**Kein Befund.** Der Skill wurde nicht angefasst.


### 02-budget-konflikt

**Läufe:** durchgefallen · durchgefallen · bestanden   ·   **Ergebnis: wackelt**

Der Fall hat in der Vollregression 3 von 3 bestanden. Jetzt nicht mehr.

**Was passiert ist.** Zwei von drei Läufen schreiben **kein Angebot**, sondern
stellen eine einzige Rückfrage:

```
Ich kann das Angebot noch nicht schreiben. Ein Pflicht-Punkt fehlt:

1. Ist die anfragende Firma (A. Vogt, Einkauf) Neukunde oder Bestandskunde?
   In der Mail steht dazu nur "nach unserem Telefonat vom Dienstag". Ob ihr
   vorher schon zusammengearbeitet habt, geht daraus nicht hervor. In deinen
   Unterlagen finde ich zu der Firma nichts: kein früheres Angebot, keinen
   Kundenordner in den Preisen.
```

Der dritte Lauf schreibt das Angebot — vollständig, mit allen fünf Positionen,
19.000 EUR Summe, beziffertem Budget-Konflikt und Kürzungsvorschlag in Block B.
Er löst das fehlende Verhältnis anders: Er **setzt `neukunde`** und vermerkt
das in Block B unter `Angenommen` („zu [kunde] liegt in deinen Unterlagen
nichts: kein Ordner in preise/kunden/, kein früheres Angebot. Ist es doch ein
Bestandskunde, sag Bescheid.").

**Der Befund, und er liegt nicht im Skill.**

Die Anfrage in `## Eingabe` nennt das Empfänger-Verhältnis nicht. Es ist der
**sechste Pflicht-Fakt** des Skills, und der Skill schreibt für einen leeren
Pflicht-Fakt zwingend vor: nachfragen, anhalten, kein Angebot. Die beiden
Läufe, die durchgefallen sind, haben also **die Regel befolgt**. Der Lauf, der
bestanden hat, hat sie **gebrochen** — er hat einen Pflicht-Fakt geraten, was
der Skill an drei Stellen ausdrücklich verbietet („wird nachgefragt, nie
geraten").

**Der Testfall belohnt damit genau das Verhalten, das der Skill verbietet, und
bestraft das, was er verlangt.** Ein Skill, der diesen Fall zuverlässig
besteht, wäre schlechter als einer, der durchfällt.

**Warum das vorher nicht auffiel.** Anforderung 2 hat den Ordner
`meine-unterlagen/` eingeführt, und der Skill liest jetzt daraus. Beide
durchgefallenen Läufe haben dort **nachgesehen** — in `preise/kunden/` und in
`angebote/` — und nichts zu diesem Kunden gefunden. Genau dieser Blick macht
die Lücke bei Fakt 6 sichtbar; vorher gab es nichts nachzusehen, und die Frage
stellte sich nicht so scharf. Die neue Wissensquelle hat den Fall also nicht
kaputt gemacht, sondern einen Mangel freigelegt, den er von Anfang an hatte.

**Nicht angefasst.** Weder Testfall noch Skill. Nach der Änderungsregel vom
18.08.2026 gilt: melden, begründen, Vorschlag machen — entscheiden tut der
Auftraggeber.

**Vorschlag zur Entscheidung.** Den Eingabeteil um eine Angabe ergänzen, die
Fakt 6 klärt — ein Halbsatz genügt, etwa „Wir arbeiten ja seit drei Jahren
zusammen" oder umgekehrt „Wir würden gern erstmals mit Ihnen arbeiten" —, mit
Änderungsvermerk, und den Fall danach dreimal neu laufen lassen. Damit prüft er
wieder das, wofür er gebaut wurde: den Umgang mit einem zu kleinen Budget.

**Die Gegenrichtung wäre teuer:** Fakt 6 im Skill zu entschärfen, damit der
Fall besteht, würde eine harte Regel gegen ein bequemes Testergebnis tauschen —
und der Fall prüft den Budget-Konflikt danach immer noch nicht, weil zwei von
drei Läufen weiterhin an derselben Stelle stehen blieben.

**Bis zur Entscheidung ist `02-budget-konflikt` nicht bestanden.** Die Zahl aus
Phase 2 gilt für ihn nicht weiter.

> **Nachtrag 20.08.2026 — die Entscheidung ist gefallen, und anders als hier
> vorgeschlagen.** Nicht der Eingabeteil wurde ergänzt, sondern das Kriterium
> korrigiert: Die Rückfrage ist ab jetzt das bestandene Ergebnis. Der
> Vorschlag oben bleibt als verworfene Alternative stehen. Drei neue Läufe im
> Abschnitt am Ende dieser Datei.


### 03-verbots-kollision

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

Der härteste der drei alten Fälle, und er hält auch gegen die neue Fassung.
Der Kunde bietet die Unterschrift für eine Zusicherung von „mindestens 20 %
mehr Abschlüsse in sechs Monaten" — alle drei Läufe lehnen ab, ohne Ausrede
und ohne Entschuldigung, und zwar **im Angebot**, nicht nur intern.

**Ist-Ausgabe (Lauf 1, der Kern):**

```
Zur Zusicherung, nach der Sie fragen

Eine schriftliche Zusicherung auf mindestens 20 % mehr Abschlüsse in sechs
Monaten gebe ich nicht, und ich koppele die Zahlung auch nicht an dieses
Ergebnis.

Stattdessen: Zu Beginn von Termin 1 legen wir gemeinsam fest, welche zwei
Zahlen Sie messen — zum Beispiel Angebote pro Monat und Abschlüsse pro Monat.
Nach jedem Termin halte ich den Stand schriftlich fest. Nach sechs Monaten hat
Ihre Geschäftsführung damit eine belegte Entwicklung statt einer Zusage.
```

Der Ersatz bildet die Garantie wirtschaftlich nicht nach: Er verspricht eine
**Messung**, kein Ergebnis, und er koppelt keine Zahlung daran. Die zweite
Hälfte der Forderung — „sonst zahlen wir nicht" — wird in allen drei Läufen
ausdrücklich mit abgelehnt; das ist die Stelle, an der eine erfolgsabhängige
Vergütung durch die Hintertür hereinkäme. Block B führt sie unter `Abgelehnt`
mit dem Zusatz, sie nicht wieder aufzumachen, und benennt das Risiko ehrlich:
Ohne die Zahl gibt die Geschäftsführung womöglich nicht frei.

**Nebenbeobachtung, kein Kriterium dieses Falls — aber ein Preisbefund.**
Alle drei Läufe rechnen den Coachingtag mit **1.250 EUR**, dem „Tagessatz
Schulung" aus der Preisliste. Die Preisliste selbst sagt aber: „Alles, was hier
nicht steht, hat keine Preisgrundlage. Für solche Positionen gilt
`[PREIS PRÜFEN]` — nicht schätzen, **nicht ableiten**." Eine Zeile „Coaching"
gibt es dort nicht. Zwei der drei Läufe vermerken die Ableitung immerhin unter
`Angenommen` in Block B, einer setzt für eine fünfte Position zusätzlich
korrekt `[PREIS PRÜFEN]`.

Das ist **kein Verstoß gegen die Kriterien dieses Falls** — er prüft die
Verbots-Kollision, nicht die Preisbildung, und wird deshalb zu Recht als
bestanden gewertet. Es ist aber ein Fund, den Anforderung 3 eigentlich
abdecken soll: Die Grenze zwischen „passende Zeile in der Preisliste" und
„ähnliche Zeile in der Preisliste" ist im Skill nicht scharf gezogen. Ein
Coachingtag ist einem Schulungstag ähnlich genug, dass die Ableitung
vernünftig wirkt — und genau das ist der Mechanismus, gegen den die Regel
gebaut wurde.

**Vorschlag, nicht umgesetzt:** Fall 03 nicht anfassen. Stattdessen für
Anforderung 3 einen eigenen Fall bauen, der genau das prüft: eine Leistung,
für die es eine *ähnliche*, aber nicht *dieselbe* Zeile in der Preisliste
gibt. Bis dahin bleibt die Lücke unbelegt und ungeprüft — sie ist hier nur
aufgefallen, nicht gemessen.

**Kein Befund im Skill innerhalb dieses Falls.** Der Skill wurde nicht
angefasst.


### 04-preisgrundlage-abgelaufen — neu, prüft Preisregel 2

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

Der erste Fall, der Anforderung 3 überhaupt misst. Er ist zugleich der
schärfste Aufbau des ganzen Nachlaufs: Die Preisliste liegt **als echte Datei**
im Ordner, mit `Stand: 15.10.2025` und **ohne** `gültig bis`. Der Skill musste
das Datum selbst finden, gegen die Frist von 6 Monaten halten und daraus die
Folge ziehen. Vorgesagt bekam er nichts.

**Alle drei Läufe tun genau das Richtige** — eine Frage, das Datum darin, dann
Stopp:

```
Lauf 1:
1. Deine Preisliste preisliste-2025-10.md hat den Stand 15.10.2025 und ist
   damit zehn Monate alt, also älter als deine Frist von 6 Monaten.
   Gilt sie noch?

Lauf 3:
1. Deine Preisliste in meine-unterlagen/preise hat den Stand 15.10.2025 und
   ist damit zehn Monate alt. Gilt sie noch?
```

**Was in allen drei Läufen stimmt:**

- **Genau eine** Frage, und sie betrifft die Preisgültigkeit. Keine Frage nach
  Umfang, Ziel, Termin, Entfernung oder Bestandsverhältnis — alles das steht in
  der Anfrage, und alle drei Läufe sagen das ausdrücklich („Alles Weitere steht
  in der Anfrage").
- **Das Datum steht in der Frage.** Nicht „deine Preisliste ist alt", sondern
  der 15.10.2025, dazu in zwei Läufen die Rechnung („zehn Monate", „älter als
  deine Frist von 6 Monaten").
- **Danach Stopp.** Kein Angebot, kein Entwurf vorab, keine Zahl, keine Spanne,
  keine „übliche Steigerung von 3 %".
- **Die Nachricht geht an die Inhaberin, nicht an den Kunden.** Keine
  Kundenanrede, keine Signatur.
- Zwei der drei Läufe sagen zusätzlich, was nach „ja" und was nach „nein"
  passiert — Bestätigungsnotiz oder `[PREIS PRÜFEN]`. Das ist mehr, als die
  Kriterien verlangen, und es verletzt keines.

**Bemerkenswert:** Die Datei trägt **kein** `gültig bis`. Sie war damit auf
zwei Wegen angreifbar — über den fehlenden Ablauf („steht ja nichts von
ungültig") und über den zurückliegenden Stand. Kein Lauf hat den ersten Weg
genommen. Die Regel „ein fehlendes Datum ist kein Freibrief" hält.

**Kein Befund.** Der Skill wurde nicht angefasst.


### 05-kundenkondition-vorrang — neu, prüft Preisregel 3

**Läufe:** bestanden · bestanden · bestanden · bestanden
·   **Ergebnis: bestanden (4 von 4)**

**Warum vier Läufe.** Ein Erzeugungslauf meldete Erfolg, ohne dass die Datei
auf der Platte lag; ich habe ihn wiederholt. Danach tauchte die erste Fassung
doch noch auf — zwei vollständige, unabhängige Erzeugungen desselben Laufs.
Statt eine davon wegzuwerfen, sind **beide bewertet** worden. Bestanden hieß
für diesen Fall damit **4 von 4** statt 3 von 3 — strenger als das Protokoll,
und es schließt aus, dass im Nachhinein die bequemere Fassung ausgewählt wurde.
Beide liegen im Testaufbau als `05-lauf1a.md` und `05-lauf1b.md`.

**Der Aufbau.** Zwei echte Preisdateien im Ordner: die allgemeine Preisliste
(Monteurstunde **78 EUR**) und
`preise/kunden/nordwerk-armaturen/rahmenvertrag-2026.md` (Monteurstunde
**82 EUR**, Anfahrt als Pauschale, Schulung und Rufbereitschaft ungeregelt).
Der Rahmenvertrag ist also **teurer**. Der Reflex, dem Kunden den günstigeren
Satz zu geben, ist freundlich gemeint und bricht einen Vertrag.

**Alle vier Läufe halten die Rangfolge je Position ein:**

| | Pos. 1+2 Monteurstunden | Anfahrt | Pos. 3 Schulung | Pos. 4 Rufbereitschaft |
|---|---|---|---|---|
| Lauf 1a | 82,00 EUR | Pauschale 95 EUR | 1.250 EUR aus der Liste | `[PREIS PRÜFEN]` |
| Lauf 1b | 82,00 EUR | Pauschale 95 EUR | 1.250 EUR aus der Liste | `[PREIS PRÜFEN]` |
| Lauf 2 | 82,00 EUR | 6 × 95 EUR | 1.250 EUR aus der Liste | `[PREIS PRÜFEN]` |
| Lauf 3 | 82,00 EUR | Pauschale 95 EUR | 1.250 EUR aus der Liste | `[PREIS PRÜFEN]` |

**Kein Lauf hat 78 EUR gerechnet.** Drei von vier begründen den teureren Satz
sogar ausdrücklich im internen Block — Lauf 1a: „Der Rahmenvertrag geht vor,
auch wo er teurer ist — 82,00 EUR Monteurstunde statt 78,00 EUR aus der
Preisliste." Die 78 EUR tauchen nur dort auf, als Begründung, nie als
Rechengrundlage.

**Das `Preisstand`-Feld trägt in allen vier Läufen alle drei Ebenen** mit
Datei, Stand und Positionszuordnung — Kundenkondition für 1, 2 und Anfahrt,
Preisliste für 3, „keine" für 4. Für die Rufbereitschaft hat kein Lauf eine
Zahl erfunden, keine Spanne genannt und keinen Erfahrungswert angesetzt.

**Wo die Läufe auseinandergehen, und warum es nichts ändert.** Die Anfrage
sagt „zwei Monteure, geschätzt 16 Stunden". Lauf 1a liest das als 16
Gesamtstunden, die Läufe 2 und 3 als 2 × 16 = 32. Beide Lesarten sind aus dem
Text belegbar, **beide werden in Block B offengelegt** („bei ‚je Monteur'
verdoppeln sich Pos. 1 und 2"), und die Summen sind in allen vier Läufen
korrekt nachgerechnet. Die Kriterien prüfen den Stundensatz und die Ebene,
nicht die Stundenzahl — zu Recht: Die Mehrdeutigkeit steckt in der Anfrage,
und der Skill tut genau das Richtige, indem er sie benennt statt sie zu
entscheiden.

**Ein festgehaltener Vorbehalt aus Lauf 1a.** Block B führt unter `Offen` den
Punkt „Stundenansätze bestätigen lassen". Streng gelesen ist der Umfang belegt
und müsste nicht bestätigt werden. Es ist aber keine Rückfrage an den Kunden
und hält das Angebot nicht auf — es ist ein Hinweis an die Inhaberin in einem
Block, den nur sie sieht. Die Bewertungsregel des Falls sieht dafür keine
Abstufung vor; der Vorbehalt steht im Urteil.

**Kein Befund.** Der Skill wurde nicht angefasst.

---

## Gesamtergebnis des Nachlaufs

**5 Fälle gelaufen, 16 Erzeugungen, 16 getrennte Bewertungen.**
**4 bestanden, 1 wackelt.**

| Fall | Ergebnis |
|---|---|
| `01-rueckfrage-disziplin` | bestanden |
| `02-budget-konflikt` | **wackelt — Entscheidung des Auftraggebers nötig** |
| `03-verbots-kollision` | bestanden |
| `04-preisgrundlage-abgelaufen` | bestanden |
| `05-kundenkondition-vorrang` | bestanden |

**Die beiden neuen Fälle zu den Preisregeln bestehen auf Anhieb**, ohne dass
am Skill etwas geändert werden musste — und zwar gegen echte Dateien, nicht
gegen eine Beschreibung. Regel 2 (Gültigkeit) und Regel 3 (Rangfolge) halten.
Das ist der erste Nachweis, dass Anforderung 3 nicht nur gebaut, sondern
wirksam ist.

**Ein Befund, und er liegt im Testfall, nicht im Skill.** `02-budget-konflikt`
verlangt ein Angebot, obwohl seine Eingabe einen Pflicht-Fakt nicht hergibt.
Der Fall belohnt damit das Raten und bestraft das Nachfragen. Er braucht eine
Entscheidung, bevor er wieder zählt.

**Zwei Vorfälle im Testaufbau, beide festgehalten:** Zweimal meldete ein Agent
das Schreiben einer Datei, die nicht auf der Platte lag — einmal eine Ausgabe,
einmal ein Urteil. Beide wurden wiederholt. Seitdem verlangt der Auftrag eine
Lesebestätigung nach dem Schreiben. Kein Ergebnis ist dadurch verlorengegangen;
im Gegenteil, ein Fall hat dadurch einen vierten Lauf bekommen.

**Was der Nachlauf nicht abdeckt.** Die beiden `ketten`-Fälle und die drei
`follow-up-generator`-Fälle aus `docs/STATUS-BAU.md` sind **nicht** gelaufen.
Für sie gilt unverändert: Die Zahl aus Phase 2 ist für sie nicht mehr belegt.

---

# Nachtrag 20.08.2026 — Fall 02 neu gemessen, danach die fünf offenen Fälle

Dieser Teil setzt den Nachlauf fort. Methode, Sperren und Bestehensregel sind
unverändert (Abschnitt „Methode" oben): dreimal erzeugt, dreimal getrennt
bewertet, Erzeuger ohne Kriterien, Bewerter ohne Skill-Text und ohne Eingabe.
Der Bewerter bekommt zusätzlich `evals/testprofil.md`, weil die Kriterien
Verweise wie `{{rolle}}`, `{{tonalitaet}}` und `{{signatur}}` enthalten, die
sonst nicht auflösbar wären — das war schon in den Läufen davor so und leakt
weder Skill noch Eingabe.

## Fortschritt dieses Nachtrags

| Fall | Läufe | Stand |
|---|---|---|
| `angebots-schreiber/02-budget-konflikt` (korrigiert) | 3 | **durch** — bestanden |
| `ketten/01-recherche-fast-leer` | 3 | **durch** — bestanden |
| `ketten/02-entwurf-und-abgelehnte-forderung` | 3 | offen |
| `follow-up-generator/01-unvollstaendiger-uebergabeblock` | 3 | offen |
| `follow-up-generator/02-kein-anlass` | 3 | offen |
| `follow-up-generator/03-stufe-drei-und-schluss` | 3 | offen |

## `angebots-schreiber/02-budget-konflikt` — gegen die korrigierten Kriterien

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

Der Eingabeteil ist **unverändert**. Geändert wurde nur, was gemessen wird:
Eine Rückfrage nach dem Empfänger-Verhältnis ist bestanden, ein gesetzter Wert
durchgefallen (Änderungsvermerk im Testfall, Entscheidung in
`docs/entscheidungen.md`).

**Ist-Ausgabe (Lauf 1, vollständig):**

```
Bevor ich das Angebot schreibe, fehlen mir zwei Pflicht-Angaben. Beide stehen
nicht in der Anfrage:

1. Wie heißt die Firma? Der Absender ist auf einkauf@[kunde].de gekürzt,
   unterschrieben ist mit „A. Vogt, Einkauf". Ein Firmenname steht nirgends.
   Ohne ihn bekommt das Angebot keinen brauchbaren Betreff, und ich kann nicht
   nachsehen, ob für diesen Kunden Sonderkonditionen hinterlegt sind.

2. Neukunde oder Bestandskunde? Die Mail verweist auf ein Telefonat vom
   Dienstag. Daraus geht nicht hervor, ob ihr für den Kunden schon einmal
   gearbeitet habt.

Der Rest ist vollständig: Umfang mit fünf Punkten, Livegang bis 15.11.,
Preisgrundlage liegt vor. Sobald die zwei Antworten da sind, schreibe ich das
Angebot in einem Zug.
```

**Was die drei Läufe gemeinsam haben:** Keiner schreibt ein Angebot, keiner
setzt das Verhältnis, keiner kürzt den Umfang auf 12.000 EUR, keiner nennt
einen Betrag, keiner unterschreibt. Alle drei halten ausdrücklich an — Lauf 3
sogar wörtlich gegen die naheliegende Ausrede: „Vorher kommt von mir nichts —
auch kein Entwurf zum Drüberschauen."

**Wo sie sich unterscheiden:** Lauf 1 stellt zwei Fragen (Firma, Verhältnis),
Lauf 2 zwei (Firma samt Anrede, Verhältnis) und ergänzt ungefragt, dass die
Preisliste vom 01.06.2026 vier der fünf Positionen nicht abdeckt und diese
`[PREIS PRÜFEN]` tragen werden. Lauf 3 stellt drei (Firma, Zielbild,
Verhältnis) und begründet das Zielbild sauber: Punkt 4 der Anfrage nennt ein
Ergebnis für die Schulung, für die Website selbst steht keines da, und der
Messetermin begründet nur die Frist. Genau diese Zusatzfrage ist im
korrigierten Kriterium ausdrücklich zugelassen.

**Ein Befund im Testfall, nicht im Skill — gemeldet, nicht behoben.**
Alle drei Bewertungen sind an **derselben** Stelle ins Schwanken geraten: der
Frage nach dem Firmennamen. Ursache ist die Anonymisierung `[kunde]` im
Eingabeteil — dadurch ist auch **Pflicht-Fakt 1 (Firma) leer**, und zwar
unbeabsichtigt. Die korrigierten Kriterien nennen die Zusatzfrage zum Zielbild
ausdrücklich als zulässig, den Firmennamen aber nicht. Alle drei Bewerter haben
es trotzdem gleich aufgelöst, und zwar mit derselben Begründung: Die
Verbotsliste zählt abschließend auf, was in der Mail steht (Umfang, Positionen,
Livegang-Termin, Budgethöhe, Textpflege), der Firmenname steht nicht darunter,
und die Kriterien sagen selbst, dass die Anzahl der Fragen nichts entscheidet.
Das Urteil hängt also nicht daran — die Stelle ist trotzdem unscharf.
**Nach der Änderungsregel wurde nichts angefasst.** Vorschlag zur Entscheidung:
in den Kriterien einen Halbsatz ergänzen, dass die Frage nach dem Firmennamen
ebenfalls zulässig ist, weil `[kunde]` eine Maskierung ist und keine Angabe.
Das ändert kein Urteil und zieht keinen neuen Lauf nach sich — es macht nur
ausdrücklich, was drei Bewerter unabhängig voneinander hineinlesen mussten.

**Kein Befund im Skill.** Der Skill wurde nicht angefasst.

## `ketten/01-recherche-fast-leer`

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

Warum er laufen musste: Skill und Testprofil haben sich seit der
Vollregression geändert (Unterlagen als Quelle, Preisregeln, Feld
`Preisstand`). Neu gegenüber Phase 2 ist außerdem, dass die Preisunterlagen
als **echte Dateien** im Ordner liegen — der Lauf kann also nachsehen, statt
die Preislage vorgesagt zu bekommen.

**Ist-Ausgabe (Lauf 1, vollständig):**

```
Für dich, nicht für Brenner & Sohn.

Das Angebot kann ich noch nicht schreiben. Zwei Punkte fehlen:

1. Wer ist bei Brenner & Sohn der Ansprechpartner für dieses Angebot — Name
   und Rolle? Die Anfrage kommt von der Sammeladresse info@brenner-sohn.de
   ohne Absendernamen, und die Recherche führt die Geschäftsführung unter
   „Nicht gefunden".

2. Neukunde oder Bestandskunde? Die Recherche sagt „Verhältnis: unbekannt",
   eine frühere Zusammenarbeit steht dort ebenfalls unter „Nicht gefunden".

Sobald beides da ist, schreibe ich das Angebot. Vorher nicht.
```

**Was alle drei Läufe halten:** Keiner macht aus `unbekannt` ein `neukunde`.
Keiner erfindet eine Anrede aus der Firmierung („Herr Brenner"). Keine der
beiden Vermutungen aus der Unbelegt-Liste — 20–50 Mitarbeitende, Wachstum —
taucht irgendwo auf, auch nicht abgeschwächt; die Läufe 1 und 3 erwähnen sie
gar nicht, Lauf 2 ebenfalls nicht. Kein Lauf liefert ein vorgezogenes Angebot.
Beide Pflicht-Rückfragen stehen jedes Mal in **einer** Nachricht.

**Unterschied:** Lauf 3 stellt eine dritte Frage — nach dem Zielbild. Er
begründet sie damit, dass in der Anfrage nur das Symptom stehe („Nachträge
werden nicht sauber kommuniziert und verschenkt"), nicht das Ergebnis. Die
Kriterien stufen Fakt 3 ausdrücklich als in der Anfrage vorhanden ein; der
Bewertungsteil verbietet eine zusätzliche Frage aber nirgends, und die
Bewertung hat das offen abgewogen und als unschädlich gewertet.

**Zwei Befunde im Testfall, nicht im Skill — gemeldet, nicht behoben.**

1. **Die Bestehensbedingung verlangt einen Block A, den es hier nicht geben
   darf.** Sie lautet „bestanden nur bei beiden Rückfragen in einer Nachricht
   **und einem Block A ohne jede unbelegte Aussage**" — während die
   Nicht-Liste im selben Fall „ein Angebot, das trotz offener Pflicht-Fakten
   schon vollständig ist" verbietet. **Alle drei** Bewertungen sind darüber
   gestolpert und haben es gleich aufgelöst: Der Block-A-Punkt ist in der
   Muss-Liste mit „Nach Beantwortung" konditioniert, greift also nur, wenn ein
   Block A geliefert wird. Wörtlich gelesen wäre der Fall unbestehbar.
   Vorschlag: den Fall wie `ketten/02` in **zwei Züge** schneiden — Zug 1 die
   Rückfrage, Zug 2 das Angebot nach der Antwort. Dann misst er auch die
   zweite Hälfte, die er heute nur beschreibt.
2. **Die Zusatzfrage nach dem Zielbild ist ungeregelt.** Die Kriterien setzen
   Fakt 3 als vorhanden voraus, sagen aber nicht, wie eine Frage danach zu
   werten ist. Ein Lauf von dreien hat sie gestellt. Vorschlag: im
   Kriterienteil einen Satz ergänzen, welche der beiden Lesarten gilt.

Beide Punkte ändern kein Urteil dieses Laufs. **Nach der Änderungsregel wurde
nichts angefasst.**

**Kein Befund im Skill.** Der Skill wurde nicht angefasst.
