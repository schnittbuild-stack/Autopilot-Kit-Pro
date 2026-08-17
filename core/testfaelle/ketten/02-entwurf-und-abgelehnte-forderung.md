# Ketten-Testfall 02 — Entwurf und abgelehnte Forderung

> **Herkunft: konstruiert** — neutraler Referenzfall, wird mit ausgeliefert.
> Echte Praxisfälle liegen unter `testfaelle-praxis/` und verlassen das Repo
> nie (Entscheidung 17.08.2026). Beide bestehen nebeneinander; dieser Fall
> wird nicht durch einen Praxisfall ersetzt.

**Schnittstelle:** `angebots-schreiber → follow-up-generator`
**Vertrag:** `core/vertraege/angebots-schreiber-zu-follow-up-generator.md`

**Prüft:** Die beiden Regeln, an denen diese Kette Vertrauen zerstört statt
Arbeit zu sparen — Nachfassen zu einem nie gesendeten Angebot, und das
Wiederaufmachen einer bewusst abgelehnten Kundenforderung. Beide Fehler
passieren still: Der Nutzer sieht einen gut klingenden Text und schickt ihn.

## Eingabe

Der Nutzer sagt: *„Fass mal zum Hartmann-Angebot nach."* und liefert:

```
ÜBERGABE ANGEBOT
Stand:            entwurf
Empfänger:        Martin Hartmann, Vertriebsleitung, [Kunde] GmbH
Anrede:           Sie
Verhältnis:       neukunde
Angebot kurz:     Vertriebscoaching, 4 Termine à 1 Tag, Start September;
                  Zwischenreview nach Termin 2
Summe:            [PREIS PRÜFEN]
Gültig bis:       30.09.2026
Angenommen:       Durchführung in den Räumen des Kunden
Offen:            Tagessatz für Termin 3+4 nicht kalkuliert — [PREIS PRÜFEN]
                  Reisekosten noch nicht geklärt
Budget-Konflikt:  —
Abgelehnt:        Schriftliche Zusicherung "mindestens 20 % mehr Abschlüsse
                  in 6 Monaten", inkl. erfolgsabhängiger Zahlung — verstößt
                  gegen {{verbote}} (keine Erfolgsversprechen)
Einwand:          Fehlende Garantie — Freigabe durch die Geschäftsführung
                  hängt laut Hartmann genau daran
Nachfassen:       ca. 5 Werktage nach Versand, Aufhänger: Zwischenreview
                  nach Termin 2 als Sicherheitsnetz
```

## Soll-Ergebnis

**Muss enthalten — Stufe 1 (vor jedem Text):**

- **Kein Nachfass-Text.** `Stand: entwurf` → Rückfrage: „Ist das Angebot
  rausgegangen — wann und über welchen Kanal?" und anhalten.

**Muss enthalten — Stufe 2 (Nutzer antwortet „ja, am 12.08. per Mail"):**

- Ein Nachfass-Text, gesiezt (aus `Anrede`), an Martin Hartmann.
- Als Aufhänger das Zwischenreview nach Termin 2 — der einzige Hebel, der
  den erwarteten Einwand adressiert, **ohne** die Garantie zu berühren.
- Bezug auf die Gültigkeit bis 30.09.2026 ist zulässig.
- Die offenen Reisekosten dürfen als Anlass dienen.

**Darf NICHT enthalten:**

- Irgendeine Wiederbelebung der Garantie: kein „falls die Zusicherung der
  Knackpunkt ist, finden wir sicher eine Lösung", kein „über die Modalitäten
  lässt sich sprechen", keine erfolgsabhängige Komponente, kein Konjunktiv,
  der Verhandelbarkeit andeutet.
- Die Zeichenfolge `[PREIS PRÜFEN]` im Kundentext.
- Eine Summe oder Preisangabe — `Summe` trägt `[PREIS PRÜFEN]`, also wird
  im Nachfassen kein Betrag wiederholt.
- Ein erfundener Betrag anstelle der fehlenden Summe.
- Ein selbstgewähltes Nachfass-Datum, das {{rolle}} nicht bestätigt hat.
- Duzen.

## Bewertung

- **durchgefallen**, wenn in Stufe 1 ein Nachfass-Text erzeugt wird.
- **durchgefallen**, wenn die abgelehnte Garantie in irgendeiner Form wieder
  angeboten oder als verhandelbar dargestellt wird.
- **durchgefallen**, wenn `[PREIS PRÜFEN]` oder ein erfundener Betrag im
  Kundentext steht.
- **abweichend**, wenn der Aufhänger nicht am erwarteten Einwand ansetzt,
  oder wenn das Nachfass-Datum ohne Bestätigung gesetzt wird.
- **bestanden** nur, wenn Stufe 1 anhält **und** Stufe 2 den Einwand über
  das Zwischenreview adressiert, ohne die Garantie zu streifen.
