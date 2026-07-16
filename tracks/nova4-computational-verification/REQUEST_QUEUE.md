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

Status: `REQUESTS_A_B_C_D_E_F_G_COMPLETE_REQUEST_H_READY`

Completed work:

- accepted theorem audits for `N3-ANA-004`, `N3-ANA-005`, `N3-ANA-007`, and `N3-ANA-010`;
- 1,978 exact divisors and 45,840 local windows;
- request C scale and high-prime computational evidence;
- request D exhaustive bounded recurrence evidence over 19,990,010 scores;
- request E primary-source scope reconstruction for three restricted sources;
- request F primary-source reconstruction of Dusart Theorem 6.9 and independent derivation of the `n/(3 log n)` prime-interval bound;
- request G exact sweep of every one of the 879,633 integers in `120368 <= n <= 1000000`;
- exact upper-half prime counts, two exact `v_2(n!)` formulas, rationally certified logarithmic ceilings, address legality, and conservative formal-profile capacity;
- valid finite certificate and rehashed minimum-slack corruption rejection.

Request G disposition:

```text
request G: ACCEPTED_AS_FINITE_CERTIFICATE
N3-ANA-011 swept interval: CONFIRMED
final N3-ANA-011 theorem decision: PENDING_REQUEST_H
minimum prime margin: n=120370
minimum Legendre proof margin: n=131071
minimum address slack: 57942 at n=120368..120371
minimum capacity margin: n=120370
audit SHA-256: e26653648c2cc9ebc30b03f01904dbb5bcca65737ead57abc9cdbc0b2f218bb0
claim SHA-256: e41f7e639c605ed4e70e4ac2cc6afe20d83ef8bf4f22e991fe0986449b9c1e88
```

Next requested study:

- request H adversarial threshold and semantics tests;
- reject a threshold below source coverage without supplementation;
- reject a larger unproved legal-address range;
- reject removal of the unit exclusion from the menu bound;
- reject formal-profile count as distinct numerical sums;
- reject `pi(ceil(n/2))` without endpoint analysis;
- reject reporting the finite sweep as an asymptotic proof.

Later studies:

- final decision for `N3-ANA-011` after request H;
- final independent decisions for `N3-ANA-006`, `N3-ANA-008`, and `N3-ANA-009`.

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
