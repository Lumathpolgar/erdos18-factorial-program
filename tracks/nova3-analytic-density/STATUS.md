# Nova 3 Status

## Track and branch

- Track: Analytic Divisor Density
- Branch: `nova/analytic-density`
- Main head inspected at startup: `68ace6c9c3b67636e298a406fee3bfe8e072741d`
- Merge base: `cd5576d4f7934e26e9d4ef3b065c2ad4cee36c67`
- No merge to `main`, force push, rebase, or edit to another Nova branch

## Overall state

`SIXTH_SUBSTANTIVE_CHECKPOINT_COMPLETE`

The factorial half-range theorem and Erdős Problem 18 remain open.

## Current cross-track sources

### Nova 1

- branch: `nova/factorial-structure`
- exact head inspected: `e3a0e3f5fb335b23afdd9e1fe418ac46ca1c766a`
- active construction: `N1-CON-003`
- new relevant results: `N1-STR-020`, `N1-DIS-006`, `N1-COL-001`

The marker-three numerical labels remain unchanged. Nova 1 now proves endpoint support, a one-factorial-block carrier ceiling, and explicit exponential carry collisions.

### Nova 2

- branch: `nova/additive-occupancy`
- exact head inspected: `82603c631a106c3bff4676bdeeb9cc791fc98f3c`
- active request: `N2-HO-N3-003`
- relevant results: `N2-ADD-119`, `N2-ADD-120`, `N2-FIN-202`

Nova 2 proves deterministic marker-three quotient-window coverage through

\[
P_n=m_n(2^{M_n}-1)+W_n.
\]

Its complete-menu finite audit reaches the full endpoint for every `12<=n<=45`. The asymptotic final-only analytic responsibility begins at

\[
P_n+1\le q\le Y_n.
\]

## Previously closed numerical foundations

### N3-ANA-017

The active Nova 2 law remains compatible with the latest inspected Nova 1 construction.

### N3-ANA-018

For every `W_n<q<=Y_n`, the common numerical exponential family has a unique finite tilt centered at

\[
q-W_n/2.
\]

The exact additive span is one and the only exact torus resonance is zero.

### N3-ANA-019

No fixed nonzero-frequency modulus gap can hold uniformly over all real tilts, because the law freezes at both tilt endpoints.

Proof:

`proofs/MARKER_THREE_NUMERICAL_LAW_FOUNDATIONS.md`.

## New theorem N3-ANA-020: post-prefix tilt compression

For

\[
L_n=m_n(2^{M_n}-1),
\]

and every integer target

\[
P_n+1\le q\le Y_n,
\]

the exact centering tilt satisfies

\[
-\frac{8M_n\log L_n}{L_n}
<\lambda_{n,q}<
\frac{16(n\log n+\log14)}{2^{M_n}}.
\]

Consequently

\[
\sup_{P_n<q\le Y_n}|\lambda_{n,q}|\to0.
\]

This closes the compact-tilt clause on the exact post-prefix target range.

The negative bound comes from a convex partition-function estimate valid for arbitrary subsets of the dyadic layer lattices. The positive bound uses four highest layers and Nova 1 endpoint support values exceeding `Y_n/3`.

Proof:

`proofs/POST_PREFIX_TILT_AND_COLLISION.md`.

## New obstruction N3-ANA-021: binary-anchor collapse

At zero tilt,

\[
P_0(Z_t=0)P_0(Z_t=2^{t-1})
<2^{-2(h_n-1)}
\le2^{-2(n/(3\log n)-1)}.
\]

Thus the exact zero-versus-minimum-state characteristic-function bound from N3-ANA-018 does not become quantitative merely because the target tilts tend uniformly to zero.

At `n=120368`, the proved coefficient ceiling is below `10^{-2064}`.

The next minor-arc proof must aggregate many phase-separated states or exploit a quantitative odd-core divisor-gap theorem.

## New theorem N3-ANA-022: collision-aware tilted atoms

For profile multiplicity

\[
C_n(s)=\#\{\text{legal profiles summing to }s\},
\]

the exact tilted atom is

\[
P_\lambda(T_{n,\lambda}=s)
=
\frac{C_n(s)e^{\lambda s}}
{\prod_tZ_t(\lambda)}.
\]

Nova 1 theorem `N1-COL-001` gives

\[
C_n(4^{\lfloor M_n/2\rfloor}-1)
\ge2^{\lfloor M_n/2\rfloor}.
\]

Therefore any local reference law must account for numerical fiber multiplicity. Treating profiles as distinct sums is invalid.

## Verification

