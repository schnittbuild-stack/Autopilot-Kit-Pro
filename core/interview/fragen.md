# Die zehn Interviewfragen (final)

<!-- Plattformneutral (Prinzip 4). Der Installer stellt genau diese Fragen,
     in dieser Reihenfolge. Zuordnung zu den Platzhaltern: mapping.md.
     Finalisiert in Phase 3 am 19.08.2026. -->

## Regeln für das ganze Interview

Diese Regeln sind Teil der Aufgabe, nicht Beiwerk:

1. **Eine Frage pro Nachricht.** Nie zwei auf einmal, auch keine „und
   nebenbei"-Frage. Wer zwei Fragen bekommt, beantwortet eine.
2. **Jede Frage bringt ihr Beispiel mit.** Das Beispiel steht in derselben
   Nachricht, kurz, und zeigt eine Antwort — keine Erklärung der Frage.
3. **Kein Fachbegriff.** Nicht „Konfiguration", „Platzhalter", „Profil-Datei",
   „Parameter". Der Nutzer soll nichts lernen müssen, um zu antworten.
4. **Jede Antwort ist gültig, auch „weiß nicht" und „überspring das".**
   Wird übersprungen, wird es im Profil als leer vermerkt — nicht geraten,
   nicht ausgeschmückt und später nicht heimlich ergänzt.
5. **Nicht nachbohren.** Höchstens **eine** Nachfrage je Frage, und nur, wenn
   die Antwort für den späteren Gebrauch nicht reicht (siehe „Nachhaken" bei
   der jeweiligen Frage). Danach weiter, egal wie dünn es ist.
6. **Nichts bewerten.** Keine Antwort wird gelobt, korrigiert oder kommentiert
   („super!", „gute Wahl"). Ein knappes Weiterschalten reicht.
7. **Nach jeder zweiten Antwort ein Fortschrittssatz**, damit der Nutzer weiß,
   wo er steht: „Vier von zehn — läuft."
8. **Antworten sofort sichern.** Nach jeder Antwort wird sie ins Profil
   geschrieben, nicht erst am Ende. Bricht die Sitzung nach Frage 6 ab, sind
   sechs Antworten da.

## Die zehn Fragen

### 1. Der Job

> Was machst du beruflich? Erklär's mir so, wie du es deinem Nachbarn über den
> Gartenzaun erklären würdest.
>
> *Zum Beispiel: „Ich verkaufe Wartungsverträge an Industriebetriebe."*

