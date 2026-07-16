# Nova 3 N3-ANA-006 Variance and Non-Gaussian Limit Audit

Date: 2026-07-16

## Frozen source

```text
branch: nova/analytic-density
handoff: N3-HO-N4-002
handoff commit: 7469dada02fa4caca08ed391ef8b0cb0f1e855b2
proof file: tracks/nova3-analytic-density/proofs/PRODUCT_MODEL_THEOREMS.md
proof file blob: 6260f8db0b377cf7dbc1850cbe25c91243099e10
source ledger blob: da81e6aaf2674fdae036d72df002547d4a71b18a
object: N3-ANA-006
```

The frozen theorem has no imported probabilistic or analytic source beyond elementary convergence and unique factorization.

## Decisions

```text
N3-ANA-006: ACCEPTED
variance asymptotic: ACCEPTED
full normalized weak limit: ACCEPTED
non-Gaussian limit: ACCEPTED
finite convergence table as proof: REJECTED
```

## Exact starting model

For a uniformly selected divisor of `n!`, write

\[
S_n=\sum_{p\le n}A_p\log p,
\qquad
A_p\sim\operatorname{Unif}\{0,\ldots,b_p\},
\qquad
b_p=v_p(n!).
\]

The coordinates are independent. Therefore

\[
\operatorname{Var}(S_n)
=
\frac1{12}\sum_{p\le n}b_p(b_p+2)(\log p)^2.
\]

For

\[
X_n=\frac{S_n-\frac12\log(n!)}{n},
\]

we have

\[
\operatorname{Var}(X_n)
=
\frac1{12}\sum_{p\le n}
\left(\frac{b_p^2}{n^2}+\frac{2b_p}{n^2}\right)(\log p)^2.
\]

## Fixed-prime limit

Legendre's formula gives

\[
b_p=\sum_{k\ge1}\left\lfloor\frac{n}{p^k}\right\rfloor.
\]

For each fixed prime `p`,

\[
\frac{b_p}{n}
\longrightarrow
\sum_{k\ge1}\frac1{p^k}
=
\frac1{p-1}.
\]

The centered discrete uniform coordinate consequently satisfies

\[
\frac{A_p-b_p/2}{n}
\Rightarrow
U_p,
\]

where

\[
U_p\sim\operatorname{Unif}
\left[-\frac1{2(p-1)},\frac1{2(p-1)}\right].
\]

Independence gives joint convergence on every fixed finite prime set.

## Uniform tail control

The exact valuation bound

\[
b_p\le\frac{n}{p-1}
\]

implies, for a fixed cutoff `Y`,

\[
\operatorname{Var}\left(\sum_{Y<p\le n}
\frac{(A_p-b_p/2)\log p}{n}\right)
\le
\frac1{12}\sum_{p>Y}\frac{(\log p)^2}{(p-1)^2}
+
\frac1{6n}\sum_{Y<p\le n}\frac{(\log p)^2}{p-1}.
\]

The second term is bounded by

\[
\frac{(\log n)^2(1+\log(n-1))}{6n},
\]

which tends to zero.

For `Y>=8`, the first term is bounded by the integer comparison

\[
\sum_{p>Y}\frac{(\log p)^2}{12(p-1)^2}
\le
\frac{(\log Y)^2+2\log Y+2}{3Y}.
\]

Thus the normalized tail variance tends uniformly to zero after first taking `n` large and then `Y` large.

## Variance asymptotic

Finite-prime convergence and the tail estimate yield

\[
\boxed{
\frac{\operatorname{Var}(S_n)}{n^2}
\longrightarrow
\frac1{12}\sum_p\frac{(\log p)^2}{(p-1)^2}
}.
\]

At prime cutoff `1,000,000`, the computed partial sum is

```text
0.1154658352305299
```

and the elementary all-integer tail bound is

```text
0.00007349978436438362
```

so the limiting variance lies in the rigorous enclosure

