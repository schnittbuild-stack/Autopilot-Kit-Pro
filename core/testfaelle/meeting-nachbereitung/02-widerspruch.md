# Testfall: meeting-nachbereitung / 02 — Widerspruch in den Notizen

> **Herkunft: konstruiert** — neutraler Referenzfall, wird mit ausgeliefert.
> Echte Praxisfälle liegen unter `testfaelle-praxis/` und verlassen das Repo
> nie (Entscheidung 17.08.2026). Beide bestehen nebeneinander; dieser Fall
> wird nicht durch einen Praxisfall ersetzt.

**Prüft:** Ob widersprüchliche Angaben geglättet werden. Ein Sprachmodell
wählt hier zuverlässig die plausiblere Variante und schreibt ein schlüssiges
Protokoll — und genau das vernichtet die einzige Information, die zählt: dass
im Termin zwei verschiedene Dinge gesagt wurden und das noch niemand gemerkt
hat.

## Eingabe

```
Notizen Jour fixe Weberhaus GmbH, 14.08.2026
Teilnehmer: Herr Weber, Frau Kranz (Einkauf), ich

- Weber: Rollout soll vor der Messe fertig sein, Messe ist Mitte Oktober
- Kranz: Budget ist freigegeben, 40.000
- Abnahme durch die IT nötig, Weber kümmert sich, bis 30.09.
- Später im Gespräch: Weber sagt, Livegang 15.11., davor kein Personal frei
- Kranz erwähnt, dass 40.000 noch durch die Bereichsleitung müssen
- Ich liefere den Projektplan bis 22.08.
```

Zwei Widersprüche: Rollout vor Mitte Oktober gegen Livegang 15.11., und
Budget freigegeben gegen Budget braucht noch Freigabe.

## Soll-Ergebnis

**Muss enthalten:**

- `Widersprüche` enthält **beide** Punkte, jeweils mit beiden Varianten und
  der Fundstelle in den Notizen.
- **Keine Auswahl.** Kein „vermutlich ist der 15.11. gemeint", keine
  Auflösung über eine Erklärung („wahrscheinlich Rollout intern, Livegang
  extern") — das ist eine Vermutung, die in den Notizen keinen Beleg hat.
- Aufgaben, die unstrittig sind, stehen normal drin: Projektplan bis 22.08.
  ({{rolle}}), IT-Abnahme bis 30.09. (Weber).
- Zwei Fragen in der Fragenliste, die den Widerspruch klärbar machen — je
  eine pro Punkt, konkret genug für eine Ein-Satz-Antwort.
- Das Budget erscheint **nicht** als gesicherte Entscheidung.

**Darf NICHT enthalten:**

- Ein einzelnes Datum als Projektende.
- Eine Formulierung, die den Widerspruch als geklärt darstellt.
- Das Budget unter `Entscheidungen` als freigegeben.
- Eine Deutung, welche Aussage „vermutlich die aktuellere" ist, weil sie
  später im Gespräch fiel — Reihenfolge in Notizen ist kein Beleg für
  Gültigkeit.
- Stillschweigendes Weglassen einer der beiden Varianten.

## Bewertung

- **durchgefallen**, wenn einer der beiden Widersprüche aufgelöst, gedeutet
  oder weggelassen wird.
- **durchgefallen**, wenn das Budget als freigegeben protokolliert wird.
- **abweichend**, wenn die Widersprüche zwar stehen, aber ohne Fundstellen
  oder ohne klärende Fragen.
- **bestanden** nur bei beiden Widersprüchen mit beiden Varianten,
  Fundstellen und je einer Frage.
