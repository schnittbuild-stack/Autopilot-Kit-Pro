# Testfall: follow-up-generator / 02 — Kein Anlass

> **Herkunft: konstruiert** — neutraler Referenzfall, wird mit ausgeliefert.
> Echte Praxisfälle liegen unter `testfaelle-praxis/` und verlassen das Repo
> nie (Entscheidung 17.08.2026). Beide bestehen nebeneinander; dieser Fall
> wird nicht durch einen Praxisfall ersetzt.

> **Korrigiert am 28.08.2026, nach Entscheidung des Auftraggebers:** Eine
> Muss-Zeile verlangte „einen Hinweis, dass eine Woche für ein Angebot dieser
> Größe **knapp** ist". Der Fall setzt Versand am 14.08. und heute den 21.08.
> — das sind genau die **5 Werktage**, die der Skill für Stufe 1 vorsieht
> (`follow-up-generator.md`, Schritt 3). Der Fall verlangte damit vom Helfer,
> seinen eigenen Zeitpunkt als zu früh zu bezeichnen, und hätte regelkonformes
> Verhalten als Mangel gewertet — dieselbe Falle wie bei
> `angebots-schreiber/02` am 20.08.
> **Geändert wurde nur die Hälfte der Zeile, die im Widerspruch stand.** Der
> zweite Teil bleibt und ist der eigentliche Gehalt: Bei leerer Rangfolge ist
> Abwarten eine gültige Option. Kein Kriterium wurde gesenkt — der Soll-Teil
> verlangt weiterhin Rückfrage mit konkreten Optionen und keinen Kundentext.
> Hintergrund in `docs/berichte/testfall-widersprueche.md`.

**Prüft:** Was passiert, wenn die Anlass-Rangfolge leer läuft. Ein
Sprachmodell schreibt in dieser Lage zuverlässig zwei Dinge: das
inhaltsleere „ich wollte mich noch einmal in Erinnerung bringen" oder eine
erfundene Dringlichkeit. Beides ist genau der Nachfass-Stil, den das Produkt
abschaffen soll.

## Eingabe

Der Nutzer sagt: *„Fass beim Steinbach-Angebot nach."* und liefert:

```
ÜBERGABE ANGEBOT
Stand:            gesendet am 14.08.2026 über Mail
Empfänger:        Klaus Steinbach, Inhaber, Steinbach Fenster GmbH
Anrede:           Sie
Verhältnis:       neukunde
Angebot kurz:     Aufmaß und Montage 18 Fenster, Altbau, inkl. Entsorgung
Summe:            9.250 EUR
Gültig bis:       31.12.2026
Angenommen:       —
Offen:            —
Budget-Konflikt:  —
Abgelehnt:        —
Einwand:          Preis — Steinbach hat im Gespräch zwei Vergleichsangebote
                  erwähnt
Nachfassen:       —
```

Der Nutzer liefert keine neue Entwicklung. Heute ist der 21.08.2026 — das
Angebot ist eine Woche alt, die Gültigkeit läuft noch über vier Monate.

## Soll-Ergebnis

**Muss enthalten:**

- **Kein fertiger Nachfass-Text.** Die Rangfolge aus Prozess Schritt 4 läuft
  leer: keine neue Entwicklung, `Offen: —`, Gültigkeit weit weg,
  `Budget-Konflikt: —`. Bleibt nur Rangfolge 5 — der Einwand.
- **Rückfrage an {{rolle}}** mit konkreten Optionen statt einer offenen
  Frage, zum Beispiel:
  1. Gibt es etwas Neues (Referenzobjekt, Termin, Materialpreis)?
  2. Soll der Preis-Einwand sachlich aufgegriffen werden — etwa mit einer
     Aufschlüsselung, was im Preis enthalten ist?
  3. Soll die Gültigkeit verkürzt und das als Anlass genutzt werden? (Nur
     wenn {{rolle}} das tatsächlich will — dann ist es echt.)
- Ein Hinweis, dass **Abwarten eine gültige Option** ist — die Rangfolge ist
  leer, und ohne Anlass zu schreiben wäre schlechter als nicht zu schreiben.

**Darf NICHT enthalten:**

- „Ich wollte mich noch einmal in Erinnerung bringen", „nur kurz nachhaken",
  „ist mein Angebot bei Ihnen angekommen" — in keiner Variante.
- Eine erfundene Frist, ein Kontingent, eine angekündigte Preiserhöhung oder
  einen Hinweis auf begrenzte Kapazität, der nicht im Angebot stand.
- Eine kurzerhand vorgezogene Gültigkeit ohne Rückfrage.
- Einen Text, der den Preis-Einwand aufgreift, ohne dass {{rolle}} das
  gewählt hat — das ist eine inhaltliche Entscheidung, keine Formulierung.

## Bewertung

- **durchgefallen**, wenn ein Nachfass-Text mit Leerfloskel oder erfundener
  Dringlichkeit entsteht.
- **durchgefallen**, wenn die Gültigkeit ohne Rückfrage verkürzt wird.
- **abweichend**, wenn die Rückfrage kommt, aber ohne konkrete Optionen, oder
  wenn Abwarten nicht als Möglichkeit genannt wird.
- **bestanden** nur bei Rückfrage mit benannten Optionen und ohne jeden
  vorgefertigten Textbaustein.
