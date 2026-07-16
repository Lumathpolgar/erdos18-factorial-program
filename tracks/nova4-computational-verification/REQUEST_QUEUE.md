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

Status: `REQUESTS_A_THROUGH_H_AND_N3_ANA_006_COMPLETE_N3_ANA_008_READY`

Completed work:

- accepted theorem audits for `N3-ANA-004`, `N3-ANA-005`, `N3-ANA-006`, `N3-ANA-007`, `N3-ANA-010`, and `N3-ANA-011`;
- 1,978 exact divisors and 45,840 local windows;
- request C scale and high-prime computational evidence;
- request D exhaustive bounded recurrence evidence over 19,990,010 scores;
- request E primary-source scope reconstruction for three restricted sources;
- request F primary-source reconstruction of Dusart Theorem 6.9 and independent derivation of the `n/(3 log n)` prime-interval bound;
- request G exact sweep of every one of the 879,633 integers in `120368 <= n <= 1000000`;
- request H exact semantic contract and rejection of all six mandated rehashed corruptions;
- final theorem certificate for `N3-ANA-011`;
- independent fixed-prime, tail-variance, weak-limit, product-convergence, and non-Gaussian reconstruction for `N3-ANA-006`;
- five rehashed `N3-ANA-006` theorem corruptions rejected.

`N3-ANA-006` disposition:

```text
N3-ANA-006: ACCEPTED
Var(S_n)/n^2 -> (1/12) sum_p (log p)^2/(p-1)^2
X_n => sum_p (log p) U_p
characteristic-function zero: 2*pi/log(2)
full-model limit: non-Gaussian
audit SHA-256: e1914a367749c8a397e77212c0d48c53335811e52418ffe0d8d1738046886119
claim SHA-256: efe6091759b788c9383b76799a6a62283a06d3d4f844f5a9e9199ed09d49dcf4
```

Next requested study:

- independently reconstruct `N3-ANA-008`, the high-prime-tail central limit theorem;
- verify the lower bound `B_{n,y}^2 >> n^2 log(y)/y` under `y->infinity` and `2y<=sqrt(n)`;
- verify `M_{n,y} << n log(y)/y` and `M_{n,y}/B_{n,y}->0`;
- verify the triangular-array Lindeberg argument and distinguish the theorem-defined half-span from the frozen script's full-span diagnostic;
- return `ACCEPTED`, `NEEDS_REPAIR`, or `REJECTED`.

Later study:

- final independent decision for `N3-ANA-009`, the coarse central-window lower bound based on Berry-Esseen.

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
