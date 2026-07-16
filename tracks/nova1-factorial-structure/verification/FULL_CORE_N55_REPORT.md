# Full-Core Marker-Three Certificate at n=55

## Result

`N1-FIN-010`, **finite certificate**.

The factorial half-range theorem remains open. This report certifies one additional finite parameter only.

## Exact parameters

For `n=55`,

\[
r_{55}=17,
\qquad
M_{55}=257,
\qquad
v_2(55!)=50.
\]

Also,

\[
Y_{55}=1{,}187{,}733{,}759{,}619{,}473{,}153{,}677{,}783{,}755{,}951{,}573{,}821,
\]

and

\[
W_{55}=43{,}689.
\]

The reserved odd core has exactly

\[
452{,}874{,}240
\]

divisors.

## Runtime-aware partitions

Two different prime-coordinate partitions were used.

### Primary replay

- partition mask: `9`;
- product split: `156 x 2,903,040`;
- maximum heap: `156`;
- wall time: `20.68` seconds;
- peak resident memory: `52,340 KiB`;
- exit status: success.

### Alternate replay

- partition mask: `808`;
- product split: `96 x 4,717,440`;
- maximum heap: `96`;
- wall time: `20.40` seconds;
- peak resident memory: `81,144 KiB`;
- exit status: success.

After excluding partition and environment metadata, both runs agree on every exact mathematical field.

## Connected-prefix certificate

The stream emits

\[
369{,}103{,}338
\]

divisors through certificate completion.

The six exact connected-prefix cardinalities are

\[
K_1=90{,}622,
\]

\[
K_2=1{,}867{,}655,
\]

\[
K_3=18{,}700{,}076,
\]

\[
K_4=92{,}180{,}941,
\]

\[
K_5=236{,}519{,}444,
\]

\[
K_6=369{,}103{,}338.
\]

The carrier endpoint is

\[
1{,}187{,}735{,}831{,}419{,}490{,}293{,}014{,}548{,}291{,}571{,}638{,}039.
\]

After correction, the construction occupies through

\[
1{,}187{,}735{,}831{,}419{,}490{,}293{,}014{,}548{,}291{,}571{,}681{,}728.
\]

The exact margin above `Y_55` is

\[
2{,}071{,}800{,}017{,}139{,}336{,}764{,}535{,}620{,}107{,}907.
\]

Therefore

\[
H_{55!}(\lfloor\sqrt{55!}\rfloor+1)\le23.
\]

The bound is `23`, rather than `22`, because `r_55=17` while six carrier layers are used.

Combining the previous certificates gives the sharper two-tier finite statement

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le22
\qquad(12\le n\le54),
\]

and

\[
H_{55!}(\lfloor\sqrt{55!}\rfloor+1)\le23.
\]

Consequently,

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le23
\qquad(12\le n\le55).
\]

All three statements are finite only.

## Effective carrier factorization

Nova 1 independently reconstructed Nova 2 theorem `N2-ADD-122` as `N1-STR-025` from exact source

`nova/additive-occupancy@2ab09dd980f7116b82530368e3d98bb53240bf0c`.

For the exact count factor, utilization factor, and endpoint factor,

\[
\widetilde\Gamma_{55}=98.919733584849\ldots,
\]

\[
\mathcal B_{55}=0.010109209300122\ldots,
\]

and

\[
\Delta_{55}=1.000000290721510\ldots.
\]

They satisfy the exact identity

\[
\Delta_{55}=\widetilde\Gamma_{55}\mathcal B_{55}.
\]

The count surplus is large, but almost all of it is consumed by packing-utilization loss. This is finite diagnostic evidence, not an asymptotic conclusion.

## Count and utilization diagnostics through n=55

| `n` | count surplus | utilization root | endpoint surplus |
|---:|---:|---:|---:|
| 51 | 120.322026488584 | 0.008311064676932 | 1.000004144206103 |
| 52 | 97.645052132052 | 0.010241184816549 | 1.000001025305911 |
| 53 | 124.609364763243 | 0.008025094814707 | 1.000001967025492 |
| 54 | 92.273264366777 | 0.010837378971591 | 1.000000334888580 |
| 55 | 98.919733584849 | 0.010109209300122 | 1.000000290721510 |

No monotonicity is asserted for any column.

## First-blocking-gap audit

For each blocked layer, let `g_t` be the first blocking gap and `D_t` the exact threshold.

At `n=55`, the largest ratio is at layer 5:

\[
\frac{144777909135068819543934}{135975582125916386901983}
=1.0647346153\ldots.
\]

Across every blocked layer for `51<=n<=55`, the maximum remains the `n=51`, layer 4 value

\[
\frac{20891689328819250}{18870510190034037}
=1.1071078162\ldots<1.108.
\]

This is `N1-CMP-008`, **computational evidence**. It is not a uniform divisor-gap theorem.

## Exact products

The connected-prefix count product is

\[
25{,}470{,}336{,}596{,}566{,}520{,}205{,}304{,}888{,}296{,}679{,}181{,}030{,}522{,}160.
\]

The exact finite requirement ceiling is

\[
27{,}185{,}483{,}168{,}218{,}657{,}671{,}727{,}712{,}427{,}365.
\]

The integer floor ratio is

\[
936{,}909{,}468{,}886.
\]

## Replay

```text
g++ -O3 -std=c++20 \
  tracks/nova1-factorial-structure/verification/marker_three_mitm_prefix_u128.cpp \
  -o marker_three_mitm_prefix_u128

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

## Claim boundary

This certificate does not prove uniform connected-prefix growth, a uniform utilization lower bound, the quotient-window theorem, the factorial half-range theorem for all sufficiently large `n`, or Erdős Problem 18.
