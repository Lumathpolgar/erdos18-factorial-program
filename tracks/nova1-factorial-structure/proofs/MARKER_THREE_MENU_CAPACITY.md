# Explicit Capacity for Marker-Three Menus

## Imported analytic theorem

This proof imports the exact prime-interval result from:

- branch: `nova/analytic-density`
- exact commit: `e60069f797af878711e7a9d4abb1fb6188a1f724`
- theorem: `N3-ANA-010`
- response handoff: `N3-HO-N1-002`

The imported theorem states that, for every integer

\[
n\ge120368,
\]

\[
\pi(n)-\pi(n/2)\ge\frac{n}{3\log n}.
\]

Nova 3's old address-capacity theorem is not imported unchanged. The proof below redoes the menu translation for `N1-CON-003`.

## Frozen notation

Let

\[
X_n=\lfloor\sqrt{n!}\rfloor,
\qquad
M_n=\lceil16(\log n)^2\rceil.
\]

Let

\[
P_n=\{p\text{ prime}:n/2<p\le n\},
\qquad
h_n=|P_n|.
\]

For `1<=t<=M_n`, the repaired core menu is

\[
U_t(n)=
\left\{
 u\ge1:
 u\text{ odd},\ 3u\mid n!,\ 3\cdot2^{t-1}u\le X_n
\right\}.
\]

## N1-STR-018: marker-three high-prime menu bound

Result label: **proved theorem**.

For every integer `n>=120368` and every `1<=t<=M_n`,

\[
|U_t(n)|\ge2^{h_n-1}
\ge2^{n/(3\log n)-1}.
\]

### Proof

Define

\[
H_n=\prod_{p\in P_n}p.
\]

Every prime in `P_n` occurs to exponent exactly one in `n!`. It is larger than `3`, so every subset product of `P_n` is odd and coprime to `3`. Therefore, for every divisor `u|H_n`,

\[
3u\mid n!.
\]

Pair every subset `S subseteq P_n` with its complement. Their products multiply to `H_n`, so at least one member of each complementary pair has product at most `sqrt(H_n)`. Unique factorization makes all subset products distinct. Hence at least

\[
2^{h_n-1}
\]

subset products satisfy

\[
u\le\sqrt{H_n}.
\]

It remains to check the numerical cutoff for the largest address `t=M_n`.

Every prime in `(n/2,n]` divides the central binomial coefficient

\[
\binom{n}{\lfloor n/2\rfloor}.
\]

Thus

\[
H_n\le\binom{n}{\lfloor n/2\rfloor}\le2^n,
\]

and

\[
\sqrt{H_n}\le2^{n/2}.
\]

Also,

\[
n!\ge(n/2)^{\lfloor n/2\rfloor},
\]

so

\[
X_n\ge(n/2)^{\lfloor n/2\rfloor/2}-1.
\]

For every `n>=120368`, the elementary inequalities

\[
M_n\le n/10
\]

and

\[
3\cdot2^{n/10+n/2}
<
(n/2)^{\lfloor n/2\rfloor/2}-1
\]

hold. The first is verified at `120368` and remains true because `16(log n)^2/n` decreases in this range. The second follows after taking logarithms, since the left logarithm is at most

\[
\log3+0.6n\log2,
\]

while the right main logarithm is at least

\[
\frac{n-1}{4}\log(n/2),
\]

which is larger at `n=120368` and has larger derivative thereafter.

Consequently,

\[
3\cdot2^{M_n-1}\sqrt{H_n}\le X_n.
\]

Therefore every one of the `2^(h_n-1)` small complementary subset products belongs to every `U_t(n)`. The imported prime-interval theorem gives the second inequality. `QED`

## N1-CAP-002: explicit profile-capacity gate

Result label: **proved theorem**.

For every integer `n>=120368`, the repaired marker-three layer system satisfies the necessary counting-capacity inequality

\[
2^{r_n}
\prod_{t=1}^{M_n}(|U_t(n)|+1)
\ge X_n+1,
\]

where

\[
r_n=\lceil4\log n\rceil.
\]

### Proof

For `n>=120368`,

\[
h_n-1
\ge
\frac{n}{3\log n}-1
\ge
\frac{n}{4\log n}.
\]

By N1-STR-018,

\[
\log_2\prod_{t=1}^{M_n}(|U_t(n)|+1)
\ge M_n(h_n-1)
\ge4n\log n.
\]

On the other hand,

\[
X_n+1\le2\sqrt{n!}
\]

and `n!<=n^n`, so

\[
\log_2(X_n+1)
\le1+\frac n2\log_2n
=1+\frac{n\log n}{2\log2}
< n\log n
\]

throughout the stated range. Therefore the rainbow profile entropy alone exceeds the target entropy, even before adding the `r_n` palette bits. `QED`

## Interpretation

The formal capacity gate is now closed for `N1-CON-003` with explicit threshold

\[
n_0=120368.
\]

This does not prove:

- injectivity of rainbow profiles;
- numerical sumset size;
- quotient maximum-gap control;
- endpoint occupancy;
- the half-range theorem.

Capacity is necessary but not sufficient.
