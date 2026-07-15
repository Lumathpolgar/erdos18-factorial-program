# Theorem Registry

This file is the authoritative index of frozen theorem, conjecture, and obstruction statements used across tracks.

## ID convention

```text
N1-STR-###   Factorial structure
N2-ADD-###   Additive occupancy
N3-ANA-###   Analytic density
N4-CMP-###   Computation or verification
INT-###      Integration theorem
HIST-###     Archived historical result
```

## Active registry

| ID | Status | Owner | Statement summary | Dependencies | Audit |
|---|---|---|---|---|---|
| INT-001 | OPEN | Integration | `h(n!) <= K(log n)^C` for absolute constants | Open chain | Not started |
| INT-002 | OPEN | Shared | `H_{n!}(floor(sqrt(n!))+1)=O((log n)^2)` | None accepted | Not started |
| HIST-001 | CONDITIONAL | Archive | INT-002 implies `h(n!)=O((log n)^3)` | INT-002 | Prior audit, reconstruction required |
| HIST-002 | OPEN | Archive | `H_{L_m}(floor(L_m^(1/3))+1)=O(log m)` | None | Historical route paused |
| HIST-012K | DISPROVED_ROUTE | Archive | Uniform entropy-scale entry mesh cannot start from the certified low scale | Historical package | Recorded |
| HIST-012L | DISPROVED_ROUTE | Archive | Maximum-gap greedy route cannot deliver `O(log m)` | Historical package | Recorded |
| HIST-012M | MIXED | Archive | Raw marker capacity survives; independent CRT and separable recursion fail | Historical package | Recorded |
| HIST-012N | DISPROVED_ROUTE | Archive | High-prime marker atlas has an additive shell gap | Historical package | Recorded |
| HIST-012O | FINITE_CERTIFICATE | Archive | Mixed-scale shared-core ladder succeeds on tested finite range | Historical package | Recorded |
| HIST-012P | DISPROVED_ROUTE | Archive | Sequential one-choice shared-core ladder requires superlogarithmic layers | Historical package | Recorded |

## Registration procedure

To add a result, provide:

- full theorem statement path;
- owner and version;
- status label from `docs/VERIFICATION_AND_EVIDENCE_STANDARD.md`;
- dependency IDs;
- proof or certificate path;
- audit result;
- superseded IDs, if any.

## Promotion rule

A conjecture becomes `PROVED` only after its proof is committed and independently reconstructed. A theorem used conditionally remains `CONDITIONAL` until every dependency is `PROVED`.
