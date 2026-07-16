# Rankin Smooth-Divisor Span Bound

## Results

- `N2-ADD-127`: **proved theorem**, Rankin weighted-divisor lower bound for the connected-prefix maximum.
- `N2-ADD-128`: **proved theorem**, explicit Euler-product carrier criterion.
- `N2-CMP-208`: **computational evidence**, exact fixed-parameter Rankin-median diagnostic for `51<=n<=55`.

The factorial formulation of Erdos Problem 18 remains open. These results concern only the sequential marker-three carrier engine.

## Frozen inputs

- Nova 2 results: `N2-ADD-120` through `N2-ADD-126`.
- Nova 1 branch: `nova/factorial-structure`.
- Exact inspected head: `8c7ee8f64af56a8d082f1fa3adabb0b0309f6e27`.
- Exact finite inputs: `N1-FIN-006` through `N1-FIN-010`.

## Reserved odd core

Put

\[
C_n=\frac{n!}{3\,2^{v_2(n!)}}
=\prod_{p\le n,\ p\text{ odd}}p^{e_p(n)},
\]

where

\[
e_3(n)=v_3(n!)-1
\]

and

\[
e_p(n)=v_p(n!)
\qquad(p\ne3).
\]

Let

\[
1=c_1<c_2<\cdots<c_{\tau_n}=C_n
\]

be the positive divisors of `C_n`. At an executed carrier layer,

\[
U_t=c_{K_t}.
\]

## Weighted divisor moment

For every real `sigma>0`, define

\[
Z_n(\sigma)
=\sum_{d\mid C_n}d^{-\sigma}.
\]

The divisor coordinates are independent, so exactly

\[
Z_n(\sigma)
=\prod_{p^{e_p}\parallel C_n}
\left(1+p^{-\sigma}+\cdots+p^{-e_p\sigma}\right)
\]

and equivalently

\[
Z_n(\sigma)
=\prod_{p^{e_p}\parallel C_n}
\frac{1-p^{-(e_p+1)\sigma}}{1-p^{-\sigma}}.
\]

This is a finite Euler product using the exact factorial prime exponents.

## N2-ADD-127: Rankin connected-prefix lower bound

For every executed layer and every `sigma>0`,

\[
U_t
\ge
\left(\frac{K_t}{Z_n(\sigma)}\right)^{1/\sigma}.
\]

Consequently

\[
A_t
=\frac{U_t}{2K_t-1}
\ge
\frac1{2K_t-1}
\left(\frac{K_t}{Z_n(\sigma)}\right)^{1/\sigma}.
\]

Define the optimized Rankin radius

\[
Q_t^{\mathrm R}
=\sup_{\sigma>0}
\left(\frac{K_t}{Z_n(\sigma)}\right)^{1/\sigma}.
\]

Then

\[
U_t\ge Q_t^{\mathrm R}.
\]

### Proof

Fix `Q>0` and `sigma>0`. Every divisor `d<Q` satisfies

\[
1<\left(\frac Qd\right)^\sigma.
\]

Therefore

\[
\#\{d:d\mid C_n,\ d<Q\}
<
Q^\sigma\sum_{d\mid C_n}d^{-\sigma}
=Q^\sigma Z_n(\sigma).
\]

Choose

\[
Q=\left(\frac{K_t}{Z_n(\sigma)}\right)^{1/\sigma}.
\]

Then fewer than `K_t` divisors lie below `Q`. Since `U_t=c_{K_t}`, one has `U_t>=Q`. Taking the supremum over `sigma` proves the optimized statement. `QED`

## N2-ADD-128: explicit Rankin-median carrier criterion

For a chosen parameter `sigma_t>0`, define

\[
R_t(\sigma_t)
=
\left(\frac{K_t}{Z_n(\sigma_t)}\right)^{1/\sigma_t}.
\]

Let

\[
S_t^{\mathrm R}
=
\max\left(
2K_t-1,
R_t(\sigma_t),
\mathbf 1_{K_t>\tau_n/2}\left\lceil\sqrt{C_n}\right\rceil
\right).
\]

Then

\[
U_t\ge S_t^{\mathrm R}.
\]

With

\[
D_t=\left\lfloor\frac{F_{t-1}}{2^{t-1}}\right\rfloor,
\]

one has

\[
\frac{F_t}{F_{t-1}}
>
\frac{D_t+1+S_t^{\mathrm R}}{D_t+1}.
\]

Hence the explicit condition

\[
\prod_{t=1}^{L}
\frac{D_t+1+S_t^{\mathrm R}}{D_t+1}
\ge
\frac{Y_n+1}{W_n+1}
\]

is sufficient for exact endpoint coverage.

### Proof

The three lower bounds entering `S_t^R` are respectively `N2-ADD-124`, `N2-ADD-127`, and the median corollary of `N2-ADD-126`. The carrier-factor inequality follows from

\[
F_{t-1}<2^{t-1}(D_t+1)
\]

exactly as in the previous span criteria. Multiplication proves the endpoint condition. `QED`

## N2-CMP-208: fixed-parameter finite diagnostic

For each exact layer at `51<=n<=55`, a fixed decimal value of `sigma_t` was selected near the numerical maximizer of the Rankin radius. No optimization claim is needed for the theorem or verifier.

The Rankin bound is used on every layer, with the stronger complement-median bound retained when available. The resulting endpoint ratios are:

| `n` | Rankin-median endpoint ratio, sixth root | unrooted `log10` ratio |
|---:|---:|---:|
| 51 | `0.000542135786332180` | `-19.5953515442` |
| 52 | `0.000488608023294683` | `-19.8662364353` |
| 53 | `0.000443191288757114` | `-20.1204527074` |
| 54 | `0.000438131601230971` | `-20.1503725273` |
| 55 | `0.000374184125626777` | `-20.5614878456` |

Relative to the complement-median diagnostic `N2-CMP-207`, the unrooted lower bound improves by roughly `10^3.4` through `10^4.2`. However, the certified product still misses the exact endpoint requirement by roughly `10^19.6` through `10^20.6`.

The fixed Rankin radii remain below the true connected maxima by approximately two decimal orders in the first layer and up to approximately ten decimal orders in the sixth layer. This is finite computational evidence only. No asymptotic trend is asserted.

## Consequence

The sequential frontier is sharpened again:

1. `N2-ADD-127` supplies a genuine factorial-specific lower bound at every layer from the exact prime-exponent Euler product;
2. the complement median remains stronger in the final two finite layers;
3. the combined theorem is still quantitatively far from endpoint closure;
4. the next valid theorem must improve the lower-tail divisor count beyond the one-parameter Rankin moment, for example through a saddle-point estimate, a multi-parameter exponent-box bound, or a direct smooth-divisor counting theorem;
5. final-only restricted-sumset and Fourier routes remain unaffected.

## Claim boundary

These results do not prove or disprove uniform marker-three quotient occupancy, the factorial half-range theorem, or Erdos Problem 18.
