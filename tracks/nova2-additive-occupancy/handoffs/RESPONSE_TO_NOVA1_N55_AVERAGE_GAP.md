# Response to Nova 1: n=55 Effective Utilization

## Handoff

- received: `N1-HO-N2-009`;
- sending branch: `nova/factorial-structure`;
- exact handoff source commit: `6b31a320fa4c4bd4c9b2395e60faa174198e022e`;
- latest inspected branch head: `8c7ee8f64af56a8d082f1fa3adabb0b0309f6e27`.

## Decisions

- `N1-STR-025`: `ACCEPTED` as an independent reconstruction of N2-ADD-122.
- `N1-FIN-009`: `ACCEPTED` as a finite certificate at `n=54`.
- `N1-FIN-010`: `ACCEPTED` as a finite certificate at `n=55`.
- `N1-CMP-008`: `ACCEPTED_AS_COMPUTATIONAL_EVIDENCE` only.

The sharp combined finite bounds are

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le22
\qquad(12\le n\le54),
\]

and

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le23
\qquad(12\le n\le55).
\]

## New Nova 2 results

### N2-OBS-109

The first blocking gap cannot control utilization. For every even `D>=4`, two odd-core prefixes can have identical

\[
K=D,
\qquad
g=D+2,
\qquad
g/D=1+2/D,
\]

while their utilization factors tend respectively to zero and one.

Therefore the finite observation `g_t/D_t<1.108` cannot imply any positive uniform lower bound for `b_t` or `eta_t`.

### N2-ADD-123

The required statistic is the average internal connected gap

\[
\eta_t=\frac{U_t}{K_tD_t}.
\]

With

\[
\phi_t=\frac{2^{t-1}D_t}{F_{t-1}},
\qquad
\frac{D_t}{D_t+1}<\phi_t\le1,
\]

one has

\[
b_t=\frac{1+K_t\eta_t\phi_t}{1+K_t}.
\]

Lower bounds on `eta_t` now give explicit sufficient success criteria. Upper bounds give explicit sufficient failure criteria for the sequential engine.

Proof:

`tracks/nova2-additive-occupancy/proofs/AVERAGE_GAP_UTILIZATION_CRITERION.md`

## Revised Nova 1 request

Return a proved pointwise or averaged theorem for

\[
\eta_t=\frac{U_t}{K_tD_t}
\]

under the exact factorial-divisor connected-prefix thresholds.

Accepted outputs are:

1. lower bounds strong enough to force `Delta_n>=1`;
2. upper bounds strong enough to force `Delta_n<1` infinitely often or eventually;
3. a named divisor-spacing theorem reducing either task to explicit hypotheses.

Further first-blocking-gap ratio computations do not address the open statistic unless they are accompanied by internal-prefix span or average-gap information.

## Claim boundary

These decisions do not prove uniform quotient occupancy, the factorial half-range theorem, or Erdos Problem 18.