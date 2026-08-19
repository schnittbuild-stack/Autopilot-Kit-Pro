# STATUS-BAU — Stand der Produktentwicklung

<!-- Unser eigenes Produkt-Prinzip, auf uns selbst angewandt: jede Session
     (Claude Code, Cowork, Mensch) liest diese Datei zuerst und pflegt sie. -->

## Stand
- [x] Phase 0 — Fundament: Entscheidungen getroffen (siehe docs/entscheidungen.md)
- [x] Phase 1 — Architektur & Repo-Skelett: Struktur, Vorlagen, Regeln, Action
- [ ] Phase 2 — Vertriebs-Skills & Verträge (BAUPLAN.md)
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
        getrennt bewertet: **30 bestanden, 1 abweichend, 1 wackelt.**
        Neun Skills und beide Ketten sind durch. **Neun Befunde gefunden und
        im Skill behoben**, kein Testfall weichgespült — **sechs davon waren
        Wackler**, die ein Einzellauf durchgewunken hätte.
  - [ ] **Zwei Fälle hängen an einer Entscheidung, nicht am Skill.**
        `meeting-nachbereitung / 01` (abweichend) und `/ 03` (wackelt)
        scheitern an Kriterien, die Einträge zählen statt Inhalte zu prüfen.
        Beide Läufe legten korrekt zusätzliche Punkte ab und fielen dafür
        durch. Vorschlag und Begründung stehen im Vollregressions-Dokument
        unter „Testfall-Befund `meeting-nachbereitung`" — **Entscheidung
        durch den Auftraggeber steht aus.**
- [ ] Phase 3 — Installer fertigstellen
  - [ ] **Sitzungswechsel unsichtbar** — neue Pflichtanforderung, siehe unten
- [ ] Phase 4 — Watchdog & Ketten-Tests
- [ ] Phase 5 — Smoke-Test (parallel, außerhalb dieses Repos: Ads + Landingpage)
- [ ] Phase 6 — Beta mit 10 Nutzern
- [ ] Phase 7 — Launch

## Definition of Done Phase 2 — Stand 18.08.2026

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
      damit der schwächste Skill im Kit. Gesamtfazit, alle neun Befunde und die
      offene Entscheidung: `docs/vollregression-phase2.md`.

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

Bisher angewandt: einmal, `angebots-schreiber/01-rueckfrage-disziplin` —
das Kriterium verlangte Kundenanrede und Signatur für eine Rückfrage, die an
den Nutzer selbst geht. Eine Prüfung aller 32 Fälle auf dieselbe Verwechslung
(Kundentext gegen interne Ausgabe) ergab keine weiteren Treffer.

## Anforderung Phase 3: Sitzungswechsel unsichtbar (18.08.2026)

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

## Offene Punkte
- Digistore24/CopeCart-Konto beantragen (Freischaltung dauert Tage)
- Produktname + Domain final
- START_HIER später zusätzlich als PDF (Markdown reicht für Beta)
- **Testfälle sind konstruiert, nicht aus der Praxis.** Die drei Fälle zu
  `angebots-schreiber` sind ehrlich hart, aber erfunden. Vor Beta gegen
  anonymisierte Realfälle tauschen — bis dahin taugen sie zur Entwicklung,
  nicht als Erfolgsquote nach außen.
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

## Vollregression — Stand 19.08.2026

Der Dreifachlauf über alle 32 Fälle läuft **portioniert über mehrere Sitzungen**,
um Nutzungskontingent nicht in einem Stück zu verbrennen. Bericht und
Fortschritt: `docs/vollregression-phase2.md`. Die Fortschrittstabelle dort
schreibt sich aus den Urteilsdateien selbst — sie ist die Quelle der Wahrheit
dafür, welcher Skill durch ist, nicht diese Datei.

**Erledigt (11 von 32 Fällen, alle bestanden, je dreimal):**
`angebots-schreiber` (3), `account-recherche` (3), `follow-up-generator` (3),
`ketten` (2).

**Zwei Befunde, beide im Skill behoben, kein Testfall angefasst:**

1. **`account-recherche`, 3× abweichend** — also stabil, kein Wackler. Das in
   der Gegenprobe verankerte Ausgabeformat für gleichlautende Firmennamen gab
   „genau 1 Unterscheidungsmerkmal" vor und hatte keine Zeile für einen Fund
   ohne Zuordnung. Die Zählvorgabe war als Zahl korrekt gebaut und inhaltlich
   falsch gewählt: Eine Rückfrage, die nur den Sitz nennt, entscheidet nichts.
   Korrigiert auf Sitz **und** Geschäftsfeld, plus Zeilen `Nicht zuordenbar`
   und `Vermutung`. Danach 3 von 3.
2. **`follow-up-generator`, `wackelt`** (bestanden · bestanden · abweichend).
   Zwei Punkte derselben Checkliste widersprachen sich, sobald beide im selben
   Fall greifen: „Rang 1–4 leer → kein Text" gegen „auf ausdrücklichen Wunsch
   entsteht der Text". Lauf 3 verweigerte, als Rückfrage getarnt. Vorrang jetzt
   an beiden Stellen geregelt. Danach 3 von 3 — und `02-kein-anlass` hält
   weiterhin, die Ausnahme hat die Kein-Anlass-Regel nicht aufgeweicht.

**Was die beiden Befunde über die Gegenprobe sagen:** Beide entstanden *durch*
sie. Sie hat die Regeln an die richtige Stelle geschrieben und dabei in einem
Fall den Inhalt beschädigt, im anderen einen Widerspruch erzeugt, der nur im
Zusammentreffen sichtbar wird. Eine Strukturprüfung kann das nicht sehen — sie
sieht saubere Regeln an sauberen Stellen. Das ist der Beleg dafür, dass der
Dreifachlauf nach der Gegenprobe kein Formalismus ist.

**Regel bestätigt:** Nach jeder Skill-Korrektur laufen **alle** Fälle dieses
Skills neu, auch die bereits bestandenen. So sind `account-recherche / 01` und
`follow-up-generator / 01` und `02` ein zweites Mal gelaufen. Mechanisch
geprüft: keine der 33 Ausgaben ist älter als die Skill-Datei, gegen die sie
gemessen wurde.

## Nächster Schritt
**Vollregression fortsetzen — 21 Fälle, sieben Skills:**
`ausschreibungs-analyse`, `crm-notiz-zu-schritt`, `einwand-sparring`,
`forecast-erklaerer`, `meeting-nachbereitung`, `outreach-personalisierer`,
`preisverhandlungs-sparring`.

Der Aufbau steht und ist wiederverwendbar: Zerlegung, getrennte Anweisungen für
Erzeugung und Bewertung, Statusskript, Berichtsgenerator. Ablauf je Fall:
dreimal erzeugen, dreimal bewerten, Bericht schreiben, committen, pushen.
Bestanden nur bei 3 von 3.

Erst danach Phase 3 (Installer). Ein Installer, der ungeprüfte Skills ausrollt,
verlagert jeden Fehler in die Beta.
