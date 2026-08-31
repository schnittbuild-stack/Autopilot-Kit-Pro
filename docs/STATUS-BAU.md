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
  - [x] **Nacharbeit aus dem Abbruch-Test (20.08.2026):** Prinzip 1 beim
        Kunden repariert, Zwischenstand in Phase 3 nachgezogen, Wächter-Vorlage
        gebaut — die Fälle 3 bis 5 danach wiederholt, **3 von 3 bestanden**
  - [x] **Riss aus Abbruch-Test Fall 2 behoben (21.08.2026)** — eiserne
        Regel 3 hält eine gestellte, unbeantwortete Frage jetzt im Stand fest;
        Fall 2 danach neu gelaufen, **bestanden**, alle sieben Prüfpunkte
        (`docs/abbruch-test-phase3.md`, vierter Durchlauf)
  - [ ] **Durchlauf auf einem fremden Rechner unter 30 Minuten — steht aus**
- [ ] **Phase 4 — Watchdog & Ketten-Tests (begonnen 26.08.2026)**
  - [x] Punkt 1 und 3 — Watchdog-Testlauf und Reparatur-Flow gebaut und
        geprüft (`core/waechter/watchdog.md`, `docs/watchdog-test.md`).
        Umfang nach Nutzung, jeder Fall dreimal. Vier Prüfanläufe, drei
        Befunde — darunter ein erfundener Abbruch im Wächter selbst.
        **Einschränkung:** Der Defekt wurde beim Lesen der Anleitung gefunden,
        nicht durch den Testlauf; der war grün. Der Nachweis ist damit
        schwächer, als die Meldung aussieht.
  - [x] **Punkt 2 — fünf Ketten-Testfälle statt zwei (27.08.2026)** — volle
        Kette, fehlendes Pflichtfeld, abgelaufener Preisstand; alle 3 von 3.
        Der Watchdog erfasst `ketten/` jetzt: Eine Kette läuft, sobald einer
        ihrer Helfer benutzt wurde. **Vorbehalt:** Fall 03 wurde viermal
        überarbeitet, bevor er grün war (`docs/ketten-testfaelle.md`).
  - [x] **Punkt 4 — kundeneigene Testfälle (28.08.2026)** — der Wächter
        bietet an, aus dem Material des Nutzers Prüffälle zu bauen;
        Sollkriterien werden einzeln bestätigt, nie vom Modell gesetzt.
        Dazu die Ketten-Rotation aus dem Kostenbefund von WO-009.
        **Offen bleibt die zweite Hälfte der Definition of Done:** drei Fälle,
        die ein Testkäufer als treffend bestätigt (`docs/eigene-testfaelle.md`).
  - [x] **Befund `ketten/01` untersucht (28.08.2026).** Reproduziert nicht —
        zwölf Läufe in vier Anordnungen, alle bestanden, darunter drei im
        **Originalbaum des Wächters**. Der eigentliche Befund liegt woanders:
        Sein Beleg war nach dem Sitzungsende weg, weil „er legt nichts ab"
        absolut galt. Behoben. Dazu die Doppeldeutigkeit im Vertrag
        (`Ansprechpartner [Optional]` gegen Pflicht-Fakt 1), die er selbst
        richtig vermutet hatte. `docs/ketten01-untersuchung.md`.
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

Bisher angewandt: **fünfmal.**

1. `angebots-schreiber/01-rueckfrage-disziplin` (18.08.) — das Kriterium
   verlangte Kundenanrede und Signatur für eine Rückfrage, die an den Nutzer
   selbst geht. Eine Prüfung aller 32 Fälle auf dieselbe Verwechslung
   (Kundentext gegen interne Ausgabe) ergab keine weiteren Treffer.
2. und 3. `meeting-nachbereitung/01-weiche-zusage` und `/03-stichwortnotizen`
   (19.08.) — beide machten eine **Anzahl** zur Bestehensbedingung und
   bestraften damit die Sorgfalt, die der Skill leisten soll. Jetzt inhaltlich
   gefasst; zusätzlich ist in Fall 03 die belegte, ausführlichere
   Teilnehmerzeile zulässig. Beide Fälle danach je 3 von 3.

4. `angebots-schreiber/02-budget-konflikt` (20.08.) — die Bestehensbedingung
   verlangte ein Angebot, obwohl die Eingabe den sechsten Pflicht-Fakt nicht
   hergibt. Sie belohnte damit das Raten und bestrafte das regelkonforme
   Nachfragen: Zwei von drei Läufen fielen durch, **weil sie sich an den Skill
   hielten**. Jetzt ist die Rückfrage das bestandene Ergebnis. Der Fall danach
   3 von 3. **Der Eingabeteil wurde nicht angefasst** — im Unterschied zum
   Vorschlag, der im Befund selbst stand.

5. `angebots-schreiber/03-verbots-kollision` (28.08.) — **dieselbe Lücke wie
   bei Fall 02, und trotzdem die umgekehrte Entscheidung: Hier wurde genau der
   Eingabeteil geändert und die Bewertung nicht angefasst.** Der Unterschied
   liegt im Zweck der Fälle. Fall 02 prüft den Umgang mit einem Budget-Konflikt;
   dort ist eine Rückfrage nach dem Verhältnis selbst ein sinnvolles Ergebnis,
   die Bewertung ließ sich also darauf umstellen, ohne den Fall zu entwerten.
   Fall 03 prüft, ob ein Verbot unter Druck hält — dazu muss ein Angebot
   entstehen, in dem das Nein steht. Eine Rückfrage sagt darüber nichts. Die
   Bewertung war hier nicht umstellbar, ohne den Fall wertlos zu machen; also
   musste die Eingabe die Lücke schließen. Gemessen: vorher **0 von 3**, danach
   2 von 3 — der verbliebene Lauf fragte nach der Firma, weil die Adresse einen
   Platzhalter trug. **Seit die Maskierung raus ist (WO-017): 3 von 3.**

**Erledigt am 19.08.2026** (hier am 28.08. nachgetragen): `einwand-sparring/03`
lieferte im Abschnitt `## Eingabe` die Bewertungslage mit und prüfte deshalb
schwächer, als er aussah. Der Absatz steht seit dem 19.08. im Kriterienteil,
mit Änderungsvermerk im Fall. Diese Zeile führte ihn neun Tage länger als
offen — der Befund stand an zwei Orten, gepflegt wurde einer.

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
**Nach der Nacharbeit vom 20.08.2026 erneut belegt:** Die drei von den
Änderungen berührten Fälle (Installer-Phasen 3, 4 und 5) sind wiederholt worden
— **3 von 3 bestanden**. Die Fälle 1 und 2 sind unberührt geblieben.
**Nach den sechs Textkorrekturen desselben Tages ein drittes Mal gemessen:**
die Fälle 2 bis 5, **drei bestanden, einer abweichend**. Keine der beiden
Durchfall-Bedingungen ist verletzt worden — in keinem Fall wurde nach dem Stand
gefragt, in keinem an der falschen Stelle fortgesetzt.
**Der Riss steckt in Fall 2 und ist echt:** Der Stand führt eine gestellte,
unbeantwortete Frage als „noch nicht gestellt", weil Phase 2 STATUS erst nach
der **Antwort** schreibt. Die frische Sitzung stellt Frage 7 deshalb ein
zweites Mal. Kosten: ein Satz, kein Datenverlust. **Nach der Skala des Tests
ist er bestanden; nach dem Wortlaut der Anforderung — „der Käufer soll nie
merken, dass eine Sitzung zu Ende geht" — merkt er es hier.** Behebung ist eine
Zeile in eiserner Regel 3; sie zieht einen neuen Phase-2-Durchlauf nach sich
und braucht deshalb eine Entscheidung. Einzelheiten im dritten Durchlauf in
`docs/abbruch-test-phase3.md`.
**BEHOBEN am 21.08.2026.** Eiserne Regel 3, Phase 2 Schritt 2 und die
Checkliste Phase 2 halten jetzt auch eine gestellte, unbeantwortete Frage im
Stand fest — so, wie `STATUS.vorlage.md` es ohnehin vormachte. Fall 2 ist
danach neu gelaufen: **bestanden, alle sieben Prüfpunkte**, mit ausdrücklicher
Würdigung von Prüfpunkt 3. Vierter Durchlauf in
`docs/abbruch-test-phase3.md`, Entscheidung in `docs/entscheidungen.md`.

