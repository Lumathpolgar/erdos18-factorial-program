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

Status: `REQUESTS_A_THROUGH_H_COMPLETE_FINAL_THEOREM_CLOSURE_READY`

Completed work:

- accepted theorem audits for `N3-ANA-004`, `N3-ANA-005`, `N3-ANA-007`, `N3-ANA-010`, and `N3-ANA-011`;
- 1,978 exact divisors and 45,840 local windows;
- request C scale and high-prime computational evidence;
- request D exhaustive bounded recurrence evidence over 19,990,010 scores;
- request E primary-source scope reconstruction for three restricted sources;
- request F primary-source reconstruction of Dusart Theorem 6.9 and independent derivation of the `n/(3 log n)` prime-interval bound;
- request G exact sweep of every one of the 879,633 integers in `120368 <= n <= 1000000`;
- request H exact semantic contract and rejection of all six mandated rehashed corruptions;
- final theorem certificate for `N3-ANA-011`.

Request H disposition:

```text
request H: ACCEPTED
N3-ANA-011: ACCEPTED
corruptions rejected: 6 of 6
endpoint witness: n=120417, floor(n/2)=60208, ceil(n/2)=60209 prime
contract SHA-256: 63b5e3ae60a38f892768c791765a6f4dd99073586dbeada06e66f7c02b5caf8b
audit SHA-256: 785517e04e7421348cad72e6e8d20718294dc9edaa32852f3e794ea2637503a9
claim SHA-256: a254a6dc271b174a8e5f809c67c22c75de5e6163f36e69a018cb0770f9b9b23c
```

Next requested study:

- independently reconstruct `N3-ANA-006`, the variance asymptotic;
- distinguish proof from request C numerical convergence evidence;
- verify convergence, domination, and interchange of the prime sum and limit;
- return `ACCEPTED`, `NEEDS_REPAIR`, or `REJECTED`.

Later studies:

- final independent decision for `N3-ANA-008`, the high-prime tail scale;
- final independent decision for `N3-ANA-009`, the full-model non-Gaussian limit and characteristic-function zero.

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
