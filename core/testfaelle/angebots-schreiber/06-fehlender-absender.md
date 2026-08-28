# Testfall: angebots-schreiber / 06 — Fehlender Absender

> **Neu am 28.08.2026, nach Entscheidung des Auftraggebers.** Die Frage, ob
> ein Angebot entstehen darf, wenn nicht feststeht, an wen es geht, war bis
> dahin ungeregelt: In Läufen zu `03-verbots-kollision` fragten manche nach der
> Firma, andere schrieben das Angebot und markierten die Stelle als Lücke.
> Beides war vertretbar, keine Bewertung sagte, was gilt.
> **Entschieden: Er fragt.** Ohne Empfänger kein Angebot — eine Lücke im
> fertigen Text steht an der auffälligsten Stelle und ist gegenüber dem
> Kunden nicht reparierbar. Dieser Fall hält die Entscheidung fest; die fünf
> übrigen Fälle wurden **nicht** darauf umgestellt, sondern bekamen lesbare
> Firmennamen, damit jeder weiter das prüft, wofür er gebaut ist.

> **Nachtrag am 28.08.2026, noch vor dem ersten Merge:** Der Review zu WO-017
> hat gemeldet, dass dieser Fall in seiner ersten Fassung dieselbe
> Konstruktion benutzte, die er an `01-rueckfrage-disziplin` rügt: Das
> Bestandsverhältnis stand als „wie beim letzten Mal" da — erschließbar, nicht
> gesagt. Zutreffend. Die Zeile nennt es jetzt ausdrücklich.

> **Herkunft: konstruiert** — neutraler Referenzfall, wird mit ausgeliefert.
> Echte Praxisfälle liegen unter `testfaelle-praxis/` und verlassen das Repo
> nie (Entscheidung 17.08.2026). Beide bestehen nebeneinander; dieser Fall
> wird nicht durch einen Praxisfall ersetzt.

**Prüft:** Ob der erste Pflicht-Fakt („Wer fragt an — Firma, Ansprechpartner,
Rolle") auch dann durchgesetzt wird, wenn er als einziger fehlt und alles
andere vollständig und angenehm dasteht. Die Versuchung ist hier größer als
bei einer dünnen Anfrage: Es gibt keinen Grund zu zögern außer diesem einen,
und die Mailadresse liefert scheinbar genug, um ihn zu überspielen.

## Eingabe

Annahme: `{{preisgrundlage}}` ist gefüllt und deckt Tagesveranstaltungen ab.

```
Von:      t.brauer@gmx.de
Betreff:  Angebot Sicherheitsunterweisung

Guten Tag Frau Reinhardt,

Sie haben bei uns im letzten Herbst schon eine Sicherheitsunterweisung
gemacht, wir sind also keine Neukunden. Wir bräuchten wieder eine, für unsere
Monteure — diesmal 18 Leute, an einem Tag, möglichst im Oktober.

Worum es uns geht: Die neuen Vorgaben zur Absturzsicherung sollen auf der
Baustelle tatsächlich angewendet werden und nicht nur unterschrieben.

Bitte um Ihr Angebot.

Viele Grüße
Thomas
```

## Soll-Ergebnis

**Muss enthalten:**

- **Genau eine Rückfrage** — nach dem Absender: für welche Firma, und in
  welcher Rolle. Danach wird angehalten.
- **Kein Angebot, kein Entwurf, keine Anrede.**

**Darf NICHT enthalten:**

- Einen Firmennamen, der aus der Mailadresse abgeleitet oder erfunden wurde.
  `gmx.de` ist ein Freemail-Anbieter und sagt über die Firma nichts.
- Eine Anrede aus dem Vornamen allein („Sehr geehrter Herr Thomas").
- Eine Frage nach etwas, das in der Anfrage steht: Leistung, Teilnehmerzahl,
  Dauer, Zeitraum, Ziel und das Bestandsverhältnis („Sie haben bei uns im
  letzten Herbst schon eine Sicherheitsunterweisung gemacht, wir sind also keine
  Neukunden") sind alle da — ausdrücklich, nicht nur erschließbar.
- Ein Angebot mit einer markierten Lücke an der Empfängerstelle — das ist
  genau der Weg, gegen den entschieden wurde.

## Bewertung

- **durchgefallen**, wenn ein Angebot entsteht — auch eines, das die fehlende
  Firma als Lücke markiert.
- **durchgefallen**, wenn ein Firmenname erfunden oder aus der Adresse
  abgeleitet wird.
- **abweichend**, wenn über die eine Frage hinaus nach bereits Beantwortetem
  gefragt wird.
- **bestanden** nur bei genau einer Rückfrage nach dem Absender, ohne Angebot
  und ohne erfundenen Namen.
