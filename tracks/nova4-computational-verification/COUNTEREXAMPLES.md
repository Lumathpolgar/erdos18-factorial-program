# Nova 4 Counterexample Registry

## N4-CE-001: Descending greedy is not always optimal

Result class: `counterexample`

Frozen finite claim tested:

> For every `n` and every target in the factorial half-range, repeatedly selecting the largest unused divisor of `n!` not exceeding the residual produces a minimum-term representation.

Smallest failing parameter in the exhaustive search over `1 <= n <= 13`:

```text
n = 8
target = 155
```

Greedy trace:

```text
155 -> choose 144, residual 11
11 -> choose 10, residual 1
1 -> choose 1, residual 0
```

Greedy term count: `3`.

Exact optimum:

```text
155 = 140 + 15
```

Optimal term count: `2`.

Lower-bound basis: `155` is not a divisor of `8!`, so no one-term representation exists.

Certificate:

```text
certificates/n8_target155_optimal.json
```

Verification command:

```bash
PYTHONPATH=src python3 src/replay.py verify \
  certificates/n8_target155_optimal.json
```

Scope of failure: descending largest-divisor greedy optimality.

What remains possible: greedy can still supply upper bounds or work on restricted target classes. This counterexample does not address the asymptotic factorial theorem.
