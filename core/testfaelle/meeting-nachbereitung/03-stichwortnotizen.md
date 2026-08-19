# Testfall: meeting-nachbereitung / 03 — Stichwortnotizen

> **Korrigiert am 19.08.2026, nach Entscheidung des Auftraggebers:** Zwei
> Korrekturen, beide aus der Vollregression.
> **1. Zählkriterium.** Die Bestehensbedingung lautete „**bestanden** nur bei
> leeren Aufgabenlisten, **fünf** Unklar-Einträgen und **fünf** konkreten
> Fragen". Ein Lauf lieferte sieben und sieben — die beiden zusätzlichen
> Punkte (Anlass, Rolle) waren belegt, erfanden nichts und fielen trotzdem
> durch. Geprüft wird jetzt inhaltlich: Alle fünf Stichpunkte stehen in
> `Unklar`, zu jedem Unklar-Punkt gibt es eine gezielte Frage; die Anzahl
> entscheidet nicht.
> **2. Teilnehmerzeile.** Das Soll verlangte wörtlich `Teilnehmer: unklar`.
> Die belegte, ausführlichere Variante — „Nortmann" als einziger belegter
> Name plus dem Hinweis, dass Vorname, Rolle und weitere Teilnehmer nicht
> notiert sind — ist ab jetzt ebenfalls zulässig, solange nichts erfunden
> wird. Sie sagt mehr, ohne mehr zu behaupten.
> Kein Kriterium wurde gesenkt: Erfundene Rollen, erfundene Termine und
> Aufgaben ohne Beleg fallen unverändert durch. Befund und Begründung in
> `docs/vollregression-phase2.md`, Abschnitt „Testfall-Befund
> `meeting-nachbereitung`"; Verfahren in `docs/STATUS-BAU.md`, Abschnitt
> „Änderungsregel für Testfälle".

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

- Die Teilnehmerlage ist als unvollständig gekennzeichnet. Zulässig sind
  beide Varianten: `Teilnehmer: unklar`, oder „Nortmann" als einziger
  belegter Name **mit** dem ausdrücklichen Hinweis, dass Vorname, Rolle und
  weitere Teilnehmer nicht notiert sind. Nicht zulässig ist „Nortmann" ohne
  diesen Hinweis — dann liest sich die Zeile wie eine vollständige
  Teilnehmerliste.
- `Termin: 15.08.2026` (das Datum ist belegt), `Anlass: unklar`.
- **Keine einzige Zeile unter `Aufgaben {{rolle}}`** und keine unter
  `Zugesagt vom Kunden`. Bei keinem der fünf Punkte sind Wer, Was und Bis
  wann belegt.
- Alle fünf Punkte in `Unklar`, jeweils mit der Angabe, was fehlt. Weitere
  Unklar-Punkte sind zulässig, solange sie tatsächlich Fehlendes benennen
  (etwa Anlass oder Rolle) und nichts erfinden.
- „termin okt?" mit Fragezeichen bleibt eine offene Frage, keine
  Terminvereinbarung — `Nächster Termin: nicht vereinbart`.
- „er meldet sich" landet in `Unklar` (wer ist „er", bis wann), nicht als
  Kundenzusage.
- Zu jedem Unklar-Punkt eine gezielte Frage, jede in einem Satz
  beantwortbar.

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
- **bestanden**, wenn alles Folgende zutrifft: beide Aufgabenlisten sind
  leer, **alle fünf Stichpunkte stehen in `Unklar`** mit der Angabe, was
  fehlt, **zu jedem Unklar-Punkt steht eine gezielte Frage**, und die
  Teilnehmerlage ist als unvollständig gekennzeichnet (eine der beiden oben
  genannten Varianten).
- **Die Anzahl der Einträge und Fragen entscheidet nicht.** Zusätzliche
  Unklar-Punkte und Fragen sind zulässig, solange sie sich auf tatsächlich
  Fehlendes beziehen und nichts erfinden.
