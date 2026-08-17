# crm-notiz-zu-schritt

<!-- Agent Nr. 7. Keine Ketteneinbindung in V1.
     Kein Profil-/Stilwissen hier (Prinzip 1). -->

## Zweck (ein Satz)
Leitet aus einer CRM-Notiz **genau einen** nächsten Schritt ab — und schlägt
das Schließen vor, wenn die Notiz das hergibt.

## Eingabe

**Pflicht:** die Notiz, so wie sie im CRM steht.

**Optional:** Stand der Opportunity, Datum, bisherige Historie, Wert.

## Prozess

1. **Belegsatz suchen.** Welcher Satz der Notiz trägt einen nächsten Schritt?
   Er wird wörtlich zitiert. **Gibt es keinen, entsteht kein Schritt** — dann
   Rückfrage. Ein Schritt ohne Belegsatz ist Vertriebsfolklore, kein Ergebnis
   aus dieser Notiz.
2. **Signal einstufen:** Fortschritt, Stillstand, Ende oder unklar. Diese
   Einstufung entscheidet über alles Weitere und wird mit ausgegeben, damit
   {{rolle}} sie widersprechen kann.
3. **Ergebnis wählen** — genau eines der vier:
   - **Aktion** — mit Wer, Was, Bis wann
   - **Wiedervorlage ohne Aktion** — mit Datum und Grund
   - **Schließen** — mit Grund
   - **Rückfrage** — die Notiz trägt keinen Schritt

   **Schließen ist ein vollwertiges Ergebnis, kein Versagen.** Eine tote
   Opportunity im Trichter kostet Forecast-Genauigkeit und Nachfass-Zeit.
   Wer sie am Leben hält, weil ein Assistent immer einen Rettungsversuch
   findet, betrügt sich selbst.
4. **Nur ein Vorschlag.** Keine Auswahl aus drei Möglichkeiten — das schiebt
   die Entscheidung zurück, für die dieser Skill da ist. {{rolle}} kann
   widersprechen, das genügt.
5. **Überprüfbar formulieren.** „Beziehung vertiefen", „Mehrwert liefern",
   „am Ball bleiben" sind keine Schritte. Ein Schritt hat ein Verb, ein
   Objekt und ein Datum.
6. **CRM-Zeile bauen.** Höchstens zwei Zeilen, direkt zum Einfügen.
7. **Selbstprüfung.**

## Ausgabeformat

```
Signal:        fortschritt | stillstand | ende | unklar
Belegsatz:     "<wörtlich aus der Notiz>"
Ergebnis:      aktion | wiedervorlage | schliessen | rueckfrage
  Wer:         <…>          (nur bei aktion)
  Was:         <…>          (nur bei aktion)
  Bis wann:    <Datum>      (bei aktion und wiedervorlage)
  Grund:       <1 Satz>     (bei wiedervorlage und schliessen)
Begründung:    1 Satz — warum dieser Schritt aus dem Belegsatz folgt
CRM-Zeile:     <max 2 Zeilen, copy-paste-fertig>
```

Bei `rueckfrage` entfallen die Unterfelder; stattdessen die eine Frage, die
den Schritt entscheidbar macht.

## Qualitätsregeln

- **Ton:** {{tonalitaet}}
- **Niemals:** {{verbote}}

Checkliste für Schritt 7:

- [ ] Genau ein Ergebnis, keine Optionsliste.
- [ ] Der Belegsatz steht **wörtlich** in der Notiz — nicht sinngemäß.
- [ ] Kein erfundener Ansprechpartner, kein erfundener Termin, kein
      erfundener Wettbewerber.
- [ ] Der Schritt ist überprüfbar: Verb, Objekt, Datum.
- [ ] Belegt die Notiz das Ende, steht `schliessen` da — kein Rettungsversuch,
      keine „letzte Chance"-Mail.
- [ ] Kein Schritt, der den Kunden gegen ein belegtes Desinteresse bearbeitet.
- [ ] Die CRM-Zeile passt in zwei Zeilen und enthält keine Markierungen wie
      `[PREIS PRÜFEN]`.
- [ ] Nichts aus {{verbote}}.

## Beispiele

> Stilneutral — der Ton kommt aus {{tonalitaet}}.

**Beispiel 1 — Fortschritt.** Notiz: „Technik ist überzeugt, Freigabe muss
noch durch den Einkauf, Frau Adam ist dort zuständig." → `aktion`: Termin mit
Frau Adam anfragen, bis Freitag. Belegsatz ist der Halbsatz zum Einkauf.

**Beispiel 2 — Ende.** Notiz: „Haben sich für den Wettbewerber entschieden,
Vertrag ist unterschrieben." → `schliessen`, Grund: Vergabe erfolgt. Kein
Nachfassen, keine Frage nach dem Warum als Rettungsversuch. (Eine
Verlustanalyse ist ein eigener Vorgang, kein nächster Schritt in dieser
Opportunity.)

**Beispiel 3 — Stillstand mit Grund.** Notiz: „Projekt liegt bis zum
Geschäftsjahreswechsel auf Eis, Budget erst ab Januar." → `wiedervorlage`
zum 10.01., Grund: Budgetfreigabe. Keine Aktion dazwischen.

**Beispiel 4 — keine Substanz.** Notiz: „Kurz telefoniert, war nett." →
`rueckfrage`: „Was war das Ergebnis — gibt es einen offenen Punkt oder eine
Zusage?" Kein erfundener Schritt.

## Testfälle

`core/testfaelle/crm-notiz-zu-schritt/` — verlorene Opportunity, leere Notiz,
Ansprechpartner weg.
