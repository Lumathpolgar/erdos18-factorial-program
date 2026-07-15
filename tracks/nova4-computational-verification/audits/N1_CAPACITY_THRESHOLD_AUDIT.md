# Independent Audit of Nova 1 Capacity Predicates

Date: 2026-07-15

Result class: `exact finite theorem audit`

Audit outcome: `ACCEPTED_FOR_FINITE_RANGE`

## Frozen source

- Branch: `nova/factorial-structure`
- Commit: `fa11f4b2cb86a2dd791df189ada12757be791804`
- Handoff: `N1-HO-N4-001`
- Study: Study A, exact capacity-threshold audit
- Nova 4 implementation and certificate checkpoint: `53b579cd5a7eeac780869cffa2cb8b9b8bdd5289`

No later Nova 1 revision is included.

## Audited range

Every integer `3 <= n <= 1,000,000` was checked. The audit recomputed

```text
V_n = v_2(n!)
m_n = pi(n)-pi(floor(n/2))
r_n = ceil(4 log n)
M_n = ceil(16(log n)^2)
K_n = M_n(m_n-1)+r_n
```

using exact integer arithmetic and rationally certified logarithmic transition boundaries.

## Predicate A

```text
A_n: r_n+M_n <= floor(V_n/2)-1
```

Exact result:

- first success: `n=1892`;
- later failures after first success: `n=1893,1894,1895`;
- success at `n=1892` and every checked `1896 <= n <= 1,000,000`.

The temporary failures are caused by the ceiling jump `M_1892=911` to `M_1893=912` before the 2-adic budget grows enough to recover.

## Predicate C

```text
C_n: 2^K_n >= floor(sqrt(n!))+1
```

The verifier uses the exact equivalence

```text
2^K >= floor(sqrt(n!))+1  iff  2^(2K) > n!.
```

For `n<=12`, it constructs `n!` exactly and uses integer square root. For every `n>=13` in the audited range, it verifies the stronger integer certificate

```text
2K >= n*bit_length(n),
```

which gives

```text
n! <= n^n < 2^(n*bit_length(n)) <= 2^(2K).
```

Exact result:

- `C_n` succeeds for `3<=n<=9`;
- `C_10` fails because `2^10=1024 < floor(sqrt(10!))+1=1905`;
- `C_n` succeeds for every checked `11<=n<=1,000,000`.

## Simultaneous threshold

The smallest `n` satisfying both predicates is `n=1892`. Both predicates then fail simultaneously only through the `A_n` failures at `1893,1894,1895`. They hold together for every checked `1896<=n<=1,000,000`.

## Certified minimum margins for C

For `3<=n<=9`, the actual minimum occurs at `n=6`:

```text
8 log 2 - log 27
in [2.2493405784752334011521212608978,
    2.2493405784752334011521212608979].
```

For `11<=n<=1,000,000`, the actual minimum occurs at `n=11`:

```text
102 log 2 - log 6318
in [61.949854435752391058110730641097,
    61.949854435752391058110730641098].
```

For every `n>=13`, a separate exact bit-length lower bound was checked. Its smallest coefficient occurs at `n=14` and is already larger than the certified upper margin at `n=11`.

## Transition rows

The only truth-state transition rows are `n = 3, 10, 11, 1892, 1893, 1896`. They are committed in `data/capacity/n1_capacity_transitions_n3_n1000000.csv`.

## Replay

```bash
PYTHONPATH=src python3 src/replay.py verify-n1-capacity \
  certificates/capacity/n1_capacity_audit_n3_n1000000.json
```

Semantic certificate checksum:

```text
3c88c2e578af86f8a760ead6f9f12bc77af5349106f9e0406aae06cfb981a7d4
```

## Scope restriction

This audit is a finite certificate for the two numerical capacity predicates. It does not prove additive occupancy, the Nova 1 conditional reduction, the factorial half-range theorem, or the global Erdős Problem 18 target.
