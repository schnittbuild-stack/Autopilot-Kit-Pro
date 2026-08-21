# Unabhängiger Review

Jede Work Order braucht vor dem geschützten Merge eine Abnahme-Quittung. Diese Datei
legt fest, wer sie ausstellt und wie. Grundlage ist `docs/agentic/ACCEPTANCE-GATE.md`;
hier steht die konkrete Ausführung für dieses Repository.

## Warum getrennt

Wer gebaut hat, kann seine eigene Arbeit nicht abnehmen. Nicht aus Misstrauen, sondern
weil er die Annahmen kennt, unter denen er gebaut hat — und genau die sind der blinde
Fleck. Der Review prüft deshalb aus einer Sitzung, die diesen Kontext nicht hat.

`scripts/aef_validate.py` erzwingt das an zwei Stellen: Das Feld `reviewer_subject`
muss mit `readonly-process:` beginnen, und es darf nicht mit `approver_subject`
übereinstimmen. Bauender, Prüfender und Freigebender sind damit drei verschiedene
Rollen — auch wenn ein Mensch am Ende alle drei anstößt.

## Ablauf

1. **Builder** legt die Work Order an, arbeitet ausschließlich innerhalb des
   `file_allowlist`, lässt die Tests laufen und öffnet den Pull Request.
2. **Prüfende Sitzung** wird frisch gestartet. Sie erhält genau drei Angaben:
   Repository, PR-Nummer und den Prüfauftrag — **keine Begründung des Builders**.
3. Sie arbeitet **ausschließlich lesend**: Diff, Work Order, betroffene Dateien.
   Kein Commit, kein Push, keine Änderung.
4. Sie postet ihr Urteil als **Kommentar am Pull Request**.
5. Bei `PASS` bindet der Builder die Quittung:

       python3 scripts/aef_scaffold_work_order.py bind <work-order.json> \
         --reviewer-subject readonly-process:claude-review \
         --evidence-ref readonly-review:<kommentar-url>

6. Beide Pflicht-Checks laufen grün. **Der menschliche Owner merged**.

Bei `FAIL` gilt `ACCEPTANCE-GATE.md`: eine Korrektur, ein erneuter Review, danach
anhalten und neu planen. Nicht beliebig oft nachbessern.

## Was der Review prüft

Materielle Mängel in vier Bereichen — und nur diese blockieren:

- **Korrektheit** — tut die Änderung, was die Work Order zusagt, und stimmt sie mit
  den Testaussagen überein?
- **Sicherheit** — Zugangsdaten, Rechteausweitung, unbeabsichtigte Außenwirkung.
- **Umfang** — liegt jede geänderte Datei im `file_allowlist`? Ist etwas passiert,
  das unter `out_of_scope` steht?
- **Betreibbarkeit** — ist der Rollback belastbar? Bleibt der Zustand nachvollziehbar?

**Nicht blockierend:** Stil, Formulierung, Geschmack, harmlose Ergänzungen. Sie dürfen
als Hinweis im Kommentar stehen, aber nie zu `FAIL` führen. Ein Review, der Geschmack
zum Mangel erklärt, macht das Verfahren wertlos — dann wird die Quittung zur Formsache.

## Format des Urteils

Der Kommentar beginnt mit genau einer dieser Zeilen:

    REVIEW: PASS
    REVIEW: FAIL

Darunter die geprüften Bereiche, jeder Befund mit Datei und Zeile. Bei `PASS` ohne
Befunde genügt ein Satz je Bereich. Unsicherheit wird benannt, nicht überspielt:
Was die Sitzung nicht prüfen konnte, steht ausdrücklich als ungeprüft da.
