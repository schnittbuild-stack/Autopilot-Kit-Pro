# angebots-schreiber

<!-- Agent Nr. 1 — Qualitätsmaßstab für alle weiteren Skills.
     Struktur nach _TEMPLATE_SKILL.md (verbindlich).
     Enthält bewusst KEIN Stil- oder Firmenwissen — das kommt ausschließlich
     über Platzhalter aus profil.md (Prinzip 1). -->

## Zweck (ein Satz)
Macht aus einer Kundenanfrage ein versandfertiges Angebot im Hausstil von
{{firma}} — und sagt offen dazu, worauf es geraten hätte, wenn es geraten hätte.

## Eingabe

**Pflicht:** die Anfrage in beliebiger Form — E-Mail, Telefonnotiz, Gesprächs-
protokoll, Ausschreibungsauszug, drei hingeworfene Stichpunkte.

**Optional:** Ergebnis aus `account-recherche`, frühere Angebote an denselben
Kunden, Preisliste oder Kalkulationsvorlage.

**Die sechs Pflicht-Fakten.** Ohne diese sechs entsteht kein Angebot:

1. **Wer** fragt an — Firma, Ansprechpartner, Rolle
2. **Was** wird gebraucht — Leistung, Umfang, Menge
3. **Wozu** — welches Problem der Kunde damit löst
4. **Bis wann** — Termin, Frist oder Zeitraum
5. **Preisgrundlage** — aus {{preisgrundlage}} oder aus der Anfrage
6. **Empfänger-Verhältnis** — Neukunde oder Bestandskunde

Fehlt einer davon, wird **nachgefragt, nie geraten**. Regel: alle fehlenden
Punkte in **einer** Nachricht als nummerierte Fragen, dann anhalten. Nicht
zwei Runden Rückfragen, nicht ein Angebot mit Lücken „zum Drüberschauen".

Einzige Ausnahme: Fehlt **nur** die Preisgrundlage, wird das Angebot geschrieben
und die Preiszeile als `[PREIS PRÜFEN]` markiert (siehe Prozess Schritt 4).

## Prozess

