# Autorendurchlauf — 21.08.2026

Paket: `autopilot-kit-v2026.0.0-test1.zip`, gebaut aus `main` durch die
Release-Action. Der Prüfstand war der entpackte ZIP-Inhalt in einem frischen
Ordner, geöffnet in einem neuen Claude-Code-Gespräch, das nichts vom Projekt
wusste. Gestartet mit dem Satz, den `START_HIER.md` dem Käufer vorgibt.

## Was dieser Durchlauf ist — und was nicht

**Er erfüllt Punkt 1 der Definition of Done nicht.** Der verlangt eine
Testperson **ohne Vorkenntnisse**. Hier lief der Autor: Er kennt jede Anweisung,
zögert nirgends, überliest nichts. Das Ergebnis ist eine **untere Schranke**.

Dazu kommt ein zweiter Abschlag: Es wurden **erfundene Antworten** gegeben, keine
echten. Damit fällt genau die Arbeit weg, die beim Käufer die Zeit frisst — die
eigene Signatur heraussuchen, die Preisliste finden, über den eigenen
Erfolgsmoment nachdenken.

Der Abstand zu den 30 Minuten ist also kleiner, als die Zahl aussehen lässt.

## Zeit

**Rund 25 Minuten** für alle fünf Phasen, mit kleinen Unterbrechungen.
Selbst berichtet, nicht gestoppt.

**Kein Protokoll geführt.** Es gibt keine Phasenzeiten, keine Stockstellen und
keine mitgeschriebenen Fragen. Das ist eine Lücke, kein Ergebnis — beim nächsten
Durchlauf gehört `docs/durchlauf-protokoll.md` daneben.

## Was gut lief

Alle fünf Phasen liefen ohne Abbruch durch. Sechs Assistenten wurden ausgewählt,
das Material-Verzeichnis angelegt, „weiter" erklärt und einmal geübt.

**Die erste echte Aufgabe hat ein belastbares Ergebnis geliefert** — ein
CRM-Eintrag. Nachgeprüft:

- Der Belegsatz ist **wörtlich** zitiert, samt Tippfehler des Kunden. Nicht
  geglättet, nicht zusammengefasst.
- `Einschätzung statt Beleg: —` — ein leeres Pflichtfeld wurde als leer
  markiert statt gefüllt. Genau die Bruchstelle, an der Modelle sonst erfinden.
- **Keine erfundene Zahl.** Der Eintrag hält ausdrücklich fest, dass die eigenen
  Raten fehlen, und trennt sie von den Wettbewerbsraten, die der Kunde selbst
  genannt hatte: „Die Wettbewerbsraten oben sind seine Angaben, nicht unsere
  Grundlage." Anforderung 3 greift also im Ernstfall, nicht nur auf dem Papier.
- Der genannte Wochentag stimmt: Der 04.09.2026 ist tatsächlich ein Freitag.

**Das Platzhalter-Prinzip hält.** 38 Dateien im erzeugten Kundenbaum tragen ihre
`{{...}}` unverändert; im Profil stehen Werte, keine Platzhalter. Die
Entscheidung vom 20.08.2026 ist damit im Feld belegt.

## Der Befund: die Gedächtnisdatei wurde beschädigt

`system/STATUS.md` enthielt nach dem Durchlauf den Text der erledigten Aufgabe
**fünfmal**. Richtig war genau eine Stelle — der Abschnitt „Laufende Aufgabe".
Die anderen vier saßen mitten in fremden Sätzen:

> - Phase 2 abgeschlossen, keine — die Aufgabe vom 21.08.2026 … offenen Fragen
>   aus dem Interview.
> - Für die Customer-Service-Aufgaben gibt es keine — die Aufgabe vom
>   21.08.2026 … n eigenen Assistenten.

**Ursache:** Der Abschnitt „Laufende Aufgabe" enthielt vorher das Wort „keine".
Beim Eintragen der erledigten Aufgabe wurde dieses Wort **in der ganzen Datei**
ersetzt statt nur in seinem Abschnitt. „keine" steht dort an fünf Stellen.

