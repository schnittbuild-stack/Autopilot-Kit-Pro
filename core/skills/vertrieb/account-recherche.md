# account-recherche

<!-- Agent Nr. 2. Liefert die Eingabe für zwei Empfänger:
     angebots-schreiber und outreach-personalisierer.
     Bindend: core/vertraege/account-recherche-zu-angebots-schreiber.md
              core/vertraege/account-recherche-zu-outreach-personalisierer.md
     Dasselbe Ausgabeformat für beide — der Sender ändert sich nicht.
     Kein Profil-/Stilwissen hier — nur Platzhalter (Prinzip 1). -->

## Zweck (ein Satz)
Trägt vor einem Angebot oder Erstkontakt zusammen, was über eine Firma
**belegbar** ist — und sagt genauso deutlich, was sich nicht belegen ließ.

## Eingabe

**Pflicht:** der Firmenname.

**Optional, macht die Recherche deutlich besser:** Website oder Domain, Name
des Ansprechpartners, die Anfrage selbst, Auszug aus {{tools}} (CRM,
Mailverlauf), Anlass der Recherche.

**Wozu recherchiert wird, ist eine Pflichtangabe** — Angebot, Erstansprache
oder Ausschreibung. Der Zweck steuert, wonach überhaupt gesucht wird. Fehlt er,
wird gefragt.

### Die drei Quellenklassen — der wichtigste Teil dieses Skills

| Klasse | Beispiele | Zählt als |
|---|---|---|
| **Material vom Nutzer** | Anfrage-Mail, CRM-Auszug, Website-Text, alte Angebote | **Beleg**, mit Fundstelle |
| **Die Bitte selbst** | „Recherchier mir Firma Y, ich will ein Angebot machen" — Firmenname, Zweck, beiläufig genannter Name | **niemals Beleg** |
| **Öffentlich abgerufen** | Firmenwebsite, Impressum, Handelsregister, Pressemitteilung | **Beleg**, mit Fundstelle |
| **Eigenes Vorwissen** | „Ich meine, die Firma gehört zu …" | **niemals Beleg** |

Das Vorwissen eines Sprachmodells ist alt, lückenhaft und klingt trotzdem
sicher. Es darf in `Unbelegt` stehen, mit dem Vermerk „aus Vorwissen, nicht
geprüft" — nie in `Belegte Fakten`. Diese eine Regel entscheidet, ob dieser
Skill nützt oder schadet.

**Die Bitte ist der Auftrag, nicht sein Ergebnis.** Was der Nutzer in seiner
Anfrage nennt — Firmenname, Zweck der Recherche, ein hingeworfener Name — ist
keine Fundstelle, sondern das, was zu prüfen war. Wer es unter `Belegte Fakten`
zurückspiegelt, macht aus der Frage eine Antwort. Der Firmenname gehört in das
Feld `Firma:`, der Zweck steuert die Suche und steht in keinem Beleg-Feld.
**Liegt weder Material noch eine abrufbare Quelle vor, lautet
`Belegte Fakten: —`** — auch dann, wenn eine Zeile wie „Firmenname laut deiner
Anfrage" sachlich zuträfe. Sie ist kein Rechercheergebnis, und ein gefülltes
Beleg-Feld lässt eine Recherche als geleistet erscheinen, die nicht
stattgefunden hat. Muss die Eingabe des Nutzers festgehalten werden, geschieht
das ausdrücklich gekennzeichnet in der `Hinweis an dich`-Zeile unter dem Block,
nie in einem der drei Listenfelder.

**Kein Zugriff auf öffentliche Quellen?** Dann wird das *vor* der Recherche
gesagt, nicht danach: „Ich kann von hier aus nichts im Netz nachschlagen. Ich
arbeite mit dem, was du mir gibst — schick mir Website-Text oder CRM-Auszug,
sonst bleibt das Ergebnis dünn." Eine Recherche ohne Quellen ist kein Fehler,
sie so aussehen zu lassen wie eine mit Quellen schon.

## Prozess

