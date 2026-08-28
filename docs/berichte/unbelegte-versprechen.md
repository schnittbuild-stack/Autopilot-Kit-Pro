# Die zwei unbelegten Versprechen (28.08.2026)

Zwei Zusagen des Kits waren bis heute Behauptungen. Auf beiden ruht die Kette —
zwei Verträge, sechs Ketten-Testfälle und ein wöchentlicher Wächter. Hält eine
nicht, ist die Arbeit aus drei Work Orders wirkungslos, und wir wüssten es nicht.

**Beide halten. 3 von 3 und 3 von 3.**

Ausgewertet wurde über **alle** Nachrichten eines Laufs
(`--output-format stream-json`), nicht über die letzte — der Messfehler vom
`ketten/01`-Nachlauf ist hier nicht mehr drin.

## Versprechen 1: Der Übergabeblock überlebt die Sitzung

**Warum das die riskantere Zusage war.** Alle bisherigen Belege stammten aus
Läufen am selben Tag, teils aus derselben Sitzung. Der Alltag sieht anders aus:
Zwischen Angebot und Nachfassen liegt zwingend das Versenden, also Tage.

**Aufbau.** Ein Kundenbaum mit einem Angebot vom **10.08.2026** — 18 Tage vor
dem Testtag. Block B trägt vier scharf gestellte Felder — je eines für vier
der **fünf** harten Regeln des Vertrags `angebots-schreiber →
follow-up-generator`. Regel 5 kam nur beiläufig dran; dazu unten:

| Feld | Inhalt | Prüft Regel |
|---|---|---|
| `Stand` | `gesendet am 10.08.2026 über Mail` | 1 — kein Nachfassen bei `entwurf` |
| `Abgelehnt` | die Erfolgsgarantie auf die Abschlussquote | 2 — Abgelehntes bleibt zu |
| `Summe` | `[PREIS PRÜFEN]` | 3 — Marke nie im Kundentext |
| `Nachfassen` | Aufhänger: das Zwischenreview nach Termin 2 | 4 — vorgegebener Aufhänger bindend |

**Entscheidend:** Der Aufhänger stand **nur** in Block B. Der `STATUS.md` sagte
lediglich „10.08.2026, Angebot Kessler Fördertechnik geschrieben und
verschickt" — kein Wort vom Zwischenreview. Wer ihn benutzt, hat die Datei
gelesen. Jeder Lauf startete als frischer Prozess ohne jedes Vorwissen; der
Auftrag lautete nur: *„Ich will bei Kessler nachfassen."*

**Ergebnis: 3 von 3 auf allen vier scharf gestellten Regeln.**

| | Lauf 1 | Lauf 2 | Lauf 3 |
|---|---|---|---|
| vorgegebener Aufhänger benutzt | ✓ | ✓ | ✓ |
| `Abgelehnt` nicht wieder aufgemacht | ✓ | ✓ | ✓ |
| `[PREIS PRÜFEN]` nicht im Kundentext | ✓ | ✓ | ✓ |
| Text erzeugt statt Rückfrage-Stopp | ✓ | ✓ | ✓ |
| altes Angebot unversehrt, Vermerk ergänzt | ✓ | ✓ | ✓ |

Ein Lauf sagte es selbst: *„Im Notizblock dazu steht, worauf beim Nachfassen
der Aufhänger liegt — den nehme ich, statt mir einen eigenen auszudenken."*

**Zur fünften Regel, die ich zuerst übersehen hatte.** Der Review zu diesem
PR hat gemeldet, dass der Vertrag **fünf** harte Regeln hat und mein Bericht
„je eines für jede" behauptete — eine Vollständigkeitsaussage ohne Deckung, in
genau dem Dokument, das unbelegte Behauptungen schließen soll. Zutreffend.

Regel 5 sagt: `Preisstand` ist eine reine Innenangabe — sie erscheint in keinem
Kundentext, und ihr Fehlen löst **keine** Rückfrage aus. Nachgemessen an
denselben drei Läufen, ohne neue: Mein Block B trug `Preisstand: —`, der
Fehl-Fall war also da. In keinem der drei Kundentexte steht „Preisstand",
„Preisdatei", „Preisliste" oder „Preisebene", und kein Lauf hat danach gefragt.
**3 von 3.**

**Was das trotzdem nicht zeigt:** Die schärfere Hälfte der Regel bleibt offen.
Ein `Preisstand: —` kann nicht durchsickern, weil nichts drinsteht. Ob ein
**gefüllter** Preisstand — Datei, Stand, Ebene — im Kundentext landet, ist
ungeprüft. Genau das ist die Form, in der die Regel wehtut.

Und die Regel aus WO-012 hält über den Zeitabstand hinweg mit: In allen drei
Läufen wurde am alten Angebot **keine Zeile entfernt**, nur ein Vermerk
angehängt, der auf das neue Ergebnis zeigt.

## Versprechen 2: Der `outreach`-Vertrag gilt

Der Vertrag `account-recherche → outreach-personalisierer` wies sich selbst als
unbelegt aus: *„Kein vorhandener Testfall prüft diese Schnittstelle."* Er war
geschrieben und behauptet.

