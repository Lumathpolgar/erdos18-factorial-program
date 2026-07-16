# Nova 4 Verification Request Queue

Date: 2026-07-16

Nova 4 never changes another track's theorem status. Every request freezes the sending branch and exact commit SHA before testing.

## N4-REQ-N3-001

Priority: `1`

Sending track: Nova 3

Superseding handoff: `N3-HO-N4-002`

Frozen branch: `nova/analytic-density`

Handoff commit: `7469dada02fa4caca08ed391ef8b0cb0f1e855b2`

Source-ledger commit for requests E and F: `697e7ed8bdb03f54b2389b2fcdd8b685dadcebc4`

Artifact: `tracks/nova3-analytic-density/handoffs/TO_NOVA4.md`

Status: `REQUESTS_A_B_C_D_E_F_COMPLETE_REQUEST_G_READY`

Completed work:

- accepted theorem audits for `N3-ANA-004`, `N3-ANA-005`, `N3-ANA-007`, and `N3-ANA-010`;
- 1,978 exact divisors and 45,840 local windows;
- request C scale and high-prime computational evidence;
- request D exhaustive bounded recurrence evidence over 19,990,010 scores;
- request E primary-source scope reconstruction for three restricted sources;
- request F primary-source reconstruction of Dusart Theorem 6.9 and independent derivation of the `n/(3 log n)` prime-interval bound;
- exact threshold prime counts `11330-6076=5254`;
- rational certificate `Q(L)>L^2-(11/5)L-18/5>0` for `L>4`;
- valid theorem certificate and rehashed threshold corruption rejection.

Request F disposition:

```text
request F: ACCEPTED
N3-ANA-010: ACCEPTED
integer threshold: 120368
audit SHA-256: 42e3675f35d0623f09b30b36ae6847bedadf448cdfe3984ef20fcef09904f212
claim SHA-256: 7d33e3f669768c555267753c5439d50e2502de2202a9298a0c209c6c9c129703
```

Next requested study:

- request G exact sweep for every integer `120368 <= n <= 1000000`;
- verify exact `pi(n)-pi(floor(n/2))`, `v_2(n!)`, ceilings in `r_n` and `M_n`, address legality, and conservative capacity exponent;
- record the exact minimum margin and its first `n` for each check.

Later studies:

- request H adversarial threshold tests;
- final independent decisions for `N3-ANA-006`, `N3-ANA-008`, `N3-ANA-009`, and `N3-ANA-011`.

## N4-REQ-N1-001

Priority: `COMPLETED`

Sending track: Nova 1

Handoff: `N1-HO-N4-001`

Frozen branch: `nova/factorial-structure`

Frozen commit: `fa11f4b2cb86a2dd791df189ada12757be791804`

Status: `COMPLETED_FOR_FROZEN_STUDIES_A_AND_B`

Study A certified the capacity predicates for every `3 <= n <= 1,000,000`. Study B found failure at the first requested target in all 61 reduced models for `20 <= n <= 80`.

## N4-REQ-N2-001

Priority: `COMPLETED`

Sending track: Nova 2

Handoff: `N2-HO-N4-001-v2`

Frozen branch: `nova/additive-occupancy`

Frozen commit: `45c74a5fa747551422ffcad7d3ddf22788fbe622`

Status: `ACCEPTED_FOR_FROZEN_MODEL`

The exact lattice obstruction and transition audit are complete. A revised candidate requires a new versioned request and exact source SHA.

## Intake rule

A received handoff is not accepted merely because its file exists. Nova 4 records `ACCEPTED`, `ACCEPTED_WITH_RESTRICTIONS`, `NEEDS_REPAIR`, or `REJECTED` only after independent reconstruction and replay.
