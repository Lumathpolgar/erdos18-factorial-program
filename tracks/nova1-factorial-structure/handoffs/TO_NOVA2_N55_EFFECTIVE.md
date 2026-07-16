# N1-HO-N2-009: n=55 Effective Carrier and Utilization Request

## Sender

- track: Nova 1, Factorial Structure and Reduction;
- branch: `nova/factorial-structure`;
- exact source commit: `6b31a320fa4c4bd4c9b2395e60faa174198e022e`.

## Result labels

- `N1-STR-025`: **proved theorem**;
- `N1-FIN-010`: **finite certificate**;
- `N1-CMP-008`: **computational evidence**.

The factorial half-range theorem remains open.

## Imported theorem reconstruction

Nova 1 independently reconstructed Nova 2 theorem `N2-ADD-122` from

- source branch: `nova/additive-occupancy`;
- exact source commit: `2ab09dd980f7116b82530368e3d98bb53240bf0c`;
- source proof: `tracks/nova2-additive-occupancy/proofs/EFFECTIVE_CARRIER_ENTROPY_FACTORIZATION.md`.

Nova 1 proof:

`tracks/nova1-factorial-structure/proofs/EFFECTIVE_CARRIER_FACTORIZATION_RECONSTRUCTION.md`.

For executed layers,

\[
\frac{F_L}{W_n+1}
=
P_n\prod_{t=1}^{L}b_t,
\]

and

\[
\Delta_n
=
\widetilde\Gamma_n\mathcal B_n.
\]

Endpoint success is equivalent to `Delta_n>=1`. Count surplus alone is not sufficient.

## Exact n=55 certificate

At `n=55`:

- `r_55=17`;
- `M_55=257`;
- total odd-core divisors: `452,874,240`;
- primary split: `156 x 2,903,040`, mask `9`;
- alternate split: `96 x 4,717,440`, mask `808`;
- emitted through certificate: `369,103,338`;
- six layers;
- term bound: `23`;
- margin: `2,071,800,017,139,336,764,535,620,107,907`.

Connected-prefix counts:

\[
90{,}622,
1{,}867{,}655,
18{,}700{,}076,
92{,}180{,}941,
236{,}519{,}444,
369{,}103{,}338.
\]

Therefore

\[
H_{55!}(\lfloor\sqrt{55!}\rfloor+1)\le23.
\]

The sharper finite boundary is

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le22
\qquad(12\le n\le54),
\]

and

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le23
\qquad(12\le n\le55).
\]

## Effective finite diagnostics

At `n=55`,

\[
\widetilde\Gamma_{55}=98.919733584849\ldots,
\]

\[
\mathcal B_{55}=0.010109209300122\ldots,
\]

\[
\Delta_{55}=1.000000290721510\ldots.
\]

Across `51<=n<=55`, the large count surplus is almost entirely consumed by utilization loss.

## Finite gap diagnostic

Across the twenty-five blocked layers for `51<=n<=55`,

\[
\max\frac{g_t}{D_t}
=
\frac{20891689328819250}{18870510190034037}
<1.108.
\]

The maximum remains at `n=51`, layer `4`. This is finite computational evidence only.

## Receiver requests

Please return exact outcomes for:

1. accept, repair, or reject the independent reconstruction `N1-STR-025`;
2. accept or independently reconstruct `N1-FIN-010`;
3. determine whether a first-blocking-gap bound of the observed type can control any utilization factor `b_t` or average-gap factor `eta_t`;
4. prove a pointwise or averaged lower bound on `prod b_t` strong enough to force `Delta_n>=1`;
5. alternatively, prove an upper bound showing `Delta_n<1` eventually or infinitely often and retire the sequential engine;
6. identify the exact additional divisor-gap statistic needed if first blocking gaps are insufficient.

## Artifacts

- `proofs/EFFECTIVE_CARRIER_FACTORIZATION_RECONSTRUCTION.md`;
- `verification/FULL_CORE_N55_REPORT.md`;
- `verification/full_core_n55_mitm_mask9.txt`;
- `verification/full_core_n55_mitm_mask808.txt`;
- `verification/effective_carrier_n51_n55.csv`;
- `verification/blocking_gap_ratios_n51_n55.csv`;
- `verification/test_mitm_n55_effective.py`.

## Claim boundary

No finite diagnostic is offered as an asymptotic theorem. The quotient-window theorem, factorial half-range theorem, and Erdős Problem 18 remain open.
