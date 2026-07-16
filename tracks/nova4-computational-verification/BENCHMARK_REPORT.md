# Nova 4 Benchmark Report

Date: 2026-07-16

Environment: CPython 3.13.5, standard library only unless otherwise stated. Timings are engineering diagnostics, not mathematical claims.

## Exact factorial half-range profiles

Every target `0 <= x <= floor(sqrt(n!))` was computed for `1 <= n <= 13`. Both exact methods agreed on 109,947 targets. The `n=14` Method A run did not complete within 30 seconds and remains `unknown due to resource limits`.

## Nova 2 lattice audit

Every `3 <= n <= 10,000` completed in approximately 1.9 seconds.

## Nova 1 capacity and rainbow audits

The capacity sweep through `n=1,000,000` completed in approximately 6.7 seconds with approximately 333 MB peak resident memory. The 61 reduced-rainbow cases completed in approximately 24.1 seconds with approximately 316 MiB peak resident memory.

## Nova 3 moments and local ceilings

The `2 <= n <= 12` audit completed in approximately 2.35 seconds with approximately 288 MiB peak resident memory, enumerating 1,978 exact divisors and checking 45,840 windows.

## Nova 3 scale evidence

Request C completed in approximately 8.55 seconds with approximately 300 MiB peak resident memory. It produced eight scale rows, 63 cutoff rows, and eight theorem-path rows.

## Nova 3 recurrence

Request D evaluated 19,990,010 scores. Generation completed in approximately 15.0 seconds and semantic recomputation in approximately 15.6 seconds, with approximately 300 MiB peak resident memory.

## Nova 3 source and Dusart audits

The restricted-source 10-test suite completed in approximately 0.004 seconds. The Dusart 12-test suite completed in approximately 0.13 seconds; artifact generation and replay each completed in approximately 1.3 seconds with approximately 305 MiB peak resident memory.

## Nova 3 exact threshold sweep

Request G checked 879,633 integers. Production completed in approximately 6.75 seconds with approximately 351,132 KiB peak resident memory. Twelve threshold tests completed in approximately 22.3 seconds.

## Nova 3 request H adversarial audit

Fourteen tests passed. Full audit replay completed in approximately 1.49 seconds, claim replay in approximately 1.34 seconds, and six-fixture replay in approximately 1.25 seconds. Peak resident memory was approximately 307 MiB.

## Nova 3 full-model variance limit

Thirteen tests passed. Audit replay completed in approximately 1.43 seconds, claim replay in approximately 1.33 seconds, and five-fixture replay in approximately 2.16 seconds. Peak resident memory was approximately 313,424 KiB.

## Nova 3 high-prime CLT and coarse-window theorem

The final `N3-ANA-008` and `N3-ANA-009` package generated independent finite diagnostics at:

```text
n=10,000      y=50    M/B=0.42704100199186046
n=100,000     y=158   M/B=0.28088934761914103
n=1,000,000   y=500   M/B=0.18044353517209441
n=10,000,000  y=1581  M/B=0.11145145759650005
```

The full-span ratio is exactly `2M/B`, confirming the earlier factor-of-two label diagnosis.

```text
isolated tests: 13 passing in approximately 23.36 seconds
audit replay: approximately 3.11 seconds
N3-ANA-008 claim replay: approximately 3.04 seconds
N3-ANA-009 claim replay: approximately 3.09 seconds
eight-fixture replay: approximately 9.62 seconds
peak resident memory: approximately 350,804 KiB
```

No timeout or unknown result occurred. The finite diagnostics are computational evidence only; the theorems come from the prime-band, Lindeberg, and Berry-Esseen proof reconstructions.

## Full-repository test status

All historical component suites have recorded passing runs, and the newly added high-prime suite passes in isolation. No GitHub Actions or other configured CI check currently runs the complete repository suite on the final branch head. A fresh complete full-repository replay remains an integration-gate requirement before merging into `main`.
