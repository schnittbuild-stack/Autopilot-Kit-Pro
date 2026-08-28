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
| Testfälle gesamt | 42 |

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
