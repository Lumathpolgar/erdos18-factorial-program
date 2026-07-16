# Nova 3 Analytic Finite Data

Frozen source: `nova/analytic-density@0ce88b28dc2e6641093526f5777bb31f658e3515`, handoff `N3-HO-N4-001`.

The committed audit covers every `2 <= n <= 12` and verifies exact divisor-vector moments plus the requested local ceilings at every divisor-log endpoint for widths `0`, `1/4`, `1/2`, `1`, and `2`.

```bash
cd tracks/nova4-computational-verification
PYTHONPATH=src python3 src/replay_n3.py verify \
  data/analytic/n3_moment_local_n2_n12.json
```

The CSV is a compact per-`n` summary. The JSON is the replayable certificate source of truth. This finite data does not prove any asymptotic theorem.
