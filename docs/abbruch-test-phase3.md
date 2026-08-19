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
| 5 — Wächter und Übergabe | offen | — | — |

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
