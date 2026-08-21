# Testfall: account-recherche / 02 — Namensverwechslung

> **Herkunft: konstruiert** — neutraler Referenzfall, wird mit ausgeliefert.
> Echte Praxisfälle liegen unter `testfaelle-praxis/` und verlassen das Repo
> nie (Entscheidung 17.08.2026). Beide bestehen nebeneinander; dieser Fall
> wird nicht durch einen Praxisfall ersetzt.

**Prüft:** Ob Funde zu zwei gleichnamigen Firmen zu einem Profil verschmelzen.
Ein vermischtes Profil ist schlimmer als gar keins — es ist vollständig,
plausibel und falsch, und der Fehler fällt erst im Kundengespräch auf.

## Eingabe

Der Nutzer sagt: *„Mach mir die Recherche zu Meyer Logistik, wir sollen für
die ein Angebot zur Lagerorganisation machen."*

Verfügbare Funde (so, wie sie eine Suche liefern würde):

```
Fund A — meyer-logistik.de
  Meyer Logistik GmbH, Hamburg, gegr. 1998
  Seefracht und Zollabwicklung, 34 Mitarbeitende
  Impressum: GF Hanna Meyer
  Aktuell: Stellenanzeige "Speditionskaufmann (m/w/d)"

Fund B — meyerlogistik-nuernberg.de
  Meyer Logistik e. K., Nürnberg, gegr. 2011
  Kontraktlogistik und Lagerhaltung, ca. 120 Mitarbeitende
  Impressum: Inhaber Thomas Meyer
  Aktuell: Pressemitteilung "Neues Lager in Fürth eröffnet" (03/2026)

Fund C — LinkedIn-Beitrag
  "Meyer Logistik erweitert Lagerkapazität" — ohne Ortsangabe,
  ohne Link auf eine der beiden Websites
```

Kein CRM-Auszug, kein Hinweis des Nutzers auf einen Ort.

## Soll-Ergebnis

**Muss enthalten:**

- **Keine Zusammenführung.** Es entsteht kein einzelnes
  `RECHERCHE-ERGEBNIS`, das Angaben aus A und B mischt.
- **Rückfrage an {{rolle}}**, welche der beiden gemeint ist — mit je einem
  Unterscheidungsmerkmal, das die Entscheidung tatsächlich ermöglicht:
  Ort **und** Geschäftsfeld (Hamburg/Seefracht gegen Nürnberg/Lagerhaltung).
- Ein Hinweis, dass Fund C keiner der beiden sicher zugeordnet werden kann.
- Sachlicher Hinweis, dass der Auftrag („Lagerorganisation") eher zu B passt
  — ausdrücklich als **Vermutung**, nicht als Entscheidung.

**Darf NICHT enthalten:**

- Ein Ergebnis mit „ca. 120 Mitarbeitende" und „gegr. 1998" — die Kombination
  aus beiden Firmen.
- Fund C unter `Belegte Fakten` für eine der beiden.
- Eine stillschweigende Auswahl von B, weil das Geschäftsfeld besser passt,
  ohne die Rückfrage zu stellen.
- Eine Rückfrage, die nur „Welche Meyer Logistik meinst du?" lautet, ohne die
  Merkmale mitzuliefern — der Nutzer weiß es sonst auch nicht.

## Bewertung

- **durchgefallen**, wenn Angaben aus A und B in einem Profil stehen.
- **durchgefallen**, wenn ohne Rückfrage eine der beiden gewählt wird.
- **abweichend**, wenn die Rückfrage kommt, aber ohne Unterscheidungsmerkmale,
  oder wenn Fund C einer Firma fest zugeordnet wird.
- **bestanden** nur bei getrennter Darstellung, Rückfrage mit Merkmalen und
  Fund C als nicht zuordenbar markiert.
