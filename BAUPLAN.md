# BAUPLAN — Arbeitsanweisung für Claude-Code-Sessions

Du arbeitest am Autopilot Kit: einem Download-Produkt (299/499 €), mit dem sich das
LLM eines Käufers nach einer KI-Schulung selbst zu einem persönlichen Assistenten-Setup
konfiguriert. Zielgruppe: Menschen ohne Technik-Hintergrund, die eine KI-Schulung
gemacht haben und nicht ins Tun kommen.

Lies zuerst `CLAUDE.md` (Regeln) und `docs/STATUS-BAU.md` (aktueller Stand).
Arbeite die Phasen in Reihenfolge ab. Nach jedem erledigten Punkt: STATUS-BAU.md
aktualisieren, committen.

---

## Phase 2 — Vertriebs-Skills & Verträge (Tag 2–5)

Ziel: 10 Agenten des Vertriebspakets als Skill-Dateien in `core/skills/vertrieb/`,
jeder zu 80 % fertig — die letzten 20 % füllt später das Installer-Interview über
Platzhalter.

Reihenfolge (wichtig):
1. **Agent Nr. 1 zuerst komplett**: `angebots-schreiber.md` nach
   `_TEMPLATE_SKILL.md`, mit 5 echten Beispielen und 3 Testfällen. Er ist der
   Qualitätsmaßstab für alle anderen.
2. **Kette definieren**: Welche Agenten übergeben aneinander?
   (Vorschlag: account-recherche → angebots-schreiber → follow-up-generator.)
3. **Verträge VOR den restlichen Agenten**: für jede Schnittstelle eine Datei in
   `core/vertraege/` nach `_TEMPLATE_VERTRAG.md`.
4. Agenten 2–10 bauen. Platzhalter-Konvention strikt: `{{firma}}`, `{{tonalitaet}}`,
   `{{signatur}}`, `{{verbote}}` — vollständige Liste in
   `core/interview/mapping.md`, dort JEDE neue Platzhalter-Variable registrieren.
5. Pro Agent 3 Testfälle in `core/testfaelle/` nach `_TEMPLATE_TESTFALL.md`.

Definition of Done: Alle 10 Skills laufen einzeln gegen ihre Testfälle; die
Hauptkette läuft einmal Ende-zu-Ende durch.

## Phase 3 — Installer (Tag 4–7)

Ziel: `adapter-claude/INSTALLER.md` von Rohbau auf fertig.

**Warum diese Phase über das Produkt entscheidet.** Der Käufer hat keine
Technikkenntnisse, kein Terminal-Wissen und keine Admin-Rechte auf seinem
Firmenlaptop. Er zahlt 299 €, entpackt ein ZIP und erwartet, dass seine KI den
Rest macht. **Alles, was er erklären oder verstehen muss, ist ein Fehler im
Produkt — nicht bei ihm.** Die zehn Skills aus Phase 2 sind geprüft; ob sie je
jemand benutzt, entscheidet sich hier.

---

### Die vier Pflichtanforderungen

Alle vier sind Bedingung für „Phase 3 fertig". Keine ist optional, keine ist
verhandelbar.

#### Anforderung 1 — Sitzungswechsel unsichtbar

Ein Sitzungswechsel ist unser Problem, nicht das des Käufers. Er hat kein Wort
für „Kontextfenster" und soll auch keines lernen müssen. Drei Bestandteile,
alle drei Pflicht:

1. **Ein Wort genügt.** Fortsetzen heißt **„weiter"** — mehr nicht. Nie ein
   Übergabeprompt, den der Nutzer formulieren, kopieren oder verstehen muss.
   Der Zustand kommt aus `STATUS.md`, nicht aus dem, was der Nutzer erzählt.
   Wenn die Fortsetzung davon abhängt, dass der Nutzer richtig zusammenfasst,
   ist sie falsch gebaut (Prinzip 2: Zustand auf der Platte).
2. **Der Assistent bietet den Wechsel von sich aus an** — in Alltagssprache,
   nach abgeschlossenen Phasen und nach langen Aufgaben, mit dem Hinweis
   **„dein Stand ist gesichert"**. Der Nutzer soll nicht merken müssen, dass
   etwas voll läuft; er wird gefragt, ob er frisch weitermachen will.
3. **Der Installer bringt es bei und legt es ab.** In Installer-Phase 5 ein
   Satz an den Nutzer, wie er weitermacht, wenn er später wiederkommt oder
   etwas abbricht. Dieselbe Anleitung zusätzlich in `notfall/`, damit sie
   auffindbar ist, wenn die Sitzung schon weg ist — genau dann kann er nicht
   mehr nachfragen.

#### Anforderung 2 — `meine-unterlagen/` als dritte Wissensquelle

Der Kundenbaum bekommt einen Ordner, in den der Käufer sein eigenes Material
legt: Preisliste oder Kalkulationsgrundlage, alte Angebote,
Leistungsbeschreibungen, AGB, E-Mails, die er gut findet. **Alles optional.**

Damit hat der Assistent genau drei Quellen, und jede hat ihre eigene Rolle:

