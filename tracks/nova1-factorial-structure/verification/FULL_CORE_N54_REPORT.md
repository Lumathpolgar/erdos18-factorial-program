# Exact Full-Core Carrier Report at n=54

## Classification

Result label: **finite certificate**.

Certificate ID: `N1-FIN-009`.

The factorial half-range theorem and Erdős Problem 18 remain open.

## Frozen construction

This report uses the marker-three valuation rainbow `N1-CON-003` and the exact meet-in-the-middle connected-prefix stream from `N1-STR-023`.

For `n=54`:

\[
r_{54}=16,
\qquad
M_{54}=255,
\qquad
v_2(54!)=50.
\]

The quotient endpoint and correction radius are

\[
Y_{54}=160153987475679647486755841698814824,
\]

\[
W_{54}=21844.
\]

## Exact divisor family

The reserved odd core has

\[
350{,}438{,}400
\]

divisors.

The primary explicit partition mask `255` gives

\[
128\times2{,}737{,}800.
\]

The alternate mask `223` gives

\[
512\times684{,}450.
\]

Both partitions enumerate the same exact divisor family and produce identical carrier data after partition and environment fields are removed.

## Connected-prefix certificate

The exact positive connected-prefix cardinalities are

\[
K_1=63{,}547,
\]

\[
K_2=1{,}308{,}259,
\]

\[
K_3=14{,}197{,}074,
\]

\[
K_4=71{,}967{,}365,
\]

\[
K_5=185{,}071{,}301,
\]

\[
K_6=287{,}853{,}491.
\]

The sixth layer has no blocking gap before its cutoff. The carrier endpoint is

\[
160154309278397458660217398005238511.
\]

Adding the correction radius gives

\[
160154309278397458660217398005260355.
\]

The exact positive margin over `Y_54` is

\[
321802717811173461556306445531.
\]

Therefore

\[
H_{54!}(\lfloor\sqrt{54!}\rfloor+1)\le22.
\]

Combining `N2-FIN-202`, `N1-FIN-005`, `N1-FIN-006`, `N1-FIN-007`, `N1-FIN-008`, and `N1-FIN-009` gives

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le22
\qquad(12\le n\le54).
\]

This is a finite theorem only.

## Exact entropy data

The connected-prefix product is

\[
P_{54}=4525233744675622115970119580522296824224000.
\]

The exact finite requirement is

\[
Q_{54}=7331379605203920690627413215785.
\]

Thus

\[
\left\lfloor\frac{P_{54}}{Q_{54}}\right\rfloor
=617241772812.
\]

The layer-normalized surplus from `N1-STR-024` is approximately

\[
\Gamma_{54}=92.27326436677728.
\]

The finite values for `n=51,52,53,54` are non-monotone. No asymptotic trend is inferred.

## Finite divisor-gap diagnostic

Result label: **computational evidence**.

For each blocked layer, compare the first blocking gap `g_t` with the exact threshold `D_t`. Across the twenty blocked layers for `51<=n<=54`,

\[
\max\frac{g_t}{D_t}
=
\frac{20891689328819250}{18870510190034037}
<1.108.
\]

The maximum occurs at `n=51`, layer `4`.

This finite diagnostic does not prove a uniform divisor-gap theorem.

## Resource audit

Primary mask `255`:

- rows: `128`;
- columns: `2,737,800`;
- wall time: `15.31` seconds;
- peak resident memory: `49,032 KiB`;
- exit status: `0`.

Alternate mask `223`:

- rows: `512`;
- columns: `684,450`;
- wall time: `18.57` seconds;
- peak resident memory: `18,056 KiB`;
- exit status: `0`.

The balanced `18,720 x 18,720` partition emitted `230,000,000` divisors before the six-minute execution boundary and did not complete. This is a resource boundary for that partition, not a mathematical failure.

The exact partition planner shows that row count and column storage must be treated as separate runtime and memory controls.

## Replay

```text
g++ -O3 -std=c++20 \
  tracks/nova1-factorial-structure/verification/marker_three_mitm_prefix_u128.cpp \
  -o marker_three_mitm_prefix_u128

python tracks/nova1-factorial-structure/verification/plan_mitm_partition.py \
  54 --max-columns 3000000 --limit 10

./marker_three_mitm_prefix_u128 54 255
./marker_three_mitm_prefix_u128 54 223

python tracks/nova1-factorial-structure/verification/test_mitm_n54_partition.py
```

Expected test output:

```text
PASS exact n=54
PASS alternate partition n=54
PASS exact connected-prefix counts
PASS normalized non-monotonicity through n=54
PASS finite first-blocking-gap ratio below 1.108
PASS all n=54 meet-in-the-middle checks
```

## Claim boundary

This certificate does not prove uniform connected-prefix growth, the quotient downward-window theorem, the final endpoint window asymptotically, the factorial half-range theorem for all sufficiently large `n`, or Erdős Problem 18.
