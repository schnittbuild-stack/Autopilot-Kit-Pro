# Platzhalter-Register (verbindlich)

Jeder Platzhalter, der in irgendeinem Skill vorkommt, steht hier — mit der
Interviewfrage, die ihn füllt. Neuer Platzhalter ohne Eintrag hier = Baufehler.

| Platzhalter | Gefüllt aus Frage | Inhalt |
|---|---|---|
| {{rolle}} | 1 | Job/Rolle des Nutzers |
| {{firma}} | 2 | Firma und Branche |
| {{nervaufgaben}} | 3 | Die drei wiederkehrenden Schmerzpunkte |
| {{tools}} | 4 | Genutzte Programme |
| {{tonalitaet}} | 5 + 9 | Förmlich/locker, abgeleitet aus Beispielen |
| {{anrede}} | 6 | Du/Sie gegenüber Kunden |
| {{signatur}} | 7 | E-Mail-Signatur wörtlich |
| {{verbote}} | 8 | No-Gos in Formulierung und Inhalt |
| {{stilbeispiele}} | 9 | Verweis auf abgelegte Beispiel-Mails |
| {{erfolgsmoment}} | 10 | Woran der Nutzer Erfolg misst (für Phase Beweis) |
| {{preisgrundlage}} | **noch keine — offen für Phase 3** | Wie der Nutzer Preise bildet: Stunden-/Tagessatz, Pauschalen, Preisliste, oder „gibt es nicht". Ohne diesen Wert markiert `angebots-schreiber` Preiszeilen mit `[PREIS PRÜFEN]` statt zu raten. |

## Offen

`{{preisgrundlage}}` wird von `angebots-schreiber` gebraucht, hat aber noch
keine Interviewfrage. In Phase 3 zu klären: als 11. Frage aufnehmen (bricht
das Limit von 10) oder als Zusatzfrage nur dann stellen, wenn ein
preisbildender Skill installiert wird. Empfehlung: bedingte Zusatzfrage —
sie betrifft nicht jeden Käufer, und das Interview soll kurz bleiben.
Solange offen, bleibt der Wert leer und der Skill markiert statt zu raten —
das ist ein funktionierender Zustand, kein Blocker.