```text
[0.1154658352305299, 0.11553933501489429]
```

The enclosure is intentionally elementary and not optimized.

## Infinite weak limit

Let the independent variables `U_p` be as above. Since

\[
\sum_p\operatorname{Var}((\log p)U_p)
=
\frac1{12}\sum_p\frac{(\log p)^2}{(p-1)^2}<\infty,
\]

the series

\[
X=\sum_p(\log p)U_p
\]

converges in `L^2`.

The finite-prime joint convergence and the uniform tail estimate give

\[
\boxed{X_n\Rightarrow X}.
\]

## Characteristic function and non-Gaussianity

The limiting characteristic function is

\[
\phi_X(t)
=
\prod_p
\frac{\sin(t\log p/[2(p-1)])}{t\log p/[2(p-1)]}.
\]

Compact convergence follows from

\[
1-\operatorname{sinc}(x)=O(x^2)
\]

and convergence of the variance series.

At

\[
t_0=\frac{2\pi}{\log2},
\]

the `p=2` argument is exactly `pi`, so that factor is zero. Hence

\[
\phi_X(t_0)=0.
\]

A nondegenerate Gaussian characteristic function never vanishes. The limiting law is therefore not Gaussian.

This conclusion applies to the full divisor model at its natural variance scale. It does not contradict a separate central limit theorem for a high-prime tail after low-prime coordinates are removed.

## Finite diagnostics

The exact valuation formula was evaluated for selected values through `n=1,000,000`.

```text
n=50       Var(S_n)/n^2 = 0.10558484561623833
n=1,000    Var(S_n)/n^2 = 0.11485212177618963
n=10,000   Var(S_n)/n^2 = 0.11544768625558857
n=100,000  Var(S_n)/n^2 = 0.11546927713679392
n=1,000,000 Var(S_n)/n^2 = 0.11546830343704997
```

These rows are computational evidence only.

## Fail-closed corruptions

The verifier rejects rehashed claims that:

1. replace the variance coefficient `1/12` by `1/6`;
2. replace `(p-1)^2` by `p^2`;
3. report the limiting law as Gaussian;
4. replace the zero frequency `2*pi/log(2)` by `pi/log(2)`;
5. report the finite convergence table as the asymptotic proof;
6. alter the frozen proof metadata or evidence hash.

## Artifacts

```text
src/factorial_lab/n3_variance_limit.py
src/replay_n3_variance.py
tests/test_n3_variance_limit.py
tests/n3_variance_fixtures/*.json
data/analytic/n3_variance_limit_audit.json
data/analytic/n3_variance_limit_audit.schema.json
data/analytic/n3_variance_convergence.csv
data/analytic/N3_VARIANCE_LIMIT_README.md
certificates/analytic/n3_ana_006_final_claim.json
certificates/analytic/n3_ana_006_final_claim.schema.json
```

Semantic SHA-256 values:

```text
audit: e1914a367749c8a397e77212c0d48c53335811e52418ffe0d8d1738046886119
claim: efe6091759b788c9383b76799a6a62283a06d3d4f844f5a9e9199ed09d49dcf4
```

## Validation

- 12 new variance-limit tests pass;
- full semantic audit replay passes;
- final claim replay passes;
- all five generated rehashed theorem corruptions are rejected;
- wrong frozen-source metadata and wrong evidence hashes are rejected;
- standalone audit replay completes in approximately 1.43 seconds;
- standalone claim replay completes in approximately 1.33 seconds;
- peak resident memory is approximately 304,400 KiB;
- no timeout or unknown result occurred.

## Scope restriction

This audit proves the normalized variance asymptotic, the full-model weak limit, the `L^2` limiting series, its characteristic-function product, and non-Gaussianity. It does not prove `N3-ANA-008`, `N3-ANA-009`, additive occupancy, the factorial half-range theorem, or Erdős Problem 18.

## Next target

Independently reconstruct and decide `N3-ANA-008`, the high-prime-tail central limit theorem.
