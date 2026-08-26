# Watchdog — der Testlauf, V1

<!-- Plattformneutral (Prinzip 4). FESTE Vorlage: Jeder Käufer bekommt genau
     diesen Testlauf. Er wird nicht kopiert, nicht umgeschrieben und nicht
     ergänzt — weder vom Installer noch im laufenden Betrieb.
     Er ist kein zweiter Wächter: Ausgelöst wird er vom Wochencheck, nach
     dessen vier Prüfpunkten (Entscheidung 20.08.2026).
     Umfang nach Nutzung, dreimal je Fall (Entscheidung 25.08.2026). -->

## Zweck (ein Satz)

Nachsehen, ob die Helfer **noch tun, was sie sollen** — indem sie gegen ihre
eigenen Testfälle laufen, nicht indem jemand ihre Ergebnisse liest.

## Warum das der Wochencheck nicht kann

Der Wochencheck sieht sich Ergebnisse und Unterlagen an. Ob ein Helfer seine
eigenen Regeln einhält, sieht man daran nicht: Ein Ergebnis kann gut aussehen
und trotzdem aus einer erfundenen Angabe entstanden sein.

Das merkt nur, wer den Helfer gegen einen Fall laufen lässt, dessen richtiges
Ergebnis vorher feststeht.

## Wann er läuft

**Nur als Teil des Wochenchecks**, nach dessen vier Prüfpunkten. Kein eigener
Auslöser, kein eigener Zeitplan, keine Erinnerung.

Er läuft **gar nicht**, wenn unter „Seit dem letzten Wochencheck benutzt"
nichts steht. Dann sagt der Wochencheck dazu nichts — kein „nichts geprüft",
keine Zeile. Wer nicht gearbeitet hat, braucht keinen Bericht.

**Steht dort etwas, läuft er — ohne weitere Bedingung.** Die Liste ist die
einzige Grundlage dafür, was geprüft wird. Das Datum daneben ist eine Notiz,
keine Bedingung: Ein Eintrag ist **nicht** deshalb erledigt, weil er älter
aussieht als der letzte Check. Er verschwindet erst, wenn sein Testlauf
gelaufen und gemeldet ist — und nur dadurch.

Erfinde hier keine zusätzliche Bedingung. Wenn die Liste und dein Eindruck
auseinandergehen, gilt die Liste.

## Was geprüft wird

**Nur die Helfer aus der Liste** „Seit dem letzten Wochencheck benutzt" in
`system/STATUS.md`. Nicht alle. Wer diese Woche kein Angebot geschrieben hat,
braucht den Angebots-Helfer nicht geprüft.

Je Helfer alle seine Fälle aus `system/core/testfaelle/<helfer>/`.

## Wie oft je Fall: dreimal

**Jeder Fall wird dreimal erzeugt und dreimal getrennt bewertet.** Bestanden
ist er nur bei drei von drei.

Das ist keine Vorsicht, sondern Erfahrung: Die häufigste Fehlerart ist der
**Wackler** — ein Helfer, der zweimal richtig und einmal falsch antwortet. Ein
einzelner Lauf hätte ihn mit zwei Dritteln Wahrscheinlichkeit übersehen und
„alles gut" gemeldet. Genau das ist die Meldung, die Schaden anrichtet.

## Wie ein Fall läuft

1. **Erzeugen.** Nimm den Eingabeteil des Falls und arbeite ihn ab wie eine
   echte Aufgabe des Nutzers — mit `mein-profil.md`, mit `meine-unterlagen/`.
   **Sieh dabei nicht in den Soll-Teil.** Wer die erwartete Antwort kennt,
   prüft nichts mehr.
2. **Bewerten.** Vergleiche das Ergebnis mit dem Soll-Teil des Falls.
   **Ohne die Anleitung des Helfers dabei zu lesen** — sonst prüfst du, ob er
   sich selbst gehorcht hat, statt ob das Ergebnis taugt.
3. Beides dreimal, danach zählen.

Kommt ein Fall nicht durch, halte fest, **welcher Punkt des Soll-Teils** nicht
erfüllt war, mit einem Beleg aus dem Ergebnis. „Weicht ab" ohne Fundstelle ist
kein Befund.

## Zwischenstand: nach jedem Fall, nicht am Ende

Ein Testlauf über drei Fälle sind achtzehn Schritte — dreimal erzeugen und
dreimal bewerten je Fall. Das dauert, und ein Gespräch kann dazwischen enden.

**Nach jedem abgeschlossenen Fall schreibst du das Ergebnis nach
`system/STATUS.md`** unter „Laufender Testlauf": den Helfer, den Fall, und wie
oft er bestanden hat. Erst dann fängst du den nächsten an.

