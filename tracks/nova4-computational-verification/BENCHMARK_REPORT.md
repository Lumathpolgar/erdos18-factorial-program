# Initial Exact Benchmark Report

Date: 2026-07-15

Result class: `exact finite theorem audit`

Environment: CPython 3.13.5, standard library only, exact integers.

## Exact coverage

The complete interval

```text
0 <= x <= floor(sqrt(n!))
```

was computed for every `1 <= n <= 13`. Both exact methods agreed for all 109,947 targets.

| n | floor(sqrt(n!)) | tau(n!) | eligible divisors | exact H | greedy failures | DP seconds | bitset seconds |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 1 | 0 | 0.000015 | 0.000009 |
| 2 | 1 | 2 | 1 | 1 | 0 | 0.000028 | 0.000007 |
| 3 | 2 | 4 | 2 | 1 | 0 | 0.000016 | 0.000006 |
| 4 | 4 | 8 | 4 | 1 | 0 | 0.000017 | 0.000007 |
| 5 | 10 | 16 | 8 | 2 | 0 | 0.000024 | 0.000013 |
| 6 | 26 | 30 | 15 | 2 | 0 | 0.000042 | 0.000019 |
| 7 | 70 | 60 | 30 | 2 | 0 | 0.000163 | 0.000047 |
| 8 | 200 | 96 | 48 | 3 | 4 | 0.000688 | 0.000170 |
| 9 | 602 | 160 | 80 | 3 | 50 | 0.004228 | 0.000294 |
| 10 | 1904 | 270 | 135 | 3 | 260 | 0.021837 | 0.000881 |
| 11 | 6317 | 540 | 270 | 3 | 1133 | 0.165852 | 0.003906 |
| 12 | 21886 | 792 | 396 | 3 | 4515 | 1.065123 | 0.021452 |
| 13 | 78911 | 1584 | 792 | 3 | 18779 | 10.757055 | 0.175369 |

The timings are diagnostic measurements, not mathematical claims.

## Exact finite values

The exact interval maxima are:

```text
H_{n!}(floor(sqrt(n!)) + 1) = 1 for 1 <= n <= 4,
H_{n!}(floor(sqrt(n!)) + 1) = 2 for 5 <= n <= 7,
H_{n!}(floor(sqrt(n!)) + 1) = 3 for 8 <= n <= 13.
```

This is an exact finite theorem audit only. It does not imply a uniform asymptotic bound.

## Smallest greedy counterexample

The descending largest-divisor greedy algorithm is first suboptimal at:

```text
n = 8
target = 155
greedy = 144 + 10 + 1
optimal = 140 + 15
```

The two-term certificate is independently replayable. A one-term representation is impossible because `155` does not divide `8!`. Therefore the optimum is exactly two terms.

## Resource limit

An exact Method A run for `n=14` did not complete within a 30 second bounded attempt. Its status is:

```text
unknown due to resource limits
```

No mathematical conclusion is inferred for `n=14` from that timeout.

## Lattice gate benchmark

Environment: CPython 3.13.5, standard library only.

The complete unit suite now contains 32 tests and completes in approximately 0.2 seconds in the recorded environment.

The exact transition audit for every `3 <= n <= 10000` completes in approximately 1.9 seconds. It uses rational interval bounds for logarithmic ceilings and exact integer checks for factorial valuation and target admissibility.

These timings are engineering diagnostics, not mathematical claims.

## Nova 1 capacity benchmark

The exact audit of all 999,998 integers in `3 <= n <= 1,000,000` completed in approximately 6.7 seconds in the recorded container. Peak resident memory was approximately 333 MB.

The complete unit suite contains 39 tests and completed in approximately 7.0 seconds. These are engineering diagnostics, not mathematical claims.
