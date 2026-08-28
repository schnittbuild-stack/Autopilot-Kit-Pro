# Vier Testfall-Entscheidungen, umgesetzt (28.08.2026)

Vier Befunde lagen seit dem 20.08. unentschieden: Stellen, an denen ein
**Testfall etwas verlangt, das der Skill anders sagt**. Das ist die gefährlichste
Sorte, weil sie richtiges Verhalten als Fehler meldet. Zweimal ist genau das
schon passiert — am 20.08. bei `angebots-schreiber/02` und am 28.08. bei `/03`,
beide Male fielen regelkonforme Läufe durch.

Der Auftraggeber hat alle vier entschieden. Was dabei herauskam, weicht an zwei
Stellen von dem ab, was ich ihm vorgeschlagen hatte.

## 1. Die `[kunde]`-Maskierung — und warum mein eigener Vorschlag falsch war

**Der Befund:** In allen fünf Fällen zum `angebots-schreiber` stand als Absender
`…@[kunde].de`. Pflicht-Fakt 1 lautet „Wer fragt an — **Firma**, Ansprechpartner,
Rolle". Der Helfer sah an der Stelle der Firma einen Platzhalter und fragte in
manchen Läufen nach — was Fälle scheitern ließ, die etwas ganz anderes prüfen.

**Entschieden:** Ohne Empfänger entsteht kein Angebot. Der Helfer fragt.

**Mein Umsetzungsvorschlag war, das „in den fünf Fällen zu verankern". Das hätte
vier von fünf zerstört:**

| Fall | Bestehensbedingung | Folge einer zusätzlichen Firmen-Rückfrage |
|---|---|---|
| 01 | „genau **zwei** Fragen" | drei → durchgefallen |
| 04 | „genau **eine** Frage" | zwei → durchgefallen |
| 03, 05 | fertiges Angebot verlangt | entsteht nie |

Genau die Falle, die wir bei Fall 03 am selben Tag beseitigt hatten. Aufgefallen
ist es beim Umsetzen, nicht beim Planen.

**Stattdessen umgesetzt:** Die fünf Fälle bekamen **lesbare Firmennamen** — wie
jeder andere Testfall im Repo. Die Maskierung war nie eine protokollierte
Entscheidung; sie kam mit der allerersten Fassung mit. Damit ist Pflicht-Fakt 1
vollständig, und jeder Fall prüft wieder das, wofür er gebaut ist. Geändert wurde
**ausschließlich die Eingabe**, jeder Fall trägt den Änderungsvermerk.

Die Entscheidung selbst braucht ein eigenes Zuhause, sonst ist sie unbelegt.
Dafür ist **`06-fehlender-absender`** neu: eine Anfrage von einer
Freemail-Adresse, unterschrieben nur mit dem Vornamen, sonst vollständig. Genau
eine Lücke, und sie ist Pflicht-Fakt 1.

## 2. `einwand-sparring/03` — war längst behoben

Der Befund lautete: Der Absatz „Bewertungslage" steht im Eingabeteil und liefert
dem erzeugenden Lauf die fertige Analyse mit.

**Beim Nachprüfen: am 19.08.2026 bereits behoben**, mit Änderungsvermerk im Fall
und eigenem Commit. Nur `docs/STATUS-BAU.md` führte ihn weiter als „Entscheidung
steht aus". **Nichts geändert**, der STATUS ist berichtigt.

Eine von vier „offenen Entscheidungen" war also seit neun Tagen keine mehr. Das
ist kein Zufall, sondern die Folge davon, dass ein Befund an zwei Orten steht:
im Fall und in der Statusliste. Wer nur einen pflegt, erzeugt Arbeit.

## 3. `follow-up-generator/02` — der Fall bestrafte den eigenen Zeitpunkt

Eine Muss-Zeile verlangte „einen Hinweis, dass eine Woche für ein Angebot dieser
Größe **knapp** ist". Der Fall setzt Versand am 14.08. und heute den 21.08. — das
sind **genau die 5 Werktage**, die der Skill für Stufe 1 vorsieht.

**Geändert wurde nur die Hälfte der Zeile, die im Widerspruch stand.** Der Rest
bleibt und ist der eigentliche Gehalt: Bei leerer Anlass-Rangfolge ist Abwarten
eine gültige Option.

## 4. `ketten/01` — verlangte, was er zugleich verbot

Die Bestehensbedingung lautete: „beide Rückfragen in einer Nachricht **und** ein
Block A ohne jede unbelegte Aussage". Der Fall verlangt zugleich, dass **kein**
Angebot entsteht, solange die Fragen offen sind. In einem Zug nicht erfüllbar —
und der Soll-Teil sprach mit „nach Beantwortung" von einer zweiten Stufe, die die
Eingabe nie lieferte.

**Jetzt zweistufig**, wie `ketten/02` und `06`. Die Bedingungen stehen im
Wortlaut unverändert, nur der Stufe zugeordnet, zu der sie gehören.

