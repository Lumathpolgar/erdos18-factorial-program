# Independent audit of N3-ANA-007 and request D

Date: 2026-07-15

## Frozen source

- repository: `Lumathpolgar/erdos18-factorial-program`
- branch: `nova/analytic-density`
- superseding handoff: `N3-HO-N4-002`
- handoff commit: `7469dada02fa4caca08ed391ef8b0cb0f1e855b2`
- proof commit: `ff57005b975c4917341306bd0eceb6d05a9b18f6`
- theorem: `N3-ANA-007`
- request: `D`

No later Nova 3 proof revision is included.

## Decisions

| Object | Decision | Basis |
|---|---|---|
| `N3-ANA-007` | `ACCEPTED` | independent reconstruction of the simultaneous-recurrence proof |
| request D | `ACCEPTED_AS_COMPUTATIONAL_EVIDENCE` | bounded exhaustive grid plus high-precision and direct-enumeration replay |

## Independent proof reconstruction

For fixed `n>=3`, write the centered characteristic function as a product of normalized coordinate factors. Centering changes only a unit phase, so the modulus is

```text
product over p<=n of
|sin((b_p+1)t log(p)/2) / ((b_p+1) sin(t log(p)/2))|.
```

Set `alpha_p=log(p)/log(2)` for odd primes `p<=n`. Dirichlet simultaneous approximation gives, for arbitrarily large approximation parameters, an integer `q` for which every `q alpha_p` is close to an integer. The selected denominators must be unbounded: otherwise one fixed nonzero `q` would recur with arbitrarily small error, forcing every `q log(p)/log(2)` to be an integer. That would imply `p^q` is a power of two for an odd prime `p`, contradicting unique factorization.

At

```text
t_q = 2*pi*q/log(2),
```

the prime-2 phase is exactly a multiple of `2*pi`, and every odd-prime phase approaches a multiple of `2*pi` along the unbounded recurrence sequence. Each normalized Dirichlet-kernel factor therefore approaches one, and the finite product approaches one. This proves

```text
limsup_{|t|->infinity} |phi_n(t)| = 1.
```

No gap was found in the frozen proof.

## Bounded computational search

The finite evidence search covers every

```text
3 <= n <= 12
1,000 <= q <= 2,000,000
```

with `t_q=2*pi*q/log(2)`. The frequency blocks are:

```text
[1,000, 9,999]
[10,000, 99,999]
[100,000, 999,999]
[1,000,000, 2,000,000]
```

The scan evaluates 1,999,001 grid points for each of ten `n` values, totaling 19,990,010 characteristic-function scores. All grid points are ranked with IEEE 754 binary64 arithmetic. The best eight candidates per `n` per block are reevaluated with 80-digit Decimal logarithms, a Decimal Machin-formula value of pi, and Decimal sine series. Every winning candidate is then cross-checked by direct complex averaging over all exact divisor exponent vectors.

## Global winners

| n | q | approximate t | high-precision |phi_n(t)| |
|---:|---:|---:|---:|
| 3 | 190,537 | 1.727165e6 | 0.9999999999999573 |
| 4 | 190,537 | 1.727165e6 | 0.9999999999999573 |
| 5 | 1,251,764 | 1.134689e7 | 0.9999994339686029 |
| 6 | 1,251,764 | 1.134689e7 | 0.9999989310408948 |
| 7 | 103,169 | 9.351981e5 | 0.9998129408843456 |
| 8 | 103,169 | 9.351981e5 | 0.9998129408843456 |
| 9 | 1,961,789 | 1.778307e7 | 0.9997421934872927 |
| 10 | 1,961,789 | 1.778307e7 | 0.9995637106203294 |
| 11 | 1,161,483 | 1.052852e7 | 0.9963488288076242 |
| 12 | 1,161,483 | 1.052852e7 | 0.9963479152311605 |

The `n=12` winner has 792 divisor exponent vectors. Its high-precision product value is

```text
0.9963479152311604567408591766877853180415119097975580065644773
```

and the independent direct-vector average differs by approximately `1.86e-15`.

The block winners for `n=12` improve from approximately `0.96354` in the first block to `0.99635` in the final block. This is illustrative finite evidence, not a monotonicity theorem or a proof of the limsup.

## Artifacts

```text
src/factorial_lab/n3_recurrence.py
src/replay_n3_recurrence.py
tests/test_n3_recurrence.py
tests/n3_recurrence_fixtures/corrupt_rehashed_candidate.json
data/analytic/n3_characteristic_recurrence_index.json
data/analytic/n3_characteristic_recurrence_blocks.csv
data/analytic/n3_characteristic_recurrence_best.csv
data/analytic/n3_characteristic_recurrence_evidence.schema.json
certificates/analytic/n3_recurrence_candidate_n12.json
certificates/analytic/n3_recurrence_candidate.schema.json
```

Full evidence semantic SHA-256:

```text
b15ad70a01046ec292ab3197faafc357bf4c9be155e97a5d498b10a6681123fc
```

Candidate certificate semantic SHA-256:

```text
ab8e8a6d0aa24440ceb1379b86d9ae70dd02b2a5b263f4db4ea89eb354f49a24
```

## Validation and resource record

- 12 new recurrence tests pass;
- full semantic replay passes;
- the `n=12` candidate certificate passes;
- a rehashed false modulus is rejected;
- a rehashed changed frequency is rejected;
- a rehashed direct-average corruption is rejected;
- wrong frozen-source metadata is rejected;
- production generation completes in approximately 15.0 seconds;
- full semantic replay completes in approximately 15.6 seconds;
- peak resident memory is approximately 300 MiB;
- no timeout or unknown result occurred.

## Scope restriction

The theorem acceptance rests on the independent proof reconstruction. The numerical search is bounded evidence only. It does not establish a quantitative recurrence rate, certify a global maximum outside the grid, provide a useful bounded minor-arc estimate, or imply additive divisor-sum coverage.

## Next target

Run request E of `N3-HO-N4-002`: reconstruct the scope of the restricted external divisor-distribution sources and verify that none directly selects the factorial sequence.
