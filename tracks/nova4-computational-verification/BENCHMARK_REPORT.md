# Nova 4 Benchmark Report

Date: 2026-07-16

Environment: CPython 3.13.5, standard library only unless otherwise stated. Timings are engineering diagnostics, not mathematical claims.

## Exact factorial half-range profiles

Every target `0 <= x <= floor(sqrt(n!))` was computed for `1 <= n <= 13`. Both exact methods agreed on 109,947 targets.

Exact values:

```text
H = 1 for 1 <= n <= 4
H = 2 for 5 <= n <= 7
H = 3 for 8 <= n <= 13
```

The `n=14` Method A run did not complete within 30 seconds and remains `unknown due to resource limits`.

## Nova 2 lattice audit

The exact transition audit for every `3 <= n <= 10,000` completed in approximately 1.9 seconds.

## Nova 1 capacity audit

The exact audit of all 999,998 integers in `3 <= n <= 1,000,000` completed in approximately 6.7 seconds with approximately 333 MB peak resident memory.

## Nova 1 reduced-rainbow audit

All 61 cases in `20 <= n <= 80` completed in approximately 24.1 seconds with approximately 316 MiB peak resident memory. Eleven reduced-rainbow tests passed.

## Nova 3 moment and local-ceiling audit

The audit for `2 <= n <= 12` completed in approximately 2.35 seconds with approximately 288 MiB peak resident memory. It enumerated 1,978 exact divisors and checked 45,840 local windows. Ten tests passed.

## Nova 3 scale evidence

Request C generation completed in approximately 8.55 seconds with approximately 300 MiB peak resident memory. It produced eight scale rows, 63 cutoff-grid rows, eight theorem-path rows, and a one-million-prime proxy. Thirteen tests passed.

## Nova 3 characteristic recurrence

Request D evaluated 19,990,010 bounded characteristic-function scores. Production generation completed in approximately 15.0 seconds and full semantic recomputation in approximately 15.6 seconds, with approximately 300 MiB peak resident memory. Twelve tests passed.

## Nova 3 restricted-source compatibility audit

Request E reconstructed three primary source scopes and generated three exact compatibility witnesses:

```text
Ford ambient-vs-fixed witness: H(120,6,7)=17, tau(120;6,7)=0
friable scope witness: 10! belongs to S(10!,10), no nonexceptionality certificate
ultrafriable mismatch: v_2(10!)=8, required 256, excluded prime 11
```

The standalone 10-test suite completed in approximately 0.004 seconds. Full audit replay and compatibility-claim replay passed. The committed rehashed false-direct-use fixture was rejected. No timeout or unknown result occurred.

The source audit uses exact integers and deterministic semantic replay. Reading and interpreting the primary papers is a proof-scope activity, not a performance benchmark.