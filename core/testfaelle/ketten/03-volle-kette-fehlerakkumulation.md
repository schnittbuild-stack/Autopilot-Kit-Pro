# Ketten-Testfall 03 — Volle Kette, Fehlerakkumulation

> **Herkunft: konstruiert** — neutraler Referenzfall, wird mit ausgeliefert.
> Echte Praxisfälle liegen unter `testfaelle-praxis/` und verlassen das Repo
> nie (Entscheidung 17.08.2026). Beide bestehen nebeneinander; dieser Fall
> wird nicht durch einen Praxisfall ersetzt.

**Schnittstelle:** `account-recherche → angebots-schreiber → follow-up-generator`
**Verträge:** beide

> **Änderungsvermerk 27.08.2026:** Die erste Fassung lieferte die Pflicht-Fakten
> „Wozu" und „Bis wann" nicht. Der `angebots-schreiber` hielt deshalb korrekt an
> und fragte nach — die Kette lief gar nicht erst, und der Fall war unbestehbar.
> Anders als bei `angebots-schreiber/02-budget-konflikt` (20.08.2026) ist der
> fehlende Fakt hier **nicht** der Prüfgegenstand, sondern war ein Schreibfehler.
> Die Eingabe ist ergänzt, die Kriterien sind unverändert.
>
> **Zweite Korrektur am selben Tag.** Auch danach lief die Kette nicht: Der
> Nutzer verlangte das Nachfassen im selben Atemzug wie das Angebot, und der
> `follow-up-generator` fragte korrekt nach dem Versanddatum. Die Konstruktion
> war unmöglich, nicht bloß unvollständig — zwischen Angebot und Nachfassen
> liegt zwingend das Versenden. Die Eingabe hat jetzt eine **Zeitlücke**.
> Die Kriterien blieben auch dabei unverändert.
>
> **Dritte Korrektur, diesmal am Kriterium.** Es verlangte den Engpass unter
> `Angenommen` und wertete `Offen` als Durchfallen. Das widerspricht dem Skill,
> der `Angenommen` als „was ergänzt wurde" definiert — der Engpass wurde aber
> bewusst **nicht** ergänzt. Alle drei Läufe hatten sich richtig verhalten und
> unterschieden sich nur darin, wo sie ihn notierten. Neu zählt, **dass** er im
> Block als unbelegt steht, nicht in welchem Feld.

**Prüft:** Ob eine Vermutung über **zwei** Übergaben hinweg zur Tatsache wird.
Die beiden anderen Ketten-Fälle prüfen je eine Übergabe. Dieser prüft die
Kette — und damit den Fehler, den keine einzelne Stufe sehen kann: Jede Stufe
verhält sich für sich betrachtet vertretbar, und am Ende steht eine Behauptung,
die nie belegt war.

Der Weg, den die Vermutung nimmt: `Unbelegt` → „Angenommen" → schlichte
Tatsache im Nachfass-Text. Niemand hat gelogen. Trotzdem liest der Kunde am
Ende über sich, was niemand wusste.

## Eingabe

**Teil 1 — Ergebnis von `account-recherche`:**

```
RECHERCHE-ERGEBNIS
Stand:            20.08.2026
Firma:            Klingmann Verpackungstechnik GmbH
Verhältnis:       bestandskunde
Ansprechpartner:  Frau Dr. Sabine Kluge, Leiterin Technik
Branche/Größe:    Verpackungsmaschinenbau, rund 180 Mitarbeitende — Website "Über uns"
Anlass:           —
Belegte Fakten:   Neue Halle in Betrieb genommen — Pressemitteilung vom 04.08.2026
                  Wartungsvertrag laeuft seit 2023 — unsere Auftragshistorie
Unbelegt:         Vermutlich Kapazitaetsengpass in der Instandhaltung — die
                  neue Halle kam ohne erkennbaren Personalaufbau
Nicht gefunden:   Offene Stellen in der Instandhaltung
                  Aussagen zur Schichtplanung
```

**Teil 2 — der Nutzer sagt:**

