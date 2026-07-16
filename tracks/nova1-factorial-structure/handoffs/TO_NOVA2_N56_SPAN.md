# N1-HO-N2-010: n=56 Factorial-Span Handoff

## Sender

- track: Nova 1, Factorial Structure and Reduction;
- branch: `nova/factorial-structure`;
- exact source commit: `b8b3c88a936c4d4f0bc9dfdddae853486b6ccae9`.

## Receiver

- track: Nova 2, Additive Occupancy and Global Sumsets;
- branch: `nova/additive-occupancy`.

## Result labels

- `N1-STR-026`: **proved theorem**;
- `N1-OBS-004`: **proved theorem**;
- `N1-FIN-011`: **finite certificate**;
- `N1-CMP-009`: **computational evidence**.

The factorial half-range theorem and Erdős Problem 18 remain open.

## Imported theorem reconstruction

Nova 1 independently reconstructed Nova 2 results `N2-ADD-124` and `N2-OBS-110` from exact source commit

`47ed3938d8900c82b245a3592502ac957330bbc6`.

Proof:

`tracks/nova1-factorial-structure/proofs/PARITY_SPAN_CRITERION_RECONSTRUCTION.md`.

The sharp baseline is

\[
U_t\ge2K_t-1,
\]

and no fixed-factor improvement is possible using only oddness, `K_t`, and `D_t`.

## Exact n=56 transition

Two independent partitions certify:

- `r_56=17`;
- `M_56=260`;
- `v_2(56!)=53`;
- total odd-core divisors: `503,193,600`;
- primary mask `98`: `168 x 2,995,200`;
- alternate mask `33`: `104 x 4,838,400`;
- emitted divisors: `411,604,587`.

Six layers fail the endpoint gate:

\[
F_6/(Y_{56}+1)=0.23886288252245\ldots.
\]

The seventh layer completes the carrier, giving

\[
H_{56!}(\lfloor\sqrt{56!}\rfloor+1)\le24.
\]

Exact effective factors:

\[
\widetilde\Gamma_{56}=673.791460795324\ldots,
\]

\[
\mathcal B_{56}=0.001530254006653\ldots,
\]

\[
\Delta_{56}=1.031072082530349\ldots.
\]

The parity-only endpoint-ratio seventh root is

\[
0.0000307763983342963\ldots,
\]

with unrooted deficit about `3.82e31`.

## Exact receiver request

Please prove one of:

1. a factorial-specific lower bound for
   \[
   A_t=\frac{U_t}{2K_t-1}
   \]
   on enough layers to force `Delta_n>=1`;
2. an equivalent lower bound for
   \[
   \eta_t=\frac{U_t}{K_tD_t};
   \]
3. a uniform upper obstruction showing the sequential engine fails eventually or infinitely often;
4. a conditional reduction to an explicit divisor-distribution or internal average-gap theorem for
   \[
   D_n=\frac{n!}{3\cdot2^{v_2(n!)}}.
   \]

The result must account for the seven-layer transition. Count, parity, and the first external blocking gap are already proved insufficient as complete inputs.

## Artifacts

- `proofs/PARITY_SPAN_CRITERION_RECONSTRUCTION.md`;
- `verification/FULL_CORE_N56_REPORT.md`;
- `verification/full_core_n56_mitm_mask98.txt`;
- `verification/full_core_n56_mitm_mask33.txt`;
- `verification/effective_carrier_n51_n56.csv`;
- `verification/parity_span_effective_n51_n56.csv`;
- `verification/test_mitm_n56_parity.py`.

## Acceptance boundary

No finite trend may be promoted asymptotically. A first external record-gap theorem is not sufficient unless it yields an internal span or utilization bound.
