# Exact Marker-Three Full-Menu Carrier Audit

## Result ID

- `N2-FIN-202`: finite certificate

## Frozen sources

- repository: `Lumathpolgar/erdos18-factorial-program`
- Nova 1 branch: `nova/factorial-structure`
- Nova 1 commit: `ebb47ba436af554366d0f285119a769f31f9e561`
- construction: `N1-CON-003`
- handoff: `N1-HO-N2-002`
- Nova 2 proof engine: `N2-ADD-119` and `N2-ADD-120`

## Scope

This audit covers every integer

\[
12\le n\le45.
\]

For each `n`, it generates the complete odd-core set

\[
\mathcal U(n)=\{u\ge1:u\text{ odd},\ 3u\mid n!\},
\]

then applies the exact layer cutoff

\[
U_t(n)=\left\{u\in\mathcal U(n):
2^{t-1}u\le Y_n\right\},
\qquad
Y_n=\left\lfloor\frac{\lfloor\sqrt{n!}\rfloor}{3}\right\rfloor.
\]

No reduced odd-core menu, sampling rule, or high-prime-only substitute is used.

The scan begins at `n=12` because this is the first value in the audited range for which the complete binary correction palette is legal:

\[
r_n-1\le v_2(n!).
\]

Only main layers with legal 2-adic address are used. The recursion stops immediately after its certified endpoint reaches `Y_n`.

## Exact method

For every layer `t`, let the previous carrier endpoint be `E_(t-1)` and define

\[
D_t=
\left\lfloor
\frac{E_{t-1}+W_n+1}{2^{t-1}}
\right\rfloor,
\qquad
W_n=
\left\lfloor\frac{2^{r_n}-3}{3}\right\rfloor.
\]

The complete sorted layer menu is scanned from zero. Consecutive cores remain in the connected component exactly while their gap is at most `D_t`. If `u_t^*` is the largest connected core, the endpoint update is

\[
E_t=E_{t-1}+2^{t-1}u_t^*.
\]

Every arithmetic operation is exact. The values `r_n` and `M_n` are certified with rational upper and lower bounds for `log n`; neither factorial endpoints nor boundary decisions use floating point.

## Certificate result

For every `12<=n<=45`, the connected-core recursion reaches the full quotient endpoint:

\[
E_{k_n}+W_n\ge Y_n
\]

using between two and six legal main layers.

Therefore N2-ADD-119 and the marker-three correction reduction give, for each audited `n`,

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
\le k_n+r_n.
\]

Across the complete audited range,

\[
k_n\le6,
\qquad
r_n\le16,
\]

so the finite uniform consequence is

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
\le22
\qquad(12\le n\le45).
\]

This is an exact finite theorem only. It is not an asymptotic occupancy theorem.

## Layer-count transitions

- two layers suffice for `12<=n<=14`;
- three layers suffice for `15<=n<=19`;
- four layers suffice for `20<=n<=25`;
- five layers suffice for `26<=n<=38`;
- six layers suffice for `39<=n<=45`.

## Exact summary