Findest du dort beim Start schon Einträge, **fängst du nicht von vorn an**,
sondern machst beim ersten Fall weiter, der noch nicht dasteht.

Ist der Testlauf gemeldet, wird der Abschnitt geleert — zusammen mit der
Nutzungsliste.

Ohne das wäre nach einem Gesprächsende die ganze Arbeit weg, und der Nutzer
zahlt sie ein zweites Mal.

## Was er ausgibt

**Höchstens zwei Zeilen**, angehängt an die fünf des Wochenchecks:

> Der Angebots-Helfer ist bei 2 von 3 Fällen abgewichen — beide Male hat er
> einen Preis gesetzt, statt `[PREIS PRÜFEN]` zu schreiben. Soll ich dir die
> Stellen zeigen?

**Alles bestanden ist eine Zeile, keine Liste:**

> Die drei Helfer, die du benutzt hast, laufen wie sie sollen.

Keine Aufzählung der geprüften Fälle. Der Nutzer hat den Check nicht bestellt,
um zu erfahren, was in Ordnung ist.

## Wenn etwas abweicht: der Reparatur-Flow

1. **Melden**, in einer Zeile, mit dem Befund — nicht mit einer Vermutung über
   die Ursache.
2. **Zeigen**, wenn er will: die Stelle im Ergebnis und der Punkt aus dem
   Soll-Teil, der nicht erfüllt war. Nebeneinander, ohne Deutung.
3. **Vorschlagen**, was zu ändern wäre — und ausdrücklich sagen, ob es sich um
   die Anleitung des Helfers handelt oder um seine Grundlage (Profil,
   Unterlagen).
4. **Erst nach seinem Ja ändern.** Und nur die genannte Stelle.
5. **In `system/STATUS.md` unter „Entscheidungen" vermerken:** was abwich, was
   geändert wurde, an welchem Tag.
6. **Danach denselben Fall erneut**, wieder dreimal. Bleibt er abweichend,
   sagst du das — und änderst nicht ein zweites Mal auf Verdacht.

## Was er nie tut

- **Er ändert nichts ohne ein Ja.** Weder Anleitung noch Profil noch ein
  fertiges Ergebnis.
- **Er ändert nie einen Testfall.** Wenn ein Fall falsch zu sein scheint, ist
  das ein Befund für den Hersteller, keine Reparatur beim Nutzer. Ein Wächter,
  der sein eigenes Maß verstellt, misst nichts mehr.
- **Er erfindet keinen Befund** und schönt keinen. Was er nicht laufen lassen
  konnte — fehlendes Material, fehlende Angabe —, nennt er „konnte ich nicht
  prüfen", nie „sauber".
- **Er läuft nicht heimlich öfter**, um ein besseres Ergebnis zu bekommen.
  Dreimal ist dreimal; das Ergebnis des vierten Laufs zählt nicht.
- **Er benutzt keinen Fachbegriff.** Es gelten dieselben Wörter wie überall:
  Ordner, Datei, Gedächtnis, Helfer.

## Danach

Die Liste „Seit dem letzten Wochencheck benutzt" wird geleert — aber erst,
**nachdem** der Testlauf durch ist und gemeldet wurde. Bricht er vorher ab,
bleibt die Liste stehen, damit der nächste Anlauf weiß, was noch offen war.

## Checkliste

- [ ] Nur die Helfer aus der Nutzungsliste geprüft, keine anderen.
- [ ] Je Fall dreimal erzeugt und dreimal getrennt bewertet.
- [ ] Beim Erzeugen nicht in den Soll-Teil gesehen, beim Bewerten nicht in die
      Anleitung.
- [ ] Je Abweichung ein Punkt aus dem Soll-Teil und ein Beleg aus dem Ergebnis.
- [ ] Höchstens zwei Zeilen ausgegeben.
- [ ] Nichts geändert ohne ausdrückliches Ja.
- [ ] Kein Testfall angefasst.
- [ ] Nach **jedem** Fall ein Zwischenstand geschrieben, nicht erst am Ende.
- [ ] Bei vorhandenem Zwischenstand fortgesetzt statt neu angefangen.
- [ ] Nutzungsliste und Zwischenstand erst nach der Meldung geleert.

## Was dieser Testlauf noch nicht kann

Er prüft **gegen die mitgelieferten Fälle**. Die sind konstruiert und neutral —
sie treffen den Alltag des Nutzers nur ungefähr. Ein Helfer kann alle drei
bestehen und in dessen Branche trotzdem danebenliegen.

Kundeneigene Fälle aus dem Material des Nutzers sind der nächste Ausbau
(`BAUPLAN.md`, Phase 4, Punkt 4). Bis dahin gilt: **Was hier grün ist, ist
gegen unsere Fälle grün — nicht gegen seine.**
