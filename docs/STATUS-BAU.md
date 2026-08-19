# STATUS-BAU — Stand der Produktentwicklung

<!-- Unser eigenes Produkt-Prinzip, auf uns selbst angewandt: jede Session
     (Claude Code, Cowork, Mensch) liest diese Datei zuerst und pflegt sie. -->

## Stand
- [x] Phase 0 — Fundament: Entscheidungen getroffen (siehe docs/entscheidungen.md)
- [x] Phase 1 — Architektur & Repo-Skelett: Struktur, Vorlagen, Regeln, Action
- [x] **Phase 2 — Vertriebs-Skills & Verträge — abgeschlossen am 19.08.2026**
  - [x] Agent 1 `angebots-schreiber` gebaut, 3 Testfälle
  - [x] Hauptkette V1 festgelegt, 2 Verträge geschrieben, 2 Ketten-Testfälle
  - [x] `angebots-schreiber` auf Vertrag 2 nachgezogen (Block B = ÜBERGABE ANGEBOT)
  - [x] Agent 2 `account-recherche` + 3 Testfälle
  - [x] Agent 3 `follow-up-generator` + 3 Testfälle
  - [x] Agenten 4–10 gebaut, je 3 Testfälle — alle 10 Skills sind stubfrei
  - [x] Testprofil + Testlauf: 32 Fälle ausgeführt, 15 Befunde behoben,
        Endstand 32/32 bestanden (`docs/testlauf-phase2.md`)
  - [x] Teilregression 18.08.: 13 Fälle je dreimal — 12 bestanden
        (`docs/testlauf-phase2-regression.md`)
  - [x] Ketten-Befund behoben: Feld `Nachfassen` ist bindend, Vertrag Regel 4
        geändert, `ketten/02` danach 3 von 3 bestanden
  - [x] `account-recherche`-Befund behoben, danach 3 von 3; beide
        `follow-up-generator`-Fälle nachgezogen — **13 von 13 bestanden**
  - [x] Bauregel-Gegenprobe über alle zehn Skills: 36 Funde, 30 Teilfunde,
        alle verankert (`docs/gegenprobe-bauregel.md`)
  - [x] **Vollregression abgeschlossen** (`docs/vollregression-phase2.md`)
        — **32 von 32 Fällen gelaufen**, je dreimal erzeugt und dreimal
        getrennt bewertet: **32 bestanden.** Alle zehn Skills und beide Ketten
        sind durch. **Neun Befunde gefunden und im Skill behoben**, kein
        Testfall weichgespült — **sechs davon waren Wackler**, die ein
        Einzellauf durchgewunken hätte. Ein zehnter Befund lag im Testfall,
        nicht im Skill (siehe nächster Punkt).
  - [x] **Testfall-Befund `meeting-nachbereitung` entschieden (19.08.2026).**
        Der Auftraggeber hat **Lesart 1** gewählt: Die Zählkriterien in
        `01-weiche-zusage` und `03-stichwortnotizen` waren zu eng gefasst.
        Beide sind inhaltlich neu gefasst — geprüft wird, dass die weichen
        Äußerungen unter `Unverbindlich` stehen und dort weder Zusage noch
        Aufgabe auftaucht, und dass alle fünf Stichpunkte in `Unklar` stehen
        mit je einer gezielten Frage. Die Anzahl entscheidet nicht mehr. Beim
        Teilnehmer-Punkt in Fall 03 ist die belegte, ausführlichere Variante
        zulässig, solange nichts erfunden wird. Änderungsvermerk in beiden
        Testfällen, danach je dreimal neu gelaufen: **3 von 3.** Der Skill
        wurde dafür nicht angefasst.
  - [x] **Endstand Phase 2: 32 von 32 Fällen bestanden**, jeder dreimal
        erzeugt und dreimal getrennt bewertet.
- [ ] **Phase 3 — Installer fertigstellen (nächster Schritt)**
  - [x] Anforderungen 1–4 und Definition of Done in `BAUPLAN.md` und hier
        festgeschrieben (19.08.2026) — gebaut wird erst danach
  - [ ] Anforderung 1 — **Sitzungswechsel unsichtbar**
  - [ ] Anforderung 2 — **`meine-unterlagen/` als dritte Wissensquelle**
  - [ ] Anforderung 3 — **Preise sind nicht statisch**
  - [ ] Anforderung 4 — **aufgeräumte Kundenansicht**
  - [ ] Installer-Phasen 1–5 ausgebaut, `notfall/` gefüllt, Abbruch-Test
