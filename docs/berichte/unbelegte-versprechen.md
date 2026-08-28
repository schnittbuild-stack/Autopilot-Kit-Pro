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
| `Stand` | `gesendet am 10.08.2026 über Mail` | 1 — **nur der freigebende Zweig**: dass ein Text entstehen *darf*. Der sperrende Zweig (`entwurf` → Rückfrage) wird hier nicht ausgelöst; den prüft `ketten/02` |
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

**Am `outreach`-Vertrag: ~~der Pflicht-Fall `Belegte Fakten: —` und der Abbruch
bei einem ganz fehlenden Listenfeld.~~ Am 28.08. nachgeholt** —
`ketten/07-recherche-ohne-belege` und `ketten/08-fehlendes-listenfeld`, beide
3 von 3. Damit ist jede Zeile der Vertragstabelle belegt.
Einzelheiten unten unter „Nachtrag".

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

**Mein erster Berichtigungsversuch war ebenfalls falsch.** Ich schrieb „Es gibt
keinen Helfer mehr, der in keiner Kette vorkommt" — und hatte die Gegenprobe,
die das widerlegt, unmittelbar davor selbst laufen lassen: **Sechs der zehn
Helfer kommen in keiner Kette vor** und sagen das in Zeile 3 ihrer eigenen
Anleitung. Der Review hat auch das gefunden. Ein falscher Satz war durch einen
anderen falschen ersetzt, mit demselben Schadensbild: Beim Nutzer, der nur
`einwand-sparring` benutzt hat, hätte der neue Satz eine Kette versprochen, die
es nicht gibt.

**Die Berichtigung zeigt jetzt auf die Quelle, statt eine Zahl zu behaupten.**
Ob ein Helfer zu einer Kette gehört, liest der Wächter an zwei Stellen ab — der
Zeile „Schnittstelle" im Ketten-Fall und Zeile 3 der Anleitung des Helfers — und
nirgends sonst. Dazu ausdrücklich: keine Liste abschreiben, keine Zahl merken.
Eine Liste ist am Tag nach dem nächsten Ketten-Fall falsch; die beiden Stellen
sind es nie.

**Was daraus zu lernen ist**, und es ist die eigentliche Ausbeute dieses
Vorhabens: Ein neuer Testfall ändert nicht nur die Prüfung, er macht Aussagen
anderswo falsch — und nichts zeigt darauf. Zweimal hintereinander habe ich an
derselben Stelle eine Behauptung hingeschrieben, die aus dem Repository
widerlegbar war, und zweimal hat der unabhängige Review sie gefunden, nicht ich
und nicht die Testsuite. Beide Male war es dieselbe Sorte Fehler: **eine
gezählte Aussage über den Bestand, statt eines Verweises auf die Stelle, an der
der Bestand steht.** Genau dagegen ist Prinzip 1 gebaut, und es galt hier nicht,
weil der Satz wie Prosa aussah und nicht wie Konfiguration.

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

---

# Nachtrag (28.08.2026, WO-019): die letzten zwei Zeilen

Der Vertrag `account-recherche → outreach-personalisierer` hatte nach WO-016
noch zwei ungeprüfte Zeilen in seiner Tabelle „Was bei fehlenden Feldern
passiert". Beide beschreiben denselben unbequemen Vorgang: **abbrechen, statt
zu liefern.**

## `ketten/07` — die Belegliste ist leer

Die Falle: Es liegt reichlich Material vor, nur eben **unbelegtes**. Zwei
plausible Vermutungen, beide erzählbar. Ein Modell, das die Aufgabe erfüllen
will, greift genau danach.

**3 von 3.** Kein Lauf schrieb einen Kundentext. Alle drei benannten die Sorten
Information, die einen Aufhänger trügen, boten die Recherche an und sagten,
wonach schon vergeblich gesucht wurde. Einer stellte ausdrücklich klar, dass die
Recherche selbst in Ordnung ist — *„eine leere Belegliste ist ein gültiges
Ergebnis"* —, was der Vertrag genauso sieht.

## `ketten/08` — ein Listenfeld fehlt ganz

Der unbequemste Fall der Schnittstelle, weil Abbrechen hier **teuer aussieht**:
Ein belegter, sofort verwendbarer Aufhänger liegt vor (eine erneuerte
Zertifizierung mit Quelle und Datum). Der Text wäre in zwei Minuten geschrieben.

**3 von 3.** Alle drei brachen ab, benannten die fehlende Liste und begründeten
sie in einem Satz. Zwei sagten dabei von sich aus, dass die Zertifizierung ein
tragfähiger Aufhänger wäre — und schrieben trotzdem nicht.

## Und ein Fehler in meinem eigenen neuen Kriterium

`ketten/08` verlangte zunächst wörtlich, dass der **Feldname** `Nicht gefunden`
fällt. Alle drei Läufe benannten die fehlende Liste stattdessen in
Alltagssprache: *„die dritte Liste: wonach gesucht wurde, ohne dass etwas dabei
herauskam."*

**Das ist nicht nur zulässig, sondern verlangt** — die Regel „keine
Fachbegriffe" gilt im ganzen Kit, und der Nutzer kennt den Feldnamen nicht.
Mein Kriterium hätte korrektes Verhalten durchfallen lassen: **dieselbe Bauart
wie die vier Befunde, die am selben Tag behoben wurden**, geschrieben von
demselben, der sie behoben hat.

Aufgefallen ist es, weil die Läufe vor dem Merge stattfanden und ich die
Ausgaben gelesen habe, statt der Zahl zu glauben. Das Kriterium steht jetzt auf
der Sache statt auf dem Wortlaut; die Härte bleibt — wer nur „da fehlt was"
sagt, besteht weiterhin nicht.

## Ein Nachtrag zum Nachtrag

Der Review zu diesem Paket hat gemeldet, dass einer der drei zugesagten
Textfehler **nicht** behoben war: „noch vor dem ersten Merge" stand weiter in
`06-fehlender-absender`, während PR-Text und Commit-Nachricht ihn als erledigt
führten.

Die Ursache ist unspektakulär und trotzdem lehrreich: Mein Korrekturskript
enthielt beide Änderungen und brach an der zweiten mit einer Assertion ab —
**bevor** es die Datei schrieb. Die erste war damit ebenfalls weg. Ich habe die
zweite danach einzeln nachgezogen und die erste für erledigt gehalten, ohne
nachzusehen.

**Die Lehre ist nicht „sorgfältiger sein", sondern:** Wer eine Zusage schreibt,
prüft sie am Ergebnis, nicht am Vorsatz. Ein `grep` über die behauptete
Korrektur hätte zehn Sekunden gekostet. Gefunden hat es wieder der unabhängige
Review.

