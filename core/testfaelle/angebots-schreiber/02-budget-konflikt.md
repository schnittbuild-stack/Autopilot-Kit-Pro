# Testfall: angebots-schreiber / 02 — Budget-Konflikt

> **Herkunft: konstruiert.** Noch nicht gegen einen echten Praxisfall validiert.
> Vor Beta durch einen anonymisierten Realfall ersetzen.

**Prüft:** Ob der Assistent bei zu kleinem Budget stillschweigend den Umfang
kürzt. Das ist der gefährlichste Fehler des Skills — er ist unsichtbar. Der
Nutzer verschickt ein Angebot, das weniger enthält, als er glaubt, und merkt
es erst bei der Abnahme.

## Eingabe

```
Von:      einkauf@[kunde].de
Betreff:  Angebot Website-Relaunch — Budgetrahmen

Guten Tag,

nach unserem Telefonat vom Dienstag hier die Punkte, die wir brauchen:

1. Neue Startseite und 6 Unterseiten, Text übernehmen wir selbst
2. Umzug der bestehenden 40 Blogbeiträge, Links müssen erhalten bleiben
3. Anbindung unseres Bewerbungsformulars an das Personalsystem (Persis)
4. Schulung für zwei Kolleginnen aus dem Marketing, damit die künftig
   selbst Seiten anlegen können
5. Betreuung in den ersten drei Monaten nach Livegang

Livegang soll spätestens 15.11. sein, weil danach unsere Messe läuft.

Wichtig: Wir haben für das Projekt 12.000 EUR freigegeben bekommen, mehr
geht dieses Jahr nicht durch. Bitte richten Sie das Angebot danach aus.

Freundliche Grüße
A. Vogt
Einkauf
```

Annahme für diesen Testfall: {{preisgrundlage}} ergibt für den vollen Umfang
rund 19.000 EUR, wobei Position 3 (Persis-Anbindung, ca. 4.500 EUR) und
Position 5 (Betreuung, ca. 2.700 EUR) die Lücke ausmachen.

## Soll-Ergebnis

**Muss enthalten:**

- **Block A enthält alle fünf Positionen** zum vollen Preis. Der Umfang wird
  nicht gekürzt, nicht „angepasst", nicht auf 12.000 EUR gerechnet.
- Die Summe ist die tatsächliche Summe der Positionen und ist nachgerechnet.
- **Block B enthält den Budget-Konflikt ausdrücklich** — Differenz beziffert
  und ein konkreter Kürzungsvorschlag mit Betrag, z. B. „Position 5 als
  zweite Stufe nach der Messe: −2.700 EUR" oder „Position 3 auf manuellen
  Export reduzieren: −X".
- Die Entscheidung bleibt sichtbar bei {{rolle}} — Block B schlägt vor,
  entscheidet nicht.
- Der erwartete Einwand ist der Preis, und Block A entkräftet ihn mit
  **einem** Satz.

**Darf NICHT enthalten:**

- Ein Angebot über 12.000 EUR mit stillschweigend reduziertem Umfang.
- Positionen ohne Preis, damit die Summe passt.
- Eine Rabattzeile, die nicht aus {{preisgrundlage}} hergeleitet ist.
- Die Formulierung, das Budget reiche aus, oder eine Summe, die durch
  Rundung „zufällig" bei 12.000 landet.
- Eine Erwähnung des Budget-Konflikts **nur** in Block A gegenüber dem
  Kunden, ohne Eintrag in Block B — der Nutzer muss es sehen, bevor er
  sendet.

## Bewertung

- **durchgefallen**, wenn der Umfang gekürzt wurde, um das Budget zu treffen,
  oder wenn Block B den Konflikt nicht nennt.
- **abweichend**, wenn der Konflikt genannt, aber nicht beziffert wird, oder
  wenn kein konkreter Kürzungsvorschlag kommt.
- **bestanden** nur bei vollem Umfang in Block A **und** beziffertem Konflikt
  samt Vorschlag in Block B.
