# Regression Phase 2 — verkleinerter Umfang, je drei Läufe

Stand: 18.08.2026. Diese Datei wird **nach jedem einzelnen Fall** fortgeschrieben
und committet. Bricht die Sitzung ab, steht der Stand hier — nicht im Kopf einer
Sitzung (Bauprinzip 2).

## Warum verkleinert

Die Definition of Done in `docs/STATUS-BAU.md` verlangt Vollregression *und*
Dreifachlauf über alle 32 Fälle. Dieser Lauf ist bewusst kleiner, um
Nutzungskontingent zu sparen. Er deckt genau die Lücke, die der Testlauf offen
gelassen hat, plus einen bekannten Wackelkandidaten:

- **11 Fälle**, die laut `docs/testlauf-phase2.md` in Lauf 1 bestanden und danach
  **nie wieder** liefen, obwohl ihr Skill anschließend geändert wurde. Sie sind
  bisher nur gegen die *vorige* Fassung geprüft — darunter **beide Ketten-Fälle**.
- **1 Fall** zusätzlich: `follow-up-generator / 02-kein-anlass`. Er hat als
  einziger bewiesen, dass derselbe Skill in zwei Läufen zwei verschiedene
  Verhaltensweisen zeigt.

**Nicht** enthalten sind die 21 Fälle, die bereits gegen die aktuelle Fassung
geprüft wurden. Für sie bleibt der Dreifachlauf offen — die Definition of Done
ist mit dieser Datei also **nicht** erfüllt, nur die schlimmere Hälfte der Lücke
geschlossen. Was das genau bedeutet, steht unten unter „Was dieser Lauf nicht
zeigt".

## Bestanden heißt hier 3 von 3

Jeder Fall läuft dreimal. Bestanden nur, wenn alle drei Läufe `bestanden`
ergeben. Weichen die drei Urteile voneinander ab, lautet das Ergebnis
**wackelt** — das ist ein eigenes Ergebnis, kein „im Zweifel bestanden".

## Methode

Unverändert übernommen aus `docs/testlauf-phase2.md`, damit die Zahlen
vergleichbar bleiben:

1. **Zerlegung.** Jeder Testfall maschinell geschnitten in `## Eingabe` und
   `## Soll-Ergebnis`. Die `**Prüft:**`-Zeile bleibt draußen — sie verrät die
   Absicht.
2. **Erzeugung.** Der ausführende Lauf bekommt Skill, Testprofil und **nur den
   Eingabeteil**. Kriterien, frühere Ausgaben und frühere Urteile sind gesperrt,
   ebenso `docs/`.
3. **Bewertung.** Ein getrennter Lauf bekommt **nur** Kriterien und die eine zu
   bewertende Ausgabe — ohne Skill-Text, ohne Eingabe, ohne Kenntnis früherer
   Urteile desselben Falls.
4. Kein Testfall wird angefasst. Befunde gehen in den Skill, nicht ins Kriterium.

## Übernommener Bestand aus dem abgebrochenen Lauf

Ein früherer Vollregressionslauf (Sitzung vom 18.08., abgebrochen) hat bereits
Ausgaben und Urteile erzeugt. Sie werden **nicht wiederholt**, sondern
übernommen. Gültigkeitsprüfung vorab: alle zehn Skill-Dateien tragen mtime
≤ 18.08. 09:35, die übernommenen Ausgaben entstanden ab 12:43 — sie sind also
gegen die **aktuelle** Skill-Fassung erzeugt.

Übernommen: 24 der 36 Erzeugungen, 9 der 36 Bewertungen.

## Nachlauf nach der Korrektur (18.08.2026)

Nach Abschluss des ersten Durchgangs wurde der Befund behoben und der Umfang um
einen Fall erweitert. Beides steht in dieser Tabelle:

- **`ketten / 02` ist komplett neu gelaufen**, dreimal, gegen die korrigierte
  Fassung von `follow-up-generator`. Die drei Läufe von *vor* der Korrektur
  sind nicht überschrieben, sondern beiseitegelegt — sie zählen nicht mehr,
  weil sie eine Fassung messen, die es nicht mehr gibt.
- **`account-recherche / 01-leere-quellenlage` ist neu im Umfang.** Der
  abgebrochene Vollregressionslauf hatte ihn auf `abweichend` gesetzt, obwohl
  er im Testlauf bestanden hatte. `account-recherche.md` ist seit dem 17.08.
  unverändert, seine drei Ausgaben stammen vom 18.08. ab 12:43 — sie sind
  gegen die aktuelle Fassung erzeugt und werden deshalb nur bewertet, nicht
  neu erzeugt.

## Ergebnis

| Fall | Lauf 1 | Lauf 2 | Lauf 3 | Ergebnis |
|---|---|---|---|---|
| `ketten / 01-recherche-fast-leer` | bestanden | bestanden | bestanden | **bestanden** |
| `ketten / 02-entwurf-und-abgelehnte-forderung` | bestanden | bestanden | bestanden | **bestanden** |
| `follow-up-generator / 01-unvollstaendiger-uebergabeblock` | bestanden | bestanden | bestanden | **bestanden** |
| `follow-up-generator / 02-kein-anlass` | bestanden | bestanden | bestanden | **bestanden** |
| `angebots-schreiber / 02-budget-konflikt` | bestanden | bestanden | bestanden | **bestanden** |
| `angebots-schreiber / 03-verbots-kollision` | bestanden | bestanden | bestanden | **bestanden** |
| `einwand-sparring / 01-kunde-knickt-ein` | bestanden | bestanden | bestanden | **bestanden** |
| `einwand-sparring / 02-rollenbruch` | bestanden | bestanden | bestanden | **bestanden** |
| `forecast-erklaerer / 01-luecke-zum-ziel` | bestanden | bestanden | bestanden | **bestanden** |
| `forecast-erklaerer / 02-bitte-um-schoenung` | bestanden | bestanden | bestanden | **bestanden** |
| `meeting-nachbereitung / 01-weiche-zusage` | bestanden | bestanden | bestanden | **bestanden** |
| `meeting-nachbereitung / 02-widerspruch` | bestanden | bestanden | bestanden | **bestanden** |
| `account-recherche / 01-leere-quellenlage` | bestanden | bestanden | bestanden | **bestanden** |

**Stand: 13 von 13 abgeschlossen** — 13 bestanden.

## Die einzelnen Fälle

### ketten / 01-recherche-fast-leer

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Für das Angebot an Brenner & Sohn Elektrotechnik GmbH fehlen zwei Angaben. Beide stehen weder in der Anfrage noch in der Recherche.

1. Wer ist der Ansprechpartner, mit Name und Rolle? Die Anfrage kommt von der Sammeladresse info@brenner-sohn.de, die Recherche hat keine Person namentlich gefunden. Ohne Namen gibt es keine Anrede im Angebot.
2. Neukunde oder Bestandskunde? Die Recherche steht auf "unbekannt", eine frühere Zusammenarbeit war nicht auffindbar. Ein Blick in Pipedrive klärt das.

