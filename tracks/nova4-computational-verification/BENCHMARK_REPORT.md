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

```text
H_{n!}(floor(sqrt(n!)) + 1) = 1 for 1 <= n <= 4,
H_{n!}(floor(sqrt(n!)) + 1) = 2 for 5 <= n <= 7,
H_{n!}(floor(sqrt(n!)) + 1) = 3 for 8 <= n <= 13.
```

## Smallest greedy counterexample

```text
n = 8
target = 155
greedy = 144 + 10 + 1
optimal = 140 + 15
```

## Resource limit

The exact Method A run for `n=14` did not complete within 30 seconds. Its status remains `unknown due to resource limits`.

## Lattice gate benchmark

The exact transition audit for every `3 <= n <= 10000` completed in approximately 1.9 seconds. The complete suite at that checkpoint contained 32 tests.

## Nova 1 capacity benchmark

The exact audit of all 999,998 integers in `3 <= n <= 1,000,000` completed in approximately 6.7 seconds. Peak resident memory was approximately 333 MB. The complete suite at that checkpoint contained 39 tests.

## Nova 1 reduced-rainbow benchmark

The deterministic Study B generation for all 61 cases in `20 <= n <= 80` completed in approximately 24.1 seconds. Peak resident memory was approximately 316 MiB.

The calculation used exact target-truncated integer bitsets through `T_n=10^7`, exact residue masks for every modulus `2<=q<=64`, and replayable record-gap witnesses. Eleven new reduced-rainbow tests passed.

## Nova 3 moment and local-ceiling benchmark

The exact finite audit for every `2 <= n <= 12` completed in approximately 2.35 seconds. Peak resident memory was approximately 288 MiB.

The run enumerated 1,978 exact divisors and checked 45,840 local windows. Local endpoint decisions used rationally certified `floor(d exp(Delta))` values rather than floating logarithm comparisons. Moment identities were checked exactly over exponent vectors and replayed with 80-digit decimal logarithms.

Ten new Nova 3 tests completed in approximately 3.7 seconds.

## Nova 3 scale-evidence benchmark

Request C generation completed in approximately 8.55 seconds with approximately 300 MiB peak resident memory.

The run produced:

```text
scale rows: 8
cutoff-grid tail rows: 63
theorem-path rows: 8
proxy prime limit: 1,000,000
proxy prime count: 78,498
```

All factorial valuations were exact integers. Logarithms, variance contributions, shares, effective dimensions, and tail ratios used 80-digit Decimal arithmetic. The frozen script's float formulas were independently replayed at all eight scale rows and nine printed tail points.

Thirteen new scale-evidence tests passed in approximately 2.7 seconds. They cover exact sieving and valuations, scale-row consistency, low-prime share totals, theorem half-span, cutoff admissibility flags, semantic replay, rehashed ratio and share corruption, wrong source metadata, frozen-script numerical cross-check, and the admissible theorem path.

No timeout or unknown result occurred in request C. All timings are engineering diagnostics, not mathematical claims.
