# Preferred Route Addendum: Checkpoint 010

## Decision

- Route ID: `N3-ROUTE-009`
- Final quotient occupancy: `OPEN`

## Active route

The exact odd-lattice normalized numerical law remains the preferred final-only model.

The dyadic part of the transformed Fourier problem now separates into two regions.

### Central-lobe region

For

\[
j\ge\rho_n-2,
\]

the dyadic ladder point lies inside the first transformed interval-kernel lobe.

These points must be absorbed into the central major-arc and reference-law analysis. They are not separate secondary minor arcs.

### Secondary dyadic region

Only

\[
1\le j\le\rho_n-3
\]

remain.

At each such scale, select transformed coordinate `1` when `j=1`, and transformed layer `j` when `j>=2`.

Multiplication of the selected positive odd core by `3` reverses its phase. Consecutive 3-adic chains reduce the selected factor, and therefore the complete transformed product, to one endpoint probability:

- lower endpoint under nonpositive tilt;
- upper endpoint under nonnegative tilt.

## Next required theorem

Prove a target-uniform gap for the sign-appropriate endpoint mass:

\[
P(B^{\operatorname{sgn}}_{n,q,j})
\le1-\varepsilon_{n,j}.
\]

The gap must be strong enough after summation over the `rho_n-3` secondary scales and must remain valid in the neighborhoods weighted by the transformed interval kernel.

Candidate inputs:

1. a factorial-specific weighted count of 3-free legal cores;
2. a weighted count of top-of-chain cores blocked by the numerical cutoff;
3. a sign theorem for the post-prefix tilt, eliminating one endpoint family;
4. a mean or entropy inequality forcing non-endpoint mass in the selected layer;
5. a direct neighborhood chain estimate retaining paired weight differences.

## Rejected substitutions

The following do not close the theorem:

- exact residue support;
- a fixed low-state carrier;
- a count of legal 3-adic chains without weighted endpoint mass;
- the small zero-state bound alone;
- exact pointwise control without neighborhood stability;
- logarithmic divisor density in place of numerical weights.

## Parallel requirements

The final theorem still requires:

- non-dyadic rational resonance audit;
- transformed moment estimates;
- collision-aware reference law;
- strict transformed weighted Fourier comparison.

## Stop condition

If the sign-appropriate endpoint mass can approach one along an exact post-prefix target sequence, freeze that sequence as a full-law dyadic obstruction instead of continuing a false contraction route.