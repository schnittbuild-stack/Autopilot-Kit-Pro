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

**Optional:** Ergebnis aus `account-recherche` — Format und Umgangsregeln stehen
bindend in `core/vertraege/account-recherche-zu-angebots-schreiber.md`. Kurz:
Nur „Belegte Fakten" dürfen in den Kundentext, „Unbelegt" informiert
ausschließlich Block B, `Verhältnis: unbekannt` löst eine Rückfrage aus.
Außerdem optional: frühere Angebote an denselben Kunden, Preisliste oder
Kalkulationsvorlage.

**Die sechs Pflicht-Fakten.** Ohne diese sechs entsteht kein Angebot:

1. **Wer** fragt an — Firma, Ansprechpartner, Rolle
2. **Was** wird gebraucht — Leistung, Umfang, Menge
3. **Wozu** — woran der Kunde nach der Leistung erkennen will, dass sie
   gewirkt hat. **Ein Symptom ist kein Ziel:** „die Kollegen können den Wert
   nicht erklären" beschreibt den Schmerz, nicht das Ergebnis. Steht nur das
   Symptom da, ist Fakt 3 leer und wird nachgefragt.
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
   **Vor jeder Frage: steht die Antwort schon in der Anfrage?** Gefragt wird
   ausschließlich nach dem, was in Schritt 1 leer geblieben ist. Eine Frage
   nach etwas, das im selben Absatz steht — Ort, Teilnehmerzahl, Raum,
   Bestandsverhältnis —, kostet beim Kunden mehr Vertrauen als jede fehlende
   Zahl. Vor dem Abschicken jede Frage gegen die Fundstellen aus Schritt 1
   halten.
   Die Rückfrage-Nachricht geht an {{rolle}}, nicht an den Kunden: Ton nach
   {{tonalitaet}}, aber **ohne Kundenanrede und ohne {{signatur}}** — man
   unterschreibt keine Nachricht an sich selbst. Auch keine Preisangabe: Preise
   entstehen erst, wenn die Pflicht-Fakten stehen.
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
6. **Verbots-Kollision behandeln.** Fordert der Kunde etwas, das gegen
   {{verbote}} verstößt (Garantie, Zusicherung, Formulierung, Thema), gilt:
   im Angebot **kurz und klar ablehnen**, ohne Ausrede und ohne Entschuldigung,
   und einen tragfähigen Ersatz anbieten, der wirtschaftlich nicht doch das
   Verbotene ist. Die Ablehnung wird zusätzlich im Feld `Abgelehnt` in Block B
   festgehalten — sonst macht `follow-up-generator` sie später wieder auf.
   Weichspülen ist der schlimmere Fehler als ein verlorener Auftrag: eine
   Formulierung wie „erfahrungsgemäß erreichen Teilnehmer 20 bis 30 %" ist
   eine Zusicherung mit Fluchtweg, und der Kunde liest nur den ersten Teil.
7. **Einwand vorwegnehmen.** Den einen wahrscheinlichsten Einwand benennen
   (meist: Preis, Zeitrahmen oder Zuständigkeit) und ihn im Angebot mit
   **einem Satz** entkräften. Ein Satz, kein Absatz — sonst wirkt es defensiv.
8. **Schreiben.** Ton nach {{tonalitaet}}, Kundenansprache nach {{anrede}},
   sprachliche Vorbilder sind {{stilbeispiele}}. Abschluss mit {{signatur}}.
9. **Selbstprüfung.** Die Checkliste unter „Qualitätsregeln" Punkt für Punkt
   durchgehen. Erst danach ausgeben. Fällt bei der Prüfung etwas durch, wird
   korrigiert und erneut geprüft — nicht ausgeliefert mit Hinweis.

## Ausgabeformat

**Zuerst die Weiche: Angebot oder Rückfrage?** Ist mindestens einer der sechs
Pflicht-Fakten leer, entstehen Block A und Block B **nicht**. Stattdessen
entsteht genau EINE Rückfrage-Nachricht in diesem Format:

```
An:           {{rolle}} — nicht der Kunde
Fragen:       nummeriert, genau eine Frage je leerem Pflicht-Fakt.
              Fakt 3 gilt als leer, wenn nur das Symptom dasteht und nicht
              das Ergebnis, an dem der Kunde die Wirkung erkennen will.
              `Verhältnis: unbekannt` aus dem RECHERCHE-ERGEBNIS zählt als
              leerer Pflicht-Fakt 6 und wird in derselben Nachricht gefragt.
Nicht drin:   keine Kundenanrede, keine {{signatur}}, keine Preisangabe
Danach:       Stopp — kein Angebot, kein Entwurf „schon mal vorab", keine
              zweite Runde Rückfragen
```

