# Nova 1 Capacity Audit Data

Frozen input:

```text
branch: nova/factorial-structure
commit: fa11f4b2cb86a2dd791df189ada12757be791804
handoff: N1-HO-N4-001, Study A
```

Generate the complete finite audit and transition CSV:

```bash
PYTHONPATH=src python3 src/replay.py audit-n1-capacity \
  --n-min 3 --n-max 1000000 \
  --output-json data/capacity/n1_capacity_audit_n3_n1000000.json \
  --output-csv data/capacity/n1_capacity_transitions_n3_n1000000.csv
```

Independently recompute every integer in the range:

```bash
PYTHONPATH=src python3 src/replay.py verify-n1-capacity \
  data/capacity/n1_capacity_audit_n3_n1000000.json
```

The JSON checksum covers the canonical semantic payload. Separate file SHA-256 values are recorded in `DATASETS.md`.
