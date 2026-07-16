# Independent Audit of N2-ADD-115 and N2-OBS-107

Date: 2026-07-15

Result class: `exact finite theorem audit`

Audit outcome: `ACCEPTED`

## Frozen sources

- Nova 2 branch: `nova/additive-occupancy`
- Nova 2 commit: `45c74a5fa747551422ffcad7d3ddf22788fbe622`
- Proof: `tracks/nova2-additive-occupancy/proofs/VALUATION_TAGGED_LATTICE_OBSTRUCTION.md`
- Handoff: `N2-HO-N4-001-v2`
- Frozen Nova 1 branch: `nova/factorial-structure`
- Frozen Nova 1 commit tested by Nova 2: `b939574eb88a08bb03abda5bbe6ff2ca97444e08`
- Frozen object: `N1-HO-N2-001`

No later Nova 1 construction is included in this acceptance.

## Statement reconstructed

For the frozen construction,

```text
r_n = ceil(4 log n)
M_n = ceil(16 (log n)^2)
e_t = r_n + t, 1 <= t <= M_n
R_n = 2^r_n - 1
```

Every nonzero term in layer `t` contains the factor `2^e_t`. Since `e_t >= r_n + 1`, every main term and every restricted rainbow sum is divisible by

```text
g_n = 2^(r_n + 1).
```

The first requested target is

```text
x_n = R_n + 1 = 2^r_n.
```

Its downward window is

```text
[x_n - R_n, x_n] = [1, 2^r_n].
```

This interval contains no multiple of `g_n`, because its largest element is `g_n / 2`. The empty sum is zero and is outside the interval. Therefore the frozen occupancy statement fails at its first requested target whenever that target and the valuation-budget side condition are admissible.

## General lemma check

The proof uses the following exact lemma.

If `S` is contained in `g Z`, `g >= 2`, and `0 <= R <= g - 2`, then the window for `x = R + 1` is `[1, R + 1]`, which is contained in `[1, g - 1]`. It therefore contains no element of `S`.

The quantifiers, endpoints, and use of zero are correct.

## Asymptotic admissibility check

The proof requires that the side conditions eventually hold.

1. `v_2(n!) >= floor(n/2)` is immediate from the multiples of two in `n!`.
2. `r_n + M_n = O((log n)^2) = o(n)`, so the valuation-budget inequality eventually holds.
3. `2^r_n` grows polynomially in `n`, while `sqrt(n!)` grows faster than every fixed power. The supplied lower bound using at least `floor(n/2)` factors of size at least `n/2` is sufficient.

These arguments establish eventual admissibility. The obstruction is therefore not merely a small-parameter artifact.

## Independent exact replay

The verifier uses rational lower and upper bounds for `log n`. It does not trust binary floating-point evaluations of the ceiling functions.

For `n = 1892`, it recomputes:

```text
r_n = 31
M_n = 911
v_2(n!) = 1886
r_n + M_n <= floor(v_2(n!)/2) - 1
R_n = 2,147,483,647
x_n = 2,147,483,648
g_n = 4,294,967,296
window = [1, 2,147,483,648]
```

The target is exactly certified to lie below or at `floor(sqrt(n!))` by checking `x_n^2 <= n!` with integers.

## Exhaustive finite transition audit

Every `3 <= n <= 10000` was checked.

- First target-range success: `n = 9`
- First valuation-budget success: `n = 1892`
- First simultaneous admissible obstruction: `n = 1892`
- Later temporary side-condition failures: `n = 1893, 1894, 1895`
- Simultaneous success for every checked `1896 <= n <= 10000`

The temporary failures are caused by a ceiling transition in `M_n`. They do not contradict the theorem's sufficiently-large quantifier.

## Audit decision

`N2-ADD-115` is accepted as a correct theorem for the exact frozen construction.

`N2-OBS-107` is accepted as a correct disproof of the exact frozen model `N1-HO-N2-001`.

This audit does not disprove the factorial half-range theorem, valuation tagging in general, or any later repaired Nova 1 construction.

## Replay commands

```bash
PYTHONPATH=src python3 src/replay.py verify-n2-obs-107 \
  certificates/lattice/n2_obs_107_n1892.json

PYTHONPATH=src python3 src/replay.py audit-n2-obs-107 \
  --n-min 3 --n-max 10000 \
  --output data/lattice/n2_obs_107_range_n3_n10000.json

PYTHONPATH=src python3 -m unittest discover -s tests -v
```
