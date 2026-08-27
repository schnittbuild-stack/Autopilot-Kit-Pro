# Die Übergabe haltbar machen — 27.08.2026

Vier Änderungen, entstanden aus einer Frage des Auftraggebers: *Kommunizieren
die Assistenten gut miteinander, wird immer ein Übergabeprotokoll geschrieben?*

## Der Befund, der die Frage ausgelöst hat

**Die Kette war unerreichbar und flüchtig zugleich.**

- `angebots-schreiber` schreibt Block B **mit jedem Angebot** — die Übergabe
  entsteht also immer.
- `follow-up-generator` weiß genau, was er damit tut.
- **Aber nichts brachte ihn hinüber.** Kein Helfer bot den nächsten Schritt an,
  kein Satz im Gedächtnis erwähnte die Kette. Und der Käufer konnte nicht
  danach fragen: „Er kennt keine Namen von Assistenten und soll keine lernen."
- **Und keine Regel verlangte, dass Block B eine Datei erreicht.** Die eiserne
  Regel sagt „fertige Ergebnisse landen in `ergebnisse/`" — das ist der
  Kundentext. Block B ist ausdrücklich „für dich, nicht für den Kunden".

Zusammen mit der Erkenntnis aus `ketten/03` — das Nachfassen passiert Tage
später, also zwangsläufig in einer neuen Sitzung — hieß das: **Die Übergabe,
die wir vertraglich gebunden, mit fünf Fällen geprüft und in den Wochencheck
aufgenommen haben, war im Alltag weg, bevor sie gebraucht wurde.**

Was ihr Verlust kostet, ist nicht „ein paar Notizen": `Abgelehnt` (sonst macht
das Nachfassen die abgelehnte Forderung wieder auf), `Nachfassen` (sonst wählt
es einen eigenen Aufhänger), `Angenommen`, `Preisstand`, `Budget-Konflikt`.
Der Kundentext bleibt erhalten — die Begründung nicht. Der nächste Schritt
**rekonstruiert** dann aus dem Angebot, was damals galt. Das ist nicht
„Information fehlt", sondern **Information wird durch Vermutung ersetzt**.

## Was geändert wurde

**Drei Teile im Gedächtnis** (`CLAUDE.vorlage.md`), weil es Verhalten
*zwischen* Helfern ist — damit fallen die 32 Skill-Testfälle nicht in den
Nachlauf:

1. **Block B kommt mit in die Ergebnisdatei**, unter den Kundentext, mit
   Trennlinie und Überschrift `NICHT AN DEN KUNDEN`.
2. **Vermerken statt löschen.** Wer auf einem Notizblock aufgebaut hat,
   schreibt darunter, was er getan hat, wann und wo das neue Ergebnis liegt.
   Nichts in `ergebnisse/` wird gelöscht oder überschrieben — dieselbe Haltung
   wie bei den Preislisten (`preisregeln.md`).
3. **Die Fortsetzung wird angeboten, nie ungefragt gestartet.** Ein Satz,
   Alltagssprache, keine Helfernamen. Sagt er ja, nimmt der Agent den Block aus
   der Datei — **er kopiert nichts**.

**Ein Teil im Vertragswerk:** `account-recherche → outreach-personalisierer`.
Diese Übergabe fand bisher ohne Vertrag statt; der Skill hielt fest, die
Trennung gelte „sinngemäß". Prinzip 3 verlangt: erst Vertrag, dann Agenten.
Der Vertrag benutzt **dasselbe Format** — der Sender ändert sich nicht.

## Ergebnis der Prüfung

**`outreach`-Testfälle nach der Vertragsbindung: 9 von 9.** Keine Regression.

**Gedächtnisregeln, zwei Angebote im echten Kundenordner:**

| Geprüft | Ergebnis |
|---|---|
| Angebot landet in `ergebnisse/` | ✓ beide |
| Block B in derselben Datei, markiert | ✓ beide |
| Bestätigung wird in der Datei vermerkt | ✓ |
| Nichts ungefragt gestartet | ✓ nach vier Zügen weiterhin zwei Dateien |

Und die Fortsetzung kam von selbst:

> „Wenn bis zum 25. September nichts von Ostermann zurückkommt, wäre Ende
> September ein Nachfassen dran; den Aufhänger dafür habe ich schon
> festgehalten."

**Er hat sie erwähnt statt angeboten** — als Auskunft, nicht als Frage. Das
Beispiel in der Regel endet mit „Soll ich?". Hier war die Auskunft die bessere
Wahl: Das Nachfassen ist erst Ende September fällig, eine Frage hätte zu
Arbeit eingeladen, die noch gar nicht geht.

**Die Regel wurde deshalb nicht nachgeschärft.** Das Verhalten liegt innerhalb
dessen, was dasteht, und das Beispiel war die engere Variante. Eine Regel
nachzuziehen, bis sie zum Beobachteten passt, ist derselbe Fehler wie ein
Kriterium nachzuziehen, bis der Test grün wird.

## Ein verfälschter erster Anlauf

Der erste Test lief in einem Kundenordner, dessen Einrichtung noch nicht
abgeschlossen war. Die Sitzung las „Passt so" als Abschluss von
Installer-Phase 4 und ging in Phase 5 — die Alltagsregeln waren gar nicht der
aktive Rahmen. Der Unterschied ist nicht akademisch: Der Käufer verbringt
zwanzig Minuten in der Einrichtung und danach Monate im Normalbetrieb.
Wiederholt nach abgeschlossener Phase 5.

## Was nicht geprüft ist

**Ob der Block Tage später gefunden und benutzt wird.** Beide Läufe fanden am
selben Tag statt. Der ehrliche Anschlusstest wäre eine Sitzung nach echtem
Zeitabstand, die auf „fass bei Ostermann nach" den Block aus der Datei zieht.
Der Prüfstand liegt dafür bereit.

**Ob der `outreach`-Vertrag im Alltag greift.** Er ist geschrieben und im Skill
verankert, die drei Fälle laufen grün — aber kein Ketten-Fall prüft diese
Schnittstelle. Ein eigener ist ein Kandidat, sobald sie benutzt wird.