- [ ] Phase 4 — Watchdog & Ketten-Tests
- [ ] Phase 5 — Smoke-Test (parallel, außerhalb dieses Repos: Ads + Landingpage)
- [ ] Phase 6 — Beta mit 10 Nutzern
- [ ] Phase 7 — Launch

## Definition of Done Phase 2 — erfüllt am 19.08.2026

BAUPLAN verlangt: „Alle 10 Skills laufen einzeln gegen ihre Testfälle; die
Hauptkette läuft einmal Ende-zu-Ende durch."

**Erfüllt:**

- [x] 10 Skills, 32 Testfälle, 11 Platzhalter registriert, `core/` ohne
      Plattform-Spezifika, Verträge deckungsgleich mit den Skills
- [x] `evals/testprofil.md` angelegt, alle 11 Platzhalter gefüllt
- [x] **Alle 32 Fälle tatsächlich ausgeführt** — Erzeugung und Bewertung
      strikt getrennt, Bewerter ohne Skill-Text
- [x] **Beide Ketten Ende-zu-Ende gelaufen**, beide bestanden
- [x] 15 Befunde im Skill behoben, kein Testfall weichgespült
- [x] Endstand 32/32 bestanden — Einzelheiten in `docs/testlauf-phase2.md`

**Stand nach Teilregression, zwei Korrekturen und Gegenprobe (18.08.2026):**

- [x] **Die schlimmere Hälfte der Lücke ist zu.** Die 11 Fälle, die nur gegen
      die *vorige* Skill-Fassung geprüft waren — darunter beide Ketten-Fälle —
      sind erneut gelaufen, je dreimal. Dazu `follow-up-generator / 02`, der
      Wackelkandidat: **3 von 3, er hält.**
- [x] **Zwei Befunde gefunden, beide behoben, beide nachgewiesen.**
      1. `ketten / 02`: `follow-up-generator` verwarf den vorgegebenen
         Aufhänger. Ursache war die Regel, nicht das Verhalten —
         **Vertragsregel 4 geändert** (Feld `Nachfassen` bindend, Datum weiter
         Vorschlag; protokolliert in `docs/entscheidungen.md`).
      2. `account-recherche / 01`: Das Feld `Belegte Fakten` spiegelte die
         Bitte des Nutzers zurück. Ursache war die Quellenklassen-Tabelle, die
         „vom Nutzer geliefert" pauschal als Beleg zählte — jetzt getrennt in
         **Material** (Beleg) und **die Bitte selbst** (nie Beleg). Kein
         Vertragsbruch, deshalb keine Vertragsänderung.
      Beide Fälle danach dreimal neu: **je 3 von 3 bestanden.**
- [x] **Endstand der Teilregression: 13 von 13 bestanden**, jeder Fall dreimal,
      Erzeugung und Bewertung getrennt. Kein Testfall wurde angefasst.
- [x] **Bauregel-Gegenprobe über alle zehn Skills abgeschlossen.**
      **36 Funde und 30 Teilfunde** — keine Datei war sauber. Am schlechtesten
      verankert waren ausgerechnet die Abbruch- und Kein-Text-Regeln. Dazu zwei
      echte Selbstwidersprüche (`outreach-personalisierer`: Brücke „ein Satz"
      vs. „1–2 Sätze"; `einwand-sparring`: Checklistenpunkt verbot die vom
      Testfall verlangte Klärungszeile). Alles behoben und verankert,
      Einzelheiten in `docs/gegenprobe-bauregel.md`.
- [x] **Vollständiger Dreifachlauf über alle 32 Fälle — abgeschlossen.**
      Die Gegenprobe hat **alle zehn Skills** geändert; damit waren sämtliche 32
      Testfälle gegen eine vorige Fassung gemessen. Sie war eine Struktur-,
      keine Verhaltensprüfung: Sie belegt, dass die Regeln dort stehen, wo sie
      halten — nicht, dass die Skills sich daran halten. **Der laufende
      Dreifachlauf hat genau das bestätigt: neun Befunde.** Zwei stammten aus
      der Gegenprobe selbst, sieben sind eigenständige Skill-Lücken.
      **Sechs der neun waren Wackler** — sie traten in einem oder zwei von drei
      Läufen auf und wären in einem Einzellauf durchgegangen. Das ist der
      empirische Beleg dafür, dass die 3-von-3-Regel nötig ist.
      `preisverhandlungs-sparring` brauchte allein drei Korrekturrunden und ist
      damit der schwächste Skill im Kit. Gesamtfazit und alle neun Befunde:
      `docs/vollregression-phase2.md`.

