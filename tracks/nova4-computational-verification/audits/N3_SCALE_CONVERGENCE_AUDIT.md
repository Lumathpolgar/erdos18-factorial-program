# Nova 3 Scale-Convergence and High-Prime Tail Audit

Date: 2026-07-15

## Frozen source

- repository: `Lumathpolgar/erdos18-factorial-program`
- branch: `nova/analytic-density`
- commit: `0ce88b28dc2e6641093526f5777bb31f658e3515`
- handoff: `N3-HO-N4-001`
- request: C

No later Nova 3 revision is included.

## Decisions

| Object | Decision | Scope |
|---|---|---|
| Request C scale table | `ACCEPTED_AS_COMPUTATIONAL_EVIDENCE` | Exact valuations with 80-digit Decimal evaluation |
| `N3-ANA-006` | `EVIDENCE_CONSISTENT, THEOREM NOT YET ACCEPTED` | Variance convergence evidence only |
| `N3-ANA-008` | `EVIDENCE_CONSISTENT, THEOREM NOT YET ACCEPTED` | High-prime tail evidence only |
| Frozen `scale_sanity.py` scale rows | `ACCEPTED_WITH_FLOATING_TOLERANCE` | Maximum independent difference below `1.6e-15` |
| Frozen `scale_sanity.py` tail-ratio label | `NEEDS_REPAIR` | The script computes twice the theorem-defined ratio |

## Finite domain

Scale rows were generated for:

```text
n = 50, 100, 200, 500, 1000, 2000, 5000, 10000
```

For each row Nova 4 recomputes:

- `log tau(n!)/(n/log n)`;
- `Var(S_n)/n^2`;
- variance shares of primes `2`, `3`, `5`, and `7`;
- participation-ratio effective dimension;
- exact factorial valuations by Legendre's formula.

The cutoff grid is:

```text
y = 2, 3, 5, 7, 10, 20, 25, 50
```

This gives 63 nonempty high-prime tail rows. Every row records whether `2y<=sqrt(n)`. A separate eight-row path uses `y_n=floor(sqrt(n))/2`, so every path row satisfies that scale condition.

## Variance evidence

The one-million-prime truncated proxy for

```text
(1/12) sum_p (log p)^2/(p-1)^2
```

is:

```text
0.115465835230529902456952892434742827354191666300733
```

This is a numerical proxy, not a certified evaluation of the infinite sum.

Selected rows:

| n | Var(S_n)/n^2 | ratio to proxy |
|---:|---:|---:|
| 50 | 0.1055848456162383 | 0.9144249933795224 |
| 100 | 0.1113706593264075 | 0.9645334405978507 |
| 500 | 0.1143125576334303 | 0.9900119581277263 |
| 1000 | 0.1148521217761896 | 0.9946848913956671 |
| 5000 | 0.1154132776328928 | 0.9995448212232460 |
| 10000 | 0.1154476862555886 | 0.9998428195240168 |

The finite sequence is consistent with the variance limit claimed in `N3-ANA-006`. No convergence rate is inferred.

## Low-prime concentration

At `n=10000`, the variance shares are approximately:

```text
p=2: 0.3465268838391148
p=3: 0.2175409932740782
p=5: 0.1168589348212424
p=7: 0.0758628098897731
combined: 0.7567896218242085
```

The participation-ratio effective dimension is approximately `5.23116`. These are finite diagnostics of low-prime dominance, not proof of a limiting distribution.

## High-prime path

Along `y_n=floor(sqrt(n))/2`, the theorem-defined `M_{n,y}/B_{n,y}` values are:

| n | y_n | M/B |
|---:|---:|---:|
| 50 | 3 | 0.8865284354970372 |
| 100 | 5 | 0.8283994852640456 |
| 200 | 7 | 0.6883910255973406 |
| 500 | 11 | 0.6713612708509065 |
| 1000 | 15 | 0.6155634327578450 |
| 2000 | 22 | 0.5731324110830504 |
| 5000 | 35 | 0.4808909749859144 |
| 10000 | 50 | 0.4270410019918603 |

This is consistent with decay but does not prove `M_{n,y}/B_{n,y}->0`.

## Supplied-script discrepancy

`N3-ANA-008` defines:

```text
M_{n,y} = max_{p>y} b_p log(p)/2.
```

The frozen script instead maximizes `b_p log(p)` and divides by `B_{n,y}`. Its printed tail values are therefore exactly:

```text
2 M_{n,y}/B_{n,y}.
```

The independent implementation reproduced all nine frozen printed tail calculations with maximum absolute difference below `2.3e-15`, and the scale-row fields with maximum difference below `1.6e-15`. The script output label requires repair. The theorem statement itself is not contradicted by this implementation issue.

## Artifacts and replay

Committed exact projections and checksums are indexed by:

```text
data/analytic/n3_scale_evidence_index.json
```

The full deterministic generated audit has semantic SHA-256:

```text
28bd8b9a6aeb3c2f4771c1bb861c0fc0f04f9e521982f56763ebac72e220cd94
```

Its generated JSON file SHA-256 is:

```text
a9c15706bed590d4fbad1845bb0901ddee2c40fa19bff1f8aaac7120673998f6
```

## Validation

- 13 new tests passed;
- full semantic replay passed;
- eight scale rows, 63 cutoff rows, and eight theorem-path rows recompute deterministically;
- rehashed tail-ratio corruption is rejected;
- rehashed variance-share corruption is rejected;
- wrong frozen-source metadata is rejected;
- generation completed in approximately 8.55 seconds;
- peak resident memory was approximately 300 MiB;
- no timeout or unknown result occurred.

## Scope restriction

This checkpoint is computational evidence. It does not accept the asymptotic proofs of `N3-ANA-006` or `N3-ANA-008`, establish a convergence rate, imply additive divisor-sum coverage, or prove the factorial half-range theorem.

## Next target

Run request D from `N3-HO-N4-001`: search bounded frequency ranges for simultaneous characteristic-function recurrences, record the range and precision, and label every finding computational evidence.
