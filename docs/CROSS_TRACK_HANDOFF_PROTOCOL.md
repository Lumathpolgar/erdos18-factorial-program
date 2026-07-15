# Cross-Track Handoff Protocol

## Purpose

A handoff transfers a theorem, counterexample, dataset, or proof obligation from one Nova to another without transferring hidden assumptions.

## Handoff package

Every handoff must contain:

1. `HANDOFF.md`
2. the frozen theorem or conjecture statement;
3. dependency list;
4. proof, derivation, code, or dataset;
5. verifier instructions;
6. known limitations;
7. requested receiving-track action.

## Required `HANDOFF.md` fields

```text
Handoff ID:
Sending track:
Receiving track:
Date:
Result status:
Theorem or object IDs:
Exact claim:
Exact hypotheses:
Dependencies:
Files:
Verification command:
Known failure modes:
What is not claimed:
Requested next action:
```

## Handoff types

### Theorem handoff

Used when another track may rely on a proved or conditional result.

The receiver must independently check:

- quantifier order;
- asymptotic range;
- endpoint conventions;
- distinctness;
- dependency compatibility;
- whether the conclusion is actually sufficient for its intended use.

### Requirement handoff

Used when one track needs another track to prove a lemma. The requirement must state the weakest known sufficient conclusion, not an unnecessarily strong guess.

### Counterexample handoff

Used to retire a conjecture or construction. It must include a reproducible witness or a general proof of failure.

### Computational handoff

Used for data, exact certificates, searches, or numerical patterns. It must state whether the computation is exact, exhaustive, randomized, or heuristic.

## Receiver outcomes

The receiving track must record one of:

- `ACCEPTED`
- `ACCEPTED_WITH_RESTRICTIONS`
- `REJECTED`
- `NEEDS_REPAIR`
- `SUPERSEDED`

Silence is not acceptance.

## Branch workflow

1. Sender commits the handoff package to its own branch.
2. Sender opens a pull request or creates a handoff issue linking the exact commit.
3. Receiver reviews without changing the sender's theorem statement.
4. Corrections are made on the sender's branch or in a new revision.
5. Accepted handoffs are registered under `integration/THEOREM_REGISTRY.md` and `integration/HANDOFF_QUEUE.md`.

## Versioning

Theorem statements are immutable after acceptance. A changed hypothesis or conclusion receives a new theorem ID or version suffix.

Example:

```text
N3-DENS-04-v1
N3-DENS-04-v2
```

## No circular handoffs

A theorem may not depend, directly or indirectly, on itself. The integration maintainer must reject any dependency cycle unless it is explicitly an induction with a well-founded decreasing parameter and a complete base case.
