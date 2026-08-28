# Testfall: angebots-schreiber / 01 — Rückfrage-Disziplin

> **Korrigiert am 18.08.2026, nach Rückfrage beim Auftraggeber:** Das
> Kriterium verlangte ursprünglich „Anrede nach {{anrede}}, Abschluss
> {{signatur}}" — sachlich falsch, weil die Rückfrage an {{rolle}} geht und
> nicht an den Kunden. Der Ton-Punkt bleibt. Siehe `docs/STATUS-BAU.md`,
> Abschnitt zur Änderungsregel für Testfälle.

> **Herkunft: konstruiert** — neutraler Referenzfall, wird mit ausgeliefert.
> Echte Praxisfälle liegen unter `testfaelle-praxis/` und verlassen das Repo
> nie (Entscheidung 17.08.2026). Beide bestehen nebeneinander; dieser Fall
> wird nicht durch einen Praxisfall ersetzt.

> **Korrigiert am 28.08.2026, nach Entscheidung des Auftraggebers:** Die
> Absenderadresse trug den maskierten Platzhalter `[kunde]`, und die Signatur nannte keine Firma.
> Damit war **Pflicht-Fakt 1** („Wer fragt an — Firma, Ansprechpartner, Rolle")
> aus der Eingabe nicht vollständig lesbar, und der Skill fragte in manchen
> Läufen zu Recht nach der Firma — was diesen Fall an einer Stelle scheitern
> ließ, die er gar nicht prüft. Die Maskierung war nie eine protokollierte
> Entscheidung; jeder andere Testfall im Repo benutzt erfundene Firmennamen.
> **Geändert wurde ausschließlich die Eingabe** (Domain und Firmenzeile in der Signatur). Soll-Teil und
> Bewertung sind Wort für Wort unverändert. Hintergrund in
> `docs/berichte/testfall-widersprueche.md`.

> **Korrigiert am 28.08.2026, nach Entscheidung des Auftraggebers:** Der Fall
> verlangt **genau zwei** Fragen und begründete das damit, dass unter anderem
> das **Bestandsverhältnis** in der Mail stehe. Es stand dort nicht — es war
> nur **ableitbar** („Sie hatten mir Ihre Karte gegeben, ich komme jetzt darauf
> zurück"). Im Nachlauf vom 28.08. fragte einer von drei Läufen danach und fiel
> deshalb auf `abweichend`: **Der Fall bestrafte den, der nicht rät** — bei
> einem Produkt, dessen Versprechen genau das Gegenteil ist. Dieselbe Bauart
> wie `02-budget-konflikt` (20.08.) und `03-verbots-kollision` (28.08.).
> **Geändert wurde ausschließlich die Eingabe:** ein Halbsatz macht aus der
> Ableitung eine Angabe. Soll-Teil und Bewertung sind Wort für Wort
> unverändert — die Zählung „genau zwei" bleibt und misst jetzt wieder
> Rückfrage-Disziplin statt Schlussfolgerungsfreude.
> Hintergrund in `docs/berichte/testfall-widersprueche.md`.

**Prüft:** Ob eine lange, freundliche, detailreiche Anfrage darüber hinweg-
täuscht, dass zwei Pflicht-Fakten fehlen. Das ist der häufigste Realfehler:
Umfang wird mit Vollständigkeit verwechselt.

## Eingabe

```
Von:      b.kessler@kessler-foerderanlagen.de
Betreff:  Anfrage Schulung Vertriebsteam

Hallo Frau/Herr [Nutzer],

wir hatten uns ja im Frühjahr auf der Messe in Hannover kurz unterhalten —
Sie hatten mir Ihre Karte gegeben. Ich komme jetzt darauf zurück.
Zusammengearbeitet haben wir bisher noch nie, das wäre also das erste Mal.

Wir sind ein Familienunternehmen im Sondermaschinenbau, 140 Mitarbeitende,
davon 11 im Vertrieb (6 Außendienst, 5 Innendienst). Die Kollegen sind
technisch top, tun sich aber schwer damit, den Wert unserer Lösungen beim
Kunden zu erklären — es endet oft in einer Feature-Diskussion und danach
im Preisgespräch. Unser Geschäftsführer hat das auch schon angesprochen.

Ich stelle mir zwei Tage vor, gern bei uns im Haus, wir haben einen
Schulungsraum mit Beamer für 15 Personen. Verpflegung machen wir selbst.
Die Kollegen sind ein bodenständiger Haufen, mit Hochglanz-Folien brauchen
Sie da nicht kommen. Auf so etwas wie Rollenspiele lassen die sich aber ein,
das haben wir bei einer Sicherheitsschulung schon gemacht.

Budget ist grundsätzlich da, das kriegen wir hin.

Schicken Sie mir gern mal was zu.

Viele Grüße
Bernd Keßler
Leiter Vertrieb
Keßler Förderanlagen GmbH
```

## Soll-Ergebnis

**Muss enthalten:**

- **Kein Angebot.** Die Ausgabe ist eine Rückfrage-Nachricht, kein Entwurf.
- Genau **zwei** nummerierte Fragen, die exakt die beiden fehlenden
  Pflicht-Fakten treffen:
  - **Bis wann / Zeitraum** — die Anfrage nennt „zwei Tage" als *Dauer*,
    aber keinen Termin und keine Frist.
  - **Wozu / Zielbild** — „Wert erklären können" ist ein Symptom, kein
    messbares Ziel. Woran soll nach der Schulung erkennbar sein, dass sie
    gewirkt hat?
- Beide Fragen in **einer** Nachricht.
- Ton nach {{tonalitaet}}.

**Darf NICHT enthalten:**

- Einen Angebotsentwurf „schon mal vorab" oder „zur ersten Orientierung".
- Ein Angebot mit Platzhaltern (`<Termin>`, `TBD`) im Terminfeld.
- Eine Preisangabe oder Preisspanne — Preise fallen erst nach geklärtem Ziel.
- Mehr als zwei Fragen. Ort, Teilnehmerzahl, Raum, Verpflegung, Stilhinweis
  und Bestandsverhältnis stehen alle in der Mail. Wer danach fragt, hat
  nicht gelesen — und das kostet beim Kunden mehr Vertrauen als jede
  fehlende Zahl.
- Rückfrage nach dem Budget. „Budget ist grundsätzlich da" ist als Antwort
  auf Pflicht-Fakt 5 ausreichend, um zu starten; die konkrete Zahl gehört
  ins Angebot, nicht in die Rückfrage.
- **Eine Kundenanrede oder {{signatur}}.** Die Rückfrage geht an {{rolle}},
  nicht an den Kunden — man siezt sich nicht selbst und unterschreibt keine
  Nachricht an sich mit der eigenen Firmensignatur.

## Bewertung

bestanden / abweichend / durchgefallen — je Kriterium ein Satz Begründung.

- **durchgefallen**, wenn ein Angebot erzeugt wurde (egal wie gut).
- **abweichend**, wenn nur eine der beiden Lücken erkannt wurde, oder wenn
  über die zwei Fragen hinaus nach bereits Beantwortetem gefragt wird.
- **bestanden** nur bei genau zwei Fragen, beide korrekt getroffen, kein Preis.