| n | r_n | layers used | odd cores | Y_n | occupied through | margin | term bound |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 12 | 10 | 2 | 60 | 7295 | 8845 | 1550 | 12 |
| 13 | 11 | 2 | 120 | 26303 | 32676 | 6373 | 13 |
| 14 | 11 | 2 | 180 | 98419 | 104316 | 5897 | 13 |
| 15 | 11 | 3 | 288 | 381178 | 560526 | 179348 | 14 |
| 16 | 12 | 3 | 288 | 1524714 | 2016377 | 491663 | 15 |
| 17 | 12 | 3 | 576 | 6286559 | 6985789 | 699230 | 15 |
| 18 | 12 | 3 | 768 | 26671611 | 27057589 | 385978 | 15 |
| 19 | 12 | 3 | 1536 | 116258858 | 119014097 | 2755239 | 15 |
| 20 | 12 | 4 | 1920 | 519925422 | 691527929 | 171602507 | 16 |
| 21 | 13 | 4 | 2880 | 2382597606 | 3722789468 | 1340191862 | 17 |
| 22 | 13 | 4 | 4320 | 11175373360 | 13749452300 | 2574078940 | 17 |
| 23 | 13 | 4 | 8640 | 53595207848 | 61296011062 | 7700803214 | 17 |
| 24 | 13 | 4 | 9600 | 262561823774 | 269981681038 | 7419857264 | 17 |
| 25 | 13 | 4 | 13440 | 1312809118871 | 1328229626310 | 15420507439 | 17 |
| 26 | 14 | 5 | 20160 | 6694039314748 | 13301385385029 | 6607346070281 | 19 |
| 27 | 14 | 5 | 26208 | 34783248603024 | 45450196963269 | 10666948360245 | 19 |
| 28 | 14 | 5 | 32760 | 184055651189076 | 206198478293137 | 22142827104061 | 19 |
| 29 | 14 | 5 | 65520 | 991170015337636 | 1461843197482335 | 470673182144699 | 19 |
| 30 | 14 | 5 | 80640 | 5428861757231651 | 6329305228098615 | 900443470866964 | 19 |
| 31 | 14 | 5 | 161280 | 30367161330041524 | 34062581585416162 | 3695420255374638 | 19 |
| 32 | 14 | 5 | 161280 | 171783017357059379 | 175480914113164681 | 3697896756105302 | 19 |
| 33 | 14 | 5 | 230400 | 986225203974375133 | 995655284426728059 | 9430080452352926 | 19 |
| 34 | 15 | 5 | 345600 | 5750385322517180785 | 5816284098842799529 | 65898776325618744 | 20 |
| 35 | 15 | 5 | 466560 | 34016684321298873156 | 34107777660954344219 | 91093339655471063 | 20 |
| 36 | 15 | 5 | 528768 | 203911928865173238938 | 203988268915871506382 | 76340050698267444 | 20 |
| 37 | 15 | 5 | 1057536 | 1240348785055006744319 | 1241234579493623778029 | 885794438617033710 | 20 |
| 38 | 15 | 5 | 1586304 | 7631400964105887377562 | 7633228434112937939901 | 1827470007050562339 | 20 |
| 39 | 15 | 6 | 2239488 | 47513036566947278987611 | 88363123625533909748205 | 40850087058586630760594 | 21 |
| 40 | 15 | 6 | 2488320 | 300500184889620382957632 | 346727343270739271958858 | 46227158381118889001226 | 21 |
| 41 | 15 | 6 | 4976640 | 1924435858273454946198848 | 2409805542455537019107258 | 485369684182082072908410 | 21 |
| 42 | 15 | 6 | 6128640 | 12474125430360483256226817 | 13123502565628906642792082 | 649377135268423386565265 | 21 |
| 43 | 16 | 6 | 12257280 | 81892903478378145417238045 | 117464987368230303059293709 | 35572083889852157642055664 | 22 |
| 44 | 16 | 6 | 15321600 | 543473558059476929409506521 | 608248962567403565372040483 | 64775404507926635962533962 | 22 |
| 45 | 16 | 6 | 18627840 | 3668446670326385075449057092 | 3760425228038003325635022840 | 91978557711618250185965748 | 22 |

## Largest completed case

At `n=45`:

- `r_n=16`;
- `M_n=232`;
- `v_2(45!)=41`;
- the exact odd-core set has `18,627,840` elements;
- six main layers suffice;
- the final term bound is `22`;
- the carrier overshoots `Y_n` by
  `91,978,557,711,618,250,185,965,748`.

The next value, `n=46`, has `27,941,760` odd cores, exceeding the declared `20,000,000` resource cap. Its status is `not audited due to resource limit`, not failure.

## Reproducibility

Generator:

`verification/marker_three_full_menu_audit.py`

Run the exact range in resource-compatible chunks, then combine the emitted `audits` arrays in increasing `n` order. Example:

```text
python verification/marker_three_full_menu_audit.py --n-min 12 --n-max 38
python verification/marker_three_full_menu_audit.py --n-min 39 --n-max 42
python verification/marker_three_full_menu_audit.py --n-min 43 --n-max 43
python verification/marker_three_full_menu_audit.py --n-min 44 --n-max 44
python verification/marker_three_full_menu_audit.py --n-min 45 --n-max 45
```

Frozen combined artifacts:

- `verification/data/marker_three_full_menu_n12_n45.json`
- `verification/data/marker_three_full_menu_n12_n45.csv`

Canonical JSON payload SHA-256:

`15f3598d3d111bfd78a7f1e51a9fd07972158c81f60686a76a5a3e03bf22224c`

CSV SHA-256:

`04c9f73c354c549d65935b1ca98c6573649cdffc9bb72873d313ea05d053e82e`

## Interpretation

The finite audit supplies three useful facts.

1. The carrier-block engine is not merely a toy prefix mechanism. On every exactly completed full-menu case, it reaches the full quotient endpoint.
2. No finite marker-three counterexample occurs in `12<=n<=45`.
3. The number of layers actually needed grows slowly in this range, from two to six, even though the complete odd-core menus grow to more than eighteen million values.

None of these facts controls the asymptotic regime. A proof must still establish uniform connected-core reach, produce a final-only additive theorem, or identify an exact obstruction beyond the completed finite range.

## Claim boundary

This result does not prove N2-ADD-120 for all sufficiently large `n`. It does not infer success at `n=46` or beyond. It does not convert profile capacity into additive occupancy. It does not remove the Phase 12P audit obligation for a sequential asymptotic proof.
