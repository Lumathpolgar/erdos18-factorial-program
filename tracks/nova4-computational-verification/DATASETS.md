# Nova 4 Dataset Registry

## N4-DATA-001: Exact factorial half-range profiles

Result class: `exact finite theorem audit`.

Coverage: every `1 <= n <= 13` and `0 <= x <= floor(sqrt(n!))`, totaling 109,947 targets. Minimum-cardinality dynamic programming and independent exact-cardinality bitsets agree.

Artifact: `data/factorial_half_range_summary_n1_n13.json`.

Generated profile SHA-256: `cfa5a728089e547ef357e3a6bf51574afa03c40b36ed9774e144e84f0a89e996`.

## N4-DATA-002: Representation certificates

Result class: `finite certificate`.

One hardest-target certificate for every `1 <= n <= 13`, plus the optimal certificate for the first descending-greedy failure at `n=8`, target `155`.

## N4-DATA-003: Nova 2 lattice-obstruction transition audit

Frozen source: `nova/additive-occupancy@45c74a5fa747551422ffcad7d3ddf22788fbe622`.

Coverage: every `3 <= n <= 10,000`. First admissible obstruction at `n=1892`; temporary side-condition failures at `1893,1894,1895`.

Artifact SHA-256: `94b8c1f074904e2aabe7d8b8ddf09279e591936050c07a5882e87977cfbd78b6`.

## N4-DATA-004: Nova 1 capacity-threshold audit

Frozen source: `nova/factorial-structure@fa11f4b2cb86a2dd791df189ada12757be791804`.

Coverage: every `3 <= n <= 1,000,000`.

Semantic SHA-256: `3c88c2e578af86f8a760ead6f9f12bc77af5349106f9e0406aae06cfb981a7d4`.

## N4-DATA-005: Nova 1 reduced-rainbow Study B

Result classes: `computational evidence` and `disproved finite claim`.

Coverage: every `20 <= n <= 80`. Every reduced model fails at its first requested target.

Semantic SHA-256: `cfc5dcbcadf9e6572a94a478eafd7632551b8e657bf41b3a69129ede088ce0f7`.

## N4-DATA-006: Nova 3 moment and local-ceiling audit

Frozen source: `nova/analytic-density@0ce88b28dc2e6641093526f5777bb31f658e3515`, handoff `N3-HO-N4-001`.

Coverage: `2 <= n <= 12`, 1,978 exact divisors, and 45,840 exact local windows.

Semantic SHA-256: `85fdfcd360faa9009531c10bf46a85bf0312e6e46252d06544e72787183f4e03`.

## N4-DATA-007: Nova 3 scale and high-prime tail evidence

Coverage: eight scale rows, 63 cutoff-grid rows, and eight admissible theorem-path rows.

Semantic SHA-256: `28bd8b9a6aeb3c2f4771c1bb861c0fc0f04f9e521982f56763ebac72e220cd94`.

The frozen script’s high-prime diagnostic is exactly `2M/B`, not the theorem-defined `M/B`.

## N4-DATA-008: Nova 3 bounded characteristic recurrence evidence

Frozen source: superseding handoff `N3-HO-N4-002`, handoff commit `7469dada02fa4caca08ed391ef8b0cb0f1e855b2`, proof commit `ff57005b975c4917341306bd0eceb6d05a9b18f6`.

Coverage: every `3 <= n <= 12` and every integer `1,000 <= q <= 2,000,000`, totaling 19,990,010 scores.

Evidence SHA-256: `b15ad70a01046ec292ab3197faafc357bf4c9be155e97a5d498b10a6681123fc`.

Candidate SHA-256: `ab8e8a6d0aa24440ceb1379b86d9ae70dd02b2a5b263f4db4ea89eb354f49a24`.

## N4-DATA-009: Nova 3 restricted-source compatibility audit

Result class: `source compatibility audit`.

Frozen source:

```text
handoff: N3-HO-N4-002
handoff commit: 7469dada02fa4caca08ed391ef8b0cb0f1e855b2
source-ledger commit: 697e7ed8bdb03f54b2389b2fcdd8b685dadcebc4
request: E
```

Primary sources reconstructed:

```text
N3-SRC-004: Kevin Ford, arXiv:math/0401223v5
N3-SRC-005: Drappeau–Tenenbaum, arXiv:1604.04204v1
N3-SRC-006: Dartyge–Feutrie–Tenenbaum, arXiv:2001.04435v1
```

Exact compatibility witnesses:

```text
H(120,6,7) = 17 while tau(120;6,7) = 0
10! belongs to S(10!,10), but the source gives no nonexceptionality certificate
v_2(10!) = 8; y<256 excludes 256, while y>=256 includes prime 11
```

Artifacts:

```text
data/analytic/n3_restricted_source_compatibility.json
data/analytic/n3_restricted_source_compatibility.schema.json
certificates/analytic/n3_restricted_source_compatibility.json
certificates/analytic/n3_source_compatibility_claim.schema.json
```

Audit semantic SHA-256: `a5be7514baa9c327e27fa27fccb7d9de0f687d42515b3e8b1de2c949387b662f`.

Claim semantic SHA-256: `ae60e9e8758df8113ac249404d8660c5ae4bb5edf02b3aab342c43c47a8124ba`.

Decision: none of the three sources directly selects the deterministic factorial sequence.

No finite dataset or source-scope audit in this registry is an asymptotic factorial theorem.