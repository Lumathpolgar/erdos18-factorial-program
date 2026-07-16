# Nova 4 Status

Date: 2026-07-15

## Track

Computation, Falsification, and Verification

## Branch

`nova/computational-verification`

## Overall state

`NOVA3_MOMENT_LOCAL_AUDIT_COMPLETE`

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
previous complete unit suite: 39 passing
new reduced-rainbow tests: 11 passing
new Nova 3 moment/local tests: 10 passing
on-disk corrupted fixtures required to fail: 12
arithmetic: exact integers, exact rational identities, rational interval bounds, and 80-digit decimal replay
```

## Current limitations

- No asymptotic factorial half-range theorem is proved.
- The accepted Nova 2 obstruction applies only to the frozen Nova 1 model at commit `b939574eb88a08bb03abda5bbe6ff2ca97444e08`.
- The reduced-rainbow disproof applies only to Study B at Nova 1 commit `fa11f4b2cb86a2dd791df189ada12757be791804`; it does not disprove the full-menu preferred route.
- The formal-profile compression statistic for Study B is a truncated-support diagnostic, not a pure collision probability.
- Nova 3 results `N3-ANA-006` through `N3-ANA-009` remain unaudited.
- No Track B source package is present for reconstruction.
- The `n=14` exact representation profile remains unknown due to resource limits.

## Next audit target

Run request C of Nova 3 handoff `N3-HO-N4-001`: independently generate the scale-convergence table, variance shares, participation ratio, and high-prime `M_{n,y}/B_{n,y}` grid, labeled `COMPUTATIONAL_EVIDENCE`.
