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
- construction has a proved deterministic initial interval;
- exact complete-menu carrier certificates now succeed for every `12<=n<=45`.

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

This route would prove every final quotient window occupied without probabilistic approximation. It remains final-only and avoids a hidden sequential interval invariant.

Main blocker: available sumset theorems do not automatically preserve one choice per label, numerical distinctness, factorial legality, downward orientation, and endpoint location.

### Rank 3: Connected-core carrier recursion

**Result label: conditional theorem with exact finite certificates.**

Nova 2 proved N2-ADD-119 and N2-ADD-120.

At layer `t`, the exact allowable core gap is

\[
D_t(E_{t-1})
=
\left\lfloor
\frac{E_{t-1}+W_n+1}{2^{t-1}}
\right\rfloor.
\]

The recursion gives an exact certificate of how far translated carrier blocks cover and records the first blocking core gap.

N2-FIN-202 generated complete odd-core menus and certified full quotient reach for every

\[
12\le n\le45.
\]

Only two through six legal main layers were needed, giving the finite uniform bound

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le22
\]

on the completed range.

The largest completed case has `18,627,840` odd cores at `n=45`. The next case has `27,941,760` cores and requires a streaming or bounded-memory generator.

This engine remains ranked third because it is sequential. Finite success does not prove the asymptotic theorem, a future failure does not automatically disprove the full model, and any asymptotic success still requires the exact Phase 12P audit.

Proof and certificate:

- `proofs/MARKER_THREE_CARRIER_BLOCK_REDUCTION.md`;
- `proofs/MARKER_THREE_FINITE_FULL_MENU_AUDIT.md`;
- `verification/marker_three_full_menu_audit.py`.

Verification request:

`handoffs/MARKER_THREE_REQUEST_TO_NOVA4.md`.

### Rank 4: Three-power normalized valuation-tagged fallback

**Result label: conditional theorem with proved prefix.**

This is the former preferred route, governed by N2-ADD-116 through N2-ADD-118. It is now `SUPERSEDED_AS_PREFERRED` but retained because its normalization, obstruction, repair, and binary-spine theorem are exact.

Marker-three is better on the current evidence because it has a smaller lattice, wider correction window, lower term count, and successful complete-menu finite carrier certificates.

### Rank 5: Uniform rainbow convolution

**Result label: heuristic.**

One fixed mean leaves endpoints in large-deviation tails. It remains a benchmark, not the preferred architecture.

### Rank 6: Fixed-law local theorem as a standalone route

**Result label: heuristic.**

Fourier analysis remains essential inside the target-dependent route, but a single fixed law is not expected to cover both endpoints uniformly.

## Structural gate for marker-three

The following are accepted:

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

1. global asymptotic quotient occupancy;
2. uniform endpoint reach near `Y_n`;
3. total-sum collision collapse;
4. final-only Fourier or deterministic sumset theorem;
5. Phase 12P audit for the sequential carrier engine;
6. exact continuation beyond `n=45` and the remaining finite exceptions.

## Deterministic certified regions

Nova 1 proves downward one-density through

\[
A_n=m_n(2^{M_n}-1),
\]

where `m_n` is the largest odd integer at most `n`.

Nova 2 extends required target-window occupancy through

\[
A_n+W_n.
\]

In addition, N2-FIN-202 proves full quotient reach through `Y_n` for each `12<=n<=45` using complete menus. Computational and analytic work must distinguish this exact finite range from the asymptotic open region.

## Exact next theorem targets

There are three parallel valid targets.

### Streaming finite target

Implement a sorted odd-divisor stream or bounded-memory connected-component generator and continue exact full-menu certification from `n=46`.

### Uniform deterministic target

Prove a lower bound on the connected core in each layer strong enough to force

\[
E_{M_n}+W_n\ge Y_n.
\]

The finite terminal-layer saturation pattern is evidence, not a theorem.

### Final-only analytic target

Prove the marker-three numerical-value weighted Fourier theorem on `[-pi,pi]` for every target beyond the deterministic protected region.

A failure of the sequential carrier engine must not terminate the final-only route.
