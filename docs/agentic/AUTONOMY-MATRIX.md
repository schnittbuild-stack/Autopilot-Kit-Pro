# Autonomy matrix

| Class | Example | Builder | Owner-Orchestrator | Final gate |
|---|---|---|---|---|
| A | Read, inspect, test | autonomous | autonomous | none |
| B | Ordinary repository-only code in allowlisted non-reserved paths | exact Work Order | integrate commits and request protected merge | PASS receipt + checks + exact-head owner comment |
| C | Deployment, provider write, data mutation or other live effect | forbidden without separate contract | plan only until exact human approval | human owner + live readback |
| D | Financial, legal, destructive, high-impact or irreversible action | forbidden | plan and escalate | human-controlled procedure |
| X | Secret exposure, protection bypass, direct main push, unbounded scope | forbidden | forbidden | no approval path in this framework |

Class B becomes reserved when it touches any configured reserved path. Classification follows
the highest-risk effect, including implicit effects such as a deployment triggered by merge.
