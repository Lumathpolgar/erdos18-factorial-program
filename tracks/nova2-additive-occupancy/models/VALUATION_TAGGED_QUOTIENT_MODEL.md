# Valuation-Tagged Quotient Occupancy Model

## Model ID

`N2-MOD-QV-001`

## Result label

**conditional theorem** as a repaired reduction.

The one-power and two-power binary repair variants are **disproved models** by `N2-OBS-108`.

## Source construction

The model normalizes Nova 1's full-menu valuation-tagged address packets:

- source branch: `nova/factorial-structure`
- inspected head: `fa11f4b2cb86a2dd791df189ada12757be791804`
- original frozen handoff commit: `b939574eb88a08bb03abda5bbe6ff2ca97444e08`

The original correction contract is rejected. This model uses the repair derived in `proofs/LATTICE_QUOTIENT_NORMALIZATION.md`.

## Parameters

Let

\[
X_n=\lfloor\sqrt{n!}\rfloor,
\qquad
r_n=\lceil4\log n\rceil,
\qquad
M_n=\lceil16(\log n)^2\rceil,
\]

and

\[
g_n=2^{r_n+1}.
\]

For `1<=t<=M_n`, define the normalized label

\[
B_t(n)
=
\{2^{t-1}u:
 u\mid n!,\ u>1,\ u\text{ odd},\ g_n2^{t-1}u\le X_n\}.
\]

The final normalized restricted rainbow sumset is

\[
Q_n
=
\left\{
\sum_{t=1}^{M_n}b_t:
 b_t\in B_t(n)\cup\{0\}
\right\}.
\]

The original main sumset is exactly

\[
R_n=g_nQ_n.
\]

## Selection and collision rules

- zero or one nonzero choice from each label;
- labels are fixed independently of the target;
- different labels have different 2-adic valuations, hence nonzero numerical supports are pairwise disjoint;
- every selected normalized value corresponds to exactly one legal original main divisor after multiplication by `g_n`;
- no intermediate sumset interval invariant is assumed.

## Repaired correction palette

Use

\[
C_n^+=\{2^0,2^1,\ldots,2^{r_n+2}\}.
\]

Its subset sums form the exact interval

\[
[0,2^{r_n+3}-1]
=[0,4g_n-1].
\]

The palette uses at most `r_n+3` terms and is numerically disjoint from the main terms because every nonzero main term has an odd factor greater than one.

## Exact occupancy target

For every quotient target

\[
0\le m\le\lfloor X_n/g_n\rfloor,
\]

prove

\[
Q_n\cap W_{n,m}\ne\varnothing,
\qquad
W_{n,m}=[\max(0,m-3),m]\cap\mathbb Z.
\]

This is a pointwise all-target theorem for final four-point windows.

It is not:

- almost-all coverage;
- average coverage;
- a growing-window theorem;
- a sequential interval-extension theorem;
- a statement about logarithmic divisor size.

## Exact term budget

If the quotient occupancy theorem holds, every original target `0<=x<=X_n` uses at most

\[
M_n+r_n+3
\]

distinct divisors of `n!`.

## Initial support audit

For all sufficiently large admissible `n`,

\[
\min(Q_n\setminus\{0\})=3.
\]

Therefore:

- quotient radius `0`, arising from correction maximum `g_n-1`, fails at `m=1`;
- quotient radius `1`, arising from correction maximum `2g_n-1`, fails at `m=2`;
- quotient radius `3`, arising from correction maximum `4g_n-1`, is the first consecutive-binary repair not already killed by the initial support gap.

## Preferred probabilistic law

For target `m` and tilt `beta`, independently choose

\[
Y_{t,\beta}\in B_t(n)\cup\{0\}
\]

with

\[
\Pr(Y_{t,\beta}=b)
=
\frac{e^{\beta b}}
{\sum_{c\in B_t(n)\cup\{0\}}e^{\beta c}}.
\]

Let

\[
T_{n,\beta}=\sum_tY_{t,\beta}.
\]

The preferred centering point is

\[
m-\frac32.
\]

The additive characteristic function is

\[
\Phi_{n,m}(\theta)
=
\mathbb E e^{i\theta T_{n,\beta_{n,m}}},
\qquad
\theta\in[-\pi,\pi].
\]

## Fourier success condition

For an explicit lattice reference law `G_{n,m}` with characteristic function `Psi_{n,m}`, set

\[
K_{n,m}(\theta)
=
\sum_{a\in W_{n,m}}e^{-ia\theta}.
\]

It is sufficient to prove

\[
\int_{-\pi}^{\pi}
|\Phi_{n,m}(\theta)-\Psi_{n,m}(\theta)|
|K_{n,m}(\theta)|\,d\theta
<
2\pi G_{n,m}(W_{n,m})
\]

for every declared bulk target, together with deterministic coverage of every excluded target.

## Structural inputs required from Nova 1

1. accept or supersede the three-power repair;
2. confirm all added powers divide `n!` in the stated range;
3. confirm `3 in B_1(n)` or list exceptions;
4. freeze the exact quotient endpoint;
5. freeze correction and main distinctness;
6. provide deterministic endpoint targets excluded by the analytic theorem.

## Analytic inputs required from Nova 3

1. exact tilt existence and target range;
2. variance lower and upper bounds;
3. exact quotient span and all torus resonances;
4. explicit reference law and four-point mass;
5. strict weighted Fourier comparison;
6. exact endpoint exclusions.

## Finite falsification required from Nova 4

For feasible `n`, compute exactly:

1. the quotient layers and their legality;
2. pairwise numerical disjointness;
3. `gcd` and residues of `Q_n` modulo small moduli;
4. every reachable quotient sum through a declared cutoff;
5. the first four-point window failure;
6. the maximum downward quotient gap;
7. regression failures for the one-power and two-power repairs;
8. the first success or failure of the three-power initial gate;
9. target-dependent tilt and variance with certified intervals when attempted.

## Current status

The normalization and repaired implication are proved. Global four-point quotient occupancy is open.
