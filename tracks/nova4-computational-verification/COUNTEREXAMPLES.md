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

## N4-CE-002: Frozen valuation-tagged occupancy model fails at first target

Result class: `disproved finite claim`

Frozen claim owner: Nova 1 model imported and rejected by Nova 2.

Frozen sources:

```text
Nova 1 branch: nova/factorial-structure
Nova 1 commit: b939574eb88a08bb03abda5bbe6ff2ca97444e08
Nova 2 branch: nova/additive-occupancy
Nova 2 audit commit: 45c74a5fa747551422ffcad7d3ddf22788fbe622
```

For every layer, the lowest 2-adic address is at least `r_n+1`. Every main sum therefore lies in

```text
2^(r_n+1) Z.
```

The claimed correction radius is `2^r_n-1`, and the first requested target is `2^r_n`. Its required window is

```text
[1, 2^r_n],
```

which contains no multiple of `2^(r_n+1)`.

Concrete independently replayed admissible witness:

```text
n = 1892
r_n = 31
target = 2,147,483,648
common divisor = 4,294,967,296
empty window = [1, 2,147,483,648]
```

Certificate:

```text
certificates/lattice/n2_obs_107_n1892.json
```

Verification command:

```bash
PYTHONPATH=src python3 src/replay.py verify-n2-obs-107 \
  certificates/lattice/n2_obs_107_n1892.json
```

Scope of failure: only the exact frozen `N1-HO-N2-001` occupancy contract.

What remains possible: revised valuation-tagged models with a larger correction radius, lower common address, or residue-breaking labels.
