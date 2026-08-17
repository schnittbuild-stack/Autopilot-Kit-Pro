# Entscheidungsprotokoll

| Datum | Entscheidung | Begründung |
|---|---|---|
| 14.08.2026 | Produkt: Autopilot Kit — Download, LLM des Käufers installiert sich selbst | Skalierbar, kein Abo-Zwang, kein FernUSG-Risiko (digitales Gut ohne Lernerfolgskontrolle) |
| 14.08.2026 | Zielgruppe V1: alle mit absolvierter KI-Schulung (After-Sales zur Schulung) | Größter Schmerz („Schulung gemacht — und jetzt?"), Konsequenz: ZIP-Pflichtweg, idiotensicherer Installer, Du-Ansprache |
| 14.08.2026 | V1 nur Claude Code; ChatGPT/Codex später als Adapter | Nur dort funktioniert Selbstinstallation vollständig; core/ bleibt plattformneutral |
| 14.08.2026 | Preis: 299 € Einführung, 499 € Anker | Genehmigungsfähig, unter Agentur-Setup (ab 1.850 €), Funnel-Mathematik |
| 14.08.2026 | GitHub = einzige Quelle der Wahrheit, Releases bauen das Kunden-ZIP | Struktur, Versionierung, kein Handbetrieb |
| 14.08.2026 | Keine API-Keys: Aufbau auf dem Claude-Abo des Kunden | Null laufende Kosten/Haftung; Keys nur optional für Drittsysteme, lokal in .env |
| 17.08.2026 | Hauptkette V1: `account-recherche → angebots-schreiber → follow-up-generator`, beide Übergaben optional, Format aber bindend | Deckt den häufigsten Vertriebsablauf ab (Kontext → Angebot → Nachfassen); optionale Übergaben, damit jeder Skill einzeln nutzbar bleibt |
| 17.08.2026 | Beide Verträge nach dem Muster „Unwissen ist ein Wert": `Unbelegt`/`Nicht gefunden`/`[PREIS PRÜFEN]`, Pflichtfelder notfalls als `—` | Ein fehlendes Feld ist von einem leeren nicht unterscheidbar — genau dort erfindet das Modell. Der Unterschied ist die Bruchstelle, die der Watchdog prüfen kann |
| 17.08.2026 | Skill-Beispiele in `core/` sind stilneutral, statt „5 echte Beispiele" wie im BAUPLAN | Echte Formulierungsbeispiele in core/ würden bei jedem Käufer denselben Hausstil erzwingen (Prinzip-1-Bruch). Stil kommt aus {{tonalitaet}}/{{stilbeispiele}} zur Installationszeit |
| 17.08.2026 | Repo-Heimat vorerst `schnittbuild-stack/Autopilot-Kit` (privat), nicht die Org `Autopilot-Kit` | Fine-grained Token war auf den User-Account ausgestellt; Org-Zugriff bräuchte neues Token + Repo. Transfer in die Org später per GitHub-Ownership-Transfer, alte URL bleibt per Redirect gültig |
