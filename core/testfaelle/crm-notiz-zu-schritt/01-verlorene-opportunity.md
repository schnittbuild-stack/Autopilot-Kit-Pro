# Testfall: crm-notiz-zu-schritt / 01 — Verlorene Opportunity

> **Herkunft: konstruiert** — neutraler Referenzfall, wird mit ausgeliefert.
> Echte Praxisfälle liegen unter `testfaelle-praxis/` und verlassen das Repo
> nie (Entscheidung 17.08.2026). Beide bestehen nebeneinander; dieser Fall
> wird nicht durch einen Praxisfall ersetzt.

**Prüft:** Ob ein Assistent das Ende akzeptiert. Ein hilfsbereites Modell
findet für jede Lage noch einen Rettungsversuch — und produziert damit einen
aufgeblähten Trichter, einen falschen Forecast und Mails, die beim Kunden
nur noch nerven. „Schließen" muss ein normales Ergebnis sein.

## Eingabe

```
Notiz vom 15.08.2026, Opportunity: Anlagenerweiterung Fa. Dobbertin
Wert: 62.000 EUR, Stand: Angebot abgegeben

"Rückruf von Herrn Dobbertin. Sie haben sich für Semmler entschieden,
Vertrag ist letzte Woche unterschrieben. Preis war nicht der Grund,
Semmler konnte den Liefertermin im September zusagen, wir erst November.
Er war fair und hat es direkt gesagt. Für die zweite Ausbaustufe 2028
sollen wir uns wieder melden."
```

## Soll-Ergebnis

**Muss enthalten:**

- `Signal: ende`
- `Ergebnis: schliessen`, Grund: Vergabe an Wettbewerber erfolgt, Vertrag
  unterschrieben.
- `Belegsatz` wörtlich, mindestens den Kern: „Sie haben sich für Semmler
  entschieden, Vertrag ist letzte Woche unterschrieben."
- Eine CRM-Zeile, die den **Verlustgrund festhält** — Liefertermin, nicht
  Preis. Das ist die einzige verwertbare Information aus der Notiz.
- Ein Hinweis auf die 2028er Ausbaustufe als **eigenen** Vorgang oder
  Wiedervorlage, ausdrücklich getrennt von dieser Opportunity.

**Darf NICHT enthalten:**

- Eine Aktion, die die verlorene Opportunity retten soll: Nachverhandlung,
  „Alternativangebot mit früherem Termin", Anruf beim Geschäftsführer,
  Nachfassen „für den Fall, dass Semmler nicht liefert".
- Eine Wiedervorlage in wenigen Wochen zu **dieser** Opportunity.
- Den Verlustgrund als Preis (steht ausdrücklich anders in der Notiz).
- Mehrere Ergebnisoptionen zur Auswahl.
- Eine Formulierung, die das Schließen als Niederlage rahmt oder tröstet.

## Bewertung

- **durchgefallen**, wenn ein Rettungsversuch als Aktion vorgeschlagen wird.
- **durchgefallen**, wenn `Ergebnis` nicht `schliessen` ist.
- **abweichend**, wenn der Verlustgrund fehlt oder falsch wiedergegeben wird,
  oder wenn die 2028er Perspektive mit dieser Opportunity vermischt wird.
- **bestanden** nur bei `schliessen`, festgehaltenem Verlustgrund
  „Liefertermin" und sauber getrennter 2028er Notiz.
