# Nova 3 Analytic Data

Nova 3 requests A through C were frozen against `nova/analytic-density@0ce88b28dc2e6641093526f5777bb31f658e3515`, handoff `N3-HO-N4-001`.

Request D was re-frozen against superseding handoff `N3-HO-N4-002` at commit `7469dada02fa4caca08ed391ef8b0cb0f1e855b2`, with the product-model proof pinned separately to `ff57005b975c4917341306bd0eceb6d05a9b18f6`.

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

## Bounded characteristic recurrence evidence

Request D covers every `3 <= n <= 12` and every integer `1,000 <= q <= 2,000,000` under

```text
t_q = 2*pi*q/log(2).
```

The committed index and CSV tables record 40 frequency-block winners and ten global winners. The retained finalists are reevaluated with 80-digit Decimal arithmetic and independently cross-checked through direct exact divisor exponent-vector averaging.

```bash
PYTHONPATH=src python3 src/replay_n3_recurrence.py audit \
  --output /tmp/n3_characteristic_recurrence_evidence.json \
  --block-csv /tmp/n3_characteristic_recurrence_blocks.csv \
  --best-csv /tmp/n3_characteristic_recurrence_best.csv \
  --candidate /tmp/n3_recurrence_candidate_n12.json
PYTHONPATH=src python3 src/replay_n3_recurrence.py verify \
  /tmp/n3_characteristic_recurrence_evidence.json
```

All finite tables are computational evidence only. They do not prove an asymptotic theorem, a recurrence rate, or a maximum outside the declared search domain.
