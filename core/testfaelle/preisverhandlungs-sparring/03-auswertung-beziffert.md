# Testfall: preisverhandlungs-sparring / 03 — Auswertung beziffert

> **Herkunft: konstruiert** — neutraler Referenzfall, wird mit ausgeliefert.
> Echte Praxisfälle liegen unter `testfaelle-praxis/` und verlassen das Repo
> nie (Entscheidung 17.08.2026). Beide bestehen nebeneinander; dieser Fall
> wird nicht durch einen Praxisfall ersetzt.

**Prüft:** Ob die Auswertung Geld nennt. „Du hast zu schnell nachgegeben" ist
eine Beobachtung, die niemanden ändert. „6.500 EUR in drei Runden, ohne
Gegenwert" ändert das nächste Gespräch. Zweitens: ob Nibbling am Schluss als
solches erkannt und mitgerechnet wird — es fällt in echten Verhandlungen
regelmäßig unter den Tisch, weil es klein wirkt.

## Eingabe

Rahmen: Ausgangspreis 48.000 EUR, Sondermaschine, Grad mittel, keine
Schmerzgrenze angegeben. Sechs Runden, dann `Stopp`.

Wörtlicher Verlauf der Nutzerseite:

```
Runde 1: "Ich kann Ihnen 5 % entgegenkommen, dann sind wir bei 45.600."
Runde 2: "Gut, machen wir 44.000, aber dann ist wirklich Schluss."
Runde 3: "Was müsste denn passieren, damit wir zusammenkommen?"
Runde 4: "42.500 kann ich noch darstellen."
Runde 5: "Die Einweisung nehmen wir mit rein, das ist kein großer Aufwand."
Runde 6: "Und die Anlieferung übernehmen wir auch, dann haben wir es."
```

Bewertungslage: Endstand 42.500 plus zwei kostenlose Leistungen. Einweisung
und Anlieferung sind laut Rahmen mit 1.200 EUR und 800 EUR kalkuliert. Eine
Gegenleistung wurde nie gefordert. Runde 3 ist die einzige tragende Äußerung.
Der Einkäufer hat Salamitaktik und Nibbling eingesetzt.

## Soll-Ergebnis

**Muss enthalten:**

- `Ausgangspreis: 48.000`, `Endstand: 42.500`.
- `Verschenkt`: **7.500 EUR** — 5.500 EUR Preisnachlass plus 1.200 EUR
  Einweisung plus 800 EUR Anlieferung. Die Sachleistungen müssen mitgerechnet
  werden; sie nur zu erwähnen genügt nicht.
- Die Sätze aus Runde 1, 2, 4, 5 und 6 wörtlich unter `Was fiel` oder
  `Ohne Gegenleistung`.
- `Gegenleistungen gefordert: nein`.
- `Was trug`: Runde 3, wörtlich — die einzige Frage, die den Einkäufer zum
  Reden gebracht hätte.
- `Taktiken des Einkäufers`: Salamitaktik und Nibbling, jeweils mit einem
  Halbsatz, woran man sie erkennt.
- `Ein Satz zum Üben`: eine konkrete „wenn …, dann …"-Formulierung.

**Darf NICHT enthalten:**

- Eine Auswertung ohne Betrag, oder nur mit dem Preisnachlass ohne die
  Sachleistungen.
- Ein Lob-Sandwich oder eine Gesamtnote („insgesamt solide verhandelt").
- Die Bewertung von Runde 2 („aber dann ist wirklich Schluss") als
  Standfestigkeit — der Satz war eine Ankündigung, die in Runde 4 gebrochen
  wurde, und genau das macht ihn teuer.
- Einen eigenen Rabattvorschlag des Skills.
- Erfundene oder sinngemäß nacherzählte Zitate.

## Bewertung

- **durchgefallen**, wenn `Verschenkt` keinen Betrag nennt.
- **durchgefallen**, wenn Einweisung und Anlieferung nicht in die Summe
  eingehen.
- **durchgefallen**, wenn Runde 2 als Stärke ausgelegt wird.
- **abweichend**, wenn die Taktikliste fehlt, oder wenn Zitate nicht wörtlich
  sind.
- **bestanden** nur bei 7.500 EUR als Summe, wörtlichen Zitaten, benannten
  Taktiken und konkretem Übungssatz.
