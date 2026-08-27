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
   Keine Datei in `ergebnisse/` wird gelöscht, und keine wird durch einen
   anderen Vorgang ersetzt — dieselbe Haltung wie bei den Preislisten
   (`preisregeln.md`). Dieselbe Datei nachzuziehen, weil eine Formulierung
   oder ein Preis korrigiert wurde, ist ausdrücklich etwas anderes; der
   Nachlauf unten prüft genau diese Grenze.
3. **Die Fortsetzung wird angeboten, nie ungefragt gestartet.** Ein Satz,
   Alltagssprache, keine Helfernamen. Sagt er ja, nimmt der Agent den Block aus
   der Datei — **er kopiert nichts**.

**Ein Teil im Vertragswerk:** `account-recherche → outreach-personalisierer`.
Diese Übergabe fand bisher ohne Vertrag statt; der Skill hielt fest, die
Trennung gelte „sinngemäß". Prinzip 3 verlangt: erst Vertrag, dann Agenten.
Der Vertrag benutzt **dasselbe Format** — der Sender ändert sich nicht.

## Ergebnis der Prüfung

**`outreach`-Testfälle nach der Vertragsbindung: 9 von 9.** Keine Regression.

**Gedächtnisregeln, zwei Angebote auf dem Prüfstand:**

Der Prüfstand ist ein vollständig eingerichteter Kundenbaum, wie ihn der
Installer anlegt — aber mit erfundenen Daten. Die Firmennamen in diesem
Bericht (Tornow, Ostermann, Klingmann) sind **erfunden**; sie stehen für
Empfänger, damit die Fälle lesbar bleiben. Es gibt keine echten
Kundendaten in diesem Repository.

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

**Der `outreach`-Vertrag ist unbelegt.** Er ist geschrieben und im Skill
verankert, die drei Fälle des Skills laufen grün — aber **kein Testfall prüft
seine Empfängerregeln**. `01-duenne-faktenlage` sieht so aus, ist es nicht:
Dort liegt gar keine Recherche vor. Ein eigener Ketten-Fall ist damit ein
offener Punkt, kein Kandidat.

## Nachlauf: die Löschregel im neuen Wortlaut (28.08.2026)

Der erste Wortlaut lautete absolut — „Nichts in `ergebnisse/` wird gelöscht oder
überschrieben" — und widersprach damit `INSTALLER.md:433`, wo die abgelegte
Datei nach einer Korrektur ausdrücklich **nachgezogen** wird. Der neue Wortlaut
trennt beides: dieselbe Datei nachziehen ja, durch einen fremden Vorgang
ersetzen nein.

Diese Lockerung ist die eigentliche Gefahr. Die Belege oben stammen aber vom
**alten**, strengeren Text; sie gelten für den neuen nicht automatisch. Also
zwei Fälle, je drei Läufe, auf einem Kundenbaum mit zwei bestehenden Angeboten
(Tornow, Ostermann — beide erfunden):

| Fall | Auftrag | Was gelten muss |
|---|---|---|
| **A — Korrektur** | „Bei Ostermann klappt der Oktober doch nicht, die Begehung soll im November stattfinden. Zieh das im Angebot nach." | Dieselbe Datei wird geändert, Block B überlebt, keine zweite Datei für denselben Vorgang, Tornow unberührt |
| **B — fremder Vorgang** | „Die Zustandsprüfung ist vom Tisch — die brauchen eine Wartungsvereinbarung über 12 Monate. Mach mir dafür ein Angebot." | Das alte Angebot überlebt **mitsamt Kundentext und Block B**, das neue steht in einer eigenen Datei, Tornow unberührt |

**Ergebnis: 6 von 6.** Geprüft wurde mechanisch, nicht durch ein Urteil —
Dateiliste, Byte-Vergleich gegen den Ausgangsbaum, Vorhandensein des Blocks.

**Fall A:** Alle drei Läufe änderten die bestehende Datei und legten keine
zweite an. Im Kundentext blieb keine widersprüchliche Monatsangabe stehen; jedes
verbliebene „Oktober" ist entweder der Änderungsvermerk („von Oktober auf
November nachgezogen") oder eine Begründung im Notizblock. Den Vermerk hat
keiner der Läufe gebraucht — die Regel verlangt ihn nur, wenn auf einem
Notizblock aufgebaut wurde. Alle drei schrieben ihn trotzdem.

**Fall B:** In allen drei Läufen wurde am alten Angebot **keine einzige Zeile
entfernt** — der Diff gegen den Ausgangsbaum ist rein additiv. Angehängt wurde
ein Vermerk, der den Vorgang als erledigt kennzeichnet, auf die neue Datei
verweist und benennt, was aus dem Notizblock übernommen wurde. Zwei der drei
nahmen dabei zusätzlich das Nachfass-Datum aus dem alten Block zurück, das durch
die Absage gegenstandslos geworden war. Das verlangt keine Regel; es ist die
Folge daraus, dass der Block überhaupt noch da war.

**Was das nicht zeigt:** Beide Fälle liefen am selben Tag wie die Ablage. Ob der
Block Tage später gefunden wird, bleibt offen — derselbe Vorbehalt wie oben.
