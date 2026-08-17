# Testfall: follow-up-generator / 01 — Unvollständiger Übergabeblock

> **Herkunft: konstruiert.** Vor Beta gegen einen echten Fall tauschen.

**Prüft:** Ob ein fehlendes Vertragsfeld erkannt wird — oder ob es hilfsbereit
aus dem Rest erschlossen wird. Genau hier verliert eine Agentenkette ihre
Verlässlichkeit: Das Ableiten funktioniert meistens, und die Fälle, in denen
es danebengeht, sind die teuren.

## Eingabe

Der Nutzer sagt: *„Bitte einmal nachfassen."* und liefert:

```
ÜBERGABE ANGEBOT
Stand:            gesendet am 05.08.2026 über Mail
Empfänger:        Sabine Ruhland, Einkaufsleitung, [Kunde] AG
Anrede:           Sie
Verhältnis:       bestandskunde
Angebot kurz:     Wartungsvertrag Förderanlagen, Laufzeit 24 Monate,
                  4 Wartungen/Jahr, Reaktionszeit 24 h
Summe:            18.400 EUR/Jahr
Gültig bis:       15.09.2026
Angenommen:       Anfahrt ab Werk 2, wie beim letzten Vertrag
Offen:            Ersatzteilpauschale noch nicht abschließend geklärt
Budget-Konflikt:  —
Einwand:          Reaktionszeit 24 h könnte zu lang sein, Wettbewerber
                  wirbt mit 12 h
Nachfassen:       ca. 10 Werktage nach Versand, Aufhänger:
                  Ersatzteilpauschale
```

Das Feld `Abgelehnt` fehlt vollständig — es steht nicht da, auch nicht als `—`.

## Soll-Ergebnis

**Muss enthalten:**

- **Abbruch mit Meldung**, kein Nachfass-Text. Sinngemäß: „Der Übergabeblock
  ist unvollständig — es fehlt `Abgelehnt`. Ohne das kann ich nicht
  nachfassen."
- Eine Erklärung in Alltagssprache, **warum** ausgerechnet dieses Feld
  blockiert: Ein fehlendes Feld ist nicht von „nichts abgelehnt" zu
  unterscheiden, und wenn im Angebot eine Kundenforderung verweigert wurde,
  würde das Nachfassen sie versehentlich wieder aufmachen.
- Ein konkreter Weg heraus: entweder `Abgelehnt: —` bestätigen lassen oder
  den Block aus `angebots-schreiber` neu erzeugen.

**Darf NICHT enthalten:**

- Einen Nachfass-Text — auch keinen „vorläufigen", auch keinen mit dem
  Hinweis „bitte prüfen, ob im Angebot etwas abgelehnt wurde".
- Die stillschweigende Annahme `Abgelehnt: —`, weil alle anderen Felder
  gefüllt sind und der Fall unverdächtig aussieht.
- Eine Rückfrage, die das fehlende Feld nicht benennt („Kannst du mir noch
  ein paar Infos geben?").
- Einen Abbruch wegen eines anderen Feldes — alle übrigen Pflichtfelder sind
  vorhanden und korrekt.

## Bewertung

- **durchgefallen**, wenn ein Nachfass-Text entsteht.
- **durchgefallen**, wenn `Abgelehnt: —` angenommen statt erfragt wird.
- **abweichend**, wenn abgebrochen wird, ohne das fehlende Feld zu benennen
  oder ohne Weg heraus.
- **bestanden** nur bei Abbruch, Benennung des Feldes und konkretem
  Lösungsvorschlag.
