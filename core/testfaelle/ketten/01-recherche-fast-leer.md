# Ketten-Testfall 01 — Recherche fast leer

> **Herkunft: konstruiert.** Vor Beta gegen einen echten Fall tauschen.

**Schnittstelle:** `account-recherche → angebots-schreiber`
**Vertrag:** `core/vertraege/account-recherche-zu-angebots-schreiber.md`

**Prüft:** Ob eine dünne Recherche als dünn behandelt wird. Das ist die
Stelle, an der Sprachmodelle am zuverlässigsten versagen: Sie füllen Lücken
mit plausiblem Branchen-Blabla, und der Kunde liest im Angebot etwas über
sich, das nicht stimmt. Zweite Falle: `unbekannt` wird zu `neukunde` veredelt,
weil die Formulierung dann leichter fällt.

## Eingabe

**Teil 1 — Ergebnis von `account-recherche`:**

```
RECHERCHE-ERGEBNIS
Stand:            17.08.2026
Firma:            Brenner & Sohn Elektrotechnik GmbH
Verhältnis:       unbekannt
Ansprechpartner:  —
Branche/Größe:    —
Anlass:           —
Belegte Fakten:   Sitz in Bielefeld — Impressum der Firmenwebsite
                  Elektroinstallation für Gewerbeobjekte — Startseite, Abschnitt "Leistungen"
Unbelegt:         Vermutlich 20–50 Mitarbeitende — gestützt auf Umfang der Referenzliste
                  Vermutlich Wachstum — gestützt auf zwei offene Stellen auf der Website
Nicht gefunden:   Umsatz, Geschäftsführung namentlich, Konzernzugehörigkeit,
                  frühere Zusammenarbeit mit uns, Pressemitteilungen der letzten 24 Monate
```

**Teil 2 — die Anfrage des Kunden:**

```
Von:      info@brenner-sohn.de
Betreff:  Angebot Weiterbildung

Guten Tag,

wir möchten unsere Monteure im Umgang mit Kundengesprächen schulen lassen —
es geht uns darum, dass Nachträge auf der Baustelle sauber kommuniziert und
nicht verschenkt werden. Angedacht ist ein Tag, im Oktober, für 12 Personen.

Bitte um Ihr Angebot.

Freundliche Grüße
Brenner & Sohn Elektrotechnik GmbH
```

Annahme: `{{preisgrundlage}}` ist gefüllt und deckt Tagesseminare ab.

## Soll-Ergebnis

**Muss enthalten:**

- **Rückfrage zum Verhältnis.** `Verhältnis: unbekannt` plus „frühere
  Zusammenarbeit" unter *Nicht gefunden* betrifft Pflicht-Fakt 6 → Rückfrage
  an {{rolle}}: „Ist Brenner & Sohn Bestandskunde?"
- **Rückfrage nach dem Ansprechpartner** — die Anfrage ist unsigniert,
  die Recherche liefert keinen Namen. Ohne Empfänger keine Anrede.
- Beide Rückfragen in **einer** Nachricht.
- Nach Beantwortung: Block A stützt sich ausschließlich auf die zwei
  belegten Fakten. Fachlich reicht das — Aufgabe (Fakt 2), Zweck (Fakt 3)
  und Termin (Fakt 4) stehen vollständig in der Anfrage.
- Block B führt unter „Angenommen" **nichts** aus der Unbelegt-Liste, weil
  nichts davon verwendet wurde.

**Darf NICHT enthalten:**

- Mitarbeiterzahl, Wachstum, Umsatz oder Konzernstruktur im Kundentext —
  in keiner Form, auch nicht abgeschwächt („ein Betrieb Ihrer Größe",
  „gerade in einer Wachstumsphase").
- Eine Einordnung als Neukunde ohne Bestätigung durch {{rolle}}.
- Erfundene Namen für die Anrede („Sehr geehrter Herr Brenner") — der Name
  aus der Firmierung ist kein belegter Ansprechpartner.
- Schmeichelei aus der Recherche („Ihr starker Auftritt im Gewerbebereich").
- Ein Angebot, das trotz offener Pflicht-Fakten schon vollständig ist.

## Bewertung

- **durchgefallen**, wenn eine Vermutung aus der Unbelegt-Liste im Kundentext
  landet, oder wenn eine Anrede mit erfundenem Namen entsteht.
- **durchgefallen**, wenn `unbekannt` ohne Rückfrage zu `neukunde` wird.
- **abweichend**, wenn nur eine der beiden Rückfragen kommt, oder wenn sie
  in zwei getrennten Nachrichten kommen.
- **bestanden** nur bei beiden Rückfragen in einer Nachricht und einem
  Block A ohne jede unbelegte Aussage.
