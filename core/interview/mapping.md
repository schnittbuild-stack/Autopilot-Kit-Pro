# Platzhalter-Register (verbindlich)

Jeder Platzhalter, der in irgendeinem Skill vorkommt, steht hier — mit der
Quelle, die ihn füllt. Neuer Platzhalter ohne Eintrag hier = Baufehler.

Es gibt drei Quellen (Entscheidung 19.08.2026):

- **Profil** — Dauerwissen über die Person, aus dem Interview (Phase 2).
- **Unterlagen** — Firmenwissen, das der Nutzer als Datei in
  `meine-unterlagen/` ablegt. Siehe `core/unterlagen/aufbau.md`.
- **Standardwert** — vom Installer gesetzt, ohne Frage, im Profil änderbar.

| Platzhalter | Quelle | Inhalt |
|---|---|---|
| {{rolle}} | Profil, Frage 1 | Job/Rolle des Nutzers |
| {{firma}} | Profil, Frage 2 | Firma und Branche |
| {{nervaufgaben}} | Profil, Frage 3 | Die drei wiederkehrenden Schmerzpunkte |
| {{tools}} | Profil, Frage 4 | Genutzte Programme |
| {{tonalitaet}} | Profil, Frage 5 + Material aus Frage 9 | Förmlich/locker, abgeleitet aus Beispielen |
| {{anrede}} | Profil, Frage 6 | Du/Sie gegenüber Kunden |
| {{signatur}} | Profil, Frage 7 | E-Mail-Signatur wörtlich |
| {{verbote}} | Profil, Frage 8 | No-Gos in Formulierung und Inhalt |
| {{stilbeispiele}} | **Unterlagen**, angestoßen von Frage 9 | Verweis auf `meine-unterlagen/stilbeispiele/` und `meine-unterlagen/angebote/` |
| {{erfolgsmoment}} | Profil, Frage 10 | Woran der Nutzer Erfolg misst (für Phase Beweis) |
| {{preisgrundlage}} | **Unterlagen**, angestoßen von Frage 9; ersatzweise bedingte Zusatzfrage | Verweis auf `meine-unterlagen/preise/` — Preisliste, Kalkulationsgrundlage, Kundenkonditionen. Ist dort nichts und wird auch die Zusatzfrage nicht beantwortet, bleibt der Wert leer und preisbildende Skills markieren `[PREIS PRÜFEN]` statt zu raten |
| {{preisfrist}} | **Standardwert** — 6 Monate, keine Frage | Wie lange ein Preisstand ohne Rückfrage gilt. Danach fragt der Skill **einmal** nach, statt stillschweigend weiterzurechnen (`core/unterlagen/preisregeln.md`) |

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
anders?" Die Antwort landet im Profilfeld `Preisgrundlage`.

Bleibt auch sie leer, ist das ein **funktionierender Zustand**, kein Fehler:
Die Skills markieren `[PREIS PRÜFEN]`, statt eine Zahl zu erfinden.

## Erledigt

**19.08.2026 — `{{preisgrundlage}}` entschieden.** Die frühere offene Frage
(„11. Frage aufnehmen oder bedingte Zusatzfrage?") ist mit `meine-unterlagen/`
hinfällig geworden: Die Preisgrundlage ist ein Dokument, kein Satz. Im Profil
trüge sie weder Stand noch Gültigkeit noch Kundenkonditionen — die Preisregeln
aus `core/unterlagen/preisregeln.md` hätten daran nichts zu prüfen. Das
Interview bleibt bei zehn Fragen. Protokolliert in `docs/entscheidungen.md`.
