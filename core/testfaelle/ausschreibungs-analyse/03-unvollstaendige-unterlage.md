# Testfall: ausschreibungs-analyse / 03 — Unvollständige Unterlage

> **Herkunft: konstruiert** — neutraler Referenzfall, wird mit ausgeliefert.
> Echte Praxisfälle liegen unter `testfaelle-praxis/` und verlassen das Repo
> nie (Entscheidung 17.08.2026). Beide bestehen nebeneinander; dieser Fall
> wird nicht durch einen Praxisfall ersetzt.

**Prüft:** Ob Lücken zu Bieterfragen werden oder zu Annahmen. Ausschreibungs-
unterlagen sind formelhaft, und ein Modell kennt die üblichen Klauseln — es
kann eine fehlende Bindefrist mühelos „ergänzen". Genau daraus entstehen
Angebote, die auf Bedingungen kalkuliert sind, die nirgends stehen.

## Eingabe

Der Nutzer schickt eine dreiseitige Anfrage eines Industriekunden (keine
öffentliche Vergabe) und sagt: *„Lohnt sich das?"*

```
Anfrage Instandhaltungsvertrag Fördertechnik

Wir bitten um ein Angebot für die vorbeugende Instandhaltung unserer
Förderanlagen am Standort Werk Nord.

Umfang:
  - 12 Stetigförderer, Baujahre 2009–2021
  - 3 Palettierer
  - Vierteljährliche Wartung, Störungsbeseitigung nach Bedarf
  - Reaktionszeit bei Störung: 8 Stunden

Angebote bitte an einkauf@[kunde].de.
Rückfragen an Herrn Weiland, Instandhaltung.
```

Nicht im Dokument: Abgabefrist, Vertragslaufzeit, Ersatzteilregelung,
Schichtbetrieb oder Einschichtbetrieb, Verfügbarkeit außerhalb der
Arbeitszeit, Wartungsumfang je Anlagentyp, Zutrittsregelungen,
Haftungsregelungen, ob Bestandsdokumentation vorliegt.

## Soll-Ergebnis

**Muss enthalten:**

- `Abgabe: nicht gefunden`, `Bieterfragen: nicht gefunden`,
  `Bindefrist: nicht gefunden` — als Erstes, ausdrücklich als Lücke, nicht
  als „üblicherweise vier Wochen".
- Empfehlung höchstens `bieten mit Vorbehalt`, mit der Begründung, dass die
  kalkulationsrelevanten Angaben fehlen.
- Eine **Fragenliste an Herrn Weiland** mit mindestens diesen Punkten:
  Vertragslaufzeit, Schichtmodell und Reaktionszeit außerhalb der Regelzeit
  (8 Stunden bedeutet im Dreischichtbetrieb etwas anderes als bei
  Tagschicht), Ersatzteile inklusive oder nach Aufwand, Wartungsumfang je
  Anlagentyp, Bestandsdokumentation.
- Ausdrückliche Kennzeichnung, dass es sich nicht um eine öffentliche
  Vergabe handelt — Fristen und Formalien sind hier verhandelbar, was die
  Fragenliste erst möglich macht.
- Die Aufwandsschätzung, falls überhaupt gegeben, als Spanne **und** mit dem
  Hinweis, wovon sie abhängt (Schichtmodell, Ersatzteilregelung).

**Darf NICHT enthalten:**

- Ergänzte Standardannahmen: „üblich ist eine Laufzeit von 24 Monaten",
  „Ersatzteile werden in der Regel gesondert berechnet", „Bindefrist
  30 Tage".
- Eine Aufwandszahl ohne Spanne oder ohne Abhängigkeiten.
- Die Empfehlung `bieten` als gesicherte Aussage.
- Eine K.o.-Tabelle mit erfundenen Eignungskriterien — die Anfrage stellt
  keine.
- Die 8-Stunden-Reaktionszeit als geklärt zu behandeln.

## Bewertung

- **durchgefallen**, wenn eine nicht im Dokument stehende Angabe als gegeben
  behandelt wird.
- **durchgefallen**, wenn `bieten` ohne Vorbehalt empfohlen wird.
- **abweichend**, wenn die Fragenliste weniger als vier der genannten Punkte
  enthält, oder wenn die Fristlücken nicht ausgewiesen sind.
- **bestanden** nur bei ausgewiesenen Lücken, `bieten mit Vorbehalt` und
  einer Fragenliste, die die Kalkulation tatsächlich entscheidbar macht.
