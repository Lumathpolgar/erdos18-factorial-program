# N3-ANA-008 and N3-ANA-009 audit

This package independently reconstructs the high-prime-tail central limit theorem and the coarse Berry-Esseen window lower bound from the exact factorial exponent model.

## Decisions

```text
N3-ANA-008: ACCEPTED
N3-ANA-009: ACCEPTED_WITH_EXTERNAL_BERRY_ESSEEN_DEPENDENCY
```

The theorem-defined maximal centered coordinate size is

\[
M_{n,y}=\max_{p>y}\frac{v_p(n!)\log p}{2}.
\]

The earlier request C script reports the full span `2M`, so its displayed ratio is twice the theorem ratio.

## Replay

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

The finite table follows `y=floor(sqrt(n))/2` through `n=10,000,000`. It is computational evidence only. The asymptotic theorem uses the prime number theorem, exact valuation bounds, and the triangular-array Lindeberg argument. The coarse local theorem additionally uses the Berry-Esseen inequality recorded as `N3-SRC-003`.
