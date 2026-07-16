# Effective Carrier Entropy Factorization

## Result

`N2-ADD-122`, proved theorem.

The factorial formulation of Erdos Problem 18 remains open. This result sharpens only the sequential marker-three carrier engine.

## Frozen inputs

- Nova 2 carrier results: `N2-ADD-119`, `N2-ADD-120`.
- Nova 1 branch: `nova/factorial-structure`.
- Exact inspected commit: `a6bdab1b917f3b3688f5a0c86e80c8a026bfbc07`.
- Handoff: `N1-HO-N2-007`.
- Imported results: `N1-STR-024`, `N1-FIN-006`, `N1-FIN-007`, `N1-FIN-008`.

## Setup

Put `F_0=W_n+1`. At executed layer `t`, let

\[
s_t=2^{t-1},\qquad D_t=\lfloor F_{t-1}/s_t\rfloor.
\]

Let

\[
0=u_{t,0}<u_{t,1}<\cdots<u_{t,K_t}=U_t
\]

be the complete zero-connected prefix, so every consecutive gap is at most `D_t` and

\[
F_t=F_{t-1}+s_tU_t.
\]

Define

\[
a_t=\frac{s_tU_t}{F_{t-1}},
\qquad
\eta_t=\frac{U_t}{K_tD_t},
\qquad
\phi_t=\frac{s_tD_t}{F_{t-1}}
\]

when `K_t>0`, with `eta_t=0` when `K_t=0`.

## Theorem

For every executed `L`-layer carrier:

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
\frac{F_L}{W_n+1}=\prod_{t=1}^L(1+a_t).
\]

Put

\[
P_n=\prod_{t=1}^L(1+K_t),
\qquad
b_t=\frac{1+a_t}{1+K_t}.
\]

Then `0<b_t<=1` and

\[
\frac{F_L}{W_n+1}=P_n\prod_{t=1}^Lb_t.
\]

Writing

\[
R_n=\frac{Y_n+1}{W_n+1},
\]

exact endpoint success is equivalent to

\[
P_n\prod_{t=1}^Lb_t\ge R_n.
\]

Define

\[
\widetilde\Gamma_n=(P_n/R_n)^{1/L},
\quad
\mathcal B_n=(\prod_tb_t)^{1/L},
\quad
\Delta_n=(F_L/(Y_n+1))^{1/L}.
\]

Then

\[
\Delta_n=\widetilde\Gamma_n\mathcal B_n,
\]

and success is equivalent to `Delta_n>=1`.

Finally,

\[
b_t=\frac{1+K_t\eta_t\phi_t}{1+K_t}\ge\eta_t\phi_t.
\]

Therefore the explicit condition

\[
\widetilde\Gamma_n
(\prod_t\eta_t\phi_t)^{1/L}\ge1
\]

is sufficient for endpoint coverage.

## Proof

There are `K_t` positive connected gaps and each is at most `D_t`, so `U_t<=K_tD_t`. This proves the bounds and the identity `a_t=K_t eta_t phi_t`. The carrier update gives `F_t=F_{t-1}(1+a_t)`, and iteration proves the product formula. Factoring `1+K_t` from each layer gives the exact utilization factorization. Since success means `F_L>=Y_n+1`, division by `W_n+1` proves the endpoint criterion. Taking positive `L`th roots proves `Delta_n=widetilde Gamma_n B_n`.

For `x=eta_t phi_t` in `[0,1]`,

\[
\frac{1+K_tx}{1+K_t}-x=\frac{1-x}{1+K_t}\ge0.
\]

This proves the sufficient condition. `QED`

## Finite diagnostics

Exact Nova 1 rows give:

| n | count surplus | utilization root | endpoint surplus |
|---:|---:|---:|---:|
| 51 | 120.322026488584 | 0.008311064676932 | 1.000004144206103 |
| 52 | 97.645052132052 | 0.010241184816549 | 1.000001025305911 |
| 53 | 124.609364763243 | 0.008025094814707 | 1.000001967025492 |

Thus the large cardinality surplus is mostly consumed by packing-efficiency loss. Prefix count alone is a necessary gate, not a sufficient endpoint theorem.

## Next exact theorem node

Prove a uniform lower bound for the utilization product `prod b_t`, or equivalently for enough average-gap factors `eta_t`, strong enough that

\[
\widetilde\Gamma_n\mathcal B_n\ge1.
\]

This theorem does not prove uniform occupancy, the factorial half-range theorem, or Erdos Problem 18.
