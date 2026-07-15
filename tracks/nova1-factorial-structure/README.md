# Nova 1: Factorial Structure and Reduction

## Branch

`nova/factorial-structure`

## Mission

Exploit the full prime-valuation structure of `n!` to build deterministic representation frameworks and exact reductions for the factorial formulation of Erdős Problem 18.

## Primary questions

1. Which decompositions of the divisor lattice of `n!` preserve distinctness while providing many controlled scales?
2. Can every target below `sqrt(n!)` be reduced to a bounded collection of structured subtargets with total polylogarithmic representation cost?
3. Can a correction palette be reserved without destroying the main construction's entropy?
4. Is the current half-range target optimal for the completed endgame, or can a weaker local theorem suffice?

## Required baseline work

- Reconstruct the definition of `H_N(X)` from `docs/COMMON_NOTATION.md`.
- Reconstruct the archived Track B local-to-global implication.
- Audit every use of `L_m` and remove it from direct factorial assumptions.
- Summarize the factorial valuation budget
  \[
  v_p(n!)=\sum_{j\ge1}\left\lfloor\frac{n}{p^j}\right\rfloor.
  \]
- Build a dependency graph for all proposed structural lemmas.

## Research program

### N1-A: Valuation-band decomposition

Partition primes and prime powers into bands that create divisor families across controlled logarithmic scales. Determine exact valuation budgets and cross-band distinctness rules.

### N1-B: Deterministic packet design

Construct packets or layers of divisors with explicit selection rules. Avoid the one-choice sequential flat-gap architecture disproved in Phase 12P unless a new ingredient breaks its hypotheses.

### N1-C: Correction architecture

Find a palette-disjoint correction mechanism for residual intervals. Prove legality, distinctness, and exact term cost.

### N1-D: Reduction improvement

Search for direct reductions from the full interval `[0,n!)` to smaller local intervals that use factorial-specific structure and improve on the current cubic logarithmic endgame.

### N1-E: Theorem contracts for other tracks

State the weakest analytic density and additive occupancy lemmas sufficient for the structural construction. Do not request stronger statements without reason.

## Forbidden shortcuts

- Raw divisor count is not interval coverage.
- A formal mixed-radix system is invalid unless all digit terms are distinct divisors of `n!`.
- Independent recursive subproblems must include their total term cost.
- Reusing the same divisor in different packets is forbidden.
- Finite constructions do not establish the asymptotic theorem.

## Deliverables

- `tracks/nova1-factorial-structure/STATUS.md`
- `tracks/nova1-factorial-structure/THEOREMS.md`
- `tracks/nova1-factorial-structure/CONSTRUCTIONS.md`
- `tracks/nova1-factorial-structure/OPEN_REQUIREMENTS.md`
- proof files for every promoted theorem
- handoffs to Nova 2 and Nova 3 with exact sufficient statements

## Initial milestone

Produce a rigorous factorial divisor-lattice atlas that states:

- available prime-power budgets by band;
- numerical ranges of generated divisors;
- collision criteria;
- maximum number of selectable terms;
- exact missing additive theorem needed for half-range coverage.

## Acceptance criteria

Nova 1 succeeds when it supplies either:

1. a complete proof of the factorial half-range theorem;
2. a deterministic structural reduction whose remaining lemmas are precise and independently plausible;
3. a proof that a proposed structural route cannot reach a polylogarithmic term count.
