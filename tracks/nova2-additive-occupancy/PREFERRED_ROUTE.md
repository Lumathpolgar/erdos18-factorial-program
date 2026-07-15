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
\qquad
W_n=\left\lfloor\frac{2^{r_n}-3}{3}\right\rfloor.
\]

Success gives

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
\le M_n+r_n
=O((\log n)^2).
\]

Why this remains preferred:

- exact main lattice `3 Z`;
- quotient span one;
- original binary correction palette suffices;
- numerical main-palette disjointness;
- exact term cost `M_n+r_n`;
- polynomially wide target windows;
- deterministic and computational endpoint evidence;
- exact finite carrier success for every `12<=n<=46`.

Preferred proof engine:

1. choose a target-dependent exponential law on the fixed numerical quotient labels;
2. center its mean inside `[q-W_n,q]`;
3. prove moment and maximal-step bounds;
4. identify every bounded-torus resonance;
5. prove a strict weighted Fourier inequality below exact reference-window mass;
6. extract a legal final rainbow representation and apply the correction palette.

Exact analytic request:

`handoffs/MARKER_THREE_REQUEST_TO_NOVA3.md`.

### Rank 2: Deterministic final restricted-sumset theorem

**Result label: conditional theorem.**

This route would prove every final quotient window occupied without probabilistic approximation. It remains final-only and therefore avoids a hidden sequential interval invariant.

Main blocker: available sumset theorems do not automatically preserve one choice per layer, numerical distinctness, factorial legality, downward orientation, and endpoint location.

### Rank 3: Connected-core carrier recursion

**Result label: conditional theorem with exact finite certificates.**

Nova 2 proved:

- N2-ADD-119: translated carrier-block lemma;
- N2-ADD-120: connected-core recursion;
- N2-ADD-121: unique-parent streaming divisor theorem and record-gap compression.

At layer `t`, the allowable core gap is

\[
D_t(E_{t-1})
=
\left\lfloor
\frac{E_{t-1}+W_n+1}{2^{t-1}}
\right\rfloor.
\]

The recursion is now exactly certified for every

\[
12\le n\le46.
\]

N2-FIN-202 covers `12<=n<=45` by full-menu materialization. N2-FIN-203 covers `n=46` by a bounded-memory stream over `24,567,748` cores below `Y_46`, using only `631` record gaps and a maximum active frontier of `3,373,952` nodes.

At `n=46`, six main layers prove

\[
H_{46!}(\lfloor\sqrt{46!}\rfloor+1)
\le22.
\]

This engine is ranked third because it is sequential. Its finite success does not remove the Phase 12P audit, and a future failure would not disprove the full marker-three model unless the complete final sumset also fails.

Proofs:

- `proofs/MARKER_THREE_CARRIER_BLOCK_REDUCTION.md`;
- `proofs/MARKER_THREE_STREAMING_N46_AUDIT.md`.

Verification:

- `verification/marker_three_full_menu_audit.py`;
- `verification/marker_three_streaming_audit.cpp`.

### Rank 4: Three-power normalized valuation-tagged fallback

**Result label: conditional theorem with proved prefix.**

This is the former preferred route, governed by N2-ADD-116 through N2-ADD-118. It is `SUPERSEDED_AS_PREFERRED` but retained because its normalization, obstruction, repair, and binary-spine theorem are exact.

Marker-three is stronger on current evidence because it has a smaller lattice, wider correction window, lower term count, and exact finite endpoint coverage through `n=46`.

### Rank 5: Uniform rainbow convolution

**Result label: heuristic.**

One fixed mean leaves endpoints in large-deviation tails. It remains a benchmark, not the preferred architecture.

### Rank 6: Fixed-law local theorem as a standalone route

**Result label: heuristic.**

Fourier analysis remains essential inside the target-dependent route, but a single fixed law is not expected to cover both endpoints uniformly.

## Structural gate for marker-three

Accepted:

1. divisor legality under the stated valuation side condition;
2. numerical distinctness across layers;
3. main-palette disjointness;
4. exact lattice `3 Z`;
5. quotient span one;
6. correction radius `R_n=2^{r_n}-1`;
7. quotient radius `W_n=floor((R_n-2)/3)`;
8. first-target coverage;
9. term count `M_n+r_n`.

Still open:

1. uniform global quotient occupancy;
2. uniform endpoint reach near `Y_n`;
3. total-sum collision collapse;
4. final-only Fourier or deterministic sumset theorem;
5. Phase 12P audit for the sequential carrier engine;
6. all remaining finite exceptions.

## Deterministic and finite protected region

Nova 1 proves downward one-density through

\[
A_n=m_n(2^{M_n}-1),
\]

where `m_n` is the largest odd integer at most `n`. Nova 2 extends required target-window occupancy through `A_n+W_n`.

In addition, N2-FIN-202 and N2-FIN-203 prove complete quotient endpoint coverage for every `12<=n<=46`.

## Exact next targets

### Deterministic computational target

Reduce the N2-ADD-121 active frontier enough to certify `n=47`, or implement an external-memory frontier with an independently replayable certificate.

### Deterministic theorem target

Prove a uniform upper bound for record gaps of odd divisors of `n!/3` that forces

\[
E_{M_n}+W_n\ge Y_n.
\]

### Final-only analytic target

Prove the marker-three numerical weighted Fourier theorem on `[-pi,pi]` for every target beyond the deterministic protected region.

A failure of the carrier engine must not terminate the final-only route.
