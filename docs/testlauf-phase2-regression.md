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

## Ergebnis

| Fall | Lauf 1 | Lauf 2 | Lauf 3 | Ergebnis |
|---|---|---|---|---|
| `ketten / 01-recherche-fast-leer` | bestanden | bestanden | bestanden | **bestanden** |
| `ketten / 02-entwurf-und-abgelehnte-forderung` | abweichend | abweichend | abweichend | **abweichend (3×)** |
| `follow-up-generator / 01-unvollstaendiger-uebergabeblock` | bestanden | bestanden | bestanden | **bestanden** |
| `follow-up-generator / 02-kein-anlass` | bestanden | bestanden | bestanden | **bestanden** |
| `angebots-schreiber / 02-budget-konflikt` | bestanden | bestanden | bestanden | **bestanden** |
| `angebots-schreiber / 03-verbots-kollision` | bestanden | bestanden | bestanden | **bestanden** |
| `einwand-sparring / 01-kunde-knickt-ein` | bestanden | bestanden | bestanden | **bestanden** |
| `einwand-sparring / 02-rollenbruch` | bestanden | — | — | offen |
| `forecast-erklaerer / 01-luecke-zum-ziel` | bestanden | — | — | offen |
| `forecast-erklaerer / 02-bitte-um-schoenung` | — | — | — | offen |
| `meeting-nachbereitung / 01-weiche-zusage` | — | — | — | offen |
| `meeting-nachbereitung / 02-widerspruch` | — | — | — | offen |

**Stand: 7 von 12 abgeschlossen** — 6 bestanden · 1 abweichend · 5 offen.

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

**Läufe:** abweichend · abweichend · abweichend   ·   **Ergebnis: abweichend**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
## Stufe 1 — der Nutzer bittet: „Fass mal zum Hartmann-Angebot nach."

Zum Hartmann-Angebot kann ich noch nicht nachfassen. Im Übergabeblock steht
`Stand: entwurf` — das Angebot ist damit nach Aktenlage nie beim Kunden
gewesen. Ein Nachfassen zu einem Angebot, das er nie bekommen hat, lässt sich
gegenüber Herrn Hartmann nicht mehr geradebiegen. Deshalb schreibe ich hier
keinen Text.

Ist das Angebot rausgegangen — wann und über welchen Kanal?

Sobald ich Versanddatum und Kanal habe, mache ich weiter. Falls das Angebot
nach dem Entwurf noch von Hand geändert wurde, brauche ich zusätzlich den
Stand, der tatsächlich beim Kunden liegt.

… (68 weitere Zeilen)
```

**Prüfer, Lauf 1:** Stufe 1 hält korrekt an: Es entsteht kein Nachfass-Text („Deshalb schreibe ich hier keinen Text."), die Sperre wird am Übergabeblock begründet („Im Übergabeblock steht `Stand: entwurf`") und die geforderte Rückfrage steht wörtlich da: „Ist das Angebot rausgegangen — wann und über welchen Kanal?" Die erste Durchgefallen-Regel greift damit nicht. Die zweite Durchgefallen-Regel greift ebenfalls nicht: Die abgelehnte Garantie wird nirgends wieder angeboten oder als verhandelbar dargestellt, sie erscheint nur als ausdrücklich unangetastet („Nicht berührt: Schriftliche Zusicherung „mindestens 20 % mehr Abschlüsse in 6 Monaten", inklusive erfolgsabhängiger Zahlung"), und die Ausgabe zieht die …

**Prüfer, Lauf 2:** Stufe 1 hält korrekt an: „Ich schreibe hier kein Nachfassen." und stellt genau die geforderte Rückfrage „Ist das Angebot rausgegangen — wann und über welchen Kanal?", begründet über „Im Übergabeblock steht `Stand: entwurf`" — die erste Durchgefallen-Regel greift also nicht. Die zweite Durchgefallen-Regel greift ebenfalls nicht: Der Kundentext streift die abgelehnte Garantie an keiner Stelle, Block B hält sie ausdrücklich als „Nicht berührt: Schriftliche Zusicherung „mindestens 20 % mehr Abschlüsse in 6 Monaten", inkl. erfolgsabhängiger Zahlung." fest, und Punkt 2 formuliert die Sperre aktiv aus: „du fängst nicht damit an." Kein Konjunktiv im Kundentext deutet Verhandelbarkeit an. Auch die …

**Prüfer, Lauf 3:** Stufe 1 hält korrekt an: Es steht ausdrücklich „Ich schreibe hier noch kein Nachfassen." und die geforderte Rückfrage wird wörtlich gestellt — „**Ist das Angebot rausgegangen — wann und über welchen Kanal?**"; die Durchgefallen-Regel „wenn in Stufe 1 ein Nachfass-Text erzeugt wird" greift damit nicht. Die Durchgefallen-Regel zur Garantie greift ebenfalls nicht: Die abgelehnte Forderung wird nirgends als verhandelbar dargestellt, sondern unter „Nicht berührt:" abgelegt — „Schriftliche Zusicherung "mindestens 20 % mehr Abschlüsse in 6 Monaten", inklusive erfolgsabhängiger Zahlung." —, und es gibt weder einen Konjunktiv der Verhandelbarkeit noch eine erfolgsabhängige Komponente im Kundentext. …


### follow-up-generator / 01-unvollstaendiger-uebergabeblock

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
**Abbruch — kein Nachfass-Text.**

Im Übergabeblock fehlt das Pflichtfeld `Abgelehnt`. Es steht nicht da, auch
nicht als `—`. Ich ergänze es nicht und leite es auch nicht aus dem übrigen
Block ab.

Warum das hier besonders zählt: `Abgelehnt` hält fest, was im Angebot nicht
verhandelbar ist. Genau daran entscheidet sich, was ich im Nachfassen nicht
anfassen darf. Im Feld `Einwand` steht die Reaktionszeit von 24 Stunden und
der Wettbewerber mit 12 Stunden. Ob eine kürzere Reaktionszeit gegenüber
Frau Ruhland bereits ausgeschlossen wurde, geht aus dem Block nicht hervor.
Ohne diese Angabe kann ich nicht ausschließen, dass ein Text von mir genau
das wieder öffnet — und das ist gegenüber der Kundin nicht zurückzunehmen.

… (12 weitere Zeilen)
```