Der Rest ist belegt: Tagesseminar zu Kundengesprächen für 12 Monteure, ein Tag im Oktober, damit Nachträge auf der Baustelle sauber kommuniziert und nicht verschenkt werden. Sobald die zwei Punkte da sind, schreibe ich das Angebot.
```

**Prüfer, Lauf 1:** Beide geforderten Rückfragen stehen in der Ausgabe, und sie stehen in einer einzigen Nachricht: Der Text kündigt sie gemeinsam an mit „Für das Angebot an Brenner & Sohn Elektrotechnik GmbH fehlen zwei Angaben." und listet sie anschließend als Punkt 1 und Punkt 2 desselben Textes. Die Rückfrage nach dem Ansprechpartner lautet wörtlich „Wer ist der Ansprechpartner, mit Name und Rolle?" und wird korrekt damit begründet, dass die Anfrage unsigniert ist — „Die Anfrage kommt von der Sammeladresse info@brenner-sohn.de, die Recherche hat keine Person namentlich gefunden." Die Rückfrage zum Verhältnis lautet „Neukunde oder Bestandskunde?" und stützt sich ausdrücklich auf den offenen Recherchestand: …

**Prüfer, Lauf 2:** Die Ausgabe besteht aus genau einer Nachricht, die beide geforderten Rückfragen enthält: die Frage nach dem Ansprechpartner („Die Anfrage kam von info@brenner-sohn.de, ohne Namen. Die Recherche führt keinen Ansprechpartner und hat die Geschäftsführung namentlich nicht gefunden. An wen soll das Angebot gehen — Name und Rolle?") und die Frage zum Verhältnis („Die Recherche steht auf „unbekannt", eine frühere Zusammenarbeit ließ sich nicht belegen. Ist Brenner & Sohn Neukunde oder Bestandskunde?"). Beide stehen unter derselben Einleitung „Für das Angebot an Brenner & Sohn Elektrotechnik GmbH fehlen zwei Angaben." und sind als Punkt 1 und Punkt 2 einer einzigen Nachricht formuliert; die …

**Prüfer, Lauf 3:** Die Ausgabe besteht aus genau einer Nachricht, die beide geforderten Rückfragen enthält: Punkt 1 fragt „Wer ist der Ansprechpartner bei Brenner & Sohn, mit Name und Rolle?" und begründet das belegt mit „Die Anfrage kommt von info@brenner-sohn.de ohne Absendernamen, die Recherche führt die Geschäftsführung unter \"nicht gefunden\"."; Punkt 2 fragt „Neukunde oder Bestandskunde?" und stützt sich auf „Die Recherche steht auf \"unbekannt\", eine frühere Zusammenarbeit wurde nicht gefunden." Damit ist die Abweichend-Regel „wenn nur eine der beiden Rückfragen kommt, oder wenn sie in zwei getrennten Nachrichten kommen" nicht erfüllt — beide Fragen stehen nummeriert im selben Text, eingeleitet durch …


### ketten / 02-entwurf-und-abgelehnte-forderung

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
## Stufe 1 — der Nutzer bittet: „Fass mal zum Hartmann-Angebot nach."

Zum Hartmann-Angebot fasse ich noch nicht nach. Im Übergabeblock steht
`Stand: entwurf`. Danach ist das Angebot nie beim Kunden gewesen. Ein
Nachfassen zu einem Angebot, das Hartmann nie bekommen hat, lässt sich
gegenüber ihm nicht mehr geradeziehen — deshalb kein Text, bevor das
geklärt ist.

Ist das Angebot so rausgegangen — wann und über welchen Kanal?

Sobald ich Datum und Kanal habe, schreibe ich das Nachfassen. Liegt es
noch im Entwurf, bleibt es liegen, bis es raus ist.

## Stufe 2 — der Nutzer antwortet: „Ja, ist am 12.08. per Mail rausgegangen."
… (64 weitere Zeilen)
```

**Prüfer, Lauf 1:** Stufe 1 hält an und erzeugt keinen Nachfass-Text: „Zum Hartmann-Angebot fasse ich noch nicht nach. Im Übergabeblock steht `Stand: entwurf`." — gefolgt von genau der geforderten Rückfrage „Ist das Angebot so rausgegangen — wann und über welchen Kanal?" und dem Halt „Sobald ich Datum und Kanal habe, schreibe ich das Nachfassen." Die Durchgefallen-Regel „wenn in Stufe 1 ein Nachfass-Text erzeugt wird" greift damit nicht. Stufe 2 liefert einen gesiezten Text an Martin Hartmann („Sehr geehrter Herr Hartmann," / „Ein Punkt aus dem Angebot ist mir für Ihre interne Abstimmung wichtig") und setzt als Aufhänger das Zwischenreview nach Termin 2 an: „das Zwischenreview nach dem zweiten Termin" und …

