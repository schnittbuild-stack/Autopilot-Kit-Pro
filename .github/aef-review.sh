#!/usr/bin/env bash
# Unabhaengiger Review-Runner
#
#   .github/aef-review.sh <pr-nummer>
#
# Startet eine frische, ausschliesslich lesende Claude-Sitzung, die den Pull Request
# gegen docs/work-orders/REVIEW.md prueft und ihr Urteil SELBST als PR-Kommentar postet.
#
# Zwei Eigenschaften sind Absicht, nicht Zufall:
#   1. Eigener Prozess, eigener Kontext — die Sitzung kennt die Ueberlegungen des
#      Builders nicht und kann sie deshalb nicht uebernehmen.
#   2. Sie postet selbst. Der Builder bekommt das Urteil nicht zuerst zu sehen und
#      kann ein FAIL weder abschwaechen noch unterschlagen.
#
# Diese Datei liegt unter .github/ und ist damit ein reservierter Pfad: Aenderungen
# daran brauchen die Freigabe des menschlichen Owners. Wer den Pruefer entschaerfen
# koennte, ohne dass jemand hinsieht, macht das ganze Verfahren wertlos.

set -euo pipefail

PR="${1:?Aufruf: .github/aef-review.sh <pr-nummer>}"
REPO="${AEF_REPO:-schnittbuild-stack/Autopilot-Kit-Pro}"

command -v claude >/dev/null || { echo "claude CLI nicht gefunden" >&2; exit 2; }
command -v gh >/dev/null     || { echo "gh CLI nicht gefunden" >&2; exit 2; }

PROMPT=$(cat <<PROMPT_END
Du bist ein unabhaengiger, ausschliesslich lesender Pruefer. Du hast diese Aenderung
nicht gebaut und kennst die Ueberlegungen des Erstellers nicht.

Pruefauftrag: Pull Request #${PR} in ${REPO}

Lies den Diff, die zugehoerige Work Order unter docs/work-orders/ und die betroffenen
Dateien. Aendere nichts: kein Commit, kein Push, keine Datei bearbeiten.

Der verbindliche Pruefvertrag steht in docs/work-orders/REVIEW.md. Lies ihn zuerst.
Vier Bereiche blockieren, und nur diese:
1. Korrektheit    - tut die Aenderung, was die Work Order zusagt?
2. Sicherheit     - Zugangsdaten, Rechteausweitung, Aussenwirkung?
3. Umfang         - liegt jede geaenderte Datei im file_allowlist? Etwas aus out_of_scope passiert?
4. Betreibbarkeit - traegt der Rollback? Bleibt der Zustand nachvollziehbar?

Du darfst die Testsuite und die Validierung ausfuehren, um Behauptungen zu pruefen
statt sie zu glauben:
  python3 -m unittest discover -s tests -p 'test*.py'
  python3 scripts/aef_validate.py --base-ref main
Nutze dafuer einen Interpreter ab Python 3.11; das System-python3 ist aelter.

Stil, Formulierung, Geschmack und harmlose Ergaenzungen sind NICHT blockierend.
Sie duerfen als Hinweis auftauchen, aber niemals zu FAIL fuehren. Ein Review, der
Geschmack zum Mangel erklaert, macht die Quittung zur Formsache.

Poste dein Urteil zum Schluss als Kommentar:
  gh pr comment ${PR} --repo ${REPO} --body "<dein urteil>"

Der Kommentar beginnt mit genau einer dieser Zeilen:
REVIEW: PASS
REVIEW: FAIL

Darunter die vier Bereiche, jeder Befund mit Datei und Zeile. Benenne ausdruecklich,
was du nicht pruefen konntest, statt es zu ueberspielen. Sei knapp.
PROMPT_END
)

echo "→ Unabhaengige Pruefsitzung fuer PR #${PR} …" >&2

claude -p "$PROMPT" \
  --allowedTools \
    "Read" "Grep" "Glob" \
    "Bash(gh pr view:*)" "Bash(gh pr diff:*)" "Bash(gh pr comment:*)" \
    "Bash(git log:*)" "Bash(git show:*)" "Bash(git diff:*)" "Bash(git status:*)" \
    "Bash(python3:*)" "Bash(*/.aef-tools/bin/python:*)"
