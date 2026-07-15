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
- Main blocker: uniform tilt, variance, major arcs, minor arcs, and endpoint regime split.

## Model F: Fourier and local-limit occupancy

- Result label: `conditional theorem` as a proof engine, `heuristic` as a fixed-law standalone route.
- Rank: 4 as a standalone model.
- File: `models/FOURIER_LOCAL_LIMIT.md`
- Frozen object: lattice characteristic function split into explicit major and minor arcs.
- Required inequality: weighted Fourier error strictly below reference window mass.
- Main blocker: target-uniform minor-arc control and additional resonances.

## Model D: Deterministic restricted-sumset growth

- Result label: `conditional theorem`
- Rank: 2
- File: `models/DETERMINISTIC_RESTRICTED_SUMSET.md`
- Frozen object: final collision-free labeled sumset, with no partial interval invariant.
- Required conclusion: every correction window intersects the final sumset.
- Main blocker: existing additive theorems do not automatically preserve labeling, distinctness, interval location, or factorial legality.

## Cross-model proved obstructions

- Profile count does not imply coverage.
- Proper lattice span blocks residue classes.
- Ordinary convolution can count illegal collisions.
- Approximation error must be smaller than the main atom or window mass.
- Tilted Bernoulli variance collapses at both support endpoints.
- Target-dependent probability spaces are not one random universal object without a coupling.

Location: `models/TOY_COUNTEREXAMPLES.md`.

## Cross-model proved sufficient conditions

- collision-free deterministic extraction;
- sampled-catalogue union bound;
- weighted Fourier window positivity;
- explicit discretized-Gaussian window lower bound;
- correction-window bridge.

Location: `models/TOY_SUFFICIENT_CONDITIONS.md`.

## Preferred hybrid

Use Model T for target centering, Model F for the proof of positive window mass, and a deterministic correction and endpoint architecture from Nova 1.

## Mandatory evaluation fields

Every future candidate must record:

1. exact fixed labels;
2. divisor legality;
3. numerical disjointness;
4. term budget;
5. support range;
6. lattice span and residues;
7. moments and maximal step;
8. target type: pointwise, windowed, almost-all, average, or finite;
9. correction width and term cost;
10. endpoint regimes;
11. exact analytic inequality;
12. exact finite falsification task.
