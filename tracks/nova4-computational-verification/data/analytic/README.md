# Nova 3 Analytic Data

Nova 3 requests A through C were frozen against `nova/analytic-density@0ce88b28dc2e6641093526f5777bb31f658e3515`, handoff `N3-HO-N4-001`.

Requests D through H and the final theorem closures were re-frozen against superseding handoff `N3-HO-N4-002` at commit `7469dada02fa4caca08ed391ef8b0cb0f1e855b2`.

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

## Full-model variance and non-Gaussian limit audit

The final `N3-ANA-006` closure independently reconstructs the normalized variance limit and the weak limit of the complete uniform-divisor model.

```bash
PYTHONPATH=src python3 src/replay_n3_variance.py verify \
  data/analytic/n3_variance_limit_audit.json
PYTHONPATH=src python3 src/replay_n3_variance.py verify-claim \
  certificates/analytic/n3_ana_006_final_claim.json \
  --audit data/analytic/n3_variance_limit_audit.json
```

Accepted statements:

```text
Var(S_n)/n^2 -> (1/12) sum_p (log p)^2/(p-1)^2
X_n => sum_p (log p)U_p
limiting series converges in L^2
limiting characteristic function vanishes at 2*pi/log(2)
full-model limit is non-Gaussian
```

```text
audit SHA-256: e1914a367749c8a397e77212c0d48c53335811e52418ffe0d8d1738046886119
claim SHA-256: efe6091759b788c9383b76799a6a62283a06d3d4f844f5a9e9199ed09d49dcf4
```

The ten-row convergence table through `n=1,000,000` is computational evidence only. The proof uses fixed-prime convergence and a uniform tail-variance estimate. This full-model non-Gaussian limit does not preclude a separate central limit theorem for the truncated high-prime tail.

Finite tables remain computational evidence or finite certificates only. No artifact here proves profile injectivity, distinct numerical sums, additive occupancy, or the factorial half-range theorem.
