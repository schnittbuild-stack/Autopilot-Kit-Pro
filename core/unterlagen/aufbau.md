# meine-unterlagen/ — die dritte Wissensquelle

<!-- Plattformneutral (Prinzip 4). Quelle der Wahrheit für den Aufbau des
     Unterlagen-Ordners. Skills verweisen hierher, statt den Aufbau selbst zu
     beschreiben. Entscheidung 19.08.2026, siehe docs/entscheidungen.md. -->

## Zweck (ein Satz)

Der Ordner, in den der Nutzer sein eigenes Firmenmaterial legt — Preise,
Angebote, Leistungsbeschreibungen, Rechtstexte, Stilbeispiele — damit die
Assistenten daraus lesen, statt jedes Mal zu fragen.

## Die drei Wissensquellen

Jede Quelle hat genau eine Rolle. Wer die Rollen vermischt, bekommt entweder
veraltetes Dauerwissen oder ein Interview, das nie endet.

| Quelle | Rolle | Wer sie füllt | Wie lange gültig |
|---|---|---|---|
| `mein-profil.md` | **Dauerwissen über die Person**: Rolle, Ton, Anrede, Signatur, Verbote | Interview (Installer-Phase 2) oder „Einstellungen ändern" | bis der Nutzer sie ändert |
| die jeweilige Aufgabe | **Anlasswissen**: diese eine Anfrage, dieses eine Protokoll, diese eine Ausschreibung | der Nutzer im Moment der Aufgabe | nur für diese Aufgabe |
| `meine-unterlagen/` | **Firmenwissen**: Preise, Leistungen, Rechtstexte, Stilmaterial | der Nutzer, jederzeit, per Datei hineinlegen | bis er eine neue Datei hineinlegt (bei Preisen zusätzlich befristet, siehe `preisregeln.md`) |

**Warum Firmenwissen nicht ins Profil gehört:** Eine Preisliste ist ein
Dokument, kein Satz. Als Profilzeile trüge sie weder Stand noch Gültigkeit noch
Kundenkonditionen — es gäbe nichts zu ersetzen und nichts zu prüfen. Als Datei
trägt sie all das.

## Aufbau

```
meine-unterlagen/
├── preise/            Preisliste, Kalkulationsgrundlage, Stundensätze
│   ├── archiv/        abgelöste Preisstände — werden nie gelöscht
│   └── kunden/        <name>/ je Kunde: Rahmenvertrag, Rabattstaffel
├── angebote/          frühere Angebote — Aufbau und Formulierung
├── leistungen/        Leistungsbeschreibungen, Standardtexte
├── rechtliches/       AGB, Standardklauseln, Standard-Zahlungsbedingungen
└── stilbeispiele/     Texte, die der Nutzer gut findet
```

**Jeder Unterordner darf leer bleiben.** Ein leerer Ordner ist kein Fehler und
keine Baustelle — er bedeutet: „danach musst du mich fragen".

## Was wohin gehört und wer es liest

| Ordner | Was hinein gehört | Wer daraus liest | Wofür |
|---|---|---|---|
| `preise/` | Preisliste, Kalkulationsgrundlage, Stunden-/Tagessätze, Pauschalen | `angebots-schreiber` | Preiszeilen rechnen, statt `[PREIS PRÜFEN]` zu setzen |
| `preise/kunden/<name>/` | Rahmenvertrag, Rabattstaffel, Sonderpreise dieses einen Kunden | `angebots-schreiber` | Vorrang vor der allgemeinen Preisliste |
| `preise/archiv/` | abgelöste Preisstände — **automatisch befüllt**, nie von Hand | niemand im Normalfall | Nachvollziehen, was früher galt |
| `angebote/` | frühere Angebote, gern die erfolgreichen | `angebots-schreiber`, `follow-up-generator`, `outreach-personalisierer` | Aufbau und Formulierung, **nicht** die Zahlen |
| `leistungen/` | Leistungsbeschreibungen, Standardtexte, Modulbeschreibungen | `angebots-schreiber`, `ausschreibungs-analyse` | Positionen sauber beschreiben, statt sie zu erfinden |
| `rechtliches/` | AGB, Standardklauseln, Zahlungs- und Stornobedingungen | `angebots-schreiber`, `ausschreibungs-analyse` | Was zugesichert werden darf und was nicht |
| `stilbeispiele/` | Texte, die der Nutzer gut findet — E-Mails, Anschreiben, Absagen | jeder schreibende Skill | Tonfall und Satzbau (`{{stilbeispiele}}`) |

