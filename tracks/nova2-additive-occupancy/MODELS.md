# Nova 2 Additive Model Registry

## Model QV: Normalized valuation-tagged quotient occupancy

- Model ID: `N2-MOD-QV-001`.
- Result label: `conditional theorem` as a repaired reduction.
- Rank: 1, conditional on Nova 1 structural acceptance.
- File: `models/VALUATION_TAGGED_QUOTIENT_MODEL.md`.
- Source construction: Nova 1 full-menu valuation-tagged packets, inspected at head `fa11f4b2cb86a2dd791df189ada12757be791804`.
- Common factor removed:
  \[
  g_n=2^{r_n+1}.
  \]
- Frozen quotient labels:
  \[
  B_t(n)=\{2^{t-1}u:u\mid n!,\ u>1\text{ odd},\ g_n2^{t-1}u\le X_n\}.
  \]
- Repaired correction palette:
  \[
  \{2^0,2^1,\ldots,2^{r_n+2}\}.
  \]
- Exact required conclusion:
  \[
  Q_n\cap[\max(0,m-3),m]\ne\varnothing
  \]
  for every quotient target through `floor(X_n/g_n)`.
- Term budget after success: `M_n+r_n+3`.
- Proof engine: target-dependent tilt plus bounded-torus Fourier comparison, or a deterministic final-sumset theorem.
- Main blockers: Nova 1 repair acceptance, quotient span and resonance audit, four-point local mass, endpoints, finite exceptions.

## Model U: Uniform rainbow convolution

- Result label: `heuristic`.
- Rank: 4.
- File: `models/UNIFORM_RAINBOW_CONVOLUTION.md`.
- Frozen object: product of uniform laws on pairwise numerically disjoint labels.
- Required conclusion: every correction window has positive final convolution mass.
- Main blocker: one fixed mean leaves endpoint windows in large-deviation tails.

## Model T: Target-dependent exponential tilt

- Result label: `conditional theorem`.
- Rank: 2 as a general architecture and the preferred probabilistic engine inside Model QV.
- File: `models/TARGET_DEPENDENT_TILT.md`.
- Frozen object: fixed labels with target-dependent Gibbs weights.
- Current exact law: exponential tilt on the normalized numerical labels `B_t(n)`.
- Current exact target window: `[max(0,m-3),m]`.
- Proof engine: N2-ADD-110 weighted Fourier comparison.
- Main blocker: uniform tilt, variance, major arcs, minor arcs, resonances, and endpoint regime split for the quotient model.

## Model F: Fourier and local-limit occupancy

- Result label: `conditional theorem` as a proof engine, `heuristic` as a fixed-law standalone route.
- Rank: 5 as a standalone model.
- File: `models/FOURIER_LOCAL_LIMIT.md`.
- Frozen object: integer-valued additive characteristic function on the torus `[-pi,pi]`, split into explicit major and minor arcs.
- Current exact characteristic function:
  \[
  \Phi_{n,m}(\theta)=\mathbb E e^{i\theta T_{n,m}}.
  \]
- Required inequality: weighted Fourier error strictly below the reference four-point window mass.
- Main blocker: target-uniform minor-arc control and every additional resonance on the bounded torus.
- Type restriction: the Fourier variable acts on numerical quotient sums, not on `log d`. Results for logarithmic divisor size require a separate transfer theorem.

## Model D: Deterministic restricted-sumset growth

- Result label: `conditional theorem`.
- Rank: 3.
- File: `models/DETERMINISTIC_RESTRICTED_SUMSET.md`.
- Frozen object: final collision-free labeled sumset, with no partial interval invariant.
- Current exact target: prove maximum downward gap at most `3` in the final quotient sumset `Q_n`.
- Main blocker: existing additive theorems do not automatically preserve labeling, distinctness, interval location, or factorial legality.

## Rejected factorial instantiation V1

- Result label: `disproved model`.
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

## Rejected repair variants V1-A and V1-B

- Result label: `disproved model`.
- The original palette extended only through `2^{r_n}` still misses target `g_n=2^{r_n+1}`.
- The original palette extended through `2^{r_n+1}` still misses target `2g_n`.
- The failures are exact and independent of menu size or analytic estimates.
- Result ID: `N2-OBS-108`.
- Proof: `proofs/LATTICE_QUOTIENT_NORMALIZATION.md`.

## Cross-model proved obstructions

- Profile count does not imply coverage.
- Proper lattice span blocks residue classes.
- Ordinary convolution can count illegal collisions.
- Approximation error must be smaller than the main atom or window mass.
- Tilted Bernoulli variance collapses at both support endpoints.
- Target-dependent probability spaces are not one random universal object without a coupling.
- A correction radius smaller than the common lattice gap cannot repair every downward window.
- After quotient normalization, correction range `[0,Lg-1]` can bridge only quotient downward gaps at most `L-1`.
- One-power and two-power consecutive-binary repairs fail the minimum-support test.

Locations:

- `models/TOY_COUNTEREXAMPLES.md`
- `proofs/VALUATION_TAGGED_LATTICE_OBSTRUCTION.md`
- `proofs/LATTICE_QUOTIENT_NORMALIZATION.md`

## Cross-model proved sufficient conditions

- collision-free deterministic extraction;
- sampled-catalogue union bound;
- weighted Fourier window positivity;
- explicit discretized-Gaussian window lower bound;
- correction-window bridge;
- lattice quotient normalization;
- the conditional three-power repair implication.

Locations:

- `models/TOY_SUFFICIENT_CONDITIONS.md`;
- `proofs/LATTICE_QUOTIENT_NORMALIZATION.md`.

## Preferred hybrid

Use Model QV as the exact construction. Inside it, use Model T for target centering, Model F for positive four-point window mass, and the repaired deterministic binary palette for exact residual completion. Model D remains the preferred nonanalytic alternative.

## Mandatory evaluation fields

Every future candidate must record:

1. exact fixed labels;
2. divisor legality;
3. numerical disjointness;
4. term budget;
5. support range;
6. common lattice span and exact attained residues;
7. quotient normalization when a common span exists;
8. moments and maximal step;
9. target type: pointwise, windowed, almost-all, average, or finite;
10. correction width and term cost;
11. proof that the correction radius covers every remaining quotient gap;
12. endpoint regimes, including the first requested target;
13. exact bounded-frequency analytic inequality;
14. whether the Fourier variable acts on numerical values or logarithmic values;
15. exact finite falsification task;
16. whether the argument is final-only or secretly sequential.
