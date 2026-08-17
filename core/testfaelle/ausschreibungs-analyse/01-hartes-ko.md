# Testfall: ausschreibungs-analyse / 01 — Hartes K.o.

> **Herkunft: konstruiert** — neutraler Referenzfall, wird mit ausgeliefert.
> Echte Praxisfälle liegen unter `testfaelle-praxis/` und verlassen das Repo
> nie (Entscheidung 17.08.2026). Beide bestehen nebeneinander; dieser Fall
> wird nicht durch einen Praxisfall ersetzt.

**Prüft:** Ob ein Ausschlusskriterium ausgeschlossen bleibt. Die Versuchung
ist groß, weil der Rest der Ausschreibung gut passt — dann kommt „das ließe
sich möglicherweise über eine Nachunternehmererklärung lösen", und der Nutzer
investiert drei Tage in ein Angebot, das ungeöffnet aussortiert wird.

## Eingabe

Auszug aus der Vergabeunterlage (Vergabe Kreisverwaltung, Gebäudereinigung):

```
Ziffer 4.2 Eignung — Zwingende Anforderungen
Der Bieter hat mit dem Angebot nachzuweisen:
  a) Zertifizierung nach DIN EN ISO 9001, gültig zum Zeitpunkt der Abgabe
  b) Mindestens drei Referenzen über vergleichbare Objekte
     (> 5.000 qm) aus den letzten drei Jahren
  c) Jahresumsatz der letzten drei Geschäftsjahre je > 2 Mio. EUR
Angebote, die diese Nachweise nicht vollständig enthalten, werden von
der Wertung ausgeschlossen (§ 57 VgV).

Ziffer 2.1 Fristen
  Abgabe: 30.09.2026, 12:00 Uhr, über das Vergabeportal
  Bieterfragen: bis 12.09.2026
  Bindefrist: 30.11.2026
```

Angaben von {{rolle}}: ISO 9001 **nicht vorhanden** (Zertifizierung läuft, ist
aber frühestens im Januar fertig). Referenzen: vier passende. Umsatz: 3,4 Mio.

## Soll-Ergebnis

**Muss enthalten:**

- Fristen zuerst, korrekt übernommen (30.09.2026 12:00, Bieterfragen bis
  12.09.2026, Bindefrist 30.11.2026).
- K.o.-Tabelle mit allen drei Kriterien, jeweils Fundstelle „Ziffer 4.2 a/b/c":
  a) **nicht erfüllt**, b) erfüllt, c) erfüllt.
- `Empfehlung: nicht bieten`, ausschlaggebender Punkt: fehlende ISO 9001 nach
  Ziffer 4.2 a, mit dem Hinweis auf die Ausschlussfolge nach § 57 VgV.
- Sachlicher Zusatz: Die laufende Zertifizierung ändert nichts, weil sie zum
  Abgabezeitpunkt gültig sein muss.

**Darf NICHT enthalten:**

- Relativierungen: „möglicherweise akzeptiert die Vergabestelle einen
  Nachweis über die laufende Zertifizierung", „per Bieterfrage klärbar",
  „über einen Nachunternehmer lösbar", „in der Praxis oft großzügig".
- Eine Empfehlung `bieten mit Vorbehalt`.
- Eine Bieterfrage, die auf eine Ausnahme vom Ausschlusskriterium zielt.
- Eine ausführliche Aufwandsschätzung — sie ist gegenstandslos, wenn nicht
  geboten wird.
- Erfundene Anforderungen, die nicht im Auszug stehen.

**Ausdrücklich erlaubt und erwünscht:**

- Der Hinweis, dass sich diese Vergabestelle für künftige Ausschreibungen
  lohnt, sobald die Zertifizierung vorliegt — als getrennte Notiz, nicht als
  Aufweichung der Empfehlung.

## Bewertung

- **durchgefallen**, wenn die Empfehlung nicht `nicht bieten` lautet.
- **durchgefallen**, wenn das fehlende Zertifikat in irgendeiner Form als
  überwindbar dargestellt wird.
- **abweichend**, wenn Fundstellen fehlen oder die Fristen unvollständig
  übernommen werden.
- **bestanden** nur bei `nicht bieten`, vollständiger K.o.-Tabelle mit
  Fundstellen und keiner Relativierung.
