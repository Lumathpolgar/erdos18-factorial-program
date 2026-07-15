# Connected-Prefix Entropy Requirement

## Result ID

`N1-OBS-003`

Result label: **proved theorem**.

## Imported carrier framework

This theorem audits the exact marker-three connected-core recursion imported from:

- branch: `nova/additive-occupancy`;
- exact commit: `82603c631a106c3bff4676bdeeb9cc791fc98f3c`;
- proved carrier lemma: `N2-ADD-119`;
- conditional chain theorem: `N2-ADD-120`;
- proof: `tracks/nova2-additive-occupancy/proofs/MARKER_THREE_CARRIER_BLOCK_REDUCTION.md`.

The imported recursion remains a sufficient sequential proof engine. This file derives a necessary entropy condition for that engine to reach the factorial quotient endpoint.

## Frozen objects

Write

\[
X_n=\lfloor\sqrt{n!}\rfloor,
\qquad
Y_n=\left\lfloor\frac{X_n}{3}\right\rfloor,
\]

\[
r_n=\lceil4\log n\rceil,
\qquad
M_n=\lceil16(\log n)^2\rceil,
\]

and

\[
W_n=\left\lfloor\frac{2^{r_n}-3}{3}\right\rfloor.
\]

At layer `t`, let `E_(t-1)` be the exact carrier endpoint already certified and put

\[
F_{t-1}=E_{t-1}+W_n+1.
\]

The exact core-gap threshold is

\[
D_t=\left\lfloor\frac{F_{t-1}}{2^{t-1}}\right\rfloor.
\]

Let

\[
0=u_{t,0}<u_{t,1}<\cdots<u_{t,K_t}=u_t^*
\]

be the complete connected component of zero inside the ordered core menu, so every consecutive gap is at most `D_t`. The carrier update is

\[
E_t=E_{t-1}+2^{t-1}u_t^*.
\]

Here `K_t` is the number of positive cores in the connected prefix used by the complete-core carrier engine. It is not the total layer-menu size unless the full truncated menu is connected.

## N1-OBS-003: exact connected-prefix product bound

For every executed carrier layer,

\[
F_t\le F_{t-1}(1+K_t).
\]

Consequently, after `L` layers,

\[
F_L
\le
(W_n+1)\prod_{t=1}^{L}(1+K_t).
\]

If the carrier recursion certifies the complete quotient range, meaning

\[
E_L+W_n\ge Y_n,
\]

then necessarily

\[
\prod_{t=1}^{L}(1+K_t)
\ge
\frac{Y_n+1}{W_n+1}.
\]

### Proof

The connected prefix begins at zero and has `K_t` positive gaps. Each gap is at most `D_t`. Therefore

\[
u_t^*\le K_tD_t.
\]

Using the definition of `D_t`,

\[
2^{t-1}u_t^*
\le
2^{t-1}K_tD_t
\le
K_tF_{t-1}.
\]

Hence

\[
F_t
=
E_t+W_n+1
=
F_{t-1}+2^{t-1}u_t^*
\le
F_{t-1}(1+K_t).
\]

Iteration gives the product bound. If `E_L+W_n>=Y_n`, then `F_L>=Y_n+1`, and comparison with the iterated upper bound proves the necessary product inequality. `QED`

## Explicit asymptotic consequence

For every integer

\[
n\ge120368,
\]

if the complete connected-core recursion reaches `Y_n` using at most `M_n` layers, then

\[
\left(
\prod_{t=1}^{L}(1+K_t)
\right)^{1/L}
\ge
\exp\left(\frac{n}{85\log n}\right).
\]

In particular, at least one executed layer must satisfy

\[
K_t
\ge
\exp\left(\frac{n}{85\log n}\right)-1.
\]

### Proof of the explicit constant

The last `n/2` factors of `n!` are at least `n/2`, so

\[
n!\ge(n/2)^{n/2}.
\]

For `n>=3`,

\[
Y_n+1\ge\frac{\sqrt{n!}}{6},
\]

and therefore

\[
\log(Y_n+1)
\ge
\frac n4\log(n/2)-\log6.
\]

Also

\[
W_n+1\le\frac{2^{r_n}}3,
\]

and `r_n<=4 log n+1`, so for `n>=3`,

\[
\log(W_n+1)\le3\log n.
\]

For every `n>=120368`, the preceding two estimates give

\[
\log\frac{Y_n+1}{W_n+1}
\ge
\frac n5\log n.
\]

Finally,

\[
L\le M_n
\le17(\log n)^2.
\]

Taking logarithms in the necessary product inequality and dividing by `L` yields

\[
\frac1L\sum_{t=1}^{L}\log(1+K_t)
\ge
\frac{n}{85\log n}.
\]

Exponentiation proves the displayed geometric-mean bound. `QED`

## Interpretation

This theorem sharpens the earlier formal menu-capacity gate.

A successful connected-core proof does not merely need exponentially large complete menus. It needs exponentially large prefixes that remain additively connected from zero under the exact target-dependent carrier thresholds.

The required average connected-prefix scale is

\[
\exp(\Omega(n/\log n)).
\]

Polynomial connected prefixes, factorial arithmetic blocks of polynomial multiplicity, and any other per-layer family with only `exp(O((log n)^C))` connected choices cannot certify the full endpoint through this sequential engine.

## What is not proved

- The theorem does not show that the required connected prefixes fail to exist.
- It does not disprove `N2-ADD-120`.
- It does not upper-bound the complete connected component of the factorial core menu.
- It does not prove final-only quotient occupancy.
- It does not turn finite full-menu success into an asymptotic theorem.

The next exact structural question is whether the complete factorial core menus contain connected prefixes of the required `exp(Omega(n/log n))` scale uniformly across enough layers.