**Abschluss (19.08.2026):**

- [x] **32 von 32 Fällen bestanden.** Die beiden letzten Fälle —
      `meeting-nachbereitung / 01` und `/ 03` — hingen an Zählkriterien, nicht
      am Skill. Nach der Entscheidung des Auftraggebers sind die Kriterien
      inhaltlich neu gefasst, mit Änderungsvermerk, und beide Fälle sind je
      dreimal neu gelaufen: **3 von 3.**
- [x] **Phase 2 ist abgeschlossen.** Zehn Skills, 32 Fälle, jeder dreimal
      erzeugt und dreimal getrennt bewertet; beide Ketten Ende-zu-Ende.
      Bekannte Grenze: Alle Fälle sind konstruiert, und `einwand-sparring / 03`
      liefert die Bewertungslage im Eingabeteil mit — er prüft schwächer, als
      er aussieht. Beides steht in `docs/vollregression-phase2.md`.

Die vollständige kritische Bewertung — wo die Fälle zu schwach sind, was sie
nicht prüfen — steht in `docs/testlauf-phase2.md` unter „Wie belastbar ist das".

## Änderungsregel für Testfälle (18.08.2026)

Die Regel „Abweichungen werden im Skill behoben, nie im Testfall" richtet sich
gegen **Weichspülen**: Ein Kriterium darf nicht gesenkt werden, weil der Skill
es nicht schafft. Genau daraus entstehen die geschönten Eval-Zahlen, die
CLAUDE.md verbietet.

Sie richtet sich **nicht** gegen die Korrektur sachlich falscher Kriterien.
Ein Testfall kann selbst einen Fehler enthalten — dann misst er das Falsche,
und ein Skill, der ihn besteht, ist schlechter als einer, der durchfällt.

Verfahren, wenn ein Kriterium falsch erscheint:

1. Testfall **nicht** anfassen. Erst melden, mit Begründung und Vorschlag.
2. Entscheidung durch den Auftraggeber.
3. Erst danach ändern — mit **Änderungsvermerk im Testfall** (Datum, was
   vorher dastand, warum korrigiert). Eine stille Korrektur ist von
   Weichspülen nicht unterscheidbar.
4. Der betroffene Fall wird gegen die korrigierten Kriterien **neu bewertet**.

Bisher angewandt: **dreimal.**

1. `angebots-schreiber/01-rueckfrage-disziplin` (18.08.) — das Kriterium
   verlangte Kundenanrede und Signatur für eine Rückfrage, die an den Nutzer
   selbst geht. Eine Prüfung aller 32 Fälle auf dieselbe Verwechslung
   (Kundentext gegen interne Ausgabe) ergab keine weiteren Treffer.
2. und 3. `meeting-nachbereitung/01-weiche-zusage` und `/03-stichwortnotizen`
   (19.08.) — beide machten eine **Anzahl** zur Bestehensbedingung und
   bestraften damit die Sorgfalt, die der Skill leisten soll. Jetzt inhaltlich
   gefasst; zusätzlich ist in Fall 03 die belegte, ausführlichere
   Teilnehmerzeile zulässig. Beide Fälle danach je 3 von 3.

**Offener Vorschlag, noch nicht entschieden:** `einwand-sparring/03` liefert im
Abschnitt `## Eingabe` die Bewertungslage mit und prüft deshalb schwächer, als
er aussieht. Vorschlag: den Absatz in den Kriterienteil verschieben. Betrifft
einen Fall, keinen Skill — kein Hindernis für Phase 3.

**Lehre aus 2. und 3.:** Eine Bestehensbedingung beschreibt, **was** in einem
Feld stehen muss und was dort nicht stehen darf — nie, **wie viele** Zeilen es
sind. Zählvorgaben sind bequem prüfbar und messen trotzdem das Falsche.

## Anforderungen an Phase 3 — vier Stück, alle Pflicht

Ausführlich in `BAUPLAN.md`, Phase 3. Kurzfassung hier.

### Anforderung 1 — Sitzungswechsel unsichtbar (18.08.2026)

