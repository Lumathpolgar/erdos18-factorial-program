# Independent audit of Dusart Theorem 6.9 and N3-ANA-010

Date: 2026-07-16

## Frozen source

- repository: `Lumathpolgar/erdos18-factorial-program`
- branch: `nova/analytic-density`
- handoff: `N3-HO-N4-002`
- handoff commit: `7469dada02fa4caca08ed391ef8b0cb0f1e855b2`
- source-ledger commit: `697e7ed8bdb03f54b2389b2fcdd8b685dadcebc4`
- proof file: `tracks/nova3-analytic-density/proofs/EXPLICIT_PRIME_INTERVAL_AND_CAPACITY.md`
- proof file blob SHA: `e36daf98db86da16bd5ed8c6c82f43530d745f66`
- request: `F`
- object: `N3-ANA-010`

No later Nova 3 proof or source-ledger revision is included.

## Decision

| Object | Decision |
|---|---|
| Request F | `ACCEPTED` |
| Dusart Theorem 6.9 thresholds | `CONFIRMED` |
| Independent algebra for `N3-ANA-010` | `CONFIRMED` |
| `N3-ANA-010` | `ACCEPTED` |

## Primary-source reconstruction

Pierre Dusart, *Estimates of Some Functions Over Primes without R.H.*, arXiv:1002.0442v1, Theorem 6.9, equation (6.6), gives

\[
\pi(x)\ge \frac{x}{\log x-1}\qquad(x\ge5393)
\]

and

\[
\pi(x)\le \frac{x}{\log x-1.1}\qquad(x\ge60184).
\]

The PDF displays both thresholds with non-strict source hypotheses.

For an integer `n`, the lower estimate is applied at `x=n`, while the upper estimate is applied at `x=n/2`. Therefore the two hypotheses both hold whenever

```text
n >= 5393
n/2 >= 60184
```

and hence for every integer

```text
n >= 120368.
```

The predecessor `n=120367` has `n/2=60183.5`, so the upper source theorem does not cover it without a separate finite supplement. Thus `120368` is the minimal threshold forced by these two unsupplemented source hypotheses. This does not claim that it is the globally smallest threshold for the final prime-interval inequality.

## Independent algebra

Put

\[
L=\log n,
\qquad
b=\log2+1.1.
\]

The source estimates imply

\[
\pi(n)-\pi(n/2)
\ge
n\left(\frac1{L-1}-\frac1{2(L-b)}\right).
\]

Subtracting `n/(3L)` and combining denominators gives

\[
\frac1{L-1}-\frac1{2(L-b)}-\frac1{3L}
=
\frac{Q(L)}{6L(L-1)(L-b)},
\]

where

\[
Q(L)=L^2+(5-4b)L-2b.
\]

The proof is certified by elementary rational inequalities:

1. The positive Taylor lower bound
   \[
   e^{7/10}>1+\frac7{10}+\frac{(7/10)^2}{2}+\frac{(7/10)^3}{6}
   =\frac{12013}{6000}>2
   \]
   proves `log(2)<7/10`, so `b<9/5`.
2. The elementary series bound `e<11/4<3` gives `e^4<81<120368`, hence `L>4` throughout the theorem range.
3. Consequently
   \[
   Q(L)>L^2-\frac{11}{5}L-\frac{18}{5}.
   \]
   This lower polynomial is increasing for `L>=4` and its value at `4` is `18/5>0`.
4. All denominators are positive because `L>4>b`.

Therefore

\[
\pi(n)-\pi(n/2)\ge\frac{n}{3\log n}
\]

for every integer `n>=120368`.

After completing this reconstruction, the frozen Nova 3 proof was inspected. Its source thresholds, substitution, rational function, polynomial `Q`, and elementary bounds agree with the independent derivation.

## Exact threshold witness

An independent sieve at `n=120368` gives

```text
pi(120368) = 11330
pi(60184) = 6076
pi(120368)-pi(60184) = 5254
```

At 80-digit Decimal precision:

```text
source-derived lower bound = 5175.0999891899846192077009850703359189801705849350393955290986993336685136592484
n/(3 log n) = 3429.7834568288243687445927595774767729879671535604430118904514711214190975705213
source margin = 1745.3165323611602504631082254928591459922034313745963836386472282122494160887271
exact-count margin = 1824.2165431711756312554072404225232270120328464395569881095485288785809024294787
```

This exact finite check supports the endpoint but is not needed for the all-`n` proof.

## Artifacts

```text
src/factorial_lab/n3_dusart.py
src/replay_n3_dusart.py
tests/test_n3_dusart.py
tests/n3_dusart_fixtures/corrupt_rehashed_threshold.json
data/analytic/n3_dusart_prime_interval_audit.json
data/analytic/n3_dusart_prime_interval_audit.schema.json
data/analytic/N3_DUSART_README.md
certificates/analytic/n3_dusart_prime_interval_claim.json
certificates/analytic/n3_dusart_prime_interval_claim.schema.json
```

Full audit semantic SHA-256:

```text
42e3675f35d0623f09b30b36ae6847bedadf448cdfe3984ef20fcef09904f212
```

Claim semantic SHA-256:

```text
7d33e3f669768c555267753c5439d50e2502de2202a9298a0c209c6c9c129703
```

## Validation and resource record

- 12 new Dusart-source tests pass;
- full audit replay passes;
- valid theorem claim replay passes;
- a rehashed threshold of `120367` is rejected;
- a rehashed source upper threshold of `60183` is rejected;
- a rehashed claim of predecessor coverage is rejected;
- wrong frozen-source metadata is rejected;
- generation completes in approximately 1.27 seconds;
- full replay completes in approximately 1.29 seconds;
- peak resident memory is approximately 305 MiB;
- no timeout or unknown result occurred.

## Scope restriction

This audit accepts the explicit prime-interval theorem only. It does not by itself establish address legality, menu capacity, numerical sumset occupancy, the factorial half-range theorem, or Erdős Problem 18.

## Next target

Run request G of `N3-HO-N4-002`: exact threshold sweep for every integer `120368<=n<=1000000`, recording minimum margins for prime counts, Legendre valuations, address legality, and conservative profile capacity.
