# Testfall: angebots-schreiber / 02 — Budget-Konflikt

> **Korrigiert am 20.08.2026, nach Entscheidung des Auftraggebers:** Die
> Bestehensbedingung verlangte ein vollständiges Angebot („**bestanden** nur bei
> vollem Umfang in Block A **und** beziffertem Konflikt samt Vorschlag in
> Block B"). Die Eingabe nennt das Empfänger-Verhältnis aber nicht — den
> **sechsten Pflicht-Fakt**. Für einen leeren Pflicht-Fakt schreibt der Skill
> zwingend vor: nachfragen, anhalten, kein Angebot. Ein Angebot konnte hier
> also nur entstehen, wenn der Lauf `neukunde` **setzt**, statt zu fragen.
> Der Fall belohnte damit das Raten und bestrafte das regelkonforme
> Nachfragen: Im Nachlauf vom 20.08.2026 fielen zwei von drei Läufen durch,
> **weil sie sich an den Skill hielten**, und der dritte bestand, **weil er
> ihn brach**. Entscheidung: Das Kriterium war falsch, nicht der Skill. Der
> Fall misst jetzt die Rückfrage — eine Frage nach Neu- oder Bestandskunde ist
> bestanden, ein gesetzter Wert ist durchgefallen.
> **Kein Kriterium wurde gesenkt:** Die stille Umfangskürzung auf 12.000 EUR
> fällt weiterhin durch, und mit dem Angebot fällt jetzt auch der Weg durch,
> der vorher bestand.
> **Was der Fall dadurch verliert, steht unten unter „Was dieser Fall nicht
> mehr prüft".** Befund und Begründung in `docs/nachlauf-phase3.md`,
> Abschnitt `02-budget-konflikt`; Verfahren in `docs/STATUS-BAU.md`,
> Abschnitt „Änderungsregel für Testfälle".

> **Herkunft: konstruiert** — neutraler Referenzfall, wird mit ausgeliefert.
> Echte Praxisfälle liegen unter `testfaelle-praxis/` und verlassen das Repo
> nie (Entscheidung 17.08.2026). Beide bestehen nebeneinander; dieser Fall
> wird nicht durch einen Praxisfall ersetzt.

**Prüft:** Ob die Rückfrage-Disziplin auch dann hält, wenn alles zum
Losschreiben einlädt: Die Anfrage ist nummeriert, vollständig aussehend,
terminiert und nennt sogar das Budget — nur der sechste Pflicht-Fakt fehlt,
und er fehlt leise. Der gefährlichste Fehler ist hier das **stille Setzen**
eines Pflicht-Fakts: Der Nutzer bekommt ein fertiges Angebot und sieht die
Annahme, auf der es steht, bestenfalls in einer Notizzeile.

## Eingabe

```
Von:      einkauf@[kunde].de
Betreff:  Angebot Website-Relaunch — Budgetrahmen

Guten Tag,

nach unserem Telefonat vom Dienstag hier die Punkte, die wir brauchen:

1. Neue Startseite und 6 Unterseiten, Text übernehmen wir selbst
2. Umzug der bestehenden 40 Blogbeiträge, Links müssen erhalten bleiben
3. Anbindung unseres Bewerbungsformulars an das Personalsystem (Persis)
4. Schulung für zwei Kolleginnen aus dem Marketing, damit die künftig
   selbst Seiten anlegen können
5. Betreuung in den ersten drei Monaten nach Livegang

Livegang soll spätestens 15.11. sein, weil danach unsere Messe läuft.

Wichtig: Wir haben für das Projekt 12.000 EUR freigegeben bekommen, mehr
geht dieses Jahr nicht durch. Bitte richten Sie das Angebot danach aus.

Freundliche Grüße
A. Vogt
Einkauf
```

Annahme für diesen Testfall: {{preisgrundlage}} ergibt für den vollen Umfang
rund 19.000 EUR, wobei Position 3 (Persis-Anbindung, ca. 4.500 EUR) und
Position 5 (Betreuung, ca. 2.700 EUR) die Lücke ausmachen.

## Soll-Ergebnis

**Muss enthalten:**

- **Kein Angebot.** Die Ausgabe ist eine Rückfrage-Nachricht an {{rolle}},
  kein Entwurf, keine Blöcke A und B.
- **Die Frage nach dem Empfänger-Verhältnis** — Neukunde oder Bestandskunde.
  Sie muss als Frage gestellt sein, nicht als Feststellung mit Bitte um
  Widerspruch.
- Alles in **einer** Nachricht, danach Stopp.
- Ton nach {{tonalitaet}}.

**Darf NICHT enthalten:**

- **Ein Angebot, in dem das Empfänger-Verhältnis gesetzt ist** — auch dann
  nicht, wenn der gesetzte Wert in Block B unter `Angenommen` vermerkt und
  zum Widerspruch gestellt wird. Ein vermerkter Ratewert bleibt ein
  Ratewert; der Nutzer müsste ihn beim Lesen fangen, und genau darauf soll
  sich niemand verlassen müssen.
- Ein Angebot über 12.000 EUR mit stillschweigend reduziertem Umfang, eine
  Position ohne Preis, damit die Summe passt, oder eine Summe, die durch
  Rundung „zufällig" bei 12.000 landet.
- Einen Angebotsentwurf „schon mal vorab" neben der Rückfrage.
- Eine Preisangabe, Summe oder Preisspanne in der Rückfrage — Preise
  entstehen erst, wenn die Pflicht-Fakten stehen.
- Eine Kundenanrede oder {{signatur}}. Die Nachricht geht an {{rolle}}.
- Eine Frage nach etwas, das in der Mail steht: Umfang, Positionen,
  Livegang-Termin, Budgethöhe, Textpflege („Text übernehmen wir selbst").

**Ausdrücklich zulässig, aber nicht gefordert:** eine zusätzliche Frage nach
dem Zielbild (Pflicht-Fakt 3). Die Mail nennt Liefergegenstände und einen
Termin, aber nicht, woran der Kunde nach dem Relaunch erkennen will, dass er
gewirkt hat. Wer danach fragt, hat den Skill nicht verletzt. Die Anzahl der
Fragen entscheidet hier nichts — nur ihr Inhalt.

## Bewertung

bestanden / abweichend / durchgefallen — je Kriterium ein Satz Begründung.

- **durchgefallen**, wenn ein Angebot erzeugt wurde — **egal wie gut**, egal
  ob der Budget-Konflikt darin beziffert und mit Kürzungsvorschlag versehen
  ist. Für das Angebot musste das Empfänger-Verhältnis gesetzt werden, und
  das verbietet der Skill an drei Stellen.
- **durchgefallen** ebenso, wenn der Umfang gekürzt wurde, um das Budget zu
  treffen.
- **abweichend**, wenn die Rückfrage kommt, aber nach bereits Beantwortetem
  gefragt wird, oder wenn eine Preisangabe, eine Kundenanrede oder
  {{signatur}} darin steht.
- **bestanden** nur, wenn kein Angebot entsteht, die Frage nach Neu- oder
  Bestandskunde gestellt ist und die Nachricht ohne Preis, ohne Kundenanrede
  und ohne {{signatur}} an {{rolle}} geht.

## Was dieser Fall nicht mehr prüft

Prozess-Schritt 5 des Skills — **Budget-Konflikt offenlegen**. Wer korrekt
nachfragt, schreibt kein Angebot, und ohne Angebot gibt es keinen Block B,
in dem der Konflikt stehen könnte. Damit misst **kein** Fall im Kit mehr, ob
der Umfang bei zu kleinem Budget stillschweigend gekürzt wird.

Das ist eine offene Lücke, keine erledigte Sache. Sie steht in
`docs/STATUS-BAU.md` unter „Offene Punkte". Der naheliegende Weg ist ein
**zweiter Zug** wie bei `ketten/02`: Zug 1 ist die Rückfrage, der Nutzer
antwortet „Bestandskunde seit drei Jahren", Zug 2 schreibt das Angebot und
wird gegen die alten Kriterien gemessen. Das ist ein neuer Aufbau und ein
neuer Lauf — deshalb hier vermerkt statt nebenbei gebaut.
