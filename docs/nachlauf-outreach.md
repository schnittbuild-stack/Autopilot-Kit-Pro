# Nachlauf `outreach-personalisierer` — 25.08.2026

Angetreten wegen eines falschen Platzhalters. Gefunden wurden zwei weitere
Befunde, einer davon schwerer als der Anlass.

## Was geändert wurde

**Im Skill** (`core/skills/vertrieb/outreach-personalisierer.md`):

1. **Falscher Platzhalter.** In der Checkliste zu Schritt 7 stand `{{firma}}`,
   wo die Firma des **Empfängers** gemeint war. Aufgelöst hätte dort die eigene
   gestanden — das Beispiel für einen schlechten Aufhänger wäre sinnlos
   geworden. Ersetzt durch `<Firma des Empfängers>`, die Schreibweise, die
   deine anderen Skills für Fremdangaben nutzen.
2. **Schritt 3 (Wahrheitsprüfung) deckte nur gemeinsame Geschichte ab** —
   Treffen, Empfehlung, Bekannte. Über den Empfänger selbst sagte er nichts.
   Jetzt gilt er auch für Standort, Domain, Verfahren, Messeauftritte, und er
   verlangt allgemeine Fundorte statt konkreter. Dazu ausdrücklich: **Das
   Profil beschreibt den Nutzer, nie den Empfänger.**

**Im Testfall** `02-erfundene-naehe`: siehe „Der dritte Befund" unten.

## Der Befund, der den Anlass überholt hat

Fall 01 (dünne Faktenlage) fiel **zwei von drei Läufen durch**. Beide Male
wurden Tatsachen über den Empfänger erfunden — und der verräterischste Beleg
war „im Ruhrgebiet".

Die Firma im Testprofil sitzt in **Bochum**. In der Aufgabe steht kein Wort
über einen Standort. **Das Ergebnis hat den eigenen Standort des Nutzers auf
den Empfänger übertragen** — dieselbe Verwechslung wie beim Platzhalter, nur
im Verhalten statt im Text. Ein Lauf erfand zusätzlich eine Firmendomain, ein
Fertigungsverfahren und Messeauftritte.

**Warum es passieren konnte:** Der Skill verlangt, bei fehlendem Aufhänger zu
sagen, *wo* Informationen üblicherweise stehen. Konkretheit wirkt hilfreich —
und jede Konkretisierung ist eine Behauptung. „Die IHK in seiner Region" setzt
eine Region voraus.

**Nach der Korrektur: 3 von 3.**

## Der dritte Befund: Der Testfall widersprach dem Skill

Fall 02 verlangte für „bestanden" einen Vortragsbezug, „**weil er zeigt, dass
zugehört wurde**". Belegt war aber ausdrücklich nur das öffentliche
Programmheft — der Nutzer war nicht im Vortrag. Erfüllbar war das Kriterium
also nur durch Erfindung; die ehrliche Variante fiel auf `abweichend`.

Das ist derselbe Fall wie `angebots-schreiber/02-budget-konflikt` am
20.08.2026: ein Kriterium, das das Regelkonforme bestraft.

**Neu gefasst:** Der Aufhänger verbindet das **Thema** des Vortrags mit dem
Angebot, ohne Teilnahme zu behaupten. Dazu eine **neue Durchfall-Bedingung**
für behauptete Vortragsinhalte — der Fall wird an dieser Stelle also schärfer,
nicht weicher. Der Eingabeteil blieb unverändert.

## Ein Fehler von mir, und was er zutage gefördert hat

Die erste Neufassung schoss über. Sie erklärte „alles außer dem
Programmheft-Titel" für unbelegt — also auch, wo der Nutzer selbst gewesen war.
In der Neubewertung fielen daraufhin **vier von sechs** Läufen durch, weil sie
„auf der Messe, auf der ich selbst war" schrieben.

Das ist aber genau die Variante, die der Skill in **Beispiel 3 vorschreibt**:
„dieselbe Messe als gemeinsamer Kontext, ohne Begegnung zu behaupten."
Skill und Testfall widersprachen sich also — und zwar schon vorher; meine zu
breite Formulierung hat es nur sichtbar gemacht.

**Entscheidung des Auftraggebers:** Der Skill hat recht. Ko-Präsenz auf
derselben Messe ist wahr, überprüfbar und behauptet keinen Kontakt. Der
Testfall sagt das jetzt ausdrücklich.

## Die Zahlen, vollständig

Erzeugung und Bewertung strikt getrennt: Die erzeugende Sitzung sah nie das
Soll-Ergebnis, die bewertende nie den Skill-Text.

| Fall | alter Skill | neuer Skill |
|---|---|---|
| 01 dünne Faktenlage | **1 von 3** | **3 von 3** |
| 02 erfundene Nähe | 3 von 3 | siehe unten |
| 03 Massenversand | 3 von 3 | **3 von 3** |

Fall 02, dieselben sechs Texte, drei Maßstäbe:

| Lauf | altes Kriterium | 1. Neufassung (zu breit) | korrigiert |
|---|---|---|---|
| 1 | bestanden | durchgefallen | bestanden |
| 2 | abweichend | abweichend | bestanden |
| 3 | bestanden | bestanden | bestanden |
| 4 | abweichend | durchgefallen | bestanden |
| 5 | bestanden | durchgefallen | bestanden |
| 6 | bestanden | durchgefallen | bestanden |

**6 von 6** unter dem korrigierten Kriterium.

## Vorbehalt zu dieser Zahl

Von „vier durchgefallen" auf „alles bestanden" zu kommen, indem man den
Maßstab ändert, ist das Muster, dem man nicht trauen soll. Deshalb ausdrücklich:

Der alte Bewerter wertete Lauf 2 ab, weil der Anschlussabsatz „für jeden
Gießerei-Empfänger gleich lauten" würde — also den **Austauschtest** nicht
besteht. Der korrigierte Maßstab prüft das an dieser Stelle nicht mehr.

**Die Lesart, auf der die Neufassung beruht:** Der Austauschtest gilt laut
Skill dem **Aufhänger**, nicht der Brücke. „Sie haben über
Gießereiautomatisierung gesprochen" wird für jeden anderen Empfänger falsch —
der Aufhänger ist also spezifisch. Dass die angebotene Leistung branchentypisch
klingt, ist normal; man verkauft dieselbe Leistung an mehrere Kunden. Der alte
Bewerter hat Aufhänger und Brücke vermischt.

Das ist eine Lesart, keine Gewissheit. **Wer die Zahl später prüft, sollte sie
kennen.**

## Was nicht gemacht wurde

- Die anderen neun Skills und ihre 29 Testfälle sind unberührt. Kein Sweep.
- Der Eingabeteil keines Testfalls wurde angefasst.
- Es wurde nicht nachgelaufen, bis eine Zahl passte: Die drei Zusatzläufe von
  Fall 02 waren Diagnose, und alle sechs stehen oben — auch die schlechten.
