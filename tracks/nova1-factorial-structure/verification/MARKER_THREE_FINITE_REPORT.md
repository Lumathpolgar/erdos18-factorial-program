# Marker-Three Finite Verification Report

Result label: **computational evidence**.

This report records exact finite checks for the repaired construction `N1-CON-003`. It does not prove the asymptotic quotient-window theorem.

## Command

```text
python tracks/nova1-factorial-structure/verification/marker_three_sanity.py
```

Environment used for the recorded run:

```text
CPython 3.13.5
standard library only
exact integer arithmetic
```

## Structural checks

The verifier checks:

1. every generated main term is a positive divisor of `n!` and lies below `floor(sqrt(n!))`;
2. every main term in layer `t` has exact 2-adic valuation `t-1`;
3. all main divisors are numerically distinct across layers;
4. every main divisor is divisible by `3` and no main divisor collides with the binary palette;
5. the main support lattice is exactly `3Z`;
6. palette subset sums attain all three residues modulo `3`;
7. the odd-digit one-gap lemma on a broad finite parameter grid;
8. exact quotient rainbow reachability for reduced admissible layer systems;
9. exact reconstruction of the complete factorial half-range from the quotient sums and palette.

## Exact reduced-parameter results

For each `7<=n<=14`, the run uses

```text
r = 3
M = min(6, v_2(n!) + 1)
```

so every tested address is legal. The full quotient range

\[
0\le q\le\left\lfloor\frac{\lfloor\sqrt{n!}\rfloor}{3}\right\rfloor
\]

is checked exhaustively.

| n | X=floor(sqrt(n!)) | layers | quotient targets | reachable quotient sums | maximum downward distance |
|---:|---:|---:|---:|---:|---:|
| 7 | 70 | 5 | 24 | 24 | 0 |
| 8 | 200 | 6 | 67 | 66 | 1 |
| 9 | 602 | 6 | 201 | 198 | 1 |
| 10 | 1904 | 6 | 635 | 622 | 1 |
| 11 | 6317 | 6 | 2106 | 2056 | 1 |
| 12 | 21886 | 6 | 7296 | 7080 | 1 |
| 13 | 78911 | 6 | 26304 | 25458 | 1 |
| 14 | 295259 | 6 | 98420 | 94710 | 1 |

The frozen reduced correction radius is

\[
W=\left\lfloor\frac{(2^3-1)-2}{3}\right\rfloor=1.
\]

No quotient-window failure occurs in the tested domain.

After multiplying quotient sums by `3` and adding the exact binary palette, every target

\[
0\le x\le\lfloor\sqrt{n!}\rfloor
\]

is reached for every tested `n`.

## Recorded output

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

## Claim boundary

The results are exact for the displayed finite parameters. They do not establish:

- the frozen asymptotic layer count `M_n=ceil(16(log n)^2)`;
- uniform quotient occupancy for all sufficiently large `n`;
- a maximum gap bound near the factorial half-range asymptotically;
- the Track B local-to-global implication;
- the main theorem.

The finite pattern is retained because it tests the corrected lattice, confirms the quotient reduction, and supplies regression cases for Nova 4.
