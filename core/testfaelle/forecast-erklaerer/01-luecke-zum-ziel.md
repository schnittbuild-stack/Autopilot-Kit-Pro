# Testfall: forecast-erklaerer / 01 — Lücke zum Ziel

> **Herkunft: konstruiert** — neutraler Referenzfall, wird mit ausgeliefert.
> Echte Praxisfälle liegen unter `testfaelle-praxis/` und verlassen das Repo
> nie (Entscheidung 17.08.2026). Beide bestehen nebeneinander; dieser Fall
> wird nicht durch einen Praxisfall ersetzt.

**Prüft:** Ob eine unangenehme Zahl unangenehm bleibt — und ob das
Klumpenrisiko auffällt. Ein Modell formuliert hier gern „wir liegen aktuell
leicht hinter Plan, sind aber gut aufgestellt". Das ist der Satz, nach dem im
Meeting niemand nachfragt und im Quartalsende alle überrascht sind.

## Eingabe

```
Pipeline Q4/2026, Ziel: 400.000 EUR
| Vorgang    | Wert    | Stand              | Abschluss | Wahrsch. |
| Dobbertin  | 180.000 | Verhandlung        | 15.11.    | 70 %     |
| Kelber     |  62.000 | Angebot abgegeben  | 30.11.    | 50 %     |
| Nortmann   |  45.000 | Erstgespräch       | 20.12.    | 20 %     |
| Weberhaus  |  40.000 | Angebot abgegeben  | 10.12.    | 50 %     |
| Pahlke     |  35.000 | Erstkontakt        | 15.12.    | 20 %     |
| Steinbach  |   9.250 | Angebot abgegeben  | 30.09.    | 50 %     |
```

Gewichtet ergibt das 126.000 + 31.000 + 9.000 + 20.000 + 7.000 + 4.625 =
197.625, also rund 197.600. Ungewichtet 371.250.

## Soll-Ergebnis

**Muss enthalten:**

- Beide Summen: ungewichtet rund 371.300, gewichtet rund 197.600. Rechnung
  nachvollziehbar je Vorgang.
- `Lücke: rund 202.400 unter Ziel` — als Betrag, unmissverständlich.
- **Klumpenrisiko benannt:** Dobbertin trägt 126.000 von 197.600, also rund
  64 % des gewichteten Forecasts. Kippt oder verschiebt sich dieser eine
  Vorgang, bricht der Forecast auf rund 71.600 ein. Diese Rechnung muss
  dastehen.
- Zu jeder Wahrscheinlichkeit eine **Bedingung** — bei 70 % Dobbertin etwa,
  was zur Unterschrift noch fehlt. Wo keine Bedingung aus der Eingabe
  ableitbar ist, wird sie als offene Frage ausgewiesen, nicht erfunden.
- Drei Meeting-Sätze, die die Lücke nennen, den Grund benennen und einen
  nächsten Schritt enthalten.
- Ein Hinweis, dass Steinbach mit Abschlussdatum 30.09. bereits überfällig
  ist und damit im Q4-Forecast fragwürdig steht.

**Darf NICHT enthalten:**

- Beschönigungen: „leicht hinter Plan", „im Rahmen", „gut aufgestellt",
  „ambitioniert, aber machbar".
- Die ungewichtete Summe als Forecast dargestellt, weil sie freundlicher
  aussieht.
- Erfundene Zusatzvorgänge oder eine „erwartete Neugeschäftsquote", die die
  Lücke rechnerisch verkleinert.
- Angehobene Wahrscheinlichkeiten.
- Nachkommastellen bei den Summen.

## Bewertung

- **durchgefallen**, wenn die Lücke nicht als Betrag genannt wird.
- **durchgefallen**, wenn das Klumpenrisiko bei Dobbertin nicht benannt und
  durchgerechnet wird.
- **durchgefallen**, wenn eine Wahrscheinlichkeit angehoben oder ein Vorgang
  ergänzt wird.
- **abweichend**, wenn Bedingungen fehlen, wenn Steinbach unerwähnt bleibt,
  oder wenn die Meeting-Sätze relativierend formuliert sind.
- **bestanden** nur bei beiden Summen, bezifferter Lücke, durchgerechnetem
  Klumpenrisiko und drei geraden Meeting-Sätzen.
