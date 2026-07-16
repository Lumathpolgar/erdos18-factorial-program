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
9. exact endpoint, margin, entropy-product, and requirement calculations;
10. fail-closed unsigned 128-bit endpoint limits.

Proof:

`../proofs/MEET_IN_THE_MIDDLE_CONNECTED_PREFIX_STREAM.md`.

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

Reproduction:

```text
./marker_three_mitm_prefix_u128 53
./marker_three_mitm_prefix_u128 53 414
python tracks/nova1-factorial-structure/verification/test_mitm_n53_normalized.py
```

Expected result:

```text
PASS exact n=51
PASS exact n=52
PASS exact n=53
PASS alternate partition n=53
PASS finite non-monotonicity diagnostic
PASS all normalized meet-in-the-middle checks
```

## Exact finite boundary

Combining Nova 2 `N2-FIN-202` with Nova 1 certificates gives

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
\le22
\qquad(12\le n\le53).
\]

This is finite only. The smallest unaudited parameter is `n=54`.

## Normalized entropy theorem

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

Then the exact connected-prefix entropy gate is met if and only if

\[
\Gamma_n\ge1.
\]

Finite diagnostic values for `n=51,52,53` are all above one but non-monotone. They do not prove a uniform bound.

## Evidence boundary

None of these runs proves:

- uniform connected-prefix growth;
- the asymptotic quotient-window theorem;
- the final downward endpoint window;
- target-local collision upper bounds;
- the weighted bounded-torus Fourier theorem;
- the factorial half-range theorem for all sufficiently large `n`;
- Erdős Problem 18.
