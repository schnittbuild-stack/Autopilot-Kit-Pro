# Gegenprobe: Wo stehen die bindenden Regeln?

Stand: 18.08.2026. Reine Lese-Prüfung aller zehn Vertriebs-Skills gegen die
Bauregel in `core/skills/vertrieb/_TEMPLATE_SKILL.md`. Keine Testläufe.

## Anlass

Der Ketten-Befund aus `docs/testlauf-phase2-regression.md` hatte eine
übertragbare Ursache: Die Bindung des Feldes `Nachfassen` stand **nur im
Prozess-Fließtext**. Genau das Muster, das die Bauregel verbietet:

> Regeln im Fließtext halten nicht. Regeln in Checkliste und Ausgabeformat
> halten.

Die Frage war also nicht, ob es weitere solche Stellen gibt, sondern wie viele.

## Verfahren

Zwei unabhängige Prüfer, je fünf Skills, ohne Kenntnis der Ergebnisse des
anderen. Gesucht wurde jede **Muss-Regel** (erkennbar an „nie", „immer",
„höchstens", „genau ein", „ausschließlich", „Abbruch", „Pflicht") aus
`## Eingabe`, `## Prozess` und den erläuternden Absätzen. Geprüft wurde je
Regel: Steht sie auch im **Ausgabeformat**? Steht sie auch in der
**Checkliste**?

- **Fund** = steht in keinem der beiden Anker.
- **Teilfund** = steht in genau einem der beiden.

## Ergebnis

| Skill | Funde | Teilfunde |
|---|---|---|
| `angebots-schreiber` | 8 | 5 |
| `einwand-sparring` | 5 | 2 |
| `account-recherche` | 4 | 3 |
| `follow-up-generator` | 4 | 2 |
| `preisverhandlungs-sparring` | 4 | 2 |
| `ausschreibungs-analyse` | 3 | 5 |
| `outreach-personalisierer` | 3 | 2 |
| `meeting-nachbereitung` | 2 | 2 |
| `forecast-erklaerer` | 2 | 3 |
| `crm-notiz-zu-schritt` | 1 | 4 |
| **Summe** | **36** | **30** |

**Keine der zehn Dateien war sauber.** Der Ketten-Befund war kein Einzelfall,
sondern der erste, den ein Testfall zufällig getroffen hat.

## Die drei Muster

1. **Abbruch- und Kein-Text-Regeln sind am schlechtesten verankert.**
   „Fehlt ein Pflicht-Fakt, entsteht kein Angebot", „`Stand: entwurf` → kein
   Text", „ohne Anknüpfungspunkt kein Text", „ohne Belegsatz kein Schritt" —
   fast alle standen allein im Fließtext. Das sind ausgerechnet die Regeln,
   deren Verletzung beim Kunden landet.
2. **Zählvorgaben schaffen es ins Format, aber nicht in die Checkliste.**
   „1 Satz", „1–3 Sätze", „2–3 Sätze", „genau 3 Sätze" — genau der Fall, an
   dem die Bauregel ihren ursprünglichen Befund festmacht.
3. **Regeln in der Checkliste, für die das Format keinen Ort hat.**
   Die Gegenrichtung: `crm-notiz-zu-schritt` verlangte eine getrennte
   Wiedervorlage, ohne Feld dafür; `ausschreibungs-analyse` verlangte eine
   Fragenliste an {{rolle}}, die bei `nicht bieten` nirgends stehen konnte.

## Zwei echte Widersprüche

Über die Verankerungsfrage hinaus fanden die Prüfer zwei Stellen, an denen ein
Skill sich selbst widersprach:

1. **`outreach-personalisierer`:** Prozess-Schritt 2 verlangte für die Brücke
   „**Ein Satz**", das Ausgabeformat „**1–2 Sätze**". Kein Testfall hängt daran.
   **Aufgelöst:** Der Prozesstext wurde auf „ein bis zwei Sätze" angeglichen;
   das Ausgabeformat bleibt, weil es der bindende Anker ist.
2. **`einwand-sparring`:** Der Checklistenpunkt „Im Sparring steht nichts außer
   der Kundenrede" verbot die in Prozess-Schritt 5 vorgeschriebene
   Klärungszeile. Der Testfall `02-rollenbruch` **verlangt** sie ausdrücklich —
   der Checklistenpunkt war also schlicht falsch.
   **Aufgelöst:** Der Punkt nennt die eine Klärungszeile jetzt als benannte
   Ausnahme. Der Testfall blieb unangetastet.

## Behebung

Alle 36 Funde und 30 Teilfunde sind verankert: 322 eingefügte, 33 ersetzte
Zeilen über zehn Dateien. Jede Ersetzung ist eine Verschärfung — geprüft wurde
zeilenweise, dass keine Zahl größer und keine Pflicht zur Empfehlung wurde.

Gegengeprüft nach der Behebung:

- Keine Claude- oder Plattform-Spezifika in `core/` (Prinzip 4).
- Kein hartkodiertes Profil-, Firmen- oder Stilwissen (Prinzip 1).
- Keine neuen Platzhalter — die neun benutzten sind in
  `core/interview/mapping.md` registriert.
- **`core/testfaelle/` unangetastet.** Kein Kriterium wurde angefasst.

## Was diese Gegenprobe nicht zeigt

Sie ist eine **Struktur**prüfung, keine Verhaltensprüfung. Sie belegt, dass die
Regeln jetzt an der Stelle stehen, an der sie erfahrungsgemäß halten — sie
belegt nicht, dass die Skills sich daran halten. Das zeigt erst der
Dreifachlauf. Alle zehn Skills sind durch diese Änderung berührt; damit sind
**alle 32 Testfälle gegen eine vorige Fassung gemessen**, auch die 13 aus
`docs/testlauf-phase2-regression.md`.

Der vollständige Dreifachlauf über alle 32 Fälle ist damit nicht mehr nur die
offene Kür aus der Definition of Done, sondern die Gegenprobe zu dieser
Umbauaktion.
