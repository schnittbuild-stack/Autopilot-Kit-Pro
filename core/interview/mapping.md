# Platzhalter-Register (verbindlich)

Jeder Platzhalter, der in irgendeiner Datei des Kits vorkommt, steht hier — mit
der Quelle, die ihn füllt, und der Stelle, an der sein Wert beim Kunden steht.
Neuer Platzhalter ohne Eintrag hier = Baufehler.

Es gibt drei Quellen (Entscheidung 19.08.2026):

- **Profil** — Dauerwissen über die Person, aus dem Interview (Phase 2).
- **Unterlagen** — Firmenwissen, das der Nutzer als Datei in
  `meine-unterlagen/` ablegt. Siehe `core/unterlagen/aufbau.md`.
- **Standardwert** — vom Installer gesetzt, ohne Frage, im Profil änderbar.

## Ein Platzhalter ist ein Verweis, keine Lücke (Entscheidung 20.08.2026)

`{{...}}` wird **nirgends durch einen Wert ersetzt** — nicht im Repo und nicht
beim Kunden. Der Platzhalter bleibt stehen und wird **beim Lesen** aufgelöst:
Wer eine Datei abarbeitet, in der `{{verbote}}` steht, schlägt den Wert dort
nach, wo er steht — in `mein-profil.md`.

**Warum das so sein muss.** Prinzip 1 verlangt, dass Profil-, Firmen- und
Stildaten genau einmal stehen. Wird ein Platzhalter beim Einrichten durch
seinen Wert ersetzt, steht die Verbotsliste danach in jeder eingerichteten
Datei — und eine Korrektur im Profil greift dort nicht mehr. Genau das ist im
Abbruch-Test passiert: siebenmal dieselbe Liste, eine Stilkorrektur, die an
fünf Stellen wirkungslos blieb (`docs/abbruch-test-phase3.md`, Befund 4).

Daraus folgen drei Regeln:

1. **Der Installer ersetzt keinen Platzhalter.** Er prüft nur, dass jeder
   `{{...}}` in den eingerichteten Dateien hier im Register steht und dass das
   zugehörige Feld im Profil vorhanden ist.
2. **Ein leeres Feld heißt: keine Angabe.** Der Assistent fragt dann nach bzw.
   schreibt `[PREIS PRÜFEN]` — er erfindet nichts. Das ist genau der Zustand,
   den vorher der leer gelassene Platzhalter hergestellt hat.
3. **Geändert wird an genau einer Stelle** — im Profil oder in
   `meine-unterlagen/`. Ab dem nächsten Lesen gilt der neue Wert überall,
   ohne dass irgendeine Datei nachgezogen werden müsste.

Das ist keine neue Mechanik, sondern die, die im Kundenbaum ohnehin schon
läuft: `core/vertraege/`, `core/unterlagen/preisregeln.md`,
`core/unterlagen/aufbau.md` und die Testfälle tragen ihre Platzhalter
unersetzt und werden beim Lesen aufgelöst. Neu ist nur, dass die Skill-Dateien
es jetzt genauso halten.

## Das Register

