# Testfall: meeting-nachbereitung / 01 — Weiche Zusage

> **Korrigiert am 19.08.2026, nach Entscheidung des Auftraggebers:** Die
> Bestehensbedingung lautete „**bestanden** nur bei genau einer eigenen
> Aufgabe, leerer Kundenliste, **zwei Einträgen unter `Unverbindlich`** und
> passenden Fragen" — sie zählte Einträge, statt zu prüfen, was in ihnen
> steht. Alle drei Läufe der Vollregression legten die beiden geforderten
> weichen Äußerungen korrekt unter `Unverbindlich` ab und dazu einen dritten,
> belegten Eintrag (Lindners Bedingung „Wenn das die Umrüstung halbiert, ist
> das interessant.") — und fielen für genau diese Sorgfalt durch. Das
> Kriterium prüft jetzt inhaltlich: beide weichen Äußerungen stehen unter
> `Unverbindlich`, und dort steht weder eine Zusage noch eine Aufgabe. Die
> Anzahl entscheidet nicht mehr. Kein Kriterium wurde gesenkt: Was vorher
> durchfiel, fällt weiterhin durch. Befund und Begründung in
> `docs/vollregression-phase2.md`, Abschnitt „Testfall-Befund
> `meeting-nachbereitung`"; Verfahren in `docs/STATUS-BAU.md`, Abschnitt
> „Änderungsregel für Testfälle".

> **Herkunft: konstruiert** — neutraler Referenzfall, wird mit ausgeliefert.
> Echte Praxisfälle liegen unter `testfaelle-praxis/` und verlassen das Repo
> nie (Entscheidung 17.08.2026). Beide bestehen nebeneinander; dieser Fall
> wird nicht durch einen Praxisfall ersetzt.

**Prüft:** Ob aus „wir schauen mal" eine Aufgabe mit Termin wird. Das ist der
häufigste und teuerste Protokollfehler: Der Kunde liest ein Protokoll, in dem
er Dinge zugesagt hat, die er nicht zugesagt hat — und korrigiert entweder
peinlich oder, schlimmer, gar nicht und erscheint später vertragsuntreu.

## Eingabe

```
Notizen Termin bei Lindner Verpackung, 12.08.2026
Teilnehmer: Frau Lindner (GF), Herr Osei (Produktion), ich

- Aktuelle Anlage läuft, aber Umrüstzeiten zu lang (45 min)
- Osei: "Wir könnten uns das Schnellwechselsystem ja mal ansehen."
- Lindner: "Wenn das die Umrüstung halbiert, ist das interessant."
- Ich schicke bis 19.08. eine Wirtschaftlichkeitsrechnung
- Lindner: "Das Thema zweite Schicht schauen wir uns im Herbst nochmal an."
- Osei fragt nach Referenzen aus der Lebensmittelbranche
- Lindner will vor einer Entscheidung den Betriebsrat einbinden,
  Termin dafür steht noch nicht
```

## Soll-Ergebnis

**Muss enthalten:**

- Unter `Aufgaben {{rolle}}` steht die Wirtschaftlichkeitsrechnung, bis
  19.08., mit Beleg — und keine Zeile, für die Wer, Was und Bis wann nicht
  belegt sind.
- `Zugesagt vom Kunden`: **leer oder `—`**. Der Kunde hat nichts mit Wer,
  Was und Bis wann zugesagt.
- `Unverbindlich` enthält beide weichen Äußerungen: Schnellwechselsystem
  („könnten uns das ja mal ansehen") und zweite Schicht („im Herbst nochmal
  ansehen").
- `Unklar` enthält die Referenzanfrage von Osei (verbindlich gemeint, aber
  ohne Termin und ohne klare Zuständigkeit) und die Betriebsrats-Einbindung
  (kein Termin).
- Zu jedem Unklar-Punkt eine Frage in der Fragenliste.
- `Nächster Termin: nicht vereinbart`.

**Darf NICHT enthalten:**

- Eine Aufgabe „Schnellwechselsystem prüfen" oder „Angebot zweite Schicht"
  — in keiner Liste außer `Unverbindlich`.
- Ein erfundenes Datum für die zweite Schicht („bis Ende Oktober"), abgeleitet
  aus „im Herbst".
- Die Referenzanfrage stillschweigend als eigene Aufgabe mit selbstgewähltem
  Termin.
- Einen Vorschlag für den nächsten Termin im Feld `Nächster Termin`.
- Ergänzte Themen, die nicht in den Notizen stehen (Wartungsvertrag,
  Schulung, Finanzierung).

## Bewertung

- **durchgefallen**, wenn eine der beiden weichen Äußerungen als Aufgabe
  auftaucht.
- **durchgefallen**, wenn ein Datum erfunden wird.
- **abweichend**, wenn die Referenzanfrage nicht in `Unklar` landet, oder
  wenn `Nächster Termin` einen Vorschlag enthält.
- **bestanden**, wenn alles Folgende zutrifft: Unter `Aufgaben {{rolle}}`
  steht die Wirtschaftlichkeitsrechnung und sonst nichts, `Zugesagt vom
  Kunden` ist leer, **beide weichen Äußerungen stehen unter `Unverbindlich`,
  und dort steht weder eine Zusage noch eine Aufgabe** — kein
  Verantwortlicher, kein Datum, keine Fälligkeit —, und zu jedem
  Unklar-Punkt gibt es eine passende Frage.
- **Die Anzahl der Einträge entscheidet nicht.** Weitere Einträge unter
  `Unverbindlich` sind zulässig, solange sie am Zitat aus den Notizen belegt
  sind und nichts erfinden. Eine belegte weiche Äußerung dort abzulegen,
  statt sie wegzulassen oder zur Zusage zu machen, ist das gewünschte
  Verhalten und darf nicht als Abweichung zählen.
