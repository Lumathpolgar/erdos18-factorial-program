# Preferred Additive Route

## Current ranking

### Rank 1: Normalized valuation-tagged quotient occupancy

**Result label: conditional theorem.**

Use the quotient labels from `models/VALUATION_TAGGED_QUOTIENT_MODEL.md`, the three-power repaired binary palette, target-dependent exponential tilting for centering, and the weighted bounded-torus Fourier inequality for exact four-point window positivity.

This is the first route attached to an explicit factorial construction whose original lattice defect has been completely normalized and whose minimum consecutive-binary repair has been identified.

### Rank 2: Deterministic restricted-sumset growth on the quotient labels

**Result label: conditional theorem.**

Prove directly that the final normalized sumset has maximum downward gap at most `3`, without any requirement on intermediate partial sumsets.

This route avoids local-limit losses but still must preserve labels, numerical distinctness, divisor legality, and the final quotient endpoint.

### Rank 3: General target-dependent exponential tilt

**Result label: conditional theorem.**

Retained as the general architecture underlying Rank 1 and for future structurally compatible labels.

### Rank 4: Uniform rainbow convolution

**Result label: heuristic.**

Useful as a benchmark, but one fixed mean leaves endpoint targets in large-deviation tails.

### Rank 5: Fixed-law Fourier or local-limit theorem

**Result label: heuristic as a standalone route.**

Fourier analysis remains a proof tool inside Rank 1. A fixed-law central theorem is not an all-target half-range mechanism.

## Structural compatibility gate

Before tilting, moment computation, dynamic programming, or Fourier inversion, every fixed label family must pass all of the following.

1. Compute the common support lattice `g_n Z` of the final main sumset.
2. Determine the exact attained residues if the support is not a single lattice coset.
3. Divide out every common factor and state the quotient labels explicitly.
4. Compare the correction range with every unresolved quotient downward gap using N2-ADD-116.
5. Test the first requested target directly.
6. Test the minimum nonzero quotient sum and the top endpoint.
7. Verify that the correction palette is numerically disjoint from every main label.
8. Verify that the full construction remains final-only and does not impose sequential interval growth.

N2-ADD-115 rejects a radius smaller than the first missing lattice block. N2-ADD-116 gives the exact quotient theorem after any valid correction range is frozen.

## Rejected original instantiation

Nova 1 handoff `N1-HO-N2-001`, imported from branch `nova/factorial-structure` at commit

`b939574eb88a08bb03abda5bbe6ff2ca97444e08`,

failed the structural gate.

Its entire main sumset lies in

\[
2^{r_n+1}\mathbb Z,
\]

while the original correction radius is only

\[
2^{r_n}-1.
\]

The first requested window is disjoint from the support. The exact model is `REJECTED`.

Proof: `proofs/VALUATION_TAGGED_LATTICE_OBSTRUCTION.md`.

## Exact quotient normalization

For the retained main layers, set

\[
g_n=2^{r_n+1}
\]

and define

\[
B_t(n)
=
\{2^{t-1}u:
 u\mid n!,\ u>1,\ u\text{ odd},\ g_n2^{t-1}u\le X_n\}.
\]

Let

\[
Q_n
=
(B_1(n)\cup\{0\})+\cdots+(B_{M_n}(n)\cup\{0\}).
\]

Then the original main sumset is exactly

\[
R_n=g_nQ_n.
\]

N2-ADD-116 proves that if correction covers `[0,Lg_n-1]`, then exact original-target coverage is equivalent to quotient downward gaps at most `L-1`.

## Minimal consecutive-binary repair

The original palette ends at `2^{r_n-1}`.

- Adding only `2^{r_n}` gives correction maximum `g_n-1` and fails at quotient target `m=1`.
- Adding through `2^{r_n+1}` gives correction maximum `2g_n-1` and fails at quotient target `m=2`.
- Adding through `2^{r_n+2}` gives correction maximum `4g_n-1` and is the first consecutive-binary extension not blocked by the initial support gap.

The first two variants are N2-OBS-108.

The proposed repaired palette is

\[
C_n^+=\{2^0,2^1,\ldots,2^{r_n+2}\}.
\]

Nova 1 must accept, restrict, supersede, or reject this repair in a versioned handoff. Contract: `handoffs/REPAIR_CONTRACT_TO_NOVA1.md`.

## Frozen exact additive theorem

The surviving global target is

\[
Q_n\cap[\max(0,m-3),m]\ne\varnothing
\]

for every integer

\[
0\le m\le\lfloor X_n/g_n\rfloor.
\]

Under this hypothesis, N2-ADD-117 proves

\[
H_{n!}(X_n+1)
\le
M_n+r_n+3
=O((\log n)^2).
\]

This is a final-only theorem. It does not require intermediate sumsets to cover intervals.

## Preferred probabilistic proof engine

For target `m`, use independent quotient-layer choices with target-dependent Gibbs weights

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

Center the mean inside the exact window

\[
W_{n,m}=[\max(0,m-3),m].
\]

The additive numerical-value characteristic function is

\[
\Phi_{n,m}(\theta)
=
\mathbb E e^{i\theta T_{n,\beta_{n,m}}},
\qquad
\theta\in[-\pi,\pi].
\]

For an explicit lattice reference law `G_{n,m}` with characteristic function `Psi_{n,m}`, it is sufficient to prove

\[
\int_{-\pi}^{\pi}
|\Phi_{n,m}(\theta)-\Psi_{n,m}(\theta)|
\left|\sum_{a\in W_{n,m}}e^{-ia\theta}\right|d\theta
<
2\pi G_{n,m}(W_{n,m}).
\]

The exact analytic contract is `handoffs/QUOTIENT_REQUEST_TO_NOVA3.md`.

## Deterministic alternative

A deterministic proof may replace all probability and Fourier work by proving directly that the final labeled quotient sumset has maximum downward gap at most `3`.

It must still establish:

- fixed labels;
- numerical distinctness;
- legal lift by multiplication with `g_n`;
- every quotient target;
- the top partial block;
- no hidden sequential interval invariant.

## Why the route survives historical no-go results

- It does not infer coverage from profile count.
- It removes the common lattice before analytic modeling.
- It does not require partial sumsets to cover intervals.
- It is not an independently decoded CRT product.
- It is not a one-choice sequential ladder.
- It tests the final globally coupled quotient sumset.
- It uses a correction range matched exactly to the quotient gap theorem.
- It rejects logarithmic-divisor estimates unless a transfer theorem is proved.

## Exact blockers

1. Nova 1 has not yet accepted or superseded the three-power repair.
2. The final quotient maximum-gap-`3` theorem is open.
3. The exact quotient span and secondary resonances are unknown.
4. No target-uniform quotient tilt and variance theorem is available.
5. No strict four-point weighted Fourier inequality has been proved.
6. No deterministic endpoint contract has been returned.
7. No exact finite quotient falsification harness has been published.
8. Finite exceptions remain open.

## Next theorem target

Prove or disprove that the final normalized rainbow sumset `Q_n` has maximum downward gap at most `3` through `floor(X_n/g_n)`. The immediate work is to run exact finite quotient-gap searches, determine all additive resonances, and identify a bulk range where a four-point local theorem could be quantitatively strong enough.
