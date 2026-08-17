# STATUS-BAU — Stand der Produktentwicklung

<!-- Unser eigenes Produkt-Prinzip, auf uns selbst angewandt: jede Session
     (Claude Code, Cowork, Mensch) liest diese Datei zuerst und pflegt sie. -->

## Stand
- [x] Phase 0 — Fundament: Entscheidungen getroffen (siehe docs/entscheidungen.md)
- [x] Phase 1 — Architektur & Repo-Skelett: Struktur, Vorlagen, Regeln, Action
- [ ] Phase 2 — Vertriebs-Skills & Verträge (BAUPLAN.md)
  - [x] Agent 1 `angebots-schreiber` gebaut, 3 Testfälle, Block-B-Übergabe skizziert
  - [ ] Kette definieren + Verträge in `core/vertraege/`
  - [ ] Agenten 2–10 (alle noch STUB)
- [ ] Phase 3 — Installer fertigstellen
- [ ] Phase 4 — Watchdog & Ketten-Tests
- [ ] Phase 5 — Smoke-Test (parallel, außerhalb dieses Repos: Ads + Landingpage)
- [ ] Phase 6 — Beta mit 10 Nutzern
- [ ] Phase 7 — Launch

## Offene Punkte
- Digistore24/CopeCart-Konto beantragen (Freischaltung dauert Tage)
- Produktname + Domain final
- START_HIER später zusätzlich als PDF (Markdown reicht für Beta)
- **Testfälle sind konstruiert, nicht aus der Praxis.** Die drei Fälle zu
  `angebots-schreiber` sind ehrlich hart, aber erfunden. Vor Beta gegen
  anonymisierte Realfälle tauschen — bis dahin taugen sie zur Entwicklung,
  nicht als Erfolgsquote nach außen.
- **`{{preisgrundlage}}` hat keine Interviewfrage** (siehe core/interview/mapping.md,
  Abschnitt „Offen"). In Phase 3 entscheiden.
- Repo liegt unter `schnittbuild-stack/Autopilot-Kit` (privat), nicht in der Org
  `Autopilot-Kit`. Transfer möglich, sobald ein Org-Token existiert.

## Nächster Schritt
Phase 2, Schritt 2+3 aus BAUPLAN.md: **Kette definieren, dann Verträge** —
`account-recherche → angebots-schreiber → follow-up-generator`. Zwei Verträge
in `core/vertraege/` nach `_TEMPLATE_VERTRAG.md`. Die Übergabe von
`angebots-schreiber` ist als Block B im Skill vorformuliert und wird die
Grundlage des zweiten Vertrags. Erst danach Agenten 2–10.
