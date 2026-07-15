# Nova 1 Structural Verification

## Python checks

```text
python tracks/nova1-factorial-structure/verification/structural_sanity.py
python tracks/nova1-factorial-structure/verification/marker_three_sanity.py
python tracks/nova1-factorial-structure/verification/endpoint_support_sanity.py
python tracks/nova1-factorial-structure/verification/block_collision_sanity.py
```

These scripts use deterministic inputs and exact integer arithmetic.

### Baseline structural checks

`structural_sanity.py` verifies finite instances of:

1. Legendre valuations and the digit-sum identity;
2. quotient-band valuations;
3. binary correction legality;
4. marker distinctness and palette disjointness;
5. complement-pair legality;
6. high-prime menu counts;
7. the downward-window counting inequality.

### Marker-three reduced checks

`marker_three_sanity.py` verifies:

1. marker-three divisor legality;
2. exact 2-adic addresses;
3. cross-layer distinctness;
4. exact main lattice `3Z`;
5. palette residues modulo `3`;
6. the odd-digit one-gap lemma;
7. reduced exact quotient rainbow reachability;
8. quotient-to-main correction;
9. complete reconstruction of every tested half-range target.

Exact tested domain:

```text
7 <= n <= 14
r = 3
M = min(6, v_2(n!) + 1)
```

Result label: **computational evidence**.

Detailed report:

`MARKER_THREE_FINITE_REPORT.md`

### Endpoint-support checks

`endpoint_support_sanity.py` verifies finite instances of:

- multiplicative 3-density for `6<=n<=20`;
- legal first-three-layer endpoint witnesses for `12<=n<=20`;
- total endpoint crossing;
- exhaustive coarse-contraction inequalities for `12<=n<=14`.

Result label: **finite certificate**.

Detailed report:

`ENDPOINT_SUPPORT_FINITE_REPORT.md`

### Block and collision checks

`block_collision_sanity.py` verifies finite instances of:

- factorial arithmetic block legality;
- exact one-block carrier inequalities;
- exponential carry-collision identities;
- asymptotic scale separation used by `N1-DIS-006`.

Result label: **finite certificate**.

Detailed report:

`BLOCK_COLLISION_FINITE_REPORT.md`

## Exact complete-core C++ verifier

Source:

`marker_three_full_core_u128.cpp`

Build:

```text
g++ -O3 -std=c++17 \
  tracks/nova1-factorial-structure/verification/marker_three_full_core_u128.cpp \
  -o marker_three_full_core_u128
```

Example runs:

```text
./marker_three_full_core_u128 --n 46 --max-values 30000000
./marker_three_full_core_u128 --n 47 --max-values 60000000
./marker_three_full_core_u128 --n 48 --max-values 60000000
./marker_three_full_core_u128 --n 49 --max-values 80000000
./marker_three_full_core_u128 --n 50 --max-values 80000000
```

The verifier uses:

- arbitrary-precision integer factorials and square roots;
- exact rational certification of `r_n` and `M_n`;
- exact prime valuations;
- complete generation of every odd core not exceeding `Y_n`;
- sorted duplicate-free core menus;
- exact connected-core thresholds and endpoints;
- a declared fail-closed value cap;
- unsigned 128-bit storage for truncated core values.

The implementation range is deliberately restricted to

```text
12 <= n <= 50
```

because the frozen verifier stores core values in unsigned 128-bit integers. An unsupported endpoint is rejected rather than silently truncated.

### N1-FIN-005

Result label: **finite certificate**.

Every `46<=n<=50` reaches the complete quotient endpoint in six main layers.

Combined with imported Nova 2 certificate `N2-FIN-202` at exact commit

`82603c631a106c3bff4676bdeeb9cc791fc98f3c`,

the complete connected-core carrier is exactly certified for every

```text
12 <= n <= 50
```

This remains finite only.

Detailed report and machine-readable records:

- `FULL_CORE_N46_N50_REPORT.md`;
- `full_core_n46_n50_summary.csv`;
- `full_core_n46_n50_layers.csv`.

## Connected-prefix theorem

`N1-OBS-003` is a **proved theorem**, not a computational result.

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

`../proofs/CONNECTED_PREFIX_ENTROPY_REQUIREMENT.md`

## Evidence boundary

None of the verification runs proves:

- uniform connected-core growth;
- the asymptotic quotient-window theorem;
- the final downward endpoint window;
- target-local collision upper bounds;
- the weighted bounded-torus Fourier theorem;
- the factorial half-range theorem for all sufficiently large `n`;
- Erdős Problem 18.