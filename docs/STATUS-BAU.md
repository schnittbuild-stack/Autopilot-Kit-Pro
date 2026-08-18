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
  - [ ] **Definition of Done NICHT erreicht** — Befund in `account-recherche`
        offen, zwei Fälle durch die Korrektur veraltet, Dreifachlauf für die
        übrigen 19 Fälle steht aus, siehe unten
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

**Stand nach Teilregression und Korrektur (18.08.2026):**

- [x] **Die schlimmere Hälfte der Lücke ist zu.** Die 11 Fälle, die nur gegen
      die *vorige* Skill-Fassung geprüft waren — darunter beide Ketten-Fälle —
      sind erneut gelaufen, je dreimal. Dazu der Wackelkandidat
      `follow-up-generator / 02-kein-anlass`: **3 von 3, er hält.**
- [x] **Ketten-Befund behoben und nachgewiesen.** `ketten / 02` fiel dreimal
      auf `abweichend`, weil `follow-up-generator` den vorgegebenen Aufhänger
      verwarf. Die Ursache lag in der Regel, nicht im Verhalten: Prozess-Schritt 4
      führte eine Rangfolge ohne das Feld `Nachfassen`, und der Vertrag nannte
      das Feld ausdrücklich unverbindlich. **Vertragsregel 4 ist geändert**
      (Feld bindend, Datum weiter Vorschlag, Abweichung nur per Rückfrage —
      protokolliert in `docs/entscheidungen.md`), Skill, Block B, Checkliste
      und Beispiele sind nachgezogen. Drei neue Läufe: **3 von 3 bestanden.**
- [ ] **Neuer bestätigter Befund: `account-recherche / 01-leere-quellenlage`.**
      Dreimal `abweichend`, dreimal dieselbe Ursache: Bei völlig leerer
      Quellenlage verlangt das Soll `Belegte Fakten: —`, der Skill füllt das
      Feld stattdessen mit der Eingabe des Nutzers (Firmenname, Zweck) — mit
      Herkunftsvermerk, also ohne Erfindung; keine Durchgefallen-Regel greift.
      Trotzdem lässt es eine Recherche als geleistet erscheinen, die es nicht
      gab. **Der Skill ist seit dem 17.08. unverändert** — im Testlauf ließ er
      das Feld leer und bestand, jetzt füllt er es dreimal. Über vier Läufe
      derselben Fassung: 1× bestanden, 3× abweichend. Korrektur gehört in
      `account-recherche`, nicht in den Testfall.
- [ ] **Zwei Fälle sind durch die Korrektur veraltet.**
      `follow-up-generator / 01` und `/ 02` stehen mit 3× `bestanden` da, diese
      Läufe stammen aber von **vor** der Änderung an `follow-up-generator`.
      Streng gelesen ist ihr Zustand offen; sie brauchen je drei neue Läufe.
- [ ] **Dreifachlauf für die übrigen 19 Fälle.** Sie sind gegen die aktuelle
      Fassung gelaufen, aber nur einmal. `account-recherche / 01` zeigt gerade,
      was ein einzelner Durchlauf wert ist: nichts.

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

## Nächster Schritt
1. **`account-recherche` korrigieren** — bei leerer Quellenlage gehört die
   Nutzereingabe nicht unter `Belegte Fakten`. Danach den Fall dreimal neu.
2. **`follow-up-generator / 01` und `/ 02` je dreimal nachziehen** — sie sind
   gegen die vorige Fassung gemessen.
3. **Dreifachlauf für die übrigen 19 Fälle.**

Belege und Zitate zu allem drei: `docs/testlauf-phase2-regression.md`.

Erst danach Phase 3 (Installer). Die Reihenfolge lohnt: Ein Installer, der
ungeprüfte Skills ausrollt, verlagert jeden Fehler in die Beta.

**Übertragbare Lehre aus dem Ketten-Befund:** Die Bindung stand nur im
Prozess-Fließtext — genau das Muster, das die neue Bauregel in
`core/skills/vertrieb/_TEMPLATE_SKILL.md` verbietet. Die Korrektur hat sie in
Ausgabeformat (`Aufhänger-Quelle`) und Checkliste verankert. Beim nächsten
Skill-Durchgang lohnt die dort beschriebene Gegenprobe für alle zehn Skills.
