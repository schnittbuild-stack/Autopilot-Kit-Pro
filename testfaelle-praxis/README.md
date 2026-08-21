# Praxis-Testfälle — intern, verlassen das Repo nie

<!-- Entscheidung vom 17.08.2026, siehe docs/entscheidungen.md -->

Hier liegen die Testfälle aus echter Beratungspraxis. Sie sind das
Qualitätsmaterial, gegen das wir vor jedem Release prüfen — und sie werden
**nicht ausgeliefert**.

## Warum dieser Ordner außerhalb von `core/` liegt

Die Release-Action kopiert `core/`, `adapter-claude/`, `notfall/` und
`START_HIER.md` ins Kunden-ZIP. Alles andere im Repo wird gar nicht erst
angefasst. Ein Praxisfall, der hier liegt, kann deshalb **nicht** versehentlich
im ZIP landen — das ist sicherer als jede Ausschlussliste, die man pflegen muss.

## Die zwei Herkunftsklassen

Jeder Testfall im ganzen Repo trägt in Zeile 3 eine Herkunftszeile:

| Marker | Wo die Datei liegt | Wird ausgeliefert |
|---|---|---|
| `Herkunft: konstruiert` | `core/testfaelle/` | **ja** — neutraler Referenzfall |
| `Herkunft: praxis` | `testfaelle-praxis/` | **nein** |

Die Release-Action prüft beides und **bricht ab**, wenn ein Fall mit
`Herkunft: praxis` im Kunden-Build auftaucht oder wenn eine Datei unter
`core/testfaelle/` gar keine Herkunftszeile hat. Unbekannte Herkunft wird
wie Praxismaterial behandelt.

Sie repariert das nicht still. Ein Praxisfall im Build ist ein Fehler im Repo,
kein Fehler im Release — und er gehört im Repo behoben.

## Pflicht vor dem Ablegen: anonymisieren

Kein Kundenname, keine Person, keine Adresse, keine Auftragsnummer, keine
Beträge, die einen Vorgang eindeutig machen. Ersetzen durch `[Kunde]`,
`[Ansprechpartner]` und gerundete Beträge. Das Repo enthält keine Kundendaten —
auch nicht in einem Ordner, der nicht ausgeliefert wird.

## Aufbau

Gleiche Struktur wie `core/testfaelle/`: ein Unterordner pro Skill, dazu
`ketten/`. Format nach `core/testfaelle/_TEMPLATE_TESTFALL.md`.

## Verhältnis zu den neutralen Fällen

Die konstruierten Fälle in `core/testfaelle/` werden **nicht** durch
Praxisfälle ersetzt — beide bleiben nebeneinander bestehen:

- Die neutralen Fälle gehen mit und geben dem Watchdog beim Kunden vom ersten
  Tag an etwas zu prüfen.
- Die Praxisfälle bleiben hier und sind der schärfere Maßstab für uns.

Dazu kommt in Phase 4 die dritte Sorte: Testfälle, die der Watchdog **beim
Kunden aus dessen eigenem Material erzeugt**. Die entstehen erst auf dem
Rechner des Käufers, liegen nur dort und sind der eigentliche Grund, warum
unser Praxismaterial das Repo nicht verlassen muss.
