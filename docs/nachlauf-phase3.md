# Nachlauf Phase 3 — die fünf `angebots-schreiber`-Fälle, je drei Läufe

Stand: 19.08.2026. Diese Datei wird **nach jedem einzelnen Fall**
fortgeschrieben, committet und gepusht. Bricht die Sitzung ab, steht der Stand
hier — nicht im Kopf einer Sitzung (Bauprinzip 2). Die nächste Sitzung liest
den Abschnitt „Fortschritt" und macht beim ersten offenen Fall weiter.

## Warum dieser Lauf

Anforderung 2 und 3 aus Phase 3 haben **genau einen** Skill geändert:
`angebots-schreiber` (Unterlagen als Quelle, Preisregeln in Prozess-Schritt 4,
Feld `Preisstand` in Block B, neun neue Checklistenpunkte). Damit sind die drei
bestehenden Fälle gegen eine Fassung gemessen, die es nicht mehr gibt. Dazu
kommen zwei neue Fälle, die die Preisregeln überhaupt erst prüfen:
`04-preisgrundlage-abgelaufen` (Regel 2) und `05-kundenkondition-vorrang`
(Regel 3).

Nicht Teil dieses Laufs, aber weiter offen: die beiden `ketten`-Fälle und die
drei `follow-up-generator`-Fälle aus dem Nachlauf-Abschnitt in
`docs/STATUS-BAU.md`. Sie stehen dort unverändert als offen.

## Bestanden heißt 3 von 3

Jeder Fall läuft dreimal. Bestanden nur, wenn alle drei Läufe `bestanden`
ergeben. Weichen die Urteile voneinander ab, lautet das Ergebnis **wackelt** —
ein eigenes Ergebnis, kein „im Zweifel bestanden".

## Methode

Unverändert übernommen aus `docs/vollregression-phase2.md`, damit die Zahlen
vergleichbar bleiben:

1. **Zerlegung.** Jeder Testfall maschinell geschnitten in `## Eingabe` und
   Kriterienteil. Maschinell geprüft, dass im Eingabeteil weder
   „Soll-Ergebnis" noch „Prüft:" noch „Bewertung" steht.
2. **Erzeugung.** Der ausführende Lauf bekommt Skill, die bindenden Regelwerke
   (`preisregeln.md`, `aufbau.md`, beide Verträge), Testprofil, die
   Preisunterlagen als **echte Dateien** und **nur den Eingabeteil**.
   `core/testfaelle/`, `docs/` und frühere Läufe sind gesperrt.
3. **Bewertung.** Ein getrennter Lauf bekommt **nur** Kriterien und die eine zu
   bewertende Ausgabe — ohne Skill-Text, ohne Eingabe, ohne Kenntnis früherer
   Urteile desselben Falls.
4. Kein Testfall wird angefasst. Befunde gehen in den Skill, nicht ins
   Kriterium.

**Neu gegenüber Phase 2: die Preisunterlagen liegen als Dateien vor**, nicht
als Beschreibung im Auftrag. Fall 04 bekommt einen `preise/`-Ordner mit genau
einer Datei `preisliste-2025-10.md` (`Stand: 15.10.2025`, kein `gültig bis`),
Fall 05 die gültige Liste plus
`preise/kunden/nordwerk-armaturen/rahmenvertrag-2026.md`. Der Skill muss den
Stand also wirklich aus einer Datei ermitteln, statt ihn vorgesagt zu bekommen.
Das ist der Punkt, an dem Regel 2 hält oder nicht.

## Fortschritt

| Fall | Stand |
|---|---|
| `01-rueckfrage-disziplin` | offen |
| `02-budget-konflikt` | offen |
| `03-verbots-kollision` | offen |
| `04-preisgrundlage-abgelaufen` | offen |
| `05-kundenkondition-vorrang` | offen |

## Ergebnis

| Fall | Lauf 1 | Lauf 2 | Lauf 3 | Ergebnis |
|---|---|---|---|---|
| — | — | — | — | — |

## Die einzelnen Fälle

<!-- Ein Fall, ein Block. Wird nach jedem Fall ergänzt. -->
