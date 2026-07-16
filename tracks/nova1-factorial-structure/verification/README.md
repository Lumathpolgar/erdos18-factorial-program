# Nova 1 Structural Verification

## Result-label rule

Every verification artifact is classified as one of:

- **finite certificate**;
- **computational evidence**.

Verification never promotes an open asymptotic statement to a proved theorem.

## Baseline exact checks

```text
python tracks/nova1-factorial-structure/verification/structural_sanity.py
python tracks/nova1-factorial-structure/verification/marker_three_sanity.py
python tracks/nova1-factorial-structure/verification/endpoint_support_sanity.py
python tracks/nova1-factorial-structure/verification/block_collision_sanity.py
```

These deterministic scripts use exact integer arithmetic and check valuation identities, legality, distinctness, support lattices, correction residues, endpoint support, factorial blocks, and carry collisions.

## Materialized complete-core verifier

Source:

`marker_three_full_core_u128.cpp`

This materializes every truncated odd core and is deliberately restricted to `12<=n<=50`.

`N1-FIN-005`, **finite certificate**, proves exact carrier coverage for `46<=n<=50`. Combined with Nova 2 `N2-FIN-202`, the exact range through `n=50` is closed.

## Unique-parent streaming verifier

Source:

`marker_three_streaming_prefix_u128.cpp`

This reconstructs Nova 2 `N2-ADD-121` with a unique-parent priority-queue divisor stream and record-gap left counts.

`N1-FIN-006`, **finite certificate**, certifies `n=51` with six carrier layers and term bound `22`.

## Meet-in-the-middle verifier

Source:

`marker_three_mitm_prefix_u128.cpp`

Build:

```text
g++ -O3 -std=c++20 \
  tracks/nova1-factorial-structure/verification/marker_three_mitm_prefix_u128.cpp \
  -o marker_three_mitm_prefix_u128
```

Usage:

```text
./marker_three_mitm_prefix_u128 n partition_mask
```

The verifier performs:

1. exact rational certification of `r_n` and `M_n`;
2. exact factorial valuations and integer square roots;
3. exact generation and sorting of two half-divisor lists;
4. duplicate rejection within each half;
5. exact count verification `|A||B|=tau(D_n)`;
6. exact minimum-heap row merge;
7. strict global-order and duplicate rejection;
8. exact connected-prefix thresholds and counts;
9. exact endpoint, margin, entropy-product, and requirement calculations;
10. fail-closed unsigned 128-bit endpoint checks.

Proof:

`../proofs/MEET_IN_THE_MIDDLE_CONNECTED_PREFIX_STREAM.md`.

## Runtime-aware partition planner

Source:

`plan_mitm_partition.py`

Usage:

```text
python tracks/nova1-factorial-structure/verification/plan_mitm_partition.py \
  n --max-columns 3000000 --limit 10
```

The planner enumerates exact prime-coordinate masks, verifies total divisor count, and ranks partitions by active merge rows subject to an explicit stored-column bound.

## Exact certificates

### N1-FIN-007 at n=52

Result label: **finite certificate**.

Six layers reach the endpoint with term bound `22`.

Artifacts:

- `FULL_CORE_N52_REPORT.md`;
- `full_core_n52_mitm.txt`;
- `full_core_n51_mitm_overlap.txt`;
- `test_mitm_overlap.py`.

### N1-FIN-008 at n=53

Result label: **finite certificate**.

Masks `350` and `414` produce identical exact mathematical output. Six layers reach the endpoint with term bound `22`.

Artifacts:

- `FULL_CORE_N53_REPORT.md`;
- `full_core_n53_mitm.txt`;
- `full_core_n53_mitm_mask414.txt`;
- `test_mitm_n53_normalized.py`.

### N1-FIN-009 at n=54

Result label: **finite certificate**.

- total odd-core divisors: `350,438,400`;
- primary mask `255`: `128 x 2,737,800`;
- alternate mask `223`: `512 x 684,450`;
- emitted through certificate: `287,853,491`;
- layers: `6`;
- term bound: `22`.

The balanced `18,720 x 18,720` partition did not complete within its execution boundary. This was a partition-specific resource boundary, not a mathematical failure.

### N1-FIN-010 at n=55

Result label: **finite certificate**.

- total odd-core divisors: `452,874,240`;
- primary mask `9`: `156 x 2,903,040`;
- alternate mask `808`: `96 x 4,717,440`;
- emitted through certificate: `369,103,338`;
- layers: `6`;
- term bound: `23`.

