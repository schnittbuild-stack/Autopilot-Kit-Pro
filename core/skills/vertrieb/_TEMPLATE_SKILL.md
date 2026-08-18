# {{SKILL_NAME}} — Vorlage für alle Vertriebs-Skills

<!-- Struktur ist verbindlich. Profil-/Stilwissen NUR über Platzhalter (Prinzip 1).
     Jeder neue Platzhalter wird in core/interview/mapping.md registriert.
     Die Bauregel direkt unten gilt für jedes Rollenpaket, nicht nur für Vertrieb.
     Sie beschreibt, wie diese Vorlage auszufüllen ist — sie wird nicht in den
     fertigen Skill hineinkopiert. -->

## Bauregel: Wo eine Regel steht (verbindlich)

**Regeln im Fließtext halten nicht. Regeln in Checkliste und Ausgabeformat
halten.**

Das ist kein Stilhinweis, sondern ein gemessener Befund: Im Testlauf Phase 2
folgten neun der dreizehn Abweichungen des ersten Durchlaufs demselben Muster.
Dieselbe Regel wurde ignoriert, solange sie erklärend im Prozesstext stand —
und eingehalten, sobald sie mit Zählvorgabe im Ausgabeformat und als Punkt in
der Checkliste stand. Beispiel: „Ein Satz, keine Rechtsberatung" im Fließtext
wurde zu drei Sätzen plus Haftungszusatz; als Formatvorgabe plus
Checklistenpunkt hielt sie.

Daraus die Bauregel für jeden Skill:

- Jede Regel, die eingehalten werden **muss**, steht an **zwei** Stellen:
  1. als Vorgabe im **Ausgabeformat** — mit Zählvorgabe, wo eine Menge gemeint
     ist („höchstens zwei Sätze", „genau ein nächster Schritt", „ein Feld je
     Zeile"), und
  2. als einzeln abhakbarer Punkt in der **Checkliste** am Ende der
     Qualitätsregeln.
- Der Prozesstext **darf** eine Regel erläutern und begründen — das Warum
  gehört dorthin. Er darf nicht ihr einziger Ort sein. Steht eine Muss-Regel
  nur im Fließtext, gilt sie als **nicht durchgesetzt**.
- Ein Checklistenpunkt ist mit ja/nein beantwortbar und ohne Auslegung prüfbar.
  „Angemessene Länge" ist kein Punkt. „Höchstens zwei Sätze" ist einer.
- Verbote werden prüfbar formuliert, nicht als Haltung: nicht „nicht zu
  ausführlich werden", sondern „Block B ist höchstens zwei Sätze lang".
- Bedingte Regeln nennen ihre Bedingung im Punkt selbst („entfällt, wenn die
  Frist abgelaufen ist"), damit die Prüfung ohne Rückgriff auf den Prozesstext
  möglich bleibt.

Gegenprobe vor jedem Commit an einem Skill: Jede Muss-Regel im Fließtext
heraussuchen und fragen — steht sie auch im Ausgabeformat **und** in der
Checkliste? Wenn nein, gehört sie dorthin, bevor der Skill fertig ist.

## Zweck (ein Satz)
Was dieser Assistent erledigt und für wen.

## Eingabe
Was der Nutzer liefert (E-Mail, Anfrage, Protokoll …) — und was passiert, wenn
etwas fehlt (nachfragen, nie raten).

## Prozess
Nummerierte Schritte. Konkret genug, dass zwei verschiedene Modelle dasselbe
Ergebnis liefern. Hier steht das Warum einer Regel — ihr verbindlicher Ort ist
trotzdem Ausgabeformat und Checkliste (siehe Bauregel oben).

## Ausgabeformat
Exakte Struktur des Ergebnisses: Felder, Reihenfolge, Längen als Zahl. Jede
Muss-Regel, die sich auf die Ausgabe auswirkt, steht hier — nicht nur im
Prozess. Wenn dieser Skill an einen anderen übergibt: Verweis auf den Vertrag
in core/vertraege/ — das Format dort ist bindend.

## Qualitätsregeln
- Ton: {{tonalitaet}}
- Absender/Signatur: {{signatur}}
- Niemals: {{verbote}}

Dazu die Checkliste, die vor der Ausgabe abgearbeitet wird — jeder Punkt
einzeln mit ja/nein:

- [ ] <prüfbare Einzelregel, ohne Auslegung beantwortbar>
- [ ] <je eine Zeile pro Muss-Regel aus Prozess und Ausgabeformat>
- [ ] <Verbote aus {{verbote}} als eigener Punkt>

## Beispiele
Mindestens 3, ideal 5 — echte, anonymisierte Fälle mit Eingabe und Soll-Ausgabe.

## Testfälle
Verweis auf core/testfaelle/<skill-name>/
