# Nova 2 Baseline Obstruction Audit

## Result status

This document is a research audit. Statements imported from the archive are not promoted beyond the status recorded in the repository.

## Repository and branch baseline

- Repository: `Lumathpolgar/erdos18-factorial-program`
- Working branch: `nova/additive-occupancy`
- Branch head at startup: `71370633b1e6726bf6f9e3b334d42cfc34512c06`
- Main head at startup: `68ace6c9c3b67636e298a406fee3bfe8e072741d`
- Merge base: `cd5576d4f7934e26e9d4ef3b065c2ad4cee36c67`
- Startup comparison: branch 4 commits ahead and 12 commits behind `main`
- Main-only changes at startup were branch-registry, next-step, and prompt files. The frozen mathematical definition files read for this audit matched the branch baseline.
- The requested path `docs/HANDOFF_PROTOCOL.md` does not exist. The repository protocol actually present and used is `docs/CROSS_TRACK_HANDOFF_PROTOCOL.md`.

No result from another Nova branch is imported in this checkpoint.

## Frozen definitions and endpoint conventions

For a positive integer `N`,

\[
\mathcal D(N)=\{d\in\mathbb Z_{>0}:d\mid N\}.
\]

For an integer `x\ge 0`,

\[
\lambda_N(x)=\min\left\{|S|:S\subseteq\mathcal D(N),\ \sum_{d\in S}d=x\right\},
\]

with `lambda_N(x)=infinity` if no representation exists. The empty set represents `0`.

For real `X\ge 1`,

\[
H_N(X)=\max_{0\le x<X,\ x\in\mathbb Z}\lambda_N(x).
\]

Thus

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
\]

covers every integer target

\[
0\le x\le \lfloor\sqrt{n!}\rfloor.
\]

All representations use numerically distinct positive divisors. Labeled copies of the same numerical divisor do not count as distinct.

For labeled finite families `A_1,...,A_k\subseteq\mathcal D(n!)`, define the collision-free restricted rainbow sumset

\[
\Sigma^{\!*}(A_1,\ldots,A_k)
=
\left\{
\sum_{i=1}^k a_i:
 a_i\in A_i\cup\{0\},
 a_i=a_j\ne 0\Rightarrow i=j
\right\}.
\]

Intermediate partial sums are not required to cover intervals.

## Current candidate proof chain

The repository's present sufficient chain is:

1. Prove absolute constants `K_0,n_0` such that for every `n\ge n_0` and every integer
   \[
   0\le x\le\lfloor\sqrt{n!}\rfloor,
   \]
   the target `x` is a sum of at most `K_0(\log n)^2` distinct divisors of `n!`.
2. Reconstruct and audit the conditional Track B local-to-global conversion under the current definition of `H_N`.
3. Conclude
   \[
   h(n!)=O((\log n)^3).
   \]

The open node owned by this track is the global additive mechanism in Step 1.

## Reconstruction of the late additive failures

The repository contains indexed summaries of Phases 12M through 12P, not the full source packages or source-level theorem statements. Consequently, the contracts below distinguish the recorded result from the exact quantitative constants that remain unavailable in the repository.

### Phase 12M: capacity survives, separability fails

**Result label: disproved model.**

Recorded conclusion:

- a legal marked-layer atlas may have enough raw combinatorial profiles;
- independently decoded CRT atlases are insufficient;
- separable recursive constructions are insufficient.

Reconstructed no-go hypotheses:

1. the global state is decomposed into independently decoded coordinate or CRT blocks;
2. the effective number of usable outcomes factors through the independent block counts;
3. no globally coupled decoding step recovers information lost by the separate decoders;
4. or, in the recursive version, each stage communicates only a separable summary to later stages.

What the obstruction does not cover:

- a single global convolution whose support is analyzed only after all labels are combined;
- target-dependent measures coupling all labels through one tilt parameter;
- Fourier cancellation or local-limit control for the final sum;
- deterministic restricted-sumset growth that is not expressible as a product of independent decoded capacities.

Missing source item: the exact quantitative effective-capacity inequality from the Phase 12M package is not present in this repository and is not asserted here.

### Phase 12N: high-prime atlas and shell-gap obstruction

**Result label: disproved model.**

Recorded conclusion:

- the original magnitude-separated high-prime atlas misses the first target immediately beyond its correction range for an infinite family;
- a correction palette disjoint from the main atlas repairs that first-entry defect;
- the high-prime construction still has an unavoidable additive shell gap.

Reconstructed no-go hypotheses:

1. main choices are confined to magnitude-separated high-prime shells;
2. the correction palette is bounded to a lower residual range and remains disjoint from the main terms;
3. attainable sums formed from the allowed shell choices leave a gap between consecutive global shells larger than the correction radius;
4. the construction does not mix enough scales inside the same final sum to bridge that gap.

What the obstruction does not cover:

- mixed-scale labels;
- target-dependent tilting over overlapping numerical scales;
- a final global sumset whose support is dense despite sparse individual shells;
- deterministic cross-shell coupling.

Missing source item: the exact infinite family and shell-gap formula are not present in the repository index and are not reconstructed as a frozen theorem here.

### Phase 12O: mixed-scale shared-core ladder

**Result label: finite certificate.**

Recorded conclusion:

- a mixed-scale shared-core construction removes the earlier quadratic-to-cubic shell gap;
- exact interval-extension certificates succeed over the tested finite range;
- no asymptotic occupancy theorem was proved.

Exact limitation:

Finite success does not imply a uniform theorem in `n`, does not supply a pointwise lower bound for every target, and does not by itself control the number of layers asymptotically.

Surviving information:

Mixed scales and shared global structure are viable design features and should not be discarded merely because the earlier high-prime atlas failed.

### Phase 12P: one-choice sequential shared-core ladder

**Result label: disproved model.**

Recorded conclusion:

A one-choice sequential shared-core ladder requires at least

\[
\Omega(\log m\log\log m)
\]

layers before reaching the required range, because smooth-number counting bounds the number of useful choices per layer.

Reconstructed no-go hypotheses:

1. layers are processed sequentially;
2. at most one choice is taken from each layer;
3. each stage must extend the currently covered range before the next stage is used;
4. useful choices per layer are bounded by the relevant smooth-number count;
5. the proof budget requires `O(log m)` layers.

What the obstruction does not cover:

- final-only coverage with no interval invariant for partial sums;
- a global convolution using all labels at once;
- target-dependent selection laws;
- nonsequential restricted-sumset theorems;
- a direct factorial construction exploiting the full valuation multiplicity of `n!` rather than the historical `L_m` architecture.

## Precise lessons for Nova 2

The following implications are invalid without proof:

- profile count larger than the target interval implies coverage;
- a Gaussian-looking histogram implies a local theorem;
- average spacing implies maximum-gap control;
- positive density or almost-all coverage implies every-target coverage;
- positive ordinary convolution mass implies a valid distinct-divisor representation when labels overlap numerically;
- a targetwise probabilistic model automatically gives one deterministic object covering every target;
- final global occupancy can be replaced by a sequential partial-interval invariant.

## Global nonsequential models still outside the obstructions

1. Collision-free uniform rainbow convolution analyzed only at the final sum.
2. Target-dependent exponential tilting with a parameter chosen separately for each target.
3. Lattice-aware Fourier inversion or a short-window local limit theorem for the final sum.
4. Deterministic restricted-sumset growth or inverse-theorem methods with no sequential coverage invariant.
5. A hybrid final-window occupancy theorem plus a numerically disjoint correction palette.
6. A globally coupled distribution on valid rainbow tuples, rather than a product measure whose positive mass may include collisions.

## Baseline blocker list

1. The repository does not yet contain source-level statements from the Phase 12M through 12P ZIP packages.
2. No frozen factorial layer family from Nova 1 is available on this branch.
3. No uniform major-arc, minor-arc, variance, or lattice theorem from Nova 3 is available.
4. No exact finite falsification queue has yet been implemented by Nova 4.
5. The branch is behind `main` in prompt and operating files, although the mathematical definition baseline used here is unchanged.

## First independent theorem target

Develop a collision-free, target-dependent window occupancy theorem whose hypotheses are stated entirely in terms of:

- pairwise numerical disjointness;
- correction radius;
- lattice span;
- a target-centered tilted law;
- a quantitative Fourier or local-limit error smaller than an explicit reference window mass.

Such a theorem remains globally nonsequential and is not ruled out by Phases 12M through 12P.
