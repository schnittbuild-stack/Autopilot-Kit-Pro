# Wochencheck — der Wächter, V1

<!-- Plattformneutral (Prinzip 4). FESTE Vorlage: Jeder Käufer bekommt genau
     diesen Wochencheck, mit genau diesen vier Prüfpunkten. Sie werden nicht
     kopiert, nicht umgeschrieben und nicht ergänzt — weder vom Installer noch
     im laufenden Betrieb. Wer einen fünften Prüfpunkt braucht, ändert diese
     Datei im Repo, nicht beim Kunden.
     Entscheidung 20.08.2026, siehe docs/entscheidungen.md.
     Ausbau in BAUPLAN.md, Phase 4 (Watchdog). -->

## Zweck (ein Satz)

Einmal die Woche nachsehen, ob die Helfer noch mit dem arbeiten, was heute
gilt — und dem Nutzer in höchstens fünf Zeilen sagen, was zu tun wäre.

## Wann er läuft

Der Nutzer sagt **„Mach den Wochencheck"**. Sonst nie. Der Check startet nicht
von selbst, erinnert nicht an sich und unterbricht keine Aufgabe.

Sieh zuerst in `system/STATUS.md` nach, wann der letzte Check war. Alles, was
seitdem passiert ist, ist der Zeitraum. Steht dort nichts, nimm die letzten
sieben Tage.

## Die vier Prüfpunkte — genau diese, keine weiteren

### 1. Klingt es noch nach ihm?

Nimm die neuesten Ergebnisse aus `ergebnisse/` seit dem letzten Check,
höchstens drei. Vergleiche sie mit `mein-profil.md`: Ton, Anrede, Signatur —
und vor allem die Liste unter „Sätze und Themen, die nie vorkommen".

**Ein Treffer aus dieser Liste ist immer ein Befund**, auch ein einzelner, auch
in einem Entwurf. Genau dafür steht die Liste da.

