# Parity-Span Count-to-Threshold Criterion

## Results

- `N2-ADD-124`: **proved theorem**, parity-span carrier lower bound.
- `N2-OBS-110`: **proved obstruction theorem**, optimality of count-threshold information.
- `N2-CMP-206`: **computational evidence**, finite parity-only deficit for `51<=n<=55`.

The factorial formulation of Erdos Problem 18 remains open. These results concern only the sequential marker-three carrier engine.

## Frozen inputs

- Nova 2 results: `N2-ADD-120`, `N2-ADD-122`, and `N2-ADD-123`.
- Nova 1 branch: `nova/factorial-structure`.
- Latest inspected head: `8c7ee8f64af56a8d082f1fa3adabb0b0309f6e27`.
- Exact finite inputs: `N1-FIN-006` through `N1-FIN-010`.

## Setup

At one executed layer put

\[
F=F_{t-1},\qquad s=2^{t-1},\qquad D=\left\lfloor\frac Fs\right\rfloor.
\]

Let

\[
0<u_1<u_2<\cdots<u_K=U
\]

be the positive odd cores in the complete zero-connected prefix. The layer update is

\[
F_t=F+sU.
\]

The exact expansion and utilization factors are

\[
1+a=\frac{F_t}{F}=1+\frac{sU}{F},
\qquad
b=\frac{1+a}{1+K}.
\]

## N2-ADD-124: parity-span lower bound

For every executed layer with `K>=1`,

\[
U\ge 2K-1.
\]

Consequently

\[
\eta=\frac{U}{KD}\ge\frac{2K-1}{KD}.
\]

Moreover,

\[
\frac{F_t}{F}
>
\frac{D+2K}{D+1},
\]

and

\[
b
>
\frac{D+2K}{(D+1)(K+1)}.
\]

For an `L`-layer carrier, define

\[
R_n=\frac{Y_n+1}{W_n+1}.
\]

The explicit count-to-threshold condition

\[
\prod_{t=1}^{L}
\frac{D_t+2K_t}{D_t+1}
\ge R_n
\]

is sufficient for exact endpoint coverage.

### Proof

The `K` positive cores are distinct positive odd integers. Their smallest possible ordered values are

\[
1,3,5,\ldots,2K-1.
\]

Hence `U>=2K-1`, proving the bound for `eta`.

Because `D=floor(F/s)`,

\[
F<s(D+1).
\]

Therefore

\[
\frac{sU}{F}>
\frac{U}{D+1}
\ge
\frac{2K-1}{D+1}.
\]

Adding one gives

\[
\frac{F_t}{F}=1+\frac{sU}{F}
>
1+\frac{2K-1}{D+1}
=
\frac{D+2K}{D+1}.
\]

Dividing by `K+1` proves the utilization bound. Multiplying the layer expansion bounds gives

\[
\frac{F_L}{W_n+1}
>
\prod_{t=1}^{L}
\frac{D_t+2K_t}{D_t+1}.
\]

If the displayed product is at least `R_n`, then `F_L>Y_n+1`, and hence the carrier reaches the required quotient endpoint. `QED`

## N2-OBS-110: optimality without factorial-specific spacing

The span bound `U>=2K-1` is exact. For every `K>=1` and every threshold `D>=2`, the abstract odd prefix

\[
1,3,5,\ldots,2K-1
\]

is connected under threshold `D` and attains equality.

The floor loss is also asymptotically sharp. Fix `D` and choose positive integers `s` with

\[
F=s(D+1)-1.
\]

Then `floor(F/s)=D` and

\[
\frac{sD}{F}\longrightarrow\frac{D}{D+1}
\]

as `s` tends to infinity.

Therefore no uniform theorem using only

- oddness of the cores,
- the connected-prefix count `K`, and
- the threshold `D`

can improve the N2-ADD-124 lower bound by a fixed positive factor. Any stronger lower bound must use additional factorial-divisor structure, such as an internal-span theorem, an average-gap theorem, or a distributional bound for divisors of the reserved odd factorial core.

### Proof

The consecutive gaps in the displayed prefix are `2`, so the prefix is connected for every `D>=2`, and its maximum is exactly `2K-1`. The formula for `F` gives

\[
D<\frac Fs<D+1,
\]

so the floor is `D`, while direct division yields the limiting floor factor. `QED`

## N2-CMP-206: exact finite diagnostic

Applying the parity-only product to the exact carrier rows for `51<=n<=55` gives the following sixth-root ratios against the required endpoint scale:

| `n` | parity-only endpoint ratio, sixth root |
|---:|---:|
| 51 | `0.0000257773398727324` |
| 52 | `0.0000185652131315783` |
| 53 | `0.0000139117330218277` |
| 54 | `0.00000997734788683994` |
| 55 | `0.00000761958530584015` |

Equivalently, the unrooted parity-only products fall below the exact endpoint requirements by factors between about `10^28` and `10^31` across this finite range.

The true exact endpoint factors are slightly above one, so factorial-specific internal spacing supplies essentially all of the missing expansion. This is finite computational evidence only and does not establish an asymptotic trend.

## Consequence

The sequential theorem target is now narrower:

1. count and parity alone are rigorously insufficient as a proof architecture;
2. the next valid input must lower-bound `U_t/(2K_t-1)` or, equivalently, the normalized average internal gap
   \[
   \eta_t=\frac{U_t}{K_tD_t};
   \]
3. a first external blocking gap remains non-identifying by `N2-OBS-109`;
4. final-only restricted-sumset and Fourier routes are unaffected.

## Claim boundary

This result does not prove or disprove uniform marker-three quotient occupancy, the factorial half-range theorem, or Erdos Problem 18.