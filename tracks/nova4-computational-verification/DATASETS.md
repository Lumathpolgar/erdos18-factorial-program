# Nova 4 Dataset Registry

## N4-DATA-001: Exact factorial half-range profiles

Result class: `exact finite theorem audit`

Coverage:

```text
1 <= n <= 13
0 <= x <= floor(sqrt(n!))
109,947 targets
```

Methods: minimum-cardinality 0/1 dynamic programming and independent exact-cardinality bitset reachability.

Artifacts:

```text
data/factorial_half_range_summary_n1_n13.json
data/half_range_summary.schema.json
```

Full generated profile SHA-256:

```text
cfa5a728089e547ef357e3a6bf51574afa03c40b36ed9774e144e84f0a89e996
```

Known limitation: the `n=14` Method A profile is `unknown due to resource limits` after a bounded 30-second attempt.

## N4-DATA-002: Representation certificates

Result class: `finite certificate`

Contents: one hardest-target certificate for each `1 <= n <= 13` and one optimal certificate for the smallest descending-greedy counterexample.

Schema and replay:

```text
certificates/representation_certificate.schema.json
PYTHONPATH=src python3 src/replay.py verify-tree certificates
```

## N4-DATA-003: Nova 2 lattice-obstruction transition audit

Result class: `exact finite theorem audit`

Frozen source:

```text
nova/additive-occupancy@45c74a5fa747551422ffcad7d3ddf22788fbe622
objects: N2-ADD-115 and N2-OBS-107
```

Coverage: every `3 <= n <= 10,000`.

Artifact and SHA-256:

```text
data/lattice/n2_obs_107_range_n3_n10000.json
94b8c1f074904e2aabe7d8b8ddf09279e591936050c07a5882e87977cfbd78b6
```

Findings: first simultaneous admissible obstruction at `n=1892`; temporary side-condition failures at `1893,1894,1895`; success for every checked `1896<=n<=10000`.

## N4-DATA-004: Nova 1 capacity-threshold audit

Result class: `exact finite theorem audit`

Frozen source: `nova/factorial-structure@fa11f4b2cb86a2dd791df189ada12757be791804`, handoff `N1-HO-N4-001`, Study A.

Coverage: every `3 <= n <= 1,000,000`.

Artifacts:

```text
data/capacity/n1_capacity_audit_n3_n1000000.json
data/capacity/n1_capacity_transitions_n3_n1000000.csv
certificates/capacity/n1_capacity_audit_n3_n1000000.json
```

Semantic SHA-256:

```text
3c88c2e578af86f8a760ead6f9f12bc77af5349106f9e0406aae06cfb981a7d4
```

Findings: first `A_n` and simultaneous success at `1892`; later `A_n` failures `1893,1894,1895`; simultaneous success for every checked `1896<=n<=1,000,000`; only later `C_n` failure at `n=10`.

## N4-DATA-005: Nova 1 reduced-rainbow Study B

Result class: `computational evidence` plus `disproved finite claim`.

Frozen source: `nova/factorial-structure@fa11f4b2cb86a2dd791df189ada12757be791804`, Study B.

Coverage: every `20 <= n <= 80`.

Artifacts:

```text
data/rainbow/n1_reduced_rainbow_summary_n20_n80.csv
data/rainbow/n1_reduced_rainbow_index.json
data/rainbow/n1_reduced_rainbow.schema.json
certificates/rainbow/n1_reduced_rainbow_first_failure_n20.json
```

Full audit semantic SHA-256:

```text
cfc5dcbcadf9e6572a94a478eafd7632551b8e657bf41b3a69129ede088ce0f7
```

Every one of the 61 reduced models fails at its first requested target. The first failure is `n=20`, target `8`, empty window `[1,8]`.

## N4-DATA-006: Nova 3 moment and local-ceiling audit

Result class: `finite certificate` supporting accepted theorem audits.

Frozen source:

```text
nova/analytic-density@0ce88b28dc2e6641093526f5777bb31f658e3515
handoff: N3-HO-N4-001
objects: N3-ANA-004 and N3-ANA-005
```

Coverage:

```text
2 <= n <= 12
1,978 exact divisors enumerated
45,840 exact local windows checked
Delta in {0,1/4,1/2,1,2}
every prime q<=n
every divisor-log endpoint
```

Artifacts:

```text
data/analytic/n3_moment_local_n2_n12.json
data/analytic/n3_moment_local_summary_n2_n12.csv
data/analytic/n3_moment_local_audit.schema.json
certificates/analytic/n3_local_ceiling_tight_n2.json
```

Semantic audit SHA-256:

```text
85fdfcd360faa9009531c10bf46a85bf0312e6e46252d06544e72787183f4e03
```

Exact findings: divisor uniqueness, exact moments, complement symmetry, all cross covariances, and every requested local ceiling pass. There are 21 tight windows, first at `n=2`, `q=2`, `Delta=0`, endpoint divisor `1`; lowering the bound from `1` to `0` and rehashing is rejected.

## N4-DATA-007: Nova 3 scale and high-prime tail evidence

Result class: `computational evidence`.

Frozen source:

```text
nova/analytic-density@0ce88b28dc2e6641093526f5777bb31f658e3515
handoff: N3-HO-N4-001
request: C
objects: N3-ANA-006 and N3-ANA-008
```

Coverage:

```text
scale n values: 50,100,200,500,1000,2000,5000,10000
cutoff grid: 2,3,5,7,10,20,25,50
scale rows: 8
grid tail rows: 63
theorem-path rows: 8
theorem path: y_n=floor(sqrt(n))/2
```

Artifacts:

```text
data/analytic/n3_scale_evidence_index.json
data/analytic/n3_scale_evidence_index.schema.json
data/analytic/n3_scale_rows.csv
data/analytic/n3_theorem_path_rows.csv
data/analytic/n3_high_prime_tail_n50_n200.csv
data/analytic/n3_high_prime_tail_n500_n1000.csv
data/analytic/n3_high_prime_tail_n2000_n5000.csv
data/analytic/n3_high_prime_tail_n10000_n10000.csv
```

Full generated audit semantic SHA-256:

```text
28bd8b9a6aeb3c2f4771c1bb861c0fc0f04f9e521982f56763ebac72e220cd94
```

Findings:

- `Var(S_n)/n^2` at `n=10000` is `0.11544768625558856535`, or `0.9998428195240168` of the one-million-prime truncated proxy;
- primes `2,3,5,7` contribute `0.7567896218242085` of the variance at `n=10000`;
- effective dimension at `n=10000` is approximately `5.23116`;
- along `y_n=floor(sqrt(n))/2`, theorem-defined `M/B` decreases from `0.88653` to `0.42704` over the tested rows;
- the frozen script's scale fields agree within `1.6e-15`;
- its high-prime routine computes `2M/B`, so the printed ratio label is `NEEDS_REPAIR`.

Replay:

```bash
PYTHONPATH=src python3 src/replay_n3_scale.py generate \
  --output-json /tmp/n3_scale_evidence.json \
  --scale-csv /tmp/n3_scale_rows.csv \
  --tail-csv /tmp/n3_high_prime_tail_rows.csv
PYTHONPATH=src python3 src/replay_n3_scale.py verify /tmp/n3_scale_evidence.json
```

No finite dataset in this registry is an asymptotic theorem.