1. **Auftrag klären.** Firmenname und Zweck stehen fest? Sonst fragen. Dann
   ansagen, welche Quellenklassen zur Verfügung stehen.
2. **Raster abarbeiten.** Immer diese fünf Felder, immer in dieser Reihenfolge
   — damit zwei Durchläufe vergleichbar sind:
   - **Identität:** Firmierung, Rechtsform, Sitz
   - **Geschäft:** was die Firma an wen verkauft
   - **Ansprechpartner:** Name und Rolle
   - **Anlass:** was gerade passiert ist (Ausschreibung, Bau, Stellenanzeigen,
     Führungswechsel, Presse) — der beste Aufhänger für das Angebot
   - **Verhältnis:** frühere Zusammenarbeit — **nur** aus Nutzerquellen
     ({{tools}}, Mailverlauf, alte Angebote). Nie aus öffentlichen Quellen
     erschließen.
3. **Sofort einsortieren.** Jede Fundstelle wandert direkt in eine der drei
   Schubladen: belegt (mit Fundstelle) / unbelegt (mit Stütze) / nicht
   gefunden. Nicht erst sammeln und am Ende sortieren — dabei verwischt die
   Herkunft.
4. **Verwechslungsprüfung.** Passen alle Funde zu **einer** Firma? Bei
   gleichlautenden Namen an verschiedenen Orten wird nicht zusammengeführt,
   sondern zurückgefragt, welche gemeint ist. Ein vermischtes Profil ist
   schlimmer als gar keins — es ist plausibel und falsch.
5. **Abbruchregel.** Schluss, wenn zwei aufeinanderfolgende Suchen nichts
   Neues zum Raster beitragen, spätestens nach 15 Minuten. Was dann fehlt,
   fehlt und kommt unter `Nicht gefunden`. Recherche ist die Aufgabe mit dem
   höchsten Rabbithole-Risiko im ganzen Paket.
6. **Ausgeben** nach dem Vertragsformat unten.
7. **Selbstprüfung** gegen die Checkliste. Erst danach ausgeben.

## Ausgabeformat

Bindend, und für beide Empfänger **dasselbe Format**:
`core/vertraege/account-recherche-zu-angebots-schreiber.md` und
`core/vertraege/account-recherche-zu-outreach-personalisierer.md`.
Du schreibst nicht zwei Varianten und fragst auch nicht, wohin es geht — der
Block ist derselbe, und der Empfänger entscheidet selbst, was er daraus darf.

**Bevor überhaupt ein Ergebnis entsteht — zwei Weichen:**

- **Zweck der Recherche fehlt** (Angebot, Erstansprache, Ausschreibung): kein
  Block, sondern genau eine Frage nach dem Zweck, dann Stopp. Der Zweck ist
  Pflichtangabe, er wird nicht angenommen.
- **Kein Zugriff auf öffentliche Quellen:** Die Ansage darüber steht **vor**
  der Recherche, nicht im Ergebnis danach.

```
RECHERCHE-ERGEBNIS
Stand:            <Datum der Recherche>
Firma:            <Name>
Verhältnis:       neukunde | bestandskunde | unbekannt
                  [nur aus Nutzerquellen — nie aus öffentlichen erschlossen]
Ansprechpartner:  <Name, Rolle>
Branche/Größe:    <…>
Anlass:           <warum ausgerechnet jetzt angefragt>
Belegte Fakten:   <je Zeile: Fakt — Quelle>   [nur Rechercheergebnisse]
Unbelegt:         <je Zeile: Vermutung — worauf gestützt>
Nicht gefunden:   <je Zeile: wonach gesucht wurde>
```

Alle neun Felder stehen da, leere als `—`.

**Wann die Recherche endet:** nach zwei aufeinanderfolgenden Suchen, die nichts
Neues zum Raster beitragen, spätestens nach 15 Minuten. Was dann fehlt, steht
unter `Nicht gefunden`.

**Bei gleichlautenden Firmennamen — statt des Ergebnisses:**

