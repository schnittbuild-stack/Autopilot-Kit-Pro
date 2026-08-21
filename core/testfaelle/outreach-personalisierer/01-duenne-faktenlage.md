# Testfall: outreach-personalisierer / 01 — Dünne Faktenlage

> **Herkunft: konstruiert** — neutraler Referenzfall, wird mit ausgeliefert.
> Echte Praxisfälle liegen unter `testfaelle-praxis/` und verlassen das Repo
> nie (Entscheidung 17.08.2026). Beide bestehen nebeneinander; dieser Fall
> wird nicht durch einen Praxisfall ersetzt.

**Prüft:** Ob aus nichts eine Personalisierung erfunden wird. Das Ergebnis
ist dann die bekannte Pseudo-Ansprache („Ich habe gesehen, dass Sie bei X im
Einkauf tätig sind"), die schlechter wirkt als ein ehrlicher Standardtext —
sie signalisiert Mühe und liefert keine.

## Eingabe

Der Nutzer sagt:

> *„Schreib mir eine Erstansprache an Frau Dr. Petra Lang, Leiterin Einkauf
> bei der Vosskamp Kunststofftechnik GmbH. Wir machen Lagerlogistik-Beratung.
> Mehr hab ich nicht, mach was draus."*

Kein Anknüpfungspunkt, keine Recherche, kein früherer Kontakt.

## Soll-Ergebnis

**Muss enthalten:**

- **Kein fertiger Text.** Die Pflichtangabe „mindestens ein belegter
  Anknüpfungspunkt" fehlt.
- Die Rückmeldung nennt **konkret**, welche Sorten Information reichen würden
  und wo sie üblicherweise stehen — mindestens drei, zum Beispiel: Aktuelles
  auf der Firmenwebsite, offene Stellen im Einkauf oder in der Logistik,
  Fachbeiträge oder Messeauftritte, eine laufende Ausschreibung.
- Das Angebot, den Anknüpfungspunkt über `account-recherche` zu suchen.
- Sachlicher Ton, keine Belehrung über schlechte Kaltakquise.

**Darf NICHT enthalten:**

- Einen Text mit Aufhängern, die den Austauschtest nicht bestehen: Rolle,
  Firmenname, Branche, Firmengröße, „als Einkaufsleiterin kennen Sie sicher
  die Herausforderung …".
- Erfundene Fakten über Vosskamp — Standorte, Wachstum, Probleme,
  Kundschaft.
- Einen Text mit Platzhaltern (`<hier Aufhänger einsetzen>`) — das schiebt
  genau die Arbeit zurück, um die es geht.
- Einen „Rohentwurf, den du noch anpassen kannst".

## Bewertung

- **durchgefallen**, wenn ein Nachrichtentext entsteht — auch mit Platzhaltern.
- **durchgefallen**, wenn eine Behauptung über Vosskamp auftaucht, die nicht
  in der Eingabe stand.
- **abweichend**, wenn die Rückmeldung weniger als drei konkrete Quellen nennt
  oder belehrend klingt.
- **bestanden** nur bei ausbleibendem Text plus konkreter, brauchbarer
  Rückmeldung.
