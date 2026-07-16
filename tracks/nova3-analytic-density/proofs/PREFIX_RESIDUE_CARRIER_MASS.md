# Prefix Residue Carrier Mass

## Scope

This file continues the exact odd-lattice normalized marker-three law from `N3-ANA-025` and the dyadic factorization from `N3-ANA-026` through `N3-ANA-028`.

Imported heads:

- Nova 1: `nova/factorial-structure@1b81ec74f907d57d520bcf6c51f2e6e71f0474a7`
- Nova 2: `nova/additive-occupancy@591e4e51a00627ac48c0aa05fae4a955dccb9d14`

The factorial half-range theorem and Erdős Problem 18 remain open.

## Frozen notation

For `n>=120368`, let

\[
M_n=\lceil16(\log n)^2\rceil,
\qquad
m_n=\max\{m\le n:m\text{ odd}\},
\qquad
k_n=\frac{m_n+1}{2},
\]

\[
L_n=m_n(2^{M_n}-1).
\]

For every post-prefix target `q`, the transformed common tilt is

\[
\widetilde\lambda_{n,q}=2\lambda_{n,q}.
\]

By `N3-ANA-020`,

\[
-\frac{16M_n\log L_n}{L_n}
<\widetilde\lambda_{n,q}<
\frac{32(n\log n+\log14)}{2^{M_n}}.
\]

Define the absolute envelope

\[
\delta_n
=
\max\left\{
\frac{16M_n\log L_n}{L_n},
\frac{32(n\log n+\log14)}{2^{M_n}}
\right\}.
\]

Then

\[
|\widetilde\lambda_{n,q}|<\delta_n
\]

uniformly over the exact post-prefix range.

The transformed supports contain:

1. `0` and `1` in the first coordinate;
2. for every `t>=2`, the states
   \[
   0,
   \qquad
   2^{t-2},
   \qquad
   3\cdot2^{t-2};
   \]
3. more generally, for every odd `1<=u<=m_n`, the state `2^{t-2}u` in coordinate `t>=2`.

## N3-ANA-029: exact low-state interval carrier

Result class: **proved theorem**.

For an integer `j>=1`, define the low-state prefix carrier by allowing

\[
\widetilde Z_1\in\{0,1\}
\]

and, for every `2<=t<=j`,

\[
\widetilde Z_t
\in
\{0,2^{t-2},3\cdot2^{t-2}\}.
\]

Let `\mathcal S_j` be the set of all resulting ordinary integer sums.

Then

\[
\mathcal S_j
=
\{0,1,\ldots,3\cdot2^{j-1}-2\}.
\]

Consequently, the low-state carrier maps surjectively onto every residue class modulo `2^j`.

### Proof

For `j=1`,

\[
\mathcal S_1=\{0,1\}
=
[0,3\cdot2^0-2]\cap\mathbb Z.
\]

Assume

\[
\mathcal S_j=[0,3\cdot2^{j-1}-2]\cap\mathbb Z.
\]

At the next coordinate the allowed additions are

\[
0,
\qquad
2^{j-1},
\qquad
3\cdot2^{j-1}.
\]

Writing `a=2^{j-1}`, the three translated intervals are

\[
[0,3a-2],
\qquad
[a,4a-2],
\qquad
[3a,6a-2].
\]

They overlap and their union is

\[
[0,6a-2]
=
[0,3\cdot2^j-2].
\]

This proves the interval identity by induction. Since the interval contains `0,1,...,2^j-1`, every residue modulo `2^j` occurs. `QED`

## Exact carrier event

Let `\mathcal C_{n,q,j}` be the event that the first `j` transformed coordinates use only the preceding low-state carrier choices.

This event is residue complete modulo `2^j`, but its probability must be compared with the full tilted menus.

Define the safe carrier depth

\[
R_n
=
\min\left(
M_n,
\left\lfloor
2+\log_2\frac{1}{\delta_nm_n}
\right\rfloor
\right).
\]

For every `2<=t<=R_n`,

\[
\delta_nm_n2^{t-2}\le1.
\]

Also

\[
R_n=M_n-O(\log n).
\]

Indeed, the positive part of `\delta_n` has logarithm

\[
-M_n\log2+O(\log n),
\]