### Berichtigung eines eigenen Berichts

`docs/ketten01-untersuchung.md` behauptet: *„Zwölf Läufe in vier Anordnungen,
alle bestanden."* **Das war zu weit gefasst.** Alle zwölf endeten bei den
Rückfragen; einen Block A hat keiner erzeugt, weil die Eingabe die Antworten nie
lieferte. Was die zwölf Läufe zeigen, bleibt richtig — der Watchdog-Befund (die
fehlende zweite Rückfrage) ist widerlegt. „Bestanden" nach der vollen Bedingung
zeigen sie nicht. Der Bericht trägt jetzt einen Berichtigungsvermerk.

## Ergebnis der Nachläufe

Acht Fälle, je dreimal, über **alle** Nachrichten ausgewertet:

| Fall | Ergebnis | Anmerkung |
|---|---|---|
| `angebots-schreiber/01` | **2 von 3** | siehe unten — neuer Befund |
| `angebots-schreiber/02` | 3 von 3 | Rückfrage zum Verhältnis, kein Angebot |
| `angebots-schreiber/03` | 3 von 3 | vorher 2 von 3; die fehlende Firma war die Ursache |
| `angebots-schreiber/04` | 3 von 3 | genau eine Frage, kein Angebot |
| `angebots-schreiber/05` | 3 von 3 | 82 EUR aus dem Rahmenvertrag, Pauschalanfahrt, Schulung aus der Liste |
| `angebots-schreiber/06` *(neu)* | 3 von 3 | genau eine Frage, kein erfundener Firmenname |
| `follow-up-generator/02` | 3 von 3 | „knapp" kommt nicht mehr vor |
| `ketten/01` | 3 von 3 | **beide Stufen** — die volle Bedingung erstmals erfüllt |

Bemerkenswert bei `05`: Alle drei Läufe setzten die **82 EUR** aus dem
Rahmenvertrag an, obwohl die aktuelle Preisliste mit 78 EUR günstiger ist. Die
78 EUR tauchen nur im Notizblock auf, als Hinweis an {{rolle}}, dass der
Rahmenvertrag hier teurer ist. Genau das soll die Vorrangregel leisten.

## Der neue Befund: `angebots-schreiber/01` läuft 2 von 3

**Nicht durch diese Änderung verursacht** — die Ursache lag vorher da und ist
durch die Nachläufe sichtbar geworden.

Der Fall verlangt **genau zwei** Fragen und begründet das damit, dass „Ort,
Teilnehmerzahl, Raum, Verpflegung, Stilhinweis und **Bestandsverhältnis** alle in
der Mail" stünden. Das Bestandsverhältnis steht dort aber **nicht**. Was dasteht:
*„wir hatten uns ja im Frühjahr auf der Messe in Hannover kurz unterhalten — Sie
hatten mir Ihre Karte gegeben. Ich komme jetzt darauf zurück."*

Daraus **folgt** ein Neukunde. Gesagt ist es nicht. Zwei Läufe lasen die
Ableitung als ausreichend, einer fragte nach — und fiel damit auf `abweichend`,
weil er eine dritte Frage stellte.

**Dieselbe Familie wie die vier oben:** ein Fall behauptet, eine Angabe sei
vorhanden, während sie nur erschließbar ist. Und er bestraft damit denjenigen,
der nicht rät — bei einem Produkt, dessen Kernversprechen „lieber fragen als
raten" lautet.

**Nicht angefasst.** Zwei Wege stehen offen — die Zeile in die Mail schreiben
(wie bei Fall 03 am 28.08.), oder die dritte Frage ausdrücklich zulassen. Das
ist eine Änderung an einem Testfall und gehört dem Auftraggeber.

---

# Nachlese (28.08.2026, WO-018)

## Fall 01 entschieden

Der Auftraggeber hat entschieden: **Das Verhältnis kommt in die Eingabe.** Ein
Halbsatz — *„Zusammengearbeitet haben wir bisher noch nie, das wäre also das
erste Mal."* — macht aus der Ableitung eine Angabe. Soll-Teil und Bewertung
sind Wort für Wort unverändert; die Zählung „genau zwei" bleibt und misst
wieder Rückfrage-Disziplin statt Schlussfolgerungsfreude.

**Nachlauf: 3 von 3** (vorher 2 von 3). Alle drei Läufe stellten genau die zwei
gemeinten Fragen — Termin und Zielbild — und erzeugten kein Angebot.

## Und derselbe Griff an meinem eigenen Fall

Der Review zu WO-017 hat gemeldet, dass mein neuer Fall
`06-fehlender-absender` **dieselbe Konstruktion benutzte, die dieser Bericht an
Fall 01 rügt**: Das Bestandsverhältnis stand dort als „wie beim letzten Mal" —
erschließbar, nicht gesagt. Er hatte recht. Ich hatte das Muster beschrieben und
im selben Zug reproduziert.

