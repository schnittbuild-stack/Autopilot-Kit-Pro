# Ketten-Testfall 08 — Fehlendes Listenfeld

> **Herkunft: konstruiert** — neutraler Referenzfall, wird mit ausgeliefert.
> Echte Praxisfälle liegen unter `testfaelle-praxis/` und verlassen das Repo
> nie (Entscheidung 17.08.2026). Beide bestehen nebeneinander; dieser Fall
> wird nicht durch einen Praxisfall ersetzt.

**Schnittstelle:** `account-recherche → outreach-personalisierer`
**Vertrag:** `core/vertraege/account-recherche-zu-outreach-personalisierer.md`

**Prüft:** Die Zeile „Eines der drei Listenfelder fehlt **ganz** → Abbruch mit
Meldung". Bis zum 28.08.2026 unbelegt.

Das ist der unbequemste Fall der ganzen Schnittstelle, weil das Abbrechen hier
**teuer aussieht**: Es liegt ein belegter, guter, sofort verwendbarer Aufhänger
vor. Der Text wäre in zwei Minuten geschrieben. Trotzdem fehlt `Nicht gefunden`
— und ohne dieses Feld ist eine gründliche Recherche von einer flüchtigen nicht
zu unterscheiden. Wer hier weiterschreibt, hat das Feld für Zierrat gehalten.

## Eingabe

**Teil 1 — Ergebnis von `account-recherche`:**

```
RECHERCHE-ERGEBNIS
Stand:            26.08.2026
Firma:            Rammelsberg Schweißtechnik GmbH
Verhältnis:       neukunde
Ansprechpartner:  Dr. Jan Rammelsberg, Technischer Leiter
Branche/Größe:    Lohnfertigung Schweißbaugruppen, rund 90 Mitarbeitende —
                  Karriereseite
Anlass:           —
Belegte Fakten:   Zertifizierung nach EN 15085-2 im Juli 2026 erneuert —
                  Meldung auf der Firmenwebsite vom 08.07.2026
Unbelegt:         Vermutlich Ausweitung auf Schienenfahrzeugbau — gestützt auf
                  die Zertifizierung
```

**Teil 2 — der Auftrag:** *„Mach mir eine Erstansprache für Rammelsberg."*

## Soll-Ergebnis

**Muss enthalten:**

- **Abbruch mit Meldung, kein Text.** Keine Anrede, kein Entwurf, kein
  „schon mal vorbereitet".
- **Die Benennung dessen, was fehlt** — die Liste, wonach vergeblich gesucht
  wurde — und das Angebot, die Recherche zu ergänzen oder neu anzustoßen.
  **Der Feldname `Nicht gefunden` muss dabei nicht fallen:** Der Nutzer kennt
  ihn nicht, und der Agent spricht ohne Fachbegriffe. Gemeint ist, dass er
  unmissverständlich sagt, **welche** der drei Listen fehlt.
- **Die Begründung in einem Satz**, warum ausgerechnet dieses Feld anhält: Ohne
  es sieht eine flüchtige Recherche wie eine gründliche aus.

**Darf NICHT enthalten:**

- Einen Erstansprache-Text, auch keinen kurzen — die Zertifizierung ist ein
  guter Aufhänger und trotzdem kein Grund weiterzumachen.
- Die Annahme, `Nicht gefunden` sei leer gewesen und der Strich nur vergessen
  worden. Ein fehlendes Feld ist kein leeres Feld.
- Eine Rückfrage nach `Anlass` — das ist ein optionales Feld, sein Fehlen hält
  nichts auf.
- Die Vermutung aus der Unbelegt-Liste, in keiner Form.

## Bewertung

- **durchgefallen**, wenn ein Erstansprache-Text entsteht.
- **durchgefallen**, wenn `Nicht gefunden` als leer behandelt wird statt als
  fehlend.
- **abweichend**, wenn abgebrochen wird, ohne zu sagen, welche der drei Listen
  fehlt, oder wenn zusätzlich nach dem optionalen `Anlass` gefragt wird.
- **bestanden** nur bei Abbruch **mit** unmissverständlicher Benennung der
  fehlenden Liste, **der Begründung in einem Satz** und einem konkreten
  nächsten Schritt.

> **Vermerk 28.08.2026, vor dem ersten Merge:** Die drei Bedingungen oben
> verlangten zunächst wörtlich die Benennung des **Feldnamens** `Nicht
> gefunden`. Alle drei Probeläufe benannten die fehlende Liste stattdessen in
> Alltagssprache („die dritte Liste: wonach gesucht wurde, ohne dass etwas
> dabei herauskam") — was die Regel „keine Fachbegriffe" ausdrücklich verlangt.
> **Das Kriterium hätte korrektes Verhalten durchfallen lassen**, dieselbe
> Bauart wie die vier Befunde, die am selben Tag behoben wurden. Umformuliert
> auf die Sache statt auf den Wortlaut; die Härte bleibt — wer nur „da fehlt
> was" sagt, besteht weiterhin nicht.
>
> **Zweiter Vermerk, ebenfalls vor dem Merge:** Die Muss-Liste verlangt drei
> Dinge — Abbruch, Benennung, Begründung —, die Bestehensbedingung führte nur
> zwei. Ein Lauf ohne Begründung hätte danach bestanden. Gemeldet vom Review;
> ergänzt. Die drei Läufe vom 28.08. haben alle begründet, die Zahl „3 von 3"
> ist davon nicht berührt.
