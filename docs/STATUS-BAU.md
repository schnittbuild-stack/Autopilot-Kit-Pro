# STATUS-BAU — Stand der Produktentwicklung

<!-- Unser eigenes Produkt-Prinzip, auf uns selbst angewandt: jede Session
     (Claude Code, Cowork, Mensch) liest diese Datei zuerst und pflegt sie. -->

## Stand
- [x] Phase 0 — Fundament: Entscheidungen getroffen (siehe docs/entscheidungen.md)
- [x] Phase 1 — Architektur & Repo-Skelett: Struktur, Vorlagen, Regeln, Action
- [ ] Phase 2 — Vertriebs-Skills & Verträge (BAUPLAN.md)
  - [x] Agent 1 `angebots-schreiber` gebaut, 3 Testfälle
  - [x] Hauptkette V1 festgelegt, 2 Verträge geschrieben, 2 Ketten-Testfälle
  - [x] `angebots-schreiber` auf Vertrag 2 nachgezogen (Block B = ÜBERGABE ANGEBOT)
  - [x] Agent 2 `account-recherche` + 3 Testfälle
  - [x] Agent 3 `follow-up-generator` + 3 Testfälle
  - [ ] Agenten 4–10 (noch STUB): ausschreibungs-analyse, crm-notiz-zu-schritt,
        einwand-sparring, forecast-erklaerer, meeting-nachbereitung,
        outreach-personalisierer, preisverhandlungs-sparring
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
- **Widerspruch: der Graben liegt im ZIP.** `core/testfaelle/README.md` nennt die
  Testfälle „der eigentliche Graben des Produkts … den kein Wettbewerber kopieren
  kann" — die Release-Action kopiert aber `core/` komplett ins Kunden-ZIP. Damit
  hat jeder Käufer (auch ein Wettbewerber für 299 €) das ganze Eval-Material.
  Vor dem ersten Release entscheiden: (a) Watchdog braucht die Fälle lokal, also
  bleibt es dabei und der Graben ist ein anderer; (b) nur Ketten-Fälle ausliefern,
  Skill-Fälle bleiben im Repo; (c) Fälle beim Kunden aus seinem eigenen Material
  erzeugen. Betrifft `.github/workflows/release.yml` und Phase 4.

## Nächster Schritt
Die verbleibenden **sieben Agenten** (4–10) nach dem Muster der ersten drei:
je Skill nach `_TEMPLATE_SKILL.md`, je 3 Testfälle, keine Ketteneinbindung.
Sie sind unabhängig voneinander — Reihenfolge frei, sinnvoll ist nach Nähe
zur Kette: `outreach-personalisierer`, `einwand-sparring`,
`meeting-nachbereitung`, `crm-notiz-zu-schritt`, `ausschreibungs-analyse`,
`preisverhandlungs-sparring`, `forecast-erklaerer`.

Danach Phase 2 Definition of Done prüfen: alle 10 Skills gegen ihre Testfälle,
Hauptkette einmal Ende-zu-Ende.