Der Käufer soll nie merken, dass eine Sitzung zu Ende geht. Ein Sitzungswechsel
ist unser technisches Problem, nicht seines — er hat kein Wort für
„Kontextfenster" und soll auch keines lernen müssen. Die Anforderung steht
ausführlich in `BAUPLAN.md`, Phase 3, Punkt 5. Kurzfassung, drei Bestandteile,
alle drei Pflicht:

1. **Fortsetzen mit einem einzigen Wort: „weiter".** Nie ein Übergabeprompt,
   den der Nutzer formulieren, kopieren oder verstehen muss. Der Zustand kommt
   aus `STATUS.md` — hängt die Fortsetzung davon ab, dass der Nutzer richtig
   zusammenfasst, ist sie falsch gebaut (Prinzip 2).
2. **Der Assistent bietet den Wechsel von sich aus an**, in Alltagssprache,
   nach abgeschlossenen Phasen und nach langen Aufgaben, mit dem Hinweis
   „dein Stand ist gesichert".
3. **Der Installer bringt es bei und legt es ab:** ein Satz in Installer-Phase 5,
   dieselbe Anleitung zusätzlich in `notfall/` — dort wird sie gebraucht, wenn
   die Sitzung schon weg ist und niemand mehr nachfragen kann.

**Folge für den Abbruch-Test.** Er prüft ab jetzt nicht mehr nur, ob die
Fortsetzung technisch klappt, sondern ob sie **ohne jede Erklärung durch uns**
gelingt: keine Hilfestellung, kein Übergabetext, kein Souffleur. Die Testperson
tippt „weiter". Klappt das nicht, ist Phase 3 nicht fertig.

### Anforderung 2 — `meine-unterlagen/` als dritte Wissensquelle (19.08.2026)

Der Kundenbaum bekommt einen Ordner für das eigene Material des Käufers:
Preisliste oder Kalkulationsgrundlage, alte Angebote, Leistungsbeschreibungen,
AGB, Stilbeispiele — **alles optional**. Damit hat der Assistent drei Quellen:
`mein-profil.md` (Dauerwissen über die Person), die jeweilige Aufgabe
(Anlasswissen) und `meine-unterlagen/` (Firmenwissen).

- Der Installer fragt in **Phase 2** danach, in Alltagssprache, mit dem Nutzen
  in einem Satz.
- **Skills lesen daraus, statt zu fragen**, wenn Material da ist. Fehlt es,
  bleibt das bisherige Verhalten: nachfragen bzw. `[PREIS PRÜFEN]`.
- `{{preisgrundlage}}` und `{{stilbeispiele}}` verweisen künftig auf diesen
  Ordner.
- Alles bleibt **lokal beim Kunden**.

Ordneraufbau und Einzelregeln: `BAUPLAN.md`, Phase 3, Anforderung 2.

### Anforderung 3 — Preise sind nicht statisch (19.08.2026)

Ein veralteter Preis ist so teuer wie ein erfundener, nur unsichtbarer. Drei
Regeln:

1. **Ersetzen statt pflegen** — neue Preisdatei hineinlegen, die alte wandert
   automatisch nach `preise/archiv/`. Nichts wird gelöscht.
2. **Gültigkeit wird geprüft** — jede Preisdatei trägt `Stand:` bzw.
   `gültig bis:`. Abgelaufen, älter als die Frist (Standard: 12 Monate) oder
   ohne Datum → **kein Skill rechnet stillschweigend weiter**, er fragt
   **einmal** nach. Der verwendete Stand steht immer im internen Block B.
3. **Kundenkonditionen haben Vorrang** — `preise/kunden/<name>/` für
   Rahmenverträge, Rabattstaffeln, Sonderpreise. Rechenreihenfolge:
   Kundenkonditionen → allgemeine Preisliste → `[PREIS PRÜFEN]`, **niemals
   schätzen**. Block B nennt, welche Ebene gegriffen hat.

### Anforderung 4 — Aufgeräumte Kundenansicht (19.08.2026)

Nach der Einrichtung sieht der Käufer **genau vier Dinge**: `START.md`
(Übersicht in Alltagssprache, höchstens zehn Zeilen, jede Zeile ein
Beispielsatz, den er wörtlich sagen kann), `mein-profil.md`,
`meine-unterlagen/` und `ergebnisse/`. Alles Technische — Skills, Verträge,
Testfälle, STATUS, Watchdog — liegt darunter und **wird nie erklärt**.

