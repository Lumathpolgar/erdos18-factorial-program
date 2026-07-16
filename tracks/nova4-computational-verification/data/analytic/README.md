# Nova 3 Analytic Data

Nova 3 requests A through C were frozen against `nova/analytic-density@0ce88b28dc2e6641093526f5777bb31f658e3515`, handoff `N3-HO-N4-001`.

Requests D through H and all final theorem closures were frozen against `N3-HO-N4-002` at commit `7469dada02fa4caca08ed391ef8b0cb0f1e855b2`.

## Existing replay commands

```bash
PYTHONPATH=src python3 src/replay_n3.py verify \
  data/analytic/n3_moment_local_n2_n12.json

PYTHONPATH=src python3 src/replay_n3_sources.py verify \
  data/analytic/n3_restricted_source_compatibility.json

PYTHONPATH=src python3 src/replay_n3_dusart.py verify \
  data/analytic/n3_dusart_prime_interval_audit.json

PYTHONPATH=src python3 src/replay_n3_threshold.py verify \
  data/analytic/n3_threshold_sweep_n120368_n1000000.json

PYTHONPATH=src python3 src/replay_n3_adversarial.py verify \
  data/analytic/n3_threshold_adversarial_audit.json

PYTHONPATH=src python3 src/replay_n3_variance.py verify \
  data/analytic/n3_variance_limit_audit.json
```

The scale audit records that the frozen request C script reports `2M/B`, not theorem-defined `M/B`.

## High-prime CLT and coarse-window audit

```bash
PYTHONPATH=src python3 src/replay_n3_high_prime.py verify \
  data/analytic/n3_high_prime_limit_audit.json

PYTHONPATH=src python3 src/replay_n3_high_prime.py verify-008 \
  certificates/analytic/n3_ana_008_final_claim.json \
  --audit data/analytic/n3_high_prime_limit_audit.json

PYTHONPATH=src python3 src/replay_n3_high_prime.py verify-009 \
  certificates/analytic/n3_ana_009_final_claim.json \
  --audit data/analytic/n3_high_prime_limit_audit.json

PYTHONPATH=src python3 src/replay_n3_high_prime.py verify-fixtures \
  tests/n3_high_prime_fixtures \
  --audit data/analytic/n3_high_prime_limit_audit.json
```

Accepted results:

```text
N3-ANA-008: ACCEPTED
B_ny^2 >> n^2 log(y)/y
M_ny = max b_p log(p)/2
M_ny/B_ny -> 0
T_ny/B_ny => N(0,1)

N3-ANA-009: ACCEPTED_WITH_EXTERNAL_BERRY_ESSEEN_DEPENDENCY
Delta >= (4 C_BE/phi(2)) M_ny
P{T_ny in [x,x+Delta]} >= (phi(2)/2) Delta/B_ny
```

```text
audit SHA-256: a9c089489b38990c6de044611a21d8a488166dd0ad570456fee54a0020dc9dd2
N3-ANA-008 claim SHA-256: 5723c037725e1bc262bd109b65510d74833a28d8869f27903cd86c33473bf930
N3-ANA-009 claim SHA-256: b3775b62ef887fbaa92e39e1ab729d6f093f360d778edfdc4a52a2a1e3397d7d
```

Finite tables remain computational evidence or finite certificates only. No artifact here proves profile injectivity, distinct numerical sums, additive occupancy, or the factorial half-range theorem.
