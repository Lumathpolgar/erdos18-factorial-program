# Nova 3 N3-ANA-008 and N3-ANA-009 High-Prime Limit Audit

Date: 2026-07-16

## Frozen source

```text
branch: nova/analytic-density
handoff: N3-HO-N4-002
handoff commit: 7469dada02fa4caca08ed391ef8b0cb0f1e855b2
proof file: tracks/nova3-analytic-density/proofs/PRODUCT_MODEL_THEOREMS.md
proof file blob: 6260f8db0b377cf7dbc1850cbe25c91243099e10
source ledger blob: da81e6aaf2674fdae036d72df002547d4a71b18a
```

External dependencies are exactly the prime number theorem `N3-SRC-002` and the Berry-Esseen inequality `N3-SRC-003`.

## Decisions

```text
N3-ANA-008: ACCEPTED
N3-ANA-009: ACCEPTED_WITH_EXTERNAL_BERRY_ESSEEN_DEPENDENCY
finite diagnostics as proof: REJECTED
request C full-span label as theorem M: REJECTED
```

## Exact model

For primes `p>y`, let

\[
Y_{p,n}=(A_p-b_p/2)\log p,
\qquad b_p=v_p(n!),
\]

where the `A_p` are independent and uniform on `{0,...,b_p}`. Put

\[
T_{n,y}=\sum_{y<p\le n}Y_{p,n},
\qquad
B_{n,y}^2=\sum_{y<p\le n}\frac{b_p(b_p+2)}{12}(\log p)^2,
\]

and

\[
M_{n,y}=\max_{p>y}\frac{b_p\log p}{2}.
\]

The factor `1/2` is mandatory because `M` is the largest centered coordinate magnitude. The full coordinate span is `2M`.

## N3-ANA-008 variance scale

Assume `y=y(n)->infinity` and `2y<=sqrt(n)` eventually. For every prime `y<p<=2y`,

\[
b_p\ge \left\lfloor\frac np\right\rfloor\ge\frac{n}{2p}
\]

for all sufficiently large `n`, because `n/p>=sqrt(n)`. Therefore each prime in this band contributes

\[
\gg \frac{n^2(\log y)^2}{y^2}
\]

to `B_{n,y}^2`. The prime number theorem gives

\[
\pi(2y)-\pi(y)\gg\frac{y}{\log y},
\]

so

\[
\boxed{B_{n,y}^2\gg n^2\frac{\log y}{y}}.
\]

Legendre's bound gives

\[
b_p\le\frac{n}{p-1}.
\]

Since `log x/(x-1)` decreases for `x>1`,

\[
M_{n,y}\le \frac n2\frac{\log y}{y-1}
\ll n\frac{\log y}{y}.
\]

Consequently,

\[
\boxed{
\frac{M_{n,y}}{B_{n,y}}
\ll \sqrt{\frac{\log y}{y}}
\longrightarrow0}.
\]

Every summand satisfies `|Y_{p,n}|<=M_{n,y}`. For every fixed `epsilon>0`, eventually `M_{n,y}<epsilon B_{n,y}`, so the Lindeberg sum is exactly zero. The Lindeberg-Feller theorem yields

\[
\boxed{T_{n,y}/B_{n,y}\Rightarrow N(0,1)}.
\]

This is a theorem only for the truncated high-prime tail. It does not make the full divisor model Gaussian. The accepted `N3-ANA-006` theorem shows the opposite for the full model.

## N3-ANA-009 coarse window theorem

Let `C_BE` be the universal constant from `N3-SRC-003`. Since `|Y_{p,n}|<=M_{n,y}`,

\[
\sum_{p>y}\mathbb E|Y_{p,n}|^3
\le M_{n,y}\sum_{p>y}\mathbb E Y_{p,n}^2
=M_{n,y}B_{n,y}^2.
\]

Berry-Esseen therefore gives Kolmogorov distance at most

\[
C_{BE}\frac{M_{n,y}}{B_{n,y}}.
\]

