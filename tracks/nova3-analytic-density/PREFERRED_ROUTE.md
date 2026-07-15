# Preferred Analytic Route

## Route decision

- Decision ID: `N3-ROUTE-003`
- Status: `PROVED` as a route ranking and obstruction decision; the final additive theorem remains `OPEN`
- Date: 2026-07-15

## Cross-track correction

Nova 2 has frozen the distinction between:

1. logarithmic divisor size,
   \[
   \mathbb E e^{it\log d};
   \]
2. numerical additive occupancy,
   \[
   \mathbb E e^{itS_{n,x}},
   \qquad S_{n,x}=\sum_iY_{i,n,x}.
   \]

A theorem for the first object does not control the second. Numerical additive inversion is periodic on `[-pi,pi]` and must include every nonzero resonance.

The first Nova 1 layer system remains ineligible for Fourier analysis because Nova 2 proved that its main sums lie in a power-of-two sublattice missing the first required window.

## Ranked analytic routes

### 1. Exact top-prime compact-tilt reservoir

Status: `PROVED_PREFERRED_INTRINSIC_COMPONENT`.

Freeze

\[
\mathcal P_n=\{p\text{ prime}:n/2<p\le n\}.
\]

Every coordinate has factorial valuation one. N3-ANA-012 proves, uniformly for each fixed

\[
|\theta|\le\theta_0<1,
\]

a Gaussian approximation, variance lower bound, coarse logarithmic-window positivity at width `K_A log n`, and a lower bound for the number of distinct subset products in the window.

Advantages:

- exact factorial divisors, not a smooth-number surrogate;
- unique-factorization distinctness;
- explicit threshold `n>=120368`;
- no bounded-exponent bookkeeping because every coordinate is Bernoulli;
- fully uniform compact-tilt constants;
- a sharp obstruction at `|theta|=1` from N3-ANA-013.

This is now the strongest clean analytic reservoir theorem on the branch.

### 2. Exact low-prime conditioning plus full high-prime tilted logarithmic analysis

Status: `PREFERRED_GENERALIZATION`.

Split

\[
S_n=S_{\le y}+S_{>y}.
\]

Treat the low-prime component exactly and apply a tilted theorem to the high-prime tail. N3-ANA-008 and N3-ANA-009 establish the zero-tilt coarse regime. Extending N3-ANA-012 from the top Bernoulli band to all bounded high-prime exponent coordinates remains open.

### 3. Structural gate followed by matched numerical additive Fourier analysis

Status: `PREFERRED_FOR_NOVA_2_AFTER_REPAIR`.

Required sequence:

1. Nova 1 proposes a versioned divisor layer system.
2. Nova 2 checks lattice, residues, correction radius, first target, endpoints, distinctness, and nonsequential legality.
3. Nova 2 freezes the exact numerical law, target weights, windows, kernel, reference law, and all major arcs.
4. Nova 3 proves the matched bounded-torus estimate or returns a resonance obstruction.

No logarithmic theorem may be substituted for this numerical additive analysis.

### 4. Explicit prime-band capacity certification

Status: `PROVED_SUPPORTING_ROUTE`.

N3-ANA-010 and N3-ANA-011 close Nova 1's explicit prime count and formal menu-capacity dependency with

\[
n_3=n_4=n_5=120368.
\]

Formal capacity is not profile-sum injectivity or occupancy.

### 5. Fine top-prime local analysis

Status: `NEXT_INTRINSIC_TARGET`.

N3-ANA-012 reaches windows

\[
\Delta\ge K_A\log n.
\]

The next intrinsic question is whether this can be lowered. A successful theorem must analyze the bounded-frequency characteristic function of the weighted Bernoulli prime-log sum. An obstruction must distinguish average density from maximum logarithmic gap.

### 6. Direct saddle point with exact low-prime convolution

Status: `SECONDARY_FOR_LOGARITHMIC_WINDOWS`.

The full tilted product identity remains valid. This route is retained for applications with a frozen low-prime family and an explicitly logarithmic target.

### 7. Full uniform-divisor Gaussian local limit

Status: `DISPROVED` by N3-ANA-006.

### 8. Unrestricted global minor-arc decay

Status: `DISPROVED` by N3-ANA-007.

### 9. Compact top-prime tilt range reaching `|theta|=1`

Status: `DISPROVED` by N3-ANA-013.

At unit tilt the Bernoulli coordinates freeze at their favored endpoints with probability tending to one, and the normalized centered law converges to zero in probability.

### 10. Smooth-number lower-bound transfer

Status: `REJECTED`.

Lower bounds for larger smooth or ultrafriable sets do not transfer to exact factorial divisors.

## Exact current deliverable

For every fixed `theta_0<1` and `A>=0`, N3-ANA-012 supplies effective constants such that top-prime subset products have positive tilted mass and explicit weighted count in every central logarithmic window satisfying

\[
K_A\log n\le\Delta\le B_{n,\theta}.
\]

The theorem is exact in divisor legality and distinctness. It is not an additive occupancy theorem.

## Stop conditions

Abandon or weaken a proposed route if it requires:

- fixed-width logarithmic windows without a local theorem;
- an unbounded pointwise minor arc;
- a Gaussian theorem through `|theta|=1` on the top-prime band;
- a full-vector Gaussian theorem without low-prime conditioning;
- lower-bound transfer from a smooth superset;
- direct control of numerical additive sums from logarithmic divisor estimates;
- Fourier work before Nova 2's structural gate passes;
- profile capacity treated as profile-sum injectivity;
- mean spacing treated as maximum-gap control.

## Next theorem target

`N3-NEXT-003`: determine the sharpest true uniform logarithmic-window scale below `K_A log n` for compactly tilted top-prime subset products. Prove a bounded-frequency local theorem, weaken to the strongest true intermediate scale, or prove a resonance or maximum-gap obstruction.