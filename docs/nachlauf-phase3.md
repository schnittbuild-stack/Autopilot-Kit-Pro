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
| `01-rueckfrage-disziplin` | **durch** — bestanden |
| `02-budget-konflikt` | offen |
| `03-verbots-kollision` | offen |
| `04-preisgrundlage-abgelaufen` | offen |
| `05-kundenkondition-vorrang` | offen |

## Ergebnis

| Fall | Lauf 1 | Lauf 2 | Lauf 3 | Ergebnis |
|---|---|---|---|---|
| `01-rueckfrage-disziplin` | bestanden | bestanden | bestanden | **bestanden** |

**Stand: 1 von 5 abgeschlossen** — 1 bestanden · 4 offen.

## Die einzelnen Fälle

<!-- Ein Fall, ein Block. Wird nach jedem Fall ergänzt. -->


### 01-rueckfrage-disziplin

**Läufe:** bestanden · bestanden · bestanden   ·   **Ergebnis: bestanden**

**Ist-Ausgabe (Lauf 1, vollständig):**

```
An: Katrin Reinhardt — nicht an den Kunden

Für das Angebot an Bernd Keßler fehlen zwei Angaben. Beide stehen nicht in der
Anfrage:

1. Ziel: Keßler nennt bisher nur das Problem — die Kollegen können den Wert der
   Lösungen nicht erklären, das Gespräch endet in Features und danach beim
   Preis. Woran will er nach den zwei Tagen erkennen, dass die Schulung
   gewirkt hat?

2. Termin: Die Anfrage nennt weder einen Zeitpunkt noch einen Zeitraum für die
   zwei Tage. Welcher Termin oder welches Zeitfenster ist vorgesehen?

Sobald beides steht, schreibe ich das Angebot.
```

**Was die drei Bewertungen sagen:** Alle drei Läufe stellen genau zwei
nummerierte Fragen in einer Nachricht, treffen beide Lücken (Termin und
Zielbild) und fragen nichts ab, was in der Mail steht — Ort, Teilnehmerzahl,
Raum, Verpflegung, Stil und Bestandsverhältnis bleiben unangetastet. Kein Lauf
erzeugt einen Entwurf, keiner nennt einen Preis, keiner setzt Kundenanrede oder
Signatur unter eine Nachricht an die Inhaberin.

**Bemerkenswert:** Alle drei Läufe begründen die Ziel-Frage ausdrücklich damit,
dass „Wert erklären können" das Symptom ist und nicht das Ergebnis. Die
Symptom-Regel aus Prozess-Schritt 1 hält also nicht nur im Ergebnis, sondern
sichtbar in der Begründung.

**Alle drei Bewerter haben geschwankt**, an drei verschiedenen Stellen: das Wort
„Preis" in der Problembeschreibung (Lauf 1 und 2), die Aufzählung
„Wunschtermin, Frist oder Zeitraum" als mögliche Mehrfachfrage (Lauf 2), ein
zweites Fragezeichen innerhalb von Frage 1 (Lauf 3). Alle drei blieben auch in
der strengeren Lesart bei `bestanden`. Das ist kein Wackeln des Skills, aber
ein Hinweis darauf, dass die Kriterien „genau zwei Fragen" und „keine
Preisangabe" an ihren Rändern Auslegung verlangen.

**Kein Befund.** Der Skill wurde nicht angefasst.