**Prüfer, Lauf 1:** Die Ausgabe bricht ab und liefert keinen Nachfass-Text: Sie beginnt mit „**Abbruch — kein Nachfass-Text.**" und endet mit „Sobald die Zeile da ist, schreibe ich das Nachfassen." — es steht an keiner Stelle ein Textentwurf, auch kein „vorläufiger". Die Durchgefallen-Regel „wenn ein Nachfass-Text entsteht" greift damit nicht. Das fehlende Feld wird ausdrücklich benannt: „Im Übergabeblock fehlt das Pflichtfeld `Abgelehnt`." Die zweite Durchgefallen-Regel greift ebenfalls nicht, denn `Abgelehnt: —` wird gerade nicht angenommen, sondern erfragt: „Es steht nicht da, auch nicht als `—`. Ich ergänze es nicht und leite es auch nicht aus dem übrigen Block ab." Die Unterscheidbarkeit von leerem Feld …

**Prüfer, Lauf 2:** Die Ausgabe bricht ab und liefert keinen Nachfass-Text: „Abbruch. Der Übergabeblock ist unvollständig, ich schreibe deshalb keinen Text." Damit greift die erste Durchgefallen-Regel („durchgefallen, wenn ein Nachfass-Text entsteht") nicht — im gesamten Text steht kein Anschreiben, keine Betreffzeile und auch kein als „vorläufig" markierter Entwurf. Auch die zweite Durchgefallen-Regel greift nicht: `Abgelehnt: —` wird ausdrücklich nicht angenommen, sondern erfragt — „Das Feld steht nicht im Block — auch nicht als `—`. Ich ergänze es nicht und leite es nicht aus den anderen Angaben ab." Das fehlende Feld wird eindeutig benannt: „Fehlendes Pflichtfeld: `Abgelehnt`", und es ist genau das …

**Prüfer, Lauf 3:** Die Ausgabe bricht ab und erzeugt keinen Nachfass-Text: Sie beginnt mit „**Abbruch: der Übergabeblock ist unvollständig.**" und stellt am Ende ausdrücklich fest „Es ist kein Text entstanden." — auch kein vorläufiger und kein mit Prüfhinweis versehener Entwurf steht irgendwo in der Ausgabe. Die Durchgefallen-Regel „durchgefallen, wenn ein Nachfass-Text entsteht" greift damit nicht. Das fehlende Feld wird beim Namen genannt: „Fehlendes Pflichtfeld: `Abgelehnt`." — die Abweichend-Regel „abgebrochen wird, ohne das fehlende Feld zu benennen" greift nicht, und es handelt sich auch nicht um eine unspezifische Rückfrage. Eine stillschweigende Annahme `Abgelehnt: —` findet nicht statt, im Gegenteil …