**3. `notfall/` deckt die fünf häufigsten Fehlerbilder ab — plus die
„weiter"-Anleitung.** — **ERFÜLLT, aber nur formal geprüft.** Die sechs Dateien
existieren und die README ordnet sie zu. Der Abbruch-Test hat sie nicht
gebraucht: In keinem der fünf Fälle war ein Notfalltext nötig, weil „weiter"
jedes Mal trug. Damit ist belegt, dass sie **da** sind — nicht, dass sie
**wirken**. Ob ein Käufer mit `03-zahl-oder-fakt-stimmt-nicht.md` sein Problem
löst, weiß erst die Beta. Die Liste der fünf Fehlerbilder ist außerdem aus
Annahmen entstanden, nicht aus Support-Fällen.

**4. Die Kundenansicht enthält keinen technischen Begriff und keinen Ordner,
der nicht erklärt wurde.** — **ERFÜLLT seit dem 20.08.2026.** Der Wurzelordner
enthält nach der Einrichtung sechs Einträge: `START.md`, `mein-profil.md`,
`meine-unterlagen/`, `ergebnisse/`, `CLAUDE.md` und `system/`. **`START.md`
erklärt jetzt alle sechs** — die fehlende Zeile zu `CLAUDE.md` steht in
`START.vorlage.md`, und die Checkliste der Installer-Phase 3 prüft sie
mechanisch mit.
**Im dritten Abbruch-Durchlauf belegt, nicht nur gebaut:** Die erzeugte
`START.md` trägt die Zeile „**CLAUDE.md** — mein Gedächtnis. Da steht, was ich
über deine Arbeit weiß. Brauchst du nie zu öffnen.", und im Wurzelordner liegen
genau diese sechs Einträge. Der Text der Kundenansicht ist weiterhin sauber:
kein Fachbegriff in `START.md`, und in keinem der neun bisher geprüften
Abbruchfälle fiel dem Nutzer gegenüber einer.
**Bis hierher offen bleibt nur die Nebenfrage**, ob die Gedächtnisdatei auch
aus einem versteckten Ordner geladen würde — dann verschwände sie ganz. Für
Punkt 4 ist das nicht mehr nötig.

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
3. **Nachlauf — vollständig erledigt am 20.08.2026.** Erst die fünf
   `angebots-schreiber`-Fälle (vier bestanden, einer wackelte), dann der
   Befund entschieden und der korrigierte Fall neu gemessen, dann die fünf
   offenen Fälle. **Endstand: sechs Fälle, alle bestanden**, 21 Erzeugungen und
   21 getrennte Bewertungen (`docs/nachlauf-phase3.md`).

Phase 3 ist damit **nicht** abgeschlossen — aber es fehlt nur noch der
Durchlauf auf einem fremden Rechner. Die Entscheidung zu Fall 2 des
Abbruch-Tests ist am 21.08.2026 gefallen, der Befund behoben und neu belegt. Der Abschnitt „Nächster Schritt" ganz unten hält den Stand.

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

**Entschieden am 20.08.2026 — und anders als hier vorgeschlagen.** Nicht der
Eingabeteil wurde ergänzt, sondern **das Kriterium korrigiert**: Eine Rückfrage
nach dem Empfänger-Verhältnis ist bestanden, ein gesetzter Wert durchgefallen.
Änderungsvermerk im Testfall, Begründung in `docs/entscheidungen.md`. Danach
**3 von 3 bestanden**. Der Preis der Entscheidung steht im Testfall unter „Was
dieser Fall nicht mehr prüft": Prozess-Schritt 5 (Budget-Konflikt offenlegen)
wird jetzt von **keinem** Fall mehr gemessen — als offener Punkt vermerkt.

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

**Erledigt am 20.08.2026 — alle fünf gelaufen, alle bestanden.** Dazu der
korrigierte Fall `02-budget-konflikt`, also sechs Fälle, 21 Erzeugungen und 21
getrennte Bewertungen. Bericht: `docs/nachlauf-phase3.md`, Abschnitt „Nachtrag
20.08.2026". **Ein Befund lag im Skill** (`follow-up-generator/03`: der
Gegenvorschlag fehlte neben dem Text auf ausdrückliche Ansage), ist dort
behoben, und danach sind **alle vier Fälle dieses Skills** neu gelaufen —
`follow-up-generator/01`, `/02`, `/03` und `ketten/02`. Die
`Preisstand`-Ausnahme aus Vertragsregel 5 trägt: Kein Lauf hat das fehlende
Feld erfragt, ergänzt oder beanstandet.

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

## Nacharbeit aus dem Abbruch-Test — begonnen am 20.08.2026

Drei der vier Befunde werden behoben, in dieser Reihenfolge: Prinzip-1-Bruch
beim Kunden (Befund 4), Zwischenstand in Installer-Phase 3 (Befund 1),
Wächter-Vorlage (Befund 3). Befund 2 (der Weg zur Anleitung im erzeugten
Gedächtnis) bleibt vorerst offen.

### Baustein 1 — Prinzip 1 beim Kunden repariert (20.08.2026)

**Die Entscheidung: Platzhalter werden nicht mehr ersetzt.** `{{verbote}}`,
`{{signatur}}`, `{{tonalitaet}}` und die übrigen bleiben in den Kundendateien
stehen und werden **beim Lesen** aufgelöst — Profilwerte aus `mein-profil.md`,
Material aus `meine-unterlagen/`. Damit steht Profilwissen beim Kunden genau
einmal, so wie im Repo. Begründung im Entscheidungsprotokoll.

**Warum das keine neue Mechanik ist:** `core/vertraege/`,
`core/unterlagen/preisregeln.md`, `core/unterlagen/aufbau.md` und die
Testfälle tragen ihre Platzhalter längst unersetzt und werden beim Lesen
aufgelöst — der Installer hat sie nie angefasst. Ersetzt wurden **nur** die
Skill-Dateien. Die Umstellung beseitigt also eine Ausnahme, statt eine Regel
einzuführen.

**Was geändert wurde — vier Dateien, keine davon ein Skill:**

- `core/interview/mapping.md` — neuer Abschnitt „Ein Platzhalter ist ein
  Verweis, keine Lücke“ mit den drei Folgeregeln; das Register hat eine
  Spalte mehr: **wo der Wert beim Kunden steht** (Feldname in
  `mein-profil.md` bzw. Ordner in `meine-unterlagen/`).
- `adapter-claude/INSTALLER.md` — Phase 3, Schritt 2 heißt jetzt „Die
  Verweise prüfen — und nichts ersetzen“: nachsehen, ob jeder Verweis im
  Register steht und sein Feld im Profil existiert, sonst nichts. Schritt 3
  zieht dieselbe Regel für `CLAUDE.md` nach. Phase 4, Schritt 4 sagt
  ausdrücklich, dass eine Korrektur **nur** ins Profil geht. Checkliste
  entsprechend: aus „Kein `{{` mehr in einer der Dateien“ wird „in den
  ausgewählten Dateien wurde nichts ersetzt“.
- `adapter-claude/vorlagen/CLAUDE.vorlage.md` — neuer Abschnitt „Was in
  doppelten Klammern steht, ist ein Verweis“; `ge{{anrede}}t` war eine
  Wortmitte-Ersetzung und ist zu „Anrede gegenüber Kunden: {{anrede}}“
  aufgelöst, weil ein Verweis in der Wortmitte nicht lesbar bleibt.
