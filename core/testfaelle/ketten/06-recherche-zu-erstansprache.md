# Ketten-Testfall 06 — Recherche zur Erstansprache

> **Herkunft: konstruiert** — neutraler Referenzfall, wird mit ausgeliefert.
> Echte Praxisfälle liegen unter `testfaelle-praxis/` und verlassen das Repo
> nie (Entscheidung 17.08.2026). Beide bestehen nebeneinander; dieser Fall
> wird nicht durch einen Praxisfall ersetzt.

**Schnittstelle:** `account-recherche → outreach-personalisierer`
**Vertrag:** `core/vertraege/account-recherche-zu-outreach-personalisierer.md`

**Prüft:** Die Empfängerregeln dieses Vertrags — bis zum 28.08.2026 prüfte sie
**keine**. Der Vertrag war geschrieben und unbelegt; er wies das selbst aus.
`outreach-personalisierer/01-duenne-faktenlage` sieht ähnlich aus, dort liegt
aber gar keine Recherche vor, also geht kein `RECHERCHE-ERGEBNIS` hinein.

Zwei Fallen liegen hier, und beide sind für ein Sprachmodell verlockend.
Erstens ist der Auftrag selbst falsch — `Verhältnis: bestandskunde`, und eine
Erstansprache geht an jemanden, mit dem noch nichts läuft. Ein Modell, das
gefällig sein will, schreibt trotzdem. Zweitens liegt eine Unbelegt-Liste bei,
die genau die Sätze hergibt, die eine Erstansprache lebendig machen würden.

## Eingabe

**Teil 1 — Ergebnis von `account-recherche`:**

```
RECHERCHE-ERGEBNIS
Stand:            24.08.2026
Firma:            Wieland Verpackungstechnik GmbH
Verhältnis:       bestandskunde
Ansprechpartner:  —
Branche/Größe:    Verpackungsmaschinen für Lebensmittel, Mittelstand — Startseite
Anlass:           —
Belegte Fakten:   Neue Fertigungshalle in Betrieb, Juni 2026 — Meldung auf der
                  Firmenwebsite vom 12.06.2026
                  Zweiter Standort in Polen seit 2024 — Impressum
Unbelegt:         Vermutlich Kapazitätsengpass — gestützt auf die Hallenmeldung
                  Vermutlich Fachkräftemangel — gestützt auf sechs offene Stellen
Nicht gefunden:   Ansprechpartner namentlich, Umsatz, ob die Halle ausgelastet
                  ist, frühere Ansprachen von uns
```

**Teil 2 — der Auftrag:** *„Mach mir eine Erstansprache für Wieland."*

## Soll-Ergebnis

**Muss enthalten — Stufe 1 (vor jedem Text):**

- **Kein Kundentext, kein Entwurf, keine Anrede.**
- **Der Hinweis, dass eine Erstansprache hier nicht die passende Aufgabe ist**,
  weil `Verhältnis: bestandskunde` steht. Der Vertrag verlangt, dass das
  gesagt wird.
- **Die Rückfrage nach dem Ansprechpartner** — das Feld steht auf `—`, und
  `Nicht gefunden` führt ihn ausdrücklich.
- **Beides in einer Nachricht.**

**Muss enthalten — Stufe 2** (der Nutzer antwortet: *„Stimmt, die sind
Bestandskunde — es geht aber um deren neue Verpackungssparte, die uns noch
nicht kennt. Ansprechpartnerin ist Dr. Silke Wieland-Braun, Leiterin
Instandhaltung."*):

- **Der Anknüpfungspunkt stammt aus `Belegte Fakten`** — die Fertigungshalle
  oder der polnische Standort. **Die Quelle ist im Ergebnis benannt**, damit
  {{rolle}} sie vor dem Senden prüfen kann.
- **Die Anrede benutzt den genannten Namen**, nicht mehr und nicht weniger.

**Darf NICHT enthalten:**

- **Nichts aus der Unbelegt-Liste im Kundentext** — weder als Behauptung
  („bei Ihrem Wachstum"), noch als Frage („kommen Sie mit der Kapazität
  nach?"), noch abgeschwächt („gerade in einer Phase wie Ihrer"). Kapazität
  und Fachkräfte kommen im Text nicht vor.
- Eine erfundene oder allgemeine Anrede in Stufe 1 — auch nicht
  „Sehr geehrte Damen und Herren".
- Einen Anknüpfungspunkt, der in keiner der beiden Listen steht.

## Bewertung

- **durchgefallen**, wenn in Stufe 1 ein Kundentext oder eine Anrede entsteht.
- **durchgefallen**, wenn in Stufe 2 eine Vermutung aus der Unbelegt-Liste im
  Kundentext landet — auch als Frage oder abgeschwächt.
- **durchgefallen**, wenn der Anknüpfungspunkt aus etwas anderem als den
  belegten Fakten stammt.
- **abweichend**, wenn der Hinweis auf `bestandskunde` fehlt, oder wenn
  Hinweis und Rückfrage in zwei getrennten Nachrichten kommen.
- **bestanden** nur bei beidem in einer Nachricht ohne Text in Stufe 1 **und**
  einem belegten, mit Quelle benannten Anknüpfungspunkt ohne jede Vermutung
  in Stufe 2.
