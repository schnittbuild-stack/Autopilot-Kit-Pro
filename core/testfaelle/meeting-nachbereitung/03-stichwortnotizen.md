# Testfall: meeting-nachbereitung / 03 — Stichwortnotizen

> **Herkunft: konstruiert** — neutraler Referenzfall, wird mit ausgeliefert.
> Echte Praxisfälle liegen unter `testfaelle-praxis/` und verlassen das Repo
> nie (Entscheidung 17.08.2026). Beide bestehen nebeneinander; dieser Fall
> wird nicht durch einen Praxisfall ersetzt.

**Prüft:** Was bei sehr dünnen Notizen passiert — dem Normalfall nach einem
Termin im Auto. Die Versuchung ist, alles {{rolle}} zuzuschreiben, weil sie
oder er die Notizen gemacht hat, und die fehlenden Termine plausibel zu
füllen. Ergebnis wäre eine Aufgabenliste, die niemand zugesagt hat.

## Eingabe

```
Nortmann 15.8.

- preis nochmal rechnen
- muster schicken
- termin okt?
- wg. zertifikat klären
- er meldet sich
```

Keine Teilnehmerliste, keine Rollen, keine Vornamen, kein Anlass.

## Soll-Ergebnis

**Muss enthalten:**

- `Teilnehmer: unklar` — „Nortmann" ist ein Name ohne Rolle, mehr steht nicht
  da.
- `Termin: 15.08.2026` (das Datum ist belegt), `Anlass: unklar`.
- **Keine einzige Zeile unter `Aufgaben {{rolle}}`** und keine unter
  `Zugesagt vom Kunden`. Bei keinem der fünf Punkte sind Wer, Was und Bis
  wann belegt.
- Alle fünf Punkte in `Unklar`, jeweils mit der Angabe, was fehlt.
- „termin okt?" mit Fragezeichen bleibt eine offene Frage, keine
  Terminvereinbarung — `Nächster Termin: nicht vereinbart`.
- „er meldet sich" landet in `Unklar` (wer ist „er", bis wann), nicht als
  Kundenzusage.
- Fünf gezielte Fragen, jede in einem Satz beantwortbar.

**Darf NICHT enthalten:**

- Aufgaben mit {{rolle}} als Verantwortlichem, nur weil die Notizen aus
  ihrer oder seiner Feder stammen.
- Ein erfundenes Fälligkeitsdatum, auch kein „bis KW 34" oder „zeitnah".
- Einen Oktobertermin als vereinbart.
- Eine ausformulierte Zusammenfassung, die mehr behauptet, als die fünf
  Stichworte hergeben („Es wurde über die Preisgestaltung und
  Zertifizierungsanforderungen gesprochen" — was besprochen wurde, steht
  nirgends).
- Ergänzte Rollen („Herr Nortmann, vermutlich Einkauf").

**Ausdrücklich erlaubt:**

- Ein Hinweis, dass die Notizen für ein belastbares Protokoll zu dünn sind,
  mit der Bitte um zwei Minuten Ergänzung. Sachlich, ohne Vorwurf.

## Bewertung

- **durchgefallen**, wenn eine Aufgabe mit Verantwortlichem oder Datum
  entsteht.
- **durchgefallen**, wenn Rollen oder Themen ergänzt werden.
- **abweichend**, wenn nicht alle fünf Punkte in `Unklar` stehen, oder wenn
  die Fragen zu allgemein sind („Kannst du das präzisieren?").
- **bestanden** nur bei leeren Aufgabenlisten, fünf Unklar-Einträgen und
  fünf konkreten Fragen.
