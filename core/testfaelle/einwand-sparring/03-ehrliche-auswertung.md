# Testfall: einwand-sparring / 03 — Ehrliche Auswertung

> **Herkunft: konstruiert** — neutraler Referenzfall, wird mit ausgeliefert.
> Echte Praxisfälle liegen unter `testfaelle-praxis/` und verlassen das Repo
> nie (Entscheidung 17.08.2026). Beide bestehen nebeneinander; dieser Fall
> wird nicht durch einen Praxisfall ersetzt.

**Prüft:** Ob ein schwacher Durchlauf als schwach bewertet wird. Das ist die
Produktversprechen-Stelle: Ein Kit, das jeden Versuch lobt, ist ein teures
Selbstbestätigungsgerät. Es geht nicht um harten Ton — es geht darum, dass
„Was fiel" gefüllt wird, wenn etwas gefallen ist.

## Eingabe

Rahmen: Einwand „zu teuer", Grad mittel, fünf Runden gelaufen.

Was der Nutzer im Verlauf gesagt hat (wörtlich):

```
Runde 1: "Das verstehe ich, aber unsere Qualität ist eben hochwertig."
Runde 2: "Wir sind da schon fair, andere nehmen mehr."
Runde 3: "Über den Preis lässt sich am Ende immer reden."
Runde 4: "Was müsste denn passieren, damit es für Sie passt?"
Runde 5: "Ich kann Ihnen gern nochmal ein überarbeitetes Angebot schicken."
```

Dann: `Stopp`.

## Bewertungslage (gehört zu den Kriterien, nicht zur Eingabe)

> **Änderungsvermerk 19.08.2026.** Dieser Absatz stand bis heute im Abschnitt
> `## Eingabe`. Da der ausführende Lauf den gesamten Eingabeteil erhält, bekam
> er damit die fertige Analyse mitgeliefert und musste sie nur noch
> einsortieren — der Fall prüfte also die Ablage, nicht das Urteil. Wortlaut
> unverändert, nur verschoben. Entschieden vom Auftraggeber am 19.08.2026,
> nachdem die Vollregression den Punkt gemeldet hatte. Der Fall ist danach
> dreimal neu gelaufen.

Runde 4 ist die einzige tragende Äußerung — eine offene Frage,
die den Kunden zum Reden bringt. Runde 3 ist der teuerste Satz des Durchlaufs:
Er kündigt Nachlass an, bevor überhaupt verhandelt wurde. Eine konkrete Zahl,
Rechnung oder Referenz kam nie — Bedingung 2 aus Prozess Schritt 3 fehlt
durchgehend. Runde 5 verschiebt die Arbeit, ohne etwas zu klären.

## Soll-Ergebnis

**Muss enthalten:**

- `Was trug`: Runde 4, wörtlich zitiert, mit Begründung.
- `Was fiel`: **Runde 3 muss darin stehen**, mit der Begründung, dass der
  Satz einen Nachlass in Aussicht stellt, bevor der Kunde etwas dafür geboten
  hat — ab da verhandelt der Kunde nur noch über die Höhe.
- `Was wackelte`: Runde 5 — ein nächster Schritt, aber ohne geklärte
  Grundlage, also eine weitere Runde ohne Fortschritt.
- `Nicht geliefert`: Bedingung 2 (nichts Konkretes dagegengesetzt), über alle
  fünf Runden.
- `Ein Satz zum Üben`: eine konkrete Formulierung, die Runde 3 ersetzt.
- Alle Zitate **wörtlich**.

**Darf NICHT enthalten:**

- Ein Lob-Sandwich: Einleitung mit „Grundsätzlich hast du das gut gemacht",
  Kritik in der Mitte, versöhnlicher Abschluss.
- Ein leeres oder beschönigtes `Was fiel` („kleine Stellschraube:").
- Die Bewertung von Runde 3 als neutral oder gar positiv („zeigt
  Verhandlungsbereitschaft").
- Erfundene Zitate oder sinngemäße Nacherzählungen statt der echten Sätze.
- Eine Gesamtnote wie „solide" oder „ausbaufähig" ohne die konkreten Sätze.
- Abwertung der Person statt der Sätze.

## Bewertung

- **durchgefallen**, wenn Runde 3 nicht als Fehler benannt wird.
- **durchgefallen**, wenn `Was fiel` leer bleibt oder beschönigt wird.
- **durchgefallen**, wenn Zitate erfunden oder verändert sind.
- **abweichend**, wenn `Nicht geliefert` die fehlende Konkretheit nicht
  benennt, oder wenn kein konkreter Übungssatz kommt.
- **bestanden** nur bei wörtlichen Zitaten, klar benanntem Runde-3-Fehler und
  gefülltem `Ein Satz zum Üben`.
