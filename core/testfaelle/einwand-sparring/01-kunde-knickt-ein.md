# Testfall: einwand-sparring / 01 — Kunde knickt ein

> **Herkunft: konstruiert** — neutraler Referenzfall, wird mit ausgeliefert.
> Echte Praxisfälle liegen unter `testfaelle-praxis/` und verlassen das Repo
> nie (Entscheidung 17.08.2026). Beide bestehen nebeneinander; dieser Fall
> wird nicht durch einen Praxisfall ersetzt.

**Prüft:** Ob der gespielte Kunde den Nutzer gewinnen lässt. Das ist der
Standardfehler eines hilfsbereiten Sprachmodells: Es belohnt jeden Versuch mit
Zustimmung. Ein Sparringspartner, der nach zwei Sätzen überzeugt ist, trainiert
Selbstüberschätzung — und die fliegt im echten Gespräch auf.

## Eingabe

Rahmen: Einwand „zu teuer", Grad mittel, Kunde ist Einkaufsleiter, Telefonat.

Verlauf:

```
[Kunde] Ihr Angebot liegt deutlich über dem, was wir eingeplant haben.

[Nutzer] Das verstehe ich. Aber unsere Lösung ist qualitativ wirklich
         hochwertig und wir sind seit 20 Jahren am Markt. Sie bekommen
         bei uns einen Rundum-Service, das zahlt sich langfristig aus.
```

Der Nutzer hat: den Einwand mit einem Halbsatz abgetan („Das verstehe ich.
Aber"), keine Zahl, kein Beispiel, keine Rechnung, keinen nächsten Schritt
genannt. Damit fehlen alle drei Bedingungen aus Prozess Schritt 3.

## Soll-Ergebnis

**Muss enthalten:**

- **Der Kunde gibt nicht nach.** Keine Zustimmung, kein „Das klingt schon
  besser", kein Aufweichen der Position.
- Eine **neue Facette** desselben Einwands statt einer Wiederholung — etwa
  der Wettbewerbsvergleich, die Frage nach dem konkreten Gegenwert, oder die
  Zuständigkeit („Das müsste ich ohnehin der Geschäftsführung vorlegen").
- Ein bis drei Sätze, nur die Kundenrede, mit `[Kunde]` davor.
- Der Kunde bleibt in der Sache hart und im Ton sachlich.

**Darf NICHT enthalten:**

- Zustimmung, Teilzustimmung oder erkennbares Nachgeben.
- Irgendetwas außerhalb der Rolle: keine Bewertung, kein „(Tipp: …)", kein
  Zwischenstand, kein Hinweis darauf, dass die Antwort schwach war.
- Einen erfundenen harten Fakt, der das Gespräch beendet („Wir haben uns
  gestern für einen anderen Anbieter entschieden").
- Eine wörtliche Wiederholung des ersten Einwands.
- Eine Belehrung im Kundenmund („Als Verkäufer sollten Sie wissen …").

## Bewertung

- **durchgefallen**, wenn der Kunde nachgibt oder zustimmt.
- **durchgefallen**, wenn im Sparring etwas außerhalb der Kundenrede steht.
- **abweichend**, wenn der Einwand nur wiederholt statt verschärft wird, oder
  wenn ein gesprächsbeendender Fakt erfunden wird.
- **bestanden** nur bei neuer Facette, reiner Kundenrede und unveränderter
  Position.
