# Nova 1 Structural Verification

## Commands

```text
python tracks/nova1-factorial-structure/verification/structural_sanity.py
python tracks/nova1-factorial-structure/verification/marker_three_sanity.py
```

Both scripts use the Python standard library only, deterministic inputs, and exact integer arithmetic.

## Baseline structural checks

`structural_sanity.py` independently verifies finite instances of:

1. Legendre's valuation formula and the digit-sum identity;
2. exact quotient-band valuations for primes above `sqrt(n)`;
3. binary correction legality and exact representation;
4. 2-adic marker distinctness and palette disjointness;
5. complement-pair legality and numerical distinctness;
6. the high-prime subset-product menu count;
7. the downward-window counting inequality on exhaustive tiny cases.

Recorded result:

```text
PASS test_legendre_and_bands
PASS test_binary_palette
PASS test_marker_distinctness
PASS test_complement_pairing
PASS test_high_prime_menu_count
PASS test_window_counting_lemma
PASS all 6 structural sanity checks
```

## Marker-three repair checks

`marker_three_sanity.py` independently verifies:

1. legality of every generated marker-three divisor;
2. exact 2-adic layer addresses;
3. cross-layer numerical distinctness;
4. exact main lattice `3Z`;
5. palette disjointness and all residues modulo `3`;
6. the odd-digit one-gap lemma over a finite parameter grid;
7. exact quotient rainbow reachability for reduced admissible systems;
8. the quotient-to-main correction reduction;
9. full half-range reconstruction for every tested target.

Exact tested domain:

```text
7 <= n <= 14
r = 3
M = min(6, v_2(n!) + 1)
0 <= q <= floor(floor(sqrt(n!)) / 3)
```

Recorded result:

```text
PASS test_legality_distinctness_and_lattice
PASS test_odd_digit_one_gap
n=7 X=70 layers=5 q_targets=24 reachable_q=24 max_downward_distance=0
n=8 X=200 layers=6 q_targets=67 reachable_q=66 max_downward_distance=1
n=9 X=602 layers=6 q_targets=201 reachable_q=198 max_downward_distance=1
n=10 X=1904 layers=6 q_targets=635 reachable_q=622 max_downward_distance=1
n=11 X=6317 layers=6 q_targets=2106 reachable_q=2056 max_downward_distance=1
n=12 X=21886 layers=6 q_targets=7296 reachable_q=7080 max_downward_distance=1
n=13 X=78911 layers=6 q_targets=26304 reachable_q=25458 max_downward_distance=1
n=14 X=295259 layers=6 q_targets=98420 reachable_q=94710 max_downward_distance=1
PASS test_quotient_reduction_exhaustively
PASS all 3 marker-three checks
```

Detailed report:

`MARKER_THREE_FINITE_REPORT.md`

## Evidence status

- Baseline exact checks: **finite certificate** for their exact tested ranges.
- Marker-three quotient behavior: **computational evidence** for the exact tested domain.

Neither run proves the open asymptotic quotient occupancy theorem.
