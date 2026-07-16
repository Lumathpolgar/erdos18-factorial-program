# Factorial Block Carrier Theorem and Ceiling

## Result IDs

- `N1-STR-021`: proved theorem
- `N1-DIS-006`: disproved route

## Imported additive criterion

This proof uses the carrier-block framework accepted by Nova 2 from:

- branch: `nova/additive-occupancy`
- exact commit: `b15278e21f91e0e188b1c7c3e9a10e58a1db20fe`
- theorem: `N2-ADD-119`
- conditional theorem: `N2-ADD-120`
- proof: `tracks/nova2-additive-occupancy/proofs/MARKER_THREE_CARRIER_BLOCK_REDUCTION.md`

Nova 2's outcome for the marker-three handoff is `ACCEPTED_WITH_RESTRICTIONS`. The present file identifies an explicit legal family of large core blocks and proves that this family alone cannot reach the factorial endpoint within the frozen layer budget.

## Frozen notation

Let

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

\[
W_n=\left\lfloor\frac{2^{r_n}-3}{3}\right\rfloor.
\]

The quotient core menu in layer `t` is

\[
U_t(n)=
\{u\ge1:u\text{ odd},\ 3u\mid n!,\ 2^{t-1}u\le Y_n\}.
\]

For an integer `k>=3`, write

\[
O_k=\frac{k!}{2^{v_2(k!)}},
\qquad
A_k=\frac{O_k}{3}.
\]

The integer `A_k` is odd because `O_k` is odd and contains at least one factor of `3`.

Let

\[
m_{n,k}=\max\{m\le n-k:m\text{ odd}\}.
\]

## N1-STR-021: factorial arithmetic core blocks

### Statement

For every pair of integers

\[
n\ge6,
\qquad
3\le k<n,
\]

the odd cores

\[
A_k,\ 3A_k,\ 5A_k,\ldots,m_{n,k}A_k
\]

all satisfy

\[
3A_kj\mid n!
\]

for odd `1<=j<=m_{n,k}`.

Consequently, whenever

\[
2^{t-1}A_km_{n,k}\le Y_n,
\]

the full arithmetic block

\[
\mathcal B_{n,k,t}
=
\{A_kj:1\le j\le m_{n,k},\ j\text{ odd}\}
\]

is contained in `U_t(n)`.

If a carrier threshold `D` satisfies

\[
D\ge2A_k,
\]

then the ordered set

\[
\{0\}\cup\mathcal B_{n,k,t}
\]

is connected from zero under the rule that consecutive gaps may not exceed `D`, and its connected endpoint is at least

\[
A_km_{n,k}.
\]

### Proof

Because

\[
3A_k=O_k,
\]

we have

\[
3A_kj=O_kj.
\]

The odd part `O_k` divides `k!`. Since `j<=n-k`, the integer `j` divides `(n-k)!`. Therefore

\[
O_kj\mid k!(n-k)!.
\]

Also

\[
k!(n-k)!\mid n!
\]

because

\[
\frac{n!}{k!(n-k)!}=\binom nk
\]

is an integer. Hence

\[
3A_kj\mid n!.
\]

All cores in the displayed block are odd. The layer cutoff gives membership in `U_t(n)`.

The first gap from `0` to `A_k` is `A_k`. Every later consecutive gap is exactly `2A_k`. Thus `D>=2A_k` connects the entire block from zero. `QED`

## Block-only carrier recursion

Consider any carrier proof that, at each layer `t`, uses only one arithmetic block of the form above.

Let `E_0=0`. At layer `t`, put

\[
a_t=2^{t-1},
\qquad
F_{t-1}=E_{t-1}+W_n+1,
\]

and let the exact Nova 2 threshold be

\[
D_t=\left\lfloor\frac{F_{t-1}}{a_t}\right\rfloor.
\]

Suppose a block parameter `k_t` is chosen with

\[
2A_{k_t}\le D_t
\]

and with its scaled endpoint below `Y_n`. The strongest endpoint certified from that one block is

\[
E_t
=
E_{t-1}+a_tA_{k_t}m_{n,k_t}.
\]

Since `m_{n,k_t}<=n` and `2A_{k_t}<=D_t`,

\[
a_tA_{k_t}m_{n,k_t}
\le
\frac n2a_tD_t
\le
\frac n2F_{t-1}.
\]

Therefore

\[
F_t=E_t+W_n+1
\le
\left(1+\frac n2\right)F_{t-1}.
\]

Induction gives the exact ceiling

\[
E_{M_n}+W_n+1
\le
(W_n+1)
\left(1+\frac n2\right)^{M_n}.
\]

## N1-DIS-006: factorial arithmetic blocks cannot reach the endpoint

### Statement

For every integer

\[
n\ge120368,
\]

the block-only carrier ceiling satisfies

\[
(W_n+1)
\left(1+\frac n2\right)^{M_n}
<Y_n.
\]

Hence no proof that applies `N2-ADD-119` using only one factorial arithmetic block per layer can certify marker-three quotient occupancy through `Y_n` with the frozen budget `M_n`.

### Proof

Since

\[
r_n\le4\log n+1,
\]

we have

\[
W_n+1\le2^{r_n}<2n^3.
\]

Also

\[
M_n\le16(\log n)^2+1
\]

and

\[
\log\left(1+\frac n2\right)\le\log n.
\]

Therefore

\[
\log\left((W_n+1)
\left(1+\frac n2\right)^{M_n}\right)
<16(\log n)^3+5\log n.
\]

For `n>=120368`, at least `n/2` factors of `n!` are at least `n/2`, so

\[
\sqrt{n!}\ge
\left(\frac n2\right)^{n/4}.
\]

The endpoint satisfies

\[
Y_n\ge\frac14\sqrt{n!}
\]

throughout this range. Since `log n>10`,

\[
\log(n/2)\ge\frac9{10}\log n.
\]

Thus

\[
\log Y_n
\ge
\frac{9n}{40}\log n-\log4.
\]

At `n=120368`,

\[
\frac{9n}{40}>27000
\]

while

\[
16(\log n)^2+5<2400.
\]

The function `n/(log n)^2` is increasing for `n>e^2`, so the strict separation persists for every larger `n`. Therefore

\[
16(\log n)^3+5\log n
<
\frac{9n}{40}\log n-\log4
\le
\log Y_n.
\]

Exponentiating proves the claim. `QED`

## Interpretation

The factorial blocks are genuine large legal subfamilies. They improve the trivial small-core chain and give an exact deterministic lower-bound engine.

However, their carrier growth is at most

\[
\exp(O((\log n)^3)),
\]

whereas

\[
Y_n=\exp(\Theta(n\log n)).
\]

The gap is asymptotic and decisive for this restricted proof engine.

This does not disprove:

- the full connected component of the complete menu `U_t(n)`;
- interactions among multiple different blocks inside one layer;
- final-only restricted-sumset arguments;
- target-dependent Fourier methods;
- the marker-three construction itself.

It disproves only the route that uses one translated factorial arithmetic block per layer as the entire carrier mechanism.

## Next structural requirement

Any successful carrier proof must exploit core families whose connected reach per layer is substantially larger than `n` times the carrier threshold. Otherwise the frozen `O((log n)^2)` layer budget cannot bridge the factorial scale.