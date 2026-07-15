# Capacity Certificates

`n1_capacity_audit_n3_n1000000.json` is a deterministic finite audit certificate for Study A of `N1-HO-N4-001`.

The verifier does not trust its transition rows, thresholds, margins, source metadata, or checksum. It reconstructs the prime counts, logarithmic ceiling tables, factorial 2-adic valuations, both predicates, all later failures, and both minimum-margin claims.

Replay:

```bash
PYTHONPATH=src python3 src/replay.py verify-n1-capacity \
  certificates/capacity/n1_capacity_audit_n3_n1000000.json
```
