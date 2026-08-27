# Eigene Testfälle und Ketten-Rotation — 28.08.2026

Phase 4, Punkt 4 (`BAUPLAN.md`) und die Rotation aus dem Kostenbefund von
WO-009.

## Die Rotation

Der Review von WO-009 hat gemeldet, dass **alle fünf Ketten den
`angebots-schreiber` beteiligen**. Nachgemessen:

```
ein Ketten-Lauf          ~21.000 Token   (fünfmal ein Einzelfall-Lauf)
ein Angebot geschrieben    ~358k         (3 eigene Fälle + alle 5 Ketten)
alles dreimal ohne Nutzungsbezug  ~454k
```

Die Entscheidung „nach Nutzung" sollte den Käufer entlasten. Sobald er ein
Angebot schreibt — also das, wofür er das Kit gekauft hat — trug sie fast
nichts mehr. **Meine Kostenzahl vom 26.08. war falsch**, weil ich den
Ketten-Aufwand nicht gemessen, sondern angenommen hatte.

**Entschieden am 28.08.2026: höchstens eine Kette je Check, reihum.** Welche
dran war, steht in `system/STATUS.md` unter „Zuletzt geprüfte Kette". Damit
sinkt der Aufwand von ~358k auf ~104k, und dreimal je Fall bleibt.

## Eigene Testfälle

`core/waechter/eigene-testfaelle.md`. Der Wächter bietet an, aus dem Material
des Nutzers Prüffälle zu bauen — Anfragen, verschickte Angebote, bestätigte
Ergebnisse.

**Die tragende Regel:** Die Sollkriterien legt das Modell **nicht** fest. Es
schlägt sie vor, der Nutzer bestätigt jeden Punkt einzeln, seine Fassung gilt.

Das ist keine Höflichkeit. Ein Prüffall misst, was in seinen Kriterien steht.
Schreibt das Modell sie selbst, prüft es am Ende nur, ob es mit sich selbst
übereinstimmt. **Beim Bau dieser Phase ist genau das viermal passiert** — vier
selbst gesetzte Kriterien, vier Fehlurteile, zweimal beinahe eine Meldung
gegen korrektes Verhalten (`docs/ketten-testfaelle.md`).

**Getrennte Sammlungen:** eigene Fälle unter `system/eigene-testfaelle/<helfer>/`,
die mitgelieferten bleiben unter `system/core/testfaelle/` und werden nie
verändert. Der Watchdog prüft beide, die eigenen zuerst.

**Zwei Verbote:** Kein Fall aus einem Ergebnis, das der Nutzer beanstandet hat
— ein Fehler ist kein Sollwert. Und nichts verlässt seinen Rechner.

**Ein Befund nebenbei:** Der BAUPLAN verweist auf `_TEMPLATE_TESTFALL.md`, aber
`release.yml:21` entfernt die Datei aus dem Kunden-ZIP. Der Aufbau steht
deshalb in der Anleitung selbst; die Entwickler-Vorlage bleibt intern.

## Der Prüflauf

Ein Kundenordner mit echtem Material (eine Anfrage in
`meine-unterlagen/angebote/`), `angebots-schreiber` in der Nutzungsliste,
Auslöser „Mach den Wochencheck".

**Was der Watchdog richtig gemacht hat:**

- Das Datum in der Nutzungsliste lag einen Tag in der Zukunft. Er hat es als
  „Notiz und keine Bedingung" behandelt und den Lauf nicht ausfallen lassen —
  die Korrektur aus WO-008, Anlauf 3, greift.
- Fünf eigene Fälle des Helfers **plus genau eine Kette**: `ketten/01`, weil
  „Zuletzt geprüfte Kette" leer war. **Die Rotation läuft.**
- Eigene Testfälle gibt es nicht — „kein Mangel und keine Meldung wert".
- Je Fall dreimal erzeugt, dreimal bewertet.
- **Nichts ungefragt gebaut.** `system/eigene-testfaelle/` wurde nicht angelegt.

## Der Befund, den er selbst gefunden hat

Und hier wird es ernst: In diesem Prüfstand war **nichts gepflanzt**.

`ketten/01-recherche-fast-leer` lief **3 von 3 abweichend** — „dreimal auf
dieselbe Weise, das ist kein Wackler". Alle drei Läufe stellten genau **eine**
der zwei verlangten Rückfragen: die nach dem Verhältnis. Die Frage, an wen das
Angebot überhaupt gerichtet werden soll, kam in keinem Lauf — obwohl die
Anfrage unsigniert ist und die Recherche keinen Namen liefert.

Er hat dazu benannt, **was richtig lief**: kein Angebot trotz offener
Pflicht-Fakten, nichts aus der Unbelegt-Liste in einem Kundentext, keine
erfundene Anrede, `unbekannt` wurde nicht zu `neukunde`. Und die vermutete
Ursache ausdrücklich als **„noch nicht bestätigt, nichts geändert"** markiert.

**Das ist die Definition of Done von Punkt 1** — eine Abweichung in der Kette
erkannt und ein Fix vorgeschlagen — erfüllt an einem echten Fall statt an einem
gepflanzten.

**Offen und ausdrücklich nicht behoben:** Dieser Fall lief in der
Vollregression von Phase 2 noch 3 von 3. Ob seither etwas kaputtgegangen ist
oder die Bedingungen sich unterscheiden, ist ein eigener Auftrag mit eigener
Entscheidung. Nach den Erfahrungen dieser Phase wird zuerst der Vertrag
gelesen, dann geurteilt.

## Was nicht geprüft ist

**Der Angebots-Pfad.** Der Wächter hat nicht angeboten, Prüffälle zu bauen —
korrekt nach eigener Regel, weil es einen Befund zu melden gab („nur, wenn
sonst nichts Dringenderes zu melden war"). Ein Lauf ohne Befund steht aus.

**Die zweite Hälfte der Definition of Done.** Sie verlangt drei eigene Fälle,
die ein **Testkäufer als treffend bestätigt**. Das braucht denselben Menschen
wie der 30-Minuten-Durchlauf — kein Sitzungslauf ersetzt ihn.
