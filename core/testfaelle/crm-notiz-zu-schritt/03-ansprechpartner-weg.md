# Testfall: crm-notiz-zu-schritt / 03 — Ansprechpartner weg

> **Herkunft: konstruiert** — neutraler Referenzfall, wird mit ausgeliefert.
> Echte Praxisfälle liegen unter `testfaelle-praxis/` und verlassen das Repo
> nie (Entscheidung 17.08.2026). Beide bestehen nebeneinander; dieser Fall
> wird nicht durch einen Praxisfall ersetzt.

**Prüft:** Ob der Schritt auf die tatsächliche Lage reagiert oder auf die
Vorgeschichte. Wenn der Ansprechpartner weg ist, ist die alte Beziehung
wertlos und das Angebot herrenlos — trotzdem schlägt ein Modell hier gern
„bei Herrn Vogler nachfassen" vor, weil der Name in der Historie steht.

## Eingabe

```
Notiz vom 17.08.2026, Opportunity: Rahmenvertrag Reinigung, Fa. Kelber
Wert: 34.000 EUR/Jahr, Stand: Angebot abgegeben 02.07.
Historie: 4 Kontakte mit Herrn Vogler (Objektleitung), Angebot an ihn

"Angerufen wegen Rückmeldung zum Angebot. Zentrale sagt, Herr Vogler ist
seit 1. August nicht mehr im Haus. Nachfolge sei noch nicht besetzt,
die Objektleitung mache kommissarisch Frau Sedlmayr aus der Verwaltung
mit. Durchwahl bekomme ich nicht, nur die Zentrale."
```

## Soll-Ergebnis

**Muss enthalten:**

- `Signal: stillstand` (nicht `ende` — die Opportunity lebt, nur der Kontakt
  ist weg).
- `Ergebnis: aktion` mit **Frau Sedlmayr** als Adressatin, über die Zentrale,
  mit Datum.
- Der Schritt adressiert die eigentliche Lage: Frau Sedlmayr kennt das
  Angebot vermutlich nicht — er muss also das Angebot neu einführen, nicht
  „nach dem Stand fragen".
- `Belegsatz` wörtlich zur kommissarischen Zuständigkeit.
- Ein Hinweis, dass das Angebot vom 02.07. an einen nicht mehr zuständigen
  Empfänger ging und der Vorgang deshalb faktisch neu anläuft.

**Darf NICHT enthalten:**

- Einen Schritt, der Herrn Vogler adressiert — Mail, Rückruf, Nachfassen.
- Eine erfundene Durchwahl, Mailadresse oder Vorname für Frau Sedlmayr. Die
  Notiz sagt ausdrücklich: nur über die Zentrale.
- `schliessen` — nichts in der Notiz belegt ein Ende.
- Die Annahme, Frau Sedlmayr kenne den Vorgang.
- Ein Nachfassen, das den Ton eines dritten Nachfassens hat, obwohl es für
  die neue Ansprechpartnerin der Erstkontakt ist.

## Bewertung

- **durchgefallen**, wenn der Schritt Herrn Vogler adressiert.
- **durchgefallen**, wenn Kontaktdaten für Frau Sedlmayr erfunden werden.
- **abweichend**, wenn der Schritt Frau Sedlmayr zwar adressiert, aber
  Kenntnis des Angebots voraussetzt, oder wenn das Signal auf `ende` steht.
- **bestanden** nur bei `stillstand`, Aktion Richtung Sedlmayr über die
  Zentrale und einem Schritt, der das Angebot neu einführt.
