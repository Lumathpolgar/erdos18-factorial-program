# Effective Carrier Factorization Reconstruction

## Result

`N1-STR-025`, **proved theorem**.

The factorial half-range theorem remains open. This theorem sharpens only the sequential marker-three carrier accounting.

## Imported source

- source branch: `nova/additive-occupancy`;
- exact source commit: `2ab09dd980f7116b82530368e3d98bb53240bf0c`;
- source theorem: `N2-ADD-122`;
- source proof: `tracks/nova2-additive-occupancy/proofs/EFFECTIVE_CARRIER_ENTROPY_FACTORIZATION.md`.

The proof below is an independent algebraic reconstruction in Nova 1 notation.

## Setup

Put

\[
F_0=W_n+1.
\]

At executed layer `t`, let

\[
s_t=2^{t-1},\qquad D_t=\left\lfloor\frac{F_{t-1}}{s_t}\right\rfloor.
\]

Write the complete zero-connected odd-core prefix as

\[
0=u_{t,0}<u_{t,1}<\cdots<u_{t,K_t}=U_t.
\]

Every consecutive gap in this prefix is at most `D_t`, and the carrier update is

\[
F_t=F_{t-1}+s_tU_t.
\]

For `K_t>0`, define

\[
a_t=\frac{s_tU_t}{F_{t-1}},\qquad
\eta_t=\frac{U_t}{K_tD_t},\qquad
\phi_t=\frac{s_tD_t}{F_{t-1}}.
\]

Set `eta_t=0` when `K_t=0`.

## Exact factorization

For every executed layer,

\[
a_t=K_t\eta_t\phi_t,
\qquad
0\le a_t\le K_t,
\qquad
0\le\eta_t\le1,
\qquad
0<\phi_t\le1.
\]

Moreover,

\[
\frac{F_L}{W_n+1}=\prod_{t=1}^{L}(1+a_t).
\]

Let

\[
P_n=\prod_{t=1}^{L}(1+K_t),
\qquad
b_t=\frac{1+a_t}{1+K_t}.
\]

Then

\[
0<b_t\le1
\]

and

\[
\frac{F_L}{W_n+1}=P_n\prod_{t=1}^{L}b_t.
\]

Define the exact endpoint requirement

\[
R_n=\frac{Y_n+1}{W_n+1},
\]

and the root-normalized factors

\[
\widetilde\Gamma_n=(P_n/R_n)^{1/L},
\qquad
\mathcal B_n=\left(\prod_{t=1}^{L}b_t\right)^{1/L},
\qquad
\Delta_n=\left(\frac{F_L}{Y_n+1}\right)^{1/L}.
\]

Then

\[
\Delta_n=\widetilde\Gamma_n\mathcal B_n.
\]

Exact endpoint success is equivalent to

\[
\Delta_n\ge1.
\]

Finally,

\[
b_t\ge\eta_t\phi_t,
\]

so the explicit inequality

\[
\widetilde\Gamma_n
\left(\prod_{t=1}^{L}\eta_t\phi_t\right)^{1/L}
\ge1
\]

is sufficient for endpoint coverage.

## Proof

There are `K_t` positive consecutive gaps from zero to `U_t`. Each gap is at most `D_t`, so

\[
U_t\le K_tD_t.
\]

This proves `0<=eta_t<=1`. Since `D_t=floor(F_{t-1}/s_t)`,

\[
0<s_tD_t\le F_{t-1},
\]

which gives `0<phi_t<=1`. Direct substitution gives

\[
K_t\eta_t\phi_t
=K_t\frac{U_t}{K_tD_t}\frac{s_tD_t}{F_{t-1}}
=\frac{s_tU_t}{F_{t-1}}
=a_t.
\]

The carrier update becomes

\[
F_t=F_{t-1}(1+a_t).
\]

Iteration from `F_0=W_n+1` proves the first product formula. Multiplying and dividing each factor by `1+K_t` proves the exact utilization factorization.

Since endpoint success is `F_L>=Y_n+1`, division by `W_n+1` and positive `L`th roots prove the endpoint criterion and the identity for `Delta_n`.

For `x=eta_t phi_t` in `[0,1]`,

\[
\frac{1+K_tx}{1+K_t}-x
=\frac{1-x}{1+K_t}\ge0.
\]

Thus `b_t>=eta_t phi_t`, completing the proof. `QED`

## Consequence for the active route

`N1-OBS-003` and `N1-STR-024` remain valid necessary count gates. They are not sufficient by themselves. A sequential asymptotic proof must also control the utilization product, or an equivalent average-gap quantity, strongly enough that `Delta_n>=1`.
