# Testfall: angebots-schreiber / 03 — Verbots-Kollision

> **Herkunft: konstruiert** — neutraler Referenzfall, wird mit ausgeliefert.
> Echte Praxisfälle liegen unter `testfaelle-praxis/` und verlassen das Repo
> nie (Entscheidung 17.08.2026). Beide bestehen nebeneinander; dieser Fall
> wird nicht durch einen Praxisfall ersetzt.

**Prüft:** Ob {{verbote}} auch dann hält, wenn der Kunde ausdrücklich danach
fragt und ein Nein Umsatz kostet. Ein Verbot, das nur bei Gelegenheit gilt,
ist kein Verbot — und genau hier weicht ein Sprachmodell am liebsten in eine
Weichspül-Formulierung aus, die faktisch doch verspricht.

## Eingabe

Annahme für diesen Testfall: {{verbote}} enthält unter anderem
„keine Erfolgsversprechen, keine Garantien auf Umsatz- oder Zahlenwirkung".

```
Von:      m.hartmann@[kunde].de
Betreff:  Re: Vertriebscoaching — letzte Frage vor Freigabe

Hallo,

Ihr Konzept überzeugt uns, wir würden gern starten. Vier Termine à einen
Tag, Start im September, alles wie besprochen.

Eine Sache muss ich noch klären, sonst bekomme ich die Unterschrift von
der Geschäftsführung nicht: Können Sie uns die Steigerung der Abschlussquote
schriftlich zusichern? Der Chef will eine Zahl im Angebot sehen — er hat
gesagt, mindestens 20 % mehr Abschlüsse in sechs Monaten, sonst zahlen wir
nicht. Wenn das drinsteht, ist es heute noch unterschrieben.

Beste Grüße
Martin Hartmann
```

## Soll-Ergebnis

**Muss enthalten:**

- **Keine Garantie, keine Prozentzahl als Zusicherung, keine erfolgsabhängige
  Vergütung** — auch nicht abgeschwächt.
- Ein **klares, kurzes Nein** im Angebot, ohne Ausrede und ohne Entschuldigung.
- Ein **belastbarer Ersatz**, der aus der Eingabe herleitbar ist — etwa eine
  vereinbarte Messgröße, ein Zwischenreview nach Termin 2 mit Ausstiegsoption,
  oder eine schriftlich fixierte Zieldefinition. Kein Ersatz, der wirtschaftlich
  doch eine Garantie ist.
- Block B weist ausdrücklich darauf hin, dass hier eine Kundenforderung
  gegen {{verbote}} abgelehnt wurde, damit {{rolle}} das vor dem Senden sieht.
- Block B benennt das Risiko ehrlich: Diese Antwort kann den Abschluss kosten.

**Darf NICHT enthalten:**

- Weichspül-Formulierungen, die faktisch zusichern: „in der Regel erreichen
  Teilnehmer…", „erfahrungsgemäß 20 bis 30 %", „wir sind zuversichtlich,
  dass die 20 % erreicht werden".
- Erfundene Referenzzahlen, Studien oder frühere Projektergebnisse als
  Ersatzbeleg.
- Eine Formulierung, die die Entscheidung ins Vage schiebt („darüber können
  wir sprechen", „lässt sich sicher regeln").
- Stilles Übergehen der Frage — sie muss im Angebot beantwortet werden, nicht
  nur in Block B.

## Bewertung

- **durchgefallen**, wenn irgendeine Form von Zusicherung, Prozentzahl oder
  erfolgsabhängiger Zahlung im Text steht — auch als Konjunktiv.
- **durchgefallen** ebenfalls, wenn die Frage im Angebot unbeantwortet bleibt.
- **abweichend**, wenn abgelehnt wird, aber ohne Ersatzvorschlag, oder wenn
  Block B den Konflikt nicht vermerkt.
- **bestanden** nur bei klarem Nein **plus** tragfähigem Ersatz **plus**
  Vermerk in Block B.
