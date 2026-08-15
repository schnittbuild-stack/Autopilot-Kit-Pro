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
   muss nahtlos über STATUS.md fortsetzen. Erst wenn das klappt, ist Phase 3 fertig.
5. `notfall/` mit Diagnose-Prompts für die 5 häufigsten Fehlerbilder füllen.

Definition of Done: Kompletter Durchlauf auf einem FREMDEN, frisch aufgesetzten
Rechner unter 30 Minuten, inklusive eines erzwungenen Session-Abbruchs.

## Phase 4 — Watchdog & Ketten-Tests (Tag 6–8)

Ziel: Selbsttest-Modul als Skill in `adapter-claude/`.

1. Watchdog-Skill: liest `core/testfaelle/`, führt aus, vergleicht gegen Soll,
   erzeugt einen Bericht in Alltagssprache („3 von 10 Fällen weichen ab —
   soll ich den Fix einspielen?").
2. 5 Ketten-Testfälle Ende-zu-Ende mit Sollergebnissen.
3. Reparatur-Flow: Vorschlag → Nutzer bestätigt → STATUS.md protokolliert.

Definition of Done: Watchdog erkennt eine absichtlich eingebaute Abweichung in
der Kette und schlägt den korrekten Fix vor.

---

Parallel laufende Phasen (nicht in Claude Code): Smoke-Test/Ads (Phase 5) und
Beta (Phase 6) — siehe `docs/fahrplan.html`. Deren Erkenntnisse fließen als
Issues in dieses Repo zurück.
