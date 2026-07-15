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
