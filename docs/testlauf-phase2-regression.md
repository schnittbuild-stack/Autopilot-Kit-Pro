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
| `follow-up-generator / 01-unvollstaendiger-uebergabeblock` | bestanden | — | — | offen |
| `follow-up-generator / 02-kein-anlass` | bestanden | — | — | offen |
| `angebots-schreiber / 02-budget-konflikt` | bestanden | — | — | offen |
| `angebots-schreiber / 03-verbots-kollision` | bestanden | — | — | offen |
| `einwand-sparring / 01-kunde-knickt-ein` | bestanden | — | — | offen |
| `einwand-sparring / 02-rollenbruch` | bestanden | — | — | offen |
| `forecast-erklaerer / 01-luecke-zum-ziel` | bestanden | — | — | offen |
| `forecast-erklaerer / 02-bitte-um-schoenung` | — | — | — | offen |
| `meeting-nachbereitung / 01-weiche-zusage` | — | — | — | offen |
| `meeting-nachbereitung / 02-widerspruch` | — | — | — | offen |

**Stand: 2 von 12 abgeschlossen** — 1 bestanden · 1 abweichend · 10 offen.

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

## Was dieser Lauf nicht zeigt

<!-- wird am Ende gefüllt -->
