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
| 1 — Ist alles startklar | offen | — | — |
| 2 — Kennenlernen | offen | — | — |
| 3 — Einrichten | offen | — | — |
| 4 — Erste echte Aufgabe | offen | — | — |
| 5 — Wächter und Übergabe | offen | — | — |

## Die fünf Fälle

<!-- Ein Fall, ein Block. Wird nach jedem Fall ergänzt. -->
