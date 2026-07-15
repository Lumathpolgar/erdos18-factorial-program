# Exact Full-Core Carrier Extension Through n=50

## Result ID

`N1-FIN-005`

Result label: **finite certificate**.

## Scope

This report independently extends the exact complete odd-core carrier audit through

\[
46\le n\le50.
\]

The imported predecessor is:

- branch: `nova/additive-occupancy`;
- exact commit: `82603c631a106c3bff4676bdeeb9cc791fc98f3c`;
- finite certificate: `N2-FIN-202`;
- audited range: `12<=n<=45`;
- proof: `tracks/nova2-additive-occupancy/proofs/MARKER_THREE_FINITE_FULL_MENU_AUDIT.md`.

Nova 1 did not reuse the predecessor payload as a substitute for computation. It independently generated the complete truncated odd-core menus and replayed the exact `N2-ADD-120` recursion.

## Exact verifier

Source:

`verification/marker_three_full_core_u128.cpp`

The verifier:

1. computes prime valuations in `n!` exactly;
2. reserves one factor of `3` and removes the complete 2-adic valuation;
3. certifies `r_n` and `M_n` using rational lower and upper bounds for `log n`;
4. computes `floor(sqrt(n!))` with arbitrary-precision integer arithmetic;
5. generates every odd core divisor not exceeding `Y_n`;
6. sorts the complete truncated core set;
7. applies the exact connected-core gap threshold at every layer;
8. stops only when the occupied endpoint reaches `Y_n` or the legal layer budget is exhausted;
9. rejects unsupported endpoints, duplicate cores, parameter-certification failure, and declared resource-limit overflow.

The stored core values use unsigned 128-bit integers. The verifier is therefore deliberately restricted to `12<=n<=50`. This is a fail-closed implementation boundary, not a mathematical boundary.

## Build and reproduction

```text
g++ -O3 -std=c++17 \
  tracks/nova1-factorial-structure/verification/marker_three_full_core_u128.cpp \
  -o marker_three_full_core_u128

./marker_three_full_core_u128 --n 46 --max-values 30000000
./marker_three_full_core_u128 --n 47 --max-values 60000000
./marker_three_full_core_u128 --n 48 --max-values 60000000
./marker_three_full_core_u128 --n 49 --max-values 80000000
./marker_three_full_core_u128 --n 50 --max-values 80000000
```

Dependencies:

- C++17 compiler;
- Boost headers for `cpp_int` and exact rational arithmetic;
- no network access;
- no floating-point parameter decisions.

## Exact summary

| n | Total odd cores | Generated cores `<=Y_n` | Layers | `Y_n` | Occupied through | Margin |
|---:|---:|---:|---:|---:|---:|---:|
| 46 | 27,941,760 | 24,567,748 | 6 | 24,726,553,787,403,193,575,874,580,719 | 24,938,550,582,416,882,103,407,947,983 | 211,996,795,013,688,527,533,367,264 |
| 47 | 55,883,520 | 48,966,794 | 6 | 169,516,712,224,674,565,219,483,890,061 | 172,700,266,481,103,715,915,641,006,385 | 3,183,554,256,429,150,696,157,116,324 |
| 48 | 58,544,640 | 52,400,981 | 6 | 1,174,446,233,220,674,217,835,300,192,240 | 1,178,063,465,166,860,608,597,996,710,577 | 3,617,231,946,186,390,762,696,518,337 |
| 49 | 75,271,680 | 66,785,773 | 6 | 8,221,123,632,544,719,524,847,101,345,683 | 8,225,440,567,980,514,473,029,671,947,169 | 4,316,935,435,794,948,182,570,601,486 |
| 50 | 88,957,440 | 78,715,976 | 6 | 58,132,122,695,453,537,232,069,776,546,341 | 58,136,587,048,292,518,061,385,718,647,169 | 4,464,352,838,980,829,594,210,082,828 |

Every case reaches the full quotient endpoint.

Therefore the exact carrier recursion has now been independently certified for every

\[
12\le n\le50,
\]

combining `N2-FIN-202` for `12<=n<=45` with `N1-FIN-005` for `46<=n<=50`.

## Connected-prefix sizes

The six connected-prefix cardinalities are:

| n | Layer 1 | Layer 2 | Layer 3 | Layer 4 | Layer 5 | Layer 6 |
|---:|---:|---:|---:|---:|---:|---:|
| 46 | 34,440 | 460,959 | 3,095,862 | 10,245,320 | 19,665,818 | 22,618,189 |
| 47 | 46,139 | 749,791 | 5,809,809 | 20,999,736 | 40,436,010 | 45,072,254 |
| 48 | 46,139 | 749,810 | 5,815,268 | 21,143,542 | 41,487,479 | 48,751,484 |
| 49 | 46,171 | 756,948 | 6,061,954 | 23,448,410 | 49,168,539 | 62,081,094 |
| 50 | 46,172 | 757,894 | 6,133,662 | 24,454,870 | 53,700,532 | 73,292,397 |

The final layer is connected through its complete truncated menu in all five cases.

## Separation from the one-block route

At `n=46`, the first carrier threshold is

\[
D_1=W_{46}+1=21845.
\]

A single factorial arithmetic block from `N1-DIS-006` can certify first-layer reach at most

\[
\frac n2D_1=502435.
\]

The complete core component instead reaches

\[
49786217.
\]

Thus the full connected component exceeds the one-block envelope by a factor greater than `99` in this exact case.

This is a finite certificate that multiple divisor blocks interact strongly. It does not prove that the complete component has the required asymptotic growth.

## Resource record

The measured runs used approximately:

| n | Wall time | Peak resident memory |
|---:|---:|---:|
| 46 | 2.6 s | 392 MB |
| 47 | 5.2 s | 773 MB |
| 48 | 5.4 s | 826 MB |
| 49 | 7.0 s | 1.05 GB |
| 50 | 8.3 s | 1.24 GB |

These measurements are environment-specific computational records. They are not mathematical claims.

## Machine-readable records

- `verification/full_core_n46_n50_summary.csv`;
- `verification/full_core_n46_n50_layers.csv`.

The first file freezes the exact endpoint summary. The second freezes every layer threshold, connected maximum, connected-prefix cardinality, first blocking gap, and carrier endpoint.

## Result boundary

This certificate proves only the five displayed finite cases.

It does not prove:

- success at `n=51`;
- a uniform connected-core divisor-gap theorem;
- the asymptotic marker-three quotient theorem;
- the final-only Fourier theorem;
- the factorial half-range theorem for all sufficiently large `n`;
- Erdős Problem 18.

The next asymptotic node is `N1-OBS-003`: a successful carrier proof must produce connected prefixes with geometric-mean size at least `exp(n/(85 log n))` for `n>=120368`.