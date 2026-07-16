# Nova 1 Structural Verification

## Python checks

```text
python tracks/nova1-factorial-structure/verification/structural_sanity.py
python tracks/nova1-factorial-structure/verification/marker_three_sanity.py
python tracks/nova1-factorial-structure/verification/endpoint_support_sanity.py
python tracks/nova1-factorial-structure/verification/block_collision_sanity.py
python tracks/nova1-factorial-structure/verification/test_mitm_overlap.py
```

These scripts use deterministic inputs and exact integer arithmetic.

### Baseline structural checks

`structural_sanity.py` verifies finite instances of Legendre valuations, quotient bands, correction legality, distinctness, complement pairing, high-prime menu counts, and the counting-capacity inequality.

### Marker-three reduced checks

`marker_three_sanity.py` verifies legality, exact 2-adic addresses, cross-layer distinctness, exact main lattice `3Z`, palette residues, the odd-digit one-gap lemma, reduced quotient reachability, correction, and complete reconstruction on its declared reduced domain.

Result label: **computational evidence**.

Report: `MARKER_THREE_FINITE_REPORT.md`.

### Endpoint-support checks

`endpoint_support_sanity.py` verifies multiplicative 3-density for `6<=n<=20`, endpoint witnesses for `12<=n<=20`, total endpoint crossing, and coarse contraction for `12<=n<=14`.

Result label: **finite certificate**.

Report: `ENDPOINT_SUPPORT_FINITE_REPORT.md`.

### Block and collision checks

`block_collision_sanity.py` verifies factorial block legality, one-block carrier inequalities, carry-collision identities, and scale separation.

Result label: **finite certificate**.

Report: `BLOCK_COLLISION_FINITE_REPORT.md`.

### Meet-in-the-middle overlap checks

`test_mitm_overlap.py` verifies:

1. every frozen `n=51` carrier field shared by the unique-parent and meet-in-the-middle implementations;
2. the exact `n=52` split, prefix counts, endpoint identity, entropy ratio, and term bound.

Recorded result:

```text
PASS test_n51_overlap
PASS test_n52_certificate
PASS all 2 meet-in-the-middle checks
```

## Materialized complete-core verifier

Source:

`marker_three_full_core_u128.cpp`

Build:

```text
g++ -O3 -std=c++17 \
  tracks/nova1-factorial-structure/verification/marker_three_full_core_u128.cpp \
  -o marker_three_full_core_u128
```

This verifier materializes every truncated core and is deliberately restricted to `12<=n<=50`.

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

Build:

```text
g++ -O3 -std=c++20 \
  tracks/nova1-factorial-structure/verification/marker_three_streaming_prefix_u128.cpp \
  -o marker_three_streaming_prefix_u128
```

Run:

```text
./marker_three_streaming_prefix_u128 51 30000000
```

The verifier independently reconstructs Nova 2 theorem `N2-ADD-121` using a unique-parent bounded-exponent divisor stream, exact priority ordering, rational logarithmic certification, record-gap compression, stored left counts, and fail-closed frontier limits.

Proof:

`../proofs/STREAMING_CONNECTED_PREFIX_CERTIFIER.md`.

### N1-FIN-006

At `n=51`:

- total odd-core divisors: `124,001,280`;
- emitted cores through `Y_51`: `108,924,509`;
- maximum frontier: `13,602,843`;
- six prefix sizes: `46,990`, `824,638`, `6,936,398`, `30,013,231`, `70,529,067`, `101,350,643`;
- term bound: `22`.

Artifacts:

- `FULL_CORE_N51_REPORT.md`;
- `full_core_n51.txt`.

At `n=52`, a five-minute run emitted `40,000,000` cores but did not complete. This is a resource-limit record, not a counterexample.

## Meet-in-the-middle connected-prefix verifier

Source:

`marker_three_mitm_prefix_u128.cpp`

Build:

```text
g++ -O3 -std=c++20 \
  tracks/nova1-factorial-structure/verification/marker_three_mitm_prefix_u128.cpp \
  -o marker_three_mitm_prefix_u128
```

Run:

```text
./marker_three_mitm_prefix_u128 51
./marker_three_mitm_prefix_u128 52
```

`N1-STR-023` partitions the odd prime-power coordinates into two balanced families. The exact half-divisor lists are merged as sorted product rows. Unique factorization across disjoint prime supports guarantees complete duplicate-free enumeration.

Proof:

`../proofs/MEET_IN_THE_MIDDLE_CONNECTED_PREFIX_STREAM.md`.

### n=51 overlap

The meet-in-the-middle verifier reproduces every frozen threshold, connected maximum, prefix count, blocking gap, endpoint, margin, product, and term bound from `N1-FIN-006`.

- split: `11,040 x 11,232`;
- runtime: `9.75` seconds;
- peak memory: `7,540 KiB`.

Machine record:

`full_core_n51_mitm_overlap.txt`.

### N1-FIN-007

At `n=52`:

- total odd-core divisors: `155,001,600`;
- balanced split: `12,420 x 12,480`;
- emitted before certificate completion: `128,277,372`;
- maximum merge heap: `12,420`;
- six prefix sizes: `47,281`, `847,667`, `7,770,345`, `34,911,862`, `85,166,200`, `128,277,372`;
- six main layers reach `Y_52`;
- term bound: `22`;
- runtime: `12.56` seconds;
- peak memory: `7,084 KiB`.

Artifacts:

- `FULL_CORE_N52_REPORT.md`;
- `full_core_n52_mitm.txt`.

Combining imported Nova 2 certificate `N2-FIN-202`, `N1-FIN-005`, `N1-FIN-006`, and `N1-FIN-007` gives

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
\le22
\qquad(12\le n\le52).
\]

This is finite only. The next unaudited parameter is `n=53`.

## Connected-prefix entropy theorem

`N1-OBS-003` is a **proved theorem**.

If `K_t` is the positive connected-prefix cardinality at layer `t`, carrier success requires

\[
\prod_t(1+K_t)
\ge
\frac{Y_n+1}{W_n+1}.
\]

For `n>=120368`, the geometric mean of the executed `1+K_t` must be at least

\[
\exp\left(\frac{n}{85\log n}\right).
\]

Proof:

`../proofs/CONNECTED_PREFIX_ENTROPY_REQUIREMENT.md`.

The exact finite product ratio decreases from more than `3,034,386,005,338` at `n=51` to `866,765,166,748` at `n=52`. The ratio remains enormous, but finite monotonicity is not available.

## Evidence boundary

None of the verification runs proves:

- uniform connected-prefix growth;
- the asymptotic quotient-window theorem;
- the final downward endpoint window;
- target-local collision upper bounds;
- the weighted bounded-torus Fourier theorem;
- the factorial half-range theorem for all sufficiently large `n`;
- Erdős Problem 18.
