# Nova 3 Request H Adversarial Audit

This directory contains the canonical semantic contract and full adversarial audit for `N3-ANA-011`.

## Decision

```text
request H: ACCEPTED
N3-ANA-011: ACCEPTED
```

The accepted theorem proves, for every integer `n>=120368`:

- address legality;
- the imported high-prime menu cardinality bound;
- formal profile capacity at least `X_n+1`.

It does not prove profile injectivity, distinct numerical sums, additive occupancy, the factorial half-range theorem, or Erdős Problem 18.

## Replay

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

## Semantic hashes

```text
canonical contract: 63b5e3ae60a38f892768c791765a6f4dd99073586dbeada06e66f7c02b5caf8b
adversarial audit: 785517e04e7421348cad72e6e8d20718294dc9edaa32852f3e794ea2637503a9
final claim: a254a6dc271b174a8e5f809c67c22c75de5e6163f36e69a018cb0770f9b9b23c
```