- `adapter-claude/vorlagen/profil.vorlage.md` — für den Nutzer ein Satz, dass
  eine Änderung hier sofort überall gilt; im Kommentar die Warnung, dass
  Feldnamen nicht stillschweigend umbenannt werden, weil Verweise darauf
  zeigen.

**Kein Skill wurde angefasst** — die Arbeitsregel vom 19.08.2026 gilt, und
keiner der 32 Testfälle verliert dadurch seine Gültigkeit.

**Zwei Stellen bleiben bewusst Kopien**, beide keine Profilwerte: die
Zuordnungstabelle in `CLAUDE.md` (Sätze des Nutzers als Wegweiser zum
richtigen Assistenten) und die Beispielsätze in `START.md` (die eine Datei,
die er wirklich liest — ein Verweis stünde dort statt eines Satzes, den er
sagen kann).

**Nebeneffekt, der einen zweiten Mangel schließt:**
`notfall/02-klingt-nicht-nach-mir.md` schickt den Nutzer ins Profil und
ändert **nur** dort. Bisher war dieser Text wirkungslos, sobald der falsche
Ton aus einer eingesetzten Kopie kam. Jetzt trägt er.

**Ein Wortlaut ist nachzuziehen, nicht behoben:**
`core/skills/vertrieb/angebots-schreiber.md` sagt in einem Kommentar, der
Hausstil komme „zur Installationszeit“ aus `{{tonalitaet}}`, `{{anrede}}` und
`{{stilbeispiele}}`. Richtig ist jetzt: beim Lesen. Das Verhalten ändert sich
dadurch nicht, der Satz ist trotzdem falsch. Nicht geändert, weil eine
Skill-Änderung die fünf Testfälle dieses Skills neu laufen lässt
(Arbeitsregel 19.08.2026).

**Nachweis erbracht (20.08.2026):** Im wiederholten Abbruch-Test blieb
`system/core/` Byte für Byte unverändert, und die Stilkorrektur des Nutzers
wirkte aus dem Profil heraus — ohne dass eine einzige Datei nachgezogen werden
musste. Abschnitt „Der Nachweis" unten.

### Baustein 2 — Installer-Phase 3 schreibt jetzt Zwischenstände (20.08.2026)

**Der Befund:** Phase 3 schrieb STATUS erst als Schritt 6, ganz am Ende — ein
Verstoß gegen Bauprinzip 2 und gegen die eigene eiserne Regel 3. Im Abbruch-Test
ging dadurch die Auswahl der sechs Assistenten verloren; die frische Sitzung
wählte neu und kam auf fünf. Schaden entstand nur zufällig keiner.

**Was geändert wurde:**

- **Eiserne Regel 3** nennt Phase 3 jetzt ausdrücklich: „Innerhalb von Phase 2
  nach **jeder** Antwort, innerhalb von Phase 3 nach **jedem** Schritt.“ Die
  Ausnahme, die bisher nur für Phase 2 geregelt war, gilt jetzt für beide.
- **Phase 3 bekommt einen Vorspann**, der begründet, warum ausgerechnet hier:
  Der Nutzer sieht nichts, der Installer redet nicht — was nicht in der Datei
  steht, ist weg.
- **Schritt 1 schreibt die Auswahl, bevor er irgendetwas anderes tut.**
  Namentlich, in der Reihenfolge. Das ist der Eintrag, dessen Fehlen den
  Testfall gekostet hat.
- **Die Schritte 2 bis 5 haken einzeln ab** — je eine Zeile „Dann STATUS“ im
  Schritt selbst, nicht nur im Fließtext davor. (Bauregel aus der Gegenprobe:
  Regeln, die nur im Fließtext stehen, werden nachweislich ignoriert.)
- **Schritt 5 räumt in derselben Reihenfolge auf wie Phase 1** — erst
  vermerken, dann verschieben, dann abhaken. Genau dieser Ablauf hat den
  Abbruch in Phase 1 überlebt.
- **Die Checkliste** prüft zwei Dinge zusätzlich: dass die Auswahl **vor** dem
  zweiten Schritt in STATUS steht, und dass es fünf Zwischenstände gibt statt
  eines Eintrags am Ende.
- **`STATUS.vorlage.md` bekommt den Platz dafür:** einen Abschnitt „Die
  ausgewählte Mannschaft“ mit der Liste und den vier Häkchen der Phase. Ohne
  eigenen Abschnitt landet die Auswahl im Fließtext und wird beim nächsten
  Überschreiben still verschluckt.

**Nachweis erbracht (20.08.2026):** Die Auswahl stand im Stand und hat den
Abbruch überlebt; die frische Sitzung hat genau diese fünf Assistenten zu Ende
eingerichtet. Abschnitt „Der Nachweis" unten.

### Baustein 3 — den Wächter gibt es jetzt (20.08.2026)

**Der Befund:** Installer-Phase 5 sagte „Richte den Wächter ein“, ohne dass
irgendwo eine Vorlage lag — mechanisch geprüft, weder in `core/` noch in
`adapter-claude/vorlagen/`. Die Testsitzung hat sich `system/wochencheck.md`
mit sieben selbst ausgedachten Prüfpunkten gebaut. Jeder Käufer bekäme einen
anderen Wächter.

**Die Entscheidung: feste Minimal-Vorlage statt Zurückstellen.** Begründung im
Entscheidungsprotokoll — kurz: Das Problem war nie, dass es einen Wächter gibt,
sondern dass ihn jede Sitzung erfindet. Eine Streichung hätte das auch
beseitigt, aber mitsamt dem Nutzen, und ausgerechnet im Übergabemoment.

**`core/waechter/wochencheck.md` — vier Prüfpunkte, keine fünf:**

1. **Klingt es noch nach ihm?** Die neuesten Ergebnisse gegen `mein-profil.md`,
   vor allem gegen die Liste „Sätze und Themen, die nie vorkommen“. Ein Treffer
   ist immer ein Befund.
2. **Rechnet er noch mit gültigen Preisen?** `meine-unterlagen/preise/` nach
   `core/unterlagen/preisregeln.md` — Stand, Frist, abgelaufene
   Kundenkonditionen.
3. **Ist etwas liegengeblieben?** Aus STATUS: Nachlieferungen und offene
   Punkte. Einmal erinnern, nie zweimal mahnen.
4. **Fehlt ein Helfer?** Eine Aufgabe ohne Eintrag in der Zuordnungstabelle —
   nachtragen anbieten, nie „nicht installiert“ sagen.

Dazu die harten Grenzen: Er **ändert nichts** ohne ausdrückliches Ja, er
erfindet keinen Befund („konnte ich nicht prüfen“ ist eine zulässige Antwort,
„sauber“ wäre eine Lüge), er gibt höchstens fünf Zeilen aus und zählt nie auf,
was er alles geprüft hat.

**Was sich am Installer ändert:** Phase 5, Schritt 1 heißt jetzt „Den
Wochencheck **bekannt machen**“. Gebaut wird nichts. Der Schritt setzt das
Datum in STATUS, prüft die Auslöser-Zeile in `CLAUDE.md` und erklärt den Check
in zwei Sätzen, die nicht mehr versprechen, als er kann. Die Checkliste verbietet
ausdrücklich, am Wächter zu bauen.

**Vier weitere Stellen, damit der Auslöser nicht ins Leere zeigt:**
`CLAUDE.vorlage.md` (Regel: „Mach den Wochencheck“ → die Datei abarbeiten,
keine eigenen Prüfpunkte), `STATUS.vorlage.md` (Zeile „Letzter Wochencheck“ —
ohne sie prüft jeder Lauf denselben Zeitraum noch einmal), `START.vorlage.md`
(eine Zeile in Alltagssprache — sonst hört der Käufer den Satz einmal in Phase 5
und findet ihn nie wieder, genau die Lücke, die beim Wort „weiter“ schon
aufgefallen ist) und `BAUPLAN.md` Phase 4 (der Watchdog baut den Wochencheck
aus, statt einen zweiten daneben zu stellen).

