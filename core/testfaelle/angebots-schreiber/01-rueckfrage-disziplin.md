# Testfall: angebots-schreiber / 01 — Rückfrage-Disziplin

> **Herkunft: konstruiert** — neutraler Referenzfall, wird mit ausgeliefert.
> Echte Praxisfälle liegen unter `testfaelle-praxis/` und verlassen das Repo
> nie (Entscheidung 17.08.2026). Beide bestehen nebeneinander; dieser Fall
> wird nicht durch einen Praxisfall ersetzt.

**Prüft:** Ob eine lange, freundliche, detailreiche Anfrage darüber hinweg-
täuscht, dass zwei Pflicht-Fakten fehlen. Das ist der häufigste Realfehler:
Umfang wird mit Vollständigkeit verwechselt.

## Eingabe

```
Von:      b.kessler@[kunde].de
Betreff:  Anfrage Schulung Vertriebsteam

Hallo Frau/Herr [Nutzer],

wir hatten uns ja im Frühjahr auf der Messe in Hannover kurz unterhalten —
Sie hatten mir Ihre Karte gegeben. Ich komme jetzt darauf zurück.

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
- Ton nach {{tonalitaet}}, Anrede nach {{anrede}}, Abschluss {{signatur}}.

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

## Bewertung

bestanden / abweichend / durchgefallen — je Kriterium ein Satz Begründung.

- **durchgefallen**, wenn ein Angebot erzeugt wurde (egal wie gut).
- **abweichend**, wenn nur eine der beiden Lücken erkannt wurde, oder wenn
  über die zwei Fragen hinaus nach bereits Beantwortetem gefragt wird.
- **bestanden** nur bei genau zwei Fragen, beide korrekt getroffen, kein Preis.
