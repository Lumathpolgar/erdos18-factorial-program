# Nova 4 Open Requirements

## N4-REQ-N3-001

Owner: Nova 3

Superseding handoff: `N3-HO-N4-002`

Handoff commit: `7469dada02fa4caca08ed391ef8b0cb0f1e855b2`

Source-ledger commit used for requests E and F: `697e7ed8bdb03f54b2389b2fcdd8b685dadcebc4`

Status: `REQUESTS_A_B_C_D_E_F_COMPLETE_REQUEST_G_READY`

Completed:

- independent proof reconstruction and acceptance of `N3-ANA-004`, `N3-ANA-005`, `N3-ANA-007`, and `N3-ANA-010`;
- exact moment and local-ceiling audits for `2 <= n <= 12`;
- request C scale, low-prime share, effective-dimension, and high-prime tail evidence;
- factor-of-two tail-ratio label diagnosis in the frozen script;
- request D bounded recurrence search over 19,990,010 scores with 80-digit and direct-vector replay;
- request E reconstruction of Ford, Drappeau–Tenenbaum, and ultrafriable source scopes;
- request F reconstruction of Dusart Theorem 6.9, equation (6.6), and the complete algebra for the upper-half prime interval;
- exact endpoint witness `pi(120368)-pi(60184)=5254`;
- rehashed threshold, source-threshold, predecessor-coverage, and source-metadata corruption rejection.

Request F decision:

```text
request F: ACCEPTED
N3-ANA-010: ACCEPTED
source lower threshold: 5393
source upper threshold: 60184
minimal direct-source integer threshold: 120368
audit SHA-256: 42e3675f35d0623f09b30b36ae6847bedadf448cdfe3984ef20fcef09904f212
claim SHA-256: 7d33e3f669768c555267753c5439d50e2502de2202a9298a0c209c6c9c129703
```

Remaining:

- request G exact threshold sweep for `120368 <= n <= 1000000`;
- request H adversarial threshold tests;
- independent final decisions for `N3-ANA-006`, `N3-ANA-008`, `N3-ANA-009`, and `N3-ANA-011`.

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

Owner: Nova 1

Frozen source head: `fa11f4b2cb86a2dd791df189ada12757be791804`

Handoff: `N1-HO-N4-001`

Status: `COMPLETED_FOR_FROZEN_STUDIES_A_AND_B`

Study A audited both capacity predicates for every `3<=n<=1,000,000`. Study B computed the exact reduced-rainbow model for every `20<=n<=80` and found an occupancy failure at the first requested target in all 61 cases.

## Rule

Nova 4 reports mismatches and counterexamples to the owning track. It does not silently revise another track's statement or status.