**Bewusst klein gehalten:** Alle vier Prüfpunkte sind **ohne Testlauf**
entscheidbar. Ob ein Assistent seine eigenen Regeln einhält, kann erst der
Watchdog aus Phase 4 feststellen — das steht in der Datei selbst unter „Was
dieser Wochencheck noch nicht kann“, damit Phase 4 nicht raten muss.

**Nachweis erbracht (20.08.2026):** Im wiederholten Fall 5 wurde kein Wächter
gebaut und keiner erfunden — es gilt die feste Vorlage. Abschnitt „Der
Nachweis" unten. **Nicht** belegt ist, dass der Check etwas Nützliches findet:
Er ist nie gelaufen.

### Der Nachweis — Fälle 3 bis 5 wiederholt, 3 von 3 bestanden (20.08.2026)

Bericht: `docs/abbruch-test-phase3.md`, Abschnitt „Wiederholung der Fälle 3
bis 5". Dort steht die Quelle der Wahrheit, nicht hier.

Alle drei Bausteine greifen in den Installer-Phasen 3 bis 5; die Fälle 1 und 2
sind von keiner Änderung berührt und gelten unverändert. Wiederholt wurde nach
demselben Aufbau: ein Durchlauf, dreimal unterbrochen, je drei getrennte
Sitzungen, dieselben sieben Prüfpunkte.

| Phase | Abbruchstelle | Fortsetzung |
|---|---|---|
| 3 — Einrichten | mitten in Schritt 2, drei von fünf Dateien geprüft | **bestanden** |
| 4 — Erste echte Aufgabe | Rückfrage raus, keine Antwort | **bestanden** |
| 5 — Wächter und Übergabe | nach Schritt 1, vor dem Zauberwort | **bestanden** |

**Was damit belegt ist:**

- **Baustein 2:** Die Auswahl hat den Abbruch überlebt. Die frische Sitzung hat
  genau die fünf Assistenten zu Ende eingerichtet, die im Stand standen — beim
  ersten Durchlauf ging die Auswahl verloren und wurde neu getroffen.
- **Baustein 1:** `system/core/` ist nach dem ganzen Durchlauf **Byte für Byte
  identisch** mit dem Auslieferungszustand; kein `{{…}}` wurde ersetzt. Die
  Stilkorrektur des Nutzers steht **einmal** im Profil, im Angebot taucht das
  verbotene Wort nicht auf, und **nichts musste nachgezogen werden**. Beim
  ersten Durchlauf blieben dafür fünf Skill-Dateien veraltet.
- **Baustein 3:** Es wurde kein Wächter erfunden. Es gibt keine Datei
  `system/wochencheck.md`; es gilt die feste Vorlage unverändert, und der
  Nutzer hat die zwei vorgeschriebenen Sätze bekommen.

**Was nicht belegt ist:** Der Wochencheck ist nie **gelaufen** — belegt ist,
dass es ihn gibt und dass ihn niemand mehr erfindet, nicht dass seine vier
Prüfpunkte etwas Nützliches finden. Das prüft erst Phase 4. Außerdem ist es ein
Durchlauf, kein Dreifachlauf, und die Antworten kamen aus einem Drehbuch — über
die 30-Minuten-Grenze sagt auch dieser Lauf nichts.

**Fünf neue Befunde**, keiner behoben, alle unten unter „Offene Punkte".
Zwei bekannte Lücken hat der Durchlauf unabhängig bestätigt: Das erzeugte
Gedächtnis nennt den Weg zur Anleitung nicht mehr, und `START.md` erklärt
`CLAUDE.md` nicht. Beide Male hat eine Testsitzung die Lücke selbst bemerkt und
repariert; beide Reparaturen wurden wieder entfernt, damit gegen das gebaute
Produkt geprüft wird (Anmerkung zur Redlichkeit im Bericht).

