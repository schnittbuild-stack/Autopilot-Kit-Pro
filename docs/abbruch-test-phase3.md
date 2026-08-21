# Abbruch-Test Phase 3 — fünf Phasen, fünf harte Abbrüche, ein Wort

Stand: 19.08.2026. Diese Datei wird **nach jedem einzelnen Fall**
fortgeschrieben, committet und gepusht (Bauprinzip 2).

## Was hier geprüft wird

Definition of Done Phase 3, Anforderung 1, Punkt 2:

> Die Sitzung wird in **jeder der fünf Phasen** hart beendet. Die Fortsetzung
> gelingt, indem die Testperson **„weiter"** tippt — ohne jede Erklärung durch
> uns, kein Übergabetext, kein Souffleur. Klappt das nicht, ist Phase 3 nicht
> fertig.

Geprüft wird also nicht, ob die Fortsetzung *technisch möglich* ist, sondern ob
sie **von allein** gelingt. Dazu kommt eine zweite Frage, die genauso hart ist
und in der Anforderung nur mitgemeint war:

> Hätte der Nutzer an dieser Abbruchstelle überhaupt erfahren, dass „weiter"
> das Zauberwort ist?

Ein Kit, dessen Fortsetzung funktioniert, das dem Nutzer aber nie gesagt hat,
wie er sie auslöst, hat die Anforderung nicht erfüllt — er tippt dann etwas
anderes, oder er fängt von vorn an. Beide Fragen werden je Fall getrennt
beantwortet.

## Aufbau des Tests

Ein einziger Durchlauf wird durch alle fünf Phasen gefahren und fünfmal
unterbrochen — nicht fünf frische Durchläufe. Der Ordner trägt also bei jedem
Abbruch die Spuren der vorigen Phasen, so wie beim echten Nutzer.

Je Fall drei getrennte Sitzungen, die nichts voneinander wissen:

1. **Die Einrichtungssitzung.** Arbeitet die Anleitung in einem echten Ordner
   ab, legt echte Dateien an. Die Antworten des Nutzers kommen aus einem festen
   Drehbuch (`evals/testprofil.md` als Person). Sie hält an einer vorgegebenen
   Stelle **mitten im Schritt** an und schreibt ausdrücklich **keinen**
   Übergabetext und keine Notiz für die nächste Sitzung.
2. **Die frische Sitzung.** Bekommt den Ordner, den Inhalt der Gedächtnisdatei
   (so, wie die Plattform ihn beim Start mitgibt) — und als einzige Nachricht
   des Nutzers das Wort `weiter`. Sonst nichts. Sie weiß nicht, dass sie
   geprüft wird, und sie weiß nichts von der vorigen Sitzung.
3. **Die Bewertung.** Sieht den Stand auf der Platte im Moment des Abbruchs,
   eine nüchterne Liste dessen, was tatsächlich erledigt war, und die
   Mitschrift der frischen Sitzung. Sie sieht **die Anleitung nicht** — sie
   urteilt über das, was der Nutzer erlebt hätte.

**Die sieben Prüfpunkte** der Bewertung: fortgesetzt statt gefragt · an der
richtigen Stelle · nichts doppelt · der erste Satz aus dem Stand · kein Blick
hinter die Kulissen · Stand fortgeschrieben · nichts kaputt.

**Durchgefallen** ist verletzt, wer nach dem Stand fragt oder an der falschen
Stelle fortsetzt — dann hat „weiter" nicht getragen. Alles andere ist
`abweichend`.

## Fortschritt

| Phase | Abbruchstelle | Fortsetzung | Wusste er von „weiter"? |
|---|---|---|---|
| 1 — Ist alles startklar | mitten im Umräumen | **bestanden** | ja, aber nur aus `START_HIER.md` |
| 2 — Kennenlernen | nach Frage 7, ohne Antwort | **bestanden** | ja — Installer hat es am Ende von Phase 1 gesagt |
| 3 — Einrichten | drei von sechs Assistenten gefüllt | **bestanden** | ja — eine Nachricht vorher gesagt |
| 4 — Erste echte Aufgabe | Rückfrage raus, keine Antwort | **bestanden** | ja — Ende Phase 3 gesagt |
| 5 — Wächter und Übergabe | vor dem Beibringen des Zauberworts | **bestanden** | ja — aus `START.md`, nicht vom Installer |

**Nachtrag 20.08.2026:** Drei der vier Befunde dieses Tests sind behoben; die
Fälle **3, 4 und 5 sind danach wiederholt worden** und wieder bestanden. Der
zweite Durchlauf steht in dieser Datei unter „Wiederholung der Fälle 3
bis 5". Die Fälle 1 und 2 sind von den Änderungen nicht berührt.

**Zweiter Nachtrag 20.08.2026:** Nach den sechs Textkorrekturen des Tages sind
die Fälle **2 bis 5** noch einmal gelaufen — **drei bestanden, einer
abweichend** (Fall 2: eine Frage wird zweimal gestellt). Dritter Durchlauf am
Ende dieser Datei. Fall 1 bleibt auch davon unberührt.

## Ergebnis

**Fünf Phasen, fünf harte Abbrüche, fünfmal nur das Wort „weiter" — fünfmal
bestanden.** In keinem Fall wurde nach dem Stand gefragt, in keinem Fall an der
falschen Stelle fortgesetzt. Anforderung 1 aus der Definition of Done ist damit
belegt, nicht mehr nur gebaut.

| Phase | Fortsetzung |
|---|---|
| 1 — mitten im Umräumen | bestanden |
| 2 — nach Frage 7, ohne Antwort | bestanden |
| 3 — drei von sechs Assistenten gefüllt | bestanden |
| 4 — Rückfrage raus, keine Antwort | bestanden |
| 5 — vor dem Beibringen des Zauberworts | bestanden |

**Drei der fünf Fälle waren keine sauberen Schnitte.** In Phase 1, 2 und 3 war
der Stand auf der Platte im Moment des Abbruchs **nachweislich falsch**. Die
Fortsetzung hat das jedes Mal überlebt, weil die Sitzung nachgesehen hat, statt
der Datei zu glauben. Das ist die eigentliche Nachricht dieses Tests: Nicht die
Standsdatei allein trägt, sondern die Regel, sie gegen die Wirklichkeit zu
prüfen.

**Und der Nutzer wusste in allen fünf Fällen, dass „weiter" das Zauberwort
ist** — aber nie, weil der Installer es ihm beigebracht hätte. Der Schritt, der
das tut, liegt ganz am Ende (Phase 5, Schritt 2) und wurde in keinem einzigen
Abbruchfall erreicht. Getragen haben ihn andere: `START_HIER.md` vor der
Einrichtung, die Phasenabschlüsse zwischendurch, `START.md` ab Ende Phase 3.
Das Netz hält, weil es vierfach gespannt ist — nicht wegen der Lehrstunde.

## Die fünf Fälle

<!-- Ein Fall, ein Block. Wird nach jedem Fall ergänzt. -->


### Phase 1 — Abbruch mitten im Umräumen

**Ergebnis: bestanden.** Alle sieben Prüfpunkte erfüllt.

