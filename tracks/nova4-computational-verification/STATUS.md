# Nova 4 Status

Date: 2026-07-16

## Track

Computation, Falsification, and Verification

## Branch

`nova/computational-verification`

## Overall state

`NOVA3_THEOREM_AUDITS_COMPLETE_INTEGRATION_GATE_ACTIVE`

## Active results

| ID | Result class | Exact statement | Artifact |
|---|---|---|---|
| N4-CMP-001 | `exact finite theorem audit` | Exact `lambda_{n!}(x)` for every `1 <= n <= 13` and `0 <= x <= floor(sqrt(n!))` | `data/factorial_half_range_summary_n1_n13.json` and deterministic generator |
| N4-CMP-002 | `exact finite theorem audit` | Two independent exact methods agree on all 109,947 tested targets | `SEARCH_METHODS.md` and dataset replay |
| N4-VER-001 | `finite certificate` | Universal representation certificate verifier is fail-closed | `src/factorial_lab/certificates.py` |
| N4-VER-004 | `finite certificate` | Explicit label families are checked for legality, collisions, gcd, residues, and exact window coverage | `src/factorial_lab/lattice.py` |
| N4-AUD-002 | `exact finite theorem audit` | `N2-ADD-115` and `N2-OBS-107` independently reconstructed and accepted for the frozen model | `audits/N2_ADD_115_LATTICE_AUDIT.md` |
| N4-AUD-003 | `exact finite theorem audit` | Nova 1 capacity predicates audited for every `3 <= n <= 1,000,000` | `audits/N1_CAPACITY_THRESHOLD_AUDIT.md` |
| N4-AUD-004 | `computational evidence` | Exact reduced-rainbow support, profiles, residues, gaps, and witnesses computed for every `20 <= n <= 80` | `audits/N1_REDUCED_RAINBOW_AUDIT.md` |
| N4-AUD-005 | `finite certificate` | `N3-ANA-004` and `N3-ANA-005` independently reconstructed and accepted | `audits/N3_MOMENT_LOCAL_CEILING_AUDIT.md` |
| N4-AUD-006 | `computational evidence` | Nova 3 request C scale evidence and factor-of-two tail-label diagnosis | `audits/N3_SCALE_CONVERGENCE_AUDIT.md` |
| N4-AUD-007 | `proved theorem audit` and `computational evidence` | `N3-ANA-007` accepted; request D scanned 19,990,010 bounded recurrence scores | `audits/N3_CHARACTERISTIC_RECURRENCE_AUDIT.md` |
| N4-AUD-008 | `source compatibility audit` | Three restricted source scopes reconstructed; none directly selects the factorial sequence | `audits/N3_RESTRICTED_SOURCE_COMPATIBILITY_AUDIT.md` |
| N4-AUD-009 | `primary-source theorem audit` | Dusart Theorem 6.9 and `N3-ANA-010` independently accepted | `audits/N3_DUSART_PRIME_INTERVAL_AUDIT.md` |
| N4-AUD-010 | `finite certificate` | Every integer `120368 <= n <= 1000000` passes the exact threshold sweep | `audits/N3_THRESHOLD_SWEEP_AUDIT.md` |
| N4-AUD-011 | `semantic adversarial theorem audit` | All six request H corruptions rejected and `N3-ANA-011` accepted with formal-profile-only scope | `audits/N3_THRESHOLD_ADVERSARIAL_AUDIT.md` |
| N4-AUD-012 | `proved theorem audit with finite diagnostics` | `N3-ANA-006` accepted: normalized variance and full non-Gaussian weak limit | `audits/N3_VARIANCE_LIMIT_AUDIT.md` |
| N4-AUD-013 | `proved and conditional theorem audits with finite diagnostics` | `N3-ANA-008` accepted and `N3-ANA-009` accepted with the exact Berry-Esseen dependency and coarse-window restriction | `audits/N3_HIGH_PRIME_LIMIT_AUDIT.md` |
| N4-CE-001 | `counterexample` | Descending greedy is suboptimal at `n=8, x=155` | `certificates/n8_target155_optimal.json` |
| N4-CE-002 | `disproved finite claim` | Frozen `N1-HO-N2-001` fails at its first requested target when admissible | `certificates/lattice/n2_obs_107_n1892.json` |
| N4-CE-003 | `disproved finite claim` | Every frozen reduced Study B model for `20 <= n <= 80` fails at its first requested target | `certificates/rainbow/n1_reduced_rainbow_first_failure_n20.json` |
| N4-LIM-001 | `unknown due to resource limits` | Exact Method A profile for `n=14` did not finish in 30 seconds | `BENCHMARK_REPORT.md` |

## Verified coverage

```text
factorial half-ranges: n = 1 through 13
representation targets: 109,947
N2 lattice transition audit: every n = 3 through 10,000
Nova 1 capacity audit: every n = 3 through 1,000,000
Nova 1 reduced-rainbow audit: every n = 20 through 80
Nova 3 exact divisors enumerated: 1,978
Nova 3 local windows checked: 45,840
Nova 3 recurrence scores: 19,990,010
Nova 3 request G integers checked: 879,633
N3-ANA-006 variance diagnostics: 10 rows through n=1,000,000
N3-ANA-008 diagnostics: 4 rows through n=10,000,000
request H semantic corruptions rejected: 6 of 6
N3-ANA-006 corruptions rejected: 5 of 5
N3-ANA-008/009 corruptions rejected: 8 of 8
new high-prime theorem tests: 13 passing
arithmetic: exact integers, rational logarithm bounds, exact prime counts, dual Legendre identities, elementary series tails, finite diagnostics, and semantic replay
```

## Current limitations

- No asymptotic factorial half-range theorem is proved.
- No artifact proves profile injectivity, distinct numerical sums, or additive occupancy.
- Request C remains computational evidence only; its frozen diagnostic reports `2M/B`, not theorem-defined `M/B`.
- `N3-ANA-006` proves the full model is non-Gaussian; `N3-ANA-008` proves only the separately truncated high-prime tail is asymptotically Gaussian.
- `N3-ANA-009` covers only coarse windows `Delta >= K M_{n,y}` and retains the external Berry-Esseen dependency.
- Request G remains a finite certificate rather than an asymptotic proof.
- No Track B source package is present for reconstruction.
- The `n=14` exact representation profile remains unknown due to resource limits.

## Integration gate

All theorem IDs requested in `N3-HO-N4-002` now have independent Nova 4 decisions. The branch is undergoing final merge-readiness checks for branch drift, complete replay availability, PR state, and integration policy. No merge is authorized by this status file.