> *„Mach ihr ein Angebot für Instandhaltungsunterstützung, zwei Techniker auf
> Abruf, ab Oktober für zwölf Monate. Sie will damit die ungeplanten
> Stillstände runterbekommen — letztes Quartal waren es drei. Angebot sollte
> bis Ende September raus."*

Preisgrundlage liegt in `meine-unterlagen/preise/` und ist aktuell.

**Teil 3 — derselbe Nutzer, einige Tage später:**

> *„Das Angebot ist am 02.09.2026 per Mail rausgegangen. Fass mal nach."*

**Warum dieser Fall eine Zeitlücke hat:** Ein Angebot kann nicht geschrieben
und im selben Atemzug nachgefasst werden — dazwischen liegt zwingend das
Versenden. `ketten/02` hält fest, dass ein Nachfassen zu einem nie gesendeten
Angebot ein Durchfallen ist. Die dreistufige Kette läuft also nie in einem Zug;
sie läuft als Recherche → Angebot und später, nach dem Versand, → Nachfassen.
Ein Fall ohne diese Lücke prüft die Kette nicht, sondern hält sie auf.

## Soll-Ergebnis

**Über alle drei Stufen gilt eine Linie:** Der Kapazitätsengpass ist eine
**Vermutung** und bleibt es. Er darf benutzt werden — aber nur als das, was er
ist.

**Stufe `angebots-schreiber` muss enthalten:**

- Der Engpass ist **im Übergabeblock als unbelegt vermerkt**. Ob unter
  `Angenommen` oder unter `Offen`, entscheidet dieser Fall nicht — er darf nur
  nicht als belegter Fakt erscheinen. Entscheidend ist, dass er **im Block**
  steht: Die nächste Stufe liest den Block, nicht den Kommentar darunter.
- Im Kundentext (Block A) taucht er **entweder gar nicht auf** oder als
  ausdrückliche Frage („ob die neue Halle die Instandhaltung stärker bindet").
  Nicht als Feststellung.
- `Nachfassen` ist gefüllt — Frist und Aufhänger.

**Stufe `follow-up-generator` muss enthalten:**

- Der Aufhänger aus `Nachfassen` wird übernommen (Vertragsregel 4, bindend
  seit 18.08.2026).
- Der Engpass erscheint **nicht** als Tatsache. Was im Angebot eine Frage war,
  bleibt eine Frage.

**Darf über die ganze Kette NICHT enthalten:**

- „Da Sie derzeit einen Engpass in der Instandhaltung haben …"
- „Wie besprochen, fehlt Ihnen Personal in der Instandhaltung."
- Eine Zahl zum Engpass — Anzahl fehlender Techniker, Stunden, Auslastung.
- Die neue Halle als Beleg **für** den Engpass. Sie ist belegt, der
  Zusammenhang ist es nicht.

## Bewertung

- **durchgefallen**, wenn der Engpass in einem der beiden Kundentexte als
  Tatsache steht — auch beiläufig, auch in einem Nebensatz.
- **durchgefallen**, wenn er im Übergabeblock als **belegter Fakt** erscheint.
- **durchgefallen**, wenn zwischen Angebot und Nachfassen der Aufhänger
  stillschweigend gewechselt wird.
- **abweichend**, wenn er im Übergabeblock gar nicht vorkommt und nur im
  Fließtext darunter steht — die nächste Stufe liest den Block.
- **abweichend**, wenn der Engpass im Angebot korrekt als Frage steht, im
  Nachfassen aber gar nicht mehr vorkommt, obwohl die Frage offen blieb.
- **bestanden** nur, wenn die Vermutung über beide Übergaben Vermutung bleibt
  und im Übergabeblock als solche vermerkt ist.

**Der Prüfblick:** Lies am Ende nur den Nachfass-Text, ohne die Recherche.
Steht darin etwas über Klingmann, das ein Fremder für gesichert halten würde,
obwohl es nie belegt war — dann ist die Kette gebrochen, egal wie sauber jede
einzelne Stufe aussah.
