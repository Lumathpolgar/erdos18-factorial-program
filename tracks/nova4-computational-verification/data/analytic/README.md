# Nova 3 Analytic Data

Frozen source: `nova/analytic-density@0ce88b28dc2e6641093526f5777bb31f658e3515`, handoff `N3-HO-N4-001`.

## Moment and local-ceiling certificate

The committed audit covers every `2 <= n <= 12` and verifies exact divisor-vector moments plus the requested local ceilings at every divisor-log endpoint for widths `0`, `1/4`, `1/2`, `1`, and `2`.

```bash
PYTHONPATH=src python3 src/replay_n3.py verify \
  data/analytic/n3_moment_local_n2_n12.json
```

## Scale and high-prime tail evidence

Request C covers eight scale rows, 63 cutoff-grid tail rows, and eight theorem-path rows. The committed index freezes the source, semantic checksum, exact projections, and per-file hashes.

```bash
PYTHONPATH=src python3 src/replay_n3_scale.py generate \
  --output-json /tmp/n3_scale_evidence.json \
  --scale-csv /tmp/n3_scale_rows.csv \
  --tail-csv /tmp/n3_high_prime_tail_rows.csv
PYTHONPATH=src python3 src/replay_n3_scale.py verify /tmp/n3_scale_evidence.json
```

The scale evidence also records that the frozen script's high-prime diagnostic is twice the theorem-defined `M/B` because the script omits the factor `1/2` in `M`.

All finite tables are computational evidence only. They do not prove an asymptotic theorem.