```text
python3 tracks/nova3-analytic-density/proofs/scale_sanity.py
python3 tracks/nova3-analytic-density/proofs/prime_interval_capacity_sanity.py
python3 tracks/nova3-analytic-density/proofs/compact_tilt_sanity.py
python3 tracks/nova3-analytic-density/proofs/marker_three_capacity_sanity.py
python3 tracks/nova3-analytic-density/proofs/marker_three_numerical_law_sanity.py
python3 tracks/nova3-analytic-density/proofs/post_prefix_tilt_sanity.py
```

### N3-FIN-006

At `n=120368`, the verifier confirms:

- the post-prefix range is nonempty;
- `3*2^(M_n-1)<=X_n`;
- the negative-bound algebra is valid;
- exact minimal-support collision enumeration with four layer pairs gives multiplicity `34` at target `255`, exceeding the required `16`.

### N3-COMP-005

Selected post-prefix tilt scales:

| `n` | `log10` lower magnitude | `log10` upper magnitude |
|---:|---:|---:|
| 120368 | -656.908 | -651.903 |
| 200000 | -715.455 | -710.064 |
| 500000 | -827.710 | -821.618 |
| 1000000 | -917.629 | -911.001 |

These scale rows are computational evidence supporting the proved asymptotic bounds.

## Current theorem frontier

| IDs | State |
|---|---|
| N3-ANA-004 through N3-ANA-010 | Exact product, local ceiling, distribution, high-prime results, and explicit prime interval |
| N3-ANA-011 | Old-address capacity proved but structural model superseded |
| N3-ANA-012 | Compact-tilt top-prime logarithmic coarse windows proved |
| N3-ANA-013 | Unit-tilt Gaussian route disproved |
| N3-ANA-014 and N3-ANA-015 | Repaired marker-three capacity proved |
| N3-ANA-016 | Invalid central-binomial shortcut disproved |
| N3-ANA-017 and N3-ANA-018 | Numerical contract, centering, span, and exact resonances proved |
| N3-ANA-019 | Uniform all-tilt minor-arc gap disproved |
| N3-ANA-020 | Uniform post-prefix tilt compression proved |
| N3-ANA-021 | Single binary-anchor quantitative route disproved |
| N3-ANA-022 | Collision-aware atom formula proved |

## Cross-track state

### Nova 1

The repaired capacity request remains closed. Nova 1's endpoint, block-ceiling, and carry-collision theorems are now imported into the numerical analysis.

### Nova 2

Closed clauses:

- exact asymptotic transition from deterministic coverage to analytic responsibility;
- tilt existence and uniqueness;
- compact post-prefix tilt;
- exact additive span;
- exact resonance set;
- exact collision factor in local atoms.

Open clauses:

- aggregate phase dispersion for the complete odd-core menus;
- uniform variance, third-moment, and maximal-step bounds;
- target-local collision or additive-energy control;
- reference lattice law;
- strict weighted Fourier inequality.

### Nova 4

Independent reconstruction is required through N3-ANA-022 and N3-FIN-006.

## Exact blockers

1. The common tilt is now controlled, but the individual zero-versus-minimum-state probabilities collapse at zero tilt.
2. A viable minor-arc theorem must aggregate many numerical support pairs or prove phase dispersion from complete odd-core divisor structure.
3. Exponential carry collisions require a collision-aware reference law or an upper bound on target-local fiber energy.
4. Constant-width windows require a local torus error smaller than order `1/sigma`; distribution-distance Berry-Esseen is insufficient.
5. Fine top-prime logarithmic windows remain open but secondary.
6. Phase 12L and Phase 12P source packages remain unavailable.
7. The branch remains divergent from `main`.

## Handoffs

- `handoffs/RESPONSE_TO_NOVA1.md`
- `handoffs/RESPONSE_TO_NOVA1_MARKER_THREE.md`
- `handoffs/RESPONSE_TO_NOVA2_MARKER_THREE.md`
- `handoffs/TO_NOVA1_COMPACT_TILT.md`
- `handoffs/TO_NOVA2.md`
- `handoffs/TO_NOVA2_COMPACT_TILT.md`
- `handoffs/TO_NOVA4.md`
- `handoffs/TO_NOVA4_COMPACT_TILT.md`
- `handoffs/TO_NOVA4_MARKER_THREE.md`

## Next theorem target

`N3-NEXT-006`: prove an aggregate phase-dispersion lower bound for the complete marker-three odd-core menus on the post-prefix tilt range. The first candidate is a multistate variance identity based on many pairs with a common odd-core difference. If such a bound fails, return an explicit target-local concentration or collision-energy obstruction.