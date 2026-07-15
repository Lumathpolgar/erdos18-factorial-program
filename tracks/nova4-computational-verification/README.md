# Nova 4: Computation, Falsification, and Verification

## Branch

`nova/computational-verification`

## Mission

Build the exact computational laboratory and independent verification system for the factorial program. Detect false conjectures early, generate reproducible evidence, and audit every theorem on the candidate proof path.

## Primary questions

1. What are the exact or certified values of relevant representation functions for feasible `n`?
2. Which structural features distinguish optimal representations from failed greedy or sequential constructions?
3. Which proposed lemmas fail first, and what are the smallest counterexamples?
4. Can every proof artifact and certificate be independently verified from raw data?

## Required baseline work

- Reconstruct all current definitions from `docs/COMMON_NOTATION.md`.
- Audit the archived Track B verifier and its fail-closed merge gate.
- Inventory reusable code and certificates from the historical packages.
- Build a clean environment specification before importing old code.

## Research program

### N4-A: Exact representation engine

Implement exact or certified computation of `lambda_{n!}(x)` over the largest feasible ranges. Use meet-in-the-middle, dynamic programming, integer programming, SAT, branch-and-bound, or hybrid methods as appropriate.

### N4-B: Construction simulator

Implement the candidate packet, layer, convolution, and correction constructions supplied by the other Novas. Verify divisor legality, distinctness, coverage, and term counts.

### N4-C: Counterexample search

Search systematically for failures of every conjectured monotonicity, density, occupancy, collision, and correction claim. Report the smallest witness found.

### N4-D: Statistical pattern mining

Measure valuation profiles, term-size distributions, layer usage, overlap structure, and residual behavior in exact or near-optimal representations. Clearly label all inferred patterns as evidence or heuristic.

### N4-E: Independent theorem audit

For every critical theorem:

- parse the frozen statement;
- reconstruct dependencies;
- test boundary cases;
- implement finite sanity checks;
- attempt adversarial falsification;
- record acceptance or failure.

## Forbidden shortcuts

- Floating-point equality may not verify exact sums.
- A solver's success status is not a certificate unless the witness is checked independently.
- Timeouts are not negative results.
- Random tests are not exhaustive tests.
- Precomputed metadata must not be trusted without recomputation.
- A finite pattern must not be promoted to an asymptotic claim.

## Deliverables

- `tracks/nova4-computational-verification/STATUS.md`
- `tracks/nova4-computational-verification/DATASETS.md`
- `tracks/nova4-computational-verification/VERIFIER_REGISTRY.md`
- `tracks/nova4-computational-verification/COUNTEREXAMPLES.md`
- environment and reproducibility instructions
- test suites for every accepted certificate format
- independent audit reports for integration gates

## Initial milestone

Create a reproducible baseline suite that:

- generates divisors of `n!` for feasible `n`;
- verifies individual representations;
- computes or bounds local representation lengths;
- compares greedy and non-greedy methods;
- imports selected historical certificates;
- rejects corrupted and duplicate-divisor certificates.

## Acceptance criteria

Nova 4 succeeds when it supplies:

1. a trusted verification framework used by all other tracks;
2. counterexamples or exact evidence that materially redirects research;
3. independent reconstruction of every theorem on the final proof path.
