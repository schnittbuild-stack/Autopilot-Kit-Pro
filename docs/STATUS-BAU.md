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
  - [x] Agenten 4–10 gebaut, je 3 Testfälle — alle 10 Skills sind stubfrei
  - [ ] **Definition of Done noch NICHT erreicht** — siehe unten
- [ ] Phase 3 — Installer fertigstellen
- [ ] Phase 4 — Watchdog & Ketten-Tests
- [ ] Phase 5 — Smoke-Test (parallel, außerhalb dieses Repos: Ads + Landingpage)
- [ ] Phase 6 — Beta mit 10 Nutzern
- [ ] Phase 7 — Launch

## Definition of Done Phase 2 — Prüfstand vom 17.08.2026

BAUPLAN verlangt: „Alle 10 Skills laufen einzeln gegen ihre Testfälle; die
Hauptkette läuft einmal Ende-zu-Ende durch."

**Geprüft und erfüllt (maschinell):**

- [x] 10 Skills gebaut, keine Stubs, alle 7 Pflichtabschnitte je Skill
- [x] 32 Testfälle (3 je Skill + 2 Ketten-Fälle), alle mit Eingabe,
      Soll-Ergebnis, Bewertung und Herkunftszeile
- [x] 11 Platzhalter, alle in `core/interview/mapping.md` registriert
- [x] `core/` frei von Plattform-Spezifika (Prinzip 4)
- [x] Beide Verträge geschrieben, Feldnamen stimmen mit den Skills überein
- [x] Release-Build läuft, Praxisordner bleibt draußen

**NICHT erfüllt — und das ist der eigentliche Teil der DoD:**

- [ ] **Kein einziger Testfall wurde ausgeführt.** Es liegen 32 Sollwerte vor
      und null Istwerte. Die Skills sind gebaut, nicht geprüft.
- [ ] Die Hauptkette ist nie Ende-zu-Ende gelaufen.

**Warum das gerade nicht geht — und was es kostet, es zu lösen:**

Die Skills stecken voller `{{platzhalter}}`, die erst das Installer-Interview
füllt (Phase 3). Ohne gefülltes Profil ist ein Durchlauf nicht aussagekräftig:
Ein Skill, der `{{tonalitaet}}` nicht auflösen kann, fällt aus Gründen durch,
die nichts mit seiner Qualität zu tun haben.

Der Ausweg ist ein **Testprofil**: ein erfundener, aber vollständiger
`profil.md`-Datensatz (Rolle, Firma, Ton, Anrede, Signatur, Verbote,
Preisgrundlage) allein für Evals, abgelegt außerhalb des Kundenbaums. Damit
laufen alle 32 Fälle, bevor der Installer existiert — und Phase 3 startet auf
geprüften statt auf vermuteten Skills.

**Zweite Einschränkung, ehrlich vermerkt:** Wer die Skills gebaut hat, sollte
sie nicht allein bewerten. Ein Durchlauf, bei dem dasselbe Modell schreibt und
benotet, ist ein schwacher Beleg. Für die Beta braucht es mindestens eine
Bewertung durch einen zweiten Durchgang mit ausschließlich den Testfall-Kriterien
im Kontext, ohne den Skill-Text.

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
- **Erledigt (17.08.2026): Der Graben bleibt intern.** Praxisfälle liegen in
  `testfaelle-praxis/` außerhalb des ausgelieferten Baums, ins ZIP gehen nur
  neutrale Referenzfälle und Ketten-Fälle. Die Release-Action prüft das und
  bricht ab statt still zu bereinigen; lokal gegen drei Fälle getestet (sauber /
  Praxisfall eingeschmuggelt / Datei ohne Herkunftszeile).
  **Offen bleibt die Gegenleistung dafür:** Phase 4 muss den Watchdog so bauen,
  dass er beim Kunden eigene Testfälle aus dessen Material erzeugt — sonst prüft
  der Käufer nur gegen unsere neutralen Fälle und nie gegen seinen echten Alltag.

## Nächster Schritt
**Testprofil anlegen und die 32 Fälle tatsächlich durchlaufen lassen.** Das
schließt Phase 2 ab. Konkret:

1. `evals/testprofil.md` — erfundenes, aber vollständiges Profil, außerhalb
   des ausgelieferten Baums (wie `testfaelle-praxis/`).
2. Alle 32 Fälle durchlaufen, Istwerte festhalten.
3. Bewertung in einem zweiten Durchgang, der nur die Kriterien sieht.
4. Abweichungen entweder im Skill beheben oder als bekannte Schwäche
   dokumentieren — nicht den Testfall weichspülen.

Erst danach Phase 3 (Installer). Die Reihenfolge lohnt: Ein Installer, der
ungeprüfte Skills ausrollt, verlagert jeden Fehler in die Beta.
