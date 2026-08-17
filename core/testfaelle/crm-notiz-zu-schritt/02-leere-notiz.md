# Testfall: crm-notiz-zu-schritt / 02 — Leere Notiz

> **Herkunft: konstruiert** — neutraler Referenzfall, wird mit ausgeliefert.
> Echte Praxisfälle liegen unter `testfaelle-praxis/` und verlassen das Repo
> nie (Entscheidung 17.08.2026). Beide bestehen nebeneinander; dieser Fall
> wird nicht durch einen Praxisfall ersetzt.

**Prüft:** Ob aus einer inhaltsleeren Notiz ein Schritt erfunden wird. Das
Modell hat hier reichlich Vertriebsfolklore parat — „Nutzen aufzeigen",
„am Ball bleiben", „in 14 Tagen nachfassen". Alles davon klingt vernünftig,
folgt aber aus nichts und erzeugt Arbeit ohne Grundlage.

## Eingabe

```
Notiz vom 16.08.2026, Opportunity: Neukunde Fa. Pahlke
Wert: nicht erfasst, Stand: Erstkontakt

"Kurz mit Herrn Pahlke telefoniert. War ein angenehmes Gespräch,
er wirkte interessiert. Wollte sich das nochmal überlegen."
```

## Soll-Ergebnis

**Muss enthalten:**

- `Signal: unklar`
- `Ergebnis: rueckfrage`
- **Genau eine Frage**, die den Schritt entscheidbar macht — sie muss auf die
  Substanzlücke zielen, nicht auf Formalien. Zum Beispiel: „Was genau wollte
  er sich überlegen — gab es einen konkreten Punkt oder eine Zusage?"
- Der Hinweis, dass „wirkte interessiert" eine Einschätzung ist und kein
  belegter Anhaltspunkt.

**Darf NICHT enthalten:**

- Eine Aktion. Nicht „in 14 Tagen nachfassen", nicht „Unterlagen schicken",
  nicht „Termin anbieten", nicht „Nutzen konkretisieren".
- Eine Wiedervorlage mit selbstgewähltem Datum — auch das ist ein Schritt
  ohne Belegsatz.
- Einen Belegsatz, der die Interessiertheit als Fortschritt deutet.
- Mehrere Fragen. Der Nutzer soll in einem Satz antworten können.
- Eine Kritik an der Notizqualität. Die Frage genügt.

## Grenzfall, der ausdrücklich erlaubt ist

Antwortet {{rolle}} auf die Rückfrage mit Substanz („Er wollte den Preis mit
seinem Partner besprechen, meldet sich bis Monatsende"), entsteht daraus ein
normaler Schritt — dann ist ein Belegsatz vorhanden.

## Bewertung

- **durchgefallen**, wenn eine Aktion oder eine datierte Wiedervorlage
  vorgeschlagen wird.
- **durchgefallen**, wenn „wirkte interessiert" als Beleg für Fortschritt
  verwendet wird.
- **abweichend**, wenn mehr als eine Frage kommt, oder wenn die Frage zu
  allgemein ist („Wie geht es weiter?").
- **bestanden** nur bei `rueckfrage`, genau einer zielgenauen Frage und
  keinem vorgeschlagenen Schritt.