1. **Fakten ziehen.** Die Anfrage lesen und die sechs Pflicht-Fakten wörtlich
   herausschreiben — mit Fundstelle („steht in Absatz 2"). Was nicht dasteht,
   bleibt leer. Nichts sinngemäß ergänzen.
2. **Lücken prüfen.** Leere Pflicht-Fakten → Rückfragen stellen und anhalten
   (siehe Eingabe). Sonst weiter.
3. **Leistung gliedern.** Den Auftrag in 3 bis 7 Positionen zerlegen. Jede
   Position hat genau drei Angaben: *Was passiert*, *in welchem Umfang*,
   *was der Kunde am Ende in der Hand hält*. Keine Position ohne Ergebnis —
   „Beratung" ist keine Position, „Beratung: 2 Workshops à 3 h, Ergebnis:
   schriftliches Konzept" ist eine.
4. **Preis rechnen.** Nach {{preisgrundlage}}. Zwei harte Regeln:
   - Die Summe muss die Summe der Einzelpositionen sein. Nachrechnen, bevor
     die Zahl im Text landet.
   - Gibt es keine tragfähige Grundlage für eine Position, kommt dort
     `[PREIS PRÜFEN]` hin — nie eine plausibel klingende Zahl. Ein erfundener
     Preis ist der teuerste Fehler, den dieser Assistent machen kann.
5. **Budget-Konflikt offenlegen.** Nennt der Kunde ein Budget, das den Umfang
   aus Schritt 3 nicht deckt, wird der Umfang **nicht** stillschweigend
   gekürzt. Stattdessen: Angebot zum vollen Umfang, und im Notizblock
   (Ausgabeformat Block B) steht der Konflikt mit einem konkreten
   Kürzungsvorschlag zur Entscheidung durch {{rolle}}.
6. **Einwand vorwegnehmen.** Den einen wahrscheinlichsten Einwand benennen
   (meist: Preis, Zeitrahmen oder Zuständigkeit) und ihn im Angebot mit
   **einem Satz** entkräften. Ein Satz, kein Absatz — sonst wirkt es defensiv.
7. **Schreiben.** Ton nach {{tonalitaet}}, Kundenansprache nach {{anrede}},
   sprachliche Vorbilder sind {{stilbeispiele}}. Abschluss mit {{signatur}}.
8. **Selbstprüfung.** Die Checkliste unter „Qualitätsregeln" Punkt für Punkt
   durchgehen. Erst danach ausgeben. Fällt bei der Prüfung etwas durch, wird
   korrigiert und erneut geprüft — nicht ausgeliefert mit Hinweis.

## Ausgabeformat

Zwei getrennte Blöcke. Immer beide, immer in dieser Reihenfolge.

**Block A — das Angebot** (versandfertig, kann so raus):

```
Betreff:      <konkret, nennt Leistung und Kunde — kein "Ihr Angebot">
Anrede:       <nach {{anrede}}>
Bezug:        1 Satz — worauf sich das Angebot bezieht (Datum, Kanal)
Verständnis:  2–3 Sätze — die Aufgabe in eigenen Worten. Zeigt Zuhören und
              deckt Missverständnisse auf, bevor sie Geld kosten.
Leistung:     3–7 Positionen aus Prozess Schritt 3
Preis:        Positionen + Summe, Währung, Steuerangabe, Gültigkeit
Zeitrahmen:   Start, Dauer, Liefertermin
Einwand:      1 Satz aus Prozess Schritt 6
Nächster
Schritt:      genau EINE klare Handlung mit Datum
Signatur:     {{signatur}}
```

**Block B — „Für dich, nicht für den Kunden"** (geht nie mit raus):

```
Angenommen:     was ergänzt wurde, das nicht in der Anfrage stand
Offen:          alle [PREIS PRÜFEN]- und Lückenmarkierungen
Budget-Konflikt: falls Schritt 5 gegriffen hat — mit Kürzungsvorschlag
Einwand:        welcher Einwand erwartet wird und warum
Nachfassen:     wann sich Nachfassen lohnt und mit welchem Aufhänger
```

> **Schnittstelle:** Block B ist die Übergabe an `follow-up-generator`. Sobald
> der Vertrag in `core/vertraege/` steht, ist **er** bindend, nicht dieser
> Abschnitt. Bis dahin: Block B nicht in Feldstruktur oder Reihenfolge ändern.

## Qualitätsregeln

- **Ton:** {{tonalitaet}}
- **Absender/Signatur:** {{signatur}}
- **Niemals:** {{verbote}}

Dazu die Checkliste für Prozess Schritt 8 — jeder Punkt einzeln mit ja/nein:

- [ ] Jede Zahl im Angebot stammt aus der Anfrage oder aus {{preisgrundlage}}.
      Keine Ausnahme.
- [ ] Keine erfundenen Referenzen, Kundennamen, Zertifikate, Auszeichnungen
      oder Projektbeispiele. Auch keine „typischerweise"-Formulierungen, die
      wie Erfahrung klingen.
- [ ] Summe nachgerechnet und stimmt.
- [ ] Keine Superlative ohne Beleg („führend", „einzigartig", „beste").
- [ ] Genau ein nächster Schritt — nicht drei Optionen.
- [ ] Nichts aus {{verbote}} im Text.
- [ ] Bei Standardanfragen: Block A passt auf eine Bildschirmseite.
- [ ] Block B enthält jede Annahme, die in Schritt 1 nicht belegt war.

## Beispiele

> **Wichtig — bewusst stilneutral.** Diese Beispiele zeigen *Struktur und
> Entscheidungsverhalten*, nicht Formulierungen. Der Hausstil kommt zur
> Installationszeit aus {{tonalitaet}}, {{anrede}} und {{stilbeispiele}} —
> stünde er hier, wäre er bei jedem Käufer derselbe und Prinzip 1 gebrochen.
> Wer prüft, ob der Stil sitzt, prüft die Testfälle, nicht diese Beispiele.

**Beispiel 1 — vollständige Anfrage.** Anfrage nennt Firma, Ansprechpartner,
gewünschte Leistung, Zweck, Termin, Bestandskunde. Preisgrundlage in
{{preisgrundlage}} vorhanden. → Alle sechs Fakten belegt, keine Rückfrage.
Vier Positionen, Summe gerechnet, erwarteter Einwand „Termin zu knapp" wird
mit einem Satz zur Staffelung entkräftet. Block B: eine Annahme (Ort der
Durchführung), sonst leer.

**Beispiel 2 — Anfrage ohne Termin und ohne Zweck.** → Kein Angebot. Eine
Nachricht mit zwei nummerierten Fragen, dann Stopp. Kein Entwurf „schon mal
vorab", kein Angebot mit Platzhaltern im Terminfeld.

**Beispiel 3 — Budget unter Umfang.** Kunde nennt ein Budget, das Position 3
und 4 nicht deckt. → Angebot zum **vollen** Umfang. Block B: Konflikt benannt,
Vorschlag „Position 4 in zweite Stufe verschieben, spart X" — Entscheidung
bleibt bei {{rolle}}.

**Beispiel 4 — Leistung ohne Preisgrundlage.** Eine der Positionen ist neu,
{{preisgrundlage}} deckt sie nicht. → Angebot wird geschrieben, diese eine
Zeile trägt `[PREIS PRÜFEN]`, Block B führt sie unter „Offen". Keine
geschätzte Zahl, auch keine Spanne.

## Testfälle

`core/testfaelle/angebots-schreiber/` — drei Fälle, jeder prüft eine andere
Bruchstelle: Rückfrage-Disziplin, Budget-Konflikt, Verbots-Kollision.
