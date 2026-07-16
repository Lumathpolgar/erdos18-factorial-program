# Nova 1 Structural Verification

## Result-label rule

Every verification artifact is classified as one of:

- **finite certificate**;
- **computational evidence**.

Verification does not promote an open asymptotic statement to a proved theorem.

## Baseline Python checks

```text
python tracks/nova1-factorial-structure/verification/structural_sanity.py
python tracks/nova1-factorial-structure/verification/marker_three_sanity.py
python tracks/nova1-factorial-structure/verification/endpoint_support_sanity.py
python tracks/nova1-factorial-structure/verification/block_collision_sanity.py
```

These scripts use deterministic inputs and exact integer arithmetic.

### `structural_sanity.py`

Checks finite instances of:

- Legendre valuations and digit-sum identities;
- quotient and dyadic bands;
- correction legality;
- marker distinctness;
- complement pairing;
- high-prime menu counts;
- counting-capacity inequalities.

Result label: **computational evidence**.

### `marker_three_sanity.py`

Checks reduced finite instances of:

- marker-three legality;
- exact 2-adic layer addresses;
- cross-layer distinctness;
- exact main lattice `3Z`;
- correction residues modulo `3`;
- odd-digit one-gap behavior;
- reduced quotient reachability and reconstruction.

Result label: **computational evidence**.

Report: `MARKER_THREE_FINITE_REPORT.md`.

### `endpoint_support_sanity.py`

Checks:

- multiplicative 3-density for `6<=n<=20`;
- endpoint witnesses for `12<=n<=20`;
- total endpoint crossing;
- coarse contraction for `12<=n<=14`.

Result label: **finite certificate**.

Report: `ENDPOINT_SUPPORT_FINITE_REPORT.md`.

### `block_collision_sanity.py`

Checks:

- factorial block legality;
- one-block carrier inequalities;
- carry-collision identities;
- scale separation used by `N1-DIS-006`.

Result label: **finite certificate**.

Report: `BLOCK_COLLISION_FINITE_REPORT.md`.

## Materialized complete-core verifier

Source:

`marker_three_full_core_u128.cpp`

Build:

```text
g++ -O3 -std=c++17 \
  tracks/nova1-factorial-structure/verification/marker_three_full_core_u128.cpp \
  -o marker_three_full_core_u128
```

This verifier materializes every truncated odd core and is deliberately restricted to `12<=n<=50`.

### N1-FIN-005

Result label: **finite certificate**.

Every `46<=n<=50` reaches the quotient endpoint in six layers.

Artifacts:

- `FULL_CORE_N46_N50_REPORT.md`;
- `full_core_n46_n50_summary.csv`;
- `full_core_n46_n50_layers.csv`.

## Unique-parent streaming verifier

Source:

`marker_three_streaming_prefix_u128.cpp`

This reconstructs Nova 2 `N2-ADD-121` with a priority-queue divisor stream and record-gap left counts.

### N1-FIN-006

Result label: **finite certificate**.

At `n=51`:

- total odd-core divisors: `124,001,280`;
- emitted through `Y_51`: `108,924,509` in the full stream and `101,350,643` through the final carrier cutoff;
- maximum unique-parent frontier: `13,602,843`;
- six layers;
- term bound: `22`.

Artifacts:

- `FULL_CORE_N51_REPORT.md`;
- `full_core_n51.txt`.

## Meet-in-the-middle connected-prefix verifier

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
./marker_three_mitm_prefix_u128 n
./marker_three_mitm_prefix_u128 n partition_mask
```

The optional partition mask enables adversarial replay with a different split of the prime-power coordinates.

The verifier performs:

1. exact rational certification of `r_n` and `M_n`;
2. exact factorial valuations and integer square roots;
3. exact generation and sorting of two half-divisor lists;
4. duplicate rejection within each half;
5. count verification `|A||B|=tau(D_n)`;
6. exact minimum-heap row merge;
7. strict global-order and duplicate rejection;
8. exact connected-prefix thresholds and counts;
9. exact endpoint, margin, count-product, and requirement calculations;
10. fail-closed unsigned 128-bit endpoint limits.

Proof:

`../proofs/MEET_IN_THE_MIDDLE_CONNECTED_PREFIX_STREAM.md`.

### Partition planner

Source:

`plan_mitm_partition.py`

Usage:

```text
python tracks/nova1-factorial-structure/verification/plan_mitm_partition.py \
  n --max-columns 3000000 --limit 10
