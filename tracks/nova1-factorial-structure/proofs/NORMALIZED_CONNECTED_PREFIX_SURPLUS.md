# Layer-Normalized Connected-Prefix Surplus

## Result

Result ID: `N1-STR-024`

Result label: **proved theorem**.

The factorial formulation of Erdős Problem 18 remains open. This theorem only normalizes the exact connected-prefix entropy requirement for the sequential carrier engine.

## Setup

Fix one parameter `n` and suppose the complete connected-core carrier executes `L>=1` layers. Let `K_t` be the number of positive odd cores in the complete zero-connected prefix at layer `t`.

Put

\[
P_n=\prod_{t=1}^{L}(1+K_t)
\]

and let

\[
Q_n=\left\lceil\frac{Y_n+1}{W_n+1}\right\rceil.
\]

By `N1-OBS-003`, successful sequential carrier coverage requires `P_n>=Q_n`.

Define

\[
\Gamma_n=\left(\frac{P_n}{Q_n}\right)^{1/L}
\]

and

\[
\Lambda_n=\frac{\log P_n-\log Q_n}{L}.
\]

## Theorem

For every exact carrier instance with `L>=1`:

1. `Gamma_n=exp(Lambda_n)`.
2. `P_n>=Q_n` if and only if `Gamma_n>=1`.
3. `P_n>=Q_n` if and only if `Lambda_n>=0`.
4. `Gamma_n` is the ratio between the geometric mean of the exact prefix factors and the per-layer geometric requirement:
   \[
   \Gamma_n=\frac{\left(\prod_{t=1}^{L}(1+K_t)\right)^{1/L}}{Q_n^{1/L}}.
   \]
5. `Gamma_n` is normalized for the number of executed layers. It does not require or imply monotonicity in `n`.

## Proof

The first and fourth statements follow from

\[
\exp\left(\frac{\log P_n-\log Q_n}{L}\right)=\left(\frac{P_n}{Q_n}\right)^{1/L}.
\]

Because `L` is positive, `x -> x^(1/L)` is strictly increasing on the positive reals. Hence

\[
P_n\ge Q_n\iff P_n/Q_n\ge1\iff\Gamma_n\ge1.
\]

The natural logarithm is strictly increasing, so

\[
P_n\ge Q_n\iff\log P_n-\log Q_n\ge0\iff\Lambda_n\ge0.
\]

This proves the theorem. `QED`

## Exact integer implementation

Since `Y_n` and `W_n` are integers,

\[
Q_n=\left\lfloor\frac{Y_n+W_n+1}{W_n+1}\right\rfloor.
\]

The verifier computes `P_n`, `Q_n`, and `floor(P_n/Q_n)` exactly. Decimal values of `Gamma_n` and `Lambda_n` are diagnostic renderings derived from those exact integers.

## Claim boundary

`Gamma_n>1` at finitely many values of `n` is a finite certificate that the necessary entropy gate is met at those values. It does not prove a uniform lower bound, asymptotic occupancy, the factorial half-range theorem, or Erdős Problem 18.
