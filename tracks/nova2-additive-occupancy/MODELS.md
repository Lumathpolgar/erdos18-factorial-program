# Nova 2 Additive Model Registry

## Model U: Uniform rainbow convolution

- Result label: `heuristic`
- Rank: 3
- File: `models/UNIFORM_RAINBOW_CONVOLUTION.md`
- Frozen object: product of uniform laws on pairwise numerically disjoint labels.
- Required conclusion: every correction window has positive final convolution mass.
- Main blocker: one fixed mean leaves endpoint windows in large-deviation tails.

## Model T: Target-dependent exponential tilt

- Result label: `conditional theorem`
- Rank: 1
- File: `models/TARGET_DEPENDENT_TILT.md`
- Frozen object: fixed labels with target-dependent Gibbs weights.
- Required conclusion: strict positive mass in `[x-R_n,x]` for every bulk target.
- Proof engine: N2-ADD-110 weighted Fourier comparison.
- Main blocker: a structurally compatible fixed label law, uniform tilt, variance, major arcs, minor arcs, and endpoint regime split.

## Model F: Fourier and local-limit occupancy

- Result label: `conditional theorem` as a proof engine, `heuristic` as a fixed-law standalone route.
- Rank: 4 as a standalone model.
- File: `models/FOURIER_LOCAL_LIMIT.md`
- Frozen object: integer-valued additive characteristic function on the torus `[-pi,pi]`, split into explicit major and minor arcs.
- Required inequality: weighted Fourier error strictly below reference window mass.
- Main blocker: target-uniform minor-arc control and every additional resonance on the bounded torus.
- Type restriction: the Fourier variable acts on numerical divisor sums, not on `log d`. Results for logarithmic divisor size require a separate transfer theorem.

## Model D: Deterministic restricted-sumset growth

- Result label: `conditional theorem`
- Rank: 2
- File: `models/DETERMINISTIC_RESTRICTED_SUMSET.md`
- Frozen object: final collision-free labeled sumset, with no partial interval invariant.
- Required conclusion: every correction window intersects the final sumset.
- Main blocker: existing additive theorems do not automatically preserve labeling, distinctness, interval location, or factorial legality.

## Rejected factorial instantiation V1

- Result label: `disproved model`
- Imported object: Nova 1 `N1-HO-N2-001`.
- Source branch: `nova/factorial-structure`.
- Source commit: `b939574eb88a08bb03abda5bbe6ff2ca97444e08`.
- Addresses: `e_t=r_n+t`, for `1<=t<=M_n`.
- Main support lattice: `2^{r_n+1} Z`.
- Requested correction radius: `2^{r_n}-1`.
- First failing target: `x=2^{r_n}`.
- Empty window: `[1,2^{r_n}]` contains no possible main sum.
- Proof: `proofs/VALUATION_TAGGED_LATTICE_OBSTRUCTION.md`.
- Handoff decision: `REJECTED` in `handoffs/RESPONSE_TO_NOVA1.md`.

This failure occurs before convolution, tilting, local limits, or finite computation. The fixed structural support must be revised.

## Cross-model proved obstructions

- Profile count does not imply coverage.
- Proper lattice span blocks residue classes.
- Ordinary convolution can count illegal collisions.
- Approximation error must be smaller than the main atom or window mass.
- Tilted Bernoulli variance collapses at both support endpoints.
- Target-dependent probability spaces are not one random universal object without a coupling.
- A correction radius smaller than the common lattice gap cannot repair every downward window.

Locations:

- `models/TOY_COUNTEREXAMPLES.md`
- `proofs/VALUATION_TAGGED_LATTICE_OBSTRUCTION.md`

## Cross-model proved sufficient conditions

- collision-free deterministic extraction;
- sampled-catalogue union bound;
- weighted Fourier window positivity;
- explicit discretized-Gaussian window lower bound;
- correction-window bridge.

Location: `models/TOY_SUFFICIENT_CONDITIONS.md`.

## Preferred hybrid

Use Model T for target centering, Model F for positive window mass, and a deterministic correction and endpoint architecture from Nova 1, but only after the label system passes the exact lattice compatibility gate N2-ADD-115.

## Mandatory evaluation fields

Every future candidate must record:

1. exact fixed labels;
2. divisor legality;
3. numerical disjointness;
4. term budget;
5. support range;
6. common lattice span and exact attained residues;
7. moments and maximal step;
8. target type: pointwise, windowed, almost-all, average, or finite;
9. correction width and term cost;
10. proof that the correction radius covers every remaining residue gap;
11. endpoint regimes, including the first requested target;
12. exact bounded-frequency analytic inequality;
13. whether the Fourier variable acts on numerical values or logarithmic values;
14. exact finite falsification task.