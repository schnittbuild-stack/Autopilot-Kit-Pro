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
| 3 — Einrichten | offen | — | — |
| 4 — Erste echte Aufgabe | offen | — | — |
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