Write `a=x/B_{n,y}` and `h=Delta/B_{n,y}`. Under `|x|<=B_{n,y}` and `0<Delta<=B_{n,y}`, the interval `[a,a+h]` lies in `[-1,2]`. The standard normal density there is at least

\[
\phi(2)=\frac{e^{-2}}{\sqrt{2\pi}}.
\]

Thus its normal mass is at least `phi(2)h`. Using both CDF endpoints costs at most

\[
2C_{BE}\frac{M_{n,y}}{B_{n,y}}.
\]

Choose

\[
K=\frac{4C_{BE}}{\phi(2)}.
\]

When `Delta>=K M_{n,y}`,

\[
\boxed{
\mathbb P\{T_{n,y}\in[x,x+\Delta]\}
\ge \frac{\phi(2)}2\frac{\Delta}{B_{n,y}}}.
\]

The use of `F(b)-F(a)` proves the same lower bound for the closed target interval even if the distribution has an atom at its left endpoint.

This theorem is coarse. It does not reach `Delta` below a constant multiple of `M_{n,y}`.

## Finite diagnostics

For `y=floor(sqrt(n))/2`:

```text
n=10,000      y=50    M/B=0.42704100199186046
n=100,000     y=158   M/B=0.28088934761914103
n=1,000,000   y=500   M/B=0.18044353517209441
n=10,000,000  y=1581  M/B=0.11145145759650005
```

The corresponding full-span ratios are exactly twice these values. The rows are computational evidence only.

## Fail-closed corruptions

The verifier rejects rehashed claims that:

1. replace the theorem half-span `M` by the full span `2M`;
2. remove the hypothesis `y->infinity`;
3. infer a Gaussian limit for the full divisor model;
4. report the finite table as asymptotic proof;
5. remove the coarse condition `Delta>=K M`;
6. subtract only one Berry-Esseen endpoint error;
7. remove the external Berry-Esseen dependency;
8. claim windows below `M` are covered;
9. alter the frozen source metadata or evidence checksum.

## Artifacts

```text
src/factorial_lab/n3_high_prime.py
src/replay_n3_high_prime.py
tests/test_n3_high_prime.py
tests/n3_high_prime_fixtures/*.json
data/analytic/n3_high_prime_limit_audit.json
data/analytic/n3_high_prime_limit_audit.schema.json
data/analytic/n3_high_prime_diagnostics.csv
data/analytic/N3_HIGH_PRIME_LIMIT_README.md
certificates/analytic/n3_ana_008_final_claim.json
certificates/analytic/n3_ana_008_final_claim.schema.json
certificates/analytic/n3_ana_009_final_claim.json
certificates/analytic/n3_ana_009_final_claim.schema.json
```

Semantic SHA-256 values:

```text
audit: a9c089489b38990c6de044611a21d8a488166dd0ad570456fee54a0020dc9dd2
N3-ANA-008 claim: 5723c037725e1bc262bd109b65510d74833a28d8869f27903cd86c33473bf930
N3-ANA-009 claim: b3775b62ef887fbaa92e39e1ab729d6f093f360d778edfdc4a52a2a1e3397d7d
```

## Validation

- 13 new tests pass;
- audit replay passes;
- both final theorem-claim replays pass;
- all eight committed rehashed fixtures are rejected;
- standalone audit replay completes in approximately 3.11 seconds;
- N3-ANA-008 claim replay completes in approximately 3.04 seconds;
- N3-ANA-009 claim replay completes in approximately 3.09 seconds;
- fixture-directory replay completes in approximately 9.62 seconds;
- full isolated test suite completes in approximately 23.36 seconds;
- peak resident memory is approximately 350,804 KiB;
- no timeout or unknown result occurred.

## Scope restriction

These theorems do not prove thin-window local limits, profile injectivity, distinct numerical sums, additive occupancy, the factorial half-range theorem, or Erdős Problem 18.
