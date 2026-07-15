# Four-Nova Parallel Research Program

## Objective

Run four independent but interoperable research tracks against the factorial formulation of Erdős Problem 18:

\[
h(n!) < (\log n)^{O(1)}.
\]

The current sufficient local target is

\[
H_{n!}\!\left(\lfloor\sqrt{n!}\rfloor+1\right)=O((\log n)^2),
\]

which the archived conditional endgame converts into

\[
h(n!)=O((\log n)^3).
\]

The four tracks may improve, replace, or bypass this sufficient theorem, but every replacement must include a complete implication to the primary objective.

## Operating principle

The tracks work independently enough to generate genuinely different ideas, but they share exact definitions, theorem labels, evidence standards, and handoff formats. No track may silently modify another track's assumptions.

## Branches

1. `nova/factorial-structure`
2. `nova/additive-occupancy`
3. `nova/analytic-density`
4. `nova/computational-verification`

No Nova works directly on `main`. Each Nova commits only to its assigned branch and opens pull requests for reviewed artifacts.

## Track responsibilities

### Nova 1: Factorial Structure and Reduction

Owns deterministic decomposition of the divisor lattice of `n!`, exact reductions, correction mechanisms, and the master dependency graph.

### Nova 2: Additive Occupancy and Global Sumsets

Owns non-greedy additive constructions, rainbow sumsets, convolution methods, anti-concentration, and final-window occupancy.

### Nova 3: Analytic Divisor Density

Owns asymptotic divisor counts, short-interval estimates, valuation-profile estimates, smooth-number tools, saddle-point analysis, and distribution lemmas needed by other tracks.

### Nova 4: Computation, Falsification, and Verification

Owns exact computation, counterexample search, finite certificates, independent theorem verification, reproducible datasets, and integration tests.

## Shared phases

### Phase A: Baseline reconstruction

Each Nova must independently reconstruct:

- the exact definition of `h(N)` and `H_N(X)`;
- the conditional half-range-to-global implication;
- the distinction between the historical `L_m` route and the direct factorial route;
- all route eliminations from Phases 12K through 12P that are relevant to its work.

### Phase B: Track-specific theorem search

Each Nova pursues its own assigned theorem program. Results must be registered as proved, conditional, finite, computational, heuristic, or disproved.

### Phase C: Cross-track handoffs

A handoff occurs only when a result has exact hypotheses, quantifiers, constants or asymptotic ranges, and a verification artifact.

### Phase D: Integration

Candidate proof chains are assembled under `integration/`. No chain is accepted until Nova 4 or another independent reviewer reconstructs it without relying on the original author's prose.

## Non-duplication boundaries

- Nova 1 may formulate density requirements but does not claim analytic estimates without Nova 3 review.
- Nova 2 may use computational experiments but does not classify them as proof without Nova 4 verification.
- Nova 3 may derive counting estimates but does not assume they imply additive coverage without Nova 2 or Nova 1 supplying the bridge.
- Nova 4 may discover patterns but does not promote them to theorem status without a proof artifact.

## Success conditions

The program succeeds only when one of the following is complete and independently audited:

1. A proof that `h(n!) <= K (log n)^C` for absolute constants `K,C` and all sufficiently large `n`.
2. A stronger theorem that explicitly implies the same bound.
3. A direct proof of the current half-range target together with the audited conditional endgame.

Everything else is progress, not a solution.
