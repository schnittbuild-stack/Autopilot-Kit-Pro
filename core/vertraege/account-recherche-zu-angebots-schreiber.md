# Übergabevertrag: account-recherche → angebots-schreiber

<!-- Geschrieben VOR account-recherche und follow-up-generator (BAUPLAN Phase 2,
     Schritt 3). Änderungen nur per Eintrag in docs/entscheidungen.md, danach
     beide beteiligten Agenten prüfen. -->

## Wer übergibt an wen, wann

`account-recherche` liefert den Firmenkontext, den `angebots-schreiber` für die
Pflicht-Fakten 1 (Wer fragt an) und 6 (Neu- oder Bestandskunde) braucht — immer
dann, wenn vor einem Angebot recherchiert wurde.

**Was diese Übergabe NICHT liefert:** die Pflicht-Fakten 2 (Was), 4 (Bis wann)
und 5 (Preisgrundlage). Die stehen in der Anfrage oder im Profil, nie in der
Recherche. `angebots-schreiber` fragt sie unverändert nach, auch wenn eine
lückenlose Recherche vorliegt.

## Übergabeformat (bindend)

Ein Block, genau diese Felder, genau diese Reihenfolge:

```
RECHERCHE-ERGEBNIS
Stand:            <Datum der Recherche>                   [Pflicht]
Firma:            <Name>                                  [Pflicht]
Verhältnis:       neukunde | bestandskunde | unbekannt    [Pflicht]
Ansprechpartner:  <Name, Rolle>                           [Optional*]
Branche/Größe:    <…>                                     [Optional]
Anlass:           <warum ausgerechnet jetzt angefragt>    [Optional]
Belegte Fakten:   <je Zeile: Fakt — Quelle>               [Pflicht, ggf. "—"]
Unbelegt:         <je Zeile: Vermutung — worauf gestützt> [Pflicht, ggf. "—"]
Nicht gefunden:   <je Zeile: wonach gesucht wurde>        [Pflicht, ggf. "—"]
```

**Die drei Listen sind das Herz dieses Vertrags:**

- **Belegte Fakten** — nur mit Quelle. Eine Zeile ohne Quelle ist ein
  Vertragsbruch, kein Schönheitsfehler. Sie gehört unter „Unbelegt".
- **Unbelegt** — Vermutungen sind erlaubt, aber sie sind gekennzeichnet.
- **Nicht gefunden** — Pflichtfeld. Eine leere Recherche ist ein **Ergebnis**,
  kein Fehler. Wer nichts findet, schreibt hin, wonach er gesucht hat. Dieses
  Feld verhindert, dass eine schwache Recherche wie eine starke aussieht.

## Was der Empfänger damit darf

Bindend für `angebots-schreiber`:

- **Block A (Kundentext) darf ausschließlich „Belegte Fakten" verwenden.**
  Kein Satz im Angebot stützt sich auf eine Vermutung.
- **„Unbelegt" darf nur Block B informieren** — als Hinweis an {{rolle}},
  nie als Aussage gegenüber dem Kunden.
- **„Nicht gefunden" mit Bezug zu einem Pflicht-Fakt löst eine Rückfrage aus**,
  gebündelt mit allen anderen Lücken in einer Nachricht.
- **`Verhältnis: unbekannt`** ist ein gültiger Wert und löst Rückfrage zu
  Pflicht-Fakt 6 aus. Es wird nicht zu „neukunde" veredelt.
- **`Ansprechpartner` ist `[Optional*]` — der Stern ist der Unterschied.**
  Optional heißt: Die Recherche muss ihn nicht liefern. Es heißt **nicht**,
  dass der `angebots-schreiber` ohne ihn weitermacht. Der Name gehört zu
  Pflicht-Fakt 1 (Wer fragt an — Firma, Ansprechpartner, Rolle). Steht er
  weder hier noch in der Anfrage, ist Fakt 1 unvollständig und löst eine
  Rückfrage aus — gebündelt mit allen anderen Lücken in derselben Nachricht.
  Für `Branche/Größe` und `Anlass` gilt das nicht: Die berühren keinen
  Pflicht-Fakt, und ihr Fehlen ist folgenlos.

## Was bei fehlenden Feldern passiert

| Fall | Reaktion |
|---|---|
| `Firma` oder `Verhältnis` fehlt | **Abbruch mit Meldung**: „Die Recherche ist unvollständig — es fehlt <Feld>. Soll ich sie neu anstoßen?" |
| Eines der drei Listenfelder fehlt ganz (nicht mal `—`) | **Abbruch mit Meldung.** Ein fehlendes „Nicht gefunden" ist nicht von einer gründlichen Recherche unterscheidbar — genau der Zustand, den dieser Vertrag ausschließt. |
| Optionales Feld fehlt (`Branche/Größe`, `Anlass`) | Weiter. Wird in Block B unter „Angenommen" nicht erwähnt, weil nichts angenommen wurde. |
| `Ansprechpartner` ist leer (`—`) oder fehlt, und steht auch nicht in der Anfrage | **Rückfrage**, gebündelt. Nicht weitermachen: Der Name gehört zu Pflicht-Fakt 1. Ohne ihn entsteht keine Anrede — und eine erfundene ist der schlimmere Fehler. |
| Recherche liegt gar nicht vor | Kein Fehler. `angebots-schreiber` arbeitet allein und fragt Fakt 1 und 6 nach. |

Nie stilles Raten, nie ein Feld sinngemäß aus einem anderen ableiten.

## Testfälle für diese Schnittstelle

`core/testfaelle/ketten/01-recherche-fast-leer.md`
