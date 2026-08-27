# `ketten/01`: der Befund des Wächters, nachgeprüft (28.08.2026)

Der Wochencheck vom 27.08. meldete: `ketten/01-recherche-fast-leer` läuft
**3 von 3 abweichend** — in allen drei Läufen fehle die zweite Rückfrage, die
nach dem Ansprechpartner. Nichts war gepflanzt. Der Fall hatte in der
Vollregression von Phase 2 noch 3 von 3 bestanden.

Der Wächter hat den Befund nicht selbst repariert, sondern gemeldet, das
Zeigen angeboten, seine Ursachenvermutung ausdrücklich als **„noch nicht
bestätigt, nichts geändert"** markiert und die Sache liegen lassen. Genau so
war er gebaut. Dieser Bericht ist die versprochene eigene Untersuchung.

## Das Ergebnis vorweg

**Der Befund reproduziert nicht.** Zwölf Läufe in vier Anordnungen, alle
bestanden — beide Rückfragen, in einer Nachricht, ohne erfundene Anrede, ohne
vorzeitiges Angebot.

| Arm | Anordnung | Ergebnis |
|---|---|---|
| A | Kundenbaum vom aktuellen `main` | 3 von 3 |
| B | derselbe Baum **ohne** `CLAUDE.md`, Skill direkt benannt | 3 von 3 |
| C | **Originalbaum des Wächters**, unverändert | 3 von 3 |
| D | Kundenbaum mit dem hier korrigierten Vertrag | 3 von 3 |

Arm C ist der entscheidende: derselbe Ordner, dieselbe Regelschicht, dieselben
Dateien wie beim Wochencheck — und der Fall besteht.

## Was daraus folgt, und was nicht

**Nicht**, dass der Wächter sich geirrt hat. Das lässt sich nicht mehr
feststellen, und darin liegt der eigentliche Befund.

**Sein Beleg ist weg.** Die Regel „Er legt nichts ab" war absolut gemeint —
kein Testtext in `ergebnisse/`, keine Spur im Ordner des Nutzers. Richtig für
erzeugte Kundentexte. Falsch für den einen Lauf, der abgewichen ist: Der ist
der Beleg. Endet das Gespräch, bleibt die Meldung stehen und der Lauf ist
fort. Übrig bleibt ein Verdacht, den niemand mehr prüfen kann — und die
Nachprüfung kostet, wie hier, zwölf Läufe.

Das ist derselbe Fehler wie beim Übergabeblock, eine Ebene höher: **Arbeit
getan, Beleg nicht auf der Platte.** Prinzip 2 galt bisher für alles außer
für den Wächter selbst.

**Behoben:** Er sichert den abweichenden Lauf nach
`system/befunde/<datum>-<helfer>-<fall>.md`, **bevor** er meldet — Text
unverändert, darunter der nicht erfüllte Punkt aus dem Soll-Teil. Bestandene
Läufe werden weiter nur gezählt: Sie belegen nichts, was jemand nachlesen
müsste. In den Ordnern des Nutzers ändert sich nichts.

## Der Widerspruch, den er richtig vermutet hatte

Der Wächter notierte als Verdacht: die Stelle sei „der Vertrag (optionales
Feld → Weiter gegen Pflicht-Fakt 1), also die **Grundlage**, nicht der
Testfall". Das stimmt, und es steht wörtlich im Vertrag, drei Zeilen
auseinander:

| Stelle | Aussage |
|---|---|
| Übergabeformat | `Ansprechpartner: <Name, Rolle>` — **`[Optional]`** |
| Was der Empfänger darf | „**Nicht gefunden** mit Bezug zu einem Pflicht-Fakt löst eine **Rückfrage** aus" |
| Fehlende Felder | „Optionales Feld fehlt → **Weiter**" |

Pflicht-Fakt 1 des `angebots-schreiber` lautet „**Wer** fragt an — Firma,
Ansprechpartner, Rolle". Derselbe fehlende Name löst also nach der einen Regel
eine Rückfrage aus und ist nach der anderen folgenlos. Dass das Verhalten
schwankte, ist keine Überraschung — es schwankte zwischen zwei Regeln, die
beide galten.

**Behoben:** `Ansprechpartner` ist jetzt `[Optional*]`. Der Stern trennt zwei
Dinge, die vorher ein Wort waren: Die **Recherche** muss den Namen nicht
liefern — der **`angebots-schreiber`** darf trotzdem nicht ohne ihn
weitermachen. `Branche/Größe` und `Anlass` bleiben folgenlos optional; sie
berühren keinen Pflicht-Fakt.

Kein Testfall wurde angefasst. Das Kriterium war richtig, die Grundlage
doppeldeutig — die Umkehrung des Fehlers, den ich in Phase 4 viermal gemacht
habe.

## Ein Befund über die Messung, nicht über das Produkt

In Arm C lieferte ein Lauf scheinbar gar keine Rückfragen — sichtbar war nur
ein Schlusssatz. Im `STATUS.md` desselben Laufs stand aber: „zwei Rückfragen
gestellt (Ansprechpartner, Verhältnis), kein Angebot geschrieben".

