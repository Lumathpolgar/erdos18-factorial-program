# Full-Core n=52 Checkpoint

## Classification

- `N1-STR-023`: **proved theorem**
- `N1-FIN-007`: **finite certificate**

The factorial half-range theorem remains open.

## Exact source state

- branch: `nova/factorial-structure`
- previous checkpoint head: `d15d49def013a4b2ed4e67f1d5d3d33ac904dbca`
- meet-in-the-middle verifier commit: `72bcf1d6142f06be3fc704cc5313d17f5281884b`
- proof commit: `3e7d8b36ee97a56bac1d7d5618555b7632157947`
- raw n=52 certificate commit: `cd72e2761f2515da5dc88755740833d93ec11e42`
- overlap record commit: `02b388ae72d30e7c45df744051d0bad455852684`
- test commit: `47558878514e8c9d24fdcf13c09d0180fdf53260`
- report commit: `d938c2880283f77c32a39e226165f8034b487aec`

## Closed node

The exact finite boundary is extended from `n=51` to `n=52`.

\[
H_{52!}(\lfloor\sqrt{52!}\rfloor+1)\le22.
\]

Together with prior certificates:

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le22
\qquad(12\le n\le52).
\]

This is finite only.

## New algorithmic theorem

The odd prime-power coordinates can be partitioned into two disjoint families. Their half-divisor lists give unique products `ab`. A heap merge of sorted product rows emits the exact global divisor order.

At `n=52`:

\[
155{,}001{,}600=12{,}420\cdot12{,}480.
\]

The active merge heap contains at most `12,420` nodes. The exact certificate completed in `12.56` seconds with `7,084 KiB` peak resident memory.

The prior unique-parent run reached `40,000,000` emitted cores in five minutes but had not completed. That run was a resource limitation, not a mathematical failure.

## Exact connected prefixes

\[
K_1=47{,}281,
\quad
K_2=847{,}667,
\quad
K_3=7{,}770{,}345,
\]

\[
K_4=34{,}911{,}862,
\quad
K_5=85{,}166{,}200,
\quad
K_6=128{,}277{,}372.
\]

The product exceeds the exact finite `N1-OBS-003` requirement by an integer factor of at least

\[
866{,}765{,}166{,}748.
\]

The corresponding factor at `n=51` was greater than

\[
3{,}034{,}386{,}005{,}338.
\]

Therefore the finite entropy margin is not monotone from `n=51` to `n=52`. No asymptotic inference may rely on monotone margin growth from these data.

## Verification

```text
g++ -O3 -std=c++20 \
  tracks/nova1-factorial-structure/verification/marker_three_mitm_prefix_u128.cpp \
  -o marker_three_mitm_prefix_u128

./marker_three_mitm_prefix_u128 51
./marker_three_mitm_prefix_u128 52
python tracks/nova1-factorial-structure/verification/test_mitm_overlap.py
```

Recorded result:

```text
PASS test_n51_overlap
PASS test_n52_certificate
PASS all 2 meet-in-the-middle checks
```

## Artifacts

- `proofs/MEET_IN_THE_MIDDLE_CONNECTED_PREFIX_STREAM.md`
- `verification/marker_three_mitm_prefix_u128.cpp`
- `verification/full_core_n51_mitm_overlap.txt`
- `verification/full_core_n52_mitm.txt`
- `verification/test_mitm_overlap.py`
- `verification/FULL_CORE_N52_REPORT.md`

## Open boundary

1. prove or disprove uniform connected-prefix growth meeting `N1-OBS-003`;
2. extend the exact finite boundary beginning at `n=53`;
3. explain the scale and variation of the finite entropy ratio without assuming monotonicity;
4. prove target-local collision control for the final-only route;
5. reconstruct Track B.

## Exact next step

Run the meet-in-the-middle connected-prefix verifier at `n=53`, record every `K_t`, and compare the normalized entropy requirement ratio across `n=51,52,53` before proposing any trend theorem.
