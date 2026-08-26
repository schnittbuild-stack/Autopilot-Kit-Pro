# Watchdog — Bau und Prüfung, 26.08.2026

Phase 4, Punkt 1 und 3 (`BAUPLAN.md`): der Testlauf und der Reparatur-Flow.
Punkt 2 (fünf Ketten-Testfälle) und Punkt 4 (kundeneigene Fälle) stehen aus.

## Was gebaut wurde

**`core/waechter/watchdog.md`** — der Testlauf. Kein zweiter Wächter: derselbe
Auslöser („Mach den Wochencheck"), angehängt an dessen vier Prüfpunkte,
höchstens zwei Zeilen Ausgabe zusätzlich (Entscheidung 20.08.2026).

**Umfang: nach Nutzung, dreimal je Fall** (Entscheidung 25.08.2026). Gemessen:
Ein voller Durchlauf über alle 34 Fälle dreimal kostet rund 454.000 Zeichen an
Modellarbeit — beim Käufer sein Kontingent, nicht unseres. Geprüft werden
deshalb nur die Helfer, die er seit dem letzten Check benutzt hat. Bei drei
Helfern sind das rund 40.000 statt 454.000.

**Die Nutzungsspur.** Bis dahin hielt nichts fest, welcher Helfer gearbeitet
hat. Neu: ein Abschnitt in `system/STATUS.md` und eine Regel im Gedächtnis,
die ihn füllt.

**Zwischenstand je Fall.** Ein Durchlauf über drei Fälle sind achtzehn
Schritte. Endet das Gespräch dazwischen, wäre ohne Zwischenstand alles weg —
derselbe Fehlertyp, der in dieser Woche dreimal im Installer behoben wurde.

## Vier Anläufe, drei Befunde

Der Nachweis sollte einfach sein: einen Defekt einbauen, sehen, ob er gefunden
wird. Er hat vier Anläufe gebraucht, und jeder Fehlschlag hat etwas gezeigt.

### Anlauf 1 — die Schicht darüber

Entfernt wurde die Schutzregel gegen erfundene Empfängerangaben, von der aus
dem Nachlauf desselben Tages bekannt war, dass sie 2 von 3 Läufen kippt.

**Ergebnis: 3 von 3 bestanden.** Der Defekt schlug nicht durch.

**Befund:** Die eisernen Regeln in `CLAUDE.md` wirken **zusätzlich** zum Skill.
Die gemessene Fehlerrate stammte aus einem isolierten Prüfstand, in dem nur der
Skill-Text galt. Im echten Kundenbaum fängt die Schicht darüber sie ab.

### Anlauf 2 — die Redundanz im Skill

Geändert wurde ein Wort: `Pflicht: mindestens ein belegter Anknüpfungspunkt`
wurde zu `Wünschenswert`.

**Ergebnis: 3 von 3 bestanden.**

**Befund:** Der Skill sagt dieselbe Regel an **sieben Stellen** — Prozess,
Weiche, Checkliste, Beispiel. Ein verfälschter Satz ändert das Verhalten nicht.

### Anlauf 3 — der Wächter erfindet eine Abbruchbedingung

Alle sieben Stellen wurden entfernt. Der Testlauf **lief gar nicht**.

Begründung des Wächters: Der Eintrag in der Nutzungsliste trage dasselbe Datum
wie der letzte Check, sei also ein Rest und schon geprüft.

**Befund gegen den Entwurf:** Diese Regel stand nirgends. `watchdog.md` ließ
offen, was gilt, wenn Nutzungsliste und Zeitraum sich widersprechen — und der
Wächter hat die Lücke plausibel gefüllt. **Er hörte auf zu prüfen und meldete
trotzdem „nichts Neues".**

Das ist derselbe Fehler, wegen dem der Wochencheck am 20.08.2026 zur festen
Vorlage wurde: Eine Testsitzung hatte damals sieben eigene Prüfpunkte erfunden.
Hier war es subtiler — keine erfundene Prüfung, sondern ein erfundener
**Abbruch**.

**Behoben:** Die Nutzungsliste ist die alleinige Grundlage. Steht etwas darin,
läuft der Testlauf, ohne weitere Bedingung. Das Datum daneben ist eine Notiz,
keine Bedingung. Ausdrücklich ergänzt: „Erfinde hier keine zusätzliche
Bedingung."

### Anlauf 4 — gefunden, aber auf einem anderen Weg

Defekt vollständig, Nutzungsliste eindeutig.

**Testlauf: 3 von 3 in allen drei Fällen** — obwohl die zentrale Regel
vollständig fehlte.

**Und trotzdem gemeldet:**

> In seiner Anleitung fehlen vier Stücke, mitten im Satz abgeschnitten, eines
> davon in der Regel, was er tun soll, wenn ihm ein Aufhänger fehlt. Auf die
> Ergebnisse hat sich das nicht ausgewirkt, aber verlassen würde ich mich
> darauf nicht. Soll ich dir die Stellen zeigen?

Die Stelle ist exakt benannt, die Wirkung ehrlich eingeordnet, der
Reparatur-Flow korrekt begonnen — melden, anbieten, nichts ändern.

## Was das für die Definition of Done heißt

Der BAUPLAN verlangt: „Watchdog erkennt eine absichtlich eingebaute Abweichung
und schlägt den korrekten Fix vor."

**Erkannt: ja.** Korrekt verortet, korrekt eingeordnet, Reparatur-Flow korrekt
begonnen.

**Aber nicht durch den gebauten Mechanismus.** Der Testlauf war grün. Gefunden
hat er es beim **Lesen der Anleitung** — eine Fähigkeit, die in `watchdog.md`
nicht steht. Er hat sie mitgebracht, nicht bekommen.

Ehrlich benannt heißt das: **Der Nachweis ist schwächer, als die Meldung
aussehen lässt.** Und es bleibt offen, ob er eine **saubere** Entfernung auch
bemerkt hätte — die hier war grob, mit abgeschnittenen Sätzen.

## Der schwerwiegendste Befund

**Das Verhalten des Skills überlebte die vollständige Entfernung seiner
zentralen Regel.** Drei Fälle, je 3 von 3.

Das Verhalten hängt nicht an einzelnen Sätzen, sondern entsteht aus dem ganzen
Dokument: Zweck, Beispiele, Checklisten, und der Schicht darüber.

**Gut:** Das Produkt ist widerstandsfähiger als angenommen. Ein Käufer bekommt
nicht bei jeder Kleinigkeit ein anderes Verhalten.

**Schlecht:** Ein Testlauf ist ein **schwacher Melder für beschädigte Regeln**.
Was die Redundanz auffängt, sieht er nie — und was sie nicht mehr auffängt, ist
dann schon ein größerer Schaden.

Für die Erwartung an Phase 4 heißt das: Der Watchdog findet **grobe**
Abweichungen. Feine Drift — ein Modellwechsel, der eine Formulierung anders
auslegt — fängt die Redundanz womöglich ebenfalls ab, und dann meldet er nichts.
Das ist kein Fehler im Watchdog, sondern eine Eigenschaft der Bauweise. Sie
gehört in jede Aussage darüber, was er leistet.

## Nebenbefund: das Kriterium von Fall 02 war falsch

Der erste Testlauf meldete eine Abweichung, die keine war. Ein Lauf schrieb
„Sie haben auf der Fachmesse über Gießereiautomatisierung gesprochen" — der
Eingabeteil sagt aber ausdrücklich, dass Reiner den Vortrag **gehalten** hat.

Das Kriterium hatte drei Dinge vermischt: **dass** er ihn hielt (belegt),
**worüber** (belegt), **was** er darin sagte (nicht belegt). Korrigiert am
26.08.2026, vom Auftraggeber vorab geprüft.

**Das war ein Fehlalarm — die schlimmste Sorte Befund für einen Wächter.** Wer
zweimal grundlos Alarm schlägt, wird beim dritten Mal ignoriert. Der vierte
Anlauf hat die Korrektur bestätigt: Fall 02 lief 3 von 3, und der Wächter
vermerkte selbst, dass der früher abgewertete Lauf nach dem korrigierten Maßstab
bestanden hätte.

## Ein fünfter Befund — aus dem Review, nicht aus den Läufen

Der unabhängige Review hat einen Fehler gefunden, den die vier Prüfanläufe
**nicht** gezeigt haben, weil er dort zufällig nicht eintrat.

`watchdog.md` wies an, jeden Fall „wie eine echte Aufgabe des Nutzers"
abzuarbeiten — und nahm den Testlauf nirgends von den eisernen Regeln aus.
Damit hätte er die erzeugten Texte nach `ergebnisse/` gelegt und die geprüften
Helfer in die Nutzungsliste eingetragen.

**Die Folge wäre ein selbstgebauter Fehlalarm gewesen:** Bei drei Helfern bis
zu 27 erfundene Kundentexte in dem Ordner, den der Nutzer als „was ich für dich
gemacht habe" kennt. Der nächste Wochencheck liest genau diesen Ordner als
Prüfpunkt 1 — und Fall 02 ist absichtlich so gebaut, dass er zu erfundener Nähe
verleitet.

Dieselbe Klasse wie Anlauf 3: **eine Lücke im Text, die eine Sitzung plausibel
füllt.** In den vier Läufen ist sie nicht eingetreten; darauf verlassen kann
man sich nicht.

**Behoben** an drei Stellen: beim Erzeugen, unter „Was er nie tut" und in der
Checkliste. Ein Testlauf hinterlässt keine Spur im Kundenordner.

## Was aussteht

- **Fünf Ketten-Testfälle** statt zwei (`BAUPLAN.md` Phase 4, Punkt 2). Erst
  damit ist die Definition of Done vollständig prüfbar — sie spricht von einer
  Abweichung **in der Kette**.
- **Kundeneigene Testfälle** (Punkt 4). Bis dahin gilt: Was hier grün ist, ist
  gegen unsere konstruierten Fälle grün, nicht gegen den Alltag des Käufers.
- **Ob eine saubere Regeländerung bemerkt wird.** Der geprüfte Defekt war grob.