## Regeln für Skills

Diese Regeln gelten für **jeden** Skill, der Unterlagen liest. Sie stehen hier
einmal, damit sie nicht in zehn Dateien auseinanderlaufen.

1. **Lesen statt fragen.** Liegt Material da, das die Frage beantwortet, wird
   es gelesen — nicht gefragt. Eine Frage nach etwas, das in den Unterlagen
   steht, kostet dasselbe Vertrauen wie eine Frage nach etwas, das in der
   Anfrage steht.
2. **Leerer Ordner ändert nichts.** Fehlt das Material, gilt unverändert das
   bisherige Verhalten: nachfragen bzw. `[PREIS PRÜFEN]`. Kein Skill wird
   schlechter, weil der Ordner leer ist, und keiner rät, weil er voll ist.
3. **Material ist Beleg, die Bitte des Nutzers ist keiner.** Was in einer
   Unterlage steht, ist belegt. Was der Nutzer sich wünscht, ist es nicht —
   auch nicht, wenn er es im selben Satz sagt.
4. **Zahlen kommen nur aus `preise/`.** Aus `angebote/` werden Aufbau und
   Formulierung übernommen, **nie** die Beträge: Ein alter Angebotspreis ist
   ein Einzelfall, keine Preisgrundlage. Wer aus `angebote/` rechnet, rechnet
   mit dem Preis eines fremden Auftrags.
5. **Herkunft steht im internen Block.** Wo ein Skill einen internen Block
   ausgibt (Block B, `ÜBERGABE …`), nennt er die benutzte Unterlage mit
   Dateinamen — und bei Preisen zusätzlich Ebene und Stand
   (`preisregeln.md`). Was aus einer Unterlage stammt, muss nachprüfbar sein,
   ohne dass jemand rät.
6. **Widerspruch wird gemeldet, nicht aufgelöst.** Sagen zwei Unterlagen etwas
   Unterschiedliches, entscheidet **nicht** der Skill. Er nennt beide Stellen
   und fragt einmal — außer bei Preisen, dort gilt die feste Rangfolge aus
   `preisregeln.md`.
7. **Nicht gefunden ist eine Aussage.** „In den Unterlagen steht dazu nichts"
   ist ein Ergebnis und wird so ausgegeben. Es wird nie durch etwas
   Plausibles ersetzt.

## Schreiben in diesen Ordner

Der Ordner gehört dem Nutzer. Es gibt genau **zwei** Schreibvorgänge, beide in
`preisregeln.md` beschrieben, beide additiv:

- Eine abgelöste Preisdatei wandert nach `preise/archiv/` (verschoben, nie
  gelöscht).
- Eine bestätigte Preisgültigkeit wird als kurze Notiz in `preise/` abgelegt.

**Sonst schreibt kein Skill hier hinein.** Keine Datei wird inhaltlich
geändert, keine gelöscht, keine umbenannt, keine „aufgeräumt". Ergebnisse
gehen nach `ergebnisse/`, nie hierher.

## Was nicht hierher gehört

- **Nichts, was der Nutzer nicht selbst hineingelegt hat.** Kein Skill legt
  hier Entwürfe, Zwischenstände oder Notizen ab.
- **Keine Zugangsdaten.** Passwörter, Schlüssel und Zugänge gehören nicht in
  Unterlagen, die ein Assistent liest.

## Bleibt lokal

Alles in diesem Ordner bleibt auf dem Rechner des Nutzers. Es wird nicht
hochgeladen, nicht mitgeschickt, nicht gesammelt und kommt nie zum Hersteller
des Kits zurück.
