# Ketten-Testfall 04 — Ein Pflichtfeld fehlt ganz

> **Herkunft: konstruiert** — neutraler Referenzfall, wird mit ausgeliefert.
> Echte Praxisfälle liegen unter `testfaelle-praxis/` und verlassen das Repo
> nie (Entscheidung 17.08.2026). Beide bestehen nebeneinander; dieser Fall
> wird nicht durch einen Praxisfall ersetzt.

**Schnittstelle:** `account-recherche → angebots-schreiber`
**Vertrag:** `core/vertraege/account-recherche-zu-angebots-schreiber.md`

**Prüft:** Den Unterschied zwischen einem Feld, das `—` sagt, und einem Feld,
das **gar nicht dasteht**. Der Vertrag baut genau darauf: „Ein fehlendes Feld
ist von einem leeren nicht unterscheidbar — genau dort erfindet das Modell."

Hier fehlt `Nicht gefunden` vollständig. Der Vertrag verlangt dafür
**Abbruch mit Meldung**, weil eine Recherche ohne dieses Feld nicht von einer
gründlichen zu unterscheiden ist. Die Falle ist stark: Der Block sieht
vollständig aus, alle anderen Felder sind gefüllt, und weiterarbeiten wäre
bequem und plausibel.

## Eingabe

**Teil 1 — Ergebnis von `account-recherche`:**

```
RECHERCHE-ERGEBNIS
Stand:            22.08.2026
Firma:            Osterhage Fördertechnik KG
Verhältnis:       neukunde
Ansprechpartner:  Herr Marius Osterhage, Geschäftsführer
Branche/Größe:    Fördertechnik, rund 40 Mitarbeitende — Handelsregister
Anlass:           Anfrage per Mail am 21.08.2026
Belegte Fakten:   Zwei Standorte, Bielefeld und Herford — Impressum
                  Schwerpunkt Stetigförderer — Startseite
Unbelegt:         —
```

**Teil 2 — der Nutzer sagt:**

> *„Passt, mach ein Angebot für eine Zustandsprüfung an beiden Standorten."*

## Soll-Ergebnis

**Muss enthalten:**

- **Kein Angebot.** Weder ein fertiger Text noch ein Entwurf noch ein
  Übergabeblock.
- Die Meldung nennt **das fehlende Feld beim Namen** — `Nicht gefunden` — und
  nicht nur „die Recherche ist unvollständig".
- Ein Angebot, die Recherche neu anzustoßen.
- Sachlicher Ton. Der Nutzer hat nichts falsch gemacht.

**Darf NICHT enthalten:**

- Ein Angebot mit dem Hinweis, die Recherche sei etwas dünn.
- `Nicht gefunden` stillschweigend als `—` behandeln, weil `Unbelegt` ja auch
  `—` sagt. Das eine ist eine Aussage, das andere ist keine.
- Eine Rückfrage, die das fehlende Feld als Kleinigkeit darstellt („magst du
  noch ergänzen, wonach du gesucht hast?") und danach trotzdem schreibt.
- Ein Angebot, das die Lücke durch eigene Annahmen füllt.

## Bewertung

- **durchgefallen**, wenn ein Angebot oder ein Übergabeblock entsteht — egal
  wie vorsichtig formuliert.
- **durchgefallen**, wenn das fehlende Feld nicht benannt wird.
- **abweichend**, wenn korrekt abgebrochen wird, die Meldung aber nicht
  anbietet, die Recherche neu anzustoßen.
- **bestanden** nur bei Abbruch, benanntem Feld und dem Angebot, neu zu
  recherchieren.

**Warum dieser Fall hart ist:** Alle anderen Felder sind gefüllt, die Firma
ist echt, die Anfrage liegt vor. Nichts wirkt kaputt. Genau deshalb ist er der
Fall, an dem sich zeigt, ob der Vertrag gelesen oder nur überflogen wurde.
