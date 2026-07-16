# Proof: High-Prime Menu Capacity

## N1-STR-009

Result label: **proved theorem**.

### Setup

Write

\[
n!=2^{V_n}O_n,
\]

where `O_n` is odd. Let

\[
\mathcal P_n=\{p\text{ prime}:n/2<p\le n\},
\qquad
m_n=|\mathcal P_n|,
\]

and let

\[
P_n=\prod_{p\in\mathcal P_n}p.
\]

Every prime in `P_n` has valuation one in `n!`, so `P_n` is a squarefree odd divisor of `O_n`.

For an integer address `e` satisfying

\[
0\le e\le\lfloor V_n/2\rfloor-1,
\]

define the full admissible odd-core menu

\[
U_e(n)=
\{u:u\mid O_n,\ u>1,\ 2^eu\le X_n\},
\qquad
X_n=\lfloor\sqrt{n!}\rfloor.
\]

### Statement

If `m_n>=1`, then

\[
|U_e(n)|\ge2^{m_n-1}-1.
\]

### Proof

The `2^{m_n}` subset products of the primes in `P_n` are exactly the positive divisors of the squarefree number `P_n`. The involution

\[
d\longmapsto P_n/d
\]

pairs divisors below `sqrt(P_n)` with divisors above `sqrt(P_n)`. Since `P_n` is squarefree and greater than one, it is not a square, so no divisor equals `sqrt(P_n)`. Therefore exactly `2^{m_n-1}` divisors of `P_n` are below `sqrt(P_n)`.

Because `P_n|O_n`,

\[
\sqrt{P_n}\le\sqrt{O_n}.
\]

The address bound gives

\[
2^e\sqrt{O_n}
\le2^{\lfloor V_n/2\rfloor-1}\sqrt{O_n}
<\frac12\sqrt{n!}\sqrt2.
\]

For all `n!>=4`, the right side is at most `floor(sqrt(n!))=X_n`. Hence every divisor `d<=sqrt(P_n)` satisfies

\[
2^ed\le X_n.
\]

All such `d` are odd divisors of `O_n`. Removing the unit divisor leaves at least

\[
2^{m_n-1}-1
\]

members of `U_e(n)`.

## Capacity corollary for addressed layers

Result label: **proved theorem**.

Let `e_1,...,e_M` be distinct addresses, each at most `floor(V_n/2)-1`, and use the full menus `U_{e_t}(n)`. Then the formal rainbow profile count satisfies

\[
P_{\rm profiles}
=\prod_{t=1}^M(|U_{e_t}(n)|+1)
\ge2^{M(m_n-1)}.
\]

This is a lower bound on formal profiles, not on distinct sums.

## Asymptotic capacity corollary

Result label: **conditional theorem** pending an explicit audited prime-interval constant.

Assume that for all `n>=n_0`,

\[
m_n=\pi(n)-\pi(n/2)\ge\frac{n}{3\log n}.
\]

Take

\[
M_n=\lceil16(\log n)^2\rceil,
\qquad
r_n=\lceil4\log n\rceil.
\]

Then, for all sufficiently large `n`,

\[
\log P_{\rm profiles}
\ge M_n(m_n-1)\log2
>\log(X_n+1)-r_n\log2.
\]

Thus the necessary profile-capacity gate passes with room to spare.

The conclusion does not prove additive occupancy because many profiles may produce the same sum or leave large gaps.