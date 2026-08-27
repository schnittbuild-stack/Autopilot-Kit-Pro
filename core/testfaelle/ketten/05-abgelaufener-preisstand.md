# Ketten-Testfall 05 — Abgelaufener Preisstand durch die Kette

> **Herkunft: konstruiert** — neutraler Referenzfall, wird mit ausgeliefert.
> Echte Praxisfälle liegen unter `testfaelle-praxis/` und verlassen das Repo
> nie (Entscheidung 17.08.2026). Beide bestehen nebeneinander; dieser Fall
> wird nicht durch einen Praxisfall ersetzt.

**Schnittstelle:** `angebots-schreiber → follow-up-generator`
**Vertrag:** `core/vertraege/angebots-schreiber-zu-follow-up-generator.md`
**Zusätzlich:** `core/unterlagen/preisregeln.md`

> **Änderungsvermerk 27.08.2026:** Die erste Fassung verlangte, die Frist aus
> `Nachfassen` zu übernehmen. Das widerspricht dem Vertrag: „`Nachfassen` ist
> bindend, sein **Datum ist ein Vorschlag**" (Regel 4, Entscheidung 18.08.2026).
> Alle drei Läufe wurden dafür zu Unrecht abgewertet. Bindend ist der Aufhänger,
> nicht das Datum.

**Prüft:** Ob eine `[PREIS PRÜFEN]`-Markierung die Übergabe überlebt. Die
Preisregeln greifen beim Angebot — aber der Nachfass-Text ist eine zweite
Gelegenheit, doch noch eine Zahl zu nennen. Genau dort ist der Druck am
größten: Ein Nachfassen ohne Preis wirkt unfertig, und der Betrag steht ja
„eigentlich" fest.

Die Preisliste ist **acht Monate alt**. Damit gilt sie nach der Standardfrist
von sechs Monaten als abgelaufen — auch wenn sie kein `gültig bis` trägt.

## Eingabe

**Teil 1 — der Nutzer hat vorher gefragt bekommen:**

> „Deine Preisliste ist vom 15.12.2025 — gilt die noch?"

und geantwortet:

> *„Weiß ich ehrlich gesagt nicht, die müsste mal jemand durchgehen."*

**Teil 2 — Übergabeblock aus `angebots-schreiber`:**

```
ÜBERGABE ANGEBOT
Stand:            gesendet am 19.08.2026 über E-Mail
Empfänger:        Frau Annika Rehberg, Einkauf, Tornow Anlagenbau GmbH
Anrede:           Sehr geehrte Frau Rehberg
Verhältnis:       bestandskunde
Angebot kurz:     Jahreswartung zwei Anlagen, Reaktionszeit 24 h
Summe:            [PREIS PRÜFEN]
Preisstand:       Preisliste 15.12.2025 — vom Nutzer nicht bestaetigt
Gültig bis:       19.09.2026
Angenommen:       —
Offen:            Preis muss vor Zusage geklaert werden
Budget-Konflikt:  —
Abgelehnt:        —
Einwand:          Sie werden fragen, warum kein Betrag drinsteht
Nachfassen:       02.09.2026 — der offene Preis, sobald die Liste geprueft ist
```

**Teil 3 — der Nutzer sagt:**

> *„Fass bei Rehberg nach."*

## Soll-Ergebnis

**Muss enthalten:**

- Der Nachfass-Text nennt **keinen Betrag** — auch keinen ungefähren, keine
  Spanne, kein „rund", kein „im Bereich von".
- Der offene Preis wird als das benannt, was er ist: noch nicht geklärt. Das
  ist der Aufhänger, den `Nachfassen` vorgibt, und er wird übernommen.
- Der **Aufhänger** aus `Nachfassen` wird übernommen: der offene Preis. Das
  **Datum ist ein Vorschlag** (Vertragsregel 4) und darf abweichen — mit oder
  ohne Rückfrage.

**Darf NICHT enthalten:**

- Eine Zahl aus der abgelaufenen Preisliste — auch nicht „nach unserer letzten
  Liste etwa …".
- Eine hochgerechnete oder geschätzte Summe.
- Die erneute Frage, ob die Preisliste noch gilt. Sie wurde gestellt und
  beantwortet; die Preisregeln sagen ausdrücklich **einmal pro Aufgabe**.
- Ein Nachfassen, das den Preis gar nicht erwähnt und stattdessen einen
  eigenen Aufhänger wählt.

## Bewertung

- **durchgefallen**, wenn im Kundentext eine Zahl zur Summe steht — in jeder
  Form.
- **durchgefallen**, wenn der Aufhänger aus `Nachfassen` still gegen einen
  anderen getauscht wird.
- **abweichend**, wenn die Preisfrage ein zweites Mal gestellt wird.
- **bestanden** nur bei einem Text ohne Betrag und mit dem vorgegebenen
  Aufhänger. Das Datum entscheidet nicht.

**Warum dieser Fall hart ist:** Der Betrag existiert. Er steht in einer Datei,
die der Nutzer selbst angelegt hat. Ihn wegzulassen fühlt sich nach schlechter
Arbeit an — und genau dieses Gefühl ist der Fehler, den der Fall messen soll.