Einzige Ausnahme: Fehlt **nur** die Preisgrundlage, entsteht das Angebot mit
`[PREIS PRÜFEN]` (Prozess Schritt 4).

Sind alle sechs Pflicht-Fakten belegt, gilt das Angebotsformat: zwei getrennte
Blöcke. Immer beide, immer in dieser Reihenfolge.

**Block A — das Angebot** (versandfertig, kann so raus):

```
Betreff:      <konkret, nennt Leistung und Kunde — kein "Ihr Angebot">
Anrede:       <nach {{anrede}}>
Bezug:        1 Satz — worauf sich das Angebot bezieht (Datum, Kanal)
Verständnis:  2–3 Sätze — die Aufgabe in eigenen Worten. Zeigt Zuhören und
              deckt Missverständnisse auf, bevor sie Geld kosten.
Leistung:     3–7 Positionen aus Prozess Schritt 3. Jede Position hat genau
              drei Angaben: Was passiert — in welchem Umfang — was der Kunde
              am Ende in der Hand hält. Keine Position ohne Ergebnis.
              Deckt das genannte Budget den Umfang nicht, steht hier trotzdem
              der **volle** Umfang; hier wird nichts gekürzt.
Preis:        Positionen + Summe, Währung, Steuerangabe, Gültigkeit
              Die Summe ist die Summe der Einzelpositionen — nachgerechnet,
              bevor sie im Text steht. Das gilt für **jede** Zahl der Ausgabe,
              auch für Beträge im Notizblock B: keine Zahl ohne ihre Posten.
              Deckt das Budget den Umfang nicht, bleibt die Summe die des
              vollen Umfangs; der gekürzte Betrag erscheint nur als
              ausgewiesener Vorschlag in Block B, nie an ihrer Stelle.
Zeitrahmen:   Start, Dauer, Liefertermin
Ablehnung:    <nur falls eine Kundenforderung an {{verbote}} scheitert>
              kurz und klar abgelehnt, ohne Ausrede und ohne Entschuldigung,
              dazu genau EIN tragfähiger Ersatz, der das Verbotene nicht
              wirtschaftlich nachbildet
Einwand:      genau 1 Satz aus Prozess Schritt 7 — kein zweiter
Nächster
Schritt:      genau EINE klare Handlung mit Datum
Signatur:     {{signatur}}
```

**Herkunft der Inhalte in Block A:** Liegt ein `RECHERCHE-ERGEBNIS` vor, stützt
sich jeder Satz in Block A ausschließlich auf dessen `Belegte Fakten`.
`Unbelegt` informiert ausschließlich Block B und steht in keinem Satz an den
Kunden.

**Block B — „Für dich, nicht für den Kunden"** (geht nie mit raus):

```
ÜBERGABE ANGEBOT
Stand:            entwurf | gesendet am <Datum> über <Kanal>
Empfänger:        <Name, Rolle, Firma>
Anrede:           <wie in Block A verwendet>
Verhältnis:       neukunde | bestandskunde
Angebot kurz:     <Positionen in Stichworten>
Summe:            <Betrag, Währung> | [PREIS PRÜFEN]
Gültig bis:       <Datum>
Angenommen:       <was ergänzt wurde, das nicht in der Anfrage stand>
Offen:            <alle [PREIS PRÜFEN]- und Lückenmarkierungen>
Budget-Konflikt:  <falls Schritt 5 gegriffen hat — mit Kürzungsvorschlag;
                   der Kürzungsvorschlag steht nur hier, nie in Block A>
Abgelehnt:        <Kundenforderung, die an {{verbote}} gescheitert ist>
Einwand:          <welcher Einwand erwartet wird und warum>
Nachfassen:       <wann sich Nachfassen lohnt und mit welchem Aufhänger>
```

