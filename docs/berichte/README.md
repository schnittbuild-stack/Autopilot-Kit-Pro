# Berichte

Hier liegen die Berichte über Testläufe, Nachläufe und Untersuchungen —
**alles ab dem 28.08.2026.**

## Warum dieser Ordner

`docs/STATUS-BAU.md` und `docs/entscheidungen.md` müssen nach unseren eigenen
Regeln in jeder Sitzung gepflegt werden. Genau diese Pflege sperrte danach den
ordentlichen Merge, weil die Dateien nicht in `ordinary_paths` standen — drei
Pull Requests mussten deshalb über die manuelle Spur.

Der naheliegende Zuschnitt `docs/**` ist technisch ausgeschlossen: Muster mit
Stern müssen auf `/**` enden, und jedes `docs/**` überschneidet sich mit dem
reservierten `docs/agentic/**`, das auf der Pflichtliste des Validators steht.
Deshalb die beiden Dateien namentlich — und dieser Ordner für alles Weitere.

## Was hier nicht liegt

Die **14 Berichte bis zum 27.08.2026** bleiben in `docs/`. Ein Umzug hätte rund
25 Dateien angefasst, darunter die reservierte `CLAUDE.md`. Sie sind
abgeschlossen und werden nicht mehr geändert; wo sie zitiert werden, stimmen
die Pfade weiter.

Für den Kunden ändert sich nichts: `docs/` erreicht das Kunden-ZIP ohnehin
nicht (`release.yml`).
