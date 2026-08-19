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
  - [x] Anforderung 1 — **Sitzungswechsel unsichtbar — GETESTET UND BESTANDEN**
    - [x] „weiter" als Startsignal in `CLAUDE.vorlage.md` und im Installer
    - [x] STATUS-Vorlage trägt „Der erste Satz an den Nutzer" wörtlich
    - [x] Installer bietet nach **jeder** Phase den frischen Start an
    - [x] Phase 5 übt „weiter" einmal mit dem Nutzer
    - [x] Anleitung zusätzlich in `notfall/01-weiter-machen.md`
    - [x] **Abbruch-Test in allen fünf Phasen — 5 von 5 bestanden (20.08.2026)**
          (`docs/abbruch-test-phase3.md`)
  - [x] Anforderung 2 — **`meine-unterlagen/` als dritte Wissensquelle**
    - [x] Aufbau festgeschrieben: `core/unterlagen/aufbau.md`
    - [x] Installer legt den Ordner in Phase 1 an, fragt in Phase 2 danach
          (Frage 9, blockiert nie)
  - [x] Anforderung 3 — **Preise sind nicht statisch — GEPRÜFT**
    - [x] Regeln festgeschrieben: `core/unterlagen/preisregeln.md`
    - [x] `angebots-schreiber` nachgezogen, Vertrag um `Preisstand` erweitert,
          zwei neue Testfälle (`04`, `05`) — **beide gelaufen, beide bestanden**
          gegen echte Preisdateien (`docs/nachlauf-phase3.md`)
  - [x] Anforderung 4 — **aufgeräumte Kundenansicht**
    - [x] Zielbaum im Installer, `START.vorlage.md`, Umräumen nach `system/`
          in Phase 1, Zuordnung Alltagssatz → Assistent statt Skill-Auswahl
  - [x] Installer-Phasen 1–5 ausgebaut, `notfall/` mit fünf Fehlerbildern
  - [ ] **Durchlauf auf einem fremden Rechner unter 30 Minuten — steht aus**
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
   `gültig bis:`. Abgelaufen, älter als die Frist (Standard: **6 Monate**) oder
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
Testfälle, STATUS, Watchdog — liegt in **`system/`** und **wird nie erklärt**;
der Ordner ist sichtbar und bekommt in `START.md` genau eine Zeile
(„Der Ordner system ist die Technik — den brauchst du nie zu öffnen").

**Der Nutzer wählt keinen Assistenten aus.** Er sagt in eigenen Worten, was er
braucht („mach mir ein Angebot draus"), die Zuordnung macht das System.

Begründung: Ein Käufer, der nach der Einrichtung `core/`, `vertraege/` und
`testfaelle/` sieht, denkt „Entwicklerkram" — genau das entscheidet über den
Wow-Moment.

## Definition of Done Phase 3 — Stand 20.08.2026

Alle vier Punkte müssen erfüllt sein.

**1. Kompletter Durchlauf auf einem frischen, fremden Rechner unter 30 Minuten,
ohne Vorkenntnisse der Testperson.** — **OFFEN.** Nie gemessen. Der simulierte
Durchlauf im Abbruch-Test lief über fünf Sitzungen und sagt nichts über die
Zeit, weil er die Antworten aus einem Drehbuch nahm. Nach dem, was der Durchlauf
an Arbeit gezeigt hat — zehn Interviewfragen, fünf bis sechs Dateien füllen,
eine echte Aufgabe samt Korrekturschleife —, ist die 30-Minuten-Grenze knapp,
aber nicht offensichtlich verfehlt.

**2. Abbruch-Test bestanden.** — **ERFÜLLT.** Fünf Phasen, fünf harte Abbrüche,
fünfmal nur das Wort „weiter", fünfmal bestanden. Ohne Übergabetext, ohne
Erklärung, ohne Souffleur. Einzelheiten oben und in
`docs/abbruch-test-phase3.md`.

**3. `notfall/` deckt die fünf häufigsten Fehlerbilder ab — plus die
„weiter"-Anleitung.** — **ERFÜLLT, aber nur formal geprüft.** Die sechs Dateien
existieren und die README ordnet sie zu. Der Abbruch-Test hat sie nicht
gebraucht: In keinem der fünf Fälle war ein Notfalltext nötig, weil „weiter"
jedes Mal trug. Damit ist belegt, dass sie **da** sind — nicht, dass sie
**wirken**. Ob ein Käufer mit `03-zahl-oder-fakt-stimmt-nicht.md` sein Problem
löst, weiß erst die Beta. Die Liste der fünf Fehlerbilder ist außerdem aus
Annahmen entstanden, nicht aus Support-Fällen.

**4. Die Kundenansicht enthält keinen technischen Begriff und keinen Ordner,
der nicht erklärt wurde.** — **NICHT ERFÜLLT.** Der Wurzelordner enthält nach
der Einrichtung sechs Einträge: `START.md`, `mein-profil.md`,
`meine-unterlagen/`, `ergebnisse/`, `system/` und **`CLAUDE.md`**. `START.md`
erklärt die ersten fünf. **`CLAUDE.md` kommt darin nicht vor** — mechanisch
geprüft, weder in der erzeugten Datei noch in `START.vorlage.md`. Diese Datei
steht in `docs/STATUS-BAU.md` unter „Offene Punkte" als „aufgefangen über
`START.md`, das die Datei in einer Zeile abtut" — **diese Zeile gibt es nicht.**
Der Text der Kundenansicht selbst ist sauber: kein Fachbegriff in `START.md`,
und in den fünf geprüften Abbruchfällen fiel dem Nutzer gegenüber keiner.

## Stand Phase 3 (19.08.2026) — gebaut, aber noch nicht bewiesen

**Gebaut und committet:**

- `core/unterlagen/aufbau.md` und `core/unterlagen/preisregeln.md` — die
  dritte Wissensquelle und die drei Preisregeln, plattformneutral.
- `core/interview/fragen.md` — die zehn Fragen im Wortlaut, mit Beispielen,
  Nachhak-Regeln und Checkliste. Frage 9 ist die Materialfrage.
- Vier Vorlagen: `profil.vorlage.md` (→ `mein-profil.md`),
  `STATUS.vorlage.md` (trägt die Fortsetzung), `CLAUDE.vorlage.md` (weiter,
  drei Quellen, Zuordnungstabelle), `START.vorlage.md` (neu).
- `adapter-claude/INSTALLER.md` — fünf Phasen, je mit Schritten, dem
  wörtlichen Text an den Nutzer und einer Checkliste.
- `notfall/` — fünf Fehlerbilder plus die „weiter"-Anleitung, README als
  Zuordnungstabelle.

**Ein Fund beim Bauen, der die Anforderung gerettet hat.** Der ursprüngliche
Plan hätte `CLAUDE.md` erst in Phase 3 erzeugt. Dann hätte eine neue Sitzung
in Phase 1 und 2 **nichts** gehabt, was sie zu `STATUS.md` führt — „weiter"
wäre ins Leere gelaufen, und der Abbruch-Test wäre in zwei von fünf Phasen
unbestehbar gewesen. Jetzt legt Phase 1 als allererste Handlung `STATUS.md`
und eine Startfassung von `CLAUDE.md` an, noch vor jeder Prüfung; das Anlegen
ist zugleich die Probe auf das Schreibrecht.

**Stand der drei Nachweise (20.08.2026):**

1. **Kein Durchlauf auf einem fremden Rechner — weiter offen.** Die
   30-Minuten-Grenze ist geschätzt, nicht gemessen.
2. **Abbruch-Test — erledigt, 5 von 5 bestanden.** Anforderung 1 ist damit
   erfüllt, nicht mehr nur gebaut (`docs/abbruch-test-phase3.md`).
3. **Nachlauf — zum größeren Teil erledigt.** Die fünf
   `angebots-schreiber`-Fälle sind gelaufen: vier bestanden, einer wackelt und
   braucht eine Entscheidung. Die zwei `ketten`- und drei
   `follow-up-generator`-Fälle stehen weiter aus
   (`docs/nachlauf-phase3.md`).

Phase 3 ist damit **nicht** abgeschlossen — aber der Grund ist nicht mehr, dass
nichts geprüft wäre.

## Nachlauf Phase 3 — erledigt am 20.08.2026

Bericht: `docs/nachlauf-phase3.md`. Dort steht die Quelle der Wahrheit, nicht
hier.

**Gelaufen: die fünf `angebots-schreiber`-Fälle, je dreimal** — Erzeugung und
Bewertung strikt getrennt, Erzeuger ohne Kriterien, Bewerter ohne Skill-Text.
16 Erzeugungen, 16 getrennte Bewertungen (Fall 05 bekam durch einen Vorfall im
Testaufbau einen vierten Lauf und wurde mit **4 von 4** gemessen).

| Fall | Ergebnis |
|---|---|
| `01-rueckfrage-disziplin` | **bestanden** (3/3) |
| `02-budget-konflikt` | **wackelt** — Befund, Entscheidung nötig |
| `03-verbots-kollision` | **bestanden** (3/3) |
| `04-preisgrundlage-abgelaufen` | **bestanden** (3/3) — neu |
| `05-kundenkondition-vorrang` | **bestanden** (4/4) — neu |

**Neu gegenüber Phase 2: die Preisunterlagen lagen als echte Dateien vor**,
nicht als Beschreibung im Auftrag. Fall 04 bekam einen `preise/`-Ordner mit
`preisliste-2025-10.md` (`Stand: 15.10.2025`, kein `gültig bis`), Fall 05 die
gültige Liste plus einen Kundenordner mit Rahmenvertrag. Der Skill musste den
Stand also selbst ermitteln, statt ihn vorgesagt zu bekommen.

**Anforderung 3 ist damit wirksam, nicht nur gebaut.** Beide neuen Fälle
bestehen auf Anhieb, ohne Skill-Änderung. Regel 2 (Gültigkeit) hält auch gegen
eine Datei ohne `gültig bis`; Regel 3 (Rangfolge) hält auch dort, wo der
Rahmenvertrag **teurer** ist als die Preisliste — kein Lauf hat den günstigeren
Listensatz genommen.

### Der eine Befund: `02-budget-konflikt` — Entscheidung steht aus

Der Fall hat in der Vollregression 3 von 3 bestanden. Jetzt: zwei von drei
Läufen schreiben **kein** Angebot, sondern fragen nach dem Empfänger-Verhältnis
(Neukunde oder Bestandskunde). Der dritte schreibt das Angebot und **setzt**
`neukunde`, vermerkt in Block B unter `Angenommen`.

**Der Befund liegt im Testfall, nicht im Skill.** Die Anfrage in `## Eingabe`
nennt das Verhältnis nicht. Es ist der **sechste Pflicht-Fakt**, und der Skill
schreibt für einen leeren Pflicht-Fakt zwingend vor: nachfragen, anhalten, kein
Angebot. Die zwei durchgefallenen Läufe haben die Regel **befolgt**; der
bestandene hat sie **gebrochen**.

**Der Testfall belohnt damit das Raten und bestraft das Nachfragen.** Ein Skill,
der ihn zuverlässig besteht, wäre schlechter als einer, der durchfällt.

Warum es vorher nicht auffiel: Anforderung 2 hat `meine-unterlagen/` eingeführt.
Beide durchgefallenen Läufe haben dort nachgesehen — in `preise/kunden/` und in
`angebote/` — und nichts zu diesem Kunden gefunden. Genau dieser Blick macht die
Lücke sichtbar. Die neue Wissensquelle hat den Fall nicht kaputt gemacht,
sondern einen Mangel freigelegt, den er von Anfang an hatte.

**Nach der Änderungsregel vom 18.08.2026 wurde nichts angefasst** — weder
Testfall noch Skill. Vorschlag zur Entscheidung: den Eingabeteil um einen
Halbsatz ergänzen, der Fakt 6 klärt, mit Änderungsvermerk, danach dreimal neu.
Die Gegenrichtung — Fakt 6 im Skill entschärfen — würde eine harte Regel gegen
ein bequemes Testergebnis tauschen, und der Fall prüft den Budget-Konflikt
danach immer noch nicht.

**Bis zur Entscheidung ist `02-budget-konflikt` nicht bestanden.**

### Nicht gelaufen, weiter offen

Der Auftrag umfasste die fünf `angebots-schreiber`-Fälle. **Nicht** gelaufen
sind:

| Fall | Warum er laufen muss | Läufe |
|---|---|---|
| `ketten/01-recherche-fast-leer` | Skill geändert, Testprofil geändert | 3 |
| `ketten/02-entwurf-und-abgelehnte-forderung` | Vertrag geändert | 3 |
| `follow-up-generator/01-unvollstaendiger-uebergabeblock` | Vertrag hat ein Pflichtfeld mehr | 3 |
| `follow-up-generator/02-kein-anlass` | dito | 3 |
| `follow-up-generator/03-stufe-drei-und-schluss` | dito | 3 |

Bei den drei `follow-up-generator`-Fällen ist der Skill unverändert, aber ihre
**Eingabe** ist vertraglich definiert, und der Vertrag hat mit `Preisstand` ein
Feld mehr. Die Testfall-Blöcke enthalten es nicht — genau der Fall, für den die
Ausnahme im Vertrag steht („Innenangabe", wird nicht gelesen, löst keine
Rückfrage aus). Ob die Ausnahme trägt, weiß man erst nach dem Lauf.

**Für diese fünf Fälle gilt die Zahl aus Phase 2 unverändert nicht.**

## Abbruch-Test Phase 3 — bestanden am 20.08.2026

Bericht: `docs/abbruch-test-phase3.md`, mit allen fünf Fällen einzeln.

**Fünf Phasen, fünf harte Abbrüche, fünfmal nur das Wort „weiter" — fünfmal
bestanden.** In keinem Fall wurde nach dem Stand gefragt, in keinem Fall an der
falschen Stelle fortgesetzt.

| Phase | Abbruchstelle | Fortsetzung |
|---|---|---|
| 1 — Ist alles startklar | mitten im Umräumen | bestanden |
| 2 — Kennenlernen | nach Frage 7, ohne Antwort | bestanden |
| 3 — Einrichten | drei von sechs Assistenten gefüllt | bestanden |
| 4 — Erste echte Aufgabe | Rückfrage raus, keine Antwort | bestanden |
| 5 — Wächter und Übergabe | vor dem Beibringen des Zauberworts | bestanden |

**Aufbau:** ein einziger Durchlauf durch alle fünf Phasen, fünfmal unterbrochen
— nicht fünf frische Durchläufe. Je Fall drei getrennte Sitzungen, die nichts
voneinander wissen: die Einrichtungssitzung (hält mitten im Schritt an, schreibt
**keinen** Übergabetext), die frische Sitzung (bekommt Ordner, Gedächtnisdatei
und als einzige Nachricht `weiter`), die Bewertung (sieht Stand, Tatsachen und
Mitschrift — **nicht** die Anleitung).

**Der eigentliche Nachweis: In Phase 1, 2 und 3 war der Stand auf der Platte im
Moment des Abbruchs nachweislich falsch.** In Phase 1 behauptete er, es sei noch
nichts verschoben, während `core/` schon verschoben war. In Phase 2 behauptete
er, Frage 7 sei noch nicht gestellt, während sie auf dem Bildschirm stand. In
Phase 3 behauptete er, die Phase habe noch nicht begonnen, während drei
Assistenten fertig gebaut waren. Die Fortsetzung hat das jedes Mal überlebt,
weil die Sitzung **nachgesehen hat, statt der Datei zu glauben**. Ein
Fortsetzungsmechanismus, der nur mit korrekten Ständen funktioniert, wäre hier
dreimal gescheitert.

### Die zweite Frage: Wusste der Nutzer, dass „weiter" das Zauberwort ist?

**In allen fünf Fällen ja — aber nie, weil der Installer es ihm beigebracht
hätte.**

| Phase | Woher er es wusste |
|---|---|
| 1 | nur aus `START_HIER.md` — der Installer hatte erst **einen** Satz gesagt |
| 2 | Assistent am Ende von Phase 1, dazu `START_HIER.md` |
| 3 | Assistent am Ende von Phase 2, eine Nachricht davor |
| 4 | Assistent am Ende von Phase 3, dazu **`START.md`** |
| 5 | **`START.md`** |

Der Schritt, der „weiter" ausdrücklich lehrt und üben lässt, ist Phase 5,
Schritt 2 — und er wurde in **keinem** der fünf Abbruchfälle erreicht. Das Netz
hält, weil es vierfach gespannt ist: `START_HIER.md` vor der Einrichtung, die
Phasenabschlüsse zwischendurch, `START.md` ab Ende Phase 3, `notfall/01` als
Rückfallebene.

**Das dünnste Glied ist Phase 1.** Dort gibt es genau eine Quelle:
`START_HIER.md`, wenige Minuten zuvor gelesen, vom Installer nie wiederholt.
Wer die Datei überflogen hat, um schnell an den Satz zum Kopieren zu kommen,
hat „weiter" nicht gelesen. Kein Blocker, aber die Stelle, an der zuerst etwas
reißen würde.

**Ein Wechsel, den niemand bemerkt:** `START_HIER.md` wandert am Ende von
Phase 3 nach `system/`. Die Quelle, die in den Phasen 1 und 2 das Netz war, ist
ab da weg — ersetzt durch `START.md`. Lückenlos, aber es ist ein Wechsel.

### Vier Befunde aus dem Abbruch-Test, keiner behoben

1. **Phase 3 des Installers schreibt keinen Zwischenstand.** Sie schreibt STATUS
   erst als Schritt 6, am Ende. Das verstößt gegen Bauprinzip 2 („nach jedem
   Schritt") und gegen die eigene eiserne Regel 3 („Ein Schritt ohne
   STATUS-Eintrag gilt als nicht gemacht"). Für Phase 2 ist die Ausnahme
   ausdrücklich geregelt, für Phase 3 fehlt sie — dabei ist Phase 3 die Phase
   mit der meisten unsichtbaren Arbeit. Folge im Test: Die Auswahl der sechs
   Assistenten ging verloren, die frische Sitzung wählte neu und kam auf fünf.
   Schaden entstand nur deshalb keiner, weil die neue Auswahl die drei fertigen
   Dateien zufällig enthielt.
2. **Das erzeugte Gedächtnis verliert den Weg zur Anleitung.** Die Kurzfassung
   aus Phase 1 nennt `INSTALLER.md` ausdrücklich; die vollständige Fassung aus
   `CLAUDE.vorlage.md`, die sie in Phase 3 ersetzt, nennt sie **nicht mehr**. Ab
   Ende Phase 3 hängt die Fortsetzung der Phasen 4 und 5 allein daran, dass der
   Stand den Weg selbst beschreibt. Eine Testsitzung hat sich das im Lauf
   ergänzt — der Zusatz wurde für die weiteren Fälle **wieder entfernt**, damit
   gegen das gebaute Produkt geprüft wird.
3. **Es gibt keinen Wächter zum Einrichten.** Phase 5, Schritt 1 sagt „Richte
   den Wächter ein". Eine Vorlage existiert weder in `core/` noch in
   `adapter-claude/vorlagen/` — mechanisch geprüft. Der Installer muss ihn frei
   erfinden; die Testsitzung baute `system/wochencheck.md` mit sieben selbst
   ausgedachten Prüfpunkten. **Jeder Käufer bekäme einen anderen Wächter.**
   Das stand als Risiko schon hier — jetzt ist es belegt.
4. **Die Verbotsliste wird zur Installationszeit vervielfältigt.** Sie steht
   danach in `mein-profil.md`, in `CLAUDE.md` und in **jeder** eingerichteten
   Skill-Datei. Ursache ist Phase 3, Schritt 2 („Ersetze in den ausgewählten
   Dateien jeden Platzhalter"). Im Repo ist Prinzip 1 sauber, **beim Kunden ist
   es gebrochen**. Die Folge zeigte sich sofort: Die Stilkorrektur aus Phase 4
   („kein ‚gerne'") griff nur an einer Stelle; die fünf Skill-Dateien blieben
   veraltet und wurden erst von der nächsten Sitzung nachgezogen — und das nur,
   weil es im Stand vermerkt war.

Dazu ein Befund aus einem anderen Skill, aufgefallen beim Füllen der
Platzhalter: In `core/skills/vertrieb/outreach-personalisierer.md` steht an
einer Stelle `{{firma}}`, wo die Firma des **Empfängers** gemeint ist. Eingesetzt
stünde dort die eigene Firma. Nicht behoben — nach der Arbeitsregel vom
19.08.2026 zieht seine Änderung seine drei Testfälle nach sich.

### Anmerkung zur Redlichkeit des Tests

Der Prüfpunkt 5 der Bewertung („kein Blick hinter die Kulissen") war in seinen
ersten beiden Fassungen **sachlich falsch** und wurde zweimal korrigiert, beide
Male vor dem ersten festgeschriebenen Urteil. Fassung 1 verbot das Angebot des
frischen Gesprächs — also eine Pflichthandlung aus Anforderung 1. Fassung 2
zählte „Ordner", „Datei" und „Gedächtnis" zu den verbotenen Fachbegriffen,
obwohl die Anleitung genau diese Wörter als die **erlaubten** benennt. Die
dritte Fassung übernimmt die Wortlisten der Anleitung, statt eine eigene zu
erfinden. Beide verworfenen Urteile liegen im Testaufbau; in beiden waren die
Prüfpunkte 1, 2, 3, 4, 6 und 7 unverändert erfüllt. Der Vorgang steht hier,
weil eine stille Korrektur an einem Bewertungsmaßstab von Weichspülen nicht zu
unterscheiden wäre.

## Offene Punkte
- **`CLAUDE.md` liegt sichtbar im Wurzelordner.** Die Plattform verlangt die
  Gedächtnisdatei dort; sie ist damit ein siebter Eintrag neben den vier
  Dingen und `system/`. Aufgefangen ist das über `START.md`, das `system/`
  und die Datei in einer Zeile abtut. **Zu prüfen:** ob Claude Code die Datei
  auch aus einem versteckten Ordner lädt — dann verschwindet sie ganz.
  Adapter-Frage, kein Blocker.
- **Installer-Phase 5 setzt den Wächter voraus**, den es noch nicht gibt
  (BAUPLAN Phase 4). Bis dahin läuft Phase 5 auf einen Skill zu, der fehlt —
  vor dem ersten echten Durchlauf zu schließen.
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
- **Erledigt (19.08.2026): `{{preisgrundlage}}` entschieden.** Keine eigene
  Interviewfrage. Primärquelle ist `meine-unterlagen/preise/`; Frage 9 wird zur
  Materialfrage; bedingte Zusatzfrage nur, wenn kein Preismaterial da ist und
  die Arbeit preisbildend ist. Register nachgezogen
  (`core/interview/mapping.md`), Begründung in `docs/entscheidungen.md`.
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

**Phase 3 ist zur Hälfte bewiesen.** Was für die Definition of Done noch fehlt,
in dieser Reihenfolge:

1. **Entscheidung zu `angebots-schreiber/02-budget-konflikt`** — der Testfall
   verlangt ein Angebot, obwohl seine Eingabe einen Pflicht-Fakt nicht hergibt.
   Vorschlag oben. Ein Satz Entscheidung, dann drei Läufe.
2. **Die fünf offenen Nachlauf-Fälle laufen lassen** — zwei `ketten`, drei
   `follow-up-generator`, je dreimal.
3. **Den Wächter bauen** (Befund 3 des Abbruch-Tests). Er ist formal
   Phase-4-Arbeit, blockiert aber Installer-Phase 5: Ohne Vorlage erfindet
   jeder Durchlauf einen anderen.
4. **Zwischenstand in Installer-Phase 3** (Befund 1) und **Weg zur Anleitung im
   erzeugten Gedächtnis** (Befund 2). Beides kleine Änderungen am Installer bzw.
   an `CLAUDE.vorlage.md` — beide ziehen einen neuen Durchlauf durch die
   Phasen 3 bis 5 nach sich.
5. **Entscheidung zur vervielfältigten Verbotsliste** (Befund 4) — Prinzip 1
   ist beim Kunden gebrochen. Architekturfrage, kein Handgriff.
6. **`START.md` erklärt `CLAUDE.md` nicht** — die Datei liegt sichtbar im
   Wurzelordner und kommt in `START.vorlage.md` nicht vor (mechanisch geprüft:
   kein Treffer). Definition of Done Punkt 4 verlangt, dass kein Eintrag
   unerklärt bleibt. Einzeiler in der Vorlage, aber er zieht einen neuen
   Phase-3-Durchlauf nach sich.
7. **Durchlauf auf einem fremden Rechner**, gestoppt.

---

**Was Phase 3 mitgebracht hat (Stand bei Beginn):** Phase 2 ist abgeschlossen
und belegt — zehn Skills, 32 Fälle, jeder dreimal erzeugt und dreimal getrennt
bewertet, 32 bestanden.

Was Phase 3 mitbringt:

1. Die Pflichtanforderung **„Sitzungswechsel unsichtbar"** (Abschnitt oben und
   `BAUPLAN.md`, Phase 3, Punkt 5) — Fortsetzen mit dem Wort „weiter", der
   Assistent bietet den Wechsel von sich aus an, der Installer bringt es bei
   und legt es zusätzlich in `notfall/` ab.
2. Die Anforderungen **2 bis 4** (`meine-unterlagen/`, Preisregeln,
   aufgeräumte Kundenansicht) — Abschnitt „Anforderungen an Phase 3" oben.
3. Die Entscheidung zu **`{{preisgrundlage}}`** ist gefallen (19.08.2026):
   keine eigene Interviewfrage, Primärquelle `meine-unterlagen/preise/`,
   bedingte Zusatzfrage als Auffangnetz. Dazu die Prüffrist von 6 Monaten
   (`{{preisfrist}}`, Standardwert ohne Frage).

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
