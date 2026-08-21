# Testfall: ausschreibungs-analyse / 02 — Frist praktisch abgelaufen

> **Herkunft: konstruiert** — neutraler Referenzfall, wird mit ausgeliefert.
> Echte Praxisfälle liegen unter `testfaelle-praxis/` und verlassen das Repo
> nie (Entscheidung 17.08.2026). Beide bestehen nebeneinander; dieser Fall
> wird nicht durch einen Praxisfall ersetzt.

**Prüft:** Die Reihenfolge. Ein Modell arbeitet ein Dokument gern von vorn
nach hinten ab und nennt die Frist dort, wo sie im Text steht — auf Seite
drei. Der Nutzer liest bis dahin eine gründliche Analyse und erfährt zuletzt,
dass sie gegenstandslos ist. Die Frist gehört in den ersten Satz.

## Eingabe

Heute ist der **17.08.2026, 16:30 Uhr**.

Der Nutzer schickt eine achtseitige Ausschreibung und sagt: *„Schau dir das
mal an, klingt spannend."*

Relevante Stellen im Dokument:

```
Seite 1, Kopf: Ausschreibung Wartung Lüftungstechnik, Los 2
Seite 3, Ziffer 6: Angebote sind bis zum 18.08.2026, 10:00 Uhr,
                   ausschließlich über das Vergabeportal einzureichen.
                   Bieterfragen konnten bis 05.08.2026 gestellt werden.
Seite 4, Ziffer 7: Nachweise: Fachkundenachweis VDI 6022, Referenzen,
                   Unbedenklichkeitsbescheinigung Finanzamt und Krankenkasse
Seite 6: Leistungsverzeichnis, 42 Positionen
```

## Soll-Ergebnis

**Muss enthalten:**

- **Der erste Satz** nennt: Abgabe morgen um 10:00 Uhr, also rund 17 Stunden,
  davon ein Nachtabschnitt. Bieterfragen-Frist ist seit 12 Tagen abgelaufen.
- Eine ausdrückliche Bewertung dieser Lage: Portalregistrierung, drei
  beizubringende Nachweise (darunter zwei Behördenbescheinigungen, die nicht
  über Nacht kommen) und 42 Positionen sind in der Zeit nicht seriös zu
  schaffen.
- Eine **verkürzte** Analyse: K.o.-Kriterien und der Realismus der Abgabe.
  Kein vollständiger Durchgang durch alle 42 Positionen.
- Empfehlung: `nicht bieten` — mit dem ausschlaggebenden Punkt Zeit, nicht
  Eignung. Falls {{rolle}} die Nachweise bereits vorliegen hat und im Portal
  registriert ist, ausdrücklich als Rückfrage, die die Empfehlung ändern
  könnte.

**Darf NICHT enthalten:**

- Eine vollständige Analyse aller 42 Positionen, bevor die Frist genannt ist.
- Die Frist erst im Abschnitt „Formalien" oder am Ende.
- Eine Aufwandsschätzung in Personentagen, die die Restzeit ignoriert.
- Die Empfehlung `bieten`, ohne die Zeitfrage geklärt zu haben.
- Der Vorschlag, eine Bieterfrage zu stellen — die Frist dafür ist vorbei.
- Eine Fristverlängerung als Möglichkeit, wenn das Dokument sie nicht nennt.

## Bewertung

- **durchgefallen**, wenn die Frist nicht im ersten Satz steht.
- **durchgefallen**, wenn eine Bieterfrage vorgeschlagen wird.
- **abweichend**, wenn die Analyse trotz Zeitmangel in voller Länge kommt,
  oder wenn die Rückfrage nach Nachweisen und Portalzugang fehlt.
- **bestanden** nur bei Frist im ersten Satz, verkürzter Analyse und
  begründeter Empfehlung.
