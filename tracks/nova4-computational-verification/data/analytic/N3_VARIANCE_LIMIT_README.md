# N3-ANA-006 variance-limit audit

This package independently reconstructs the full uniform-divisor limit theorem from the exact factorial exponent model.

## Accepted theorem

For

\[
X_n=\frac{S_n-\frac12\log(n!)}{n},
\]

Nova 4 accepts

\[
\frac{\operatorname{Var}(S_n)}{n^2}
\longrightarrow
\frac1{12}\sum_p\frac{(\log p)^2}{(p-1)^2},
\]

and

\[
X_n\Rightarrow\sum_p(\log p)U_p,
\]

where the independent variables `U_p` are uniform on

\[
[-1/(2(p-1)),1/(2(p-1))].
\]

The limiting characteristic function has a zero at `2*pi/log(2)`, so the full-model limit is not Gaussian.

## Replay

```bash
PYTHONPATH=src python3 src/replay_n3_variance.py verify \
  data/analytic/n3_variance_limit_audit.json

PYTHONPATH=src python3 src/replay_n3_variance.py verify-claim \
  certificates/analytic/n3_ana_006_final_claim.json \
  --audit data/analytic/n3_variance_limit_audit.json

PYTHONPATH=src python3 src/replay_n3_variance.py verify-fixtures \
  tests/n3_variance_fixtures \
  --audit data/analytic/n3_variance_limit_audit.json
```

## Artifacts

- `n3_variance_limit_audit.json`: complete semantic theorem audit;
- `n3_variance_convergence.csv`: finite computational diagnostics through `n=1,000,000`;
- `../../certificates/analytic/n3_ana_006_final_claim.json`: final theorem certificate;
- `../../tests/n3_variance_fixtures/`: five rehashed semantic corruptions.

The finite convergence table is computational evidence only. The asymptotic result comes from fixed-prime convergence and a uniform normalized tail-variance estimate.
