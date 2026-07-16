# Nova 4 Status

Date: 2026-07-16

## Track

Computation, Falsification, and Verification

## Branch

`nova/computational-verification`

## Overall state

`NOVA3_REQUEST_G_THRESHOLD_SWEEP_COMPLETE`

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
| N4-AUD-005 | `finite certificate` | `N3-ANA-004` and `N3-ANA-005` independently reconstructed and accepted; exact finite moments and local ceilings replayed for every `2 <= n <= 12` | `audits/N3_MOMENT_LOCAL_CEILING_AUDIT.md` |
| N4-AUD-006 | `computational evidence` | Nova 3 request C scale rows, low-prime shares, effective dimension, and high-prime tail grid independently generated | `audits/N3_SCALE_CONVERGENCE_AUDIT.md` |
| N4-AUD-007 | `proved theorem audit` and `computational evidence` | `N3-ANA-007` independently reconstructed and accepted; request D scanned 19,990,010 bounded recurrence scores | `audits/N3_CHARACTERISTIC_RECURRENCE_AUDIT.md` |
| N4-AUD-008 | `source compatibility audit` | Ford, Drappeau–Tenenbaum, and ultrafriable source scopes reconstructed; none directly selects the factorial sequence | `audits/N3_RESTRICTED_SOURCE_COMPATIBILITY_AUDIT.md` |
| N4-AUD-009 | `primary-source theorem audit` | Dusart Theorem 6.9 and the algebra proving `N3-ANA-010` independently reconstructed and accepted | `audits/N3_DUSART_PRIME_INTERVAL_AUDIT.md` |
| N4-AUD-010 | `finite certificate` | Every integer `120368 <= n <= 1000000` passes the exact prime, Legendre, ceiling, address, and conservative profile-capacity checks | `audits/N3_THRESHOLD_SWEEP_AUDIT.md` |
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
Nova 3 moment audit: every n = 2 through 12
Nova 3 exact divisors enumerated: 1,978
Nova 3 local windows checked: 45,840
Nova 3 scale rows: 8
Nova 3 high-prime cutoff rows: 63
Nova 3 theorem-path rows: 8
Nova 3 recurrence scores: 19,990,010
Nova 3 restricted primary sources reconstructed: 3
Nova 3 source-compatibility witnesses: 3
Dusart primary theorem reconstructed: Theorem 6.9, equation (6.6)
Dusart threshold witness: pi(120368)-pi(60184) = 5254
Nova 3 request G integers checked: 879,633
certified r_n transitions in request G: 10
certified M_n transitions in request G: 865
new Nova 3 source tests: 10 passing
new Nova 3 Dusart tests: 12 passing
new Nova 3 threshold-sweep tests: 12 passing
arithmetic: exact integers, rational logarithm bounds, exact prime counts, dual Legendre identities, 80-digit finalist evaluation, and semantic replay
```

## Current limitations

- No asymptotic factorial half-range theorem is proved.
- The accepted Nova 2 obstruction applies only to the frozen Nova 1 model at commit `b939574eb88a08bb03abda5bbe6ff2ca97444e08`.
- The reduced-rainbow disproof applies only to Study B at Nova 1 commit `fa11f4b2cb86a2dd791df189ada12757be791804`; it does not disprove the full-menu preferred route.
- Nova 3 request C is computational evidence only. `N3-ANA-006` and `N3-ANA-008` remain theorem-audit pending.
- Request D does not prove a quantitative recurrence rate or certify a maximum outside its grid.
- Request E confirms source scope only. It does not reprove the cited papers or establish a deterministic factorial divisor law.
- Request G is a finite certificate. It confirms the requested range but does not establish profile injectivity or additive occupancy.
- Final theorem-status disposition for `N3-ANA-011` remains pending request H's adversarial semantic audit.
- No Track B source package is present for reconstruction.
- The `n=14` exact representation profile remains unknown due to resource limits.

## Next audit target

Run request H of superseding Nova 3 handoff `N3-HO-N4-002`: reject all six specified semantic corruptions, including larger unproved address ranges, removal of the menu-unit exclusion, profile-count versus distinct-sum conflation, the `pi(ceil(n/2))` endpoint substitution, and reporting the finite sweep as an asymptotic proof.
