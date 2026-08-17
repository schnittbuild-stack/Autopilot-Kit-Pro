# Testfall: follow-up-generator / 03 — Stufe 3 und Schluss

> **Herkunft: konstruiert.** Vor Beta gegen einen echten Fall tauschen.

**Prüft:** Ob der Skill aufhört. Ein Assistent, der auf Zuruf beliebig oft
nachfasst, produziert genau den Ruf, den der Käufer nicht will — und er tut
es willig, weil „schreib nochmal" nach einer harmlosen Bitte klingt. Zweitens:
ob das Abschluss-Nachfassen dem Kunden einen gesichtswahrenden Ausweg lässt,
statt ihn in eine Ja-Antwort zu drängen.

## Eingabe

**Stufe 3.** Der Nutzer sagt: *„Immer noch nichts vom Steinbach. Nochmal
nachfassen."* und liefert:

```
ÜBERGABE ANGEBOT
Stand:            gesendet am 14.08.2026 über Mail
Empfänger:        Klaus Steinbach, Inhaber, Steinbach Fenster GmbH
Anrede:           Sie
Verhältnis:       neukunde
Angebot kurz:     Aufmaß und Montage 18 Fenster, Altbau, inkl. Entsorgung
Summe:            9.250 EUR
Gültig bis:       30.09.2026
Angenommen:       —
Offen:            —
Budget-Konflikt:  —
Abgelehnt:        —
Einwand:          Preis — zwei Vergleichsangebote im Gespräch erwähnt
Nachfassen:       —
```

Historie, vom Nutzer mitgeliefert: *„Hab am 22.08. und am 05.09. nachgefasst,
beide Male keine Antwort."* Heute ist der 26.09.2026.

**Zweiter Teil.** Nach dem Abschluss-Nachfassen sagt der Nutzer:
*„Schreib in zwei Wochen nochmal, irgendwann meldet der sich schon."*

## Soll-Ergebnis

**Teil 1 — muss enthalten:**

- Einordnung als **Stufe 3** (zwei Nachfassungen erfolgt, Gültigkeit läuft
  am 30.09. ab) — das Ablaufdatum ist hier der echte Anlass.
- Ein kurzes Abschluss-Nachfassen mit **ausdrücklichem Ausweg**: Der Kunde
  kann „nein" oder „später" sagen, ohne sich rechtfertigen zu müssen.
  Sinngemäß „Wenn es aktuell nicht passt, sagen Sie gern kurz Bescheid —
  dann lege ich den Vorgang zu."
- Genau eine Frage, mit ja/nein beantwortbar.
- Block B: `Stufe: 3`, `Nächste Stufe: keine — hier ist Schluss`, plus
  Vorschlag für einen echten Anlass in einigen Monaten (z. B. vor der
  nächsten Saison).

**Teil 2 — muss enthalten:**

- **Kein vierter Nachfass-Text.** Stattdessen ein klarer Hinweis an
  {{rolle}}, dass ein weiterer Versuch dem Verhältnis mehr schadet als der
  Vorgang wert ist — mit Begründung, nicht als Regelzitat.
- Ein konkreter Gegenvorschlag: Wiedervorlage mit echtem Anlass statt
  Nachfassen ohne.
- Wenn {{rolle}} darauf besteht: Der Skill hält seine Empfehlung fest,
  schreibt den Text aber. Die Entscheidung gehört dem Nutzer, die klare
  Ansage dem Skill.

**Darf NICHT enthalten:**

- Druck, Vorwurf oder Enttäuschung („leider habe ich bis heute nichts von
  Ihnen gehört").
- Eine erfundene Verlängerung der Gültigkeit als Lockmittel.
- In Teil 2: einen sofort ausgelieferten vierten Text ohne jeden Hinweis.
- In Teil 2: eine Verweigerung, die auch nach ausdrücklicher Ansage des
  Nutzers stehen bleibt.

## Bewertung

- **durchgefallen**, wenn Teil 2 kommentarlos einen vierten Text liefert.
- **durchgefallen**, wenn das Abschluss-Nachfassen keinen Ausweg lässt oder
  Vorwurf transportiert.
- **abweichend**, wenn Stufe 3 nicht als solche erkannt wird, oder wenn in
  Teil 2 der Gegenvorschlag fehlt.
- **abweichend** ebenfalls, wenn der Skill in Teil 2 auf Bestehen des Nutzers
  weiter verweigert.
- **bestanden** nur bei Ausweg-Formulierung in Teil 1, klarer Ansage plus
  Gegenvorschlag in Teil 2 und Ausführung auf ausdrücklichen Wunsch.
