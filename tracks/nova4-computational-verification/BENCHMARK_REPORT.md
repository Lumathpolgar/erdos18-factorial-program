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

Request E reconstructed three primary source scopes and generated three exact compatibility witnesses. The standalone 10-test suite completed in approximately 0.004 seconds. Full audit replay and compatibility-claim replay passed. No timeout or unknown result occurred.

## Nova 3 Dusart primary-source audit

Request F reconstructed Theorem 6.9, equation (6.6), and independently certified the algebra for `N3-ANA-010`.

```text
source lower threshold: 5393
source upper threshold: 60184
derived integer threshold: 120368
pi(120368): 11330
pi(60184): 6076
upper-half prime count: 5254
```

The 12-test suite completed in approximately 0.13 seconds. Artifact generation completed in approximately 1.27 seconds and full semantic replay in approximately 1.29 seconds, with peak resident memory approximately 305 MiB. No timeout or unknown result occurred.

## Nova 3 exact threshold sweep

Request G checked all 879,633 integers in `120368 <= n <= 1000000`.

```text
exact upper-half prime counts: every n
exact v_2(n!): Legendre division and n-bit_count(n)
certified r_n transitions: 10
certified M_n transitions: 865
minimum prime margin: n=120370
minimum Legendre proof margin: n=131071
minimum address slack: 57942 at n=120368..120371
minimum conservative capacity margin: n=120370
```

The production sweep completed in approximately 6.75 seconds with peak resident memory approximately 351132 KiB. Twelve threshold-sweep tests passed in approximately 22.3 seconds when the full sweep was generated once and semantically replayed again. The committed rehashed false minimum-slack fixture was rejected. No timeout or unknown result occurred.

All discrete quantities in request G are exact. Margin rankings use a complete binary64 screening pass followed by 80-digit Decimal replay of the retained minima and runners-up. The finite sweep is not an asymptotic proof or an additive-occupancy result.
