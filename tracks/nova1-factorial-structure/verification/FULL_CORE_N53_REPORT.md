# Exact Meet-in-the-Middle Carrier Certificate at n=53

## Result IDs

- `N1-STR-024`: proved theorem, layer-normalized connected-prefix surplus.
- `N1-FIN-008`: finite certificate, complete connected-core carrier coverage at `n=53`.
- `N1-CMP-006`: computational evidence, normalized entropy diagnostics for `n=51,52,53`.

The factorial formulation of Erdős Problem 18 remains open. No finite result below is promoted to an asymptotic theorem.

## Frozen source

- repository: `Lumathpolgar/erdos18-factorial-program`
- branch: `nova/factorial-structure`
- predecessor head: `d8a6f299a29f6cb93e78178e83f16351d252692b`
- construction: `N1-CON-003`
- carrier engine: Nova 2 `N2-ADD-119` and `N2-ADD-120`
- meet-in-the-middle theorem: `N1-STR-023`

## Exact parameters

\[
r_{53}=16,
\qquad M_{53}=253,
\qquad v_2(53!)=49.
\]

The reserved odd core has `310,003,200` divisors. The balanced split is

\[
17{,}550\times17{,}664.
\]

The primary exact partition mask is `350`.

## Exact carrier result

The verifier emits `255,794,579` divisors before completing the certificate. The maximum merge heap contains `17,550` rows.

The six complete connected-prefix cardinalities are

\[
63{,}547,
\quad 1{,}308{,}251,
\quad 14{,}186{,}800,
\]

\[
70{,}586{,}242,
\quad 175{,}389{,}561,
\quad 255{,}794{,}579.
\]

The first five layers terminate at exact record gaps larger than their carrier thresholds. No blocking gap occurs before the sixth-layer cutoff.

The final occupied endpoint exceeds `Y_53` by

\[
257{,}219{,}713{,}671{,}656{,}581{,}137{,}253{,}687{,}630.
\]

Thus the six-layer quotient carrier reaches every quotient target through `Y_53`. Applying the exact marker-three correction reduction gives

\[
H_{53!}(\lfloor\sqrt{53!}\rfloor+1)
\le 6+r_{53}=22.
\]

This is `N1-FIN-008`, a finite certificate.

Combining the imported and Nova 1 certificates gives

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
\le22
\qquad(12\le n\le53).
\]

## Adversarial partition replay

The exact run was repeated with partition mask `414`. This mask places a different set of prime-power coordinates in the first half while retaining the same split dimensions.

After excluding the metadata field `mitm_partition_mask`, the two complete outputs agree exactly in every field:

- divisor count and split dimensions;
- emitted count;
- all six thresholds;
- all six connected maxima and `K_t` values;
- all five blocking gaps;
- every carrier endpoint;
- final margin and term bound;
- exact prefix product and exact finite requirement.

This checks that the certificate is independent of the chosen balanced coordinate partition.

## Normalized entropy diagnostics

Define

\[
P_n=\prod_{t=1}^{L}(1+K_t),
\qquad
Q_n=\left\lceil\frac{Y_n+1}{W_n+1}\right\rceil,
\]

and

\[
\Gamma_n=(P_n/Q_n)^{1/L},
\qquad
\Lambda_n=\log(\Gamma_n).
\]

The exact integer inputs and diagnostic decimal renderings are:

| `n` | `L` | `floor(P_n/Q_n)` | `Gamma_n` | `Lambda_n` |
|---:|---:|---:|---:|---:|
| 51 | 6 | 3,034,386,005,338 | 120.322026489 | 4.790171703 |
| 52 | 6 | 866,765,166,748 | 97.645052132 | 4.581338987 |
| 53 | 6 | 3,743,726,317,282 | 124.609364763 | 4.825183762 |

The sequence decreases from `n=51` to `n=52` and rebounds at `n=53`. Neither the raw ratio nor the layer-normalized surplus is monotone on this finite range.

All three values exceed the exact necessary threshold `Gamma_n>=1`. This is finite evidence only and supplies no uniform asymptotic lower bound.

## Reproduction

```text
g++ -O3 -std=c++20 \
  tracks/nova1-factorial-structure/verification/marker_three_mitm_prefix_u128.cpp \
  -o marker_three_mitm_prefix_u128

./marker_three_mitm_prefix_u128 53
./marker_three_mitm_prefix_u128 53 414
python tracks/nova1-factorial-structure/verification/test_mitm_n53_normalized.py
```

## Resource record

Primary run:

- wall time: `26.75` seconds;
- peak resident memory: `9,860 KiB`;
- exit status: `0`.

Alternate-partition run:

- wall time: `26.47` seconds;
- peak resident memory: `8,328 KiB`;
- exit status: `0`.

Resource timings are environment-dependent and are not mathematical claims.

## Claim boundary

This certificate does not prove uniform connected-prefix growth, quotient occupancy for all sufficiently large `n`, the final-only marker-three theorem, the factorial half-range theorem, or Erdős Problem 18.
