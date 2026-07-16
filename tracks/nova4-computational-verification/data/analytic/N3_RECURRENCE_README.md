# Nova 3 bounded characteristic recurrence evidence

Frozen sources:

```text
handoff: N3-HO-N4-002
handoff commit: 7469dada02fa4caca08ed391ef8b0cb0f1e855b2
proof commit: ff57005b975c4917341306bd0eceb6d05a9b18f6
object: N3-ANA-007
```

The deterministic scan evaluates every integer `q` from `1,000` through `2,000,000` at

```text
t_q = 2*pi*q/log(2).
```

This makes the prime-2 coordinate an exact recurrence. Every grid point is ranked with binary64 arithmetic. The best eight candidates for every `n` and frequency block are then reevaluated at 80-digit Decimal precision. Finalists are independently cross-checked by direct averaging over all exact divisor exponent vectors.

Replay:

```bash
cd tracks/nova4-computational-verification
PYTHONPATH=src python3 src/replay_n3_recurrence.py audit \
  --output /tmp/n3_characteristic_recurrence_evidence.json \
  --block-csv /tmp/n3_characteristic_recurrence_blocks.csv \
  --best-csv /tmp/n3_characteristic_recurrence_best.csv \
  --candidate /tmp/n3_recurrence_candidate_n12.json

PYTHONPATH=src python3 src/replay_n3_recurrence.py verify \
  /tmp/n3_characteristic_recurrence_evidence.json

PYTHONPATH=src python3 src/replay_n3_recurrence.py verify-candidate \
  certificates/analytic/n3_recurrence_candidate_n12.json
```

The bounded scan is computational evidence only. It does not prove an unbounded limsup statement or certify a maximum outside the declared grid.
