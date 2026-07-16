# Nova 4 Verification Request Queue

Date: 2026-07-15

Nova 4 never changes another track's theorem status. Every request freezes the sending branch and exact commit SHA before testing.

## N4-REQ-N3-001

Priority: `1`

Sending track: Nova 3

Handoff: `N3-HO-N4-001`

Frozen branch: `nova/analytic-density`

Frozen commit: `0ce88b28dc2e6641093526f5777bb31f658e3515`

Artifact: `tracks/nova3-analytic-density/handoffs/TO_NOVA4.md`

Status: `REQUESTS_A_B_C_COMPLETE_REQUEST_D_READY`

Completed work:

- independent reconstruction and acceptance of `N3-ANA-004`;
- independent reconstruction and acceptance of `N3-ANA-005`;
- exact enumeration of 1,978 divisors across `2 <= n <= 12`;
- exact rational coordinate moments and covariance checks;
- 45,840 exact local-window checks;
- valid tight certificate and rehashed corrupted-bound rejection;
- eight request C scale rows;
- 63 exact cutoff-grid high-prime rows;
- eight admissible `y_n=floor(sqrt(n))/2` path rows;
- variance shares for primes `2`, `3`, `5`, and `7`;
- participation-ratio effective dimension;
- one-million-prime truncated variance proxy;
- frozen-script float cross-check and factor-of-two tail-label diagnosis.

Request C disposition:

```text
scale table: ACCEPTED_AS_COMPUTATIONAL_EVIDENCE
N3-ANA-006: EVIDENCE_CONSISTENT, THEOREM NOT YET ACCEPTED
N3-ANA-008: EVIDENCE_CONSISTENT, THEOREM NOT YET ACCEPTED
scale_sanity.py tail label: NEEDS_REPAIR_FOR_TAIL_RATIO_LABEL
```

Next requested study:

- bounded characteristic-function recurrence search for small `n`;
- explicit frequency range, resolution, and numerical precision;
- near-one values of `|phi_n(t)|` with reproducible witnesses;
- all results labeled computational evidence.

Later studies:

- source-compatibility reconstruction;
- final independent proof decisions for `N3-ANA-006` through `N3-ANA-009`.

## N4-REQ-N1-001

Priority: `COMPLETED`

Sending track: Nova 1

Handoff: `N1-HO-N4-001`

Frozen branch: `nova/factorial-structure`

Frozen commit: `fa11f4b2cb86a2dd791df189ada12757be791804`

Status: `COMPLETED_FOR_FROZEN_STUDIES_A_AND_B`

Completed work:

- certified Study A capacity predicates for every `3 <= n <= 1,000,000`;
- exact Study B high-prime core menus and layers for every `20 <= n <= 80`;
- exact factorial divisibility, address, numerical-collision, residue, and witness checks;
- target-truncated zero-or-one-per-layer support and gap audits;
- first-failure certificate at `n=20`, target `8`, window `[1,8]`;
- exact failure at the first requested target in all 61 reduced models;
- CSV summary, deterministic full-audit checksum, replay commands, and corrupted-certificate tests.

Acceptance scope: Study A is an exact finite theorem audit. Study B is computational evidence plus a disproved finite claim for the exact reduced models only.

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
