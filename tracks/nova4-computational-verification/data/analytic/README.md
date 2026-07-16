# Nova 3 Analytic Data

Nova 3 requests A through C were frozen against `nova/analytic-density@0ce88b28dc2e6641093526f5777bb31f658e3515`, handoff `N3-HO-N4-001`.

Requests D and E were re-frozen against superseding handoff `N3-HO-N4-002` at commit `7469dada02fa4caca08ed391ef8b0cb0f1e855b2`.

## Moment and local-ceiling certificate

```bash
PYTHONPATH=src python3 src/replay_n3.py verify \
  data/analytic/n3_moment_local_n2_n12.json
```

## Scale and high-prime tail evidence

```bash
PYTHONPATH=src python3 src/replay_n3_scale.py verify \
  /tmp/n3_scale_evidence.json
```

The scale audit records that the frozen script’s high-prime diagnostic is twice the theorem-defined `M/B`.

## Bounded characteristic recurrence evidence

Request D covers every `3 <= n <= 12` and every integer `1,000 <= q <= 2,000,000` under `t_q=2*pi*q/log(2)`.

```bash
PYTHONPATH=src python3 src/replay_n3_recurrence.py verify \
  /tmp/n3_characteristic_recurrence_evidence.json
```

## Restricted-source compatibility audit

Request E reconstructs the primary-source scope of Ford’s divisor-in-an-interval theorem, the Drappeau–Tenenbaum almost-all friable Gaussian law, and ultrafriable arithmetic-progression estimates.

```bash
PYTHONPATH=src python3 src/replay_n3_sources.py verify \
  data/analytic/n3_restricted_source_compatibility.json
PYTHONPATH=src python3 src/replay_n3_sources.py verify-claim \
  certificates/analytic/n3_restricted_source_compatibility.json
```

The exact witnesses show that ambient counts do not imply a pointwise statement for `n!`, an exceptional-set theorem does not certify the factorial sequence, and a common ultrafriability cap does not equal the prime-dependent factorial valuations.

All finite tables are computational evidence or source-scope audits only. They do not prove an asymptotic factorial theorem.