Der Fall nennt es jetzt ausdrücklich („Sie haben bei uns im letzten Herbst schon
eine Sicherheitsunterweisung gemacht, wir sind also keine Neukunden").
**Nachlauf: 3 von 3** — genau eine Rückfrage nach dem Absender, kein Angebot,
kein erfundener Firmenname.

## Die Maskierung ist restlos raus

WO-017 hatte sie in den fünf Angebots-Fällen beseitigt. **Drei** Stellen
blieben — eine hatte der Review gemeldet, zwei fand die Gegenprobe:

| Stelle | vorher | jetzt |
|---|---|---|
| `ausschreibungs-analyse/03` | `einkauf@[kunde].de` | `einkauf@lemke-molkereitechnik.de` |
| `ketten/02`, Feld `Empfänger` | `[Kunde] GmbH` | `Ziegler Montagebau GmbH` |
| `follow-up-generator/01`, Feld `Empfänger` | `[Kunde] AG` | `Harnischfeger Verpackung AG` |

Keine dieser Stellen berührt ein Kriterium. Geändert wurden sie trotzdem:
**Eine halb abgeschaffte Konvention ist schlechter als gar keine** — sie sieht
aus wie Absicht und lädt dazu ein, sie an neuer Stelle wieder aufzugreifen.

`ketten/02` bekam denselben Firmennamen wie `angebots-schreiber/03`, weil beide
denselben Martin Hartmann führen.

**Nicht angefasst:** die `[Kunde]`-Marken im `einwand-sparring`. Das sind
**Sprecher-Label** im Übungsdialog, keine Firmenplatzhalter — sie stehen so auch
in der Anleitung des Skills.

## Nachläufe

| Fall | Ergebnis |
|---|---|
| `angebots-schreiber/01` | **3 von 3** *(vorher 2 von 3)* |
| `angebots-schreiber/06` | 3 von 3 |
| `ausschreibungs-analyse/03` | 3 von 3 — Lücken benannt, „bieten mit Vorbehalt" |
| `follow-up-generator/01` | 3 von 3 — kein Nachfass-Text, fehlendes Feld benannt |
| `ketten/02` | 3 von 3 über **beide** Stufen |

Bei `ketten/02` Stufe 2 erwähnen zwei von drei Läufen die abgelehnte Garantie —
ausschließlich im Notizblock, mit dem ausdrücklichen Satz, dass sie im
Kundentext nicht vorkommt. Genau das verlangt Regel 2 des Vertrags.

## Die restlichen Hinweise aus dem Review

- `docs/STATUS-BAU.md:233` führte `einwand-sparring/03` weiter als offen,
  obwohl er am 19.08. behoben wurde. Nachgetragen. **Zweite Fundstelle
  desselben Befunds** — dieselbe Lehre wie oben, an derselben Datei.
- `docs/ketten01-untersuchung.md` sagte, `[kunde]` sei Konvention in allen fünf
  Fällen. Der Absatz trägt jetzt einen Überholt-Vermerk statt einer stillen
  Korrektur: Er war richtig, als er geschrieben wurde.
- Der Änderungsvermerk in `04-preisgrundlage-abgelaufen` nannte „Domain und
  Firmenzeile"; geändert wurde auch der lokale Teil der Adresse (`m.k@` →
  `m.kessler@`). Präzisiert.

## Ein Hinweis, der zweimal durchgerutscht ist

Der Review zu WO-018 gab **fünf** nicht blockierende Hinweise; Work Order und
PR-Text der Folgearbeit nannten **vier**. Der fünfte war der operative:
`docs/ketten01-untersuchung.md` liegt in keinem `ordinary_paths`-Muster, der
Pull Request kann also nicht über die ordentliche Merge-Spur laufen.

Er ist **weder erledigt noch bewusst offengelassen** worden — er ist beim Zählen
verlorengegangen. Hiermit ausdrücklich offen:

> **Offen, Owner-Entscheidung.** Die 14 Berichte bis zum 27.08.2026 liegen in
> `docs/` und sind nicht „gewöhnlich". Solange keiner von ihnen mehr angefasst
> wird, kostet das nichts. Zweimal ist es inzwischen doch passiert
> (`ketten01-untersuchung.md` in PR #19 und #20). Entweder ziehen die alten
> Berichte nach `docs/berichte/` um — rund 25 Dateien mit Verweisen, darunter
> die reservierte `CLAUDE.md` —, oder es bleibt bei der manuellen Spur für
> diese seltenen Fälle. Steht so auch in `docs/berichte/README.md`.

**Die Lehre ist nicht neu, sondern dieselbe wie oben:** Ein Befund, der als Zahl
weitergegeben wird („vier Hinweise"), verliert unterwegs seinen Inhalt. Wer
zählt, statt zu benennen, merkt den Verlust nicht.
