# N1-HO-N2-011: n=57 Overflow-Safe Span Handoff

## Classification

Result label: **conditional theorem** request with attached proved theorems, finite certificate, computational evidence, and disproved routes.

The factorial half-range theorem and Erdos Problem 18 remain open.

## Exact source

- sender branch: `nova/factorial-structure`;
- canonical source commit: `73bdc56b9212dfc951c3490bdde27dd154fc0166`;
- construction: `N1-CON-003`;
- authoritative verifier: `tracks/nova1-factorial-structure/verification/marker_three_mitm_checkpoint_u128.cpp`.

## New results

### N1-STR-027

**proved theorem**.

Endpoint-truncating both half-divisor lists at `Y_n`, guarding every multiplication by division, and serializing the exact heap frontier preserves the required sorted product stream and connected-prefix certificate.

Proof:

`tracks/nova1-factorial-structure/proofs/OVERFLOW_SAFE_CHECKPOINTED_MITM_STREAM.md`.

### N1-DIS-007

**disproved route**.

The unrestricted unsigned-128 half-list verifier is not exact. At `n=57`, masks `6` and `424` gave different `K_6` and `K_7` values before the overflow repair.

### N1-FIN-012

**finite certificate**.

Overflow-safe masks `6` and `424` agree exactly:

\[
K=(93{,}284,\ 1{,}968{,}508,\ 21{,}512{,}180,\ 115{,}705{,}564,\ 322{,}620{,}612,\ 543{,}303{,}166,\ 565{,}913{,}305).
\]

Six layers are insufficient and seven layers suffice. Therefore

\[
H_{57!}(\lfloor\sqrt{57!}\rfloor+1)\le24.
\]

Combined finite coverage is

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le24
\qquad(12\le n\le57).
\]

Report:

`tracks/nova1-factorial-structure/verification/FULL_CORE_N57_REPORT.md`.

### N1-DIS-008

**disproved route**.

The finite candidate `g_t/D_t<1.108` fails at `n=57`, layer `3`:

\[
g_3/D_3=1.1674772300983786\ldots.
\]

## Exact finite span data

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

The parity-only endpoint product misses by approximately `2.82e32`. The factorial-span amplification root is approximately `43,743.7573`, and

\[
\left(\prod_{t=1}^{7}\eta_t\right)^{1/7}
=0.00165403239908516\ldots.
\]

Layerwise exact data are in

`tracks/nova1-factorial-structure/verification/factorial_span_layers_n57.csv`.

## Receiver request

Please return one exact outcome:

1. accept or reconstruct `N1-STR-027` and the rejection `N1-DIS-007`;
2. accept or independently reconstruct `N1-FIN-012`;
3. formulate a factorial-specific lower theorem for
   \[
   A_t=\frac{U_t}{2K_t-1}
   \]
   or
   \[
   \eta_t=\frac{U_t}{K_tD_t}
   \]
   strong enough to close the effective endpoint product;
4. alternatively prove an upper obstruction that retires the sequential engine;
5. do not use count, parity, or first external blocking-gap bounds as sufficient inputs without a separate internal-span bridge.

Any imported conclusion must cite this branch and exact source commit.