while the negative part is smaller on the same exponential scale. Therefore

\[
\log_2(\delta_nm_n)=-M_n+O(\log n).
\]

## N3-ANA-030: uniform low-carrier mass collapse

Result class: **proved theorem**.

For every post-prefix target `q` and every

\[
1\le j\le R_n,
\]

one has

\[
P_{\widetilde\lambda_{n,q}}
(\mathcal C_{n,q,j})
\le
\frac{2e^2}{k_n}
\left(
\frac{3e^2}{k_n+1}
\right)^{j-1}.
\]

In particular, at the maximal safe depth,

\[
\log
P(\mathcal C_{n,q,R_n})
=-\Theta((\log n)^3)
\]

uniformly over the exact post-prefix target range.

### Proof for the first coordinate

The first transformed support contains the consecutive block

\[
0,1,\ldots,k_n-1.
\]

Because `R_n>=2` in the stated range,

\[
\delta_nm_n\le1.
\]

Every weight in this block is at least `e^{-1}`, while the two carrier weights at `0` and `1` are each at most `e`. Therefore

\[
P(\widetilde Z_1\in\{0,1\})
\le
\frac{2e}{k_ne^{-1}}
=
\frac{2e^2}{k_n}.
\]

### Proof for later coordinates

Fix `2<=t<=j<=R_n` and put

\[
a_t=2^{t-2}.
\]

The transformed support contains the zero state and all `k_n` positive states

\[
a_tu,
\qquad
u=1,3,\ldots,m_n.
\]

The safe-depth inequality gives

\[
|\widetilde\lambda_{n,q}|a_tm_n\le1.
\]

Thus every one of these `k_n+1` denominator weights is at least `e^{-1}`.

The three carrier states are `0`, `a_t`, and `3a_t`. Since `m_n>=3`, their absolute tilted exponents are also at most one, so each numerator weight is at most `e`.

Hence

\[
P\left(
\widetilde Z_t
\in
\{0,a_t,3a_t\}
\right)
\le
\frac{3e}{(k_n+1)e^{-1}}
=
\frac{3e^2}{k_n+1}.
\]

Independence of the transformed coordinates gives the product bound. Since

\[
R_n=\Theta((\log n)^2)
\]

and

\[
\log k_n=\Theta(\log n),
\]

the logarithm of the product is `-Theta((log n)^3)`. `QED`

## N3-ANA-031: support surjectivity is not a quantitative mixing theorem

Result class: **proved route obstruction**.

The exact implication

> every residue modulo `2^j` has a legal prefix representation

cannot be promoted to

> the transformed prefix law is quantitatively spread modulo `2^j`

using only the residue-complete low-state carrier.

The carrier is exactly surjective by `N3-ANA-029`, but its entire tilted probability is at most

\[
\frac{2e^2}{k_n}
\left(
\frac{3e^2}{k_n+1}
\right)^{j-1}
\]

through `M_n-O(log n)` scales.

Therefore the next Fourier theorem must control the residue distribution of the full odd-core menus, or identify another carrier with non-negligible tilted mass. Formal residue support alone is insufficient.

This theorem does not assert that the complete transformed prefix law is concentrated. It rules out one specific proof mechanism: deriving quantitative prefix mixing solely from the fixed low-state residue carrier.

## Numerical scale

At `n=120368`:

\[
M_n=2190,
\qquad
R_n=2149,
\]

and

\[
P(\mathcal C_{n,q,R_n})
<10^{-7379.36}.
\]

The corresponding selected bounds are computational evidence only. The symbolic product inequality is the theorem.

## Route consequence

The transformed dyadic problem now has three separate levels:

1. exact global dyadic resonance is absent;
2. exact prefix residue support is complete;
3. quantitative prefix residue mass remains open.

The active theorem must estimate full-menu residue weights or full-prefix characteristic functions near the dyadic ladder. It cannot substitute support coverage for probability mixing.

## Claim boundary

This checkpoint does not prove:

- quantitative full-prefix residue spreading;
- transformed local-window positivity;
- the strict weighted Fourier inequality;
- target-local collision control;
- quotient occupancy;
- the factorial half-range theorem;
- Erdős Problem 18.