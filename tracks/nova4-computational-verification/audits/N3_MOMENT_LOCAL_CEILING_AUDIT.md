# Independent Audit of N3-ANA-004 and N3-ANA-005

Date: 2026-07-15

## Frozen source

- repository: `Lumathpolgar/erdos18-factorial-program`
- branch: `nova/analytic-density`
- exact commit: `0ce88b28dc2e6641093526f5777bb31f658e3515`
- handoff: `N3-HO-N4-001`
- proof: `tracks/nova3-analytic-density/proofs/PRODUCT_MODEL_THEOREMS.md`
- supplied script: `tracks/nova3-analytic-density/proofs/scale_sanity.py`

No later Nova 3 revision is included.

## Decisions

| Theorem ID | Decision | Scope |
|---|---|---|
| `N3-ANA-004` | `ACCEPTED` | Exact product model, mean, variance, and strict tilted convexity |
| `N3-ANA-005` | `ACCEPTED` | Exact uniform local-count ceiling for all stated parameters |
| `N3-ANA-006` | `NOT_YET_AUDITED` | Deferred to the scale and limit audit |
| `N3-ANA-007` | `NOT_YET_AUDITED` | Deferred to characteristic recurrence testing |
| `N3-ANA-008` | `NOT_YET_AUDITED` | Deferred to high-prime scale audit |
| `N3-ANA-009` | `NOT_YET_AUDITED` | Deferred to dependency and coarse-window audit |

## Proof reconstruction: N3-ANA-004

Unique factorization gives a bijection

```text
(a_p)_{p<=n}, 0<=a_p<=v_p(n!)  <->  divisors of n!.
```

The uniform measure on the Cartesian product makes the coordinates independent and uniform. For a uniform integer `A` on `{0,...,b}`,

```text
E[A] = b/2
Var(A) = b(b+2)/12.
```

Summing the independent coordinates weighted by `log p` gives the claimed mean and variance exactly. Under exponential tilt, the logarithm of the product partition function differentiates to the tilted mean and variance. At least one coordinate is nonconstant for `n>=2`, so the variance is strictly positive and the saddle map is strictly increasing. The endpoint limits follow coordinatewise.

No gap was found in the proof.

## Proof reconstruction: N3-ANA-005

Fix all exponent coordinates except `a_q`. The remaining values are an arithmetic progression with spacing `log q`. A closed interval of length `Delta` contains at most

```text
floor(Delta/log q) + 1
```

such values. There are exactly `tau(n!)/(v_q(n!)+1)` fixed choices of the other coordinates. Multiplication gives the stated ceiling. Taking `q=2` and using `v_2(n!)=n-s_2(n)` gives the uniform `O_Delta(tau(n!)/n)` consequence.

No gap was found in the proof.

## Independent finite certificate

Every divisor of every `n!` for `2<=n<=12` was enumerated as an exact integer before logarithms were evaluated.

Exact coverage:

```text
n values: 11
divisors enumerated across all cases: 1,978
local windows checked: 45,840
widths: 0, 1/4, 1/2, 1, 2
endpoints: every log d with d|n!
primes q: every prime q<=n
```

For every `n`, the verifier checks:

- numerical divisor uniqueness;
- exact divisor count `tau(n!)`;
- complement symmetry `d <-> n!/d`;
- exact rational first and second moments of every exponent coordinate;
- exact vanishing of every cross covariance;
- 80-digit decimal replay of the log mean and variance;
- every requested local ceiling using certified integer window endpoints.

The window checker does not compare floating logarithms. It certifies

```text
floor(d exp(Delta))
```

with rational Taylor bounds and counts exact integer divisors in `[d, floor(d exp(Delta))]`. It separately certifies `floor(Delta/log q)` using rational upper and lower bounds for `log q`.

## Tight and corrupted cases

There are 21 tight windows in the enumerated domain. The first is

```text
n = 2
q = 2
Delta = 0
endpoint divisor = 1
actual = ceiling = 1
```

Lowering the claimed ceiling to zero and recomputing the outer SHA-256 is rejected by semantic recomputation. Corrupting the cached actual count is also rejected.

## Supplied script comparison

The frozen script was inspected and its logic was executed in a local reconstruction. It reported `PASS` for the exhaustive `n<=12` checks. Nova 4's committed verifier is independently written and strengthens the local-window step by removing floating-log endpoint decisions.

The larger scale rows printed by the supplied script are recorded only as pending computational evidence and are not accepted in this checkpoint.

## Artifacts

```text
src/factorial_lab/n3_moments.py
src/replay_n3.py
tests/test_n3_moments.py
tests/n3_fixtures/corrupt_rehashed_downward_bound.json
data/analytic/n3_moment_local_n2_n12.json
data/analytic/n3_moment_local_summary_n2_n12.csv
certificates/analytic/n3_local_ceiling_tight_n2.json
```

Semantic audit SHA-256:

```text
85fdfcd360faa9009531c10bf46a85bf0312e6e46252d06544e72787183f4e03
```

## Validation record

- 10 new tests passed;
- full semantic replay passed;
- valid tight certificate replay passed;
- rehashed downward-bound corruption was rejected;
- rehashed cached-count corruption was rejected;
- generation completed in approximately 2.35 seconds;
- peak resident memory was approximately 288 MiB;
- no timeout or unknown result occurred.

## Scope restriction

The finite enumeration certifies only the stated finite domain. Acceptance of `N3-ANA-004` and `N3-ANA-005` rests on the independently reconstructed elementary proofs, with the computation serving as a finite audit. No additive divisor-sum coverage and no asymptotic factorial theorem is inferred.

## Next target

Run request C from `N3-HO-N4-001`: independently generate the scale-convergence table, prime variance shares, participation ratio, and high-prime `M_{n,y}/B_{n,y}` grid, labeling every result `COMPUTATIONAL_EVIDENCE`.
