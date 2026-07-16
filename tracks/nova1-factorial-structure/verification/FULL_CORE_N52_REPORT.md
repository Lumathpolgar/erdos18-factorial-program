# Exact Meet-in-the-Middle Full-Core Audit at n=52

## Result IDs

- `N1-STR-023`: **proved theorem**
- `N1-FIN-007`: **finite certificate**

## Frozen source

- branch: `nova/factorial-structure`
- previous checkpoint head: `d15d49def013a4b2ed4e67f1d5d3d33ac904dbca`
- construction: `N1-CON-003`
- carrier requirement: `N1-OBS-003`
- previous finite result: `N1-FIN-006`

The factorial half-range theorem remains open. This report records one exact finite certificate and one exact algorithmic theorem.

## Resource obstruction from the unique-parent stream

The unique-parent priority-queue verifier was first run at `n=52`. After five minutes it had emitted `40,000,000` cores and had an active frontier of `14,796,355` nodes. The run ended at the execution limit before producing a certificate.

This was classified as `unknown due to resource limits`, not as mathematical failure.

## Meet-in-the-middle replacement

`N1-STR-023` partitions the odd prime-power coordinates into two disjoint families. At `n=52`, the exact divisor count factors as

\[
155{,}001{,}600=12{,}420\cdot12{,}480.
\]

The verifier builds the two exact half-divisor lists and merges the `12,420` sorted product rows with a minimum heap. Unique factorization across disjoint prime supports prevents duplicate products.

Exact verifier:

`marker_three_mitm_prefix_u128.cpp`

Implementation commit:

`72bcf1d6142f06be3fc704cc5313d17f5281884b`

## Independent overlap at n=51

The new verifier was first replayed at `n=51`. It exactly reproduced the frozen `N1-FIN-006` values for:

- `r_51`, `M_51`, and `v_2(51!)`;
- `Y_51` and `W_51`;
- the total odd-core divisor count;
- all six gap thresholds;
- all six connected maxima;
- all six connected-prefix cardinalities;
- all five blocking gaps;
- every carrier endpoint;
- the final endpoint margin;
- the connected-prefix product;
- the term bound `22`.

The overlap run used a `11,040 x 11,232` split, completed in `9.75` seconds, and used `7,540 KiB` peak resident memory.

Machine record:

`full_core_n51_mitm_overlap.txt`

## Exact n=52 parameters

\[
r_{52}=16,
\qquad
M_{52}=250,
\qquad
v_2(52!)=49.
\]

The quotient endpoint and correction width are

\[
Y_{52}=2{,}993{,}663{,}218{,}105{,}571{,}862{,}989{,}260{,}568{,}857{,}358,
\]

\[
W_{52}=21{,}844.
\]

The complete reserved odd core has

\[
155{,}001{,}600
\]

divisors.

## N1-FIN-007

The exact meet-in-the-middle stream emitted `128,277,372` divisors before the sixth-layer certificate completed. The maximum heap contained `12,420` nodes.

The exact connected-prefix data are:

| layer | threshold | connected maximum | connected count | carrier endpoint |
|---:|---:|---:|---:|---:|
| 1 | 21,845 | 63,955,203 | 47,281 | 63,955,203 |
| 2 | 31,988,524 | 857,162,109,375 | 847,667 | 1,714,388,173,953 |
| 3 | 428,597,048,949 | 50,934,187,150,221,375 | 7,770,345 | 203,738,462,989,059,453 |
| 4 | 25,467,307,873,635,162 | 6,716,153,885,666,392,715,625 | 34,911,862 | 53,729,434,823,794,130,784,453 |
| 5 | 3,358,089,676,487,133,175,393 | 1,220,703,263,560,386,037,072,265,625 | 85,166,200 | 19,531,305,946,401,000,387,287,034,453 |
| 6 | 610,353,310,825,031,262,102,720,509 | 93,551,940,730,324,679,221,030,295,008,125 | 128,277,372 | 2,993,681,634,676,336,136,073,356,727,294,453 |

No blocking gap occurs before the sixth-layer cutoff. Therefore

\[
E_6+W_{52}
=
2{,}993{,}681{,}634{,}676{,}336{,}136{,}073{,}356{,}727{,}316{,}297.
\]

This exceeds `Y_52` by

\[
18{,}416{,}570{,}764{,}273{,}084{,}096{,}158{,}458{,}939.
\]

Hence

\[
H_{52!}(\lfloor\sqrt{52!}\rfloor+1)
\le6+r_{52}=22.
\]

This is an exact finite theorem.

## Combined finite range

Combining `N2-FIN-202`, `N1-FIN-005`, `N1-FIN-006`, and `N1-FIN-007` gives

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
\le22
\qquad(12\le n\le52).
\]

No asymptotic conclusion is asserted.

## Connected-prefix entropy measurement

The exact product is

\[
\prod_{t=1}^{6}(1+K_t)
=
118{,}782{,}467{,}311{,}926{,}842{,}592{,}580{,}351{,}058{,}316{,}666{,}013{,}104.
\]

The exact finite `N1-OBS-003` requirement ceiling is

\[
137{,}041{,}117{,}789{,}222{,}790{,}706{,}764{,}045{,}267.
\]

The product exceeds the requirement by an integer factor of at least

\[
866{,}765{,}166{,}748.
\]

The geometric mean of the six factors is approximately

\[
7{,}011{,}195.18.
\]

The corresponding ratio at `n=51` was greater than `3,034,386,005,338`. Therefore the finite margin is not increasing from `n=51` to `n=52`. This does not indicate failure because the margin remains enormous. It does reject any inference based only on monotone growth across these two points.

## Reproducibility

```text
g++ -O3 -std=c++20 \
  tracks/nova1-factorial-structure/verification/marker_three_mitm_prefix_u128.cpp \
  -o marker_three_mitm_prefix_u128

./marker_three_mitm_prefix_u128 51
./marker_three_mitm_prefix_u128 52
python tracks/nova1-factorial-structure/verification/test_mitm_overlap.py
```

Recorded test result:

```text
PASS test_n51_overlap
PASS test_n52_certificate
PASS all 2 meet-in-the-middle checks
```

At `n=52`:

- elapsed wall time: `12.56` seconds;
- user CPU time: `11.74` seconds;
- maximum resident memory: `7,084 KiB`;
- exit status: `0`.

## Machine records

- `full_core_n51_mitm_overlap.txt`
- `full_core_n52_mitm.txt`
- `test_mitm_overlap.py`

## Claim boundary

This certificate does not prove uniform connected-prefix growth, the asymptotic quotient-window theorem, the final endpoint window for all sufficiently large `n`, Track B, or Erdős Problem 18.
