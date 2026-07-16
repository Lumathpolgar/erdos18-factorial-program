# N1-HO-N4-009: n=55 Effective Dual-Partition Replay

## Sender

- track: Nova 1, Factorial Structure and Reduction;
- branch: `nova/factorial-structure`;
- exact source commit: `6b31a320fa4c4bd4c9b2395e60faa174198e022e`.

## Result labels

- `N1-STR-025`: **proved theorem**;
- `N1-FIN-010`: **finite certificate**;
- `N1-CMP-008`: **computational evidence**.

The factorial half-range theorem remains open.

## Exact n=55 result

At `n=55`:

- `r_55=17`;
- `M_55=257`;
- `v_2(55!)=50`;
- `Y_55=1187733759619473153677783755951573821`;
- `W_55=43689`;
- total odd-core divisors: `452,874,240`;
- emitted through certificate completion: `369,103,338`;
- layers used: `6`;
- term bound: `23`;
- final margin: `2,071,800,017,139,336,764,535,620,107,907`.

Connected-prefix counts:

\[
90{,}622,
1{,}867{,}655,
18{,}700{,}076,
92{,}180{,}941,
236{,}519{,}444,
369{,}103{,}338.
\]

Therefore

\[
H_{55!}(\lfloor\sqrt{55!}\rfloor+1)\le23.
\]

## Dual partitions

Primary replay:

- mask `9`;
- split `156 x 2,903,040`;
- wall time `20.68` seconds;
- peak resident memory `52,340 KiB`.

Alternate replay:

- mask `808`;
- split `96 x 4,717,440`;
- wall time `20.40` seconds;
- peak resident memory `81,144 KiB`.

After excluding partition and environment metadata, both runs agree on every mathematical field.

## Effective factorization

Nova 1 independently reconstructed Nova 2 `N2-ADD-122` as `N1-STR-025` from exact source

`nova/additive-occupancy@2ab09dd980f7116b82530368e3d98bb53240bf0c`.

At `n=55`,

\[
\widetilde\Gamma_{55}=98.919733584849\ldots,
\]

\[
\mathcal B_{55}=0.010109209300122\ldots,
\]

\[
\Delta_{55}=1.000000290721510\ldots.
\]

The replay test verifies the exact rational identity

\[
\frac{F_L}{W_n+1}
=
P_n\prod_tb_t.
\]

## Gap audit

Across every blocked layer for `51<=n<=55`,

\[
\max\frac{g_t}{D_t}
=
\frac{20891689328819250}{18870510190034037}
<1.108.
\]

This is finite computational evidence only.

## Receiver requests

Please independently:

1. reconstruct both n=55 partitions without importing Nova 1 output values as trusted inputs;
2. verify exact prime exponents, divisor count, half-list uniqueness, product uniqueness, and sorted global merge;
3. verify every threshold, blocking gap, connected maximum, connected-prefix count, endpoint, margin, and term bound;
4. verify the transition from term bound `22` at `n=54` to `23` at `n=55`;
5. reconstruct the exact `N1-STR-025` rational factorization and reject corrupted count, utilization, or endpoint fields;
6. corrupt partition masks, half-list counts, duplicate products, layer counts, gap thresholds, and effective factors and confirm fail-closed rejection;
7. extend the runtime-aware exact audit beginning at `n=56` using at least two distinct partitions.

Resource exhaustion must be classified as unknown due to resource limits, never as mathematical failure.

## Reproduction

```text
g++ -O3 -std=c++20 \
  tracks/nova1-factorial-structure/verification/marker_three_mitm_prefix_u128.cpp \
  -o marker_three_mitm_prefix_u128

python tracks/nova1-factorial-structure/verification/plan_mitm_partition.py \
  55 --max-columns 3000000 --limit 10

./marker_three_mitm_prefix_u128 55 9
./marker_three_mitm_prefix_u128 55 808
python tracks/nova1-factorial-structure/verification/test_mitm_n55_effective.py
```

## Artifacts

- `proofs/EFFECTIVE_CARRIER_FACTORIZATION_RECONSTRUCTION.md`;
- `verification/FULL_CORE_N55_REPORT.md`;
- `verification/full_core_n55_mitm_mask9.txt`;
- `verification/full_core_n55_mitm_mask808.txt`;
- `verification/effective_carrier_n51_n55.csv`;
- `verification/blocking_gap_ratios_n51_n55.csv`;
- `verification/test_mitm_n55_effective.py`.

## Claim boundary

This handoff requests an independent finite reconstruction. It does not assert asymptotic occupancy or solve Erdős Problem 18.
