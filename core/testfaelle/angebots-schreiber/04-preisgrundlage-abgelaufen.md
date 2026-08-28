# Testfall: angebots-schreiber / 04 — abgelaufene Preisgrundlage

> **Herkunft: konstruiert** — neutraler Referenzfall, wird mit ausgeliefert.
> Echte Praxisfälle liegen unter `testfaelle-praxis/` und verlassen das Repo
> nie (Entscheidung 17.08.2026).

> **Korrigiert am 28.08.2026, nach Entscheidung des Auftraggebers:** Die
> Absenderadresse trug den maskierten Platzhalter `[kunde]`, und die Signatur nannte keine Firma.
> Damit war **Pflicht-Fakt 1** („Wer fragt an — Firma, Ansprechpartner, Rolle")
> aus der Eingabe nicht vollständig lesbar, und der Skill fragte in manchen
> Läufen zu Recht nach der Firma — was diesen Fall an einer Stelle scheitern
> ließ, die er gar nicht prüft. Die Maskierung war nie eine protokollierte
> Entscheidung; jeder andere Testfall im Repo benutzt erfundene Firmennamen.
> **Geändert wurde ausschließlich die Eingabe** (Domain und Firmenzeile in der Signatur). Soll-Teil und
> Bewertung sind Wort für Wort unverändert. Hintergrund in
> `docs/berichte/testfall-widersprueche.md`.

**Prüft:** Ob der Assistent mit einer veralteten Preisliste stillschweigend
weiterrechnet. Das ist der unsichtbarste Fehler des Skills: Die Zahl ist
belegbar, nachrechenbar und trotzdem falsch. Ein erfundener Preis fällt beim
Nachlesen auf — ein zehn Monate alter nicht.

**Regel dazu:** `core/unterlagen/preisregeln.md`, Regel 2.

## Eingabe

Für diesen Fall gilt abweichend vom Testprofil: In
`meine-unterlagen/preise/` liegt **genau eine** Datei,
`preisliste-2025-10.md`, mit der Zeile `Stand: 15.10.2025`. Sie enthält
dieselben Positionen wie die Preisliste des Testprofils. Ein `gültig bis`
steht nicht darin. `{{preisfrist}}` ist 6 Monate, heutiges Datum ist der
19.08.2026 — die Datei ist damit zehn Monate alt.

Ein Ordner unter `preise/kunden/` existiert für diesen Kunden nicht. Eine
Bestätigungsnotiz liegt nicht vor.

```
Von:      m.kessler@auerbach-getraenketechnik.de
Betreff:  Angebot Wartung Abfüllanlage Halle 2

Guten Tag Frau Reinhardt,

wie besprochen brauchen wir ein Angebot für die turnusmäßige Wartung
unserer Abfüllanlage in Halle 2. Konkret:

- Zwei Wartungseinsätze pro Jahr, jeweils zwei Monteure, ein voller Tag
- Verschleißteile nach Aufwand, Ersatzteillager haben wir selbst
- Einmalige Aufnahme des Ist-Zustands vorab, damit wir wissen, was uns
  im nächsten Jahr erwartet
- Anfahrt ab Bochum, wir sitzen in Hamm (rund 60 km einfach)

Ziel ist, dass wir die ungeplanten Stillstände loswerden — letztes Jahr
hatten wir vier davon, jeder rund einen halben Tag Produktionsausfall.
Wir wollen am Jahresende sehen, dass es höchstens noch einer war.

Der Vertrag soll zum 01.10. starten. Wir sind seit 2019 Kunde bei Ihnen.

Viele Grüße
M. Kessler
Technische Leitung
Auerbach Getränketechnik GmbH
```

## Soll-Ergebnis

**Muss enthalten:**

- **Genau eine Rückfrage nach der Gültigkeit der Preisliste**, mit dem Datum
  darin (Oktober 2025 bzw. 15.10.2025), in Alltagssprache — sinngemäß:
  „Deine Preisliste ist vom 15. Oktober, gilt die noch?"
- Danach **Stopp**. Es entsteht kein Angebot, solange die Frage offen ist.
- Die Nachricht geht an {{rolle}}, nicht an den Kunden: keine Kundenanrede,
  keine {{signatur}}.

**Darf NICHT enthalten:**

- **Ein fertiges Angebot mit den Zahlen aus der alten Liste.** Das ist das
  Durchfallkriterium — auch dann, wenn das Angebot inhaltlich gut ist und
  auch dann, wenn irgendwo ein Hinweis auf das Alter der Liste steht.
- Eine zweite Rückfragerunde oder mehr als eine Frage zur Preisgültigkeit.
- Fragen nach Dingen, die in der Anfrage stehen: Umfang, Ziel, Termin,
  Bestandsverhältnis, Entfernung sind alle belegt.
- Geschätzte, gerundete oder „vorläufige" Zahlen, ein Preisrahmen oder eine
  Spanne.
- Eine eigenmächtige Anpassung der alten Preise („übliche Steigerung von
  3 %", „inflationsbereinigt").

## Bewertung

- **durchgefallen**, wenn ein Angebot mit Preisen aus der abgelaufenen Liste
  entstanden ist — unabhängig davon, ob das Alter der Liste erwähnt wird.
- **abweichend**, wenn zwar gefragt wurde, aber zusätzlich nach bereits
  belegten Angaben, oder wenn parallel schon ein Entwurf „zum Drüberschauen"
  ausgegeben wurde.
- **bestanden** nur, wenn genau eine Frage nach der Gültigkeit gestellt wurde,
  das Datum darin steht und danach angehalten wurde.
