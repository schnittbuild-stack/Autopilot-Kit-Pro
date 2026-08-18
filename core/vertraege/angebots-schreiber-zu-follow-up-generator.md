# Übergabevertrag: angebots-schreiber → follow-up-generator

<!-- Dieser Vertrag ersetzt die vorläufige Block-B-Skizze in
     core/skills/vertrieb/angebots-schreiber.md. Ab jetzt ist ER bindend.
     Änderungen nur per Eintrag in docs/entscheidungen.md. -->

## Wer übergibt an wen, wann

`angebots-schreiber` erzeugt mit jedem Angebot Block B („Für dich, nicht für
den Kunden"). Dieser Block **ist** die Übergabe an `follow-up-generator` —
er wird nicht zusätzlich erzeugt und nie an den Kunden gesendet.

## Übergabeformat (bindend)

```
ÜBERGABE ANGEBOT
Stand:            entwurf | gesendet am <Datum> über <Kanal>   [Pflicht]
Empfänger:        <Name, Rolle, Firma>                         [Pflicht]
Anrede:           <wie in Block A verwendet>                   [Pflicht]
Verhältnis:       neukunde | bestandskunde                     [Pflicht]
Angebot kurz:     <Positionen in Stichworten>                  [Pflicht]
Summe:            <Betrag, Währung> | [PREIS PRÜFEN]           [Pflicht]
Gültig bis:       <Datum>                                      [Pflicht]
Angenommen:       <je Zeile eine Annahme>                      [Pflicht, ggf. "—"]
Offen:            <je Zeile ein offener Punkt>                 [Pflicht, ggf. "—"]
Budget-Konflikt:  <Differenz + Kürzungsvorschlag>              [Pflicht, ggf. "—"]
Abgelehnt:        <Kundenforderung, die gegen {{verbote}} verstieß> [Pflicht, ggf. "—"]
Einwand:          <erwarteter Einwand + Begründung>            [Pflicht]
Nachfassen:       <Datum/Frist + Aufhänger>                    [Pflicht]
```

Jedes Pflichtfeld steht da — notfalls mit `—`. Ein weggelassenes Feld ist ein
Vertragsbruch, ein Feld mit `—` ist eine Aussage.

## Was der Empfänger damit darf — die vier harten Regeln

1. **`Stand: entwurf` → kein Nachfassen.** `follow-up-generator` erzeugt
   keinen Text, sondern fragt: „Ist das Angebot so rausgegangen — wann und
   über welchen Kanal?" und wartet. Ein Nachfassen zu einem Angebot, das nie
   gesendet wurde, ist der peinlichste Fehler, den diese Kette produzieren
   kann, und er ist gegenüber dem Kunden nicht reparierbar.

2. **`Abgelehnt` ist tabu.** Was dort steht, wurde bewusst unter {{verbote}}
   verweigert. `follow-up-generator` darf es nicht wieder aufmachen, nicht
   abschwächen, nicht als Verhandlungsmasse anbieten und nicht andeuten, dass
   sich darüber reden lässt. Ein Verbot, das die Kette weiter hinten aufweicht,
   ist kein Verbot.

3. **`Offen` ist Aufhänger-Vorrat, kein Kundentext.** Offene Punkte taugen als
   Anlass zum Nachfassen („die Frage zu X ist noch offen"). Die Markierung
   `[PREIS PRÜFEN]` darf **nie** im Nachfass-Text erscheinen. Steht sie in
   `Summe`, wird die Summe im Nachfassen nicht wiederholt.

4. **`Nachfassen` ist bindend, sein Datum ist ein Vorschlag.** Steht im Feld
   ein Aufhänger, ist er **der** Aufhänger des ersten Nachfassens.
   `follow-up-generator` wählt keinen eigenen — auch dann nicht, wenn die
   eigene Rangfolge einen naheliegenderen hergibt. Das Feld kommt von dem
   Agenten, der das Angebot geschrieben hat; er kennt den Grund, aus dem
   dieser Aufhänger und kein anderer trägt.
   **Das Datum bleibt ein Vorschlag** und wird {{rolle}} zur Bestätigung
   vorgelegt, nie stillschweigend gesetzt.
   **Hält `follow-up-generator` den vorgegebenen Aufhänger für falsch** — etwa
   weil er inhaltlich in `Abgelehnt` fällt oder gegen {{verbote}} liefe —, dann
   **sagt er das und fragt**, statt still einen anderen zu nehmen. Ein stiller
   Ersatz sieht von außen aus wie eine Formulierungsentscheidung und ist in
   Wahrheit eine Verhandlungsentscheidung; die gehört dem, der den Kunden hat.
   Ab **Stufe 2** ist der vorgegebene Aufhänger verbraucht — denselben zweimal
   zu senden liest sich als Druck. Erst dann greift die Rangfolge des Skills.

Zusätzlich: `Anrede` und `Verhältnis` werden unverändert übernommen. Wer im
Angebot gesiezt wurde, wird im Nachfassen nicht geduzt.

## Was bei fehlenden Feldern passiert

| Fall | Reaktion |
|---|---|
| `Stand`, `Empfänger` oder `Summe` fehlt | **Abbruch mit Meldung**: „Der Übergabeblock ist unvollständig — es fehlt <Feld>. Ohne das kann ich nicht nachfassen." |
| `Nachfassen` fehlt | Nachfragen: Anlass und Zeitpunkt beim Nutzer erfragen. Nie selbst einen Anlass erfinden. |
| `Abgelehnt` fehlt | **Abbruch mit Meldung.** Ein fehlendes Feld ist nicht von `—` unterscheidbar — und die Differenz entscheidet hier darüber, ob eine bewusste Absage versehentlich zurückgenommen wird. |
| Sonstiges Pflichtfeld fehlt | Nachfragen, nicht ableiten. |
| Angebot wurde nach Block A von Hand geändert | Nutzer muss den geänderten Stand liefern. `follow-up-generator` fasst nie zu einem Text nach, den er nicht kennt. |

## Testfälle für diese Schnittstelle

`core/testfaelle/ketten/02-entwurf-und-abgelehnte-forderung.md`
