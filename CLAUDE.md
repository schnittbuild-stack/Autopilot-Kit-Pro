# Autopilot Kit — Arbeitsregeln für dieses Repo

Dieses Repo ist die einzige Quelle der Wahrheit für das Produkt "Autopilot Kit".
Jede Session (Mensch, Claude Code, Cowork) arbeitet nach diesen Regeln.

## Bei Session-Start — immer zuerst

1. Lies `docs/STATUS-BAU.md` — dort steht, was erledigt ist, welche Entscheidungen
   gefallen sind und was der nächste Schritt ist. Setze dort fort.
2. Lies `BAUPLAN.md` für die Phase, an der gerade gearbeitet wird.

## Die vier Bauprinzipien (nicht verhandelbar)

1. **Eine Quelle der Wahrheit.** Profil-, Firmen- und Stildaten stehen genau einmal
   (beim Kunden: `profil.md`). Skills referenzieren sie über Platzhalter, duplizieren
   sie nie. Kein Agent ändert gemeinsame Konfigurationsdateien selbst.
2. **Zustand auf der Platte.** Jeder mehrstufige Prozess schreibt seinen Fortschritt
   nach jedem Schritt in eine STATUS-Datei. Sessions dürfen jederzeit sterben —
   Kontextverlust ist kein Ereignis. Das gilt für den Kunden-Installer UND für
   unsere eigene Arbeit an diesem Repo.
3. **Übergabeverträge.** Wo ein Agent an einen anderen übergibt, ist das Format in
   `core/vertraege/` fest definiert. Interne Änderungen an einem Agenten sind erlaubt,
   Vertragsbrüche nicht. Neue Schnittstelle = erst Vertrag, dann Agenten.
4. **Kern ≠ Plattform.** Alles in `core/` ist plattformneutrales Markdown ohne
   Claude-Spezifika. Plattformwissen (Hooks, CLAUDE.md-Mechanik, Pfade) lebt nur in
   `adapter-claude/`. Die ChatGPT/Codex-Variante wird später ein weiterer Adapter.

## Git-Disziplin

- `main` ist immer auslieferbar. Gearbeitet wird auf Branches pro Fahrplan-Phase
  (`phase-2-skills`, `phase-3-installer`), Merge per Pull Request.
- Jede Arbeitssession endet mit Commits. Messages auf Deutsch, Präsens, konkret:
  `skills: angebots-schreiber v1 mit 3 Beispielen` statt `update`.
- Nach jedem inhaltlichen Meilenstein: `docs/STATUS-BAU.md` aktualisieren und
  mitcommitten. Eine Session, die STATUS nicht pflegt, ist nicht fertig.
- Entscheidungen (Preis, Zielgruppe, Architektur) werden in
  `docs/entscheidungen.md` protokolliert — mit Datum und Begründung.
- Releases per Tag `v2026.<minor>.<patch>`. Der Tag löst die GitHub Action aus,
  die das Kunden-ZIP baut. Niemals ZIPs von Hand bauen.

## Was NIE passiert

- Kein Profil-/Stilwissen in Skill-Dateien hartkodieren (Prinzip 1).
- Keine Claude-Spezifika in `core/` (Prinzip 4).
- Kein Inhalt aus `vermarktung/` oder `docs/` im Kunden-Release (regelt die Action).
- Keine Secrets, Keys oder Kundendaten in diesem Repo. Nirgends.
- Keine geschönten Testfälle. Lieber 4 harte als 20 weiche — eine geschönte
  Eval-Zahl zerstört das Produktversprechen öffentlich.

## Zielgruppe & Ton (Entscheidung vom 14.08.2026)

V1 richtet sich an **alle, die eine KI-Schulung gemacht haben** (LoAI, LinkedIn,
IHK, intern) und danach nicht ins Tun kommen — das After-Sales-Produkt zur Schulung.
Konsequenzen: Auslieferung als ZIP ist der Pflichtweg (GitHub nur optionaler
Update-Kanal), der Installer ist brutal idiotensicher (keine Vorkenntnisse, keine
API-Keys, kein Terminal-Wissen vorausgesetzt), Kundenansprache per **Du**,
jargonfrei. Jeder Text im Kit wird gegen die Frage geprüft: "Versteht das jemand,
der noch nie ein Terminal gesehen hat?"
