# BAUPLAN — Arbeitsanweisung für Claude-Code-Sessions

Du arbeitest am Autopilot Kit: einem Download-Produkt (299/499 €), mit dem sich das
LLM eines Käufers nach einer KI-Schulung selbst zu einem persönlichen Assistenten-Setup
konfiguriert. Zielgruppe: Menschen ohne Technik-Hintergrund, die eine KI-Schulung
gemacht haben und nicht ins Tun kommen.

Lies zuerst `CLAUDE.md` (Regeln) und `docs/STATUS-BAU.md` (aktueller Stand).
Arbeite die Phasen in Reihenfolge ab. Nach jedem erledigten Punkt: STATUS-BAU.md
aktualisieren, committen.

---

## Phase 2 — Vertriebs-Skills & Verträge (Tag 2–5)

Ziel: 10 Agenten des Vertriebspakets als Skill-Dateien in `core/skills/vertrieb/`,
jeder zu 80 % fertig — die letzten 20 % füllt später das Installer-Interview über
Platzhalter.

Reihenfolge (wichtig):
1. **Agent Nr. 1 zuerst komplett**: `angebots-schreiber.md` nach
   `_TEMPLATE_SKILL.md`, mit 5 echten Beispielen und 3 Testfällen. Er ist der
   Qualitätsmaßstab für alle anderen.
2. **Kette definieren**: Welche Agenten übergeben aneinander?
   (Vorschlag: account-recherche → angebots-schreiber → follow-up-generator.)
3. **Verträge VOR den restlichen Agenten**: für jede Schnittstelle eine Datei in
   `core/vertraege/` nach `_TEMPLATE_VERTRAG.md`.
4. Agenten 2–10 bauen. Platzhalter-Konvention strikt: `{{firma}}`, `{{tonalitaet}}`,
   `{{signatur}}`, `{{verbote}}` — vollständige Liste in
   `core/interview/mapping.md`, dort JEDE neue Platzhalter-Variable registrieren.
5. Pro Agent 3 Testfälle in `core/testfaelle/` nach `_TEMPLATE_TESTFALL.md`.

Definition of Done: Alle 10 Skills laufen einzeln gegen ihre Testfälle; die
Hauptkette läuft einmal Ende-zu-Ende durch.

## Phase 3 — Installer (Tag 4–7)

Ziel: `adapter-claude/INSTALLER.md` von Rohbau auf fertig. Der Rohbau definiert
die 5 Phasen und die Regeln (STATUS nach jeder Phase, <15 Min pro Phase,
Abbruch-Sicherheit). Aufgaben:

1. Interviewfragen aus `core/interview/fragen.md` final formulieren (max. 10) und
   gegen `adapter-claude/vorlagen/profil.vorlage.md` mappen.
2. Selbstbau-Logik: Skill-Auswahl (5–6 passende), Platzhalter füllen,
   Kunden-CLAUDE.md aus `CLAUDE.vorlage.md` erzeugen.
3. Phase „Beweis": echte Aufgabe des Käufers anfordern und live erledigen.
4. **Abbruch-Test**: Session in jeder Installer-Phase hart beenden — neue Session
   muss nahtlos über STATUS.md fortsetzen. Geprüft wird dabei **nicht nur, ob die
   Fortsetzung technisch klappt, sondern ob sie ohne jede Erklärung durch uns
   gelingt**: Die Testperson bekommt keinen Hinweis, keinen Übergabetext und
   keine Anleitung von uns — sie tippt „weiter". Wenn wir daneben sitzen und
   soufflieren müssen, ist der Test nicht bestanden. Erst wenn das klappt, ist
   Phase 3 fertig.
5. **Sitzungswechsel unsichtbar machen.** Ein Sitzungswechsel ist unser Problem,
   nicht das des Käufers. Er hat kein Wort für „Kontextfenster" und soll auch
   keines lernen müssen. Drei Bestandteile, alle drei Pflicht:
   1. **Ein Wort genügt.** Fortsetzen heißt **„weiter"** — mehr nicht. Nie ein
      Übergabeprompt, den der Nutzer formulieren, kopieren oder verstehen muss.
      Der Zustand kommt aus `STATUS.md`, nicht aus dem, was der Nutzer erzählt.
      Wenn die Fortsetzung davon abhängt, dass der Nutzer richtig zusammenfasst,
      ist sie falsch gebaut (Prinzip 2: Zustand auf der Platte).
   2. **Der Assistent bietet den Wechsel von sich aus an** — in Alltagssprache,
      nach abgeschlossenen Phasen und nach langen Aufgaben, mit dem Hinweis
      **„dein Stand ist gesichert"**. Der Nutzer soll nicht merken müssen, dass
      etwas voll läuft; er wird gefragt, ob er frisch weitermachen will.
   3. **Der Installer bringt es bei und legt es ab.** In Installer-Phase 5 ein
      Satz an den Nutzer, wie er weitermacht, wenn er später wiederkommt oder
      etwas abbricht. Dieselbe Anleitung zusätzlich in `notfall/`, damit sie
      auffindbar ist, wenn die Sitzung schon weg ist — genau dann kann er nicht
      mehr nachfragen.
6. `notfall/` mit Diagnose-Prompts für die 5 häufigsten Fehlerbilder füllen.

Definition of Done: Kompletter Durchlauf auf einem FREMDEN, frisch aufgesetzten
Rechner unter 30 Minuten, inklusive eines erzwungenen Session-Abbruchs, den die
Testperson **allein mit dem Wort „weiter"** überwindet — ohne Hilfestellung, ohne
Rückfrage an uns.

## Phase 4 — Watchdog & Ketten-Tests (Tag 6–8)

Ziel: Selbsttest-Modul als Skill in `adapter-claude/`.

1. Watchdog-Skill: liest `core/testfaelle/`, führt aus, vergleicht gegen Soll,
   erzeugt einen Bericht in Alltagssprache („3 von 10 Fällen weichen ab —
   soll ich den Fix einspielen?").
2. 5 Ketten-Testfälle Ende-zu-Ende mit Sollergebnissen.
3. Reparatur-Flow: Vorschlag → Nutzer bestätigt → STATUS.md protokolliert.
4. **Kundeneigene Testfälle erzeugen** (Entscheidung 17.08.2026). Der Watchdog
   baut aus dem Material des Käufers — echte Anfragen, verschickte Angebote,
   Mailverläufe, Stilbeispiele aus dem Interview — eigene Testfälle nach
   `_TEMPLATE_TESTFALL.md` und legt sie beim Kunden ab. Sie entstehen dort,
   bleiben dort und kommen nie zu uns zurück. Regeln: nur mit ausdrücklicher
   Zustimmung, Sollkriterien werden dem Nutzer zur Bestätigung vorgelegt (nicht
   vom Modell allein festgelegt), und ein selbstgebauter Fall wird als solcher
   markiert. Das ist die Gegenleistung dafür, dass unsere Praxisfälle das Repo
   nicht verlassen — ohne diesen Punkt prüft der Käufer nur gegen neutrale
   Fremdfälle und nie gegen seinen eigenen Alltag.

Definition of Done: Watchdog erkennt eine absichtlich eingebaute Abweichung in
der Kette und schlägt den korrekten Fix vor — **und** hat aus dem Material eines
Testkäufers mindestens 3 eigene Testfälle erzeugt, die dieser als treffend
bestätigt.

---

Parallel laufende Phasen (nicht in Claude Code): Smoke-Test/Ads (Phase 5) und
Beta (Phase 6) — siehe `docs/fahrplan.html`. Deren Erkenntnisse fließen als
Issues in dieses Repo zurück.
