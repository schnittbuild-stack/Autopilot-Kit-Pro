# Der zweite Adapter: ChatGPT/Codex (31.08.2026)

Der Bauplan sah zwei Plattformen von Anfang an vor. Gebaut war eine. Die
nächste Testperson hat kein Claude-Konto — ohne zweiten Adapter kann der
30-Minuten-Durchlauf nicht stattfinden, und der blockiert Phase 3.

## Was gemessen wurde, bevor gebaut wurde

Ich kann Codex aus dieser Umgebung nicht starten; der Befehl ist nicht
erreichbar, nur die Datenordner sind sichtbar. Geraten habe ich trotzdem
nicht — der Auftraggeber hat auf seinem Rechner gemessen:

| Frage | Antwort | Wie belegt |
|---|---|---|
| Liest Codex eine `AGENTS.md` im Projektordner von selbst? | **ja** | Probe mit einem Losungswort in einer sonst leeren `AGENTS.md`; Codex nannte es auf Anfrage, ohne Hinweis auf die Datei |
| Darf er Dateien anlegen? | **ja, ohne Rückfrage** | „Uneingeschränkter Zugriff" steht in der App am Eingabefeld |
| Wie öffnet man einen Ordner? | **„Projekt auswählen"**, unten am Eingabefeld | Bildschirmfoto der App |

Damit ist die Gedächtnis-Mechanik **dieselbe wie bei Claude**, und der Installer
ließ sich fast eins zu eins übersetzen: 11 Erwähnungen von `CLAUDE.md` wurden zu
`AGENTS.md`, vier Pfade zu `adapter-codex`. Genau **eine** Stelle brauchte
echte Arbeit.

## Die eine Stelle: Schritt 4

Der Claude-Installer prüft dort die Version von Claude Code und bietet ein
Update an. Für die ChatGPT-App ergibt das keinen Sinn — sie aktualisiert sich
selbst, es gibt nichts zu prüfen und nichts nachzuinstallieren.

An seine Stelle tritt ein **Zugriffs-Check**: Steht „Uneingeschränkter Zugriff"
da, geht es wortlos weiter. Muss der Agent um Erlaubnis bitten, sagt er **einmal**
an, was kommt („Ich frage gleich noch ein paar Mal nach, ob ich etwas speichern
darf") — und danach nie wieder. Wer bei jeder Datei erklärt, erzeugt das Gefühl,
dass etwas nicht stimmt.

## Der Einstieg — und warum er neu geschrieben wurde

`START_HIER.md` gabelt sich jetzt in zwei Wege. Der Claude-Weg ist unverändert.
Der Codex-Weg beschreibt, **was auf dem Bildschirm steht**:

> Ganz unten, direkt über dem Eingabefeld, steht **„Projekt auswählen"** —
> klick darauf und wähle diesen Ordner aus.

**Warum so konkret:** Beim Vorbereiten dieser Arbeit habe ich den Auftraggeber
zweimal gebeten, „Codex in einem Ordner zu öffnen". Beide Male kam zurück, dass
er nicht weiß, was gemeint ist — bei jemandem, der dieses Projekt seit zwei
Wochen kennt und Codex schon benutzt hat.

**Das ist der wertvollste Befund dieses Pakets, und er betrifft nicht Codex.**
Der gefährlichste Satz im ganzen Kit ist der erste. Nicht die Skills, nicht der
Wächter — der erste Klick. Eine Anweisung, die eine Bedienoberfläche voraussetzt,
scheitert bei genau der Person, für die das Kit gebaut ist.

## Belegt: Der Agent greift nicht zum falschen Adapter

Das eigentliche Risiko der Gabelung ist, dass im Kundenordner künftig **beide**
Adapter liegen und der Agent den falschen liest — dann legt er beim
Claude-Nutzer eine `AGENTS.md` an, die dort niemand liest.

Geprüft in einem Ordner wie nach dem Entpacken, mit beiden Adaptern, dem Satz
aus `START_HIER.md`, dreimal:

| | Lauf 1 | Lauf 2 | Lauf 3 |
|---|---|---|---|
| `adapter-claude` gelesen | ✓ | ✓ | ✓ |
| `adapter-codex` angefasst | nein | nein | nein |
| `CLAUDE.md` angelegt | ✓ | ✓ | ✓ |
| `AGENTS.md` fälschlich angelegt | nein | nein | nein |

**3 von 3.**

## Neue Sicherung in der Release-Action

Ein unvollständiger Adapter lässt den Nutzer mitten in der Einrichtung stehen —
und das fällt erst beim Kunden auf. Die Action prüft deshalb jetzt für **jeden**
Adapter im Build:

- Installer und die drei gemeinsamen Vorlagen sind da
- genau **eine** Gedächtnis-Vorlage, egal wie sie heißt
- der Adapter wird in `START_HIER.md` genannt — sonst findet ihn niemand

Die Prüfung ist so geschrieben, dass ein dritter Adapter automatisch mitgeprüft
wird, ohne dass jemand eine Liste pflegt. **Dieselbe Regel wie überall seit dem
28.08.: eine Quelle, keine Aufzählung.**

Gegenprobe: Alle drei Fälle wurden künstlich herbeigeführt — fehlende
Gedächtnis-Vorlage, fehlender Installer, Adapter nicht im Einstieg genannt. Die
Sicherung schlägt in allen drei Fällen an.

## Was ausdrücklich ungeprüft bleibt

- **Der Codex-Installer ist nie gelaufen.** Ich kann Codex hier nicht starten.
  Was gemessen und was angenommen ist, steht im Kopf von
  `adapter-codex/INSTALLER.md` — getrennt aufgeführt, damit beim ersten
  Durchlauf klar ist, wo zu suchen ist, wenn es klemmt.
- **Ob `AGENTS.md` auch aus einem Unterordner gefunden wird**, ist offen. Der
  Installer legt sie im Wurzelordner an und der Nutzer wählt genau diesen als
  Projekt — der Fall tritt im Normalbetrieb nicht auf.
- **Ob ein Rechner mit eingeschränktem Zugriff sich anders verhält**, ist offen.
  Schritt 4 fängt es ab, statt es vorauszusetzen.

Der erste echte Beleg ist der 30-Minuten-Durchlauf selbst. Er misst dann
**zwei** Dinge auf einmal — Kit und Adapter —, und das steht hier, damit es
später niemand für ein reines Kit-Ergebnis hält.
