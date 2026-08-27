# Übergabeverträge

Hier liegt pro Agenten-Schnittstelle ein Vertrag (nach `_TEMPLATE_VERTRAG.md`).
Grundregel: Neue Schnittstelle → erst Vertrag, dann Agenten.
Der Watchdog testet genau diese Punkte — hier bricht Drift zuerst sichtbar.

## Hauptkette V1 (festgelegt 17.08.2026)

```
   Anfrage des Kunden
          │
          ▼
  account-recherche  ──[RECHERCHE-ERGEBNIS]──►  angebots-schreiber
                                                        │
                                                Block A ─┴─ Block B
                                                   │         │
                                            an den Kunden    │
                                                             ▼
                                                  [ÜBERGABE ANGEBOT]
                                                             │
                                                             ▼
                                                   follow-up-generator
```

Drei Schnittstellen, drei Verträge:

| Vertrag | Datei |
|---|---|
| account-recherche → angebots-schreiber | `account-recherche-zu-angebots-schreiber.md` |
| angebots-schreiber → follow-up-generator | `angebots-schreiber-zu-follow-up-generator.md` |
| account-recherche → outreach-personalisierer | `account-recherche-zu-outreach-personalisierer.md` |

**Alle drei Übergaben sind optional in eine Richtung:** `angebots-schreiber`
und `outreach-personalisierer` laufen auch ohne Recherche (fragen dann nach),
und nicht jedes Angebot geht ins Nachfassen. Was nicht optional ist: Wenn
übergeben wird, dann in diesem Format.

## Das gemeinsame Muster aller Verträge

Alle sind um dieselbe Idee gebaut — **Unwissen ist ein Wert, kein Nichts**:

- Was nicht belegt ist, wird als unbelegt gekennzeichnet und darf nicht in
  den Kundentext (`Unbelegt`, `Nicht gefunden`, `[PREIS PRÜFEN]`).
- Pflichtfelder stehen immer da, notfalls als `—`. Ein leeres Feld ist eine
  Aussage, ein fehlendes Feld ist ein Vertragsbruch — der Unterschied
  entscheidet, ob der nächste Agent rät.
- Fehlt etwas Tragendes: Abbruch mit Meldung oder Rückfrage. Nie stilles
  Weiterarbeiten.

## Namenskonvention

`<agent-a>-zu-<agent-b>.md`, kleingeschrieben, Bindestriche wie die
Skill-Dateinamen in `core/skills/`.