| Quelle | Was darin steht | Wer sie füllt |
|---|---|---|
| `mein-profil.md` | Dauerwissen über die Person: Rolle, Ton, Anrede, Signatur, Verbote | Installer-Phase 2 oder „Einstellungen ändern" |
| die jeweilige Aufgabe | Anlasswissen: diese eine Anfrage, dieses eine Protokoll | der Nutzer im Moment der Aufgabe |
| `meine-unterlagen/` | Firmenwissen: Preise, Leistungen, Rechtstexte, Stilmaterial | der Nutzer, jederzeit, per Datei hineinlegen |

Regeln:

- Der Installer fragt in **Phase 2** danach — in Alltagssprache, mit dem Nutzen
  in einem Satz („dann muss ich dich nicht jedes Mal nach deinen Preisen
  fragen"). Kein Zwang: Wer nichts hat, sagt „nichts" und kommt weiter.
- **Skills lesen daraus, statt zu fragen**, wenn Material vorhanden ist.
  Fehlt es, bleibt das bisherige Verhalten unverändert: nachfragen bzw.
  `[PREIS PRÜFEN]`. Kein Skill wird schlechter, weil der Ordner leer ist.
- `{{preisgrundlage}}` und `{{stilbeispiele}}` verweisen künftig auf diesen
  Ordner statt auf eine Interviewantwort (Entscheidung 19.08.2026, siehe
  `docs/entscheidungen.md`).
- **Alles bleibt lokal beim Kunden.** Nichts davon kommt je zu uns zurück.

Aufbau (der Installer legt ihn an, alle Unterordner dürfen leer bleiben):

```
meine-unterlagen/
├── preise/            Preisliste, Kalkulationsgrundlage, Stundensätze
│   ├── archiv/        abgelöste Preisstände — werden nie gelöscht
│   └── kunden/        <name>/ je Kunde: Rahmenvertrag, Rabattstaffel
├── angebote/          frühere Angebote — Aufbau und Formulierung
├── leistungen/        Leistungsbeschreibungen, Standardtexte
├── rechtliches/       AGB, Standardklauseln
└── stilbeispiele/     E-Mails, die der Nutzer gut findet
```

#### Anforderung 3 — Preise sind nicht statisch

Ein veralteter Preis ist so teuer wie ein erfundener, nur unsichtbarer. Drei
Regeln, alle drei Pflicht:

**(a) Ersetzen statt pflegen.** Der Nutzer legt eine neue Preisdatei in
`meine-unterlagen/preise/` — die alte wandert automatisch nach
`preise/archiv/`. Nichts wird gelöscht, nichts wird von Hand gepflegt, keine
Datei muss der Nutzer öffnen. Liegt mehr als eine gültige Preisdatei da,
räumt der Assistent auf, bevor er rechnet, und sagt in einem Satz, was er
weggelegt hat.

**(b) Gültigkeit wird geprüft.** Jede Preisdatei trägt einen `Stand:` oder ein
`gültig bis:`. Ist sie abgelaufen oder älter als die vereinbarte Frist, rechnet
**kein Skill stillschweigend weiter** — er fragt **einmal** nach („deine
Preisliste ist von März, gilt die noch?") und rechnet dann mit der Antwort
weiter. Fehlt das Datum ganz, gilt die Datei als ungeprüft und löst dieselbe
eine Rückfrage aus. **Der verwendete Stand steht immer im internen Block B.**
Standardfrist: 12 Monate, im Profil änderbar.

**(c) Kundenkonditionen haben Vorrang.** `preise/kunden/<name>/` nimmt
Rahmenverträge, Rabattstaffeln und Sonderpreise auf. Rechenreihenfolge, hart:

```
1. Kundenkonditionen (preise/kunden/<name>/)
2. allgemeine Preisliste (preise/)
3. [PREIS PRÜFEN]
```

Niemals schätzen, niemals interpolieren, niemals „branchenüblich". **Block B
nennt, welche Ebene gegriffen hat** — Ebene, Datei und Stand.

#### Anforderung 4 — Aufgeräumte Kundenansicht

Nach der Einrichtung sieht der Käufer **genau vier Dinge**:

```
START.md            Übersicht in Alltagssprache, höchstens zehn Zeilen,
                    jede Zeile ein Beispielsatz, den er wörtlich sagen kann
mein-profil.md      was die KI über ihn weiß
meine-unterlagen/   sein Material (Anforderung 2)
ergebnisse/         was die KI für ihn gemacht hat
```

Alles Technische — Skills, Verträge, Testfälle, STATUS, Watchdog, Installer —
liegt darunter und **wird nie erklärt**. Plattformbedingte Systemdateien
(Gedächtnisdatei der KI) liegen versteckt und zählen nicht zu den vier Dingen.

**Der Nutzer wählt keinen Assistenten aus.** Er sagt in eigenen Worten, was er
braucht („mach mir ein Angebot draus", „was war nochmal in dem Meeting"), die
Zuordnung macht das System. Es gibt keine Liste von Skill-Namen, die er lernen
muss, und keinen Befehl, den er sich merken muss.

Begründung: Ein Käufer, der nach der Einrichtung `core/`, `vertraege/` und
`testfaelle/` sieht, denkt „Entwicklerkram" — genau das entscheidet über den
Wow-Moment, für den er bezahlt hat.

---

### Bauaufgaben (in dieser Reihenfolge)

1. **Kundenbaum und Preisregeln festschreiben** (Anforderungen 2–4), bevor ein
   Skill oder der Installer sie benutzt. Plattformneutral in `core/`.
2. **Installer-Phase 1 (Systemcheck)** — Betriebssystem, Version, Plan
   erkennen; Fehlendes selbst erledigen oder in zwei Klicks erklären. Kein
   Fachbegriff, nirgends.
3. **Installer-Phase 2 (Interview)** — die zehn Fragen aus
   `core/interview/fragen.md` final formulieren, eine pro Nachricht, je mit
   einem Beispiel als Hilfe, gegen `vorlagen/profil.vorlage.md` gemappt. Hier
   auch die Frage nach `meine-unterlagen/`.
4. **Installer-Phase 3 (Selbstbau)** — Skill-Auswahl aus dem Profil (5–6
   passende), Platzhalter füllen, Kunden-`CLAUDE.md` aus `CLAUDE.vorlage.md`
   erzeugen, aufgeräumte Ansicht herstellen, Zuordnung Alltagssatz → Skill.
5. **Installer-Phase 4 (Beweis)** — echte Aufgabe des Käufers anfordern und
   live erledigen. Das ist der Moment, für den er bezahlt hat.
6. **Installer-Phase 5 (Wächter + Übergabe)** — Watchdog installieren, den
   „weiter"-Satz beibringen, mit den drei Sätzen verabschieden, die er morgen
   braucht.
7. **`notfall/` füllen** — die fünf häufigsten Fehlerbilder, dazu die
   „weiter"-Anleitung aus Anforderung 1.
8. **Abbruch-Test** — Session in jeder der fünf Phasen hart beenden.

### Bauregeln (gelten aus Phase 2 unverändert weiter)

- **Regeln gehören in Checkliste und Ausgabeformat, nie nur in den Fließtext.**
  Dort werden sie nachweislich ignoriert (`docs/gegenprobe-bauregel.md`).
- Jede Phase schreibt ihren Stand in `STATUS.md`, **bevor** sie weitergeht.
- Jede Phase bleibt unter 15 Minuten. Dauert etwas länger: aufteilen, STATUS
  schreiben, weitermachen.
- Keine Claude-Spezifika in `core/` (Prinzip 4).
- **Keine allgemeinen Regel-Sweeps über die zehn Skills** (Entscheidung
  19.08.2026). Macht eine Anforderung eine Skill-Änderung nötig, wird nur der
  betroffene Skill geändert — mit Vermerk, welche Testfälle dadurch neu laufen
  müssen.

### Definition of Done Phase 3

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

## Phase 4 — Watchdog & Ketten-Tests (Tag 6–8)

Ziel: Selbsttest-Modul als Skill in `adapter-claude/`.

1. Watchdog-Skill: liest `core/testfaelle/`, führt aus, vergleicht gegen Soll,
   erzeugt einen Bericht in Alltagssprache („3 von 10 Fällen weichen ab —
   soll ich den Fix einspielen?").
2. 5 Ketten-Testfälle Ende-zu-Ende mit Sollergebnissen.
3. Reparatur-Flow: Vorschlag → Nutzer bestätigt → STATUS.md protokolliert.
4. **Kundeneigene Testfälle erzeugen** (Entscheidung 17.08.2026). Der Watchdog
   baut aus dem Material des Käufers — echte Anfragen, verschickte Angebote,
   Mailverläufe, Stilbeispiele aus dem Interview — eigene Testfälle nach
   `_TEMPLATE_TESTFALL.md` und legt sie beim Kunden ab. Sie entstehen dort,
   bleiben dort und kommen nie zu uns zurück. Regeln: nur mit ausdrücklicher
   Zustimmung, Sollkriterien werden dem Nutzer zur Bestätigung vorgelegt (nicht
   vom Modell allein festgelegt), und ein selbstgebauter Fall wird als solcher
   markiert. Das ist die Gegenleistung dafür, dass unsere Praxisfälle das Repo
   nicht verlassen — ohne diesen Punkt prüft der Käufer nur gegen neutrale
   Fremdfälle und nie gegen seinen eigenen Alltag.

Definition of Done: Watchdog erkennt eine absichtlich eingebaute Abweichung in
der Kette und schlägt den korrekten Fix vor — **und** hat aus dem Material eines
Testkäufers mindestens 3 eigene Testfälle erzeugt, die dieser als treffend
bestätigt.

---

Parallel laufende Phasen (nicht in Claude Code): Smoke-Test/Ads (Phase 5) und
Beta (Phase 6) — siehe `docs/fahrplan.html`. Deren Erkenntnisse fließen als
Issues in dieses Repo zurück.