**Was geprüft wird, ist der Text, der zum Kunden gegangen wäre** — das Angebot,
die Mail, das Protokoll. Eine Notiz **über** die Arbeit gehört nicht dazu: Steht
ein verbotenes Wort dort ausdrücklich als gestrichen oder ersetzt da („statt
‚zeitnah‘ jetzt ein Datum"), ist das der Beleg, dass die Regel gegriffen hat,
und kein Befund. Im Kundentext selbst bleibt jeder einzelne Treffer ein Befund —
auch dann, wenn eine Notiz daneben behauptet, er sei entfernt worden.

### 2. Rechnet er noch mit gültigen Preisen?

Prüfe `meine-unterlagen/preise/` nach `core/unterlagen/preisregeln.md`:

- Liegt dort mehr als eine Preisdatei?
- Lässt sich der Stand ermitteln (`gültig bis`, `Stand`, Datum im Dateinamen,
  Bestätigungsnotiz)?
- Liegt der Stand innerhalb der Frist aus dem Profil („Wie lange ein Preisstand
  ohne Rückfrage gilt")?
- Ist eine Kundenkondition in `preise/kunden/` abgelaufen?

Ein Befund ist hier keine Rechnung, sondern ein Hinweis mit dem Datum darin.

### 3. Ist etwas liegengeblieben?

Sieh in `system/STATUS.md` unter „Was der Nutzer noch nachliefern wollte" und
„Offene Punkte" nach. Nenne, was offen ist — **einmal, freundlich, ohne
Nachdruck**. Was er beim letzten Mal schon nicht nachgeliefert hat, wird nicht
zum zweiten Mal angemahnt; es bleibt in der Liste, nicht in der Meldung.

### 4. Fehlt ein Helfer?

Gab es im Zeitraum eine Aufgabe, für die die Zuordnungstabelle in `CLAUDE.md`
keinen Eintrag hat? Dann schlag vor, sie nachzutragen — nicht, etwas
„nachzuinstallieren". Der Nutzer soll nie hören, dass ihm etwas fehlt.

## Nach den vier Prüfpunkten: der Testlauf

Steht in `system/STATUS.md` unter „Seit dem letzten Wochencheck benutzt"
mindestens ein Helfer, arbeitest du anschließend
`system/core/waechter/watchdog.md` ab. Er lässt genau diese Helfer gegen ihre
eigenen Testfälle laufen — das ist die einzige Art, ihr **Verhalten** zu
prüfen statt nur ihre Ergebnisse.

Steht dort nichts, entfällt der Testlauf. Ohne Erwähnung.

**Das ist kein fünfter Prüfpunkt und kein zweiter Wächter:** derselbe
Auslöser, dieselbe Ausgabe, höchstens zwei Zeilen mehr.

## Was der Check nie tut

- **Er ändert nichts.** Kein Profil, keine Unterlage, keine Assistenten-Datei,
  kein fertiges Ergebnis. Er meldet und schlägt vor; geändert wird erst nach
  einem ausdrücklichen Ja des Nutzers, und dann nur die genannte Stelle.
- **Er erfindet keinen Befund.** Was er nicht prüfen konnte — kein Material,
  kein Ergebnis im Zeitraum —, nennt er als „konnte ich nicht prüfen", nie als
  „sauber".
- **Er rechnet nichts nach** und schreibt kein Ergebnis neu, solange niemand
  ihn darum bittet.
- **Er benutzt keinen Fachbegriff.** Es gelten dieselben Wörter wie überall:
  Ordner, Datei, Gedächtnis, Helfer.

## Was er ausgibt

Höchstens **fünf Zeilen**. Je Befund eine Zeile: was aufgefallen ist, und ein
Vorschlag, der mit einer Frage endet.

> In zwei Angeboten von letzter Woche steht „zeitnah" — das wolltest du nicht.
> Soll ich die Stellen korrigieren?
> Deine Preisliste ist vom 3. März und damit älter als ein halbes Jahr. Gilt
> die noch?

**Nichts gefunden ist ein Ergebnis, kein Anlass für eine Liste:**

> Alles sauber, nichts zu tun.

Keine Aufzählung dessen, was geprüft wurde. Der Nutzer hat den Check nicht
bestellt, um zu erfahren, was alles in Ordnung ist.

## Danach

Trag in `system/STATUS.md` ein, wann der Check gelaufen ist und was gemeldet
wurde. Ohne diesen Eintrag prüft der nächste Check denselben Zeitraum noch
einmal und meldet dasselbe zum zweiten Mal.

## Checkliste

- [ ] Zeitraum aus dem letzten Check-Datum bestimmt, nicht geraten.
- [ ] Alle vier Prüfpunkte durchgegangen — auch die, zu denen es nichts gibt.
- [ ] Kein fünfter Prüfpunkt dazuerfunden.
- [ ] Nichts geändert; jeder Vorschlag endet mit einer Frage.
- [ ] Was nicht prüfbar war, steht als „konnte ich nicht prüfen" da.
- [ ] Höchstens fünf Zeilen, kein Fachbegriff, keine Aufzählung des Geprüften.
- [ ] Datum und Meldung stehen in `system/STATUS.md`.
- [ ] Stand ein Helfer in der Nutzungsliste, ist der Testlauf gelaufen —
      und die Liste erst danach geleert.

## Was dieser Wochencheck noch nicht kann

Die vier Prüfpunkte sehen sich **Ergebnisse und Unterlagen** an — nicht das
Verhalten der Helfer. Dafür gibt es seit Phase 4 den Testlauf
(`watchdog.md`), der im Abschnitt darüber angehängt ist.

Auch mit ihm bleibt eine Lücke: Er prüft gegen die **mitgelieferten** Fälle.
Die sind konstruiert und neutral. Eigene Fälle aus dem Material des Käufers
sind der nächste Ausbau (Entscheidung 17.08.2026, `BAUPLAN.md` Phase 4).

**Diese Fassung ist bewusst klein:** vier Prüfpunkte, die ohne Testlauf zu
entscheiden sind. Ein Wächter, der bei jedem Käufer anders aussieht, ist
schlechter als ein kleiner, der überall gleich ist.
