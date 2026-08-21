# Preisregeln — welcher Preis gilt, und seit wann

<!-- Plattformneutral (Prinzip 4). Quelle der Wahrheit für alle preisbildenden
     Skills. Ein Skill verweist hierher und übernimmt die Checkliste am Ende —
     er beschreibt die Regeln nicht selbst neu.
     Anforderung 3 aus BAUPLAN.md, Phase 3. -->

## Zweck (ein Satz)

Regelt, aus welcher Datei ein Preis kommt, wie alt er sein darf und was
passiert, wenn beides unklar ist — damit kein Assistent stillschweigend mit
einem Preis von vorletztem Jahr rechnet.

**Der Satz, aus dem alles folgt:** Ein veralteter Preis ist so teuer wie ein
erfundener, nur unsichtbarer. Beim erfundenen fällt wenigstens auf, dass
niemand ihn belegen kann.

## Regel 1 — Ersetzen statt pflegen

Der Nutzer pflegt keine Preisdatei. Er legt eine neue in
`meine-unterlagen/preise/`, und die alte verschwindet aus dem Weg.

Ablauf, jedes Mal, bevor gerechnet wird:

1. **Genau eine Preisdatei in `preise/`** (Unterordner `archiv/` und `kunden/`
   zählen nicht mit) → das ist die gültige. Weiter mit Regel 2.
2. **Mehrere Preisdateien** → die mit dem jüngsten Stand gilt. Alle übrigen
   werden nach `preise/archiv/` **verschoben**, nicht gelöscht, nicht
   umbenannt. Danach ein Satz an den Nutzer: „Du hattest zwei Preislisten
   drin — ich rechne mit der von <Datum> und habe die ältere ins Archiv
   gelegt."
3. **Lässt sich nicht entscheiden, welche jünger ist** (kein Stand, kein Datum
   im Dateinamen) → **nicht raten**. Einmal fragen: „In deinen Preisen liegen
   zwei Dateien — welche gilt?" Die andere wandert danach ins Archiv.
4. **Keine Preisdatei** → es gibt keine Preisgrundlage. Jede Preiszeile trägt
   `[PREIS PRÜFEN]`. Das ist ein funktionierender Zustand, kein Fehler.

