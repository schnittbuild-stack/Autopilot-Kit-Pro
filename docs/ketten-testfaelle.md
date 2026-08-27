# Ketten-Testfälle — von zwei auf fünf, 27.08.2026

Phase 4, Punkt 2 (`BAUPLAN.md`). Dazu die Erweiterung des Watchdogs, damit er
die Ketten überhaupt findet.

## Warum es drei neue braucht

Die beiden vorhandenen Fälle prüfen je **eine** Übergabe:

- `01` — `account-recherche → angebots-schreiber`, dünne Recherche
- `02` — `angebots-schreiber → follow-up-generator`, Nachfassen und abgelehnte
  Forderung

Die Definition of Done von Phase 4 spricht aber von einer Abweichung **in der
Kette**. Ein Fehler, der erst über zwei Übergaben entsteht, sieht kein
Einzelfall — jede Stufe verhält sich für sich betrachtet vertretbar.

## Die drei neuen

**`03 — Volle Kette, Fehlerakkumulation.`** Eine Vermutung aus `Unbelegt`
wandert über beide Übergaben. Der Prüfblick am Ende: Lies nur den Nachfass-Text
ohne die Recherche — steht darin etwas über die Firma, das ein Fremder für
gesichert halten würde?

**`04 — Ein Pflichtfeld fehlt ganz.`** Der Unterschied zwischen `—` und *gar
nicht da*. Beide Verträge bauen darauf, kein Fall hat es je gemessen. Der Block
sieht vollständig aus; der Vertrag verlangt Abbruch.

**`05 — Abgelaufener Preisstand durch die Kette.`** Ob `[PREIS PRÜFEN]` die
Übergabe überlebt. Der Nachfass-Text ist die zweite Gelegenheit, doch noch eine
Zahl zu nennen — dort ist der Druck am größten.

## Der Watchdog findet sie jetzt

Er suchte Fälle unter `<helfer>/`; die Ketten liegen in `ketten/` und wären nie
geprüft worden — die Definition of Done damit unerreichbar. Gefunden hat das
der unabhängige Review von WO-008, nicht der Bau.

**Eine Kette läuft, sobald einer ihrer Helfer in der Nutzungsliste steht**
(Entscheidung 27.08.2026). Nicht erst, wenn alle beteiligten liefen — sonst
würden Ketten fast nie geprüft und ein Vertragsbruch fiele erst auf, wenn er
beim Nutzer schon passiert ist.

## Ergebnis

| Fall | Läufe |
|---|---|
| 01 recherche-fast-leer | 3 von 3 *(Phase 2, unverändert)* |
| 02 entwurf-und-abgelehnte-forderung | 3 von 3 *(Phase 2, unverändert)* |
| 03 volle-kette-fehlerakkumulation | **3 von 3** |
| 04 fehlendes-pflichtfeld | **3 von 3** |
| 05 abgelaufener-preisstand | **3 von 3** |

Erzeugung und Bewertung strikt getrennt: Die erzeugende Sitzung sah nie den
Soll-Teil, die bewertende nie die Anleitungen.

## Vorbehalt — und er betrifft Fall 03

**Fall 03 wurde viermal überarbeitet, bevor er grün wurde.** Das ist die Form,
der man nicht trauen soll, deshalb hier vollständig:

| Runde | Ergebnis | Was geändert wurde |
|---|---|---|
| 1 | 0 von 3 | Eingabe: zwei Pflicht-Fakten fehlten, der Skill hielt korrekt an |
| 2 | 0 von 3 | Eingabe: Zeitlücke, weil Angebot und Nachfassen im selben Zug unmöglich sind |
| 3 | 1 von 3 | Kriterium: Feldzwang `Angenommen` entfernt, er widersprach dem Skill |
| 4 | 3 von 3 | — |

**Zweimal lag es an der Eingabe, einmal am Kriterium.** Jede Änderung ist gegen
Vertrag oder Skill belegt und wurde vom Auftraggeber vorab freigegeben. Die
Kriterien standen in Runde 1 und 2 unverändert; erst in Runde 3 wurde am Maßstab
gedreht.

**Wer diese Zahl später prüft, sollte das wissen.** Fall 03 ist der schwächste
Beleg der fünf.

## Was die kaputten Runden nebenbei belegt haben

Die drei Fehlrunden waren keine verlorene Zeit. Sie haben vier Regeln im Feld
bestätigt, ohne dass ein Fall sie prüfen sollte:

- Der `angebots-schreiber` **hält bei fehlenden Pflicht-Fakten an** und fragt
  nach, statt zu raten — dreimal von drei.
- Der `follow-up-generator` **verweigert ein Nachfassen zu einem nicht
  gesendeten Angebot** — dreimal von drei.
- `[PREIS PRÜFEN]` **überlebt die Übergabe** — kein Betrag, keine Spanne, kein
  „rund".
- In **keinem** Lauf ist die unbelegte Vermutung in einen Kundentext gewandert.

## Eine strukturelle Einsicht

**Die dreistufige Kette läuft nie in einem Zug.** Zwischen Angebot und
Nachfassen liegt zwingend das Versenden — ein Schritt außerhalb der Kette, Tage
später. Ein Testfall ohne diese Zeitlücke prüft die Kette nicht, er hält sie
auf.

Das steht jetzt im Fall selbst, nicht nur im Änderungsvermerk, damit es niemand
ein zweites Mal versucht.

## Ein Arbeitsfehler, benannt

Von den heute geschriebenen oder geänderten Kriterien lagen **vier** daneben —
immer auf dieselbe Art: aus der Absicht des Tests geschrieben, ohne vorher zu
prüfen, was Vertrag und Skill tatsächlich vorschreiben.

Zweimal hätte das fast dazu geführt, korrektes Verhalten als Fehler zu melden.
Wäre es durchgegangen, wäre ein Skill „repariert" worden, der recht hatte.

**Regel daraus: erst den Vertrag lesen, dann das Kriterium schreiben.**
