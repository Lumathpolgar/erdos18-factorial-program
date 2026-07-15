# Nova 4 Verification Request Queue

Date: 2026-07-15

Nova 4 never changes another track's theorem status. Every request freezes the sending branch and exact commit SHA before testing.

## N4-REQ-N1-001

Priority: `1`

Sending track: Nova 1

Handoff: `N1-HO-N4-001`

Frozen branch: `nova/factorial-structure`

Frozen commit: `fa11f4b2cb86a2dd791df189ada12757be791804`

Artifact: `tracks/nova1-factorial-structure/handoffs/TO_NOVA4.md`

Status: `STUDY_A_COMPLETE_STUDY_B_READY`

Study A completed at `53b579cd5a7eeac780869cffa2cb8b9b8bdd5289`. Remaining requested studies:

- reduced rainbow falsification model for `20 <= n <= 80`;
- exact divisor legality, layer-address, collision, and witness checks;
- CSV transition rows and machine-readable first-failure artifacts.

## N4-REQ-N3-001

Priority: `2`

Sending track: Nova 3

Handoff: `N3-HO-N4-001`

Frozen branch: `nova/analytic-density`

Frozen commit: `0ce88b28dc2e6641093526f5777bb31f658e3515`

Artifact: `tracks/nova3-analytic-density/handoffs/TO_NOVA4.md`

Status: `RECEIVED_READY_FOR_AUDIT`

Requested studies:

- independent exact moment audit for `2 <= n <= 12`;
- exhaustive local-count ceiling audit with corrupted-bound rejection;
- scale convergence tables labeled computational evidence;
- characteristic-function recurrence search labeled evidence;
- source-compatibility reconstruction for imported analytic results.

## N4-REQ-N2-001

Priority: `COMPLETED`

Sending track: Nova 2

Handoff: `N2-HO-N4-001-v2`

Frozen branch: `nova/additive-occupancy`

Frozen commit: `45c74a5fa747551422ffcad7d3ddf22788fbe622`

Status: `ACCEPTED_FOR_FROZEN_MODEL`

Completed work:

- reusable common-gcd, residue, and exact finite support gate;
- exact factorial-divisor and numerical-collision validation;
- independent replay of `N2-OBS-107`;
- proof reconstruction of `N2-ADD-115`;
- exhaustive transition audit for `3 <= n <= 10000`;
- corrupted-certificate rejection tests.

Acceptance is limited to the exact model frozen by Nova 2. A revised candidate requires a new versioned request and exact source SHA.

## Intake rule

A received handoff is not accepted merely because its file exists. Nova 4 records `ACCEPTED`, `ACCEPTED_WITH_RESTRICTIONS`, `NEEDS_REPAIR`, or `REJECTED` only after independent reconstruction and replay.
