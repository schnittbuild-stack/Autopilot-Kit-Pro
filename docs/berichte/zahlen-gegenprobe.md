# Gegenprobe auf veraltete Bestandsaussagen (28.08.2026)

Am 28.08. ist mir viermal derselbe Fehler unterlaufen: **eine Aussage steht an
mehreren Orten, gepflegt wird einer.** Der Bericht dazu endet mit der Lehre,
eine Aussage über den Bestand gehöre an genau eine Stelle, alles andere
verweise dorthin — und wo sie doch mehrfach stehe, sei die Gegenprobe ein
`grep`, nicht das Gedächtnis.

Dieses Paket wendet die Lehre an, statt sie nur aufzuschreiben.

## Der Ist-Bestand, ausgezählt statt erinnert

| | Ist |
|---|---|
| Ketten-Testfälle | 8 |
| Übergabeverträge | 3 |
| Helfer | 10 |
| Testfälle gesamt | 41 |

## Was die Gegenprobe gefunden hat

Gesucht wurde nach Zahlwörtern vor „Verträge", „Ketten", „Helfer", „Fälle" —
in `core/`, `adapter-claude/` und `notfall/`, also in allem, was zum Kunden
geht. **Vier Skill-Dateien trugen veraltete Aufzählungen:**

| Datei | behauptete | tatsächlich |
|---|---|---|
| `angebots-schreiber.md` | „**fünf** Fälle" | sechs, seit `06-fehlender-absender` |
| `angebots-schreiber.md` | „die **beiden** Schnittstellen-Fälle: 01 und 02" | fünf Ketten führen ihn |
| `account-recherche.md` | nur `ketten/01` | sechs Ketten führen ihn |
| `follow-up-generator.md` | nur `ketten/02` | drei Ketten führen ihn |
| `outreach-personalisierer.md` | **keine** Kette genannt | drei Ketten führen ihn |

