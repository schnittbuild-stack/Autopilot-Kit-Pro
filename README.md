# Autopilot Kit (intern)

Download-Produkt: Das LLM des Käufers installiert und konfiguriert sich selbst
zu einem persönlichen Assistenten-Setup. Zielgruppe: Menschen nach einer
KI-Schulung, die nicht ins Tun kommen.

- Regeln & Prinzipien: `CLAUDE.md`
- Arbeitsanweisung für Bau-Sessions: `BAUPLAN.md`
- Aktueller Stand: `docs/STATUS-BAU.md`
- Fahrplan (interaktiv): `docs/fahrplan.html`
- Entscheidungen: `docs/entscheidungen.md`

Kunden-ZIP entsteht ausschließlich über einen Release-Tag (`v2026.x.y`).

## Governance

Dieses Repository arbeitet unter dem Autonomous Engineering Framework (AEF).

Der Mensch setzt die Produktrichtung und behält jede vorbehaltene Entscheidung. Arbeit wird
in begrenzte Work Orders geschnitten; Builder arbeiten ausschließlich innerhalb einer
Work Order und mergen oder veröffentlichen nie selbstständig.

- Pull Requests kommen von `@alexanderschnittcher-gif` (Builder).
- `@schnittbuild-stack` (Owner) bestätigt den exakten finalen Head sichtbar mit
  `AEF-APPROVE <head-sha>`, bevor der geschützte Workflow mergen darf.
- Frei bebaubar: `core/**`, `adapter-claude/**`, `notfall/**`, `evals/**`,
  `docs/work-orders/**`, `src/**`
- Owner-Review nötig: `.github/**`, `AGENTS.md`, `CLAUDE.md`, `governance/**`,
  `scripts/aef_*.py`, `docs/agentic/**`, `tests/test_aef_governance.py`

Codex liest `AGENTS.md` direkt. Claude Code liest `CLAUDE.md`, das dieselbe Datei importiert —
die Regeln stehen genau einmal. Beide Clients aus dem Repository-Wurzelverzeichnis starten.
Weiterführende `docs/agentic/`-Referenzen nur laden, wenn die aktive Work Order sie braucht.

Niemals einen App-Private-Key, Token oder andere Zugangsdaten in den Chat, nach
`.aef/profile.json`, in den Onboarding-Zustand, die Commit-History oder Nachweistexte schreiben.
