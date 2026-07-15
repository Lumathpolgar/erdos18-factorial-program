# Nova 4 Status

Date: 2026-07-15

## Track

Computation, Falsification, and Verification

## Branch

`nova/computational-verification`

## Overall state

`FIRST_EXACT_CHECKPOINT_BUILT`

## Active results

| ID | Result class | Exact statement | Artifact |
|---|---|---|---|
| N4-CMP-001 | `exact finite theorem audit` | Exact `lambda_{n!}(x)` for every `1 <= n <= 13` and `0 <= x <= floor(sqrt(n!))` | `data/factorial_half_range_summary_n1_n13.json` and deterministic generator |
| N4-CMP-002 | `exact finite theorem audit` | Method A and Method B agree on all 109,947 tested targets | `SEARCH_METHODS.md` and dataset replay |
| N4-VER-001 | `finite certificate` | Universal representation certificate verifier is fail-closed | `src/factorial_lab/certificates.py` |
| N4-CE-001 | `counterexample` | Descending greedy is suboptimal at `n=8, x=155` | `certificates/n8_target155_optimal.json` |
| N4-LIM-001 | `unknown due to resource limits` | Exact Method A profile for `n=14` did not finish in 30 seconds | `BENCHMARK_REPORT.md` |

## Exact finite coverage

```text
n range: 1 through 13
targets checked: 109,947
arithmetic: exact integers
optimality checks: two independent exact methods
representation certificates: 14
corrupted fixtures required to fail: 5
unit tests: 21 passing
```

## Current limitations

- No asymptotic theorem is proved.
- No Track B source package is present for reconstruction.
- Formal handoffs from Novas 1, 2, and 3 were received after the initial dataset build and are queued by exact commit SHA.
- Those handoffs have been inspected but not yet independently executed or accepted.
- The full detailed profile JSON is reproducibly generated and checksummed; the compact first-checkpoint summary is committed.

## Next audit target

Implement the Nova 2 exact lattice and residue gate and reproduce the frozen `N2-OBS-107` obstruction. Then run Nova 1 capacity and reduced-rainbow studies, followed by Nova 3 independent theorem audits.
