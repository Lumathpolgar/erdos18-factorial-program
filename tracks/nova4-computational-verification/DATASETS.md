# Nova 4 Dataset Registry

## N4-DATA-001: Exact factorial half-range profiles

Every `1 <= n <= 13` and `0 <= x <= floor(sqrt(n!))`, totaling 109,947 targets. Two exact methods agree. Semantic SHA-256: `cfa5a728089e547ef357e3a6bf51574afa03c40b36ed9774e144e84f0a89e996`.

## N4-DATA-002: Representation certificates

One hardest-target certificate for every `1 <= n <= 13`, plus the optimal certificate for the first descending-greedy failure at `n=8`, target `155`.

## N4-DATA-003: Nova 2 lattice transition audit

Every `3 <= n <= 10,000`. First admissible obstruction at `n=1892`. SHA-256: `94b8c1f074904e2aabe7d8b8ddf09279e591936050c07a5882e87977cfbd78b6`.

## N4-DATA-004: Nova 1 capacity threshold audit

Every `3 <= n <= 1,000,000`. Semantic SHA-256: `3c88c2e578af86f8a760ead6f9f12bc77af5349106f9e0406aae06cfb981a7d4`.

## N4-DATA-005: Nova 1 reduced-rainbow Study B

Every `20 <= n <= 80`; every reduced model fails at its first requested target. Semantic SHA-256: `cfc5dcbcadf9e6572a94a478eafd7632551b8e657bf41b3a69129ede088ce0f7`.

## N4-DATA-006: Nova 3 moments and local ceilings

`2 <= n <= 12`, 1,978 exact divisors, and 45,840 windows. Semantic SHA-256: `85fdfcd360faa9009531c10bf46a85bf0312e6e46252d06544e72787183f4e03`.

## N4-DATA-007: Nova 3 scale evidence

Eight scale rows, 63 cutoff rows, and eight theorem-path rows. The frozen diagnostic is `2M/B`, not theorem-defined `M/B`. Semantic SHA-256: `28bd8b9a6aeb3c2f4771c1bb861c0fc0f04f9e521982f56763ebac72e220cd94`.

## N4-DATA-008: Bounded characteristic recurrence

Every `3 <= n <= 12` and every `1,000 <= q <= 2,000,000`, totaling 19,990,010 scores. Evidence SHA-256: `b15ad70a01046ec292ab3197faafc357bf4c9be155e97a5d498b10a6681123fc`.

## N4-DATA-009: Restricted-source compatibility

Ford, Drappeau-Tenenbaum, and ultrafriable source scopes reconstructed. Audit SHA-256: `a5be7514baa9c327e27fa27fccb7d9de0f687d42515b3e8b1de2c949387b662f`.

## N4-DATA-010: Dusart prime-interval theorem

`pi(n)-pi(n/2) >= n/(3 log n)` for every integer `n>=120368`. Audit SHA-256: `42e3675f35d0623f09b30b36ae6847bedadf448cdfe3984ef20fcef09904f212`.

## N4-DATA-011: Exact threshold sweep

Every integer `120368 <= n <= 1000000`, totaling 879,633 integers. Audit SHA-256: `e26653648c2cc9ebc30b03f01904dbb5bcca65737ead57abc9cdbc0b2f218bb0`.

## N4-DATA-012: N3-ANA-011 semantic adversaries

Canonical theorem contract, six rehashed corruptions, and exact endpoint witness `n=120417`. Audit SHA-256: `785517e04e7421348cad72e6e8d20718294dc9edaa32852f3e794ea2637503a9`.

## N4-DATA-013: Full-model variance and non-Gaussian limit

Ten finite diagnostics through `n=1,000,000`, limiting-series cutoff `1,000,000`, and five rehashed theorem corruptions. Audit SHA-256: `e1914a367749c8a397e77212c0d48c53335811e52418ffe0d8d1738046886119`.

## N4-DATA-014: High-prime CLT and coarse-window theorem

Result classes: `proved theorem audit`, `conditional theorem audit`, and `computational evidence`.

Frozen source:

```text
handoff: N3-HO-N4-002
handoff commit: 7469dada02fa4caca08ed391ef8b0cb0f1e855b2
proof blob: 6260f8db0b377cf7dbc1850cbe25c91243099e10
source-ledger blob: da81e6aaf2674fdae036d72df002547d4a71b18a
```

Accepted results:

```text
N3-ANA-008: ACCEPTED
B_ny^2 >> n^2 log(y)/y
M_ny = max_{p>y} b_p log(p)/2
M_ny/B_ny -> 0
T_ny/B_ny => N(0,1)

N3-ANA-009: ACCEPTED_WITH_EXTERNAL_BERRY_ESSEEN_DEPENDENCY
Delta >= (4 C_BE/phi(2)) M_ny
P{T_ny in [x,x+Delta]} >= (phi(2)/2) Delta/B_ny
```

Finite diagnostics use `y=floor(sqrt(n))/2` for `n=10,000`, `100,000`, `1,000,000`, and `10,000,000`. The theorem ratio `M/B` falls from `0.42704100199186046` to `0.11145145759650005`. Eight committed rehashed corruptions are rejected.

```text
audit SHA-256: a9c089489b38990c6de044611a21d8a488166dd0ad570456fee54a0020dc9dd2
N3-ANA-008 claim SHA-256: 5723c037725e1bc262bd109b65510d74833a28d8869f27903cd86c33473bf930
N3-ANA-009 claim SHA-256: b3775b62ef887fbaa92e39e1ab729d6f093f360d778edfdc4a52a2a1e3397d7d
```

No finite dataset or theorem audit in this registry proves profile injectivity, distinct numerical sums, additive occupancy, or the factorial half-range theorem.
