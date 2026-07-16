# Nova 3 Analytic Data

Nova 3 requests A through C were frozen against `nova/analytic-density@0ce88b28dc2e6641093526f5777bb31f658e3515`, handoff `N3-HO-N4-001`.

Requests D through H were re-frozen against superseding handoff `N3-HO-N4-002` at commit `7469dada02fa4caca08ed391ef8b0cb0f1e855b2`.

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

Request E reconstructs the source scope of Ford’s divisor-in-an-interval theorem, the Drappeau–Tenenbaum almost-all friable Gaussian law, and ultrafriable arithmetic-progression estimates.

```bash
PYTHONPATH=src python3 src/replay_n3_sources.py verify \
  data/analytic/n3_restricted_source_compatibility.json
PYTHONPATH=src python3 src/replay_n3_sources.py verify-claim \
  certificates/analytic/n3_restricted_source_compatibility.json
```

## Dusart primary-source theorem audit

Request F reconstructs Pierre Dusart’s Theorem 6.9, equation (6.6), and the independent algebra proving `N3-ANA-010`.

```bash
PYTHONPATH=src python3 src/replay_n3_dusart.py verify \
  data/analytic/n3_dusart_prime_interval_audit.json
PYTHONPATH=src python3 src/replay_n3_dusart.py verify-claim \
  certificates/analytic/n3_dusart_prime_interval_claim.json \
  --audit data/analytic/n3_dusart_prime_interval_audit.json
```

## Exact threshold sweep

Request G checks every integer `120368 <= n <= 1000000` and records the exact prime, Legendre, certified ceiling, address, and conservative formal-capacity minima.

```bash
PYTHONPATH=src python3 src/replay_n3_threshold.py verify \
  data/analytic/n3_threshold_sweep_n120368_n1000000.json
PYTHONPATH=src python3 src/replay_n3_threshold.py verify-claim \
  certificates/analytic/n3_threshold_sweep_claim.json \
  --audit data/analytic/n3_threshold_sweep_n120368_n1000000.json
```

The threshold sweep covers 879,633 integers. Its full audit semantic SHA-256 is `e26653648c2cc9ebc30b03f01904dbb5bcca65737ead57abc9cdbc0b2f218bb0`.

## Semantic adversarial theorem audit

Request H freezes the exact `N3-ANA-011` theorem contract, independently reconstructs its proof, and rejects all six required rehashed semantic corruptions.

```bash
PYTHONPATH=src python3 src/replay_n3_adversarial.py verify \
  data/analytic/n3_threshold_adversarial_audit.json
PYTHONPATH=src python3 src/replay_n3_adversarial.py verify-contract \
  data/analytic/n3_ana_011_contract.json
PYTHONPATH=src python3 src/replay_n3_adversarial.py verify-claim \
  certificates/analytic/n3_ana_011_final_claim.json
PYTHONPATH=src python3 src/replay_n3_adversarial.py verify-fixtures \
  tests/n3_adversarial_fixtures
```

The final decision is `N3-ANA-011: ACCEPTED`. The theorem proves address legality, menu cardinality, and formal profile capacity only.

```text
contract SHA-256: 63b5e3ae60a38f892768c791765a6f4dd99073586dbeada06e66f7c02b5caf8b
audit SHA-256: 785517e04e7421348cad72e6e8d20718294dc9edaa32852f3e794ea2637503a9
claim SHA-256: a254a6dc271b174a8e5f809c67c22c75de5e6163f36e69a018cb0770f9b9b23c
```

Finite tables remain computational evidence or finite certificates only. The accepted theorem comes from the proof reconstruction, not from extrapolating request G. No artifact here proves profile injectivity, distinct numerical sums, additive occupancy, or the factorial half-range theorem.
