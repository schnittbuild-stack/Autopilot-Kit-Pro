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

Je Helfer alle seine Fälle — aus **zwei** Sammlungen:

1. `system/eigene-testfaelle/<helfer>/` — die Fälle aus seinem eigenen
   Material. **Diese zuerst**, weil sie näher an seinem Alltag sind.
2. `system/core/testfaelle/<helfer>/` — die mitgelieferten, neutralen Fälle.

Gibt es keine eigenen, ist das kein Mangel und keine Meldung wert. Wie welche
entstehen, steht in `system/core/waechter/eigene-testfaelle.md`.

**Dazu die Ketten.** In `system/core/testfaelle/ketten/` liegen Fälle, die
nicht einem Helfer gehören, sondern einer **Übergabe** zwischen zweien. Jeder
nennt oben unter „Schnittstelle", welche Helfer beteiligt sind.

**Eine Kette kommt in Frage, sobald einer ihrer Helfer in der Nutzungsliste
steht.** Nicht erst, wenn alle beteiligten liefen — sonst würden die Ketten
fast nie geprüft, und ein Vertragsbruch fiele erst auf, wenn er beim Nutzer
schon passiert ist.

**Aber es läuft höchstens eine Kette je Check, reihum.** Ein Ketten-Fall
kostet ein Vielfaches eines Einzelfalls, weil er zwei Anleitungen und beide
Verträge mitträgt. Liefen alle fünf bei jedem Angebot mit, wäre der Check so
teuer wie eine Vollprüfung — und der Nutzungsbezug umsonst.

Welche dran ist, steht in `system/STATUS.md` unter **„Zuletzt geprüfte Kette"**.
Genommen wird die nächste in der Reihenfolge der Dateinamen, die überhaupt in
Frage kommt. Danach wird der Name dort eingetragen.

Steht dort nichts, fang bei der ersten an. Steht dort ein Name, den es nicht
mehr gibt, fang ebenfalls bei der ersten an — und sag dazu nichts, das ist
keine Meldung wert.

Wer nur Erstansprachen geschrieben hat, bekommt keine Kette geprüft: Der
`outreach-personalisierer` kommt in keiner vor.

**Warum die Ketten eigene Fälle brauchen:** Jede Stufe kann für sich
tadellos arbeiten, und trotzdem steht am Ende etwas Falsches — weil eine
Vermutung über zwei Übergaben hinweg zur Tatsache geworden ist. Das sieht kein
Einzelfall.

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
   **Aber es ist keine echte Aufgabe, und nichts davon wird abgelegt.** Das
   Erzeugte bleibt im Gespräch: **nichts nach `ergebnisse/`**, kein Eintrag in
   die Nutzungsliste, keine Änderung am Profil. Sonst füllt der Testlauf den
   Ordner, den der Nutzer als „was ich für dich gemacht habe" kennt, mit
   erfundenen Texten — und der nächste Wochencheck prüft an ihnen, ob es noch
   nach ihm klingt.
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

1. **Zuerst den Beleg sichern — vor der Meldung.** Lege den Lauf, der abgewichen ist,
   nach `system/befunde/<datum>-<helfer>-<fall>.md`: den erzeugten Text
   unverändert, darunter den Punkt aus dem Soll-Teil, der nicht erfüllt war.
   Wörtlich, ohne Deutung, ohne Kürzung.
   **Das ist keine Ausnahme von der Regel, nichts abzulegen — sondern ihr
   Grund:** In seinen Ordner kommt nichts, in deinen schon. Ein Gespräch kann
   jederzeit enden — und dann ist der Lauf weg, während die Meldung stehen
   bleibt. Ein Befund, den niemand mehr nachprüfen kann, ist keine Warnung,
   sondern ein Verdacht, der Arbeit macht.
2. **Melden**, in einer Zeile, mit dem Befund — nicht mit einer Vermutung über
   die Ursache.
3. **Zeigen**, wenn er will: die Stelle im Ergebnis und der Punkt aus dem
   Soll-Teil, der nicht erfüllt war. Nebeneinander, ohne Deutung. Willst du es
   später noch einmal zeigen, liest du es aus der Datei — nicht aus dem
   Gedächtnis des Gesprächs.
4. **Vorschlagen**, was zu ändern wäre — und ausdrücklich sagen, ob es sich um
   die Anleitung des Helfers handelt oder um seine Grundlage (Profil,
   Unterlagen).
5. **Erst nach seinem Ja ändern.** Und nur die genannte Stelle.
6. **In `system/STATUS.md` unter „Entscheidungen" vermerken:** was abwich, was
   geändert wurde, an welchem Tag — **und wie die Belegdatei heißt.**
7. **Danach denselben Fall erneut**, wieder dreimal. Bleibt er abweichend,
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
- **Er legt nichts in den Ordnern des Nutzers ab.** Kein erzeugter Testtext
  kommt nach `ergebnisse/`, nichts nach `meine-unterlagen/`, kein Helfer aus
  einem Testlauf kommt in die Nutzungsliste. Ein Testlauf ist keine Arbeit für
  den Nutzer und darf in seinem Ordner keine Spur hinterlassen.
  **Ausgenommen ist einzig `system/befunde/`** — sein eigener Ordner, nicht der
  des Nutzers. Dort landet nur ein Lauf, der abgewichen ist, nie ein
  bestandener. Bestandene Läufe werden gezählt, nicht aufbewahrt: Sie belegen
  nichts, was jemand später nachlesen müsste.
- **Er benutzt keinen Fachbegriff.** Es gelten dieselben Wörter wie überall:
  Ordner, Datei, Gedächtnis, Helfer.

## Danach

Die Liste „Seit dem letzten Wochencheck benutzt" wird geleert — aber erst,
**nachdem** der Testlauf durch ist und gemeldet wurde. Bricht er vorher ab,
bleibt die Liste stehen, damit der nächste Anlauf weiß, was noch offen war.

## Checkliste

- [ ] Nur die Helfer aus der Nutzungsliste geprüft, keine anderen.
- [ ] Jede Kette geprüft, an der ein Helfer aus der Liste beteiligt ist —
      und keine, an der keiner beteiligt ist.
- [ ] Je Fall dreimal erzeugt und dreimal getrennt bewertet.
- [ ] Beim Erzeugen nicht in den Soll-Teil gesehen, beim Bewerten nicht in die
      Anleitung.
- [ ] Je Abweichung ein Punkt aus dem Soll-Teil und ein Beleg aus dem Ergebnis.
- [ ] Je Abweichung eine Datei in `system/befunde/` — **vor** der Meldung
      geschrieben, nicht danach.
- [ ] Höchstens zwei Zeilen ausgegeben.
- [ ] Nichts geändert ohne ausdrückliches Ja.
- [ ] Kein Testfall angefasst.
- [ ] Nichts in `ergebnisse/` abgelegt und niemand in die Nutzungsliste
      eingetragen — ein Testlauf hinterlässt keine Spur im Kundenordner.
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
