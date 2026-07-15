# Master Integration Plan

## Purpose

Assemble accepted results from the four Nova tracks into a single auditable proof chain for

\[
h(n!)<(\log n)^{O(1)}.
\]

## Current candidate chain

The present sufficient chain is:

1. Direct factorial half-range theorem
   \[
   H_{n!}(\lfloor\sqrt{n!}\rfloor+1)=O((\log n)^2).
   \]
2. Audited Track B conversion.
3. Global conclusion
   \[
   h(n!)=O((\log n)^3).
   \]

The local theorem is open. The conversion is conditional and must be reconstructed under the repository's frozen notation.

## Integration roles

- Nova 1 supplies structural constructions and reductions.
- Nova 2 supplies additive coverage or occupancy.
- Nova 3 supplies analytic estimates.
- Nova 4 independently verifies statements, code, and finite exceptions.

## Candidate proof bundle

A candidate proof bundle must contain:

- `STATEMENT.md`
- `DEPENDENCIES.md`
- `PROOF.md`
- `BOUNDARY_CASES.md`
- `FINITE_EXCEPTIONS.md`
- `EXTERNAL_RESULTS.md`
- `AUDIT_1.md`
- `AUDIT_2.md`
- code and certificate references where applicable

## Assembly procedure

1. Freeze all component theorem statements.
2. Build a directed acyclic dependency graph.
3. Check every implication locally.
4. Normalize notation and endpoints.
5. Sum every term-cost contribution.
6. Verify distinctness across the entire construction, not only within individual modules.
7. Resolve transition ranges between asymptotic regimes.
8. Handle finite exceptions.
9. Run independent reconstruction audits.
10. Apply every gate in `docs/INTEGRATION_GATES.md`.

## Competing proof chains

Multiple chains may coexist. Each receives a chain ID:

```text
CHAIN-A
CHAIN-B
CHAIN-C
```

A chain document must state which open nodes remain. A chain with an open node is conditional.

## Merge policy

A component may be merged into the integration record when its statement and status are stable. This does not imply that the main theorem is proved.

The final-solution branch should be created only after one chain has no open nodes and passes Gates 0 through 10.

## Current status

- Direct factorial local theorem: `OPEN`
- Track B conversion: `CONDITIONAL`, archived and previously audited
- End-to-end proof: `OPEN`
- Solution claim: prohibited
