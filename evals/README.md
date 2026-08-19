# evals — Testprofil und Testlauf-Material

Liegt außerhalb des ausgelieferten Baums. Die Release-Action kopiert nur
`core/`, `adapter-claude/`, `notfall/` und `START_HIER.md` — dieser Ordner
kommt daher nie ins Kunden-ZIP, genauso wie `testfaelle-praxis/`.

- `testprofil.md` — erfundenes, vollständiges Profil. Füllt alle 12
  Platzhalter, damit die Skills laufen, bevor der Installer aus Phase 3
  echte Profile erzeugt.
- `meine-unterlagen/` — simuliert den Unterlagen-Ordner des Kunden
  (`core/unterlagen/aufbau.md`). Enthält die Preisliste, mit der die
  Angebots-Fälle rechnen. Testfälle, die eine andere Preislage brauchen —
  abgelaufen, kundenspezifisch —, beschreiben sie in der eigenen Datei und
  überschreiben damit diesen Ordner.

Ergebnisse eines Durchlaufs stehen in `docs/testlauf-phase2.md`.
