# Nova 3 Scale Evidence

Frozen source: `nova/analytic-density@0ce88b28dc2e6641093526f5777bb31f658e3515`, handoff `N3-HO-N4-001`, request C.

Committed artifacts:

```text
n3_scale_evidence_index.json
n3_scale_evidence_index.schema.json
n3_scale_rows.csv
n3_theorem_path_rows.csv
n3_high_prime_tail_n50_n200.csv
n3_high_prime_tail_n500_n1000.csv
n3_high_prime_tail_n2000_n5000.csv
n3_high_prime_tail_n10000_n10000.csv
```

The larger generated JSON audit is deterministic but is not committed as a monolith. Its semantic SHA-256 and file SHA-256 are frozen in the index.

Generate and replay it with:

```bash
PYTHONPATH=src python3 src/replay_n3_scale.py generate \
  --output-json /tmp/n3_scale_evidence.json \
  --scale-csv /tmp/n3_scale_rows.csv \
  --tail-csv /tmp/n3_high_prime_tail_rows.csv

PYTHONPATH=src python3 src/replay_n3_scale.py verify \
  /tmp/n3_scale_evidence.json
```

All rows are `computational evidence`. They do not prove convergence, a convergence rate, or an asymptotic theorem.