**Warum die Anleitung das zuließ:** Phase 4, Schritt 6 sagte nur „STATUS
schreiben" — kein Wort darüber, *wie*. Nirgends im Installer stand, dass nur der
betroffene Abschnitt geändert werden darf.

**Warum das schwer wiegt:** `STATUS.md` ist die einzige Grundlage der
Fortsetzung. Bauprinzip 2 steht und fällt mit ihr. Ein Käufer, der am nächsten
Tag „weiter" tippt, liest zerrissene Sätze.

**Warum kein früherer Test es gefunden hat:** Der Abbruch-Test bricht *während*
der Phasen ab und prüft die Fortsetzung. Dieser Schaden entsteht erst *am Ende*
von Phase 4 — wenn von außen alles gelungen aussieht.

## Behoben

Die Regel sagt jetzt, **wie** geschrieben wird: nur im betroffenen Abschnitt,
nie ein Wort über die ganze Datei, danach die Datei einmal ganz lesen. An vier
Stellen, weil der Fehler sonst im Dauerbetrieb liegen bliebe:

- `adapter-claude/INSTALLER.md` — eiserne Regel 3
- `adapter-claude/INSTALLER.md` — Checkliste Phase 4, eigener Prüfpunkt
- `adapter-claude/vorlagen/STATUS.vorlage.md` — Hinweis im Kopf
- `adapter-claude/vorlagen/CLAUDE.vorlage.md` — für die Zeit **nach** der
  Einrichtung; dort verlangt das Kit denselben Zwischenstand, ohne bisher zu
  sagen wie

## Was offen bleibt

**Punkt 1 der Definition of Done Phase 3 ist weiterhin offen.** Es braucht eine
Testperson ohne Vorkenntnisse an einem fremden Rechner, mit geführtem Protokoll.

Zusätzlich unbeantwortet: Der Durchlauf lief auf **Opus 5 mit einem
Max-Konto**. `START_HIER.md` nennt „Pro- oder Max-Konto" als Voraussetzung. Ob
das Kit unter Pro genauso trägt, hat niemand geprüft.

## Nachweis der Behebung

Ein frischer Prüfstand aus dem korrigierten Stand (66 Dateien, wie im
Kunden-ZIP), eine eigene Sitzung, Phasen 1 bis 4 vollständig, in Phase 4 eine
echte Aufgabe mit vier Rückfragen des Assistenten.

**Ergebnis: `system/STATUS.md` ist unversehrt.**

- Das Wort „keine" steht an fünf Stellen — **jede in ihrem eigenen,
  vollständigen Satz**. Kein Ersetzen über die Datei mehr.
- Der Abschnitt „Laufende Aufgabe" trägt genau einen Eintrag, kurz und in
  seinem Abschnitt.
- Kein Satz ist zerrissen, kein verwaistes Zeichen.

## Ein zweiter Verdacht, der sich nicht bestätigt hat

Ein **abgebrochener** erster Prüflauf zeigte einen Stand, der gleichzeitig
„Phase 3 ist fertig" und „Phase 3 hat noch nicht begonnen" behauptete — ein
alter Absatz blieb stehen, ein neuer kam darüber. Das wäre ein anderer Fehler
gewesen als das globale Ersetzen: nicht falsch platziert, sondern nicht
aufgeräumt.

**Er ist im sauberen Lauf nicht aufgetreten.** „Woran wir gerade sind" enthielt
einen zusammenhängenden Absatz zum Jetzt-Zustand, „Der nächste Schritt" genau
eine Handlung, nichts Überholtes.

Der Abbruch des ersten Laufs war ein Zeitlimit des Prüfwerkzeugs, das den
Prozess mitten in Phase 4 beendet hat — die wahrscheinlichere Erklärung für
den Widerspruch. **Deshalb wurde dafür keine Regel ergänzt.** Eine Vorschrift
gegen ein Problem, das sich nicht belegen lässt, macht die Anleitung länger
und nicht besser. Wenn der Fall wiederkehrt, steht er hier und ist beim
nächsten Mal schneller einzuordnen.
