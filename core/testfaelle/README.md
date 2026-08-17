# Testfälle (Evals)

Pro Skill ein Unterordner mit mindestens 3 Fällen, dazu `ketten/` mit
Ende-zu-Ende-Durchläufen der Hauptkette.

Grundregel: Lieber 4 ehrlich harte Testsätze als 20 geschönte.

## Was hier liegt — und was nicht

In diesem Ordner liegen **neutrale Referenzfälle**. Sie sind konstruiert, hart
und tragen in Zeile 3 den Marker `Herkunft: konstruiert`. Sie werden mit
ausgeliefert, damit der Watchdog beim Kunden vom ersten Tag an etwas zu prüfen
hat.

Testfälle aus echter Beratungspraxis liegen **nicht hier**, sondern in
`testfaelle-praxis/` außerhalb des ausgelieferten Baums. Die Release-Action
bricht ab, wenn ein Praxisfall im Kunden-ZIP auftaucht oder wenn eine Datei
hier keine Herkunftszeile trägt.

## Die drei Sorten Testfälle

| Sorte | Wo | Wofür |
|---|---|---|
| Neutrale Referenzfälle | `core/testfaelle/` | Grundprüfung, geht mit ins ZIP |
| Praxisfälle | `testfaelle-praxis/` | unser schärferer Maßstab, bleibt intern |
| Kundeneigene Fälle | entstehen beim Käufer | erzeugt der Watchdog in Phase 4 aus dem Material des Käufers, bleiben auf dessen Rechner |

Die dritte Sorte ist der Grund, warum die zweite das Repo nicht verlassen muss:
Was beim Kunden zählt, sind seine eigenen Fälle in seinem eigenen Stil — nicht
unsere.
