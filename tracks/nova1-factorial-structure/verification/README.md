# Nova 1 Structural Verification

## Result-label rule

Every verification artifact is classified as one of:

- **finite certificate**;
- **computational evidence**;
- **disproved route** when a verifier or finite candidate is rejected.

Verification does not promote an open asymptotic statement to a proved theorem.

## Baseline checks

```text
python tracks/nova1-factorial-structure/verification/structural_sanity.py
python tracks/nova1-factorial-structure/verification/marker_three_sanity.py
python tracks/nova1-factorial-structure/verification/endpoint_support_sanity.py
python tracks/nova1-factorial-structure/verification/block_collision_sanity.py
```

These scripts use deterministic inputs and exact integer arithmetic.

## Historical complete-core verifiers

### Materialized verifier

`marker_three_full_core_u128.cpp` materializes every truncated odd core and is restricted to the small finite range used by `N1-FIN-005`.

### Unique-parent streaming verifier

`marker_three_streaming_prefix_u128.cpp` independently reconstructs the unique-parent divisor stream used for `N1-FIN-006` at `n=51`.

### Retired unguarded MITM verifier

`marker_three_mitm_prefix_u128.cpp` is intentionally fail closed.

Result label: **disproved route**.

The former implementation generated unrestricted half divisors and multiplied unsigned 128-bit values before applying the endpoint cutoff. At `n=57`, masks `6` and `424` produced different connected-prefix counts. A partition-independent exact divisor stream cannot do this.

Do not use this source for a certificate.

## Authoritative overflow-safe checkpointed verifier

Source:

`marker_three_mitm_checkpoint_u128.cpp`

Build:

```text
g++ -O3 -std=c++20 \
  tracks/nova1-factorial-structure/verification/marker_three_mitm_checkpoint_u128.cpp \
  -o marker_three_mitm_checkpoint_u128
```

Usage:

```text
./marker_three_mitm_checkpoint_u128 n partition_mask
./marker_three_mitm_checkpoint_u128 n partition_mask chunk_divisors
```

When `chunk_divisors` is present, the process emits an exact resource checkpoint and exits with status `3` after at least that many newly consumed divisors. Repeating the same command resumes from the saved frontier.

The default cache and checkpoint directory is `/tmp`. To isolate state:

```text
export NOVA_MITM_STATE_DIR=/path/to/exact-state-directory
```

The verifier performs:

1. exact rational certification of `r_n` and `M_n`;
2. exact factorial valuations and integer square roots;
3. endpoint-truncated generation of two half-divisor lists;
4. division-based multiplication guards before every product;
5. duplicate rejection and exact half-list ordering checks;
6. unique product row merge in global increasing order;
7. exact connected-prefix thresholds, counts, and blocking gaps;
8. exact effective endpoint, margin, and term-bound calculations;
9. exact serialization of the carrier and heap frontier;
10. deterministic continuation from the serialized frontier;
11. fail-closed cache, checkpoint, mask, integer, and ordering checks.

Proof:

`../proofs/OVERFLOW_SAFE_CHECKPOINTED_MITM_STREAM.md`.

## Why endpoint truncation is exact

All half divisors are positive. If a half divisor exceeds `Y_n`, multiplying it by any positive divisor cannot produce a required product at or below `Y_n`.

Therefore replacing both half lists by their intersections with `[1,Y_n]` preserves exactly every merged product relevant to the carrier. The source checks multiplication using division:

```text
current <= Y_n / prime
row_factor <= Y_n / column_factor
```

No wrapped unsigned-128 value can enter the stream.

## Partition planner

Source:

`plan_mitm_partition.py`

Usage:

```text
python tracks/nova1-factorial-structure/verification/plan_mitm_partition.py \
  n --max-columns 5000000 --limit 10
```

The planner enumerates prime-coordinate masks and ranks exact partitions by active row count under an explicit full half-list column bound. The authoritative verifier can truncate the actual stored columns below this full count.

## Overflow-safe regression through n=56

Report:

`OVERFLOW_SAFE_REGRESSION_N52_N56.md`

Overflow-safe replays reproduce every accepted mathematical field at:

| `n` | safe mask | emitted | layers | term bound |
|---:|---:|---:|---:|---:|
| 52 | 511 | 128,277,372 | 6 | 22 |
| 53 | 511 | 255,794,579 | 6 | 22 |
| 54 | 292 | 287,853,491 | 6 | 22 |
| 55 | 808 | 369,103,338 | 6 | 23 |
| 56 | 98 | 411,604,587 | 7 | 24 |

This preserves all earlier finite mathematical conclusions while replacing their authoritative replay method.

## N1-FIN-012 at n=57

Result label: **finite certificate**.

Exact parameters:

- `r_57=17`;
- `M_57=262`;
- `v_2(57!)=53`;
- total odd-core divisor count: `696,729,600`.

Primary safe replay:

- mask `6`;
- truncated split `140 x 4,974,362`.

Alternate safe replay:

- mask `424`;
- truncated split `144 x 4,807,084`.

Both emit `565,913,305` divisors through certificate completion and agree on every mathematical field.

Connected-prefix counts:

```text
93,284
1,968,508
21,512,180
115,705,564
322,620,612
543,303,166
565,913,305
```

Six layers are insufficient and seven layers suffice. The exact term bound is `24`.

Artifacts:

- `FULL_CORE_N57_REPORT.md`;
- `full_core_n57_safe_mask6.txt`;
- `full_core_n57_safe_mask424.txt`;
- `factorial_span_layers_n57.csv`;
- `effective_carrier_n51_n57.csv`;
- `parity_span_effective_n51_n57.csv`;
- `blocking_gap_ratios_n51_n57.csv`;
- `test_mitm_n57_overflow_safe.py`.

Reproduction:

```text
export NOVA_MITM_STATE_DIR=/tmp/nova57-mask6
./marker_three_mitm_checkpoint_u128 57 6 100000000
# Repeat until the finite certificate is printed.

export NOVA_MITM_STATE_DIR=/tmp/nova57-mask424
./marker_three_mitm_checkpoint_u128 57 424 100000000
# Repeat until the finite certificate is printed.

python tracks/nova1-factorial-structure/verification/test_mitm_n57_overflow_safe.py
```

Expected test result:

```text
PASS safe dual-partition n=57
PASS seven-layer necessity and sufficiency n=57
PASS 1.108 candidate counterexample
PASS overflow guards and checkpoint source audit
PASS all n=57 overflow-safe carrier checks
```

## Finite effective diagnostics

At `n=57`,

\[
\widetilde\Gamma_{57}=604.565529127372549\ldots,
\]

\[
\mathcal B_{57}=0.00167399672600756826\ldots,
\]

\[
\Delta_{57}=1.0120407164162547937\ldots.
\]

The parity-only endpoint product misses by approximately `2.82e32`. The factorial-span amplification root is approximately `43,743.7573`, and the geometric mean of `eta_t=U_t/(K_tD_t)` is approximately `0.00165403239909`.

Result label: **computational evidence**.

## Blocking-gap counterexample

Result label: **disproved route**.

At `n=57`, layer `3`,

\[
D_3=2{,}911{,}465{,}312{,}076,
\qquad
g_3=3{,}399{,}069{,}458{,}070,
\]

so

\[
g_3/D_3=1.1674772300983786\ldots>1.108.
\]

The finite candidate constant `1.108` is false.

## Exact finite boundary

Combining Nova 2 `N2-FIN-202` with Nova 1 certificates gives

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
\qquad(12\le n\le57).
\]

These results are finite only. The smallest unaudited parameter is `n=58`.

## Evidence boundary

None of these runs proves uniform connected-prefix growth, a uniform packing-utilization or factorial-span lower bound, asymptotic quotient occupancy, the final endpoint window, target-local collision control, the weighted Fourier theorem, the factorial half-range theorem for all sufficiently large `n`, or Erdos Problem 18.