The term-bound increase is caused by `r_55=17`.

### N1-FIN-011 at n=56

Result label: **finite certificate**.

Exact parameters:

\[
r_{56}=17,
\qquad
M_{56}=260,
\qquad
v_2(56!)=53.
\]

- total odd-core divisors: `503,193,600`;
- primary mask `98`: `168 x 2,995,200`;
- alternate mask `33`: `104 x 4,838,400`;
- emitted through certificate: `411,604,587`;
- layers: `7`;
- term bound: `24`;
- final margin: `2,123,056,480,890,000,163,585,785,602,493,899,728`.

Connected-prefix counts:

\[
90{,}625,
1{,}870{,}175,
18{,}876{,}460,
95{,}201{,}963,
252{,}731{,}752,
404{,}825{,}440,
411{,}604{,}587.
\]

After six layers,

\[
F_6/(Y_{56}+1)=0.23886288252245\ldots<1.
\]

The seventh layer is therefore necessary and completes without a blocking gap before its cutoff.

Reproduction:

```text
python tracks/nova1-factorial-structure/verification/plan_mitm_partition.py \
  56 --max-columns 3000000 --limit 10

./marker_three_mitm_prefix_u128 56 98
./marker_three_mitm_prefix_u128 56 33
python tracks/nova1-factorial-structure/verification/test_mitm_n56_parity.py
```

Expected result:

```text
PASS exact n=56
PASS alternate partition n=56
PASS seven-layer transition and term bound 24
PASS effective factorization through n=56
PASS parity-only deficit diagnostic
PASS finite first-blocking-gap ratio below 1.108 through n=56
PASS all n=56 parity-span carrier checks
```

Artifacts:

- `FULL_CORE_N56_REPORT.md`;
- `full_core_n56_mitm_mask98.txt`;
- `full_core_n56_mitm_mask33.txt`;
- `effective_carrier_n51_n56.csv`;
- `blocking_gap_ratios_n51_n56.csv`;
- `parity_span_effective_n51_n56.csv`;
- `test_mitm_n56_parity.py`.

## Exact finite boundary

Combining Nova 2 and Nova 1 certificates gives

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le22
\qquad(12\le n\le54),
\]

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le23
\qquad(12\le n\le55),
\]

and

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le24
\qquad(12\le n\le56).
\]

These are finite only. The smallest unaudited parameter is `n=57`.

## Exact effective carrier theorem

`N1-STR-025` is a **proved theorem**. For

\[
P_n=\prod_{t=1}^{L}(1+K_t),
\qquad
b_t=\frac{F_t/F_{t-1}}{1+K_t},
\]

\[
\frac{F_L}{W_n+1}=P_n\prod_tb_t.
\]

With

\[
\widetilde\Gamma_n=(P_n/R_n)^{1/L},
\qquad
\mathcal B_n=\left(\prod_tb_t\right)^{1/L},
\]

\[
\Delta_n=\left(\frac{F_L}{Y_n+1}\right)^{1/L},
\]

one has

\[
\Delta_n=\widetilde\Gamma_n\mathcal B_n.
\]

At `n=56`:

\[
\widetilde\Gamma_{56}=673.791460795324\ldots,
\]

\[
\mathcal B_{56}=0.001530254006653\ldots,
\]

\[
\Delta_{56}=1.031072082530349\ldots.
\]

## Sharp parity-span baseline

`N1-STR-026` and `N1-OBS-004` are **proved theorems**.

Every positive odd-core prefix satisfies

\[
U_t\ge2K_t-1.
\]

The resulting parity-only carrier product is optimal if only oddness, count, and threshold are supplied. At `n=56`, its endpoint-ratio seventh root is

\[
0.0000307763983342963\ldots,
\]

and its unrooted endpoint deficit is approximately `3.82e31`.

The next theorem must exploit factorial-specific internal span or average gaps.

## Finite divisor-gap diagnostic

Result label: **computational evidence**.

Across the 31 blocked layers for `51<=n<=56`,

\[
\max g_t/D_t
=
\frac{6963896442939750}{6290170063344679}
<1.108.
\]

The maximum occurs at `n=51`, layer `4`. This does not imply an internal average-gap theorem.

## Evidence boundary

None of these runs proves uniform internal-span amplification, a uniform utilization lower bound, asymptotic quotient-window occupancy, the final downward endpoint window, target-local collision bounds, weighted Fourier positivity, the factorial half-range theorem for all sufficiently large `n`, or Erdős Problem 18.
