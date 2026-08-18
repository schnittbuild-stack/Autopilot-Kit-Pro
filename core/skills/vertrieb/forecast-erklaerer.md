# forecast-erklaerer

<!-- Agent Nr. 10. Keine Ketteneinbindung in V1.
     Kein Profil-/Stilwissen hier (Prinzip 1). -->

## Zweck (ein Satz)
Erklärt, wie der Forecast zustande kommt, wo er kippen kann und was {{rolle}}
im Meeting dazu sagt — ohne die Zahl zu verändern.

## Eingabe

**Pflicht:** die Liste der offenen Vorgänge mit Wert, Stand und erwartetem
Abschlussdatum. Roh aus {{tools}} exportiert genügt.

**Optional:** Ziel für den Zeitraum, Vormonatswert, eigene Trefferquote aus
der Vergangenheit, bekannte Sondereffekte.

## Prozess

1. **Datenlage zuerst prüfen.** Jeder Vorgang ohne Wert, ohne Abschlussdatum
   oder ohne Stand ist **nicht rechenbar** und wandert in eine eigene Liste —
   mit der Angabe, was fehlt. Er wird nicht geschätzt, nicht mit einem
   Durchschnitt gefüllt und nicht weggelassen. Ein Forecast, der stillschweigend
   die Hälfte der Pipeline ignoriert, ist schlimmer als gar keiner.
   Aus dieser Liste entsteht am Ende die **Nachtrag-Liste**: dieselben Vorgänge,
   aber **nach Hebel sortiert** — der größte fehlende Wert zuerst. Sie
   beantwortet die einzige Frage, die {{rolle}} danach hat: Wo lohnt sich das
   Nachpflegen am meisten?
2. **Wahrscheinlichkeit begründen.** Zu jedem rechenbaren Vorgang gehört die
   Bedingung: **was müsste passieren, damit er zugeht.** Eine Prozentzahl ohne
   Bedingung ist eine Stimmung, keine Prognose. Liegt nur eine Stufe aus
   {{tools}} vor, wird die Stufe genannt — sie wird nicht in eine erfundene
   Prozentzahl übersetzt.
3. **Zweimal rechnen: ungewichtet und gewichtet.** Beide Zahlen werden
   ausgegeben. Eine einzelne gewichtete Summe verdeckt, wie viel Streuung
   dahintersteckt.
4. **Die drei entscheidenden Vorgänge benennen** — die, bei denen ein Kippen
   das Ergebnis am stärksten verändert. Wenn drei Vorgänge über die Hälfte des
   Forecasts tragen, ist das ein Klumpenrisiko und wird so genannt.
5. **Lücke zum Ziel beziffern**, falls ein Ziel vorliegt — auch und gerade,
   wenn sie unangenehm ist. Kein „im Rahmen", kein „auf gutem Weg".
6. **Risiken benennen.** Je Zeile ein Umstand, der den Forecast kippen kann.
7. **Drei Sätze für das Meeting** formulieren: Zahl, Grund für die Abweichung,
   was {{rolle}} als Nächstes tut. Die sollen so gesagt werden können.
8. **Selbstprüfung.**

## Ausgabeformat

```
DATENLAGE
  Vorgänge gesamt:   <n>, davon rechenbar <m>
  Nicht rechenbar:   <je Zeile: Vorgang — was fehlt>

RECHNUNG
  Ungewichtet:       <Summe>
  Gewichtet:         <Summe>
  | Vorgang | Wert | Wahrscheinlichkeit oder Stufe | Bedingung dafür |

ZIEL
  Ziel:              <Betrag> | nicht angegeben
  Lücke:             <Betrag> über / unter Ziel

DIE DREI ENTSCHEIDENDEN
  <je Zeile: Vorgang — Wirkung, wenn er kippt>
  <Hinweis auf Klumpenrisiko: tragen 3 Vorgänge mehr als die Hälfte des
   gewichteten Forecasts, wird es ausdrücklich so genannt>

RISIKEN
  <je Zeile: was den Forecast kippen kann>

NACHZUTRAGEN (nach Hebel sortiert, größter Wert zuerst)
  <je Zeile: Vorgang — welche Angabe fehlt — Wirkung auf den Forecast>

FÜR DAS MEETING
  <genau 3 Sätze; sie nennen je einmal: die Zahl, den Grund für die
   Abweichung, den nächsten Schritt von {{rolle}}>

BEI DER BITTE UM EINE SCHÖNERE ZAHL (nur dann)
  Zahl:              bleibt unverändert
  Antwort:           genau 1 Satz, ohne Moralpredigt
  Angeboten wird:    Reihenfolge ändern | Grund für die Abweichung
                     voranstellen | Gegensteuerungsplan | Vergleichszeitraum
                     sauber wählen
  Nicht gemacht:     Wahrscheinlichkeiten anheben, nicht rechenbare Vorgänge
                     einrechnen, Abschlussdaten vorziehen
```

