# Testfall: preisverhandlungs-sparring / 02 — Schmerzgrenze

> **Herkunft: konstruiert** — neutraler Referenzfall, wird mit ausgeliefert.
> Echte Praxisfälle liegen unter `testfaelle-praxis/` und verlassen das Repo
> nie (Entscheidung 17.08.2026). Beide bestehen nebeneinander; dieser Fall
> wird nicht durch einen Praxisfall ersetzt.

**Prüft:** Ob der gespielte Einkäufer Wissen benutzt, das seine Rolle nicht
haben kann. Der Nutzer gibt seine Schmerzgrenze für die Auswertung an — wenn
der Gegner sie dann zielgenau ansteuert, wirkt die Übung realistisch und ist
wertlos: Der Nutzer trainiert gegen einen Gegner, der seine Karten sieht, und
lernt daraus, dass Verhandeln aussichtslos ist.

## Eingabe

Rahmen, vom Nutzer gesetzt:

> *„Sparring Preisverhandlung. Ich verkaufe eine Wartungsvereinbarung für
> 24.000 EUR im Jahr. Meine Schmerzgrenze liegt bei 19.500, darunter geht es
> nicht. Einkäufer, Grad hart."*

Verlauf:

```
[Einkauf] 24.000 im Jahr ist zu viel. Wo können Sie hin?

[Nutzer] Nennen Sie mir Ihre Vorstellung.
```

## Soll-Ergebnis

**Muss enthalten:**

- Eine Forderung des Einkäufers, die **nicht** auf 19.500 zielt und nicht
  knapp darunter liegt. Ein Einkäufer, der den Ausgangspreis für zu hoch hält,
  fordert deutlich mehr Nachlass, als der Verkäufer geben kann — etwa 17.000
  oder 18.000, oder er nennt ein Budget statt einer Zahl.
- Rollentreue: nur Einkäufer-Rede, ein bis drei Sätze.
- Bei Grad „hart": knapp, Zeitdruck oder Wettbewerbsvergleich als Hebel.

**Darf NICHT enthalten:**

- Die Zahl 19.500 oder eine Zahl, die erkennbar darauf zielt (19.400, 19.600,
  „knapp unter 20").
- Jeden Hinweis darauf, dass der Einkäufer eine Grenze kennt: „Ich weiß, da
  geht noch was", „Sie haben doch sicher Luft bis …".
- Ein Ansteuern in Etappen, das am Ende punktgenau bei 19.500 landet — das
  ist derselbe Fehler, nur langsamer.
- Eine Erwähnung der Schmerzgrenze im Sparring-Teil, in welcher Form auch
  immer.

## Nachgelagert — in der Auswertung

Erst dort darf die Schmerzgrenze vorkommen: eine Zeile, wie nah der Endstand
daran lag. Vorher nie.

## Bewertung

- **durchgefallen**, wenn 19.500 oder eine erkennbar darauf zielende Zahl im
  Sparring auftaucht.
- **durchgefallen**, wenn der Einkäufer Kenntnis einer Grenze andeutet.
- **abweichend**, wenn die Forderung so nah an der Grenze liegt, dass kein
  Verhandlungsraum entsteht, oder wenn der Grad „hart" nicht erkennbar ist.
- **bestanden** nur bei einer Forderung deutlich unterhalb der Grenze, ohne
  jeden Hinweis auf Vorwissen.
