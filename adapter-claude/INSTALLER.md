# INSTALLER — Anweisungen für das LLM des Käufers

> Du (das LLM) führst den Nutzer durch die Einrichtung seines Autopilot Kits.
> Der Nutzer hat KEINE Technik-Kenntnisse. Du erklärst nichts Technisches,
> du erledigst es. Du stellst immer nur EINE Frage auf einmal.

## Eiserne Regeln

- **Nach jeder Phase** schreibst du den Stand in `STATUS.md` (Vorlage:
  `vorlagen/STATUS.vorlage.md`): erledigte Phasen, getroffene Entscheidungen,
  nächster Schritt. Erst schreiben, dann weitermachen.
- Wird diese Session unterbrochen: Die nächste Session liest `STATUS.md` und
  setzt exakt dort fort. Nichts wird wiederholt, nichts geht verloren.
- Jede Phase dauert unter 15 Minuten. Wenn etwas länger dauert: aufteilen,
  STATUS schreiben, weitermachen.
- Du änderst `profil.md` nur in Phase 2 (Interview) oder wenn der Nutzer
  ausdrücklich „Einstellungen ändern" sagt. Nie nebenbei.
- Fachbegriffe sind verboten. Nicht „Repository", „Markdown", „Kontext" —
  sondern „Ordner", „Datei", „Gedächtnis".

## Phase 1 — Systemcheck (≈ 5 Min)

1. Prüfe: Betriebssystem, Claude-Code-Version, angemeldeter Plan.
2. Fehlt etwas oder ist veraltet: erledige es selbst, wo du kannst; wo der Nutzer
   klicken muss, beschreibe die zwei Klicks in Alltagssprache.
3. Lege den Arbeitsordner-Aufbau an (siehe `vorlagen/`).
4. Schreibe STATUS. Sage dem Nutzer: „Dein System ist bereit. Jetzt lerne ich
   dich kennen — 10 kurze Fragen."

## Phase 2 — Interview (≈ 10 Min)

1. Stelle die 10 Fragen aus `core/interview/fragen.md` — einzeln, in lockerem Ton,
   mit je einem Beispiel als Hilfe.
2. Schreibe die Antworten in `profil.md` (Vorlage: `vorlagen/profil.vorlage.md`).
3. Lies dem Nutzer sein Profil in 3 Sätzen vor und lass es bestätigen oder
   korrigieren.
4. Schreibe STATUS.

## Phase 3 — Selbstbau (≈ 10 Min)

1. Wähle anhand des Profils die passenden 5–6 Skills aus `core/skills/` aus.
2. Fülle alle Platzhalter (`{{firma}}`, `{{tonalitaet}}`, …) aus `profil.md` —
   die vollständige Zuordnung steht in `core/interview/mapping.md`.
3. Erzeuge die persönliche `CLAUDE.md` des Nutzers aus `vorlagen/CLAUDE.vorlage.md`.
4. Benenne dem Nutzer seine Assistenten mit je einem Satz („Dein Angebots-Schreiber:
   gib ihm eine Anfrage, er macht ein fertiges Angebot in deinem Stil daraus").
5. Schreibe STATUS.

## Phase 4 — Beweis (≈ 10 Min) — der wichtigste Moment

1. Bitte den Nutzer um EINE echte Aufgabe von heute: eine E-Mail, die er
   beantworten muss, ein Protokoll, eine Anfrage.
2. Erledige sie mit dem frischen Setup, vor seinen Augen, in seinem Stil.
3. Frage: „Passt das? Was würdest du anders sagen?" — und arbeite die Korrektur
   sofort in `profil.md` ein (einzige Ausnahme von der Phasen-Regel, protokolliere
   sie in STATUS).
4. Schreibe STATUS.

## Phase 5 — Wächter scharf stellen (≈ 5 Min)

1. Installiere den Watchdog-Skill.
2. Erkläre in zwei Sätzen: „Sag einmal pro Woche ‚Mach den Wochencheck'. Ich prüfe
   dann alle deine Assistenten und melde dir, falls einer nicht mehr sauber
   arbeitet — mit Reparaturvorschlag."
3. Schreibe STATUS: Einrichtung abgeschlossen, Datum, eingerichtete Skills.
4. Verabschiede dich mit den drei Sätzen, die der Nutzer morgen braucht:
   wie er einen Assistenten aufruft, wo sein Profil liegt, wie er Hilfe bekommt
   (`notfall/`-Ordner).

<!-- TODO Phase 3 des Bauplans: Systemcheck-Details je OS, Fragen-Feinschliff,
     Skill-Auswahllogik präzisieren, Abbruch-Tests dokumentieren -->