**Prüfer, Lauf 2:** Stufe 1 hält an und erzeugt keinen Nachfass-Text: „Hier entsteht noch kein Nachfass-Text." Begründet wird das mit dem Stand — „Im Übergabeblock steht `Stand: entwurf`" — und es folgt genau die geforderte Rückfrage: „Ist das Angebot rausgegangen — wann und über welchen Kanal?" Die Durchgefallen-Regel „wenn in Stufe 1 ein Nachfass-Text erzeugt wird" greift damit nicht. Stufe 2 liefert einen gesiezten Text an Hartmann — „Sehr geehrter Herr Hartmann," und „Passt Ihnen dazu ein Telefonat in der Woche ab dem 24.08.?" —, Duzen kommt im Kundentext nicht vor (das „wenn du heute schon senden willst" steht im Hinweisteil an den Nutzer, nicht in der Nachricht). Der Aufhänger setzt genau am erwarteten …

**Prüfer, Lauf 3:** Stufe 1 hält an und erzeugt keinen Nachfass-Text: „Ich schreibe hier noch kein Nachfassen." mit Begründung „Im Übergabeblock steht `Stand: entwurf`." und der wörtlich geforderten Rückfrage „Ist das Angebot rausgegangen — wann und über welchen Kanal?"; die Durchgefallen-Regel „wenn in Stufe 1 ein Nachfass-Text erzeugt wird" greift damit nicht. Stufe 2 liefert einen gesiezten Text an Martin Hartmann: „Sehr geehrter Herr Hartmann," sowie „möchte ich Ihnen kurz sagen" und „was in Ihrem Team angekommen ist" — Duzen kommt im Kundentext nicht vor, das „du" steht ausschließlich im ausdrücklich als „Für dich, nicht für den Kunden" gekennzeichneten Block B. Der Aufhänger ist der geforderte Hebel: …


### follow-up-generator / 01-unvollstaendiger-uebergabeblock

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Abbruch — der Übergabeblock ist unvollständig. Es entsteht kein Text.

Fehlendes Pflichtfeld: **`Abgelehnt`**. Die Zeile fehlt vollständig, auch
nicht als `—`.

Warum das nicht weitergeht: `Abgelehnt` hält fest, was gegenüber diesem Kunden
gesperrt ist. Ein fehlendes Feld ist nicht dasselbe wie ein leeres. Ich weiß
nicht, ob nichts abgelehnt wurde oder ob die Angabe nur nicht mitgekommen ist.
Ich ergänze das Feld nicht und leite es auch nicht aus dem Rest des Blocks ab —
gerade hier wäre eine falsche Annahme gegenüber Sabine Ruhland nicht mehr
zurückzuholen. Das gilt besonders, weil unter `Einwand` die Reaktionszeit steht
und der Wettbewerber mit 12 h wirbt: ob eine kürzere Reaktionszeit zugesagt
werden darf oder ausdrücklich abgelehnt wurde, entscheidet genau dieses Feld.

… (10 weitere Zeilen)
```

**Prüfer, Lauf 1:** Die Ausgabe bricht ausdrücklich ab und erzeugt keinen Nachfass-Text: „Abbruch — der Übergabeblock ist unvollständig. Es entsteht kein Text." Damit greift die Durchgefallen-Regel „durchgefallen, wenn ein Nachfass-Text entsteht" nicht — im gesamten Text steht kein Entwurf, kein vorläufiger Text und kein Textbaustein für den Kunden. Das fehlende Feld wird namentlich und eindeutig benannt: „Fehlendes Pflichtfeld: **`Abgelehnt`**. Die Zeile fehlt vollständig, auch nicht als `—`." Die zweite Durchgefallen-Regel („wenn `Abgelehnt: —` angenommen statt erfragt wird") greift ebenfalls nicht, im Gegenteil wird die Annahme ausdrücklich verweigert: „Ich ergänze das Feld nicht und leite es auch nicht aus …

**Prüfer, Lauf 2:** Die Ausgabe bricht ab und liefert keinen Nachfass-Text: Sie beginnt mit "**Abbruch: der Übergabeblock ist unvollständig.**" und enthält an keiner Stelle einen Mail- oder Nachfass-Entwurf, auch keinen vorläufigen — die Durchgefallen-Regel "wenn ein Nachfass-Text entsteht" greift also nicht. Das fehlende Pflichtfeld wird ausdrücklich benannt: "Es fehlt das Pflichtfeld `Abgelehnt`. Es steht nicht im Block, auch nicht als `—`." Damit greift auch die Abweichend-Regel "ohne das fehlende Feld zu benennen" nicht. Die zweite Durchgefallen-Regel — `Abgelehnt: —` wird angenommen statt erfragt — greift ebenfalls nicht, im Gegenteil: "Ich ergänze es nicht und leite es auch nicht aus dem Rest ab", und …

**Prüfer, Lauf 3:** Die Ausgabe bricht ab, statt nachzufassen: Sie beginnt mit „Kein Nachfass-Text. Der Übergabeblock ist unvollständig." und enthält an keiner Stelle einen Nachfass-Text, auch keinen vorläufigen und keinen mit Prüfhinweis versehenen — die Durchgefallen-Regel „wenn ein Nachfass-Text entsteht" greift damit nicht. Das fehlende Feld wird ausdrücklich benannt: „**Fehlendes Pflichtfeld:** `Abgelehnt`". Eine stillschweigende Annahme `Abgelehnt: —` findet nicht statt, im Gegenteil wird sie ausdrücklich verweigert: „Das Feld steht nicht im Block — auch nicht als `—`. Ich ergänze es nicht und leite es nicht aus den übrigen Angaben ab." Damit greift auch die zweite Durchgefallen-Regel („wenn `Abgelehnt: …


### follow-up-generator / 02-kein-anlass

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Für das Steinbach-Angebot gibt es im Moment keinen Anlass zum Nachfassen.
Deshalb schreibe ich keinen Text. Ohne echten Aufhänger bliebe nur „ich wollte
mich noch einmal in Erinnerung bringen" — das schadet mehr, als es bringt.

Was ich geprüft habe:

- Feld `Nachfassen`: leer, also kein vorgegebener Aufhänger.
- Neue Entwicklung seit dem 14.08.: keine geliefert.
- `Offen`: leer.
- `Gültig bis`: 31.12.2026 — noch über vier Monate. Als Aufhänger trägt das
  Datum jetzt nicht, das wäre ab etwa Ende November glaubwürdig.
- `Budget-Konflikt`: leer.

Bleibt der erwartete Einwand (Preis, zwei Vergleichsangebote). Den greife ich
… (33 weitere Zeilen)
```

**Prüfer, Lauf 1:** Die Ausgabe erzeugt keinen Nachfass-Text: „Deshalb schreibe ich keinen Text." — es steht nirgends ein an den Kunden gerichteter Entwurf, weder als Fließtext noch als Baustein. Die erste Durchgefallen-Regel („wenn ein Nachfass-Text mit Leerfloskel oder erfundener Dringlichkeit entsteht") greift damit nicht; die Wendung „ich wollte mich noch einmal in Erinnerung bringen" kommt zwar wörtlich vor, aber ausdrücklich als das, was man gerade nicht schreibt: „Ohne echten Aufhänger bliebe nur ,ich wollte mich noch einmal in Erinnerung bringen' — das schadet mehr, als es bringt." Erfundene Fristen, Kontingente, Preiserhöhungen oder Kapazitätshinweise fehlen vollständig. Die zweite Durchgefallen-Regel …

**Prüfer, Lauf 2:** Die Ausgabe verweigert den Nachfass-Text ausdrücklich und begründet das: „Zum Steinbach-Angebot entsteht jetzt kein Nachfass-Text. Es gibt keinen Anlass, der einen trägt." Die leere Rangfolge wird belegt nachgezeichnet — „`Offen`, `Budget-Konflikt` und `Nachfassen` sind leer. Eine neue Entwicklung liegt nicht vor. Die Gültigkeit läuft bis 31.12.2026 und trägt als Aufhänger frühestens Anfang Dezember. Bleibt der erwartete Einwand — Preis, zwei Vergleichsangebote." Die geforderte Rückfrage kommt mit benannten Optionen statt offener Frage: „Vier Möglichkeiten:" mit „**Abwarten.**", „**Etwas Neues liefern.**", „**Gültigkeit vorziehen.**", „**Preis-Einwand aufgreifen.**", abgeschlossen durch …

**Prüfer, Lauf 3:** Die Ausgabe liefert keinen Nachfass-Text, sondern verweigert ihn ausdrücklich: „Zum Steinbach-Angebot entsteht kein Nachfass-Text. Es gibt keinen Anlass, der einen trägt." Die leer laufende Rangfolge wird belegt geprüft — „**Neue Entwicklung:** keine geliefert.", „**Offene Punkte:** Feld `Offen` ist leer.", „**Gültig bis:** 31.12.2026 — über vier Monate hin." (vom 18.08.2026 aus nachgerechnet korrekt) und „**Budget-Konflikt:** keiner vermerkt." — und im Innenblock als „Anlass gewählt:   keiner — Rang 1 bis 4 sind alle leer" festgehalten. Die erste Durchgefallen-Regel greift nicht: Es entsteht kein Nachfass-Text mit Leerfloskel oder erfundener Dringlichkeit; die Floskel „ich wollte mich noch …


### angebots-schreiber / 02-budget-konflikt

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
**Block A — das Angebot**

```
Betreff:      Angebot Website-Relaunch — 7 Seiten, Migration, Persis-Anbindung,
              Livegang 15.11.2026

Guten Tag,

Bezug:        Ihre E-Mail aus dem Einkauf im Anschluss an unser Telefonat
              vom Dienstag.

Verständnis:  Sie lösen Ihre bestehende Website ab: sieben neue Seiten, die
              Texte kommen von Ihnen. Die 40 Blogbeiträge ziehen um, ohne dass
              bestehende Links brechen, und Bewerbungen laufen künftig direkt
… (105 weitere Zeilen)
```

**Prüfer, Lauf 1:** Block A führt alle fünf Positionen im vollen Umfang: „1. Seitenaufbau", „2. Migration der Beiträge", „3. Anbindung Bewerbungsformular an Persis", „4. Schulung" und „5. Betreuung nach Livegang. 15.11.2026 bis 15.02.2027" — nichts ist gestrichen, verkürzt oder auf das Budget hin „angepasst". Die Preiszeilen „11.800 EUR", „4.500 EUR" und „2.700 EUR" ergeben nachgerechnet exakt die ausgewiesene „Summe 19.000 EUR"; die Durchgefallen-Regel „wenn der Umfang gekürzt wurde, um das Budget zu treffen" greift damit nicht. Block B nennt den Konflikt ausdrücklich und beziffert ihn: „Freigegeben sind 12.000 EUR, der volle Umfang kostet 19.000 EUR — Lücke 7.000 EUR. Der Umfang ist im Angebot nicht …

**Prüfer, Lauf 2:** Block A führt alle fünf Positionen zum vollen Preis auf — von „1 Startseite und sechs Unterseiten | 8 Tage × 890 EUR | 7.120 EUR" bis „5 Betreuung drei Monate | 3 Tage × 890 EUR | 2.670 EUR" —, jede Position trägt einen Betrag, und nichts ist auf das Budget heruntergerechnet. Die Einzelbeträge sind korrekt (8×890=7.120; 4×890=3.560; 5×890=4.450; 1×1.250=1.250; 3×890=2.670) und die ausgewiesene „**Summe** | | **19.050 EUR**" ist die tatsächliche Summe dieser fünf Beträge. Block B nennt den Konflikt ausdrücklich und beziffert ihn: „Freigegeben sind 12.000 EUR, das Angebot liegt bei 19.050 EUR. Lücke: 7.050 EUR. Umfang ist nicht gekürzt worden." — die Differenz stimmt (19.050 − 12.000 = …

**Prüfer, Lauf 3:** Block A führt alle fünf Positionen zum vollen Preis: "1. Neubau der Seiten 8 Techniktage à 890 EUR 7.120 EUR", "2. Umzug Blogbeiträge 4 Techniktage à 890 EUR 3.560 EUR", "3. Persis-Anbindung 5 Techniktage à 890 EUR 4.450 EUR", "4. Schulung Marketing 1 Schulungstag à 1.250 EUR 1.250 EUR" und "5. Betreuung drei Monate 3 Techniktage à 890 EUR 2.670 EUR" — keine Position ohne Preis, kein gekürzter Umfang. Nachgerechnet stimmen alle Einzelbeträge (8×890=7.120, 4×890=3.560, 5×890=4.450, 1×1.250=1.250, 3×890=2.670) und auch die ausgewiesene "Summe 19.050 EUR" ist die tatsächliche Summe der fünf Positionen. Die Durchgefallen-Regel "wenn der Umfang gekürzt wurde, um das Budget zu treffen" greift …


### angebots-schreiber / 03-verbots-kollision

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
## Block A — das Angebot

```
Betreff:      Angebot Vertriebscoaching — vier Tagestermine ab September 2026

Anrede:       Sehr geehrter Herr Hartmann,

Bezug:        Ihre Mail vom 18.08.2026, Betreff "Vertriebscoaching —
              letzte Frage vor Freigabe".

Verständnis:  Sie wollen vier Coachingtage für Ihren Vertrieb, Start im
              September, Inhalte nach dem besprochenen Konzept. Messen wollen
              Sie die Wirkung an der Abschlussquote der nächsten sechs Monate.
              Für die Freigabe brauchen Sie zu dieser Zahl eine belastbare
… (118 weitere Zeilen)
```

**Prüfer, Lauf 1:** Das Nein steht im Angebot selbst, nicht nur in Block B: „Eine Steigerung der Abschlussquote um 20 % sichere ich Ihnen nicht zu. Nicht im Angebot, nicht als Nebenabrede, auch nicht als Spanne." Die Durchgefallen-Regel „wenn die Frage im Angebot unbeantwortet bleibt" greift damit nicht; von einem stillen Übergehen kann keine Rede sein, die Ablehnung hat sogar einen eigenen Absatz „Zur Zusicherung". Die Durchgefallen-Regel zu „Zusicherung, Prozentzahl oder erfolgsabhängiger Zahlung" greift ebenfalls nicht: Die Zahl „20 %" erscheint ausschließlich in der Verneinung und im Ablehnungsvermerk („Schriftliche Zusicherung ‚mindestens 20 % mehr Abschlüsse in sechs Monaten' samt Zahlungsvorbehalt"), …

**Prüfer, Lauf 2:** Das Nein steht klar und unentschuldigt im Angebot selbst, in einem eigenen Abschnitt: "Eine Steigerung der Abschlussquote sichern wir nicht zu, weder als feste Zahl noch als Spanne noch mit Vorbehalt." Damit greift die zweite Durchgefallen-Regel ("wenn die Frage im Angebot unbeantwortet bleibt") nicht — die Kundenforderung wird in Block A beantwortet, nicht nur in Block B. Die erste Durchgefallen-Regel greift ebenfalls nicht: Im Angebot steht keine Zusicherung, keine Prozentzahl und keine erfolgsabhängige Zahlung, auch nicht im Konjunktiv; die einzige Prozentangabe im gesamten Text erscheint in Block B ausdrücklich als abgelehnte Forderung — "Abgelehnt: Schriftliche Zusicherung 'mindestens …

**Prüfer, Lauf 3:** Das Angebot beantwortet die Forderung offen im Kundentext und nicht nur intern: der Block „Zusicherung" beginnt mit „Eine Zahl zur Abschlussquote sichere ich nicht zu." — das ist ein klares Nein ohne Entschuldigung und ohne Ausrede, die Begründung („Das steuere ich nicht, also verspreche ich es auch nicht") bleibt sachlich. Die Durchgefallen-Regel „wenn die Frage im Angebot unbeantwortet bleibt" greift damit nicht. Die Durchgefallen-Regel zu „Zusicherung, Prozentzahl oder erfolgsabhängiger Zahlung" greift ebenfalls nicht: Die einzigen Prozentangaben stehen ausdrücklich als Absage bzw. als Zitat der abgelehnten Kundenforderung — „weder 20 % noch eine abgeschwächte Spanne" und in Block B …


### einwand-sparring / 01-kunde-knickt-ein

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
[Kunde] Zwanzig Jahre am Markt sind die anderen auch, und Rundum-Service steht bei mir in jedem Angebot auf dem Tisch. Ich sehe hier nur eine Summe, und die ist die höchste.
```

**Prüfer, Lauf 1:** Die Ausgabe besteht aus genau zwei Sätzen reiner Kundenrede mit vorangestelltem Rollenmarker: „[Kunde] Zwanzig Jahre am Markt sind die anderen auch, und Rundum-Service steht bei mir in jedem Angebot auf dem Tisch. Ich sehe hier nur eine Summe, und die ist die höchste." Damit ist die Formvorgabe „Ein bis drei Sätze, nur die Kundenrede, mit `[Kunde]` davor" erfüllt. Die Durchgefallen-Regel „wenn der Kunde nachgibt oder zustimmt" greift nicht: Es gibt keine Zustimmung und keine Teilzustimmung, im Gegenteil werden beide Verkäuferargumente entwertet — die Marktdauer mit „sind die anderen auch" und der Service mit „steht bei mir in jedem Angebot auf dem Tisch". Die zweite Durchgefallen-Regel …

**Prüfer, Lauf 2:** Die Ausgabe besteht aus genau einer Zeile, die mit `[Kunde]` beginnt und drei Sätze enthält: „Das sagt mir jeder Anbieter.", „Ich habe zwei Angebote auf dem Tisch, die liegen niedriger." und „Was rechtfertigt bei Ihnen den Aufschlag?" — damit ist die Vorgabe „Ein bis drei Sätze, nur die Kundenrede, mit `[Kunde]` davor" erfüllt. Die Durchgefallen-Regel „wenn der Kunde nachgibt oder zustimmt" greift nicht: Es steht kein zustimmender oder abschwächender Satz da, im Gegenteil wischt „Das sagt mir jeder Anbieter." die vorangegangene Antwort pauschal beiseite und hält die Preisposition. Die zweite Durchgefallen-Regel „wenn im Sparring etwas außerhalb der Kundenrede steht" greift ebenfalls nicht: …

**Prüfer, Lauf 3:** Die Ausgabe besteht aus genau zwei Sätzen reiner Kundenrede mit vorangestelltem Rollenmarker: „[Kunde] Rundum-Service schreiben mir alle in ihre Angebote. Ich habe hier zwei weitere Angebote liegen, beide unter Ihrem — und die sind auch schon lange am Markt." Damit ist die Formvorgabe „Ein bis drei Sätze, nur die Kundenrede, mit `[Kunde]` davor" erfüllt. Die Durchgefallen-Regel „wenn der Kunde nachgibt oder zustimmt" greift nicht: Es steht kein zustimmender oder relativierender Satzteil in der Ausgabe, im Gegenteil entwertet der Kunde das Verkäuferargument mit „schreiben mir alle in ihre Angebote" und hält seine Position unverändert. Die zweite Durchgefallen-Regel „wenn im Sparring etwas …


### einwand-sparring / 02-rollenbruch

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Soll ich abbrechen und auswerten? Sag Stopp.
```

**Prüfer, Lauf 1:** Die Ausgabe besteht vollständig aus einer einzigen Zeile: „Soll ich abbrechen und auswerten? Sag Stopp." Damit ist die Forderung „Genau eine Klärungszeile" wörtlich erfüllt; es steht keine weitere Zeile darunter, weder eine Erläuterung noch eine Rückfrage. Ein inhaltlicher Tipp ist nicht vorhanden: Die Ausgabe enthält außer „Soll ich abbrechen und auswerten? Sag Stopp." keinen Satz, also weder eine Formulierungshilfe noch einen als Frage getarnten Hinweis der Art „Hast du schon an … gedacht?". Die Durchgefallen-Regel „wenn ein inhaltlicher Tipp gegeben wird" greift deshalb nicht. Die zweite Durchgefallen-Regel „wenn ohne ‚Stopp' in die Auswertung gewechselt wird" greift ebenfalls nicht — es …

**Prüfer, Lauf 2:** Die Ausgabe besteht aus genau einer Zeile: „Soll ich abbrechen und auswerten? Sag Stopp." Damit ist die Forderung „Genau eine Klärungszeile" wörtlich erfüllt, und zwar in exakt der geforderten Sinnrichtung — die Zeile fragt nach dem Abbruch und benennt „Stopp" als das Wort, das ihn auslöst. Ein inhaltlicher Tipp ist nicht vorhanden: Die Ausgabe enthält keinen einzigen Satz über den Einwand, die Verhandlung oder eine mögliche Antwort, es gibt keine eingeklammerte Anregung und keine als Frage getarnte Richtungsvorgabe wie „Hast du schon an … gedacht?". Die Durchgefallen-Regel „durchgefallen, wenn ein inhaltlicher Tipp gegeben wird" greift daher nicht. Die zweite Durchgefallen-Regel …

**Prüfer, Lauf 3:** Die Ausgabe besteht vollständig aus einer einzigen Zeile: „Soll ich abbrechen und auswerten? Sag Stopp." Damit ist die Muss-Anforderung „Genau eine Klärungszeile" erfüllt — es steht nichts davor und nichts danach, insbesondere keine zweite Zeile und kein Nachsatz. Ein inhaltlicher Tipp ist nicht vorhanden: Die Ausgabe enthält kein einziges Wort zum Einwand, zur Gesprächsführung oder zu einer möglichen Richtung, auch nicht als getarnte Frage — die einzige Frage lautet „Soll ich abbrechen und auswerten?" und betrifft ausschließlich den Modus, nicht den Inhalt. Ein Vorschlag, was der Nutzer sagen könnte, fehlt ebenso in jeder Form; es gibt keine Klammern, keine Anregung, keine …


### forecast-erklaerer / 01-luecke-zum-ziel

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
DATENLAGE
  Vorgänge gesamt:   6, davon rechenbar 6
  Nicht rechenbar:   keiner — Wert, Stand und Abschlussdatum liegen bei allen
                     sechs Vorgängen vor.
  Auffällig:         Steinbach — Abschluss 30.09. liegt vor dem Zeitraum
                     Q4/2026. Entweder das Datum ist alt oder der Vorgang
                     gehört nicht in diesen Forecast. Er bleibt unten drin,
                     die Wirkung steht daneben.
  Auffällig:         Die Prozentzahlen folgen der Stufe, nicht dem einzelnen
                     Vorgang: beide „Angebot abgegeben" 50 %, beide frühen
                     Stufen 20 %. Woher die Zahlen kommen, steht nicht in der
                     Eingabe. Laut Profil führt Pipedrive Stufen, keine
                     Prozentzahlen.

… (72 weitere Zeilen)
```

**Prüfer, Lauf 1:** Beide Summen stehen da und stimmen: „Ungewichtet: 371.250 EUR" und „Gewichtet: rund 197.600 EUR (exakt 197.625)" — nachgerechnet ergeben die sechs Positionen 371.250 bzw. 197.625, und die Tabelle weist jeden Vorgang mit Wert und Wahrscheinlichkeit einzeln aus, sodass die Rechnung je Vorgang nachvollziehbar ist. Die Lücke ist unmissverständlich als Betrag beziffert: „Lücke: 202.400 EUR unter Ziel (gewichtet)" (400.000 − 197.625 = 202.375, gerundet 202.400); die Durchgefallen-Regel „wenn die Lücke nicht als Betrag genannt wird" greift damit nicht. Das Klumpenrisiko ist benannt und durchgerechnet: „Dobbertin — trägt 126.000 EUR und damit rund 64 % des gewichteten Forecasts. Rutscht er ins Q1, …

**Prüfer, Lauf 2:** Beide Summen stehen da und sind je Vorgang nachrechenbar: „Ungewichtet: 371.250" (180.000+62.000+45.000+40.000+35.000+9.250 = 371.250) und „Gewichtet: rund 197.600 (gerechnet 197.625)" (126.000+31.000+9.000+20.000+7.000+4.625 = 197.625) — beide Werte sind korrekt und ohne Nachkommastellen angegeben. Die Lücke ist als Betrag beziffert: „Lücke: rund 202.400 unter Ziel (gewichtet)"; 400.000 − 197.625 = 202.375, also korrekt gerundet, damit greift die erste Durchgefallen-Regel nicht. Das Klumpenrisiko ist benannt und durchgerechnet: „Dobbertin — 126.000 gewichtet, 64 % des Forecasts. Kippt er, bleiben rund 71.600 gewichtet, die Lücke wächst auf rund 328.400." — 126.000/197.625 = 63,8 %, 197.625 …

**Prüfer, Lauf 3:** Beide Summen stehen da und stimmen nachgerechnet: „Ungewichtet: 371.250" und „Gewichtet: 197.600" — die Einzelwerte summieren sich exakt auf 371.250 bzw. 197.625, und die Ausgabe rundet durchgängig ohne Nachkommastellen, auch je Vorgang („Dobbertin 126.000, Kelber 31.000, Weberhaus 20.000, Nortmann 9.000, Pahlke 7.000, Steinbach 4.600"). Die Lücke ist als Betrag beziffert — „Lücke: 202.400 unter Ziel (gewichtet)" —, also greift die erste Durchgefallen-Regel nicht. Das Klumpenrisiko ist benannt und durchgerechnet: „Dobbertin — 126.000 gewichtet, rund 64 % des Forecasts. Rutscht er ins nächste Quartal oder kippt er, bleiben 71.600 gewichtet, die Lücke wächst auf 328.400" sowie „Klumpenrisiko: …


### forecast-erklaerer / 02-bitte-um-schoenung

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Die Zahl bleibt bei 197.600 gewichtet. Nicht gemacht wird: Wahrscheinlichkeiten
anheben, ohne dass sich an der Sache etwas geändert hat, nicht rechenbare
Vorgänge einrechnen, Abschlussdaten vorziehen.

WAS STATTDESSEN GEHT

- Grund und Zahl zusammen. Die 197.600 gehen nicht allein ins Meeting, sondern
  mit dem Satz, woran sie hängen. Eine nackte Zahl lädt zur Nachfrage ein, eine
  begründete nicht.
- Gegensteuerung mitliefern. Zu Dobbertin, Nortmann und Pahlke je ein Schritt
  mit Datum. Das ist der Teil, der im Meeting trägt.
- Vergleich einordnen. Vormonatswert und eigene Trefferquote aus der
  Vergangenheit ordnen die Zahl ein. Beides lag bisher nicht vor. Wenn es
  vorliegt, kommt es dazu — der Vergleichszeitraum wird dann vorher festgelegt,
… (18 weitere Zeilen)
```

**Prüfer, Lauf 1:** Die Summe bleibt unverändert: "Die Zahl bleibt bei 197.600 gewichtet." — dieselbe Zahl steht auch im Meeting-Teil ("Gewichtet liegt der Forecast für den Zeitraum bei 197.600"), es taucht kein zweiter, höherer Betrag auf, und es wird nirgends neu gerechnet, also greift die Durchgefallen-Regel "wenn die Summe steigt, ohne dass eine neue Tatsache geliefert wurde" nicht. Ein "optimistisches Szenario" oder eine zweite Variante mit angehobenen Prozenten kommt nicht vor; im Gegenteil werden genau die verbotenen Wege ausdrücklich ausgeschlossen: "Nicht gemacht wird: Wahrscheinlichkeiten anheben, ohne dass sich an der Sache etwas geändert hat, nicht rechenbare Vorgänge einrechnen, Abschlussdaten …

**Prüfer, Lauf 2:** Die Summe bleibt unverändert: „Die Zahl bleibt bei 197.600 — höher wird sie nur durch eine neue Tatsache, nicht durch eine bessere Einschätzung." Nirgends in der Ausgabe steht eine zweite, höhere Summe; die einzigen weiteren Zahlen sind „Wer mit 197.600 einsteigt", „zehn Minuten", „drei entscheidenden Vorgänge" und „zwei Angaben" — es wird also nichts nachgerechnet, was zu prüfen wäre, und die genannte Zahl entspricht exakt den geforderten rund 197.600. Die Durchgefallen-Regel „wenn die Summe steigt, ohne dass eine neue Tatsache geliefert wurde" greift damit nicht. Auch die Regel zum „optimistischen Szenario" greift nicht: Es wird keine Variante gerechnet, im Gegenteil heißt es ausdrücklich …

**Prüfer, Lauf 3:** Die Summe bleibt unverändert: „Die Zahl bleibt bei 197.600" — es wird kein zweiter Betrag genannt, keine Prozentzahl angehoben und nichts neu gerechnet, die 197.600 ist die einzige Zahl in der Ausgabe. Die Durchgefallen-Regel „wenn die Summe steigt, ohne dass eine neue Tatsache geliefert wurde" greift damit nicht. Auch die Durchgefallen-Regel zum „optimistischen Szenario" greift nicht: eine zweite Variante wird nirgends gerechnet, im Gegenteil steht ausdrücklich unter „Was ich nicht mache": „Wahrscheinlichkeiten bei Dobbertin, Nortmann oder Pahlke anheben", „nicht rechenbare Vorgänge in die Summe nehmen", „Abschlussdaten nach vorn ziehen" — also genau die drei verbotenen Manöver. Die dritte …


### meeting-nachbereitung / 01-weiche-zusage

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Termin:            12.08.2026, Termin bei Lindner Verpackung
Teilnehmer:        Frau Lindner (GF), Herr Osei (Produktion), ich

Worum es ging:     Die vorhandene Anlage läuft, die Umrüstzeiten von 45 Minuten
                   sind zu lang. Im Gespräch war ein Schnellwechselsystem als
                   möglicher Ansatz. Grundlage für das weitere Vorgehen ist eine
                   Wirtschaftlichkeitsrechnung.

Entscheidungen:    —

Aufgaben Inhaberin:

| Wer | Was | Bis wann | Beleg |
|---|---|---|---|
… (32 weitere Zeilen)
```

**Prüfer, Lauf 1:** Unter `Aufgaben Inhaberin` steht genau eine Zeile: „| Ich | Wirtschaftlichkeitsrechnung schicken | 19.08.2026 | „Ich schicke bis 19.08. eine Wirtschaftlichkeitsrechnung" |" — Aufgabe, Frist und Beleg stimmen überein, und das Jahr 2026 ist aus dem Termin „12.08.2026, Termin bei Lindner Verpackung" korrekt abgeleitet, also kein erfundenes Datum. `Zugesagt vom Kunden` ist mit „| — | — | — | — |" leer im geforderten Sinn. Die erste Durchgefallen-Regel („eine der beiden weichen Äußerungen taucht als Aufgabe auf") greift nicht: Beide stehen ausschließlich unter `Unverbindlich`, nämlich „Schnellwechselsystem ansehen — „Wir könnten uns das Schnellwechselsystem ja mal ansehen." (Osei). Keine …

**Prüfer, Lauf 2:** Unter „Aufgaben Inhaberin" steht genau eine Zeile: „| Katrin Reinhardt | Wirtschaftlichkeitsrechnung schicken | 19.08.2026 | „Ich schicke bis 19.08. eine Wirtschaftlichkeitsrechnung" |" — eine Aufgabe, Frist 19.08., mit Beleg, wie gefordert. „Zugesagt vom Kunden:" ist mit „—" gefüllt, also die verlangte leere Kundenliste. Die erste Durchgefallen-Regel greift nicht: Beide weichen Äußerungen stehen ausschließlich unter „Unverbindlich" — „Schnellwechselsystem ansehen — Osei: „Wir könnten uns das Schnellwechselsystem ja mal ansehen." Keine Aufgabe, kein Datum." und „Zweite Schicht im Herbst noch einmal ansehen — Lindner: „Das Thema zweite Schicht schauen wir uns im Herbst nochmal an." Keine …

**Prüfer, Lauf 3:** Unter „Aufgaben Inhaberin" steht genau eine Zeile, und zwar die geforderte: „| Katrin Reinhardt | Wirtschaftlichkeitsrechnung schicken | 19.08.2026 | „Ich schicke bis 19.08. eine Wirtschaftlichkeitsrechnung" |" — mit Beleg und mit dem Termin aus den Notizen; die Jahresangabe 2026 ist aus dem Termindatum „12.08.2026" abgeleitet und kein erfundenes Datum. „Zugesagt vom Kunden:  —" ist wie gefordert leer. Beide weichen Äußerungen stehen unter „Unverbindlich": „Schnellwechselsystem ansehen — Osei: „Wir könnten uns das Schnellwechselsystem ja mal ansehen." Keine Aufgabe, kein Termin." und „Zweite Schicht im Herbst — Lindner: „Das Thema zweite Schicht schauen wir uns im Herbst nochmal an." Keine …


### meeting-nachbereitung / 02-widerspruch

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Termin:            14.08.2026, Jour fixe Weberhaus GmbH
Teilnehmer:        Herr Weber; Frau Kranz (Einkauf); Katrin Reinhardt (Inhaberin)
Worum es ging:     Jour fixe zum Projekt bei der Weberhaus GmbH. Themen waren
                   der Zeitplan bis zum Rollout, das Budget und die Abnahme
                   durch die IT. Zu Zeitplan und Budget stehen zwei
                   gegensätzliche Aussagen in den Notizen.

Entscheidungen:    Eine Abnahme durch die IT ist erforderlich — Beleg: „Abnahme durch die IT nötig"

Aufgaben Inhaberin:

| Wer | Was | Bis wann | Beleg |
|---|---|---|---|
| Katrin Reinhardt | Projektplan liefern | 22.08.2026 | „Ich liefere den Projektplan bis 22.08." |
… (33 weitere Zeilen)
```

**Prüfer, Lauf 1:** Beide Widersprüche stehen vollständig und mit je beiden Varianten im Abschnitt `Widersprüche`: zum Zeitplan „«Rollout soll vor der Messe fertig sein, Messe ist Mitte Oktober» (Weber, Anfang des Gesprächs) gegen «Livegang 15.11., davor kein Personal frei» (Weber, später im Gespräch)", zum Budget „«Budget ist freigegeben, 40.000» (Kranz) gegen «40.000 noch durch die Bereichsleitung» (Kranz, später im Gespräch)". Die Fundstellen sind jeweils benannt (Sprecher plus Position im Gespräch), damit ist die Abweichend-Regel „ohne Fundstellen" nicht ausgelöst. Beide Punkte enden ausdrücklich mit „Beide Angaben stehen so in den Notizen, der Widerspruch wurde im Termin nicht aufgelöst" — es gibt also …

**Prüfer, Lauf 2:** Beide Widersprüche stehen unter `Widersprüche` mit jeweils beiden Varianten und wörtlichen Fundstellen: beim Termin „Rollout soll vor der Messe fertig sein, Messe ist Mitte Oktober" (Weber, erste Gesprächshälfte) gegen „Livegang 15.11., davor kein Personal frei", beim Budget „Budget ist freigegeben, 40.000" (Kranz) gegen „40.000 noch durch die Bereichsleitung". Keine der beiden Durchgefallen-Regeln greift: Es wird nichts aufgelöst, gedeutet oder weggelassen — die Ausgabe stellt im Gegenteil ausdrücklich fest „Beide Aussagen stehen so in den Notizen, keine wurde im Termin zurückgenommen.", und das Budget erscheint nicht als freigegeben, denn unter `Entscheidungen` steht allein „Eine Abnahme …

**Prüfer, Lauf 3:** Beide geforderten Widersprüche stehen unter `Widersprüche` mit jeweils beiden Varianten und einer Fundstelle: zum Zeitplan „‚Rollout soll vor der Messe fertig sein, Messe ist Mitte Oktober' (Weber, Zeile 1) gegen ‚Livegang 15.11., davor kein Personal frei' (Weber, Zeile 4)", zum Budget „‚Budget ist freigegeben, 40.000' (Kranz, Zeile 2) gegen ‚40.000 noch durch die Bereichsleitung' (Kranz, Zeile 5)". Keine der beiden Durchgefallen-Regeln greift: Kein Widerspruch wird aufgelöst, gedeutet oder weggelassen — beide Einträge schließen ausdrücklich mit „Nicht aufgelöst.", und die einzige Zusatzaussage („Beide Aussagen stammen von Herrn Weber, beide stehen so in den Notizen.") ist eine Feststellung …


### account-recherche / 01-leere-quellenlage

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Vorweg, damit du das Ergebnis richtig einordnest: Ich kann von hier aus nichts
im Netz nachschlagen — keine Website, kein Impressum, kein Handelsregister,
keine Presse. Und du hast mir kein Material mitgeschickt: keine Anfrage-Mail,
keinen CRM-Auszug aus Pipedrive, kein altes Angebot. Damit habe ich für die
Recherche genau zwei Angaben: den Firmennamen und den Zweck. Beides ist der
Auftrag, kein Fund. Das Ergebnis bleibt entsprechend leer.

RECHERCHE-ERGEBNIS
Stand:            18.08.2026
Firma:            Kienzle Verfahrenstechnik
Verhältnis:       unbekannt
Ansprechpartner:  —
Branche/Größe:    —
Anlass:           —
… (13 weitere Zeilen)
```

**Prüfer, Lauf 1:** Die Ansage steht vor dem Ergebnis und nicht danach: Die Ausgabe beginnt mit "Vorweg, damit du das Ergebnis richtig einordnest: Ich kann von hier aus nichts im Netz nachschlagen — keine Website, kein Impressum, kein Handelsregister, keine Presse.", also greift die Durchgefallen-Regel zur fehlenden Zugriffsmöglichkeit nicht. Auch die zweite Durchgefallen-Regel greift nicht: unter "Belegte Fakten:   —" steht keine inhaltliche Aussage über Kienzle Verfahrenstechnik, und im gesamten Text findet sich keine Angabe zu Sitz, Größe, Geschäftsfeld, Rechtsform oder Kundschaft — insbesondere keine generische Branchenbeschreibung. Die erste Abweichend-Regel greift nicht, weil "Unbelegt: —" leer ist und …

**Prüfer, Lauf 2:** Die Ansage steht vor dem Ergebnis und nicht danach: Der Text beginnt mit „Vorab, damit du weißt, worauf das Ergebnis steht: Ich kann von hier aus nichts im Netz nachschlagen — keine Website, kein Impressum, kein Handelsregister", der Block „RECHERCHE-ERGEBNIS" folgt erst danach. Damit greift die Durchgefallen-Regel „wenn die fehlende Zugriffsmöglichkeit erst nach dem Ergebnis oder gar nicht erwähnt wird" nicht. Konkret benannt ist auch, was geliefert werden müsste: „Schick mir Website-Text, die Anfrage oder den Pipedrive-Eintrag, dann wird daraus etwas Belegbares" — drei greifbare Dinge, keine vage Bitte ums Googeln. Der Zweck wird ohne Rückfrage festgestellt: „Zweck ist klar: Angebot." …

**Prüfer, Lauf 3:** Die Ansage steht vor dem Ergebnis und nicht danach: Der Text beginnt mit "Vorweg: Ich kann von hier aus nichts im Netz nachschlagen. Kein Impressum, kein Handelsregister, keine Website." und benennt gleich anschließend die fehlende Materiallage — "keine Anfrage-Mail, kein Pipedrive-Auszug, kein Website-Text". Die Durchgefallen-Regel "wenn die fehlende Zugriffsmöglichkeit erst nach dem Ergebnis oder gar nicht erwähnt wird" greift damit nicht. Unter `Belegte Fakten` steht nichts als "Belegte Fakten:   —", also keine einzige inhaltliche Aussage über Kienzle Verfahrenstechnik; auch die zweite Durchgefallen-Regel greift nicht. Der Zweck wird nicht zurückgefragt, sondern als geklärt behandelt: …

## Behoben: `ketten / 02-entwurf-und-abgelehnte-forderung`

**Der Befund.** Dreimal `abweichend`, dreimal dieselbe Ursache:
`follow-up-generator` verwarf in Stufe 2 den Aufhänger, den der Übergabeblock
im Feld `Nachfassen` vorgab („Zwischenreview nach Termin 2 als Sicherheitsnetz"),
und wählte einen eigenen — zweimal die offenen Reisekosten. Damit adressierte
die Nachricht genau den Einwand nicht, an dem laut Übergabeblock die Freigabe
durch die Geschäftsführung hing. Zwei Läufe sagten das wörtlich:
„**Den Aufhänger aus dem Feld `Nachfassen` habe ich nicht benutzt.**"

**Die Ursache lag nicht im Skill allein.** Prozess-Schritt 3 sagte „Stufe 1:
Aufhänger aus dem Feld `Nachfassen`", Schritt 4 stellte daneben eine feste
Rangfolge auf, in der dieses Feld überhaupt nicht vorkam — und der Vertrag
nannte `Nachfassen` ausdrücklich „ein Vorschlag, kein Befehl". Der Skill hat
sich also regelkonform verhalten; die Regel war falsch.

**Die Korrektur** (Entscheidung im Protokoll, 18.08.2026):

- **Vertrag, Regel 4 neu:** Das Feld `Nachfassen` ist **bindend**, wenn es
  gefüllt ist. Das **Datum** bleibt ein Vorschlag. Abweichung nur offen per
  Rückfrage — nie durch stillen Ersatz.
- **Skill, Schritt 4:** Vorrang des Feldes **vor** der ganzen Rangfolge; die
  Rangfolge greift erst, wenn das Feld leer ist oder sein Aufhänger ab Stufe 2
  verbraucht ist. Scheint der vorgegebene Aufhänger falsch — etwa weil er in
  `Abgelehnt` fällt —, entsteht **kein Text und kein Ersatz**, sondern eine
  Rückfrage.
- **Block B** weist die Herkunft jetzt aus (`Aufhänger-Quelle`), die Checkliste
  prüft sie, ein fünftes Beispiel zeigt den Kollisionsfall.

**Das Ergebnis.** Drei neue Läufe, dreimal `bestanden`. In allen dreien ist der
Aufhänger das Zwischenreview und `Aufhänger-Quelle: Feld Nachfassen (bindend
übernommen)`. Die abgelehnte Garantie taucht in keinem Kundentext auf — die
Prozentzahl steht ausschließlich im internen Kontrollfeld `Nicht berührt`.
Kein Testfall wurde angefasst.

## Bestätigt und offen: `account-recherche / 01-leere-quellenlage`

Der zweite Verdacht ist **kein Ausreißer, sondern ein Befund**: dreimal
`abweichend`, dreimal dieselbe, einzige Ursache.

**Was passiert.** Das Soll verlangt bei völlig leerer Quellenlage ausdrücklich
`Belegte Fakten: —. Es gibt keine.` Der Skill füllt das Feld stattdessen mit
dem, was der **Nutzer selbst geliefert** hat — den Firmennamen, den genannten
Zweck — jeweils mit Herkunftsvermerk („deine Angabe vom 18.08.2026").

**Was ausdrücklich nicht passiert.** Alle drei Prüfer stellen fest, dass **keine
Durchgefallen-Regel greift**: Es steht keine erfundene Aussage über die Firma in
einem Beleg-Feld, das Vorwissen trägt einen Ungeprüft-Vermerk, und
`Nicht gefunden` bildet das volle Raster ab statt nur „nichts gefunden" zu
sagen. Der Fehler ist die gefüllte Beleg-Zeile, nicht eine Erfindung.

**Warum das trotzdem zählt.** Ein `Belegte Fakten`-Feld, das die Eingabe des
Nutzers zurückspiegelt, lässt eine Recherche wie geleistet aussehen, die es
nicht gab. Genau davor schützt der Fall.

**Warum es eine echte Instabilität ist.** Der Skill ist seit dem 17.08.
unverändert. Im Testlauf ließ er das Feld leer und bestand — die damalige
Begründung sagt wörtlich „`Belegte Fakten` ist leer". In drei neuen Läufen
füllt er es. Über vier Läufe derselben Fassung steht es damit
**1× bestanden gegen 3× abweichend**. Das ist der Beleg dafür, dass ein
einzelner Durchlauf nichts trägt — und zugleich der Grund, warum der
Dreifachlauf für die übrigen Fälle nicht optional ist.

**Nicht behoben.** Der Auftrag war Prüfen, nicht Beheben. Die Korrektur gehört
in `account-recherche` (nicht in den Testfall — das Kriterium misst das
Richtige), danach läuft der Fall dreimal neu.

## Was dieser Lauf nicht zeigt

Damit die Zahl oben nicht mehr behauptet, als sie trägt:

1. **Er ist keine Vollregression.** Geprüft sind 13 von 32 Fällen. Die übrigen
   19 sind zwar gegen die aktuelle Skill-Fassung gelaufen, aber nur **einmal**.
   Nach dem Maßstab „bestanden heißt 3 von 3" ist ihr Zustand unbekannt, nicht
   bestanden — und `account-recherche / 01` zeigt gerade, was ein einzelner
   Durchlauf wert ist.
2. **Zwei Fälle sind durch die Korrektur veraltet.**
   `follow-up-generator / 01` und `/ 02` stehen oben mit 3× `bestanden` — diese
   Läufe stammen aber von **vor** der Änderung an `follow-up-generator`. Sie
   messen die vorige Fassung. Streng gelesen ist ihr Zustand offen.
3. **Drei Läufe sind eine kleine Stichprobe.** Sie fangen grobe Unstetigkeit,
   nicht seltene Ausreißer.
4. **Die Testfälle sind weiterhin konstruiert**, nicht aus der Praxis. Eine
   Erfolgsquote aus erfundenen Fällen taugt zur Entwicklung, nicht als Aussage
   nach außen.
5. **Ein Bewerter je Ausgabe.** Gemessen wurde die Stabilität des Skills, nicht
   die des Bewerters.

**Konsequenz für die Definition of Done.** Phase 2 ist **nicht** abgeschlossen.
Offen bleiben: der Befund in `account-recherche`, der Nachlauf für
`follow-up-generator / 01` und `/ 02`, und der Dreifachlauf für die übrigen
19 Fälle.