```

The planner enumerates exact prime-coordinate masks, verifies the total divisor count, and ranks partitions by merge-row count subject to an explicit half-list column bound.

Result label for each emitted plan: **finite certificate**.

### N1-FIN-007

Result label: **finite certificate**.

At `n=52`, six layers reach the endpoint with term bound `22`.

Artifacts:

- `FULL_CORE_N52_REPORT.md`;
- `full_core_n52_mitm.txt`;
- `full_core_n51_mitm_overlap.txt`;
- `test_mitm_overlap.py`.

### N1-FIN-008

Result label: **finite certificate**.

At `n=53`:

- total odd-core divisors: `310,003,200`;
- split: `17,550 x 17,664`;
- emitted through the certificate: `255,794,579`;
- maximum heap: `17,550`;
- connected-prefix sizes: `63,547`, `1,308,251`, `14,186,800`, `70,586,242`, `175,389,561`, `255,794,579`;
- six layers;
- term bound: `22`;
- final margin: `257,219,713,671,656,581,137,253,687,630`.

Partition masks `350` and `414` produce identical carrier outputs after excluding partition and resource metadata.

Artifacts:

- `FULL_CORE_N53_REPORT.md`;
- `full_core_n53_mitm.txt`;
- `full_core_n53_mitm_mask414.txt`;
- `connected_prefix_normalized_n51_n53.csv`;
- `test_mitm_n53_normalized.py`.

### N1-FIN-009

Result label: **finite certificate**.

At `n=54`:

- total odd-core divisors: `350,438,400`;
- primary mask `255`: `128 x 2,737,800`;
- alternate mask `223`: `512 x 684,450`;
- emitted through the certificate: `287,853,491`;
- connected-prefix sizes: `63,547`, `1,308,259`, `14,197,074`, `71,967,365`, `185,071,301`, `287,853,491`;
- six layers;
- term bound: `22`;
- final margin: `321,802,717,811,173,461,556,306,445,531`.

The two explicit masks produce identical mathematical output after excluding partition and environment fields.

Primary mask `255`:

- wall time: `15.31` seconds;
- peak memory: `49,032 KiB`.

Alternate mask `223`:

- wall time: `18.57` seconds;
- peak memory: `18,056 KiB`.

The balanced `18,720 x 18,720` partition did not complete inside the six-minute execution boundary after emitting `230,000,000` divisors. This is a resource boundary for that partition, not a mathematical failure.

Artifacts:

- `FULL_CORE_N54_REPORT.md`;
- `full_core_n54_mitm_mask255.txt`;
- `full_core_n54_mitm_mask223.txt`;
- `connected_prefix_normalized_n51_n54.csv`;
- `plan_mitm_partition.py`;
- `test_mitm_n54_partition.py`.

### N1-FIN-010

Result label: **finite certificate**.

At `n=55`:

- `r_55=17`;
- `M_55=257`;
- total odd-core divisors: `452,874,240`;
- primary mask `9`: `156 x 2,903,040`;
- alternate mask `808`: `96 x 4,717,440`;
- emitted through the certificate: `369,103,338`;
- connected-prefix sizes: `90,622`, `1,867,655`, `18,700,076`, `92,180,941`, `236,519,444`, `369,103,338`;
- six layers;
- term bound: `23`;
- final margin: `2,071,800,017,139,336,764,535,620,107,907`.

The term bound changes from `22` to `23` because `r_55=17`.

Primary mask `9`:

- wall time: `20.68` seconds;
- peak memory: `52,340 KiB`.

Alternate mask `808`:

- wall time: `20.40` seconds;
- peak memory: `81,144 KiB`.

The two masks produce identical mathematical output after excluding partition and environment fields.

Artifacts:

- `FULL_CORE_N55_REPORT.md`;
- `full_core_n55_mitm_mask9.txt`;
- `full_core_n55_mitm_mask808.txt`;
- `effective_carrier_n51_n55.csv`;
- `blocking_gap_ratios_n51_n55.csv`;
- `test_mitm_n55_effective.py`.

Reproduction:

```text
./marker_three_mitm_prefix_u128 55 9
./marker_three_mitm_prefix_u128 55 808
python tracks/nova1-factorial-structure/verification/test_mitm_n55_effective.py
```

Expected result:

```text
PASS exact n=55
PASS alternate partition n=55
PASS effective carrier factorization
PASS term-bound transition from 22 to 23
PASS finite first-blocking-gap ratio below 1.108 through n=55
PASS all n=55 effective carrier checks
```

## Exact finite boundary

Combining Nova 2 `N2-FIN-202` with Nova 1 certificates gives

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
\le22
\qquad(12\le n\le54),
\]

and

\[
H_{55!}(\lfloor\sqrt{55!}\rfloor+1)
\le23.
\]

Consequently,

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
\le23
\qquad(12\le n\le55).
\]

These statements are finite only. The smallest unaudited parameter is `n=56`.

## Count-surplus theorem

`N1-STR-024` is a **proved theorem**.

Define

\[
P_n=\prod_{t=1}^{L}(1+K_t),
\qquad
Q_n=\left\lceil\frac{Y_n+1}{W_n+1}\right\rceil,
\]

\[
\Gamma_n=(P_n/Q_n)^{1/L}.
\]

Then the exact connected-prefix count gate is met if and only if

\[
\Gamma_n\ge1.
\]

This is a necessary count gate, not a sufficient endpoint theorem.

## Effective carrier theorem

`N1-STR-025` is a **proved theorem**, independently reconstructed from Nova 2 `N2-ADD-122` at exact commit

`2ab09dd980f7116b82530368e3d98bb53240bf0c`.

For

\[
a_t=\frac{s_tU_t}{F_{t-1}},
\qquad
b_t=\frac{1+a_t}{1+K_t},
\]

one has

\[
\frac{F_L}{W_n+1}
=
P_n\prod_{t=1}^{L}b_t.
\]

With

\[
\widetilde\Gamma_n=(P_n/R_n)^{1/L},
\qquad
\mathcal B_n=\left(\prod_tb_t\right)^{1/L},
\qquad
\Delta_n=\left(\frac{F_L}{Y_n+1}\right)^{1/L},
\]

\[
\Delta_n=\widetilde\Gamma_n\mathcal B_n.
\]

Endpoint success is equivalent to `Delta_n>=1`.

Finite diagnostic values are:

| `n` | count surplus | utilization root | endpoint surplus |
|---:|---:|---:|---:|
| 51 | 120.322026488584 | 0.008311064676932 | 1.000004144206103 |
| 52 | 97.645052132052 | 0.010241184816549 | 1.000001025305911 |
| 53 | 124.609364763243 | 0.008025094814707 | 1.000001967025492 |
| 54 | 92.273264366777 | 0.010837378971591 | 1.000000334888580 |
| 55 | 98.919733584849 | 0.010109209300122 | 1.000000290721510 |

The count surplus is mostly consumed by utilization loss. No uniform bound follows.

## Finite divisor-gap diagnostic

Result label: **computational evidence**.

Across the twenty-five blocked layers for `51<=n<=55`,

\[
\max g_t/D_t
=
\frac{20891689328819250}{18870510190034037}
<1.108.
\]

The exact maximum occurs at `n=51`, layer `4`. No asymptotic divisor-gap or utilization theorem is claimed.

## Evidence boundary

None of these runs proves:

- uniform connected-prefix growth;
- a uniform packing-utilization lower bound;
- a uniform divisor record-gap or average-gap bound;
- the asymptotic quotient-window theorem;
- the final downward endpoint window;
- target-local collision upper bounds;
- the weighted bounded-torus Fourier theorem;
- the factorial half-range theorem for all sufficiently large `n`;
- Erdős Problem 18.