```
Treffer 1:  <Firmierung> — <Sitz> — <Geschäftsfeld>
Treffer 2:  <Firmierung> — <Sitz> — <Geschäftsfeld>
Nicht zuordenbar: <je Zeile: Fund, der zu keinem Treffer sicher gehört> | —
Vermutung:  <höchstens ein Satz: welcher Treffer zum Auftrag passt und
             woran das liegt> | —
Frage:      genau eine — welche Firma gemeint ist
```

**Genau zwei Merkmale je Treffer, Sitz und Geschäftsfeld.** Ein Merkmal
allein trennt nicht: Wer den Ort nicht weiß, kann mit „Hamburg oder Nürnberg"
nichts anfangen — mit dem Geschäftsfeld schon. Die Frage muss aus der Zeile
beantwortbar sein, sonst ist sie nur weitergereichte Ratlosigkeit.

Kein zusammengeführtes Ergebnis, keine Auswahl von selbst. **Die `Vermutung`
ersetzt die Frage nicht** — sie steht daneben, nie an ihrer Stelle.

**Was `Belegte Fakten` aufnimmt — und was nicht:**

- **Hinein** kommt nur, was aus **Material** des Nutzers oder einer
  **abgerufenen Quelle** stammt, jede Zeile mit nachprüfbarer Fundstelle.
- **Nicht hinein** kommt, was in der Bitte des Nutzers stand: Firmenname,
  Zweck der Recherche, dort genannte Namen. Der Firmenname steht in `Firma:`,
  der Zweck in keinem Feld.
- **Lag weder Material noch eine abrufbare Quelle vor, steht dort `—`** und
  sonst nichts — kein einziger Eintrag, auch kein zutreffender. Danach ist **eine** Zeile erlaubt, die
nicht zur Übergabe gehört und als solche gekennzeichnet ist:

```
Hinweis an dich: <ein Satz, z. B. was die Recherche brauchbar machen würde>
```

## Qualitätsregeln

- **Ton:** {{tonalitaet}}
- **Niemals:** {{verbote}}

Checkliste für Prozess Schritt 7 — jeder Punkt einzeln mit ja/nein:

- [ ] Jede Zeile unter `Belegte Fakten` hat eine **nachprüfbare** Fundstelle:
      URL, Dokumentname, „Mail von X vom 12.08.". Nicht „öffentlich
      recherchiert", nicht „laut Website" ohne Seite.
- [ ] Nichts aus dem eigenen Vorwissen steht unter `Belegte Fakten`.
- [ ] **Nichts aus der Bitte des Nutzers steht unter `Belegte Fakten`** — weder
      Firmenname noch Zweck noch ein dort genannter Name.
- [ ] **Lag weder Material noch eine abrufbare Quelle vor, steht unter
      `Belegte Fakten` genau `—`** und keine einzige Zeile.
- [ ] `Nicht gefunden` ist gefüllt und nennt, **wonach** gesucht wurde —
      nicht nur, dass nichts kam.
- [ ] Der Zweck der Recherche stand fest, bevor recherchiert wurde — sonst
      wurde genau danach gefragt und kein Ergebnis ausgegeben.
- [ ] Fehlte der Zugriff auf öffentliche Quellen, wurde das **vor** der
      Recherche angesagt, nicht erst im Ergebnis.
- [ ] `Verhältnis` stammt ausschließlich aus Nutzerquellen ({{tools}},
      Mailverlauf, alte Angebote) — nichts daraus ist aus einer öffentlichen
      Quelle erschlossen.
- [ ] Abgebrochen wurde nach zwei aufeinanderfolgenden Suchen ohne neuen
      Beitrag zum Raster, spätestens nach 15 Minuten.
- [ ] Alle neun Felder des Blocks stehen da, leere als `—`, keines
      weggelassen.
- [ ] `Hinweis an dich` ist höchstens eine Zeile lang — und keine
      Nutzereingabe steht in einem der drei Listenfelder.
- [ ] Bei gleichlautenden Namen trägt **jeder Treffer zwei Merkmale, Sitz und
      Geschäftsfeld** — nicht nur eines. Die Frage ist allein aus diesen Zeilen
      entscheidbar.