Die letzte Zeile ist die aufschlussreichste: Der Helfer stand seit dem 28.08. in
drei Ketten und wusste es selbst nicht. Genau dieselbe Stelle hatte der Wächter
schon einmal falsch beschrieben („der `outreach-personalisierer` kommt in keiner
vor") — dort behoben, in der Anleitung des Helfers übersehen.

## Was daraus geworden ist — und was ausdrücklich nicht

**Die Zahlen sind nicht nachgezogen worden.** Eine berichtigte Aufzählung ist
mit dem nächsten Ketten-Fall wieder falsch, und dann fällt es niemandem auf,
weil sie ja gerade erst gepflegt wurde.

Stattdessen zeigen die vier Stellen jetzt auf die Quelle:

> **Welche das sind, steht in den Fällen selbst**, oben unter „Schnittstelle" —
> hier steht bewusst keine Liste, weil sie mit dem nächsten Ketten-Fall falsch
> wäre.

Dasselbe Verfahren, das der Wächter seit dem 28.08. für die Ketten-Zugehörigkeit
befolgt, und dieselbe Regel, die Prinzip 1 für Profildaten aufstellt: **eine
Quelle, alles andere verweist.**

Die Aufzählung der Bruchstellen im `angebots-schreiber` bleibt — sie sagt, was
die Fälle prüfen, nicht wie viele es sind. Der neue sechste ist ergänzt.

## Der Sweep selbst war zu eng — und der Review hat es gezeigt

Meine Gegenprobe suchte nach **Zahlwörtern** vor „Verträge", „Ketten",
„Helfer", „Fälle". Sie hat damit eine ganze Klasse übersehen: **bloße
Pfad-Aufzählungen ohne Zahlwort.** Genau die standen in zwei Verträgen:

| Datei | führte auf | tatsächlich |
|---|---|---|
| `account-recherche-zu-angebots-schreiber.md` | nur `ketten/01` | `01`, `03`, `04` |
| `angebots-schreiber-zu-follow-up-generator.md` | nur `ketten/02` | `02`, `03`, `05` |

Dieselbe Bauart, dieselbe Wirkung, in `core/` — und die Work Order hatte eine
Gegenprobe „über **alle** Bestandsaussagen in `core/`" zugesagt. Gefunden hat
sie der unabhängige Review, nicht mein Sweep.

Beide Stellen zeigen jetzt auf dieselbe Quelle wie die vier Skills. Die Zusage
der Work Order ist damit eingelöst — aber sie war es zum Zeitpunkt der
Behauptung nicht.

**Was das über die Methode sagt:** Ein `grep` ist nur so gut wie sein Muster.
„Eine Aussage über den Bestand" ist keine Zeichenfolge; sie kann als Zahl, als
Aufzählung oder als einzelner Pfad auftreten. Wer nach der Zahl sucht, findet
die Aufzählung nicht — und hält seine Suche trotzdem für vollständig. **Das ist
dieselbe Falle wie die Vollständigkeitsaussage im Vertrag**, eine Ebene höher:
Nicht die Aussage war falsch, sondern die Annahme, sie geprüft zu haben.

## Nachlauf

Eine Änderung am Skill zieht nach der Arbeitsregel vom 19.08.2026 dessen
Testfälle nach sich. Betroffen sind vier Helfer.

**Umfang ausdrücklich benannt:** Ich habe **je einen** Fall der vier Helfer
dreimal laufen lassen, nicht alle. Grund: Die Änderung betrifft ausschließlich
den Testfall-Abschnitt am Dateiende, keine Verhaltensregel. Ein Vollnachlauf
wären 45 Läufe für eine Literaturangabe.

| Fall | Ergebnis |
|---|---|
| `angebots-schreiber/01-rueckfrage-disziplin` | 3 von 3 — genau zwei Fragen, kein Angebot |
| `account-recherche/01-leere-quellenlage` | 3 von 3 — leere Belegliste, `Nicht gefunden` gefüllt, keine Vermutung als Beleg |
| `follow-up-generator/02-kein-anlass` | 3 von 3 — kein Kundentext, Rückfrage mit Optionen |
| `outreach-personalisierer/02-erfundene-naehe` | 3 von 3 — Themenbezug ohne behaupteten Vortragsinhalt |

Bei `outreach/02` schreiben alle drei Läufe „ich war selbst dort" bzw. „ich war
auf derselben Messe". Das ist **keine** angedeutete Begegnung, sondern die
Ko-Präsenz, die die Entscheidung vom 25.08.2026 ausdrücklich zulässt.

## Die zwei Hinweise aus dem Review zu WO-020

- Der Fehlverweis auf „offenen Punkt 3" stand an **zwei** Stellen im STATUS;
  korrigiert war eine. Die zweite trug außerdem einen überholten Stand — Fall
  03 läuft seit der Maskierungs-Korrektur 3 von 3, nicht 2 von 3. Beides
  nachgezogen.
- Die Ausgangslage im Bericht sprach von sechs Ketten-Fällen bei Beginn der
  Arbeit; es waren fünf. Berichtigt.

**Beide sind wieder dieselbe Bauart.** Das ist an diesem Tag die fünfte und
sechste Fundstelle — und der Grund, warum dieses Paket die Aufzählungen nicht
repariert, sondern abschafft.

---

## Nachtrag: die siebte Fundstelle

Der Review zu diesem Paket hat zum Schluss angemerkt, dass `STATUS-BAU.md` und
`entscheidungen.md` weiter „vier Skills" sagen — obwohl in Runde 2 zwei
Verträge dazugekommen sind.

**Siebte Fundstelle derselben Bauart an einem Tag, ausgerechnet in dem Paket,
das sie abschafft.** Beide Rückblicke sind berichtigt; sie sind datierte
Aussagen über ein abgeschlossenes Paket, dort ist eine Zahl legitim — sie war
nur falsch.

### Der Sweep, diesmal nach dem Muster

Die Lehre aus Runde 1 war: Ein `grep` ist nur so gut wie sein Muster, und „eine
Aussage über den Bestand" ist keine Zeichenfolge. Also diesmal nicht nach
Zahlwörtern gesucht, sondern nach der **Form**: nennt eine ausgelieferte Datei
einzelne Testfall-Pfade?

Drei Treffer, alle im `outreach`-Vertrag — und alle **keine** Bestandsaussage:
Es sind Belege, je mit Fall, geprüfter Regel und Datum. Ein neuer Ketten-Fall
macht keinen davon falsch.

**Trotzdem geändert**, um eine Zeile: Der Abschnitt sagt jetzt selbst, dass er
Belege führt und keine Bestandsliste, und verweist für die vollständige
Zugehörigkeit auf dieselbe Quelle wie alle anderen Stellen. Der Unterschied
zwischen „hier sind die Belege" und „hier sind die Fälle" ist einem Leser sonst
nicht anzusehen — und genau diese Verwechslung hat den ganzen Tag über Arbeit
gemacht.

### Die Bilanz des Tages

| | |
|---|---|
| Fundstellen derselben Bauart | 7 |
| davon vom unabhängigen Review gefunden | 7 |
| davon von der Testsuite gefunden | 0 |
| davon von mir vor der Meldung gefunden | 0 |

Das ist der belastbarste Befund dieses Tages, und er betrifft nicht das Produkt,
sondern das Verfahren: **Ein Bauender findet die eigene Duplikatspflege nicht.**
Nicht aus Nachlässigkeit — sondern weil er beim Schreiben der zweiten Stelle
sicher ist, die erste zu kennen. Der Review teilt diese Sicherheit nicht, und
darin liegt sein ganzer Wert.