Füllt: `{{rolle}}` · **Nachhaken**, wenn nur eine Berufsbezeichnung kommt
(„Vertrieb"): „Und was machst du an einem normalen Dienstag davon konkret?"

### 2. Die Firma

> In welcher Firma arbeitest du, und was macht die? Das bleibt auf deinem
> Rechner.
>
> *Zum Beispiel: „Reinhardt Industrieservice, 18 Leute, wir warten und
> montieren Anlagen für Mittelständler."*

Füllt: `{{firma}}` · **Nicht nachhaken.**

### 3. Was nervt

> Welche drei Aufgaben nerven dich jede Woche am meisten? Gern die, bei denen
> du denkst „das schon wieder".
>
> *Zum Beispiel: „Angebote schreiben nach einem langen Tag, Nachfassen ohne
> guten Anlass, Protokolle aus meinen Kritzeleien im Auto."*

Füllt: `{{nervaufgaben}}` · **Wichtigste Frage des Interviews** — sie
entscheidet in Phase 3, welche Assistenten eingerichtet werden.
**Nachhaken**, wenn nur eine Aufgabe kommt: „Und was noch? Zwei reichen mir
auch."

### 4. Die Programme

> Womit arbeitest du täglich? Einfach aufzählen, was du morgens aufmachst.
>
> *Zum Beispiel: „Outlook, Excel, unser CRM heißt Pipedrive, und DATEV für
> die Zahlen."*

Füllt: `{{tools}}` · **Nicht nachhaken.**

### 5. Der Ton

> Wenn du einem Kunden schreibst — eher förmlich („Sehr geehrter Herr Meyer")
> oder eher locker („Hallo Herr Meyer")? Und schreibst du kurz und knapp oder
> ausführlich?
>
> *Zum Beispiel: „Eher förmlich, aber kurz. Ich mag keine Werbesprache."*

Füllt: `{{tonalitaet}}` (zusammen mit dem Material aus Frage 9)
**Nicht nachhaken** — was hier fehlt, holt das Material nach.

### 6. Du oder Sie

> Duzt oder siezt du deine Kunden?
>
> *Zum Beispiel: „Siezen. Außer die zwei, die ich seit zwanzig Jahren kenne."*

Füllt: `{{anrede}}` · **Nicht nachhaken.** Ausnahmen werden wörtlich
übernommen, nicht zu einer Regel verallgemeinert.

### 7. Die Signatur

> Wie sieht deine E-Mail-Signatur aus? Einfach hier reinkopieren, so wie sie
> in deinen Mails steht.
>
> *Zum Beispiel: „Mit freundlichen Grüßen / Katrin Reinhardt / Reinhardt
> Industrieservice GmbH / Telefon 0234 5558820"*

Füllt: `{{signatur}}` · **Nicht nachhaken.** Wird **wörtlich** übernommen,
nichts umformatiert, nichts ergänzt, keine Zeile weggelassen.

### 8. Die No-Gos

> Gibt es Sätze oder Themen, die du nie schreiben würdest? Sachen, bei denen
> du zusammenzuckst, wenn du sie in einer Mail liest.
>
> *Zum Beispiel: „Keine Erfolgsversprechen. Kein ‚zeitnah'. Und nichts, was
> nach Drängeln klingt."*

Füllt: `{{verbote}}` · **Nachhaken**, wenn „nö, eigentlich nicht" kommt:
„Auch nichts, was du rechtlich nie zusagen dürftest — Garantien,
Erfolgsversprechen?" Danach weiter, auch wenn es leer bleibt.

### 9. Dein Material

> Hast du Sachen rumliegen, die ich kennen sollte? Deine Preisliste, ein paar
> alte Angebote, Leistungsbeschreibungen, deine AGB, E-Mails, die du gut
> findest. Alles freiwillig — aber je mehr davon da ist, desto seltener muss
> ich dich fragen und desto mehr klingt es nach dir.
>
> Wenn du was hast: Zieh die Dateien in den Ordner **meine-unterlagen**, den
> ich gerade angelegt habe. Du kannst das auch später machen — ich komme von
> allein darauf zurück.
>
> *Zum Beispiel: „Preisliste hab ich als Excel, alte Angebote liegen als PDF
> im Kundenordner."*

Füllt: `{{stilbeispiele}}` und `{{preisgrundlage}}` (siehe `mapping.md`)

**Diese Frage blockiert nie.** „Hab ich nicht", „später" und „keine Lust"
sind vollwertige Antworten. Was fehlt, wird später gefragt — nicht erfunden.

**Nachhaken** genau einmal, und nur bei „ich weiß nicht, was du meinst":
„Alles, was du sonst raussuchen müsstest, wenn ein Angebot ansteht."

### 10. Der Moment, an dem es sich gelohnt hat

> Woran würdest du merken, dass sich das hier gelohnt hat? Ein Moment, nicht
> eine Zahl.
>
> *Zum Beispiel: „Freitagabend ist kein Angebot mehr offen, das eigentlich
> Montag hätte rausgehen sollen."*

Füllt: `{{erfolgsmoment}}` · **Nicht nachhaken.** Die Antwort steuert, welche
Aufgabe in Phase 4 (Beweis) vorgeschlagen wird.

## Die bedingte Zusatzfrage

Wird **nur** gestellt, wenn **beides** zutrifft:

1. In `meine-unterlagen/preise/` liegt nichts, **und**
2. die Antworten auf Frage 1 und 3 zeigen preisbildende Arbeit — Angebote,
   Kalkulation, Verhandlung.

Dann genau eine zusätzliche Frage, direkt nach Frage 9:

> Wie kommst du normalerweise auf deinen Preis — Stundensatz, Tagessatz,
> Pauschale? Oder ist das jedes Mal anders?
>
> *Zum Beispiel: „Technik 890 am Tag, Schulung 1.250, Monteurstunde 78."*

Füllt: `{{preisgrundlage}}` · Bleibt auch sie leer, ist das **kein Fehler**:
Die Assistenten schreiben dann `[PREIS PRÜFEN]` an die Preiszeile, statt eine
Zahl zu erfinden.

## Was nicht gefragt wird

- **Keine Zugangsdaten**, keine Passwörter, keine Schlüssel. Nie, in keiner
  Phase, aus keinem Grund.
- **Keine Kundendaten auf Vorrat.** Namen und Firmen kommen mit der jeweiligen
  Aufgabe, nicht ins Profil.
- **Nichts, was schon in einer Antwort steht.** Wer bei Frage 1 die Firma
  nennt, wird bei Frage 2 nicht noch einmal danach gefragt — dann bestätigen
  statt fragen: „Du hattest Reinhardt Industrieservice gesagt — stimmt das so?"
- **Nichts Technisches.** Nicht nach Ordnern, Dateiformaten, Versionen,
  Konten oder Einstellungen. Das erledigt der Installer selbst.

## Checkliste — vor dem Weitergehen zur nächsten Phase

- [ ] Genau zehn Fragen gestellt, jede einzeln, jede mit Beispiel.
- [ ] Die Zusatzfrage nur gestellt, wenn beide Bedingungen zutrafen — sonst
      gar nicht.
- [ ] Höchstens eine Nachfrage je Frage, und nur wo oben erlaubt.
- [ ] Jede Antwort steht im Profil, wörtlich bei Signatur und No-Gos.
- [ ] Übersprungene Fragen stehen als leer im Profil — nichts ergänzt,
      nichts geraten.
- [ ] Keine Zugangsdaten erfragt, keine Kundendaten auf Vorrat.
- [ ] Kein Fachbegriff gefallen — auch nicht in den Zwischensätzen.
- [ ] Das Profil wurde dem Nutzer in drei Sätzen vorgelesen und von ihm
      bestätigt oder korrigiert.