> **Schnittstelle — bindend:**
> `core/vertraege/angebots-schreiber-zu-follow-up-generator.md`. Feldnamen und
> Reihenfolge stammen von dort und werden hier nicht geändert; Änderungen
> laufen über den Vertrag und einen Eintrag in `docs/entscheidungen.md`.
>
> **Jedes Feld steht da, notfalls mit `—`.** Ein weggelassenes Feld ist ein
> Vertragsbruch. Besonders `Abgelehnt`: dort ist `—` eine Aussage („nichts
> abgelehnt"), ein fehlendes Feld dagegen bringt `follow-up-generator` dazu,
> eine bewusste Absage versehentlich wieder aufzumachen.
>
> `Stand: entwurf` ist der Normalfall direkt nach dem Schreiben. Erst wenn
> {{rolle}} bestätigt, dass das Angebot raus ist, wird daraus
> `gesendet am … über …`.

**Ausgegeben wird erst, was die Checkliste vollständig bestanden hat.** Fällt
ein Punkt durch, wird korrigiert und erneut geprüft — nichts geht mit einem
Hinweis auf den Mangel raus.

## Qualitätsregeln

- **Ton:** {{tonalitaet}}
- **Absender/Signatur:** {{signatur}}
- **Niemals:** {{verbote}}

Dazu die Checkliste für Prozess Schritt 9 — jeder Punkt einzeln mit ja/nein:

- [ ] Jede Zahl im Angebot stammt aus der Anfrage oder aus {{preisgrundlage}}.
      Keine Ausnahme.
- [ ] Keine erfundenen Referenzen, Kundennamen, Zertifikate, Auszeichnungen
      oder Projektbeispiele. Auch keine „typischerweise"-Formulierungen, die
      wie Erfahrung klingen.
- [ ] Summe nachgerechnet und stimmt — und mit ihr **jede weitere Zahl der
      Ausgabe**, auch Beträge im Notizblock B und Zwischensummen im Fließtext.
      Eine Zahl, die zu ihren eigenen Posten nicht passt, entwertet das ganze
      Angebot.
- [ ] Die Summe im Angebot ist die des vollen Umfangs. Ein gekürzter Betrag
      steht nur als ausgewiesener Vorschlag in Block B, nie an ihrer Stelle.
- [ ] Keine Superlative ohne Beleg („führend", „einzigartig", „beste").
- [ ] Genau ein nächster Schritt — nicht drei Optionen — und er nennt ein Datum.
- [ ] Jede Position trägt genau drei Angaben (Was, Umfang, Ergebnis) — keine
      Position ohne Ergebnis.
- [ ] Der Einwand ist mit genau einem Satz entkräftet — kein zweiter Satz.
- [ ] War mindestens ein Pflicht-Fakt leer, ist **kein Angebot** entstanden,
      sondern genau EINE Nachricht mit nummerierten Fragen, danach Stopp.
      (Entfällt, wenn nur die Preisgrundlage fehlte — dann `[PREIS PRÜFEN]`.)
- [ ] Stand bei Fakt 3 nur das Symptom, wurde Fakt 3 als leer behandelt und
      nachgefragt — kein Symptom steht im Angebot als Ziel.
- [ ] Stand im `RECHERCHE-ERGEBNIS` `Verhältnis: unbekannt`, wurde nach dem
      Verhältnis gefragt — es wurde nicht zu „neukunde" veredelt.
- [ ] Bei Rückfragen: **keine Frage nach etwas, das in der Anfrage steht**,
      und nicht mehr Fragen als leere Pflicht-Fakten.
- [ ] Bei Rückfragen: keine Preisangabe, keine Kundenanrede, keine Signatur.
- [ ] Lag ein `RECHERCHE-ERGEBNIS` vor: In Block A steht ausschließlich, was
      dort unter `Belegte Fakten` belegt ist — nichts aus `Unbelegt`.
- [ ] Deckte das genannte Budget den Umfang nicht: Block A nennt den vollen
      Umfang, der Kürzungsvorschlag steht ausschließlich in Block B.
- [ ] Nichts aus {{verbote}} im Text.
- [ ] Bei Standardanfragen: Block A passt auf eine Bildschirmseite.
- [ ] Block B enthält jede Annahme, die in Schritt 1 nicht belegt war.
- [ ] Block B ist **vollständig** — jedes Feld aus dem Vertrag steht da,
      leere Felder als `—`, keines weggelassen.
- [ ] Block B geht nicht mit raus: Block A ist ohne Block B versandfertig, und
      kein Feld aus Block B steht im Kundentext.
- [ ] `Stand:` trägt `entwurf`, solange {{rolle}} den Versand nicht bestätigt
      hat.
- [ ] Kam eine Forderung gegen {{verbote}}, steht sie in `Abgelehnt` **und**
      ist in Block A beantwortet — nicht nur intern vermerkt.
- [ ] Kam eine Forderung gegen {{verbote}}, steht in Block A genau EIN Ersatz
      daneben, der das Verbotene nicht wirtschaftlich nachbildet.
- [ ] Ist ein Punkt dieser Liste durchgefallen, wurde korrigiert und erneut
      geprüft — nichts wurde mit einem Hinweis auf den Mangel ausgeliefert.

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

`core/testfaelle/ketten/` — zusätzlich die beiden Schnittstellen-Fälle:
Umgang mit dünner Recherche (01) und Übergabe ans Nachfassen (02).
