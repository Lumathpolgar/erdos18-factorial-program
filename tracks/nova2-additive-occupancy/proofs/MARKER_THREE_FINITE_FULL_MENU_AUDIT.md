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

This exact audit covers every integer

\[
12\le n\le45.
\]

For each `n`, it generates the complete odd-core set

\[
\mathcal U(n)=\{u\ge1:u\text{ odd},\ 3u\mid n!\},
\]

and then uses the exact layer cutoff

\[
U_t(n)=\left\{u\in\mathcal U(n):2^{t-1}u\le Y_n\right\},
\qquad
Y_n=\left\lfloor\frac{\lfloor\sqrt{n!}\rfloor}{3}\right\rfloor.
\]

No reduced odd-core menu, sampling rule, or high-prime-only substitute is used.

The scan begins at `n=12`, where the full binary correction palette first satisfies the required legality check in this audited range:

\[
r_n-1\le v_2(n!).
\]

Only layers with legal 2-adic address are used. The recursion stops once its certified occupied endpoint reaches `Y_n`.

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

The complete sorted menu is scanned from zero. Consecutive cores remain in the connected component precisely while their gap is at most `D_t`. If `u_t^*` is the largest connected core, then

\[
E_t=E_{t-1}+2^{t-1}u_t^*.
\]

All factorial endpoints, divisibility tests, menu values, gaps, and endpoint comparisons use exact integer arithmetic. The parameters `r_n` and `M_n` are certified using rational upper and lower bounds for `log n`.

## Certificate result

For every `12<=n<=45`, the connected-core recursion reaches the complete quotient endpoint:

\[
E_{k_n}+W_n\ge Y_n.
\]

It requires only two through six legal main layers. Therefore N2-ADD-119 and the marker-three correction reduction give the exact finite bounds

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
\le k_n+r_n.
\]

Across the whole audited range,

\[
k_n\le6,
\qquad
r_n\le16,
\]

and hence

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

## Largest completed case

At `n=45`:

- `r_n=16`;
- `M_n=232`;
- `v_2(45!)=41`;
- the exact odd-core set has `18,627,840` elements;
- the exact quotient endpoint is
  `3,645,731,459,384,007,323,435,539,335`;
- six main layers suffice;
- the certified occupied endpoint is
  `3,737,710,017,095,625,573,621,505,083`;
- the overshoot margin is
  `91,978,557,711,618,250,185,965,748`;
- the resulting term bound is `22`.

The next value, `n=46`, has `27,941,760` odd cores, exceeding the declared `20,000,000` generation cap. Its status is `not audited due to resource limit`, not failure.

## Reproducibility

Generator:

`verification/marker_three_full_menu_audit.py`

The completed range was replayed in resource-compatible chunks:

```text
python verification/marker_three_full_menu_audit.py --n-min 12 --n-max 38
python verification/marker_three_full_menu_audit.py --n-min 39 --n-max 42
python verification/marker_three_full_menu_audit.py --n-min 43 --n-max 43
python verification/marker_three_full_menu_audit.py --n-min 44 --n-max 44
python verification/marker_three_full_menu_audit.py --n-min 45 --n-max 45
```

Frozen artifacts:

- `verification/data/marker_three_full_menu_n12_n45.json`
- `verification/data/marker_three_full_menu_n12_n45.csv`

Canonical JSON payload SHA-256:

`15f3598d3d111bfd78a7f1e51a9fd07972158c81f60686a76a5a3e03bf22224c`

CSV SHA-256:

`04c9f73c354c549d65935b1ca98c6573649cdffc9bb72873d313ea05d053e82e`

The CSV contains the exact per-`n` summary. The JSON additionally records every per-layer menu size, threshold, connected core, first blocking gap, and carrier endpoint.

## Interpretation

The finite audit establishes three facts.

1. The carrier-block engine reaches the full quotient endpoint in every exactly completed full-menu case.
2. No marker-three counterexample occurs for `12<=n<=45`.
3. The number of main layers required grows only from two to six over this range, even though the exact odd-core menu grows beyond eighteen million values.

These facts do not control the asymptotic regime. A proof must still establish uniform connected-core reach, obtain a final-only additive theorem, or identify an exact obstruction after the completed finite range.

## Claim boundary

This result does not prove N2-ADD-120 for all sufficiently large `n`. It does not infer success at `n=46` or beyond. It does not convert formal profile capacity into occupancy. It does not remove the Phase 12P audit obligation for a sequential asymptotic proof.