| Platzhalter | Quelle | Wo der Wert beim Kunden steht | Inhalt |
|---|---|---|---|
| {{rolle}} | Profil, Frage 1 | `mein-profil.md` → „Was du machst" | Job/Rolle des Nutzers |
| {{firma}} | Profil, Frage 2 | `mein-profil.md` → „Deine Firma" | Firma und Branche |
| {{nervaufgaben}} | Profil, Frage 3 | `mein-profil.md` → „Was dich jede Woche nervt" | Die drei wiederkehrenden Schmerzpunkte |
| {{tools}} | Profil, Frage 4 | `mein-profil.md` → „Womit du arbeitest" | Genutzte Programme |
| {{tonalitaet}} | Profil, Frage 5 + Material aus Frage 9 | `mein-profil.md` → „Ton" | Förmlich/locker, abgeleitet aus Beispielen |
| {{anrede}} | Profil, Frage 6 | `mein-profil.md` → „Kunden duzen oder siezen" | Du/Sie gegenüber Kunden |
| {{signatur}} | Profil, Frage 7 | `mein-profil.md` → „Deine Signatur" | E-Mail-Signatur wörtlich |
| {{verbote}} | Profil, Frage 8 | `mein-profil.md` → „Sätze und Themen, die nie vorkommen" | No-Gos in Formulierung und Inhalt |
| {{stilbeispiele}} | **Unterlagen**, angestoßen von Frage 9 | `meine-unterlagen/stilbeispiele/` und `meine-unterlagen/angebote/` | Texte, an denen sich Ton und Satzbau ausrichten |
| {{erfolgsmoment}} | Profil, Frage 10 | `mein-profil.md` → „Der Moment, an dem es sich gelohnt hat" | Woran der Nutzer Erfolg misst (für Phase Beweis) |
| {{preisgrundlage}} | **Unterlagen**, angestoßen von Frage 9; ersatzweise bedingte Zusatzfrage | `meine-unterlagen/preise/`; ersatzweise `mein-profil.md` → „Wie du Preise bildest" | Preisliste, Kalkulationsgrundlage, Kundenkonditionen. Ist dort nichts und wird auch die Zusatzfrage nicht beantwortet, bleibt der Wert leer und preisbildende Skills markieren `[PREIS PRÜFEN]` statt zu raten |
| {{preisfrist}} | **Standardwert** — 6 Monate, keine Frage | `mein-profil.md` → „Wie lange ein Preisstand ohne Rückfrage gilt" | Wie lange ein Preisstand ohne Rückfrage gilt. Danach fragt der Skill **einmal** nach, statt stillschweigend weiterzurechnen (`core/unterlagen/preisregeln.md`) |

Die Feldnamen in der dritten Spalte sind die Überschriften bzw. Zeilenanfänge
aus `adapter-claude/vorlagen/profil.vorlage.md`. Wer dort eine Zeile umbenennt,
ändert sie **hier zuerst** — sonst zeigt ein Verweis ins Leere.

## Frage 9 ist die Materialfrage

Frage 9 fragt nicht mehr nur nach zwei, drei guten E-Mails, sondern nach allem
Material, das der Nutzer ohnehin hat: Preisliste oder Kalkulationsgrundlage,
alte Angebote, Leistungsbeschreibungen, AGB, E-Mails, die er gut findet. Er
legt es in `meine-unterlagen/` — der Installer nennt ihm den Ordner und sagt
in einem Satz, was er davon hat.

Alles daran ist optional. Wer nichts hat, sagt „nichts" und kommt weiter; jeder
Skill funktioniert dann wie bisher, nur mit mehr Rückfragen.

## Bedingte Zusatzfrage zur Preisgrundlage

Wird **nur dann** gestellt, wenn beides zutrifft:

1. In `meine-unterlagen/preise/` liegt nichts, **und**
2. die Antworten auf Frage 1 und 3 zeigen preisbildende Arbeit (Angebote,
   Kalkulation, Verhandlung).

Dann eine einzige Zusatzfrage, in Alltagssprache: „Wie kommst du normalerweise
auf deinen Preis — Stundensatz, Tagessatz, Pauschale? Oder ist das jedes Mal
anders?" Die Antwort landet im Profilfeld `Wie du Preise bildest`.

Bleibt auch sie leer, ist das ein **funktionierender Zustand**, kein Fehler:
Die Skills markieren `[PREIS PRÜFEN]`, statt eine Zahl zu erfinden.

## Erledigt

**19.08.2026 — `{{preisgrundlage}}` entschieden.** Die frühere offene Frage
(„11. Frage aufnehmen oder bedingte Zusatzfrage?") ist mit `meine-unterlagen/`
hinfällig geworden: Die Preisgrundlage ist ein Dokument, kein Satz. Im Profil
trüge sie weder Stand noch Gültigkeit noch Kundenkonditionen — die Preisregeln
aus `core/unterlagen/preisregeln.md` hätten daran nichts zu prüfen. Das
Interview bleibt bei zehn Fragen. Protokolliert in `docs/entscheidungen.md`.

**20.08.2026 — Platzhalter werden nicht mehr ersetzt.** Sie bleiben als
Verweise stehen und werden beim Lesen aufgelöst (Abschnitt oben). Damit steht
Profilwissen beim Kunden genau einmal — so, wie es im Repo schon immer stand.
Protokolliert in `docs/entscheidungen.md`.
