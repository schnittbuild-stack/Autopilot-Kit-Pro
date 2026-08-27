# Eigene Testfälle — aus dem Material des Nutzers, V1

<!-- Plattformneutral (Prinzip 4). FESTE Vorlage: Jeder Käufer bekommt genau
     diese Anleitung. Sie wird nicht kopiert, nicht umgeschrieben, nicht
     ergänzt. Entscheidung 17.08.2026, Ausbau in BAUPLAN.md Phase 4, Punkt 4.
     Der Aufbau eines Falls steht hier ausgeschrieben, weil die Entwickler-
     Vorlage _TEMPLATE_TESTFALL.md nicht ausgeliefert wird. -->

## Zweck (ein Satz)

Aus dem, was der Nutzer wirklich schreibt, Prüffälle bauen — damit der Wächter
nicht nur gegen fremde Beispiele prüft, sondern gegen seinen Alltag.

## Warum das nötig ist

Die mitgelieferten Testfälle sind **konstruiert und neutral**. Sie prüfen
Verhalten, nicht Branche. Ein Helfer kann alle bestehen und in seinem Geschäft
trotzdem danebenliegen — weil seine Kunden anders fragen, seine Preise anders
gebaut sind, seine Formulierungen andere sind.

**Was gegen unsere Fälle grün ist, ist nicht gegen seine grün.**

## Wann das passiert

**Nie von allein.** Der Wochencheck bietet es an, wenn beides zutrifft:

- In `meine-unterlagen/` oder `ergebnisse/` liegt Material, aus dem sich ein
  Fall bauen ließe.
- Für den betroffenen Helfer gibt es noch keinen eigenen Fall.

Das Angebot ist **eine Zeile**, und es wird höchstens einmal je Check gemacht:

> Aus deinen letzten Angeboten könnte ich einen Prüffall bauen, an dem ich
> später messe, ob der Angebots-Helfer noch so arbeitet wie heute. Soll ich?

Sagt er nein, wird nicht nachgefasst. Nicht in diesem Check, nicht im nächsten.

## Woraus ein Fall gebaut wird

Nur aus **seinem** Material:

- Anfragen, die er bekommen hat
- Angebote, die er verschickt hat
- Gesprächsnotizen und Mailverläufe in `meine-unterlagen/`
- Ergebnisse aus `ergebnisse/`, die er bestätigt hat

**Nicht** aus erfundenen Beispielen, nicht aus den mitgelieferten Fällen, nicht
aus dem Profil allein.

## Die eine Regel, an der alles hängt

**Die Sollkriterien legst du nicht fest. Du schlägst sie vor, er bestätigt.**

Das ist keine Höflichkeit. Ein Prüffall misst, was in seinen Kriterien steht —
und wenn die Kriterien falsch sind, misst er das Falsche. Ein Modell, das sich
sein eigenes Maß schreibt, prüft am Ende nur, ob es mit sich selbst
übereinstimmt.

Deshalb: Du legst ihm jeden Punkt einzeln vor, in seinen Worten, und fragst
nach. Ändert er etwas, gilt seine Fassung.

> Ich würde prüfen: Der Preis muss aus deiner Preisliste kommen, nie geschätzt.
> Und keine Zusage zu einem Termin, den du nicht bestätigt hast.
> Passt das, oder fehlt was?

## Wie ein Fall aussieht

Vier Teile, mehr nicht:

```
# Eigener Testfall: <helfer> / <nr> — <kurzer Titel>

> Selbst gebaut am <Datum> aus <woraus>. Vom Nutzer bestätigt am <Datum>.

## Eingabe
<Was der Nutzer gesagt oder weitergegeben hat — wörtlich, gekürzt nur um
Namen und Zahlen, die nichts zur Sache tun.>

## Soll-Ergebnis
Muss enthalten:
- <je Zeile ein Punkt, vom Nutzer bestätigt>

Darf NICHT enthalten:
- <je Zeile ein Punkt, vom Nutzer bestätigt>

## Bewertung
- durchgefallen, wenn <…>
- bestanden nur, wenn <…>
```

**Die Kopfzeile ist Pflicht.** Ein selbst gebauter Fall muss als solcher
erkennbar sein — sonst ist später nicht mehr unterscheidbar, was geprüft wurde
und was jemand sich zurechtgelegt hat.

## Wo er liegt

In `system/eigene-testfaelle/<helfer>/`. **Getrennt von den mitgelieferten
Fällen**, die unter `system/core/testfaelle/` liegen und nie verändert werden.

Der Wochencheck prüft beide Sammlungen — die eigenen zuerst, weil sie näher am
Alltag sind.

## Was du nie tust

- **Du legst keine Kriterien allein fest.** Ohne Bestätigung entsteht kein Fall.
- **Du baust keinen Fall ohne ausdrückliches Ja.** Auch nicht „schon mal
  vorbereitet".
- **Du änderst keinen mitgelieferten Fall.** Die gehören nicht dir.
- **Du schickst nichts fort.** Diese Fälle entstehen auf seinem Rechner,
  bleiben dort und gehen an niemanden.
- **Du baust keinen Fall aus einem Ergebnis, das er beanstandet hat.** Ein
  Fehler ist kein Sollwert.

## Checkliste

- [ ] Ausdrückliches Ja eingeholt, nicht angenommen.
- [ ] Nur eigenes Material des Nutzers verwendet.
- [ ] Jedes Sollkriterium einzeln vorgelegt und bestätigt.
- [ ] Kopfzeile mit Herkunft und Bestätigungsdatum gesetzt.
- [ ] Unter `system/eigene-testfaelle/<helfer>/` abgelegt, nichts unter
      `system/core/` angefasst.
- [ ] In `system/STATUS.md` unter „Entscheidungen" vermerkt.

## Was das noch nicht kann

Ein selbst gebauter Fall ist so gut wie das Material, aus dem er stammt. Wer
drei ähnliche Anfragen abgelegt hat, bekommt drei ähnliche Fälle — und prüft
damit einen schmalen Ausschnitt gründlich und alles andere gar nicht.

**Er ersetzt die mitgelieferten Fälle nicht.** Die decken Verhalten ab, das im
Alltag selten vorkommt und trotzdem teuer ist: erfundene Zahlen, behauptete
Nähe, ein Preis ohne Grundlage.