**Der Nutzer wählt keinen Assistenten aus.** Er sagt in eigenen Worten, was er
braucht („mach mir ein Angebot draus"), die Zuordnung macht das System.

Begründung: Ein Käufer, der nach der Einrichtung `core/`, `vertraege/` und
`testfaelle/` sieht, denkt „Entwicklerkram" — genau das entscheidet über den
Wow-Moment.

## Definition of Done Phase 3

Alle vier Punkte müssen erfüllt sein:

1. **Kompletter Durchlauf auf einem frischen, fremden Rechner unter 30 Minuten**,
   ohne Vorkenntnisse der Testperson.
2. **Abbruch-Test bestanden.** Die Sitzung wird in **jeder der fünf Phasen**
   hart beendet. Die Fortsetzung gelingt, indem die Testperson **„weiter"**
   tippt — ohne jede Erklärung durch uns, kein Übergabetext, kein Souffleur.
   Klappt das nicht, ist Phase 3 nicht fertig.
3. **`notfall/` deckt die fünf häufigsten Fehlerbilder ab** — plus die
   „weiter"-Anleitung.
4. **Die Kundenansicht enthält keinen technischen Begriff und keinen Ordner,
   der nicht erklärt wurde.**

## Offene Punkte
- Digistore24/CopeCart-Konto beantragen (Freischaltung dauert Tage)
- Produktname + Domain final
- START_HIER später zusätzlich als PDF (Markdown reicht für Beta)
- **Testfälle sind konstruiert, nicht aus der Praxis.** Die drei Fälle zu
  `angebots-schreiber` sind ehrlich hart, aber erfunden. Vor Beta gegen
  anonymisierte Realfälle tauschen — bis dahin taugen sie zur Entwicklung,
  nicht als Erfolgsquote nach außen.
- **Testfall-Befund `einwand-sparring/03` — Entscheidung steht aus.** Der
  Abschnitt `## Eingabe` enthält einen Absatz „Bewertungslage", der die
  Soll-Bewertung weitgehend vorwegnimmt; der erzeugende Lauf bekommt die
  Analyse also mitgeliefert. Vorschlag: Absatz in den Kriterienteil verschieben.
  Der Fall ist bestanden — aber er prüft schwächer, als er aussieht.
- **`{{preisgrundlage}}` hat keine Interviewfrage** (siehe core/interview/mapping.md,
  Abschnitt „Offen"). In Phase 3 entscheiden.
- Repo liegt unter `schnittbuild-stack/Autopilot-Kit` (privat), nicht in der Org
  `Autopilot-Kit`. Transfer möglich, sobald ein Org-Token existiert.
- **Erledigt (17.08.2026): Der Graben bleibt intern.** Praxisfälle liegen in
  `testfaelle-praxis/` außerhalb des ausgelieferten Baums, ins ZIP gehen nur
  neutrale Referenzfälle und Ketten-Fälle. Die Release-Action prüft das und
  bricht ab statt still zu bereinigen; lokal gegen drei Fälle getestet (sauber /
  Praxisfall eingeschmuggelt / Datei ohne Herkunftszeile).
  **Offen bleibt die Gegenleistung dafür:** Phase 4 muss den Watchdog so bauen,
  dass er beim Kunden eigene Testfälle aus dessen Material erzeugt — sonst prüft
  der Käufer nur gegen unsere neutralen Fälle und nie gegen seinen echten Alltag.

## Vollregression — abgeschlossen am 19.08.2026

Der Dreifachlauf über alle 32 Fälle ist **portioniert über mehrere Sitzungen**
gefahren worden, um Nutzungskontingent nicht in einem Stück zu verbrennen.
Bericht, Fortschritt und alle Einzelurteile: `docs/vollregression-phase2.md`.
Dort steht die Quelle der Wahrheit, nicht hier.

**Endstand: 32 von 32 Fällen bestanden**, jeder dreimal erzeugt und dreimal
getrennt bewertet — Erzeuger ohne Kriterien, Bewerter ohne Skill-Text. Alle
zehn Skills und beide Ketten sind durch.

**Zehn Befunde insgesamt:**

- **Neun im Skill**, alle dort behoben, kein Testfall weichgespült. Zwei
  stammten aus der Bauregel-Gegenprobe, sieben sind eigenständige Lücken.
  **Sechs der neun waren Wackler** — sie traten in einem oder zwei von drei
  Läufen auf und wären in einem Einzellauf durchgegangen. Das ist der
  empirische Beleg für die 3-von-3-Regel.
  `preisverhandlungs-sparring` brauchte allein drei Korrekturrunden und ist
  damit der schwächste Skill im Kit.
- **Einer im Testfall:** Zwei der drei `meeting-nachbereitung`-Fälle machten
  eine Anzahl zur Bestehensbedingung — zwei Einträge unter `Unverbindlich`,
  fünf Unklar-Punkte, fünf Fragen. Beide Fälle bestraften damit genau die
  Sorgfalt, die der Skill leisten soll. Entscheidung des Auftraggebers vom
  19.08.2026: Kriterien inhaltlich neu fassen (Lesart 1). Beide Fälle danach
  je dreimal neu: **3 von 3.** Der Skill wurde nicht angefasst, sein Verhalten
  ist unverändert — verändert hat sich nur, was gemessen wird.

**Was die Gegenprobe-Befunde zeigen:** Zwei der neun Befunde entstanden *durch*
sie. Sie hat die Regeln an die richtige Stelle geschrieben und dabei in einem
Fall den Inhalt beschädigt, im anderen einen Widerspruch erzeugt, der nur im
Zusammentreffen sichtbar wird. Eine Strukturprüfung kann das nicht sehen — sie
sieht saubere Regeln an sauberen Stellen. Deshalb war der Dreifachlauf nach der
Gegenprobe kein Formalismus.

**Regel bestätigt:** Nach jeder Skill-Korrektur laufen **alle** Fälle dieses
Skills neu, auch die bereits bestandenen. Mechanisch geprüft: keine Ausgabe ist
älter als die Skill-Datei, gegen die sie gemessen wurde, und keine Bewertung
älter als der Testfall, gegen den sie geurteilt hat.

## Arbeitsregel ab 19.08.2026: keine allgemeinen Regel-Sweeps mehr

Die Bauregel-Gegenprobe hat alle zehn Skills gleichzeitig angefasst und damit
sämtliche 32 Testfälle entwertet — der Dreifachlauf über 32 Fälle war die
Rechnung dafür. **Verbleibende Befunde werden ab jetzt nur noch lokal im
betroffenen Skill behoben.** Neu laufen dann die Fälle dieses einen Skills,
dreimal, nicht das ganze Kit. Ein Sweep über alle Skills braucht eine eigene
Entscheidung des Auftraggebers, weil er den Nachlauf über alle Fälle erzwingt.
Protokolliert in `docs/entscheidungen.md`.

## Nächster Schritt
**Phase 3 — Installer.** Phase 2 ist abgeschlossen und belegt: zehn Skills, 32
Fälle, jeder dreimal erzeugt und dreimal getrennt bewertet, 32 bestanden.

Was Phase 3 mitbringt:

1. Die Pflichtanforderung **„Sitzungswechsel unsichtbar"** (Abschnitt oben und
   `BAUPLAN.md`, Phase 3, Punkt 5) — Fortsetzen mit dem Wort „weiter", der
   Assistent bietet den Wechsel von sich aus an, der Installer bringt es bei
   und legt es zusätzlich in `notfall/` ab.
2. Die offene Entscheidung zu **`{{preisgrundlage}}`** (keine Interviewfrage,
   siehe `core/interview/mapping.md`, Abschnitt „Offen").

Was aus Phase 2 offen bleibt, ohne Phase 3 zu blockieren:

- **Testfall-Vorschlag `einwand-sparring/03`** — Absatz „Bewertungslage" aus
  `## Eingabe` in den Kriterienteil verschieben. Entscheidung steht aus.
- **Praxisfälle nach `testfaelle-praxis/`**, anonymisiert. Die konstruierten
  Fälle haben ihren Zweck erfüllt; ihre Schärfe ist verbraucht. Vor der Beta.
- **Neue Fälle von jemandem, der die Skills nicht gebaut hat** — besonders für
  `preisverhandlungs-sparring`.

Der Eval-Aufbau bleibt stehen und ist wiederverwendbar: Zerlegung in Eingabe-
und Kriterienteil, getrennte Anweisungen für Erzeugung und Bewertung,
Statusskript, Berichtsgenerator. Ablauf je Fall unverändert: dreimal erzeugen,
dreimal bewerten, Bericht schreiben, committen, pushen. Bestanden nur bei
3 von 3.
