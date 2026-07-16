# Nova 3 Analytic Certificates

## Existing certificates

The directory preserves certificates for:

- the tight local-ceiling equality case;
- the bounded characteristic recurrence candidate;
- restricted-source compatibility;
- Dusart's explicit prime-interval theorem;
- the exact request G threshold sweep;
- the final scoped `N3-ANA-011` theorem;
- the final `N3-ANA-006` variance and non-Gaussian limit theorem.

Each certificate has a matching fail-closed semantic replay and preserves its source commit or blob metadata.

## Final N3-ANA-008 theorem certificate

```text
N3-ANA-008: ACCEPTED
B_ny^2 >> n^2 log(y)/y
M_ny = max_{p>y} b_p log(p)/2
M_ny/B_ny -> 0
T_ny/B_ny => N(0,1)
```

```bash
PYTHONPATH=src python3 src/replay_n3_high_prime.py verify-008 \
  certificates/analytic/n3_ana_008_final_claim.json \
  --audit data/analytic/n3_high_prime_limit_audit.json
```

Claim SHA-256: `5723c037725e1bc262bd109b65510d74833a28d8869f27903cd86c33473bf930`.

## Final N3-ANA-009 conditional theorem certificate

```text
N3-ANA-009: ACCEPTED_WITH_EXTERNAL_BERRY_ESSEEN_DEPENDENCY
0 < Delta <= B_ny
abs(x) <= B_ny
Delta >= (4 C_BE/phi(2)) M_ny
P{T_ny in [x,x+Delta]} >= (phi(2)/2) Delta/B_ny
```

```bash
PYTHONPATH=src python3 src/replay_n3_high_prime.py verify-009 \
  certificates/analytic/n3_ana_009_final_claim.json \
  --audit data/analytic/n3_high_prime_limit_audit.json
```

Claim SHA-256: `b3775b62ef887fbaa92e39e1ab729d6f093f360d778edfdc4a52a2a1e3397d7d`.

## Corruption replay

Eight committed fixtures recompute their outer checksums after changing the half-span normalization, growth hypotheses, full-model interpretation, finite/asymptotic classification, coarse-window condition, endpoint error count, external dependency, or fine-window scope.

```bash
PYTHONPATH=src python3 src/replay_n3_high_prime.py verify-fixtures \
  tests/n3_high_prime_fixtures \
  --audit data/analytic/n3_high_prime_limit_audit.json
```

All eight must fail semantic verification.

These certificates do not prove thin-window local limits, additive occupancy, the factorial half-range theorem, or Erdős Problem 18.