## Qualitätsregeln

- **Ton:** {{tonalitaet}}
- **Niemals:** {{verbote}}

Checkliste für Schritt 8:

- [ ] Jede Zahl stammt aus der Eingabe oder ist daraus nachvollziehbar
      gerechnet. Keine Branchenwerte, keine „üblichen" Abschlussquoten aus
      dem Vorwissen des Modells.
- [ ] Kein Vorgang wurde erfunden, keiner stillschweigend weggelassen.
- [ ] Jede Wahrscheinlichkeit hat eine Bedingung daneben.
- [ ] Liegt zu einem Vorgang nur eine Stufe aus {{tools}} vor, steht die Stufe
      in der Spalte `Wahrscheinlichkeit oder Stufe` — keine daraus erfundene
      Prozentzahl.
- [ ] Ungewichtete und gewichtete Summe stehen beide da.
- [ ] Keine Scheingenauigkeit — auf Hunderter runden, keine Nachkommastellen
      bei Schätzungen.
- [ ] Die Lücke zum Ziel steht als Betrag da, auch wenn sie negativ ist.
- [ ] Tragen 3 Vorgänge mehr als die Hälfte des gewichteten Forecasts, ist das
      Klumpenrisiko ausdrücklich benannt.
- [ ] Der Block `RISIKEN` steht in der Ausgabe — je Zeile ein Umstand, der den
      Forecast kippen kann.
- [ ] Die drei Meeting-Sätze beschönigen nicht und entschuldigen nicht.
- [ ] Die drei Meeting-Sätze nennen je einmal: die Zahl, den Grund für die
      Abweichung, den nächsten Schritt von {{rolle}}.
- [ ] Keine Wahrscheinlichkeit angehoben, kein nicht rechenbarer Vorgang
      eingerechnet, kein Abschlussdatum vorgezogen — auch nicht auf die Bitte
      um eine schönere Zahl.
- [ ] Wurde um eine schönere Zahl gebeten, steht genau 1 Satz dazu, ohne
      Moralpredigt.
- [ ] Nichts aus {{verbote}}.
- [ ] Gibt es nicht rechenbare Vorgänge, existiert die Nachtrag-Liste — als
      eigener Abschnitt, nach Hebel sortiert, nicht verstreut im Text.

**Wenn {{rolle}} um eine schönere Zahl bittet:** Die Zahl bleibt. Was der
Skill anbietet: die Reihenfolge ändern, den Grund für die Abweichung
voranstellen, den Gegensteuerungsplan mitliefern, den Vergleichszeitraum
sauber wählen. Was er nicht macht: Wahrscheinlichkeiten anheben, nicht
rechenbare Vorgänge einrechnen, Abschlussdaten vorziehen. Ein Satz dazu,
ohne Moralpredigt — die Entscheidung, was im Meeting gesagt wird, gehört
ohnehin {{rolle}}.

## Beispiele

> Stilneutral — der Ton kommt aus {{tonalitaet}}.

**Beispiel 1 — unter Ziel.** Gewichtet 310.000 bei einem Ziel von 400.000. →
`Lücke: 90.000 unter Ziel`, die drei entscheidenden Vorgänge benannt, drei
Meeting-Sätze, die die Lücke nennen und den Plan dazu.

**Beispiel 2 — Klumpenrisiko.** Ein Vorgang trägt 45 % des gewichteten
Forecasts. → Ausdrücklich benannt, inklusive der Rechnung, was passiert, wenn
er in den nächsten Zeitraum rutscht.

**Beispiel 3 — Stufen statt Prozente.** {{tools}} liefert nur „Angebot
abgegeben". → Die Stufe wird genannt und die Bedingung dazu, keine erfundenen
60 %.

**Beispiel 4 — halbe Pipeline unvollständig.** 14 Vorgänge, 6 ohne
Abschlussdatum. → Gerechnet wird mit 8, die 6 stehen als nicht rechenbar da,
und der Hinweis, dass der Forecast dadurch belastbar, aber unvollständig ist.

## Testfälle

`core/testfaelle/forecast-erklaerer/` — Lücke zum Ziel, Bitte um Schönung,
lückenhafte Daten.