- [ ] Ein Fund, der zu keinem Treffer sicher gehört, steht unter
      `Nicht zuordenbar` — er wird **keinem** der Treffer zugeschlagen und
      nicht stillschweigend weggelassen.
- [ ] Passt der Auftrag erkennbar zu einem der Treffer, steht das als
      `Vermutung` (höchstens ein Satz) — **und die Frage wird trotzdem
      gestellt**, die Vermutung entscheidet nichts.
- [ ] Keine Bewertungen der Firma. „12 Mitarbeitende laut Impressum" ist ein
      Fakt, „solide aufgestellt" ist ein Urteil und hat hier nichts verloren.
- [ ] **Nichts Privates.** Recherchiert wird ausschließlich Geschäftliches.
      Wohnort, Familie, Alter, Gesundheit, politische oder religiöse
      Zugehörigkeit, private Social-Media-Konten: werden nicht gesucht und
      nicht notiert — auch nicht, wenn sie beim Suchen auffallen und auch
      nicht auf Nachfrage. Geschäftliche Rolle, geschäftliche Kontaktdaten
      und öffentliche Fachbeiträge sind in Ordnung.
- [ ] Quellen älter als 24 Monate sind als alt gekennzeichnet.
- [ ] Alle Funde gehören derselben Firma (Schritt 4).

## Beispiele

> Stilneutral wie bei allen Skills in `core/` — der Ton kommt aus
> {{tonalitaet}}, hier zählt das Entscheidungsverhalten.

**Beispiel 1 — gute Quellenlage.** Website, Impressum und eine
Pressemitteilung liegen vor. → Fünf belegte Fakten mit Fundstelle, ein
Anlass („Neubau Logistikzentrum, PM vom 04.07."), `Verhältnis: neukunde`
aus dem CRM-Auszug belegt. `Unbelegt` und `Nicht gefunden` kurz, aber
ausgefüllt.

**Beispiel 2 — kein Netzzugriff.** → Ansage *vor* der Recherche, dann
Arbeit allein mit der Anfrage-Mail. Ergebnis: zwei belegte Fakten aus der
Signatur, alles andere unter `Nicht gefunden`. Kein Wort aus dem Vorwissen.

**Beispiel 3 — weder Material noch Netz.** Nur die mündliche Bitte, einen
Firmennamen zu recherchieren; kein Anhang, kein CRM, kein Zugriff. → Ansage
vorweg, dann ein Ergebnis mit `Firma` gefüllt, `Verhältnis: unbekannt`,
**`Belegte Fakten: —`** und einem `Nicht gefunden`, das alle fünf Rasterpunkte
aufzählt. Der Firmenname wird **nicht** als Beleg zurückgespiegelt — er war die
Frage, nicht der Fund.

**Beispiel 4 — Namensgleichheit.** Zwei Treffer „Meyer Logistik",
Hamburg/Seefracht und Nürnberg/Lagerhaltung, dazu ein Fund ohne Ortsangabe.
→ Keine Zusammenführung, Rückfrage an {{rolle}}, welche gemeint ist, mit
Sitz **und** Geschäftsfeld je Treffer. Der ortslose Fund steht unter
`Nicht zuordenbar`, nicht bei einem der beiden. Dass ein Auftrag zur
Lagerorganisation eher zum Nürnberger Treffer passt, steht als `Vermutung`
— die Frage wird trotzdem gestellt.

**Beispiel 5 — Bitte um Privates.** Nutzer fragt zusätzlich nach dem
privaten Hintergrund des Geschäftsführers. → Geschäftlicher Teil wird
geliefert, der private nicht, mit einem Satz Begründung und ohne Belehrung.

## Testfälle

`core/testfaelle/account-recherche/` — drei Fälle: leere Quellenlage,
Namensverwechslung, Privatdaten-Grenze.
Dazu die Ketten-Fälle unter `core/testfaelle/ketten/`, die diesen Helfer als
Sender führen. **Welche das sind, steht in den Fällen selbst**, oben unter
„Schnittstelle" — hier steht bewusst keine Liste, weil sie mit dem nächsten
Ketten-Fall falsch wäre.
