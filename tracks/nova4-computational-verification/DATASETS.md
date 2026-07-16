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

Frozen source: handoff `N3-HO-N4-002` at `7469dada02fa4caca08ed391ef8b0cb0f1e855b2`, source ledger `697e7ed8bdb03f54b2389b2fcdd8b685dadcebc4`.

Decision: Ford, Drappeau–Tenenbaum, and ultrafriable results do not directly select the deterministic factorial sequence.

Audit SHA-256: `a5be7514baa9c327e27fa27fccb7d9de0f687d42515b3e8b1de2c949387b662f`.

Claim SHA-256: `ae60e9e8758df8113ac249404d8660c5ae4bb5edf02b3aab342c43c47a8124ba`.

## N4-DATA-010: Dusart primary-source prime-interval audit

Result class: `primary-source theorem audit`.

Primary source: Pierre Dusart, arXiv:1002.0442v1, Theorem 6.9, equation (6.6), PDF page 9.

Accepted result:

```text
pi(n)-pi(n/2) >= n/(3 log n) for every integer n>=120368
```

Exact endpoint witness: `pi(120368)-pi(60184)=5254`.

Audit SHA-256: `42e3675f35d0623f09b30b36ae6847bedadf448cdfe3984ef20fcef09904f212`.

Claim SHA-256: `7d33e3f669768c555267753c5439d50e2502de2202a9298a0c209c6c9c129703`.

## N4-DATA-011: Nova 3 exact threshold sweep

Result class: `finite certificate`.

Coverage: every integer `120368 <= n <= 1000000`, totaling 879,633 integers, with exact prime-prefix counts, dual exact `v_2(n!)` formulas, certified logarithmic ceilings, address legality, and conservative formal capacity.

Minimum findings:

```text
prime margin: n=120370
Legendre proof margin: n=131071
address slack: 57942 at n=120368,120369,120370,120371
capacity margin: n=120370
```

Audit semantic SHA-256: `e26653648c2cc9ebc30b03f01904dbb5bcca65737ead57abc9cdbc0b2f218bb0`.

Claim semantic SHA-256: `e41f7e639c605ed4e70e4ac2cc6afe20d83ef8bf4f22e991fe0986449b9c1e88`.

Decision: request G is accepted as a finite certificate.

## N4-DATA-012: Nova 3 request H semantic adversarial audit

Result class: `semantic adversarial theorem audit`.

Coverage: canonical `N3-ANA-011` theorem contract, six rehashed semantic corruption fixtures, independent uniform address proof reconstruction, exact Nova 1 menu-definition compatibility, and formal profile-capacity proof reconstruction.

Exact endpoint witness: `n=120417`, `floor(n/2)=60208`, `ceil(n/2)=60209`, and `60209` is prime.

Contract SHA-256: `63b5e3ae60a38f892768c791765a6f4dd99073586dbeada06e66f7c02b5caf8b`.

Audit SHA-256: `785517e04e7421348cad72e6e8d20718294dc9edaa32852f3e794ea2637503a9`.

Claim SHA-256: `a254a6dc271b174a8e5f809c67c22c75de5e6163f36e69a018cb0770f9b9b23c`.

Decision: request H and `N3-ANA-011` are accepted. The theorem is restricted to address legality, menu cardinality, and formal profile capacity.

## N4-DATA-013: Nova 3 full-model variance and non-Gaussian limit audit

Result class: `proved theorem audit with finite diagnostics`.

Frozen source:

```text
handoff: N3-HO-N4-002
handoff commit: 7469dada02fa4caca08ed391ef8b0cb0f1e855b2
proof file blob: 6260f8db0b377cf7dbc1850cbe25c91243099e10
source ledger blob: da81e6aaf2674fdae036d72df002547d4a71b18a
object: N3-ANA-006
```

Accepted results:

```text
Var(S_n)/n^2 -> (1/12) sum_p (log p)^2/(p-1)^2
X_n => sum_p (log p) U_p
the limiting series converges in L^2
the limiting characteristic function vanishes at 2*pi/log(2)
the full-model limit is non-Gaussian
```

Finite diagnostics contain ten exact-valuation rows from `n=50` through `n=1,000,000`. At prime cutoff `1,000,000`, the limiting-series partial sum is `0.1154658352305299` and the elementary remaining-tail bound is `0.00007349978436438362`.

Artifacts:

```text
data/analytic/n3_variance_limit_audit.json
data/analytic/n3_variance_limit_audit.schema.json
data/analytic/n3_variance_convergence.csv
certificates/analytic/n3_ana_006_final_claim.json
certificates/analytic/n3_ana_006_final_claim.schema.json
tests/n3_variance_fixtures/*.json
```

Audit SHA-256: `e1914a367749c8a397e77212c0d48c53335811e52418ffe0d8d1738046886119`.

Claim SHA-256: `efe6091759b788c9383b76799a6a62283a06d3d4f844f5a9e9199ed09d49dcf4`.

Decision: `N3-ANA-006` is accepted. The finite table remains computational evidence only and does not decide the separately truncated high-prime-tail theorem.

No finite dataset or semantic audit in this registry proves additive occupancy or the factorial half-range theorem.