## Offene Punkte
- **Erledigt (20.08.2026): Das Gedächtnis erlaubt die Profiländerung, die
  Phase 4 verlangt.** `CLAUDE.vorlage.md` hat jetzt eine eng gefasste Ausnahme:
  Korrigiert der Nutzer eine Formulierung an einem Ergebnis, geht sie in
  `mein-profil.md`, wird ihm gesagt und in STATUS vermerkt — **nur ins Profil**.
  Begründung in `docs/entscheidungen.md`. **Belegt** im dritten Abbruch-Durchlauf,
  Fall 4: Die Stilkorrektur („kein ‚gerne‘") landete an genau einer Stelle, und
  das Wort taucht im Angebot nicht auf. Der ursprüngliche Befund lautete:
- ~~**Das Gedächtnis verbietet, was Installer-Phase 4 verlangt (20.08.2026).**~~
  `CLAUDE.vorlage.md` sagt: „`mein-profil.md` wird nur geändert, wenn der
  Nutzer ‚Einstellungen ändern‘ sagt. Nie nebenbei." Phase 4, Schritt 4
  verlangt aber genau **eine** Profiländerung — die Stilkorrektur. Eine frische
  Sitzung, die mitten in Phase 4 einsteigt und nur das Gedächtnis liest, würde
  sie nicht eintragen; der Nutzer müsste sie ein zweites Mal sagen.
  **Folgebefund von Baustein 1:** Seit Werte nicht mehr kopiert werden, hängt
  die Wirkung jeder Stilkorrektur allein am Profil — und damit an dieser einen
  Regel. Behebung: Ausnahme in `CLAUDE.vorlage.md`. Zieht einen neuen
  Phase-3-bis-5-Durchlauf nach sich.
- **Erledigt (20.08.2026): Eiserne Regel 1 nimmt die Rückfrage des Assistenten
  aus.** In Phase 4 fragt der Installer so, wie der Assistent es täte — alle
  fehlenden Pflichtangaben in **einer** nummerierten Nachricht. Die Ein-Frage-Regel
  gilt für die Fragen zur Einrichtung, nicht für die Arbeit des Assistenten.
  **Belegt** im dritten Abbruch-Durchlauf: Die Einrichtungssitzung hat Termin und
  Zielbild in einer Nachricht erfragt, ohne den Widerspruch neu entscheiden zu
  müssen. Der ursprüngliche Befund lautete:
- ~~**Eiserne Regel 1 widerspricht dem `angebots-schreiber` (20.08.2026).**~~ Der
  Installer sagt „Eine Frage pro Nachricht. Immer.", der Assistent stellt alle
  fehlenden Pflicht-Fakten in **einer** nummerierten Nachricht — und
  `angebots-schreiber/01-rueckfrage-disziplin` wertet genau das als bestanden.
  Phase 4 verlangt zugleich, nachzufragen, „wie es der Assistent später auch
  täte". Die Testsitzung hat sich für den Assistenten entschieden und den
  Widerspruch selbst vermerkt. Ohne Ausnahme in `INSTALLER.md` entscheidet das
  jede Sitzung neu.
- **Erledigt, aber ungeprüft (20.08.2026): Wochencheck-Prüfpunkt 1 prüft den
  Kundentext, nicht die Notiz darüber.** Von den zwei angebotenen Wegen ist der
  erste gewählt worden — der Fehler lag in der Reichweite des Prüfpunkts, nicht
  in der Schreibweise der Notiz. Ein verbotenes Wort, das in einer Notiz
  ausdrücklich als gestrichen dasteht, ist der Beleg, dass die Regel gegriffen
  hat; im Kundentext bleibt jeder Treffer ein Befund. **Nicht belegt:** Der
  Wochencheck ist nie gelaufen, die Korrektur greift erst dann. Prüft Phase 4.
  Der ursprüngliche Befund lautete:
- ~~**Der Wochencheck meldet die eigene Änderungsnotiz als Befund (20.08.2026).**~~
  Wer in `ergebnisse/` notiert, *welches* verbotene Wort gestrichen wurde,
  schreibt genau dieses Wort dorthin, wo Prüfpunkt 1 sagt: „immer ein Befund".
  Entweder nimmt `core/waechter/wochencheck.md` Änderungsnotizen aus, oder die
  Vorlagen schreiben vor, dass eine Notiz das Wort nicht nennt, sondern aufs
  Profil verweist.
- **Der Zwischenstand kennt nur ganze Schritte (20.08.2026).** Ein Schritt der
  Phase 3 kann fünf Dateien umfassen; bricht es mittendrin ab, sagt der Stand
  „Schritt hat noch nicht begonnen". Im Test hat die frische Sitzung drei
  bereits geprüfte Dateien noch einmal mitgeprüft — Kosten: ein zweiter Blick,
  kein Schaden, die Bewertung hat deshalb nicht abgewertet. Genauer wäre, auch
  die einzelne Datei innerhalb eines Schrittes abzuhaken.
- **Erledigt (20.08.2026): Die bedingte Zusatzfrage hat eine dritte Bedingung.**
  Sie wird nur noch gestellt, wenn der Nutzer **nicht** angekündigt hat, dass
  Preismaterial nachkommt. Angekündigtes Material kommt in STATUS unter „Was der
  Nutzer noch nachliefern wollte"; der Wochencheck erinnert später einmal daran.
  Geändert in `core/interview/fragen.md` und `core/interview/mapping.md`, samt
  Checklistenpunkt. **Belegt** im dritten Abbruch-Durchlauf: Auf „Preisliste hab
  ich, die leg ich gleich rein" folgte keine Frage mehr, sondern ein Vermerk.
  Der ursprüngliche Befund lautete:
- ~~**Die bedingte Zusatzfrage zum Preis greift zu mechanisch (20.08.2026).**~~ Sie
  wurde gestellt, weil `meine-unterlagen/preise/` leer war — obwohl der Nutzer
  eine Nachricht zuvor gesagt hatte: „Preisliste hab ich, die leg ich gleich
  rein." Kein Regelbruch, aber eine vermeidbare Frage. Betrifft
  `core/interview/mapping.md` und `core/interview/fragen.md`.
- **Wortlaut-Nachzug in `angebots-schreiber` — bewusst zurückgestellt
  (Entscheidung 20.08.2026).** Ein Kommentar dort sagt, der Hausstil komme „zur
  Installationszeit" aus `{{tonalitaet}}`, `{{anrede}}` und `{{stilbeispiele}}`.
  Seit Baustein 1 stimmt das nicht mehr — richtig ist: beim Lesen. **Das
  Verhalten ändert sich dadurch nicht**, der Satz ist trotzdem falsch. Er wird
  **nicht jetzt** behoben, weil eine Skill-Änderung die fünf Testfälle dieses
  Skills neu laufen ließe (Arbeitsregel 19.08.2026) — für einen Kommentar, der
  nichts steuert, ist das der falsche Preis. **Er gehört in den
  Prüfdurchgang vor der Beta** (eigener Abschnitt unten): Dort werden mehrere
  Wortlaut-Korrekturen in **einem** Zug gemacht und **ein** Nachlauf dafür
  bezahlt, statt einer je Satz.
- **Erledigt (20.08.2026): `START.md` erklärt `CLAUDE.md`.** Eine Zeile in
  `START.vorlage.md`, dazu ein mechanischer Prüfpunkt in der Checkliste der
  Installer-Phase 3 („`START.md` erklärt alle sechs Einträge"). **Belegt** im
  dritten Abbruch-Durchlauf an der erzeugten Datei. **Punkt 4 der Definition of
  Done ist damit erfüllt.** **Zu prüfen bleibt** die Nebenfrage, ob die
  Gedächtnisdatei auch aus einem versteckten Ordner geladen würde — für Punkt 4
  ist das nicht mehr nötig. Der ursprüngliche Befund lautete:
- ~~**`CLAUDE.md` liegt sichtbar im Wurzelordner — und ist NICHT aufgefangen.**~~
  Hier stand bis zum 20.08.2026, das sei „über `START.md` aufgefangen, das
  `system/` und die Datei in einer Zeile abtut". **Das war falsch.** Mechanisch
  geprüft: `START.vorlage.md` erwähnt `CLAUDE.md` mit keinem Wort, und die im
  Abbruch-Test erzeugte `START.md` auch nicht. `system/` wird erklärt, die
  Gedächtnisdatei nicht. Damit ist Punkt 4 der Definition of Done verletzt.
  Behebung: eine Zeile in `START.vorlage.md`. Sie zieht einen neuen
  Phase-3-Durchlauf nach sich, deshalb hier notiert statt nebenbei erledigt.
  **Zu prüfen bleibt** außerdem, ob Claude Code die Datei auch aus einem
  versteckten Ordner lädt — dann verschwindet sie ganz.
- **Erledigt (20.08.2026): Der Wächter existiert.** `core/waechter/wochencheck.md`
  liefert vier feste Prüfpunkte; Installer-Phase 5 baut ihn nicht mehr, sondern
  macht ihn bekannt. Abschnitt „Baustein 3“ oben, Begründung in
  `docs/entscheidungen.md`. **Belegt** im wiederholten Fall 5: kein erfundener
  Wächter mehr. **Nicht** belegt: dass der Check etwas findet — er ist nie
  gelaufen, das prüft Phase 4.
- **Erledigt (21.08.2026): Phase 2 schreibt den Stand erst nach der Antwort — die
  gestellte Frage geht verloren.** Eiserne Regel 3 verlangt für Phase 2 „nach
  **jeder Antwort**". Eine Frage, die auf dem Bildschirm steht und noch nicht
  beantwortet ist, hat damit keinen Platz im Stand — die frische Sitzung stellt
  sie ein zweites Mal. **Das ist die Ursache der einen Abweichung im dritten
  Abbruch-Durchlauf** (Fall 2). Bitter: `STATUS.vorlage.md` macht als
  Musterformulierung ausgerechnet den feineren Fall vor („Frage 7 ist gestellt
  und noch nicht beantwortet"), den die Regel so nie erzeugt. Behebung: eine
  Zeile in Regel 3. Zieht einen neuen Phase-2-Durchlauf nach sich.
  **Behoben am 21.08.2026** an drei Stellen im INSTALLER (Regel 3, Phase 2
  Schritt 2, Checkliste Phase 2); die Vorlage blieb unverändert. Fall 2 danach
  neu gelaufen: **bestanden**, alle sieben Prüfpunkte — vierter Durchlauf in
  `docs/abbruch-test-phase3.md`.
- **Erledigt (21.08.2026): Phase 4 hat zwischen Entwurf und „Passt das?" keinen
  Zwischenstand.** Bricht es dort ab, ist das fertige Angebot weg — dieselbe
  Lücke, die Phase 3 schon geschlossen bekommen hat. `INSTALLER.md` nennt STATUS
  für Phase 4 erst als Schritt 6.
  **Behoben:** Das Ablegen ist vor die Rückfrage gezogen; der Stand hält fest,
  dass „Passt das?" gestellt und unbeantwortet ist. **Belegt** durch einen
  sechsten Abbruchpunkt — Abbruch genau in diesem Fenster, das Ergebnis lag auf
  der Platte, die frische Sitzung setzte fort ohne eine zweite Aufgabe zu
  verlangen (`docs/abbruch-test-phase3.md`).
- **Neu (20.08.2026): Die Beispiele in `core/interview/fragen.md` sind die Daten
  der Testperson.** Frage 7 zeigt die Signatur samt Telefonnummer aus
  `evals/testprofil.md` als „Beispiel", Frage 10 deren Erfolgsmoment wörtlich.
  Beim echten Käufer ist das nur ein fremder Name; im Prüfstand kollidiert es und
  macht jede Mitschrift schief. Beispiele sollten eine andere Person nennen als
  das Testprofil.
- **Neu (20.08.2026): Der Installer sichert Antworten in der dritten Person**,
  obwohl `mein-profil.md` den Nutzer durchgängig duzt. Kein Fehler im Inhalt,
  aber die Datei liest sich uneinheitlich.
- **Erledigt (21.08.2026): „Liegt fertig in `ergebnisse/`"** — gesagt über ein
  Angebot, das `Stand: entwurf` ist und eine `[PREIS PRÜFEN]`-Zeile trägt.
  Nichts erfunden, aber der Abschlusssatz verspricht mehr, als dasteht.
  **Behoben** im selben Zug wie der Zwischenstand: Phase 4, Schritt 6 verlangt
  jetzt, das Ergebnis so zu beschreiben, wie es ist — offene Punkte und
  `[PREIS PRÜFEN]` werden benannt. Die frische Sitzung im sechsten
  Abbruchpunkt hat genau das getan.
- **Neu (20.08.2026): Prozess-Schritt 5 des `angebots-schreiber` wird von keinem
  Fall mehr gemessen.** Folge der Kriterienkorrektur an `02-budget-konflikt`:
  Wer korrekt nachfragt, schreibt kein Angebot, und ohne Angebot gibt es keinen
  Block B, in dem der Budget-Konflikt stünde. Vorschlag im Testfall selbst: ein
  **zweiter Zug** wie bei `ketten/02`.
- **Neu (20.08.2026): Vier Testfall-Befunde aus dem Nachlauf, alle gemeldet,
  keiner angefasst** (`docs/nachlauf-phase3.md`): der Firmenname in
  `02-budget-konflikt` (Folge der Maskierung `[kunde]`, alle drei Bewerter
  stolperten an derselben Stelle), zwei Punkte in `ketten/01` (die
  Bestehensbedingung verlangt einen Block A, den der Fall zugleich verbietet;
  die Zusatzfrage zum Zielbild ist ungeregelt) und der Widerspruch in
  `follow-up-generator/02` (die Muss-Zeile „eine Woche ist knapp" steht gegen die
  Zeitregel des Skills). Keiner ändert ein Urteil; alle brauchen eine
  Entscheidung.
- Digistore24/CopeCart-Konto beantragen (Freischaltung dauert Tage)
- Produktname + Domain final
- START_HIER später zusätzlich als PDF (Markdown reicht für Beta)
- **Testfälle sind konstruiert, nicht aus der Praxis.** Die drei Fälle zu
  `angebots-schreiber` sind ehrlich hart, aber erfunden. Vor Beta gegen
  anonymisierte Realfälle tauschen — bis dahin taugen sie zur Entwicklung,
  nicht als Erfolgsquote nach außen.
- **Erledigt (20.08.2026): `angebots-schreiber/02-budget-konflikt` entschieden.**
  Das Kriterium war falsch, nicht der Skill: Eine Rückfrage nach dem
  Empfänger-Verhältnis ist bestanden, ein gesetzter Wert durchgefallen. Testfall
  mit Änderungsvermerk korrigiert, danach 3 von 3. **Blockiert Phase 3 nicht
  mehr.** Der ursprüngliche Befund lautete:
- ~~**Testfall-Befund `angebots-schreiber/02-budget-konflikt` — Entscheidung
  steht aus (20.08.2026).**~~ Der Fall verlangt ein Angebot, obwohl seine Eingabe
  den sechsten Pflicht-Fakt (Empfänger-Verhältnis) nicht hergibt. Er belohnt
  damit das Raten und bestraft das regelkonforme Nachfragen. Zwei von drei
  Läufen fielen durch, weil sie sich an den Skill hielten. Vorschlag und
  Begründung im Abschnitt „Nachlauf Phase 3" oben. **Blockiert den Abschluss
  von Phase 3.**
- **Erledigt (25.08.2026): Befund `outreach-personalisierer`: falscher Platzhalter (20.08.2026).** An
  einer Stelle steht `{{firma}}`, wo die Firma des **Empfängers** gemeint ist —
  eingesetzt stünde dort die eigene. Aufgefallen beim Abbruch-Test. Nicht
  behoben: Nach der Arbeitsregel vom 19.08.2026 zieht die Änderung die drei
  Testfälle dieses Skills nach sich. **Vorgemerkt für den Prüfdurchgang vor der
  Beta** (Abschnitt unten) — dort mit Vorrang, weil er als einziger der
  gesammelten Punkte das Verhalten wirklich ändert.
  **Behoben am 25.08.2026** — und der Nachlauf hat einen schwereren Befund
  hochgespült: Fall 01 fiel zwei von drei Läufen durch, weil der eigene
  Standort des Nutzers auf den Empfänger übertragen wurde. Schritt 3 des Skills
  deckt jetzt auch Angaben über den Empfänger ab; danach 3 von 3.
  Testfall `02` musste dafür neu gefasst werden. Alles in
  `docs/nachlauf-outreach.md`.
- **Erledigt (20.08.2026): Prinzip 1 beim Kunden repariert.** Platzhalter
  werden beim Einrichten nicht mehr ersetzt, sondern beim Lesen aufgelöst —
  Profilwissen steht beim Kunden wieder genau einmal, wie im Repo. Einzelheiten
  im Abschnitt „Baustein 1“ oben, Begründung in `docs/entscheidungen.md`.
  **Belegt** im wiederholten Abbruch-Test (Fälle 3 bis 5, 3 von 3).
- **Erledigt (19.08.2026, am 28.08. nachgetragen): `einwand-sparring/03`.** Der
  Absatz „Bewertungslage" stand im Eingabeteil und lieferte dem erzeugenden Lauf
  die fertige Analyse mit. **Bereits am 19.08. in den Kriterienteil verschoben**,
  mit Änderungsvermerk im Fall und eigenem Commit — diese Liste führte ihn nur
  weiter als offen. Ein Befund an zwei Orten: im Fall und hier. Wer nur einen
  pflegt, erzeugt Arbeit.
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

## Prüfdurchgang vor der Beta — gesammelte Wortlaut-Korrekturen

**Warum es diesen Abschnitt gibt.** Die Arbeitsregel vom 19.08.2026 macht jede
Skill-Änderung teuer: Danach laufen alle Fälle dieses Skills neu, dreimal. Für
einen falschen Kommentar, der **nichts steuert**, ist das der falsche Preis —
für zehn falsche Kommentare, in einem Zug korrigiert, ist es der richtige.
Deshalb werden Wortlaut-Befunde ab jetzt hier gesammelt und **gemeinsam** vor
der Beta abgearbeitet: ein Durchgang, ein Nachlauf.

**Was drinliegt (Stand 20.08.2026):**

| Fundstelle | Was falsch ist | Zieht nach sich |
|---|---|---|
| `core/skills/vertrieb/angebots-schreiber.md` | Der Hausstil komme „zur Installationszeit" aus `{{tonalitaet}}`, `{{anrede}}`, `{{stilbeispiele}}` — richtig ist: beim Lesen (seit Baustein 1) | 5 Fälle |
| `core/skills/vertrieb/outreach-personalisierer.md` | `{{firma}}` steht dort, wo die Firma des **Empfängers** gemeint ist — eingesetzt stünde dort die eigene | 3 Fälle |
| `core/interview/fragen.md` | Die Beispiele bei Frage 7 und 10 sind die Daten der Testperson | kein Skill-Fall, aber ein Abbruch-Durchlauf |
| `adapter-claude/INSTALLER.md`, Phase 5 | „Liegt fertig in `ergebnisse/`" über ein Angebot im Entwurfsstand | ein Abbruch-Durchlauf |

**Regel für diesen Abschnitt:** Was hier landet, muss **verhaltensneutral**
sein — ein Satz, der falsch ist, ohne dass ein Lauf sich anders verhält. Alles
andere gehört sofort behoben, nicht gesammelt. Der
`outreach-personalisierer`-Befund ist der Grenzfall: Er **ist** verhaltensrelevant
und steht hier nur, weil er ohnehin drei Fälle nach sich zieht — er hat unter
den vieren Vorrang.

## Nächster Schritt — Stand 20.08.2026, abends

> **Überholt.** Den aktuellen Stand hält der Abschnitt „Nächster Schritt —
> Stand 21.08.2026" am Ende dieser Datei. Dieser Abschnitt bleibt als Verlauf
> stehen.

**Erledigt an diesem Tag, in dieser Reihenfolge:**

1. Prinzip-1-Bruch beim Kunden, Zwischenstand in Installer-Phase 3,
   Wächter-Vorlage — gebaut **und** im zweiten Abbruch-Durchlauf belegt (3 von 3).
2. **Testfall `02-budget-konflikt` entschieden und korrigiert** — 3 von 3.
3. **Sechs Textbefunde an Installer und Vorlagen** in einem Durchgang behoben.
4. **Die fünf offenen Nachlauf-Fälle gelaufen** — alle bestanden. Ein Befund
   lag im Skill, ist dort behoben, danach alle vier Fälle dieses Skills neu.
5. **Abbruch-Test, Fälle 2 bis 5, ein drittes Mal gelaufen** — drei bestanden,
   einer abweichend.

**Was für die Definition of Done Phase 3 noch fehlt:**

1. **Durchlauf auf einem fremden Rechner**, gestoppt, mit einer Testperson ohne
   Vorkenntnisse. **Der einzige Punkt, zu dem es bis heute keine Messung gibt.**
2. ~~**Eine Entscheidung zu Fall 2 des Abbruch-Tests.**~~ **Gefallen am
   21.08.2026, Befund behoben und neu belegt.** Nach der Skala des Tests
   ist er bestanden — nach dem Wortlaut der Anforderung („der Käufer soll nie
   merken, dass eine Sitzung zu Ende geht") merkt er es dort. Behebung ist eine
   Zeile in eiserner Regel 3 und kostet einen neuen Phase-2-Durchlauf. **Ob das
   Phase 3 blockiert oder in die Beta darf, ist eine Entscheidung, keine
   Messung.**

**Mehr ist es nicht.** Punkt 4 der Definition of Done ist seit heute erfüllt,
Punkt 2 belegt, Punkt 3 unverändert formal erfüllt.

**Was übrig bleibt, ohne Phase 3 zu blockieren** — vollständig unter „Offene
Punkte" oben, hier nur die Überschriften:

- **Sieben Befunde, keiner behoben:** fünf aus dem dritten Abbruch-Durchlauf
  (davon zwei Wortlaut, siehe Prüfdurchgang), der Zwischenstand, der nur ganze
  Schritte kennt, und die Deckungslücke beim Budget-Konflikt.
- **Vier Testfall-Befunde aus dem Nachlauf**, alle gemeldet, alle unangetastet,
  keiner urteilsrelevant — aber jeder braucht eine Entscheidung.
- **Der Wochencheck ist nie gelaufen.** Gebaut, bekannt gemacht, nicht mehr
  erfunden — aber nicht gemessen. Die Korrektur an Prüfpunkt 1 ist damit
  eingebaut und ungeprüft. Prüft Phase 4.
- **`notfall/` ist nur formal geprüft.** Die sechs Dateien existieren; dass sie
  wirken, weiß erst die Beta.
- **Die Testfälle sind konstruiert.** Vor der Beta gegen anonymisierte
  Realfälle tauschen.

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

## Nächster Schritt — Stand 21.08.2026

> **Überholt.** Den aktuellen Stand hält der Abschnitt „Nächster Schritt —
> Stand 28.08.2026" am Ende dieser Datei.

Dieser Abschnitt hält den Stand. Alle „Nächster Schritt"-Abschnitte darüber
sind Verlauf.

**Erledigt an diesem Tag:**

1. **AEF-Governance eingerichtet** — die Weiterentwicklung läuft ab jetzt im
   Repository `schnittbuild-stack/Autopilot-Kit-Pro` unter Work Orders,
   unabhängigem Review und geschütztem `main`.
2. **Riss aus Abbruch-Test Fall 2 behoben und neu belegt.** Eiserne Regel 3
   hält eine gestellte, unbeantwortete Frage jetzt im Stand fest. Fall 2 danach
   neu gelaufen: **bestanden**, alle sieben Prüfpunkte. Vierter Durchlauf in
   `docs/abbruch-test-phase3.md`, Entscheidung in `docs/entscheidungen.md`.

**Ebenfalls am 21.08.2026:** Der erste Durchlauf mit dem gebauten Kunden-ZIP
(Autorendurchlauf, rund 25 Minuten) hat einen **Fehler in der Gedächtnisdatei**
gefunden — der Text der erledigten Aufgabe stand fünfmal in `system/STATUS.md`,
viermal mitten in fremden Sätzen. Ursache, Behebung an vier Stellen und der
Nachweis stehen in `docs/durchlauf-autor.md`. Der Abbruch-Test hätte das nie
gefunden: Der Schaden entsteht am **Ende** von Phase 4, nicht während der Phasen.

**Was für die Definition of Done Phase 3 noch fehlt — genau ein Punkt:**

**Kompletter Durchlauf auf einem frischen, fremden Rechner unter 30 Minuten,
mit einer Testperson ohne Vorkenntnisse.** Nie gemessen. Der einzige Punkt, den
keine Sitzung simulieren kann: Er braucht einen echten Menschen an einem echten
fremden Rechner. Punkte 2, 3 und 4 der Definition of Done sind erfüllt.

**Was übrig bleibt, ohne Phase 3 zu blockieren:** unverändert unter „Offene
Punkte" oben — die Testfall-Befunde aus dem Nachlauf, der nie gelaufene
Wochencheck, die Wortlaut-Befunde aus dem dritten Abbruch-Durchlauf.

## Nächster Schritt — Stand 28.08.2026

Dieser Abschnitt hält den Stand. Alle „Nächster Schritt"-Abschnitte darüber
sind Verlauf.

**Seit dem 21.08. erledigt:**

1. **Phase 4 vollständig gebaut** — Watchdog-Testlauf und Reparatur-Flow, fünf
   Ketten-Testfälle statt zwei, kundeneigene Prüffälle, Ketten-Rotation.
   Einzelheiten in `docs/watchdog-test.md`, `docs/ketten-testfaelle.md`,
   `docs/eigene-testfaelle.md`.
2. **Die Übergabe haltbar gemacht** (27.08.). Der Notizblock „für dich, nicht
   für den Kunden" überlebt jetzt die Sitzung, ein abgearbeiteter Vorgang wird
   vermerkt statt gelöscht, und die Fortsetzung wird angeboten statt ungefragt
   gestartet. Dazu der bis dahin fehlende Vertrag
   `account-recherche → outreach-personalisierer`. Bericht:
   `docs/uebergabe-haltbar.md`.

**Was offen ist:**

1. **Der 30-Minuten-Durchlauf** mit einer Testperson ohne Vorkenntnisse. Der
   einzige Punkt, der Phase 3 noch blockiert — und der einzige, den keine
   Sitzung ersetzen kann.
2. **Drei kundeneigene Testfälle, von einem Testkäufer bestätigt** — die zweite
   Hälfte der Definition of Done von Phase 4. Braucht denselben Menschen.
3. **Die kopflose Auswertung war blind für alles außer der letzten Nachricht.**
   `claude -p` gibt nur diese aus; ein Lauf, der die Arbeit tut und danach den
   Zwischenstand aufräumt, wurde als abweichend gezählt. Ein Lauf von neun am
   28.08. Der Fehler geht immer in dieselbe Richtung — bestanden wird zu
   abweichend, nie umgekehrt. **Ab jetzt** wird über alle Nachrichten
   ausgewertet; ältere Berichte werden nicht rückwirkend umgeschrieben.

Dazu die acht Befunde aus dem Rückstand oben, von denen vier eine Entscheidung
des Auftraggebers brauchen.

**Seit dem 28.08. zusätzlich erledigt:**

3. **`ketten/01` untersucht** — der Befund reproduziert nicht (zwölf Läufe,
   vier Anordnungen). Der Wächter sichert seinen Beleg jetzt nach
   `system/befunde/`; die Doppeldeutigkeit im Vertrag ist aufgelöst.
   `docs/ketten01-untersuchung.md`.
4. **Die zwei unbelegten Versprechen sind belegt** (28.08.). Der
   Übergabeblock überlebt die Sitzung: 18 Tage Abstand, frischer Prozess ohne
   Vorwissen, Aufhänger nur in Block B — **3 von 3 auf vier scharf gestellten
   Regeln**, plus Regel 5 in ihrer Fehl-Form beiläufig belegt. **Offen bleibt
   Regel 5 mit gefülltem `Preisstand`** — ein leeres Feld kann nicht
   durchsickern. Und der `outreach`-Vertrag hat seinen Ketten-Testfall:
   `ketten/06`, zweistufig, **3 von 3**. Damit sind es sechs Ketten-Fälle.
   Dabei vom Review gefunden: Der Wächter behauptete, der
   `outreach-personalisierer` komme in keiner Kette vor — durch `ketten/06`
   falsch geworden, und die Datei widersprach sich selbst. Berichtigt.
   `docs/berichte/unbelegte-versprechen.md`.

5. **Zustandsprotokoll und Berichte sind gewöhnliche Pfade.**
   `docs/STATUS-BAU.md`, `docs/entscheidungen.md` und `docs/berichte/**` stehen
   in `ordinary_paths`. Damit sperrt die von uns selbst verlangte Pflege nicht
   mehr den ordentlichen Merge. **Berichte ab dem 28.08. liegen in
   `docs/berichte/`**, die 14 älteren bleiben in `docs/` — siehe
   `docs/berichte/README.md`.

   **Was das noch nicht bewirkt, ausdrücklich:** `.aef/onboarding-state.json`
   steht auf `activation_status: inactive`, und `aef_merge.py:189` verlangt
   `configuration_verified`. **Die ordentliche Spur ist damit heute für jeden
   Pull Request zu**, unabhängig von den Pfaden. Gemeldet vom Review zu WO-014;
   meine Formulierung „ab dem nächsten PR greift die Änderung" ging zu weit.
   Die Pfad-Sperre ist beseitigt, die Aktivierungssperre nicht — das ist
   dieselbe Sache wie der Org-Zwang und braucht einen eigenen Auftrag.

6. **Vier Testfall-Entscheidungen umgesetzt** (28.08.). Die `[kunde]`-Maskierung
   ist raus — die fünf Angebots-Fälle tragen lesbare Firmennamen, wie jeder
   andere Fall im Repo. Neu: `06-fehlender-absender` hält die Entscheidung fest,
   dass ohne Empfänger kein Angebot entsteht. `follow-up-generator/02` verlangt
   nicht mehr, dass der Helfer seinen eigenen Zeitpunkt für zu früh erklärt.
   `ketten/01` ist zweistufig und erfüllt seine volle Bedingung erstmals.
   Acht Fälle je dreimal nachgelaufen: siebenmal 3 von 3, einmal 2 von 3 (siehe
   Punkt 7 dieser Liste). `docs/berichte/testfall-widersprueche.md`.

7. **Nachlese (28.08.).** `angebots-schreiber/01` bekam das Bestandsverhältnis
   ausdrücklich in die Eingabe — **3 von 3** statt 2 von 3. Denselben Griff
   brauchte mein eigener neuer Fall 06, der die gerügte Konstruktion selbst
   benutzte; gefunden hat das der Review, nicht ich. Die `[kunde]`-Maskierung
   ist jetzt **restlos** raus, auch aus `ausschreibungs-analyse/03`,
   `ketten/02` und `follow-up-generator/01`. Fünf Fälle nachgelaufen, fünfmal
   3 von 3. `docs/berichte/testfall-widersprueche.md`.

8. **Drei der vier Zeilen des `outreach`-Vertrags sind belegt** (28.08.). Die letzten
   zwei Zeilen seiner Tabelle — leere Belegliste und ganz fehlendes Listenfeld —
   haben mit `ketten/07` und `ketten/08` eigene Fälle, beide **3 von 3**. Damit
   acht Ketten-Fälle. **Dabei ein Fehler in meinem eigenen neuen Kriterium:**
   `ketten/08` verlangte wörtlich den Feldnamen `Nicht gefunden`, während alle
   drei Läufe ihn regelkonform in Alltagssprache umschrieben — dieselbe Bauart
   wie die vier Befunde vom selben Tag. Vor dem Merge korrigiert.
   **Die vierte Tabellenzeile bleibt ohne eigenen Fall** und braucht auch
   keinen: Sie beschreibt den Fall, in dem gar keine Recherche vorliegt, der
   Vertrag also nicht greift. Ich hatte hier und im Vertrag „vollständig
   belegt" geschrieben — falsch, dreimal vom Review gemeldet, am 28.08.
   berichtigt. `docs/berichte/unbelegte-versprechen.md`.

9. **Gegenprobe auf veraltete Bestandsaussagen** (28.08.). Vier ausgelieferte
   Skill-Dateien **und zwei Verträge** nannten Testfälle und Ketten namentlich
   und waren dadurch veraltet — der `outreach-personalisierer` stand in drei
   Ketten und wusste es selbst nicht. **Die Zahlen sind nicht nachgezogen,
   sondern durch Verweise auf die Quelle ersetzt** worden; eine berichtigte
   Liste wäre mit dem nächsten Ketten-Fall wieder falsch. Je ein Fall der vier
   Helfer dreimal nachgelaufen, viermal 3 von 3. **Die zwei Verträge fand
   erst der Review** — mein Sweep suchte nach Zahlwörtern und übersah bloße
   Pfad-Aufzählungen.
   `docs/berichte/zahlen-gegenprobe.md`.

10. **Drei Verstöße gegen Bauprinzip 4 behoben** (31.08.). `core/` und
    `notfall/` nannten an drei Stellen `CLAUDE.md` oder einen
    `adapter-claude/`-Pfad. Aufgefallen bei der Frage, ob das Kit für Codex
    bereit ist. Behoben nicht durch Aufzählung beider Plattformen, sondern
    durch Verweis auf die Quelle, die den Namen kennt. Prüfpunkt 4 des
    Wochenchecks dreimal nachgelaufen: 3 von 3.
    `docs/berichte/prinzip-vier.md`.

11. **Zweiter Adapter: das Kit läuft auch mit ChatGPT/Codex** (31.08.).
    `adapter-codex` mit eigenem Installer und vier Vorlagen, Gedächtnisdatei
    `AGENTS.md`. **Vorher gemessen statt geraten:** Der Auftraggeber hat auf
    seinem Rechner belegt, dass Codex eine `AGENTS.md` von selbst liest —
    damit ließ sich der Installer fast eins zu eins übersetzen, nur der
    Software-Check wich einem Zugriffs-Check. `START_HIER.md` gabelt sich in
    zwei Wege. **Belegt:** Bei zwei Adaptern im Ordner greift der Agent 3 von
    3 zum richtigen. **Ungeprüft:** Der Codex-Installer ist nie gelaufen — ich
    kann Codex von hier nicht starten. **Offen:** `adapter-codex/**` und
    `START_HIER.md` stehen in keinem `ordinary_paths`-Muster — heute
    folgenlos, weil die Spur ohnehin zu ist, aber ein eigener Auftrag,
    weil die Korrektur in `governance/policy.json` liegt.
    `docs/berichte/adapter-codex.md`.

**Zum Weg dieser Änderung:** Sie lag als WO-011 schon einmal zum Review vor und
ist **zweimal beanstandet** worden — beim zweiten Mal, weil die neue Regel
„nichts wird überschrieben" der Korrekturschleife aus `INSTALLER.md` widersprach
und weil ein Prüfstand-Bericht nach echten Kundendaten klang. Nach der Regel des
Abnahme-Tors („eine Korrektur, ein erneuter Review, dann anhalten und neu
planen") ist der Versuch abgebrochen und als **WO-012 neu geplant** worden,
auf einem frischen Branch von `main`. Der gescheiterte Versuch bleibt als
geschlossener Pull Request sichtbar.