**Die Abbruchstelle.** Der bösartigste Punkt, den Phase 1 hergibt, und die
Anleitung beschreibt ihn selbst: Der Stand wird geschrieben („Ordner werden
gerade umgeräumt, noch ist nichts verschoben"), dann wird verschoben — und
mittendrin stirbt die Sitzung. Auf der Platte lag danach:

- `CLAUDE.md` und `system/STATUS.md` angelegt, alle neuen Ordner angelegt
- `core/` **bereits** nach `system/` verschoben
- `adapter-claude/` und `notfall/` **noch nicht** verschoben
- ein Stand, der behauptet, es sei **noch nichts** verschoben

Der Stand war also im Moment des Abbruchs nachweislich **falsch**. Das ist
kein konstruierter Sonderfall, sondern der Normalfall eines harten Abbruchs:
Zwischen „ich schreibe auf, was ich vorhabe" und „ich habe es getan" liegt
immer eine Lücke.

**Was der Nutzer gesehen hat.** Genau einen Satz: „Ich schau kurz, ob bei dir
alles bereitsteht. Dauert eine Minute, du musst nichts tun." Danach lief alles
still — so, wie die Anleitung es verlangt. Dann war das Fenster weg.

**Was auf „weiter" passiert ist.** Die frische Sitzung hat sich wörtlich mit
dem Satz aus dem Stand gemeldet: „Ich war gerade beim Aufräumen der Ordner —
ich mach da einfach weiter, du musst nichts tun." Sie hat **nicht** dem Stand
geglaubt, sondern nachgesehen, was tatsächlich schon unter `system/` liegt,
`core/` in Ruhe gelassen und nur `adapter-claude/` und `notfall/` verschoben.
Danach Phase 1 zu Ende gebracht, Stand fortgeschrieben, frisches Gespräch
angeboten.

**Das ist der eigentliche Nachweis dieses Falls:** Die Fortsetzung hat einen
falschen Stand überlebt, weil die Anleitung an dieser Stelle „prüfen, was
schon verschoben ist" vorschreibt und die Sitzung das auch getan hat. Ein
Fortsetzungsmechanismus, der nur mit korrekten Ständen funktioniert, hätte
hier `core/` ein zweites Mal verschoben oder wäre steckengeblieben.

**Hätte der Nutzer gewusst, dass „weiter" das Zauberwort ist?**

**Ja — aber nur aus `START_HIER.md`, nicht vom Installer.** Der Installer
hatte es an dieser Stelle noch nicht gesagt: Er bietet den frischen Start nach
**jeder abgeschlossenen Phase** an (eiserne Regel 5), und Phase 1 war nicht
abgeschlossen. Die einzige Quelle war die Datei, aus der der Nutzer wenige
Minuten zuvor abgelesen hat, wie er überhaupt startet — sie nennt „weiter"
ausdrücklich, mit der Beruhigung dazu. Zusätzlich liegt `notfall/01-weiter-machen.md`
im Ordner, aber dorthin muss er von selbst kommen.

**Bewertung dieses Risikos:** vertretbar, aber es ist das dünnste Glied der
ganzen Kette. Zwischen dem Lesen von `START_HIER.md` und dem Abbruch liegen
im schlechtesten Fall zwei Minuten — dafür spricht, dass er sich erinnert.
Dagegen spricht, dass er in diesen zwei Minuten nichts getan hat, was das Wort
verankert: Der Installer hat es weder wiederholt noch geübt. **In Phase 1 gibt
es keinen zweiten Halt.** Wer `START_HIER.md` überflogen hat, um schnell an
den Satz zum Kopieren zu kommen, hat „weiter" nicht gelesen.

**Randbeobachtung ohne Notenwirkung:** Die frische Sitzung kündigt die zehn
Fragen an und vermerkt als nächsten Schritt Frage 1 — stellt sie im sichtbaren
Text aber nicht. Der Nutzer bekommt „zehn kurze Fragen" angesagt und dann das
Angebot eines frischen Gesprächs, ohne dass eine Frage dasteht. Das kostet
keinen Prüfpunkt, ist aber eine unnötige Leerstelle an einer Phasengrenze.

**Zwei Korrekturen an den Prüfpunkten, beide vor diesem Urteil.**
Prüfpunkt 5 war in seiner ersten Fassung sachlich falsch: Er verbot, dem
Nutzer das frische Gespräch anzubieten — also genau die Handlung, die
Anforderung 1 Punkt 2 zwingend verlangt. Die zweite Fassung zählte „Ordner",
„Datei" und „Gedächtnis" zu den verbotenen Fachbegriffen; die Anleitung nennt
genau diese Wörter als die **erlaubten** Alltagswörter (eiserne Regel 2). Beide
Fassungen hätten eine Pflichthandlung als Fehler gezählt. Die dritte Fassung
erfindet keine Liste mehr, sondern übernimmt die Wortlisten der Anleitung.

Beide verworfenen Urteile liegen im Testaufbau unter
`urteil-p1-VOR-KORREKTUR.md` und `urteil-p1-VOR-KORREKTUR-2.md`. **In beiden
waren die Prüfpunkte 1, 2, 3, 4, 6 und 7 unverändert erfüllt** — die
Korrekturen haben nur den Prüfpunkt bewegt, der falsch formuliert war, nicht
das Ergebnis der Fortsetzung. Der Vorgang steht hier, weil eine stille
Korrektur an einem Bewertungsmaßstab von Weichspülen nicht zu unterscheiden
wäre.


### Phase 2 — Abbruch unmittelbar nach Frage 7

**Ergebnis: bestanden.** Alle sieben Prüfpunkte erfüllt.

**Die Abbruchstelle.** Die Fragen 1 bis 6 sind beantwortet und in
`mein-profil.md` gesichert. Frage 7 (Signatur) steht als letzte Nachricht auf
dem Bildschirm — dann ist die Sitzung weg. Der Nutzer hat sie gelesen und nie
beantwortet.

**Wieder klafft eine Lücke zwischen Stand und Wirklichkeit**, diesmal in die
andere Richtung als in Phase 1: Der Stand sagt „Frage 7 ist noch **nicht**
gestellt", obwohl sie auf dem Bildschirm stand. Der Stand wird nämlich
geschrieben, **bevor** die Frage rausgeht — so schreibt es die Anleitung vor,
und so ist es auch richtig. Die Alternative wäre gefährlicher: Stünde dort
„Frage gestellt, warte auf Antwort", könnte die nächste Sitzung sie für
erledigt halten und nicht wiederholen — und im frischen Gespräch sieht der
Nutzer die alte Frage nicht mehr.

**Was auf „weiter" passiert ist.** Die frische Sitzung hat den Satz aus dem
Stand Zeichen für Zeichen übernommen:

```
Wir sind beim Kennenlernen — sechs von zehn Fragen sind durch. Weiter mit
Nummer sieben: Wie sieht deine E-Mail-Signatur aus? Einfach hier reinkopieren,
so wie sie in deinen Mails steht. (Zum Beispiel: „Mit freundlichen Grüßen /
Katrin Reinhardt / Reinhardt Industrieservice GmbH / Telefon 0234 5558820")
```

Mehr nicht. Keine zweite Nachricht, keine Rückfrage, keine Zusammenfassung des
Bisherigen. Sie hat vorher in `mein-profil.md` nachgesehen, ob die sechs
Antworten wirklich drinstehen und das Signaturfeld leer ist — und dann nichts
geschrieben, weil es nichts zu sichern gab.

**Ein Prüfpunkt war strittig, und die Begründung dagegen ist die bessere.**
Prüfpunkt 6 verlangt, dass der Stand fortgeschrieben wird. Die Sitzung hat
nichts geschrieben. Die strenge Lesart wäre: Die Frage zu stellen ist ein
Schritt, also gehört er in den Stand. Die Bewertung hat dagegen entschieden,
und die Begründung trägt: Es gab kein Arbeitsergebnis, das verlorengehen
könnte, und die unveränderte Datei führt die nächste Sitzung verlustfrei an
dieselbe Stelle. Ein Eintrag „warte auf Antwort" wäre das schlechtere Verhalten.

**Hätte der Nutzer gewusst, dass „weiter" das Zauberwort ist?**

**Ja, und diesmal aus zwei Quellen.** Am Ende von Phase 1 — also eine Nachricht
vor dem Beginn des Interviews — hat der Assistent es ihm selbst gesagt: „Das
war's für diesen Teil. Wenn du magst, fang gleich ein frisches Gespräch an und
schreib einfach **weiter** — dein Stand ist gesichert." Dazu weiterhin
`START_HIER.md`.

Damit ist die Lage in Phase 2 deutlich besser als in Phase 1: Der Hinweis kam
vom Assistenten, im Fluss der Unterhaltung, wenige Minuten vor dem Abbruch.
**Innerhalb** von Phase 2 fällt das Wort allerdings kein einziges Mal mehr —
geprüft an der Mitschrift, kein Treffer über zehn Fragen hinweg. Wer zwischen
Frage 1 und Frage 10 abbricht, verlässt sich auf die Erinnerung an eine
Nachricht am Phasenende. Das trägt, ist aber kein Netz mit zwei Böden.


### Phase 3 — Abbruch mitten im Bauen

**Ergebnis: bestanden.** Alle sieben Prüfpunkte erfüllt — aber dieser Fall hat
die schwerste Lücke der ganzen Reihe freigelegt.

**Die Abbruchstelle.** Sechs Assistenten sind ausgewählt, drei davon sind
fertig gebaut (`angebots-schreiber`, `follow-up-generator`,
`meeting-nachbereitung` — mechanisch geprüft, kein `{{` mehr darin). Das
Gedächtnis steht noch auf der Kurzfassung aus Phase 1, `START.md` gibt es
nicht, aufgeräumt ist nichts.

**Der Stand sagt: „Phase 3 (Einrichten) hat noch nicht begonnen."**

Das ist die größte Lücke zwischen Stand und Wirklichkeit in allen fünf Fällen —
und anders als in Phase 1 und 2 ist sie **kein Zeitfenster von Sekunden,
sondern ein Konstruktionsfehler**:

> Die Anleitung verlangt für Phase 3 **keinen** Zwischenstand. Sie schreibt
> STATUS erst als Schritt 6, ganz am Ende der Phase.

Damit verstößt Phase 3 gegen Bauprinzip 2 („Jeder mehrstufige Prozess schreibt
seinen Fortschritt **nach jedem Schritt**") und gegen die eigene eiserne Regel
3 („Ein Schritt ohne STATUS-Eintrag gilt als nicht gemacht"). Für Phase 2 ist
die Ausnahme ausdrücklich geregelt — „innerhalb von Phase 2 schreibst du nach
**jeder** Antwort" —, für Phase 3 fehlt die entsprechende Zeile. Dabei ist
Phase 3 die Phase mit der meisten unsichtbaren Arbeit: Auswahl treffen, zehn
Dateien durchgehen, Lücken füllen.

**Was auf „weiter" passiert ist.** Die frische Sitzung ist nicht in die Falle
gelaufen. Sie hat sich nicht auf den Stand verlassen, sondern nachgesehen:
Platzhaltersuche über die Skill-Dateien plus Änderungszeiten (Dateien 23:12,
letzter Stand 23:08). Die drei fertigen Dateien hat sie erkannt, geprüft und
**nicht** neu gebaut. Dann hat sie zwei weitere gefüllt, das Gedächtnis und
`START.md` erzeugt, aufgeräumt und den Stand dreimal fortgeschrieben.

**Was sie nicht retten konnte:** Welche sechs Assistenten ausgewählt waren,
stand nirgends. Sie hat deshalb **neu ausgewählt und kam auf fünf** — jeder
davon aus den Antworten des Nutzers begründbar, und „fünf bis sechs" ist
erlaubt. Die Bewertung hat das als zulässig gewertet und das Schwanken
vermerkt. Für den Nutzer ist der Unterschied unsichtbar. **Trotzdem ist eine
Auswahl verlorengegangen, und niemand hat es gemerkt** — nur weil die neue
Auswahl die drei fertigen Dateien zufällig enthielt, gibt es keinen Schaden.
Hätte sie anders gewählt, lägen jetzt bis zu neun gefüllte Dateien im Ordner,
von denen die Zuordnungstabelle nur fünf kennt.

**Befund 1 — Phase 3 braucht einen Zwischenstand.** Nach der Auswahl gehört
sie in den Stand („diese sechs, in dieser Reihenfolge"), und nach jeder
gefüllten Datei gehört sie abgehakt. Das ist dieselbe Regel, die Phase 2 schon
hat. Nicht umgesetzt — es ist eine Änderung am Installer, und sie zieht einen
neuen Durchlauf durch die Phasen 3 bis 5 nach sich.

**Befund 2 — das erzeugte Gedächtnis verliert den Weg zur Anleitung.** Die
Kurzfassung aus Phase 1 nennt `system/adapter-claude/INSTALLER.md`
ausdrücklich. Die vollständige Fassung aus `CLAUDE.vorlage.md`, die sie in
Phase 3 ersetzt, nennt sie **nicht mehr**. Ab dem Ende von Phase 3 hängt die
Fortsetzung der Phasen 4 und 5 allein daran, dass der Stand den Weg selbst
beschreibt. Die frische Sitzung hat das bemerkt und sich im Lauf einen Halbsatz
ergänzt.

**Dieser Halbsatz wurde für die weiteren Fälle wieder entfernt.** Die Phasen 4
und 5 sind gegen das gebaute Produkt zu prüfen, nicht gegen eine Reparatur, die
im Testlauf entstanden ist. Die `CLAUDE.md` im Testordner entspricht jetzt
wieder genau dem, was `CLAUDE.vorlage.md` hergibt.

**Befund 3 — ein Baufehler im Repo, außerhalb dieses Tests.** Beim Füllen fiel
auf: In `core/skills/vertrieb/outreach-personalisierer.md` steht an einer
Stelle `{{firma}}`, wo die Firma des **Empfängers** gemeint ist, nicht die des
Nutzers. Eingesetzt würde dort die eigene Firma stehen. Nicht behoben — es ist
ein anderer Skill, und nach der Arbeitsregel vom 19.08.2026 zieht seine
Änderung seine drei Testfälle nach sich.

**Hätte der Nutzer gewusst, dass „weiter" das Zauberwort ist?**

**Ja, denkbar knapp davor.** Der Assistent hat es am Ende von Phase 2 gesagt —
in der Nachricht unmittelbar vor „Jetzt baue ich dir deine Assistenten". Danach
schweigt er, wie es die Anleitung für Phase 3 vorschreibt („Ab hier redest du
**nicht** über das, was du tust"). Der Nutzer sitzt also vor einem stillen
Fenster, und das letzte, was er gelesen hat, war der Hinweis auf „weiter". Das
ist die beste Ausgangslage aller fünf Fälle.


### Phase 4 — Abbruch mitten in der ersten echten Aufgabe

**Ergebnis: bestanden.** Alle sieben Prüfpunkte erfüllt.

**Die Abbruchstelle.** Der Nutzer hat eine echte Anfrage hereingegeben (Bernd
Keßler, zwei Tage Schulung fürs Vertriebsteam) mit den Worten „Die kam heute
Morgen rein, mach mir was draus." Der Assistent hat die Fakten gezogen, zwei
Lücken gefunden — Termin und Zielbild — und die Rückfrage rausgeschickt.
Antwort: keine. Fenster zu. `ergebnisse/` ist leer.

**Das ist der Abbruch, der am meisten weh tut.** Nicht weil viel Arbeit
verlorenginge, sondern weil es der Moment ist, für den der Käufer bezahlt hat.
Bricht es hier ab und der Neustart misslingt, ist das Produkt für ihn
gescheitert — egal wie sauber die Einrichtung lief.

**Zum ersten Mal decken sich Stand und Wirklichkeit vollständig.** Der Stand
führt die laufende Aufgabe mit der Anfrage im Wortlaut, mit dem, was schon
feststeht, was fehlt, dass die Rückfrage raus ist — und er regelt sogar den
Fall einer **Teilantwort** vor („Antwortet er nur auf eine der beiden Fragen,
wird die andere noch einmal gestellt — nichts geraten"). Das ist die
ausführlichste Standsdatei der ganzen Reihe, und sie entsteht, weil die
Anleitung für Phase 4 einen Abschnitt „Laufende Aufgabe" vorsieht.

**Was auf „weiter" passiert ist.** Die frische Sitzung hat sich mit dem Satz
aus dem Stand gemeldet und die zwei unbeantworteten Fragen erneut gestellt:

```
Wir sind bei der Anfrage von Herrn Keßler — zwei Tage Schulung für sein
Vertriebsteam. Zwei Sachen brauche ich noch, dann ist das Angebot fertig:

1. Wann soll die Schulung laufen?
2. Woran will er nach der Schulung merken, dass sie gewirkt hat?
```

Kein Angebot vor der Zeit, nichts aus den Phasen 1 bis 3 wiederholt, kein Wort
über Technik.

**Sie hat mehr getan als nötig, und das war der einzige Wackelpunkt.** Weil
beide Fragen nur der Kunde beantworten kann, hat sie zusätzlich eine
versandfertige Mail an Keßler geschrieben und nach `ergebnisse/` gelegt —
mit genau diesen zwei Fragen, ohne Preis und ohne Umfang. Die Bewertung hat
das geprüft und als unschädlich gewertet: Es verschiebt den Fortsetzungspunkt
nicht, es rät nichts, und es nimmt der Inhaberin Arbeit ab. Der Punkt steht
trotzdem im Urteil, weil die Anleitung diesen Zwischenschritt nicht vorsieht.

**Hätte der Nutzer gewusst, dass „weiter" das Zauberwort ist?**

**Ja.** Am Ende von Phase 3 hat der Assistent es gesagt. Danach kam die Frage
nach der echten Aufgabe, seine Anfrage, die Rückfrage — drei, vier Nachrichten
Abstand. Dazu steht es seit dem Ende von Phase 3 in **`START.md`**, die er
gerade eben bekommen hat und die dafür gebaut ist, aufgeschlagen zu werden.
Ab hier trägt die Kundenansicht den Hinweis selbst, nicht mehr nur die
Erinnerung an eine Nachricht.

Zu beachten: **`START_HIER.md` ist am Ende von Phase 3 nach `system/`
gewandert.** Die Quelle, die in den Phasen 1 und 2 das Netz war, ist ab hier
weg — ersetzt durch `START.md`. Der Wechsel ist lückenlos, aber er ist ein
Wechsel, und er passiert ohne dass jemand es merkt.

### Phase 5 — Abbruch, bevor „weiter" beigebracht wurde

**Ergebnis: bestanden.** Alle sieben Prüfpunkte erfüllt.

**Die Abbruchstelle, und warum genau diese.** Phase 5 hat fünf Schritte.
Schritt 1 richtet den Wochencheck ein, **Schritt 2 bringt dem Nutzer „weiter"
bei und lässt ihn einmal üben**. Der Abbruch liegt genau dazwischen. Das ist
der einzige Punkt im ganzen Durchlauf, an dem die Einrichtung an der Stelle
stirbt, die für die Fortsetzung zuständig ist — der Test, der sich selbst
prüft.

Vorher fertig: alle vier Phasen, das Angebot für Keßler samt eingearbeiteter
Korrektur in `ergebnisse/`, der Wochencheck. Nicht gemacht: „weiter"
beibringen, üben lassen, „hilfe" zeigen, verabschieden, den Stand abschließen.

**Was auf „weiter" passiert ist.** Die frische Sitzung hat sich mit dem Satz
aus dem Stand gemeldet und Schritt 2 begonnen — und dann etwas getan, das die
Anleitung nicht vorsieht und das trotzdem richtiger ist als das Vorgesehene:

```
Üben musst du das nicht mehr: Du hast es eben selbst gemacht. Deine Nachricht
war weiter — und du siehst, was passiert ist. Ich mache da weiter, wo wir
stehen geblieben sind, ohne dass du mir irgendetwas noch mal erzählen musstest.
Mehr ist es nicht.
```

Die Anleitung verlangt „Probier's gleich aus — schreib mal weiter." Der Nutzer
hatte es gerade getan. Ihn dasselbe Wort unmittelbar noch einmal tippen zu
lassen, wäre die Wiederholung gewesen, die Prüfpunkt 3 verbietet. Die Bewertung
hat erwogen, das als falsche Stelle zu werten, und sich dagegen entschieden;
die Begründung steht im Urteil, der Rest ist dort als offen vermerkt.

Danach hat sie Schritt 3 bis 5 abgearbeitet, einen offenen Punkt aus dem Stand
nachgezogen und die Einrichtung abgeschlossen.

**Hätte der Nutzer gewusst, dass „weiter" das Zauberwort ist?**

**Ja — aber ausgerechnet hier nicht vom Installer.** Das ist die Pointe dieses
Falls: Der Abbruch liegt **vor** dem Schritt, der es beibringt. Getragen hat es
**`START.md`**, seit Ende Phase 3 im Wurzelordner, mit der Zeile „**weiter** —
wir machen da weiter, wo wir aufgehört haben. Dein Stand ist gesichert, auch
wenn du das Fenster zugemacht hast."

**Die Anforderung ist also erfüllt, aber nicht durch den Mechanismus, der dafür
gebaut wurde.** Phase 5, Schritt 2 ist die einzige Stelle, an der „weiter"
ausdrücklich gelehrt und geübt wird — und sie wird in keinem der fünf
Abbruchfälle erreicht. Wer das für ein Detail hält, sollte es andersherum
lesen: Die Lehrstunde ist der **letzte** Faden des Netzes, nicht der erste.
Fiele `START.md` weg oder überflöge der Käufer `START_HIER.md`, stünde die
Anforderung auf einem einzigen Satz am Ende jeder Phase.

**Zwei Befunde am Kit, aufgefallen beim Bauen dieses Falls, beide am Repo
nachgeprüft:**

**1. Es gibt keinen Wächter zum Einrichten.** Phase 5, Schritt 1 sagt „Richte
den Wächter ein". Eine Vorlage dafür existiert weder in `core/` noch in
`adapter-claude/vorlagen/` — mechanisch geprüft: Treffer auf „Wochencheck",
„Wächter" oder „Watchdog" nur in zwei READMEs, in `STATUS.vorlage.md` und in
`INSTALLER.md` selbst, nirgends eine Quelle. Der Installer muss ihn **frei
erfinden**, und die Testsitzung hat genau das getan: `system/wochencheck.md`
mit sieben selbst ausgedachten Prüfpunkten. **Jeder Käufer bekommt damit einen
anderen Wächter.** Der Punkt stand als Risiko in `docs/STATUS-BAU.md` — jetzt
ist er belegt, nicht mehr vermutet.

**2. Die Verbotsliste wird zur Installationszeit vervielfältigt.** Sie steht
danach in `mein-profil.md`, in `CLAUDE.md` und in **jeder** eingerichteten
Skill-Datei — im Testordner siebenmal. Ursache ist Phase 3, Schritt 2:
„Ersetze in den ausgewählten Dateien jeden Platzhalter durch die Angaben aus
`mein-profil.md`." Im Repo ist Prinzip 1 sauber — überall steht `{{verbote}}`,
nirgends der Inhalt. **Beim Kunden ist es gebrochen.**

Die Folge zeigte sich sofort und ungeplant: Die Stilkorrektur aus Phase 4
(„kein ‚gerne'") konnte nicht an einer Stelle greifen. Eine Sitzung zog Profil
und Gedächtnis nach und vermerkte die fünf veralteten Skill-Dateien als offenen
Punkt; erst die nächste Sitzung räumte sie hinterher. Das ging nur gut, weil es
im Stand stand. Eine Abweichung, die niemand notiert, bleibt liegen — und der
Käufer merkt sie erst, wenn ein Assistent etwas schreibt, das er abgestellt zu
haben glaubte.

**Beide Befunde sind nicht behoben.** Der Wächter ist Phase-4-Arbeit
(BAUPLAN), und die Vervielfältigung der Profildaten ist eine
Architekturentscheidung, keine Korrektur nebenbei.

---

# Wiederholung der Fälle 3 bis 5 — 20.08.2026

## Warum wiederholt wurde

Drei der vier Befunde dieses Tests sind behoben worden
(`docs/STATUS-BAU.md`, Abschnitt „Nacharbeit aus dem Abbruch-Test"):

1. **Platzhalter werden nicht mehr ersetzt**, sondern beim Lesen aufgelöst —
   Prinzip 1 gilt jetzt auch beim Kunden.
2. **Installer-Phase 3 schreibt nach jedem Schritt STATUS**, die Auswahl der
   Assistenten zuerst.
3. **Den Wächter gibt es** — feste Vorlage in `core/waechter/wochencheck.md`,
   Phase 5 macht ihn nur noch bekannt.

Alle drei greifen in den Phasen 3 bis 5. Die Fälle 1 und 2 (Umräumen,
Interview) sind von keiner der Änderungen berührt — dort wurde nichts
angefasst, und ihr Ergebnis vom ersten Durchlauf gilt unverändert.

## Aufbau — derselbe wie beim ersten Mal

Ein Durchlauf, dreimal unterbrochen. Je Fall drei getrennte Sitzungen:
Einrichtungssitzung (hält mitten im Schritt an, kein Übergabetext), frische
Sitzung (bekommt Ordner, Gedächtnisdatei und als einzige Nachricht `weiter`),
Bewertung (sieht Stand, Tatsachen und Mitschrift — **nicht** die Anleitung).
Dieselben sieben Prüfpunkte, dieselbe Notenskala, dieselben Auftragstexte.

**Zwei Änderungen am Prüfstand, beide offengelegt:**

1. **Das Datum** ist der 20.08.2026 statt der 19.
2. **Die Antworten für Phase 4 stehen jetzt im Drehbuch** — die zwei Angaben
   auf die Rückfrage und die Stilkorrektur („‚gerne‘ schreibe ich nie"). Im
   ersten Durchlauf hat die Sitzung sie frei erfunden; die Korrektur ist im
   Bericht überliefert. Jetzt hören beide Läufe dieselbe Person antworten.
   Die Korrektur ist zugleich der schärfste Test für Baustein 1 — sie ist
   genau die, die beim ersten Mal an fünf Stellen nicht griff.

**Der Abbruchpunkt in Phase 3 musste neu bestimmt werden.** „Drei von sechs
Assistenten gefüllt" gibt es nicht mehr: Gefüllt wird nichts. Der neue Punkt
ist die gleiche Sorte Schnitt — **mitten in Schritt 2**, drei von fünf Dateien
auf ihre Verweise geprüft, der STATUS-Eintrag für diesen Schritt noch nicht
geschrieben. Damit bleibt die Eigenschaft erhalten, die den ersten Durchlauf
hart gemacht hat: **Der Stand ist im Moment des Abbruchs falsch.**

## Ergebnis

| Phase | Abbruchstelle | Fortsetzung |
|---|---|---|
| 3 — Einrichten | mitten in Schritt 2, drei von fünf Dateien geprüft | **bestanden** |
| 4 — Erste echte Aufgabe | Rückfrage raus, keine Antwort | **bestanden** |
| 5 — Wächter und Übergabe | nach Schritt 1, vor dem Beibringen des Zauberworts | **bestanden** |

**Drei von drei bestanden, alle sieben Prüfpunkte je Fall erfüllt.** Zusammen
mit den unberührten Fällen 1 und 2 steht Anforderung 1 weiterhin auf **5 von 5**.

## Was die Wiederholung belegt — und was nicht

### Baustein 2 hält: die Auswahl überlebt den Abbruch

Das ist der Punkt, an dem der erste Durchlauf Schaden genommen hat. Damals
stand die Auswahl nirgends; die frische Sitzung wählte neu, kam auf fünf statt
sechs, und dass daraus kein Schaden entstand, war Zufall.

Diesmal stand im Stand:

```
Ausgewählt am 20.08.2026, fünf Assistenten, in dieser Reihenfolge:
1. angebots-schreiber — aus Frage 3: „Angebote schreiben, meistens abends …"
…
- [x] Auswahl getroffen (Schritt 1)
- [ ] Verweise geprüft
```

Die frische Sitzung hat **genau diese fünf** zu Ende eingerichtet und keine
zweite Auswahl getroffen. Der Nutzer bekam am Ende „Du hast jetzt fünf Helfer"
mit fünf Beispielsätzen — dieselben fünf, die die abgebrochene Sitzung gewählt
hatte.

### Baustein 1 hält: die Stilkorrektur wirkt an einer Stelle

Mechanisch nachgeprüft, im Zustand nach Phase 5:

- **`system/core/` ist Byte für Byte identisch mit dem Auslieferungszustand**
  (`diff -rq`, kein Unterschied). Keine Assistenten-Datei wurde angefasst,
  kein `{{…}}` ersetzt.
- Die Korrektur des Nutzers steht **einmal**, datiert, in `mein-profil.md`.
- Im fertigen Angebot kommt das verbotene Wort nicht vor.
- **Nichts musste nachgezogen werden.** Beim ersten Durchlauf blieben fünf
  Skill-Dateien veraltet und wurden erst von der nächsten Sitzung repariert —
  und das nur, weil es jemand im Stand vermerkt hatte.

Nebenbei ist damit auch die Zahl weg, die den Befund ausgelöst hat: Die
Verbotsliste steht beim Kunden jetzt **einmal** statt siebenmal.

### Baustein 3 hält: kein erfundener Wächter

Die Einrichtungssitzung hat in Phase 5 **nichts gebaut**. Es gibt keine Datei
`system/wochencheck.md`; es gilt `system/core/waechter/wochencheck.md`
unverändert. Der Nutzer hat die zwei Sätze bekommen, die der Installer
vorschreibt:

> Sag einmal die Woche „Mach den Wochencheck". Dann sehe ich nach, ob noch
> alles zu dir passt — dein Ton, deine Preise, was liegengeblieben ist — und
> sage dir, was zu tun wäre.

Die Auslöser-Zeile stand bereits in `CLAUDE.md` und musste nicht nachgetragen
werden, das Datum steht in STATUS. **Jeder Käufer bekommt ab jetzt denselben
Wächter.**

### Was nicht belegt ist

- **Der Wochencheck ist nie gelaufen.** Belegt ist, dass er existiert, dass er
  bekannt gemacht wird und dass niemand ihn mehr erfindet — nicht, dass seine
  vier Prüfpunkte etwas Nützliches finden. Das prüft erst Phase 4.
- **Ein Durchlauf, kein Dreifachlauf.** Für die Skills gilt die 3-von-3-Regel;
  der Abbruch-Test ist ein Verhaltensbeleg an einem Fall, kein Eval.
- **Die Antworten kommen aus einem Drehbuch.** Über die 30-Minuten-Grenze sagt
  auch dieser Durchlauf nichts.

## Fünf neue Befunde, keiner behoben

Alle fünf sind beim Durchlauf aufgefallen und stehen in
`docs/STATUS-BAU.md` unter „Offene Punkte".

1. **Das Gedächtnis verbietet, was der Installer verlangt.**
   `CLAUDE.vorlage.md` sagt: „`mein-profil.md` wird nur geändert, wenn der
   Nutzer ‚Einstellungen ändern‘ sagt. Nie nebenbei." Installer-Phase 4,
   Schritt 4 verlangt aber genau **eine** Profiländerung — die Stilkorrektur.
   Eine frische Sitzung, die mitten in Phase 4 einsteigt und nur das Gedächtnis
   liest, würde sie nicht eintragen. **Folgebefund von Baustein 1:** Solange
   Werte kopiert wurden, fiel das nicht auf; jetzt hängt die Wirkung jeder
   Stilkorrektur allein am Profil — und damit an dieser einen Regel.
2. **Eiserne Regel 1 widerspricht dem `angebots-schreiber`.** Der Installer
   sagt „Eine Frage pro Nachricht. Immer.", der Assistent stellt alle
   fehlenden Pflicht-Fakten in **einer** nummerierten Nachricht — und
   `angebots-schreiber/01-rueckfrage-disziplin` wertet genau das als
   bestanden. Die Sitzung hat sich für den Assistenten entschieden und den
   Widerspruch selbst vermerkt. Ohne Ausnahme in `INSTALLER.md` entscheidet
   das jede Sitzung neu.
3. **Der Wochencheck meldet die eigene Änderungsnotiz als Befund.** Wer in
   `ergebnisse/` notiert, *welches* verbotene Wort gestrichen wurde, schreibt
   genau dieses Wort dorthin, wo Prüfpunkt 1 sagt: „immer ein Befund". Die
   Sitzung hat es von sich aus umschrieben.
4. **Ein Schritt kann fünf Dateien umfassen — der Zwischenstand kennt nur
   ganze Schritte.** Der Stand sagte „Schritt 2 hat noch nicht begonnen",
   obwohl drei Dateien geprüft waren; die frische Sitzung hat sie noch einmal
   mitgeprüft. Kosten: ein zweiter Blick, kein Schaden. Genauer wäre, innerhalb
   eines Schrittes auch die einzelne Datei abzuhaken.
5. **Die bedingte Zusatzfrage zum Preis greift zu mechanisch.** Sie wurde
   gestellt, weil `meine-unterlagen/preise/` leer war — obwohl der Nutzer eine
   Nachricht zuvor gesagt hatte: „Preisliste hab ich, die leg ich gleich rein."

Dazu zwei **bekannte** Befunde, die dieser Durchlauf unabhängig bestätigt hat:
Das erzeugte Gedächtnis nennt den Weg zur Anleitung nicht mehr (Befund 2 des
ersten Durchlaufs), und `START.md` erklärt `CLAUDE.md` nicht (Punkt 4 der
Definition of Done). **Beide Male hat eine Testsitzung die Lücke von selbst
bemerkt und repariert** — beim ersten Mal genau einmal, jetzt zweimal
unabhängig voneinander.

## Anmerkung zur Redlichkeit

**Die zwei Selbstreparaturen wurden wieder entfernt**, wie beim ersten Mal, weil
die folgenden Fälle gegen das **gebaute** Produkt zu prüfen sind und nicht gegen
eine Reparatur, die im Testlauf entstanden ist.

Das hat eine Nebenwirkung, die hier stehen muss: Die Sitzungen hatten beide
Reparaturen in STATUS als erledigt vermerkt. Nach dem Entfernen behauptete der
Stand also etwas, das auf der Platte nicht mehr zutraf — und die frische
Sitzung im Fall 5 hat genau das bemerkt und nachgezogen. **Das ist kein
Verhalten des Produkts, sondern eine Folge des Eingriffs.** Für das Urteil ist
es unschädlich: Die Prüfpunkte 1 und 2 hängen nicht daran, und die Bewertung
hat den Punkt selbst geprüft und offengelegt.

Der Prüfstand mit allen Ständen, Tatsachen, Mitschriften und Urteilen liegt
außerhalb des Repos.

---

# Wiederholung der Fälle 2 bis 5 — 20.08.2026, nach den sechs Textkorrekturen

## Warum wiederholt wurde

Am 20.08.2026 sind sechs Textbefunde in einem Durchgang behoben worden
(Commit „installer+vorlagen: sechs Textbefunde aus dem Abbruch-Test in einem
Durchgang behoben"):

1. `CLAUDE.vorlage.md` nennt den **Weg zur Anleitung** wieder.
2. `CLAUDE.vorlage.md` bekommt die **Ausnahme für die Stilkorrektur**, die
   Installer-Phase 4 verlangt.
3. `START.vorlage.md` **erklärt `CLAUDE.md`**; die Checkliste der Phase 3
   prüft das mechanisch.
4. **Eiserne Regel 1** nimmt die Rückfrage des Assistenten aus (Phase 4).
5. **Wochencheck, Prüfpunkt 1** prüft den Kundentext, nicht die Notiz darüber.
6. Die **bedingte Zusatzfrage zum Preis** bekommt eine dritte Bedingung.

**Welche Fälle das berührt, steht mechanisch geprüft im Prüfstand
(`BETROFFEN.md`):** die Fälle 2 bis 5. **Fall 1 ist von keiner der sechs
Änderungen berührt** — die Kurzfassung von `CLAUDE.md`, die Phase 1 anlegt,
ist unverändert, eiserne Regel 1 nur um eine Ausnahme für Phase 4 ergänzt,
Regel 3 gar nicht. Sein Ergebnis vom ersten Durchlauf gilt weiter.

## Aufbau — derselbe wie zweimal zuvor

Ein Durchlauf, viermal unterbrochen. Je Fall drei getrennte Sitzungen:
Einrichtungssitzung (hält mitten im Schritt an, **kein** Übergabetext), frische
Sitzung (bekommt Ordner, Gedächtnisdatei und als einzige Nachricht `weiter`),
Bewertung (sieht Stand, Tatsachen und Mitschrift — **nicht** die Anleitung).
Dieselben sieben Prüfpunkte, dieselbe Notenskala.

**Zwei Änderungen am Prüfstand, beide offengelegt:**

1. **Das Drehbuch sagt bei Frage 9 ausdrücklich „Preisliste hab ich, die leg
   ich gleich rein."** Das ist genau die Lage, in der die bedingte Zusatzfrage
   nach der Korrektur **nicht mehr** gestellt werden darf — der Fall aus dem
   letzten Durchlauf, wörtlich nachgestellt.
2. **Der Nutzer legt die Preisliste zwischen Phase 2 und 3 tatsächlich ab.**
   Ohne das hätte Phase 4 nichts zu rechnen gehabt. Der Kopiervorgang ist von
   Hand gemacht worden, so wie ihn ein Käufer im Dateimanager machen würde.

## Ergebnis

| Phase | Abbruchstelle | Fortsetzung |
|---|---|---|
| 2 — Kennenlernen | nach Frage 7, ohne Antwort | **abweichend** |
| 3 — Einrichten | mitten in Schritt 2, drei von fünf Dateien geprüft | **bestanden** |
| 4 — Erste echte Aufgabe | Rückfrage raus, keine Antwort | **bestanden** |
| 5 — Wächter und Übergabe | nach Schritt 1, vor dem Zauberwort | **bestanden** |

**Drei von vier bestanden, einer abweichend.** In **keinem** Fall wurde nach
dem Stand gefragt, in **keinem** an der falschen Stelle fortgesetzt — die
beiden Durchfall-Bedingungen sind nirgends verletzt. Anforderung 1 hält also
weiter; die eine Abweichung ist ein Riss, kein Bruch.

### Der abweichende Fall 2 — und warum die Abweichung echt ist

Der Stand sagte im Moment des Abbruchs: „Frage 7 ist noch **nicht gestellt**."
Auf dem Bildschirm stand sie. Die frische Sitzung hat getan, was der Stand
verlangte — und Katrin hat Frage 7 damit **zweimal** gelesen.

**Die Ursache liegt in der Regel, nicht in der Sitzung.** Eiserne Regel 3
schreibt für Phase 2 vor: STATUS **nach jeder Antwort**. Eine Frage, die
gestellt, aber nicht beantwortet ist, hat damit keinen Platz im Stand. Bitter
daran: **Die `STATUS.vorlage.md` macht als Musterformulierung ausgerechnet den
feineren Fall vor** — „Frage 7 ist gestellt und noch nicht beantwortet" —, den
die Schreibregel so nie erzeugt. Die Vorlage weiß es besser als die Regel.

**Kosten:** ein Satz. Kein Datenverlust, keine falsche Stelle, keine
Rückfrage. Die Bewertung hat beide Lesarten notiert und sich für die strengere
entschieden, weil Prüfpunkt 3 („nichts doppelt") genau darauf zielt: Der
Nutzer soll nicht merken, dass ein Gespräch zu Ende ging — und eine Frage zum
zweiten Mal zu lesen ist die billigste Art, es zu merken.

**Nicht behoben.** Wie in den beiden Durchläufen davor werden Befunde aus dem
Abbruch-Test gesammelt und in einem Zug behoben, nicht einzeln — sonst zieht
jede Korrektur sofort den nächsten Durchlauf nach sich.

## Was die Wiederholung belegt

### Alle sechs Korrekturen sind im Kundenbaum angekommen — mechanisch geprüft

- `START.md` enthält die Zeile **„CLAUDE.md — mein Gedächtnis. Da steht, was
  ich über deine Arbeit weiß. Brauchst du nie zu öffnen."** Im Wurzelordner
  liegen genau sechs Einträge, und **`START.md` erklärt alle sechs.**
  **Punkt 4 der Definition of Done ist damit erfüllt**, nicht mehr verletzt.
- Das erzeugte `CLAUDE.md` nennt `system/adapter-claude/INSTALLER.md` als Weg
  zur Anleitung — an zwei Stellen.
- Die **Profil-Ausnahme** steht im erzeugten Gedächtnis **und hat gegriffen**:
  In Fall 4 hat die frische Sitzung Katrins Stilkorrektur („‚gerne‘ schreibe
  ich nie") eingetragen — **nur** in `mein-profil.md`, keine Assistenten-Datei
  angefasst. Im Angebot kommt das Wort nicht vor.
- Die **Ausnahme zu eiserner Regel 1 wird benutzt:** Die Einrichtungssitzung
  in Phase 4 hat beide fehlenden Pflicht-Angaben — Termin und Zielbild — in
  **einer** nummerierten Nachricht gestellt, so wie der Assistent es täte, und
  ist nicht mehr in den Konflikt mit „eine Frage pro Nachricht" geraten.
- **Die bedingte Zusatzfrage zum Preis wurde nicht gestellt.** Katrin hatte
  angekündigt, die Preisliste selbst abzulegen; die Sitzung hat den Punkt
  stattdessen in STATUS unter „Was der Nutzer noch nachliefern wollte"
  vermerkt und mit einem Satz quittiert. **Genau der Befund aus dem letzten
  Durchlauf, und er tritt nicht mehr auf.**

### Baustein 1 hält weiterhin

`system/core/` ist nach dem ganzen Durchlauf identisch mit dem
Auslieferungszustand — bis auf **eine** Datei, `follow-up-generator.md`, und
die Abweichung stammt aus dem Repo, nicht vom Installer: Sie ist am selben Tag
**nach** dem Kopieren des Prüfstands korrigiert worden (Befund aus
`docs/nachlauf-phase3.md`). Kein einziges `{{…}}` wurde ersetzt; alle elf
Skill-Dateien tragen ihre Verweise unverändert.

### Baustein 3 hält weiterhin

Es gibt keine Datei `system/wochencheck.md`. Die Einrichtungssitzung hat in
Phase 5 nichts gebaut und keinen eigenen Prüfpunkt erfunden — sie hat
`system/core/waechter/wochencheck.md` gelesen, das Datum in STATUS gesetzt und
den Check in zwei Sätzen erklärt.

### Was nicht belegt ist

- **Der Wochencheck ist weiterhin nie gelaufen.** Belegt ist nur, dass er
  existiert und nicht erfunden wird. Die Korrektur an Prüfpunkt 1
  (Änderungsnotiz) ist damit **eingebaut, aber ungeprüft** — sie greift erst,
  wenn der Check läuft, und das tut er erst in Phase 4.
- **Ein Durchlauf, kein Dreifachlauf**, und die Antworten kommen aus einem
  Drehbuch. Über die 30-Minuten-Grenze sagt auch dieser Lauf nichts.
- **Fall 5 belegt die Wiederaufnahme, nicht die Wortunabhängigkeit.** Der
  Abbruch liegt vor dem Schritt, der „weiter" beibringt. Getragen hat es —
  wie im ersten Durchlauf — **`START.md`**, das die Zeile „**weiter** — wir
  machen da weiter, wo wir aufgehört haben" seit Ende Phase 3 im Wurzelordner
  trägt; mechanisch nachgeprüft. Die Bewertung hat an dieser Stelle
  geschlossen, `START.md` nenne das Wort nicht — sie **konnte die Datei nicht
  sehen**, weil ihr der Kundenordner gesperrt ist. Ihr Vorschlag bleibt
  trotzdem richtig: Ein Fall, der mit „Hallo?" oder „Wo waren wir?" eröffnet,
  würde prüfen, was dieser Aufbau nicht prüft.

## Fünf neue Befunde, keiner behoben

1. **Phase 2 schreibt den Stand erst nach der Antwort — die gestellte Frage
   geht verloren.** Ursache der Abweichung in Fall 2. `STATUS.vorlage.md` macht
   den richtigen Fall bereits vor; eiserne Regel 3 erzeugt ihn nicht.
2. **Phase 4 hat zwischen Entwurf und „Passt das?" keinen Zwischenstand.**
   Bricht es dort ab, ist das fertige Angebot weg. Dieselbe Lücke, die Phase 3
   schon geschlossen bekommen hat — für Phase 4 nennt `INSTALLER.md` STATUS
   erst als Schritt 6.
3. **Die Beispiele in `core/interview/fragen.md` sind die Daten der
   Testperson.** Frage 7 zeigt Katrins Signatur samt Telefonnummer als
   „Beispiel", Frage 10 ihren Erfolgsmoment wörtlich. Beim echten Käufer ist
   das nur ein fremder Name — im Prüfstand kollidiert es und macht die
   Mitschrift schief. Beispiele sollten eine andere Person nennen als das
   Testprofil.
4. **Der Installer sichert Antworten in der dritten Person**, obwohl
   `mein-profil.md` den Nutzer durchgängig duzt („Vertrieb und Angebote macht
   **sie** selbst"). Kein Fehler im Inhalt, aber die Datei liest sich
   uneinheitlich.
5. **„Liegt fertig in `ergebnisse/`"**, während das Angebot `Stand: entwurf`
   ist und eine `[PREIS PRÜFEN]`-Zeile trägt. Nichts erfunden, aber der
   Abschlusssatz verspricht mehr, als dasteht.

## Anmerkung zur Redlichkeit

**Es wurde in diesem Durchlauf nichts am Kit repariert und nichts wieder
entfernt.** Anders als bei den ersten beiden Malen hat keine Sitzung eine
Lücke selbst geschlossen — es gab keine mehr zu schließen, die vorher
aufgefallen wäre. Der Prüfstand mit Ordner, Ständen, Tatsachen, Mitschriften
und allen vier Urteilen liegt außerhalb des Repos.

---

# Vierter Durchlauf — Fall 2 nach der Korrektur (21.08.2026)

## Warum überhaupt

Der dritte Durchlauf ließ Fall 2 als `abweichend` stehen: Der Stand führte eine
gestellte, unbeantwortete Frage als „noch nicht gestellt", und die frische
Sitzung stellte Frage 7 ein zweites Mal. Der Befund wurde damals ausdrücklich
**nicht** behoben, sondern als Entscheidung vermerkt, weil die Korrektur einen
neuen Durchlauf nach sich zieht. Diese Entscheidung ist am 21.08.2026 gefallen.

## Was geändert wurde

Drei Stellen in `adapter-claude/INSTALLER.md`, alle dieselbe Lücke:

- **Eiserne Regel 3** kannte nur „nach jeder Antwort". Ein Zustand *gestellt,
  aber unbeantwortet* konnte damit nie entstehen.
- **Phase 2, Schritt 2** sagte dasselbe und hätte der korrigierten Regel
  widersprochen.
- **Checkliste Phase 2** hat den Punkt jetzt als eigene Zeile.

Bemerkenswert: `vorlagen/STATUS.vorlage.md` machte den feineren Fall als
Musterformulierung **schon immer** vor — „Frage 7 ist gestellt und noch nicht
beantwortet". Die Vorlage wusste es besser als die Regel. Geändert wurde
deshalb die Regel, nicht die Vorlage.

## Aufbau

Unverändert zur Methodik der ersten drei Durchläufe: drei getrennte Sitzungen,
die nichts voneinander wissen, jede ein eigener Prozess.

Der Prüfstand wurde neu aufgebaut und enthält **genau das, was die
Release-Action ins Kunden-ZIP legt** — `START_HIER.md`, `core/`,
`adapter-claude/`, `notfall/`, ohne die drei `_TEMPLATE_`-Dateien. 66 Dateien.
Das Drehbuch (`evals/testprofil.md`) lag außerhalb des Kundenordners.

## Der Stand im Moment des Abbruchs

Die Einrichtungssitzung hat Phase 1 vollständig abgearbeitet, die Fragen 1 bis 6
gestellt, beantwortet und gesichert, Frage 7 gestellt — und angehalten. Kein
Übergabetext, keine Notiz. `system/STATUS.md` sagte:

> Phase 2 läuft: Fragen 1 bis 6 sind beantwortet und in mein-profil.md
> gesichert. Frage 7 (Die Signatur) ist **gestellt und noch nicht beantwortet**.

Und als nächsten Schritt: auf die Antwort warten, sie wörtlich ins Profil
schreiben, dann Frage 8 — „Frage 7 **nicht** noch einmal stellen."

**Das ist der Unterschied zum dritten Durchlauf.** Dort behauptete der Stand,
Frage 7 sei nicht gestellt.

## Was die frische Sitzung auf „weiter" tat

> Wir sind beim Kennenlernen — sechs von zehn Fragen sind durch, meine siebte
> steht noch offen: Wie sieht deine E-Mail-Signatur aus? Einfach hier
> reinkopieren, so wie sie in deinen Mails steht.

Dazu das Beispiel aus `fragen.md`. Sonst nichts: keine Begrüßung, keine
Rückfrage nach dem Stand, kein Wort über Dateien, Phasen oder einen Abbruch.

## Ergebnis: bestanden

Alle sieben Prüfpunkte erfüllt. Die Bewertung hat sich an Prüfpunkt 3
(„nichts doppelt") ausdrücklich abgearbeitet, weil dort der Riss saß, und
gegen ein `abweichend` entschieden — mit drei Gründen:

1. „Doppelt" ist, was doppelte **Arbeit** verursacht. Frage 7 wurde nie
   beantwortet; es gibt nichts zu verdoppeln, nur eine offene Schleife.
2. Das alte Fenster ist tot. Ohne Wiederholung müsste der Nutzer zurückscrollen
   oder raten — beides genau das Ausfallgefühl, das der Test sucht.
3. Die Formulierung behandelt die Frage als hängend, nicht als neu: „meine
   siebte steht noch offen" liest sich als Weitersprechen, nicht als Neuanfang.

Der Hinweis „Frage 7 nicht noch einmal stellen" im Stand zielt erkennbar auf
die Zeit **nach** der Antwort, nicht auf den Wiedereinstieg.

## Anmerkung zur Redlichkeit

**Die Bewertung lief auf dem Schnappschuss des Abbruchmoments, nicht auf dem
Ordner nach der Fortsetzung.** Sie hat das selbst als Einschränkung bei
Prüfpunkt 6 vermerkt. Getrennt nachgeprüft: Die frische Sitzung hat **keine
einzige Datei geändert** — korrekt, sie wartet auf die Antwort. Das
Signaturfeld im Profil ist leer geblieben, nicht mit dem Beispiel gefüllt.

**Was dieser Durchlauf nicht zeigt.** Nur Fall 2 ist gelaufen. Die Fälle 1 und
3 bis 5 sind von der Änderung nicht berührt und wurden nicht wiederholt. Über
die 30-Minuten-Grenze sagt auch dieser Durchlauf nichts — sie bleibt offen und
braucht eine echte Testperson an einem fremden Rechner.
