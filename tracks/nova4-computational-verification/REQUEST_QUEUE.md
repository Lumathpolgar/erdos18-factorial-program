# Nova 4 Verification Request Queue

Date: 2026-07-16

Nova 4 never changes another track's theorem status. Every request freezes the sending branch and exact commit SHA before testing.

## N4-REQ-N3-001

Priority: `1`

Sending track: Nova 3

Superseding handoff: `N3-HO-N4-002`

Frozen branch: `nova/analytic-density`

Handoff commit: `7469dada02fa4caca08ed391ef8b0cb0f1e855b2`

Source-ledger commit for request E: `697e7ed8bdb03f54b2389b2fcdd8b685dadcebc4`

Artifact: `tracks/nova3-analytic-density/handoffs/TO_NOVA4.md`

Status: `REQUESTS_A_B_C_D_E_COMPLETE_REQUEST_F_READY`

Completed work:

- accepted theorem audits for `N3-ANA-004`, `N3-ANA-005`, and `N3-ANA-007`;
- 1,978 exact divisors and 45,840 local windows;
- request C scale and high-prime computational evidence;
- request D exhaustive bounded recurrence evidence over 19,990,010 scores;
- request E primary-source reconstruction for `N3-SRC-004`, `N3-SRC-005`, and `N3-SRC-006`;
- exact Ford witness `H(120,6,7)=17` while `tau(120;6,7)=0`;
- exact friable membership without a nonexceptionality certificate for `10!`;
- exact ultrafriable common-cap contradiction at `n=10` using `2^8=256` and prime `11`;
- valid compatibility certificate and rehashed direct-use corruption rejection.

Request E disposition:

```text
request E: ACCEPTED
restricted sources reconstructed: 3
direct factorial sources: 0
semantic SHA-256: a5be7514baa9c327e27fa27fccb7d9de0f687d42515b3e8b1de2c949387b662f
claim SHA-256: ae60e9e8758df8113ac249404d8660c5ae4bb5edf02b3aab342c43c47a8124ba
```

Next requested study:

- request F primary-source reconstruction of Dusart Theorem 6.9;
- independently verify the lower bound at `x>=5393` and upper bound at `x>=60184`;
- derive the prime-interval inequality for integer `n>=120368` without using Nova 3's intermediate algebra;
- return a separate decision for `N3-ANA-010`.

Later studies:

- request G exact threshold sweep for every `120368 <= n <= 1000000`;
- request H adversarial threshold tests;
- final independent decisions for `N3-ANA-006`, `N3-ANA-008`, `N3-ANA-009`, `N3-ANA-010`, and `N3-ANA-011`.

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