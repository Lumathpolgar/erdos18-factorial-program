# Preferred Additive Route

## Current ranking

### Rank 1: Marker-three quotient occupancy with final-only target-dependent Fourier control

**Result label: conditional theorem.**

Frozen structural source:

- branch: `nova/factorial-structure`
- exact commit: `ebb47ba436af554366d0f285119a769f31f9e561`
- construction: `N1-CON-003`
- handoff: `N1-HO-N2-002`
- Nova 2 outcome: `ACCEPTED_WITH_RESTRICTIONS`

The marker-three construction uses quotient labels

\[
B_t(n)=
\{2^{t-1}u:u\text{ odd},\ 3u\mid n!,\ 2^{t-1}u\le Y_n\},
\]

where

\[
Y_n=\left\lfloor\frac{\lfloor\sqrt{n!}\rfloor}{3}\right\rfloor.
\]

The required quotient theorem is

\[
Q_n\cap[q-W_n,q]\ne\varnothing,
\]

with

\[
W_n=\left\lfloor\frac{2^{r_n}-3}{3}\right\rfloor.
\]

Success gives

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
\le M_n+r_n
=O((\log n)^2).
\]

Why this is preferred:

- exact main lattice `3 Z`;
- quotient span one;
- original binary correction palette suffices;
- numerical main-palette disjointness;
- exact term cost `M_n+r_n`;
- target window is polynomially wide rather than four points;
- construction already has a proved deterministic initial interval.

Preferred proof engine:

1. choose a target-dependent exponential law on the fixed numerical quotient labels;
2. center the mean inside `[q-W_n,q]`;
3. prove moment and maximal-step bounds;
4. identify every bounded-torus resonance;
5. prove a strict weighted Fourier inequality below exact reference window mass;
6. use collision-free extraction and the binary correction palette.

Exact analytic request:

`handoffs/MARKER_THREE_REQUEST_TO_NOVA3.md`.

### Rank 2: Deterministic final restricted-sumset theorem for marker-three labels

**Result label: conditional theorem.**

This route would prove every final quotient window occupied without probabilistic approximation. It remains final-only and therefore avoids a hidden sequential interval invariant.

Main blocker: available sumset theorems do not automatically preserve one choice per label, numerical distinctness, factorial legality, downward orientation, and endpoint location.

### Rank 3: Connected-core carrier recursion

**Result label: conditional theorem.**

Nova 2 proved N2-ADD-119 and N2-ADD-120.

At layer `t`, the exact allowable core gap is

\[
D_t(E_{t-1})
=
\left\lfloor
\frac{E_{t-1}+W_n+1}{2^{t-1}}
\right\rfloor.
\]

The recursion gives a scalable exact certificate of how far translated carrier blocks cover. It can also produce a first blocking core gap.

This engine is ranked third because it is sequential. A failure does not disprove the full model, and a success requires an exact Phase 12P compatibility audit.

Proof:

`proofs/MARKER_THREE_CARRIER_BLOCK_REDUCTION.md`.

Verification request:

`handoffs/MARKER_THREE_REQUEST_TO_NOVA4.md`.

### Rank 4: Three-power normalized valuation-tagged fallback

**Result label: conditional theorem with proved prefix.**

This is the former preferred route, governed by N2-ADD-116 through N2-ADD-118. It is now `SUPERSEDED_AS_PREFERRED` but retained because its normalization, obstruction, repair, and binary-spine theorem are exact.

Marker-three is better on the current evidence because it has a smaller lattice, wider correction window, and lower term count.

### Rank 5: Uniform rainbow convolution

**Result label: heuristic.**

One fixed mean leaves endpoints in large-deviation tails. It remains a benchmark, not the preferred architecture.

### Rank 6: Fixed-law local theorem as a standalone route

**Result label: heuristic.**

Fourier analysis remains essential inside the target-dependent route, but a single fixed law is not expected to cover both endpoints uniformly.

## Structural gate for marker-three

The following are now accepted:

1. divisor legality under the stated valuation side condition;
2. numerical distinctness across layers;
3. main-palette disjointness;
4. exact lattice `3 Z`;
5. quotient span one;
6. correction radius `R_n=2^{r_n}-1`;
7. quotient radius `W_n=floor((R_n-2)/3)`;
8. first-target coverage;
9. term count `M_n+r_n`.

The following remain open:

1. global quotient occupancy;
2. endpoint reach near `Y_n`;
3. total-sum collision collapse;
4. final-only Fourier or deterministic sumset theorem;
5. Phase 12P audit for the sequential carrier engine;
6. finite exceptions.

## Deterministic protected region

Nova 1 proves downward one-density through

\[
A_n=m_n(2^{M_n}-1),
\]

where `m_n` is the largest odd integer at most `n`.

Nova 2 extends required target-window occupancy through

\[
A_n+W_n.
\]

Computational and analytic work should focus beyond this boundary.

## Exact next theorem target

There are now two parallel valid targets.

### Deterministic target

Compute or prove the connected-core recursion and determine whether

\[
E_{M_n}+W_n\ge Y_n.
\]

### Final-only analytic target

Prove the marker-three numerical-value weighted Fourier theorem on `[-pi,pi]` for every target beyond the deterministic protected region.

A failure of the deterministic carrier engine must not terminate the final-only route.