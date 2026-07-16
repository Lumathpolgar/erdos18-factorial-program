# Nova 4 Open Requirements

## N4-REQ-N3-001

Owner: Nova 3

Superseding handoff: `N3-HO-N4-002`

Handoff commit: `7469dada02fa4caca08ed391ef8b0cb0f1e855b2`

Status: `COMPLETE`

Independent final decisions now exist for every requested theorem ID:

```text
N3-ANA-004: ACCEPTED
N3-ANA-005: ACCEPTED
N3-ANA-006: ACCEPTED
N3-ANA-007: ACCEPTED
N3-ANA-008: ACCEPTED
N3-ANA-009: ACCEPTED_WITH_EXTERNAL_BERRY_ESSEEN_DEPENDENCY
N3-ANA-010: ACCEPTED
N3-ANA-011: ACCEPTED_WITH_FORMAL_PROFILE_ONLY_SCOPE
```

The completed package includes exact finite audits, source reconstruction, theorem reconstruction, bounded recurrence evidence, the complete request G sweep, request H semantic adversaries, and fail-closed certificates for the final limit theorems.

Final high-prime hashes:

```text
audit: a9c089489b38990c6de044611a21d8a488166dd0ad570456fee54a0020dc9dd2
N3-ANA-008 claim: 5723c037725e1bc262bd109b65510d74833a28d8869f27903cd86c33473bf930
N3-ANA-009 claim: b3775b62ef887fbaa92e39e1ab729d6f093f360d778edfdc4a52a2a1e3397d7d
```

## N4-REQ-INT-002

Owner: Integration

Status: `ACTIVE_MERGE_READINESS_GATE`

Before merging this branch into `main`:

1. inspect the exact branch divergence and merge base;
2. confirm GitHub reports the draft PR mergeable;
3. run or obtain a complete branch test replay in an environment containing the full repository;
4. resolve the absence of configured CI checks;
5. review the 12 commits currently present on `main` but absent from this branch;
6. preserve the research-scope language and do not convert finite evidence into asymptotic claims.

The Nova 4 branch itself must not merge or rebase `main` under its standing branch rules. Integration must occur through an authorized integration action after this gate is cleared.

## N4-REQ-N2-002

Owner: Nova 2

Status: `AWAITING_REVISED_MODEL`

The frozen regression request is complete. Any new occupancy candidate must supply a versioned machine-readable label family, correction palette, target interval, and exact source commit for the lattice-first verifier.

## N4-REQ-INT-001

Owner: Integration

Status: `BLOCKED_MISSING_SOURCE_ARTIFACT`

Reconstruct the Track B half-range-to-global implication. The archive index exists, but the named source ZIP and verifier are not present in the repository.

## N4-REQ-CMP-001

Owner: Nova 4

Result class: `unknown due to resource limits`

Extend exact profiles to `n=14` with a more memory-efficient witness strategy, a target-partitioned proof certificate, or a different exact algorithm.

## Completed external requests

### N4-REQ-N1-001

Status: `COMPLETED_FOR_FROZEN_STUDIES_A_AND_B`

Study A audited both capacity predicates for every `3<=n<=1,000,000`. Study B computed the exact reduced-rainbow model for every `20<=n<=80` and found an occupancy failure at the first requested target in all 61 cases.

## Rule

Nova 4 reports mismatches and counterexamples to the owning track. It does not silently revise another track's statement or status.
