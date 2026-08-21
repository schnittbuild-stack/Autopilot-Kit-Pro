# meeting-nachbereitung

<!-- Agent Nr. 6. Keine Ketteneinbindung in V1.
     Kein Profil-/Stilwissen hier (Prinzip 1). -->

## Zweck (ein Satz)
Macht aus Notizen eines Kundentermins ein Protokoll, das zwischen **zugesagt**,
**angedacht** und **unklar** unterscheidet — statt alles zu Aufgaben zu machen.

## Eingabe

**Pflicht:** die Notizen — Stichworte, Mitschrift, Diktat, Transkript, egal
wie roh.

**Optional:** Datum, Teilnehmer, Anlass, vorheriges Protokoll.

Fehlen Datum oder Teilnehmer und lassen sie sich nicht aus den Notizen
belegen, kommen sie in die Unklar-Liste. Sie werden nicht geschätzt.

## Prozess

1. **Verbindlichkeit einstufen.** Das ist die eigentliche Arbeit dieses
   Skills. Jede Aussage bekommt genau eine Stufe:

   | Stufe | Erkennungsmerkmal | Landet in |
   |---|---|---|
   | **zugesagt** | Wer + Was + Bis wann sind belegt | Aufgaben |
   | **angedacht** | „könnten wir mal", „wäre interessant", „schauen wir uns an" | Unverbindlich |
   | **unklar** | verbindlich gemeint, aber Wer oder Bis wann fehlt | Unklar |

   „Wir schauen uns das mal an" ist **angedacht**, nicht zugesagt — auch wenn
   es im Termin nach Fortschritt klang. Wer aus solchen Sätzen Aufgaben mit
   Datum macht, produziert ein Protokoll, dem der Kunde bei der nächsten
   Sitzung widerspricht.
2. **Belegen.** Jede Zeile in Aufgaben und Entscheidungen trägt den Satz aus
   den Notizen, auf den sie sich stützt — verkürzt, aber wörtlich.
   **Belegt heißt belegt, auch wenn es verkürzt notiert ist.** „15.8." ist ein
   Datum, „Nortmann" ist ein Name, „Okt." ist ein Monat. Solche Kürzel werden
   aufgelöst — das Jahr aus dem Zusammenhang — und als **belegt** geführt, nicht
   in die Unklar-Liste geschoben. Die Regel „nie raten" schützt vor Erfindung,
   nicht vor Lesen. Wer {{rolle}} nach etwas fragt, das sie oder er zwei Zeilen
   vorher selbst aufgeschrieben hat, verbrennt genau das Vertrauen, das die
   Regel aufbauen soll.
3. **Seiten trennen.** Was {{rolle}} tun muss und was der Kunde zugesagt hat,
   stehen getrennt. Vermischt kann niemand daraus arbeiten.
4. **Widersprüche stehen lassen.** Nennen die Notizen zwei verschiedene
   Termine, Zahlen oder Zuständige, werden **beide** aufgeführt und der
   Widerspruch benannt. Nicht die plausiblere Variante wählen, nicht glätten.
5. **Nichts ergänzen.** Keine Teilnehmer, keine Themen, keine „üblichen"
   nächsten Schritte, die nicht besprochen wurden. Ein Protokoll ist keine
   Vervollständigung.
6. **Fragen bündeln.** Zu jedem Unklar-Punkt genau eine Frage, alle am Ende
   in einer Liste — beantwortbar in zwei Minuten.
7. **Selbstprüfung** gegen die Checkliste.

## Ausgabeformat

```
<Jede Aussage aus den Notizen: genau eine Stufe, genau ein Block — nie in zweien.>

Termin:            <Datum, Anlass> | unklar
Teilnehmer:        <Namen, Rollen> | unklar
Worum es ging:     2–3 Sätze, sachlich

Entscheidungen:    <je Zeile: Entscheidung — Beleg, wörtlich aus den Notizen> | —

Aufgaben {{rolle}}:
  | Wer | Was | Bis wann | Beleg (wörtlich) |

Zugesagt vom Kunden:
  | Wer | Was | Bis wann | Beleg (wörtlich) |

Unverbindlich:     <Angedachtes, ausdrücklich ohne Aufgabe> | —
Widersprüche:      <je Zeile: beide Varianten + Fundstellen> | —
Unklar:            <je Zeile: was fehlt> | —
Nächster Termin:   <Datum> | nicht vereinbart

Fragen an dich:    <nummeriert, eine je Unklar-Punkt> | —
```

## Qualitätsregeln

- **Ton:** {{tonalitaet}}
- **Niemals:** {{verbote}}

Checkliste für Schritt 7:

- [ ] Keine Aufgabe ohne alle drei Angaben — Wer, Was, Bis wann. Unvollständig
      heißt Unklar, nicht „bis KW 34" geraten.
- [ ] Keine Aufgabe aus einer angedachten Äußerung.
- [ ] Jede Aussage steht in genau einem Block — keine Aussage taucht in
      zwei Blöcken auf.
- [ ] Jede Aufgabe und jede Entscheidung hat einen Beleg aus den Notizen.
- [ ] Jeder Beleg steht wörtlich in den Notizen — verkürzen erlaubt,
      umformulieren nicht.
- [ ] Keine Namen, Zahlen, Termine oder Themen, die nicht in den Notizen
      stehen.
- [ ] Widersprüche sind benannt, nicht aufgelöst.
- [ ] Kundenzusagen stehen nicht bei den eigenen Aufgaben.
- [ ] `Nächster Termin` steht auf „nicht vereinbart", wenn keiner vereinbart
      wurde — nicht auf einem Vorschlag.
- [ ] `Worum es ging` ist höchstens 3 Sätze lang.
- [ ] Zu jedem Punkt in `Unklar` steht genau eine Frage in `Fragen an dich`.
- [ ] Nichts aus {{verbote}}.
- [ ] Nichts steht in `Unklar`, was in den Notizen belegt ist — verkürzte
      Datums-, Monats- und Namensangaben zählen als belegt.

## Beispiele

> Stilneutral — der Ton kommt aus {{tonalitaet}}.

**Beispiel 1 — klare Zusage.** „Herr Brandt schickt uns die Stückliste bis
Freitag." → Aufgabe beim Kunden, alle drei Angaben belegt.

**Beispiel 2 — weiche Formulierung.** „Das mit der zweiten Schicht schauen
wir uns nochmal an." → `Unverbindlich`, keine Aufgabe, kein Datum. Frage in
der Liste: „Soll daraus eine Aufgabe werden — wer und bis wann?"

**Beispiel 3 — Widerspruch.** Notizen enthalten „Liefertermin Ende
September" und weiter unten „Livegang 15.10.". → Beide aufgeführt,
Widerspruch benannt, keine Auswahl.

**Beispiel 4 — Stichwortnotizen.** „Preis nochmal rechnen. Muster
schicken. Termin Okt." → Drei Aufgaben ohne Verantwortlichen, alle in
`Unklar`, drei gezielte Fragen. Nicht stillschweigend {{rolle}} zuschreiben,
nur weil sie oder er die Notizen gemacht hat.

## Testfälle

`core/testfaelle/meeting-nachbereitung/` — weiche Zusage, Widerspruch,
Stichwortnotizen.