**Aus `archiv/` wird nie gerechnet.** Der Ordner wird nur gelesen, wenn der
Nutzer ausdrücklich danach fragt („was galt im März?").

## Regel 2 — Gültigkeit wird geprüft

### Den Stand ermitteln

In dieser Reihenfolge, der erste Treffer gilt:

1. `gültig bis: <Datum>` in der Datei
2. `Stand: <Datum>` in der Datei
3. ein Datum im Dateinamen (`preisliste-2026-03.pdf`)
4. eine Bestätigungsnotiz in `preise/`, die **genau diese Datei** nennt
   (entsteht in Schritt „Nachfragen", siehe unten)
5. nichts davon → die Datei gilt als **ungeprüft**

### Prüfen

- `gültig bis` liegt in der Vergangenheit → **abgelaufen**
- Stand älter als `{{preisfrist}}` (Standard: 6 Monate) → **abgelaufen**
- ungeprüft → wird **wie abgelaufen** behandelt

Ein fehlendes Datum ist kein Freibrief. Genau dort, wo niemand weiß, wie alt
die Zahl ist, wird sonst am selbstverständlichsten weitergerechnet.

### Nachfragen — genau einmal

Ist die Grundlage abgelaufen oder ungeprüft, wird **nicht** stillschweigend
weitergerechnet. Eine Frage, in Alltagssprache, mit dem Datum darin:

> „Deine Preisliste ist vom 3. März — gilt die noch?"

**Einmal heißt: einmal pro Aufgabe**, nicht einmal pro Position. In einem
Angebot mit fünf Positionen wird nicht fünfmal gefragt.

Was danach passiert:

| Antwort | Folge |
|---|---|
| „ja, gilt noch" | Es wird gerechnet. Die Bestätigung wird als kurze Notiz in `preise/` abgelegt (`stand-bestaetigt-<datum>.md`, mit dem Namen der bestätigten Datei). Ein Satz an den Nutzer. Ab jetzt ist das Bestätigungsdatum der Stand, die Frist läuft neu. Eine ältere Bestätigungsnotiz wandert ins Archiv. |
| „nein" / „weiß nicht" | Jede betroffene Preiszeile trägt `[PREIS PRÜFEN]`. Es wird **nicht** geschätzt, nicht hochgerechnet, nicht „vorläufig" gerechnet. |
| keine Antwort, Abbruch | wie „weiß nicht" |

## Regel 3 — Kundenkonditionen haben Vorrang

### Die Rangfolge

Sie gilt **je Position**, nicht je Angebot. Eine Position kann aus dem
Rahmenvertrag kommen, die nächste aus der Preisliste.

```
1. Kundenkonditionen   meine-unterlagen/preise/kunden/<name>/
2. allgemeine Preisliste   meine-unterlagen/preise/
3. [PREIS PRÜFEN]
```

Zwischen 2 und 3 gibt es nichts. Kein Schätzen, kein Interpolieren, kein
„branchenüblich", keine Spanne, kein gerundeter Näherungswert.

### Den richtigen Kundenordner finden

- **Eindeutiger Treffer** zum Empfänger des Angebots → er gilt.
- **Ähnlicher, aber nicht eindeutiger Name** („Müller GmbH" gegen
  „Mueller & Partner") → **fragen**, nie zuordnen. Ein fremder Rabatt ist
  teurer als eine Rückfrage.
- **Kein Ordner** → keine Sonderkonditionen, es gilt Ebene 2. Das ist kein
  Mangel und wird nicht als Lücke gemeldet.

### Abgelaufene Kundenkonditionen

Für `kunden/<name>/` gilt Regel 2 unverändert. Ist der Rahmenvertrag
abgelaufen, wird **gefragt** — und **nicht** still auf die allgemeine
Preisliste zurückgefallen. Der stille Rückfall ist eine Preiserhöhung ohne
Ansage: Der Kunde bekommt plötzlich Listenpreise, und niemand hat es
entschieden.

## Was im internen Block steht

Jeder preisbildende Skill schreibt in seinen internen Block (Block B) das Feld
`Preisstand`. Es nennt **Ebene, Datei und Stand** — je Zeile eine Ebene:

```
Preisstand:       kundenkondition — kunden/mueller-gmbh/rahmenvertrag.md,
                  Stand 01.02.2026 (Pos. 1–2)
                  preisliste — preisliste-2026-03.pdf, Stand 03/2026 (Pos. 3)
                  keine — [PREIS PRÜFEN] (Pos. 4)
```

Weitere zulässige Formen:

- `Preisstand:  preisliste — preisliste-2026-03.pdf, Stand 03/2026`
  (eine Ebene für alles)
- `Preisstand:  preisliste — preisliste.pdf, Stand am 19.08.2026 bestätigt`
  (nach einer Rückfrage nach Regel 2)
- `Preisstand:  keine — keine Preisdatei hinterlegt, alle Zeilen [PREIS PRÜFEN]`
- `Preisstand:  —` (es wurden keine Preise gerechnet)

Das Feld ist **nur für den Nutzer**. Es steht nie in einem Kundentext, und
kein nachgelagerter Skill leitet daraus etwas ab.

## Niemals

- Eine Zahl schätzen, interpolieren oder „auf einen üblichen Wert" runden.
- „branchenüblich", „erfahrungsgemäß", „üblicherweise liegt das bei".
- Aus `angebote/` rechnen — ein alter Angebotspreis ist ein Einzelfall,
  keine Grundlage.
- Aus `preise/archiv/` rechnen.
- Mit einer abgelaufenen oder ungeprüften Grundlage rechnen, ohne die eine
  Rückfrage gestellt zu haben.
- Von einer abgelaufenen Kundenkondition still auf die Preisliste
  zurückfallen.
- Eine Preisdatei löschen, überschreiben oder inhaltlich ändern.

## Checkliste — von jedem preisbildenden Skill zu übernehmen

- [ ] Vor dem Rechnen geprüft, ob in `preise/` mehr als eine Preisdatei liegt;
      abgelöste Dateien sind nach `archiv/` verschoben und der Nutzer hat einen
      Satz dazu bekommen.
- [ ] Der Stand der benutzten Grundlage ist ermittelt (Datei, Dateiname oder
      Bestätigungsnotiz) — nicht angenommen.
- [ ] War die Grundlage abgelaufen oder ohne Datum, wurde **genau einmal**
      gefragt — nicht je Position, und nicht gar nicht.
- [ ] Nach „nein" oder „weiß nicht" trägt jede betroffene Zeile
      `[PREIS PRÜFEN]`. Keine geschätzte Zahl, keine Spanne, kein „vorläufig".
- [ ] Rangfolge je Position eingehalten: Kundenkondition → Preisliste →
      `[PREIS PRÜFEN]`. Nichts dazwischen.
- [ ] Bei ähnlichem, nicht eindeutigem Kundennamen wurde gefragt statt
      zugeordnet.
- [ ] Bei abgelaufener Kundenkondition wurde gefragt — **kein** stiller
      Rückfall auf die allgemeine Preisliste.
- [ ] `Preisstand` steht im internen Block, mit Ebene, Datei und Stand — und
      steht in keinem Kundentext.
- [ ] Keine Zahl stammt aus `angebote/` oder aus `preise/archiv/`.
