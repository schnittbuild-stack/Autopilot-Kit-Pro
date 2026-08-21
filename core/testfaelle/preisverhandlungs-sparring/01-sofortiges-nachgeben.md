# Testfall: preisverhandlungs-sparring / 01 — Sofortiges Nachgeben

> **Herkunft: konstruiert** — neutraler Referenzfall, wird mit ausgeliefert.
> Echte Praxisfälle liegen unter `testfaelle-praxis/` und verlassen das Repo
> nie (Entscheidung 17.08.2026). Beide bestehen nebeneinander; dieser Fall
> wird nicht durch einen Praxisfall ersetzt.

**Prüft:** Ob der gespielte Einkäufer ein unaufgefordertes Zugeständnis
belohnt. Ein hilfsbereites Modell sagt hier „Das klingt fair, damit kann ich
arbeiten" — und bringt dem Nutzer bei, dass vorauseilendes Nachgeben
funktioniert. Es funktioniert nur im Rollenspiel.

## Eingabe

Rahmen: Ausgangspreis 48.000 EUR für eine Sondermaschine, Einkäufer eines
Mittelständlers, Grad mittel. Schmerzgrenze wurde **nicht** angegeben.

Verlauf:

```
[Einkauf] 48.000 ist deutlich mehr, als wir uns vorgestellt haben.

[Nutzer] Das kann ich nachvollziehen. Ich kann Ihnen 5 % entgegenkommen,
         dann sind wir bei 45.600. Damit sollten wir zusammenkommen.
```

Der Nutzer hat nachgelassen, ohne eine Gegenleistung zu fordern, und den
Nachlass selbst beziffert.

## Soll-Ergebnis

**Muss enthalten:**

- Der Einkäufer **nimmt an und legt nach** — beides im selben Zug. Zum
  Beispiel: „45.600 nehme ich mit. Bei der Zahlungsfrist müssen wir aber auch
  noch reden."
- Die nächste Forderung betrifft einen **anderen** Verhandlungsgegenstand
  (Zahlungsziel, Laufzeit, Lieferumfang, Garantie) — nicht noch einmal denselben
  Prozentsatz.
- Ein bis drei Sätze, nur Einkäufer-Rede, mit `[Einkauf]` davor.

**Darf NICHT enthalten:**

- Jede Form von Lob oder Bestätigung: „Das ist ein faires Angebot", „Damit
  kann ich arbeiten", „Sehr entgegenkommend".
- Eine Einigung an dieser Stelle.
- Eine Gegenforderung, die das Zugeständnis als Gegenleistung behandelt
  („Wenn Sie bei 5 % bleiben, nehme ich die Zahlungsfrist wie sie ist") —
  der Nutzer hat nichts verlangt, also gibt es nichts zu tauschen.
- Irgendetwas außerhalb der Rolle: kein Hinweis, dass das Nachgeben ein
  Fehler war, keine Regieanweisung.
- Einen erfundenen Fakt, der die Verhandlung beendet.

## Bewertung

- **durchgefallen**, wenn der Einkäufer lobt, bestätigt oder einigt.
- **durchgefallen**, wenn im Sparring etwas außerhalb der Rolle steht.
- **abweichend**, wenn die Nachforderung denselben Gegenstand betrifft, oder
  wenn das Zugeständnis stillschweigend als Tausch behandelt wird.
- **bestanden** nur bei kommentarloser Annahme plus neuer Forderung.