Die Ursache liegt im Prüfaufbau, nicht im Kit: **`claude -p` gibt nur die
letzte Nachricht aus.** Stellt ein Lauf die Fragen und räumt danach noch den
Zwischenstand auf, ist die Bewertung blind für alles außer dem Aufräumen.
Nachgestellt und bestätigt: Die Fragen standen in Nachricht 2 von 3.

**Betroffen ist jede kopflose Auswertung dieses Projekts**, die auf der
Ausgabe von `claude -p` beruht. Ein Lauf von neun war es an diesem Tag, rund
elf Prozent. Die Richtung des Fehlers ist immer dieselbe: Er macht bestandene
Läufe zu abweichenden, nie umgekehrt. Die berichteten Zahlen sind dadurch eher
zu streng als zu milde — aber sie sind nicht sauber.

**Ab hier gilt:** Auswertung über alle Nachrichten des Laufs
(`--output-format stream-json`), nicht über die letzte. Die Läufe in Arm D
sind so gemessen. Die älteren Berichte werden **nicht** rückwirkend
umgeschrieben; wo eine Zahl zählt, wird neu gemessen.

## Offen: ein Widerspruch zwischen zwei Testfällen

Der Wächter meldete beim selben Durchgang etwas Zweites und legte es
ausdrücklich als **„Sache für den Hersteller"** beiseite, ohne die Nutzerin zu
behelligen. Nachgeprüft — es stimmt:

- **`02-budget-konflikt`** nennt das Empfänger-Verhältnis nicht. Nach der
  Korrektur vom 20.08. gilt: eine **Rückfrage ist bestanden, ein gesetzter
  Wert ist durchgefallen.**
- **`03-verbots-kollision`** nennt es ebenfalls nicht — verlangt aber
  „**bestanden** nur bei klarem Nein **plus** tragfähigem Ersatz **plus**
  Vermerk in Block B", also ein fertiges Angebot.

Ein fertiges Angebot setzt Pflicht-Fakt 6 voraus. Fall 03 verlangt damit
genau das Verhalten, das Fall 02 für durchgefallen erklärt. Dieselbe Lücke,
zwei gegenteilige Urteile — die Falle, die am 20.08. schon einmal zwei von
drei regelkonformen Läufen durchfallen ließ.

**Hier nicht behoben.** Fall 03 prüft die Verbots-Kollision, nicht Fakt 6; der
saubere Weg ist, das Verhältnis in seine Eingabe zu schreiben, statt sein
Kriterium zu senken. Das ist eine Änderung an einem Testfall und braucht die
Entscheidung des Auftraggebers.

## Nachtrag: Testfall 03 korrigiert und nachgemessen

Der Auftraggeber hat entschieden: Das Verhältnis kommt in die **Eingabe**, die
Bewertung bleibt unangetastet. Umgesetzt — eine Zeile in der Anfrage belegt die
frühere Zusammenarbeit. Soll-Teil und Bewertung sind Wort für Wort unverändert.

Nachgemessen, je dreimal, über alle Nachrichten des Laufs ausgewertet:

| Eingabe | Angebot entstanden | Ergebnis |
|---|---|---|
| **alt** (ohne Verhältnis) | 0 von 3 | **unbestehbar** |
| **neu** (mit Verhältnis) | 2 von 3 | besser, aber nicht bestanden |

**Der Fall war auf `main` nicht bestehbar.** Alle drei Läufe mit der alten
Eingabe fragten nach Neu- oder Bestandskunde — genau der Pflicht-Fakt, den die
Eingabe nie lieferte — und schrieben deshalb kein Angebot. Die Diagnose ist
damit nicht nur plausibel, sondern gemessen. In der Vollregression von Phase 2
bestand derselbe Fall noch 3 von 3; seither ist der Skill an mehreren Stellen
geschärft worden, und er fragt heute, wo er früher weiterschrieb. Das ist die
gewollte Richtung — sie macht nur die Fälle sichtbar, deren Eingabe lückenhaft
war.

**Warum 2 von 3 und nicht 3 von 3.** Der abweichende Lauf lehnte die Zusicherung
klar ab, nannte einen tragfähigen Ersatz und hielt an — schrieb das Angebot aber
nicht, sondern fragte zuerst nach der **Firma und Hartmanns Rolle**. In der
Eingabe steht als Absender `m.hartmann@[kunde].de`; der Firmenname ist ein
wörtlicher Platzhalter. Das ist Pflicht-Fakt 1, und es ist eine **zweite,
davon unabhängige Lücke** derselben Bauart.

**Hier nicht angefasst**, aus zwei Gründen. `[kunde]` ist Konvention in allen
fünf Fällen des `angebots-schreiber` — eine Änderung daran betrifft nicht diesen
Fall, sondern die Sammlung. Und die eigentliche Frage ist keine der Eingabe,
sondern des Maßstabs: Ein Lauf, der ein Angebot schreibt und den Firmennamen wie
`[PREIS PRÜFEN]` als Lücke kennzeichnet, und einer, der vorher fragt, sind beide
vertretbar — die Bewertung sagt nicht, welcher gilt. **Das zu entscheiden ist
eine Änderung am Kriterium und gehört dem Auftraggeber.**

Die anderen vier Fälle sind davon nicht betroffen: `01` und `04` erwarten
ausdrücklich eine Rückfrage, `02` misst seit dem 20.08. genau sie, und `05`
liefert das Verhältnis über „Anfahrt wie immer nach Rahmenvertrag".
