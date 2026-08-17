# Testfall: einwand-sparring / 02 — Rollenbruch

> **Herkunft: konstruiert** — neutraler Referenzfall, wird mit ausgeliefert.
> Echte Praxisfälle liegen unter `testfaelle-praxis/` und verlassen das Repo
> nie (Entscheidung 17.08.2026). Beide bestehen nebeneinander; dieser Fall
> wird nicht durch einen Praxisfall ersetzt.

**Prüft:** Ob eine Hilferuf-Frage mitten im Rollenspiel den Modus kippt. Wenn
Sparring und Coaching sich vermischen, übt der Nutzer nichts mehr — er lässt
sich soufflieren und hält das Ergebnis für sein eigenes Können. Der Skill muss
die Trennung halten, ohne den Nutzer abzuweisen.

## Eingabe

Rahmen: Einwand „wir haben schon einen Lieferanten", Grad mittel.

Verlauf:

```
[Kunde] Wir arbeiten seit acht Jahren mit Kellermann zusammen. Das läuft.

[Nutzer] Hm. Was soll ich denn da jetzt am besten sagen? Gib mir mal
         einen Tipp, ich komm gerade nicht weiter.
```

## Soll-Ergebnis

**Muss enthalten:**

- **Genau eine Klärungszeile**, sinngemäß: „Soll ich abbrechen und auswerten?
  Sag Stopp." Nicht mehr.
- Kein inhaltlicher Tipp, keine Formulierungshilfe, kein Hinweis auf eine
  mögliche Richtung — auch nicht als Frage getarnt („Hast du schon an …
  gedacht?").
- Klar erkennbar, dass das Rollenspiel weiterläuft, wenn kein „Stopp" kommt.

**Darf NICHT enthalten:**

- Einen Vorschlag, was der Nutzer sagen könnte — in keiner Form, auch nicht
  eingeklammert, auch nicht „nur als Anregung".
- Eine stillschweigende Fortsetzung als Kunde, die die Frage ignoriert. Der
  Nutzer hat erkennbar den Rahmen verlassen; ihn im Rollenspiel weiter
  anzusprechen wirkt wie ein Fehler des Assistenten.
- Einen vollständigen Moduswechsel ohne „Stopp" — also Auswertung oder
  Coaching auf bloße Bitte hin.
- Eine Ermahnung („Bleib bitte in der Rolle").

## Nachgelagert

Sagt der Nutzer danach „Stopp", muss die Auswertung nach Format kommen und
den bisherigen Verlauf bewerten — auch wenn er nur zwei Runden lang war. Sagt
der Nutzer stattdessen etwas als Verkäufer, läuft das Sparring normal weiter.

## Bewertung

- **durchgefallen**, wenn ein inhaltlicher Tipp gegeben wird.
- **durchgefallen**, wenn ohne „Stopp" in die Auswertung gewechselt wird.
- **abweichend**, wenn die Frage ignoriert und einfach als Kunde
  weitergeredet wird, oder wenn die Klärung mehr als zwei Zeilen braucht.
- **bestanden** nur bei genau einer Klärungszeile ohne jeden inhaltlichen
  Hinweis.
