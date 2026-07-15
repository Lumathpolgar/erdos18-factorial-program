# Nova 4 Verification Request Queue

Date: 2026-07-15

Nova 4 never changes another track's theorem status. Every request freezes the sending branch and exact commit SHA before testing.

## N4-REQ-N2-001

Priority: `1`

Sending track: Nova 2

Handoff: `N2-HO-N4-001-v2`

Frozen branch: `nova/additive-occupancy`

Frozen commit: `45c74a5fa747551422ffcad7d3ddf22788fbe622`

Artifact: `tracks/nova2-additive-occupancy/handoffs/TO_NOVA4.md`

Status: `RECEIVED_READY_FOR_AUDIT`

First audit:

- implement the exact common-gcd and residue-lattice gate;
- reproduce the frozen `N2-OBS-107` obstruction before any convolution;
- reject numerical duplicates and illegal factorial divisors;
- return the lexicographically smallest exact failure;
- identify every tested external input by branch and commit SHA.

Reason for priority: the handoff marks this as a mandatory first gate, and a symbolic lattice obstruction takes precedence over expensive enumeration.

## N4-REQ-N1-001

Priority: `2`

Sending track: Nova 1

Handoff: `N1-HO-N4-001`

Frozen branch: `nova/factorial-structure`

Frozen commit: `fa11f4b2cb86a2dd791df189ada12757be791804`

Artifact: `tracks/nova1-factorial-structure/handoffs/TO_NOVA4.md`

Status: `RECEIVED_READY_FOR_AUDIT`

Requested studies:

- exact capacity-threshold audit for `3 <= n <= 1,000,000` with certified comparisons;
- reduced rainbow falsification model for `20 <= n <= 80`;
- exact divisor legality, layer-address, collision, and witness checks;
- CSV transition rows and machine-readable first-failure artifacts.

## N4-REQ-N3-001

Priority: `3`

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

## Intake rule

A received handoff is not accepted merely because its file exists. Nova 4 records `ACCEPTED`, `ACCEPTED_WITH_RESTRICTIONS`, `NEEDS_REPAIR`, or `REJECTED` only after independent reconstruction and replay.
