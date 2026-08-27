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

`core/testfaelle/outreach-personalisierer/01-duenne-faktenlage.md` prüft den
Hauptfall: Recherche fast leer, kein Text, drei Sorten Fundort, Suche
angeboten. Ein eigener Ketten-Fall für diese Schnittstelle ist ein Kandidat,
sobald sich zeigt, dass sie im Alltag benutzt wird.
