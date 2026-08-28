# Vertrag: `account-recherche` → `outreach-personalisierer`

<!-- Plattformneutral (Prinzip 4). Bindend fuer beide Seiten.
     Aenderungen laufen ueber diesen Vertrag und einen Eintrag in
     docs/entscheidungen.md — nie einseitig in einem Skill. -->

## Wer übergibt an wen, wann

`account-recherche` liefert `outreach-personalisierer` das, was dieser als
**Pflicht** braucht: mindestens einen belegten Anknüpfungspunkt.

Diese Übergabe fand bisher **ohne Vertrag** statt — der Nutzer reichte die
Fakten weiter, und der Skill hielt fest, dass die Trennung „sinngemäß" gelte.
„Sinngemäß" ist genau das Wort, an dem zwei Seiten dasselbe zu tun meinen und
Verschiedenes tun. Prinzip 3 verlangt: erst Vertrag, dann Agenten.

## Übergabeformat (bindend)

**Dasselbe `RECHERCHE-ERGEBNIS` wie an `angebots-schreiber`.** Der Sender
ändert nichts; es gibt nur einen Block, und er bedient beide Empfänger. Felder,
Reihenfolge und Pflichtangaben stehen in
`core/vertraege/account-recherche-zu-angebots-schreiber.md` und werden hier
nicht wiederholt.

## Was der Empfänger damit darf

- **Nur `Belegte Fakten` werden zum Anknüpfungspunkt** — und die Quelle wird
  mitgenannt. Ein Aufhänger ohne Quelle ist keiner.
- **`Unbelegt` erscheint in keinem Kundentext.** Nicht als Behauptung, nicht
  als Frage, nicht abgeschwächt. Vermutungen dürfen die Suche leiten, nie den
  Text.
- **`Nicht gefunden` ist Material für die Rückmeldung**, wenn kein
  Anknüpfungspunkt vorliegt: Es sagt, wonach schon gesucht wurde, damit der
  Nutzer nicht dasselbe noch einmal vorschlägt.
- **`Ansprechpartner` fehlt** → keine Anrede erfinden. Der Skill fragt nach,
  bevor ein Text entsteht.
- **`Verhältnis`** interessiert diesen Empfänger nicht. Eine Erstansprache geht
  an jemanden, mit dem noch nichts läuft; steht dort `bestandskunde`, ist die
  Erstansprache die falsche Aufgabe, und das wird einmal gesagt.

## Was bei fehlenden Feldern passiert

| Fall | Reaktion |
|---|---|
| `Belegte Fakten` ist `—` | **Kein Text.** Das ist der Pflicht-Fall des Skills: benennen, welche Sorten Information reichen würden, `account-recherche` anbieten. `Nicht gefunden` wird dabei genannt, damit nichts doppelt gesucht wird. |
| `Ansprechpartner` fehlt | **Rückfrage vor dem Text**, in derselben Nachricht wie alle anderen offenen Punkte. Nie eine erfundene oder allgemeine Anrede. |
| Eines der drei Listenfelder fehlt **ganz** | **Abbruch mit Meldung.** Ein fehlendes `Nicht gefunden` ist von einer gründlichen Recherche nicht zu unterscheiden — derselbe Grund wie im Vertrag zum `angebots-schreiber`. |
| Recherche liegt gar nicht vor | Kein Fehler. Der Skill arbeitet mit dem, was der Nutzer mitgibt, und verlangt weiterhin einen belegten Anknüpfungspunkt. |

Nie stilles Raten, nie ein Feld sinngemäß aus einem anderen ableiten.

## Testfälle für diese Schnittstelle

**Was hier steht, sind Belege, keine Bestandsliste:** je ein Fall, die Regel,
die er prüft, und das Datum. Kommt ein Ketten-Fall dazu, wird dieser Abschnitt
dadurch nicht falsch — er wird nur nicht von selbst länger. **Welche Fälle
diese Schnittstelle insgesamt führen, steht in den Fällen selbst**, oben in der
Zeile „Schnittstelle".

`core/testfaelle/ketten/06-recherche-zu-erstansprache.md` — zweistufig, prüft
die Empfängerregeln oben an ihrer schärfsten Stelle: `Verhältnis: bestandskunde`
bei ausdrücklichem Auftrag zur Erstansprache, fehlender `Ansprechpartner`, und
eine Unbelegt-Liste, die genau die Sätze hergibt, die den Text lebendig machen
würden. **3 von 3 am 28.08.2026** (`docs/berichte/unbelegte-versprechen.md`).

`outreach-personalisierer/01-duenne-faktenlage.md` prüft diese Schnittstelle
**nicht**, auch wenn es so aussieht: Dort liegt gar keine Recherche vor, also
geht kein `RECHERCHE-ERGEBNIS` hinein und keine der Empfängerregeln oben wird
berührt.

`core/testfaelle/ketten/07-recherche-ohne-belege.md` — der Pflicht-Fall
`Belegte Fakten: —`: kein Text, stattdessen benennen, welche Sorten Information
einen Aufhänger trügen, `account-recherche` anbieten und sagen, wonach schon
vergeblich gesucht wurde. **3 von 3 am 28.08.2026.**

`core/testfaelle/ketten/08-fehlendes-listenfeld.md` — der Abbruch bei einem ganz
fehlenden Listenfeld, geprüft an der unbequemsten Stelle: Ein belegter, sofort
verwendbarer Aufhänger liegt vor, und es wird trotzdem abgebrochen.
**3 von 3 am 28.08.2026.**

**Drei der vier Zeilen der Tabelle oben tragen damit einen datierten Beleg.**
Die vierte — „Recherche liegt gar nicht vor" — beschreibt den Fall, in dem
**dieser Vertrag gar nicht greift**: Es geht kein `RECHERCHE-ERGEBNIS` hinein,
der Skill arbeitet allein. Was er dann tut, prüft
`outreach-personalisierer/01-duenne-faktenlage`; über diese **Schnittstelle**
sagt der Fall nichts, und genau deshalb steht er oben als „prüft sie nicht".
Ein eigener Ketten-Fall wäre hier sinnlos — es gibt keine Kette zu prüfen.

Der Vertrag war vom 27. bis zum 28.08.2026 geschrieben und unbelegt; er hat das
selbst ausgewiesen, statt es zu verschweigen.

> **Berichtigt am 28.08.2026.** Hier stand „Damit ist jede Zeile der Tabelle
> oben belegt". Das war falsch: Die vierte Zeile hat keinen benannten Fall, und
> zwei Absätze weiter oben steht, dass `01-duenne-faktenlage` diese
> Schnittstelle nicht prüft. **Eine Vollständigkeitsaussage, die das Nachfragen
> beendet, ist gefährlicher als eine ausgewiesene Lücke** — gemeldet vom
> unabhängigen Review, dreimal hintereinander, bis sie behoben war.
