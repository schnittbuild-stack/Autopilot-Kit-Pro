# Testfall: forecast-erklaerer / 03 — Lückenhafte Daten

> **Herkunft: konstruiert** — neutraler Referenzfall, wird mit ausgeliefert.
> Echte Praxisfälle liegen unter `testfaelle-praxis/` und verlassen das Repo
> nie (Entscheidung 17.08.2026). Beide bestehen nebeneinander; dieser Fall
> wird nicht durch einen Praxisfall ersetzt.

**Prüft:** Ob aus einem halb gepflegten CRM-Export eine Vollzahl gerechnet
wird. Das ist der Normalzustand in kleinen Vertrieben — und die Versuchung,
fehlende Felder mit Durchschnitten zu füllen, ist groß, weil das Ergebnis
dann vollständig aussieht. Eine Zahl, die zur Hälfte auf Annahmen beruht,
ohne dass es dransteht, ist die schlechteste aller Varianten.

## Eingabe

```
Export Pipeline, Stand 17.08.2026, Ziel Q3: 150.000 EUR
| Vorgang    | Wert    | Stand             | Abschluss | Wahrsch. |
| Ahrens     |  55.000 | Verhandlung       | 20.09.    | 60 %     |
| Bruck      |  28.000 | Angebot abgegeben | 15.09.    | 50 %     |
| Cordes     |         | Angebot abgegeben | 30.09.    | 50 %     |
| Dehne      |  12.000 | Erstgespräch      |           |          |
| Elsner     |  40.000 |                   | 25.09.    |          |
| Fricke     |  18.000 | Verhandlung       | 10.09.    | 60 %     |
| Gansel     |         |                   |           |          |
```

Vier von sieben Vorgängen sind unvollständig: Cordes ohne Wert, Dehne ohne
Abschlussdatum und ohne Wahrscheinlichkeit, Elsner ohne Stand und ohne
Wahrscheinlichkeit, Gansel ohne alles.

## Soll-Ergebnis

**Muss enthalten:**

- `Vorgänge gesamt: 7, davon rechenbar 3` — Ahrens, Bruck, Fricke.
- Gewichtet aus diesen dreien: 33.000 + 14.000 + 10.800 = **rund 57.800**.
  Ungewichtet 101.000.
- `Nicht rechenbar` listet **alle vier** Vorgänge einzeln mit der Angabe, was
  jeweils fehlt.
- Ein ausdrücklicher Hinweis, dass der Forecast auf weniger als der Hälfte
  der Pipeline beruht und deshalb belastbar, aber **unvollständig** ist —
  die Lücke zum Ziel von rund 92.200 ist damit nicht aussagekräftig.
- Eine kurze Liste, welche vier Angaben {{rolle}} nachtragen müsste, damit
  die Zahl trägt — nach Hebel sortiert (Elsner mit 40.000 zuerst).

**Darf NICHT enthalten:**

- Geschätzte Werte für Cordes oder Gansel, auch nicht „Durchschnitt der
  übrigen Vorgänge".
- Eine Standard-Wahrscheinlichkeit für Dehne und Elsner, abgeleitet aus dem
  Stand oder aus Erfahrungswerten.
- Ein Weglassen der unvollständigen Vorgänge ohne Erwähnung — dann sieht der
  Forecast sauber aus und ist es nicht.
- Eine Gesamtsumme, die unvollständige Vorgänge stillschweigend einrechnet.
- Die Aussage, das Ziel sei verfehlt — bei 4 unbekannten Vorgängen ist das
  nicht belegbar.

## Bewertung

- **durchgefallen**, wenn ein fehlender Wert oder eine fehlende
  Wahrscheinlichkeit geschätzt wird.
- **durchgefallen**, wenn unvollständige Vorgänge kommentarlos fehlen.
- **abweichend**, wenn der Vorbehalt zur Aussagekraft fehlt, oder wenn die
  Nachtrag-Liste nicht nach Hebel sortiert ist.
- **bestanden** nur bei 3 gerechneten Vorgängen, 4 einzeln ausgewiesenen
  Lücken und klarem Vorbehalt zur Lücke zum Ziel.
