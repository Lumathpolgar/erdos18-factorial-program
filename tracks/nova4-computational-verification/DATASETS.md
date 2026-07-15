# Nova 4 Dataset Registry

## N4-DATA-001: Exact factorial half-range profiles

Result class: `exact finite theorem audit`

Parameters:

```text
1 <= n <= 13
0 <= x <= floor(sqrt(n!))
```

Coverage: 109,947 targets.

Arithmetic: exact integers.

Methods:

1. minimum-cardinality 0/1 dynamic programming;
2. independent exact-cardinality bitset reachability.

Committed compact data:

```text
data/factorial_half_range_summary_n1_n13.json
```

Schema:

```text
data/half_range_summary.schema.json
```

Full generated profile name:

```text
data/factorial_half_range_profiles_n1_n13.json
```

Full profile SHA-256:

```text
cfa5a728089e547ef357e3a6bf51574afa03c40b36ed9774e144e84f0a89e996
```

Generation command:

```bash
PYTHONPATH=src python3 src/replay.py generate-dataset \
  --n-min 1 --n-max 13 \
  --output data/factorial_half_range_profiles_n1_n13.json \
  --certificate-dir certificates
```

Verification command:

```bash
PYTHONPATH=src python3 src/replay.py verify-dataset \
  data/factorial_half_range_profiles_n1_n13.json
```

Known limitation: Method A for `n=14` did not complete in a 30 second bounded attempt. That case is `unknown due to resource limits`.

## N4-DATA-002: Representation certificates

Result class: `finite certificate`

Contents:

- one certificate for a hardest target for each `1 <= n <= 13`;
- one optimal certificate for the smallest descending-greedy counterexample.

Schema:

```text
certificates/representation_certificate.schema.json
```

Verification command:

```bash
PYTHONPATH=src python3 src/replay.py verify-tree certificates
```

## N4-DATA-003: Nova 2 lattice-obstruction transition audit

Result class: `exact finite theorem audit`

Frozen source:

```text
branch: nova/additive-occupancy
commit: 45c74a5fa747551422ffcad7d3ddf22788fbe622
objects: N2-ADD-115 and N2-OBS-107
```

Parameter range:

```text
3 <= n <= 10000
```

Committed data:

```text
data/lattice/n2_obs_107_range_n3_n10000.json
```

Schema:

```text
data/lattice/n2_obs_107_range_audit.schema.json
```

SHA-256:

```text
94b8c1f074904e2aabe7d8b8ddf09279e591936050c07a5882e87977cfbd78b6
```

Exact findings:

- first target-range success: `n=9`;
- first valuation-budget success: `n=1892`;
- first simultaneous admissible obstruction: `n=1892`;
- temporary later side-condition failures: `n=1893,1894,1895`;
- simultaneous success at every checked `1896 <= n <= 10000`.

Generation command:

```bash
PYTHONPATH=src python3 src/replay.py audit-n2-obs-107 \
  --n-min 3 --n-max 10000 \
  --output data/lattice/n2_obs_107_range_n3_n10000.json
```

## N4-DATA-004: Nova 1 capacity-threshold audit

Result class: `exact finite theorem audit`

Frozen source:

```text
branch: nova/factorial-structure
commit: fa11f4b2cb86a2dd791df189ada12757be791804
handoff: N1-HO-N4-001, Study A
Nova 4 certificate checkpoint: 53b579cd5a7eeac780869cffa2cb8b9b8bdd5289
```

Parameter range: every `3 <= n <= 1,000,000`.

Artifacts:

```text
data/capacity/n1_capacity_audit_n3_n1000000.json
data/capacity/n1_capacity_transitions_n3_n1000000.csv
certificates/capacity/n1_capacity_audit_n3_n1000000.json
```

Semantic checksum:

```text
3c88c2e578af86f8a760ead6f9f12bc77af5349106f9e0406aae06cfb981a7d4
```

File SHA-256:

```text
JSON: 508feff0c91a03f8097b3dbeca8982d143417ee38d31449bc26c8a3c45d992d6
CSV:  289c5cafbedd3c6501518289f0e5d150c831014ab5ede7c17f1c823446f16ba4
```

Exact findings:

- first `A_n` success: `1892`;
- first simultaneous success: `1892`;
- later `A_n` failures: `1893,1894,1895`;
- simultaneous success for every checked `1896<=n<=1,000,000`;
- only `C_n` failure after its initial success: `n=10`.

Replay:

```bash
PYTHONPATH=src python3 src/replay.py verify-n1-capacity \
  data/capacity/n1_capacity_audit_n3_n1000000.json
```

## N4-DATA-005: Nova 1 reduced-rainbow Study B

Result class: `computational evidence`

Frozen source:

```text
branch: nova/factorial-structure
commit: fa11f4b2cb86a2dd791df189ada12757be791804
handoff: N1-HO-N4-001, Study B
```

Parameter range: every `20 <= n <= 80`.

Committed artifacts:

```text
data/rainbow/n1_reduced_rainbow_summary_n20_n80.csv
data/rainbow/n1_reduced_rainbow_index.json
data/rainbow/n1_reduced_rainbow.schema.json
certificates/rainbow/n1_reduced_rainbow_first_failure_n20.json
```

The deterministic full generated audit includes exact residue sets for every modulus `2<=q<=64` and replayable witnesses for every new maximum downward gap. Its semantic SHA-256 is:

```text
cfc5dcbcadf9e6572a94a478eafd7632551b8e657bf41b3a69129ede088ce0f7
```

First-failure certificate semantic SHA-256:

```text
0c5dcdf30a72a28de6900c4e2d574dbcd5a5e210de07c305118af2730da04e8c
```

Exact finite findings:

- all 61 reduced models fail at their first requested target `2^(r_n^*)`;
- every nonzero layer term has gcd `2^(r_n^*+1)`;
- the first failure is `n=20`, target `8`, empty window `[1,8]`;
- exact reachable-set sizes range from `159` to `311,688`;
- additional residue deficiencies beyond the gcd subgroup occur only at `n=22` for moduli `45`, `55`, and `57`.

Generation and replay:

```bash
PYTHONPATH=src python3 src/replay_rainbow.py audit \
  --n-min 20 --n-max 80 \
  --output-json /tmp/n1_reduced_rainbow_full.json \
  --output-csv data/rainbow/n1_reduced_rainbow_summary_n20_n80.csv \
  --output-failure certificates/rainbow/n1_reduced_rainbow_first_failure_n20.json

PYTHONPATH=src python3 src/replay_rainbow.py verify \
  /tmp/n1_reduced_rainbow_full.json
```

The profile-compression fields are truncated-support diagnostics, not pure collision probabilities and not asymptotic claims.