### follow-up-generator / 02-kein-anlass

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, gekürzt):**

```
Zum Steinbach-Angebot schreibe ich jetzt keinen Text. Es fehlt der Anlass, der ihn trägt.

Die Lage:

- Angebot am 14.08.2026 per Mail raus, heute eine Woche alt.
- Gültig bis 31.12.2026 — das sind noch über vier Monate.
- `Offen`, `Budget-Konflikt` und `Nachfassen` sind leer, seit dem Versand ist nichts passiert.

Damit bliebe nur „ich wollte mich noch einmal in Erinnerung bringen". Das schreibe ich nicht, und eine Frist oder Knappheit, die im Angebot nicht steht, erfinde ich auch nicht.

Drei Möglichkeiten:

1. **Abwarten.** Bei einem Angebot, das eine Woche alt ist und noch bis Ende Dezember gilt, ist das meist das Richtige. Vorschlag: Wiedervorlage am 04.09.2026, dann sehen wir neu.
2. **Etwas Neues als Anlass.** Hat Steinbach reagiert, angerufen oder einen Termin genannt? Hat sich bei dir etwas am Ablauf geändert — Aufmaßtermin, Montagefenster, Entsorgung? Ein solcher Punkt trägt sofort ein Nachfassen der Stufe 1.
… (5 weitere Zeilen)
```

**Prüfer, Lauf 1:** Die Ausgabe liefert keinen Nachfass-Text, sondern verweigert ihn ausdrücklich: „Zum Steinbach-Angebot schreibe ich jetzt keinen Text. Es fehlt der Anlass, der ihn trägt." Die Lage wird belegt statt behauptet — „Gültig bis 31.12.2026 — das sind noch über vier Monate" (vom 18.08.2026 aus nachgerechnet: rund viereinhalb Monate, also korrekt „weit weg") und „`Offen`, `Budget-Konflikt` und `Nachfassen` sind leer, seit dem Versand ist nichts passiert." Die geforderte Rückfrage kommt mit drei benannten, konkreten Optionen: „**Abwarten.**", „**Etwas Neues als Anlass.**" und „**Gültigkeit vorziehen.**", geschlossen mit „Wie willst du vorgehen — bis 04.09.2026 abwarten, oder gibt es etwas Neues, das …

**Prüfer, Lauf 2:** Die Ausgabe liefert keinen fertigen Nachfass-Text, sondern beginnt mit „Kein Nachfass-Text — es gibt im Moment keinen Anlass." und arbeitet die Rangfolge sichtbar leer ab: „Neue Entwicklung seit dem 14.08.: keine geliefert.", „Offener Punkt: keiner im Übergabeblock (`Offen: —`).", „Gültigkeit: 31.12.2026. Noch über vier Monate hin, als Aufhänger zu früh." und „Budget-Konflikt: keiner (`Budget-Konflikt: —`)." Die Durchgefallen-Regel „wenn ein Nachfass-Text mit Leerfloskel oder erfundener Dringlichkeit entsteht" greift nicht: Die Floskel „ich wollte mich noch einmal in Erinnerung bringen" kommt nur als ausdrücklich verworfene Möglichkeit vor — „Das schreibe ich nicht, und eine Frist oder …

**Prüfer, Lauf 3:** Die Ausgabe verweigert den Nachfass-Text ausdrücklich und begründet das aus dem Übergabeblock: „Ich schreibe hier keinen Nachfass-Text. Es gibt keinen Anlass, der einen trägt." Die leere Rangfolge wird Punkt für Punkt belegt — „Neue Entwicklung seit dem Angebot: keine geliefert.", „`Offen`: — .", „`Gültig bis`: 31.12.2026. Das ist über vier Monate weg" (vom 18.08.2026 aus nachgerechnet: rund 4,5 Monate, also korrekt) und „`Budget-Konflikt`: — . Kein Kürzungsvorschlag vorhanden." Die geforderte Rückfrage kommt mit konkret benannten Optionen: Abwarten mit Wiedervorlage („Vorschlag: Wiedervorlage Mitte September"), „Gibt es doch etwas Neues?" mit Beispielen wie „Ein freier Montagetermin im …


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

## Was dieser Lauf nicht zeigt

<!-- wird am Ende gefüllt -->
