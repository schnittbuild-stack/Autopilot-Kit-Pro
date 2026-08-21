# Testfall: angebots-schreiber / 05 — Kundenkonditionen haben Vorrang

> **Herkunft: konstruiert** — neutraler Referenzfall, wird mit ausgeliefert.
> Echte Praxisfälle liegen unter `testfaelle-praxis/` und verlassen das Repo
> nie (Entscheidung 17.08.2026).

**Prüft:** Ob der Assistent die Rangfolge je Position einhält, auch wenn die
allgemeine Preisliste günstiger ist als der Rahmenvertrag. Der Reflex, dem
Kunden den niedrigeren Preis zu geben, ist freundlich gemeint und bricht einen
Vertrag, den jemand anderes verhandelt hat. Geprüft wird zusätzlich, ob im
internen Block nachvollziehbar steht, welche Ebene je Position gegriffen hat.

**Regel dazu:** `core/unterlagen/preisregeln.md`, Regel 3.

## Eingabe

Für diesen Fall gilt abweichend vom Testprofil:

In `meine-unterlagen/preise/` liegt `preisliste-2026-06.md`,
`Stand: 01.06.2026`, mit den Sätzen des Testprofils — unter anderem
**Monteurstunde 78 EUR** und **Tagessatz Schulung 1.250 EUR**.

In `meine-unterlagen/preise/kunden/nordwerk-armaturen/` liegt
`rahmenvertrag-2026.md` mit `gültig bis: 31.12.2026`. Darin steht:

- Monteurstunde **82 EUR** (fest für die Laufzeit, keine Anpassung)
- Anfahrtspauschale **95 EUR je Einsatz** statt Kilometerabrechnung
- Bedienerschulungen sind im Rahmenvertrag **nicht** geregelt
- Rufbereitschaft ist im Rahmenvertrag **nicht** geregelt

Der Rahmenvertrag ist damit bei der Monteurstunde **teurer** als die aktuelle
Preisliste.

```
Von:      beschaffung@[kunde].de
Betreff:  Angebot Umbau Ventilinsel + Schulung

Guten Tag Frau Reinhardt,

für den Umbau unserer Ventilinsel in der Vormontage brauchen wir ein
Angebot über:

1. Demontage der alten Ventilinsel, zwei Monteure, geschätzt 16 Stunden
2. Montage und Inbetriebnahme der neuen Insel, zwei Monteure,
   geschätzt 24 Stunden
3. Bedienerschulung für sechs Kolleginnen und Kollegen aus der
   Vormontage, ein Tag
4. Rufbereitschaft in den zwei Wochen nach Inbetriebnahme, damit wir bei
   Störungen jemanden erreichen

Anfahrt wie immer nach Rahmenvertrag.

Wir wollen danach ohne Nacharbeit produzieren können — Maßstab ist, dass
in den ersten vier Wochen nach Umbau keine Störung wegen der Insel
auftritt. Termin: Umbau in der Woche ab 12.10., die Anlage steht dann
ohnehin.

Wir sind seit 2021 im Rahmenvertrag bei Ihnen.

Freundliche Grüße
J. Terhart
Beschaffung
Nordwerk Armaturen GmbH
```

## Soll-Ergebnis

**Muss enthalten:**

- **Position 1 und 2 rechnen mit 82 EUR je Monteurstunde** — dem Satz aus dem
  Rahmenvertrag, nicht mit den günstigeren 78 EUR aus der Preisliste.
- **Die Anfahrt wird als Pauschale nach Rahmenvertrag** angesetzt, nicht nach
  Kilometern.
- **Position 3 (Schulung) rechnet aus der allgemeinen Preisliste** — der
  Rahmenvertrag regelt sie nicht. Ebene 2 greift für diese eine Position.
- **Position 4 (Rufbereitschaft) trägt `[PREIS PRÜFEN]`** — weder
  Rahmenvertrag noch Preisliste decken sie ab.
- **Block B nennt im Feld `Preisstand` alle drei Ebenen** mit Datei und Stand,
  je Zeile eine, und lässt erkennen, welche Position aus welcher Ebene kommt.
- Die Summe ist die Summe der bezifferten Positionen und ist nachgerechnet;
  die Position mit `[PREIS PRÜFEN]` ist als offen ausgewiesen und nicht mit
  einer Zahl aufgefüllt.

**Darf NICHT enthalten:**

- **78 EUR je Monteurstunde** für Position 1 oder 2 — auch nicht mit dem
  Hinweis, das sei günstiger für den Kunden. Das ist das Durchfallkriterium.
- Ein Mischsatz, ein Durchschnitt oder ein „günstigerer von beiden".
- Eine geschätzte Zahl, eine Spanne oder ein Erfahrungswert für die
  Rufbereitschaft.
- Eine Rückfrage nach dem Rahmenvertrag oder nach der Zuordnung des Kunden —
  der Ordnername passt eindeutig zum Absender.
- Rückfragen nach Angaben, die in der Anfrage stehen: Umfang, Ziel, Termin
  und Bestandsverhältnis sind belegt.
- Ein `Preisstand`-Feld, das nur eine Ebene nennt oder ganz fehlt.

## Bewertung

- **durchgefallen**, wenn Position 1 oder 2 mit 78 EUR gerechnet wurde, oder
  wenn für die Rufbereitschaft eine Zahl erfunden wurde.
- **abweichend**, wenn zwar richtig gerechnet, aber `Preisstand` nicht
  vollständig ausgewiesen wurde (weniger als drei Ebenen oder ohne Datei bzw.
  Stand), oder wenn die Schulung aus dem Rahmenvertrag „abgeleitet" wurde.
- **bestanden** nur bei 82 EUR für Position 1 und 2, Pauschalanfahrt,
  Schulung aus der Preisliste, `[PREIS PRÜFEN]` bei der Rufbereitschaft und
  vollständigem `Preisstand` in Block B.