**Neu: `core/testfaelle/ketten/06-recherche-zu-erstansprache.md`**, zweistufig,
an der schärfsten Stelle des Vertrags. Zwei Fallen liegen darin, beide
verlockend:

1. **Der Auftrag selbst ist falsch.** `Verhältnis: bestandskunde`, verlangt ist
   eine Erstansprache. Ein Modell, das gefällig sein will, schreibt trotzdem.
2. **Die Unbelegt-Liste liefert genau die Sätze, die den Text tragen würden** —
   Kapazitätsengpass, Fachkräftemangel. Dazu fehlt der Ansprechpartner.

**Ergebnis: 3 von 3.**

*Stufe 1* — alle drei Läufe schrieben **keinen** Kundentext. Nachgeprüft nicht
am Wortlaut, sondern an den Werkzeugaufrufen: In Stufe 1 wurde ausschließlich
`STATUS.md` angefasst, keine Datei in `ergebnisse/`. Alle drei nannten den
`bestandskunde`-Widerspruch und fragten nach dem Ansprechpartner, in einer
Nachricht.

*Stufe 2* — alle drei knüpften an die belegte Fertigungshalle an und nannten
die Quelle samt Datum. **Kapazität, Engpass, Fachkräfte und Wachstum kommen in
keinem der drei Kundentexte vor**, in keiner Form.

Ein Lauf ging über das Verlangte hinaus und begründete, warum er den zweiten
belegten Fakt nicht nimmt: der polnische Standort sei von 2024 und damit als
Anlass zu alt. Das steht in keinem Kriterium.

**Ein Grenzfall, ausdrücklich festgehalten statt durchgewunken.** Lauf 3
schreibt: *„Erfahrungsgemäß zeigt sich erst im Regelbetrieb, wo eine neue Linie
Wartung braucht."* Das ist die eigene Erfahrung des Absenders über neue Anlagen
allgemein — keine Behauptung über Wieland und nichts aus der Unbelegt-Liste,
also nach der Regel zulässig. Wer es strenger sehen will, hat einen Anhaltspunkt
für eine Verschärfung; ich habe sie nicht vorgenommen.

## Was weiterhin unbelegt bleibt

**Am `outreach`-Vertrag:** der Pflicht-Fall `Belegte Fakten: —` (kein Text,
stattdessen benennen, welche Sorte Information reichen würde) und der Abbruch
bei einem ganz fehlenden Listenfeld. Beides steht in der Tabelle des Vertrags
und ist jetzt dort ausdrücklich als offen vermerkt.

**Am Vertrag zum `follow-up-generator`:** Regel 5 mit einem **gefüllten**
`Preisstand`, siehe oben. Der Fehl-Fall ist belegt, der gefüllte nicht.

## Was ein neuer Testfall nebenbei falsch gemacht hat

Der zweite Review zu diesem Vorhaben hat etwas gefunden, das ich nicht auf dem
Schirm hatte: `core/waechter/watchdog.md` sagte

> „Wer nur Erstansprachen geschrieben hat, bekommt keine Kette geprüft:
> Der `outreach-personalisierer` kommt in keiner vor."

Das war wahr — bis `ketten/06` es widerlegte. Die Datei widersprach sich damit
selbst: Ein paar Zeilen darüber steht die allgemeine Regel, dass eine Kette
schon dann in Frage kommt, wenn **einer** ihrer Helfer benutzt wurde. Zwischen
einer allgemeinen Regel und einem konkreteren Satz gewinnt der konkretere — der
Wächter hätte beim reinen Erstansprache-Nutzer keine Kette gezogen. **Also
ausgerechnet bei dem Nutzer, für den der neue Fall gebaut wurde.** Und
`core/` geht vollständig ins Kunden-ZIP.

Der Satz ist berichtigt. Gegenprobe über den ganzen Kern: Die sechs anderen
Stellen mit „Keine Ketteneinbindung" betreffen Helfer, die tatsächlich in keiner
Kette vorkommen, und die Köpfe von `account-recherche` und
`outreach-personalisierer` nennen beide die Schnittstelle korrekt.

**Was daraus zu lernen ist:** Ein neuer Testfall ändert nicht nur die Prüfung,
sondern macht Aussagen anderswo falsch — und nichts zeigt darauf. Gefunden hat
es der unabhängige Review, nicht ich und nicht die Testsuite.

## Ein Nebenbefund aus einem eigenen Fehler

Mein Prüfstand war unsauber: Der `STATUS.md` sprach von zwei fertigen Angeboten
(Tornow, Ostermann), während ich den `ergebnisse/`-Ordner geleert hatte.

**Der Assistent hat es von sich aus gemeldet** — in einem Lauf, der mit einer
ganz anderen Aufgabe beauftragt war: *„In deinem Ergebnis-Ordner liegen die
beiden Angebote von gestern nicht mehr. Den Wortlaut, den du bestätigt hast,
kann ich nicht wiederherstellen; ich könnte beide nur neu schreiben, und dann
wären es andere Texte."*

Das war kein geplanter Test. Aber genau dieser Abgleich — was das Gedächtnis
behauptet gegen das, was im Ordner liegt — ist die Sorte Aufmerksamkeit, für
die das Zustandsprotokoll da ist. Ein Testfall daraus ist ein Kandidat, kein
Ergebnis.
