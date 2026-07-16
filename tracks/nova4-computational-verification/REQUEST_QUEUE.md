# Nova 4 Verification Request Queue

Date: 2026-07-16

Nova 4 never changes another track's theorem status. Every request freezes the sending branch and exact commit SHA before testing.

## N4-REQ-INT-002

Priority: `1`

Owner: Integration

Status: `ACTIVE_MERGE_READINESS_GATE`

Target branch: `nova/computational-verification`

Required disposition:

- verify branch divergence and merge base against `main`;
- confirm draft PR mergeability and unmerged state;
- obtain a complete full-repository test replay;
- address the absence of configured CI checks;
- inspect the 12 `main` commits absent from the branch;
- preserve all finite, conditional, and scope restrictions.

Nova 4 does not merge or rebase `main` into its working branch.

## N4-REQ-N3-001

Priority: `COMPLETED`

Sending track: Nova 3

Superseding handoff: `N3-HO-N4-002`

Frozen branch: `nova/analytic-density`

Handoff commit: `7469dada02fa4caca08ed391ef8b0cb0f1e855b2`

Status: `COMPLETE`

Final decisions:

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

High-prime closure:

```text
B_ny^2 >> n^2 log(y)/y
M_ny = max b_p log(p)/2
M_ny/B_ny -> 0
T_ny/B_ny => N(0,1)
Delta >= (4 C_BE/phi(2)) M_ny implies a coarse central-window lower bound
```

The theorem package does not prove additive occupancy, the factorial half-range theorem, or Erdős Problem 18.

## N4-REQ-N1-001

Priority: `COMPLETED`

Status: `COMPLETED_FOR_FROZEN_STUDIES_A_AND_B`

Study A certified the capacity predicates for every `3 <= n <= 1,000,000`. Study B found failure at the first requested target in all 61 reduced models for `20 <= n <= 80`.

## N4-REQ-N2-001

Priority: `COMPLETED`

Status: `ACCEPTED_FOR_FROZEN_MODEL`

The exact lattice obstruction and transition audit are complete. A revised candidate requires a new versioned request and exact source SHA.

## Intake rule

A received handoff is not accepted merely because its file exists. Nova 4 records `ACCEPTED`, `ACCEPTED_WITH_RESTRICTIONS`, `NEEDS_REPAIR`, or `REJECTED` only after independent reconstruction and replay.
