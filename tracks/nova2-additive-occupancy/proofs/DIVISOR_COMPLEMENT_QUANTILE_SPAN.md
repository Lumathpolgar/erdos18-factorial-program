# Divisor Complement Quantile Span

## Results

- `N2-ADD-125`: **proved theorem**, exact divisor-complement order-statistic identity.
- `N2-ADD-126`: **proved theorem**, lower-tail quantile and median carrier bounds.
- `N2-CMP-207`: **computational evidence**, exact median-hybrid deficit for `51<=n<=55`.

The factorial formulation of Erdos Problem 18 remains open. These results concern only the sequential marker-three carrier engine.

## Frozen inputs

- Nova 2 results: `N2-ADD-120` through `N2-ADD-124`.
- Nova 1 branch: `nova/factorial-structure`.
- Exact inspected head: `8c7ee8f64af56a8d082f1fa3adabb0b0309f6e27`.
- Exact finite inputs: `N1-FIN-006` through `N1-FIN-010`.

## Reserved odd core

Put

\[
C_n=\frac{n!}{3\,2^{v_2(n!)}}.
\]

Let its positive divisors be

\[
1=c_1<c_2<\cdots<c_{\tau_n}=C_n,
\qquad
\tau_n=\tau(C_n).
\]

At an executed carrier layer, the complete zero-connected prefix contains exactly the first `K_t` positive divisors, so

\[
U_t=c_{K_t}.
\]

Write

\[
J_t=\tau_n-K_t
\]

for the number of positive divisors outside the connected prefix.

## N2-ADD-125: exact complement-tail identity

For every executed layer,

\[
U_t\,c_{J_t+1}=C_n.
\]

Equivalently,

\[
U_t=\frac{C_n}{c_{\tau_n+1-K_t}}
\]

and the factorial span-amplification factor is exactly

\[
A_t
=\frac{U_t}{2K_t-1}
=\frac{C_n}{(2K_t-1)c_{\tau_n+1-K_t}}.
\]

### Proof

The divisor-complement map

\[
d\longmapsto \frac{C_n}{d}
\]

is an order-reversing involution on the positive divisors of `C_n`. Therefore

\[
c_i c_{\tau_n+1-i}=C_n
\]

for every `i`. Substituting `i=K_t` proves the identity. `QED`

## N2-ADD-126: lower-tail quantile criterion

For `B>=1`, define the exact lower-tail divisor count

\[
L_n(B)=\#\{d:d\mid C_n,\ d\le B\}.
\]

If

\[
L_n(B)\ge J_t+1,
\]

then

\[
c_{J_t+1}\le B
\]

and hence

\[
U_t\ge\frac{C_n}{B},
\qquad
A_t\ge\frac{C_n}{(2K_t-1)B}.
\]

Thus any certified lower-tail divisor family immediately yields a factorial-specific carrier-span lower bound.

### Median corollary

If

\[
K_t\ge \left\lfloor\frac{\tau_n}{2}\right\rfloor+1,
\]

then

\[
U_t\ge\left\lceil\sqrt{C_n}\right\rceil.
\]

Indeed, at least half of the divisor list lies at or below `sqrt(C_n)`, with the central divisor equal to `sqrt(C_n)` when `C_n` is a square.

### Hybrid layer bound

Define

\[
S_t=
\max\left(
2K_t-1,
\mathbf 1_{K_t>\tau_n/2}\left\lceil\sqrt{C_n}\right\rceil
\right).
\]

Then `U_t>=S_t`. With

\[
D_t=\left\lfloor\frac{F_{t-1}}{2^{t-1}}\right\rfloor,
\]

one has

\[
\frac{F_t}{F_{t-1}}
>
\frac{D_t+1+S_t}{D_t+1}.
\]

Consequently the explicit hybrid condition

\[
\prod_{t=1}^{L}
\frac{D_t+1+S_t}{D_t+1}
\ge
\frac{Y_n+1}{W_n+1}
\]

is sufficient for exact endpoint coverage.

### Proof

The quantile claim follows from `N2-ADD-125`. For the median claim, the complementary order statistic `c_{J_t+1}` lies at or below `sqrt(C_n)`, so `U_t=C_n/c_{J_t+1}` lies at or above `sqrt(C_n)`. The parity bound `U_t>=2K_t-1` is `N2-ADD-124`.

Finally, from `D_t=floor(F_{t-1}/2^{t-1})`,

\[
F_{t-1}<2^{t-1}(D_t+1).
\]

Therefore

\[
\frac{F_t}{F_{t-1}}
=1+\frac{2^{t-1}U_t}{F_{t-1}}
>
1+\frac{S_t}{D_t+1},
\]

which is the displayed layer factor. Multiplication proves the endpoint criterion. `QED`

## N2-CMP-207: exact finite median-hybrid diagnostic

For every `51<=n<=55`, the exact fifth and sixth carrier layers satisfy

\[
K_t>\frac{\tau_n}{2}.
\]

Using the parity bound on layers one through four and the stronger square-root bound on layers five and six gives:

| `n` | median-hybrid endpoint ratio, sixth root | unrooted `log10` ratio |
|---:|---:|---:|
| 51 | `0.000145487587879522` | `-23.023044339` |
| 52 | `0.000123906257046752` | `-23.441440572` |
| 53 | `0.0000907853071519960` | `-24.251906596` |
| 54 | `0.0000892960011035230` | `-24.295007937` |
| 55 | `0.0000740382055592177` | `-24.783264694` |

The complement-median input improves the parity-only product by roughly `10^4.5` through `10^5.9`, but the resulting lower bound still misses the exact endpoint requirement by roughly `10^23` through `10^25`.

This is finite computational evidence only. No asymptotic trend is asserted.

## Consequence

The sequential rank-three frontier is now exact:

1. `N2-ADD-125` converts span amplification into the complementary lower-tail order statistic `c_{tau_n+1-K_t}`;
2. parity, prefix count, first external blocking gaps, and median symmetry are insufficient as complete proof inputs;
3. the next valid theorem must certify substantially deeper lower-tail divisor counts `L_n(B)`, or directly upper-bound the complementary quantile;
4. final-only restricted-sumset and Fourier routes remain unaffected.

## Claim boundary

These results do not prove or disprove uniform marker-three quotient occupancy, the factorial half-range theorem, or Erdos Problem 18.