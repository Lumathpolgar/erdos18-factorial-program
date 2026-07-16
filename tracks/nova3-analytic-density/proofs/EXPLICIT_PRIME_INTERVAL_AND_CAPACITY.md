# Explicit Prime Interval and Factorial Menu Capacity

## Imported request

- Sending branch: `nova/factorial-structure`
- Exact source commit: `fa11f4b2cb86a2dd791df189ada12757be791804`
- Source file: `tracks/nova1-factorial-structure/handoffs/TO_NOVA3.md`
- Imported structural theorem: `N1-STR-009` from `tracks/nova1-factorial-structure/proofs/HIGH_PRIME_MENU_CAPACITY.md`
- Responding theorem request: `N1-REQ-N3-001-A`

No statement from another branch is used without the branch and exact commit above.

## N3-ANA-010, explicit primes in the upper half interval

Result class: **proved theorem**.

### Statement

For every integer

\[
n\ge 120368,
\]

one has

\[
\pi(n)-\pi(n/2)\ge \frac{n}{3\log n}.
\]

Here `pi(x)` denotes the number of primes not exceeding the real number `x`, and every logarithm is natural.

### External theorem used

Pierre Dusart, *Estimates of Some Functions Over Primes without R.H.*, arXiv:1002.0442v1, Theorem 6.9, proves

\[
\pi(x)\ge \frac{x}{\log x-1}\qquad (x\ge 5393)
\]

and

\[
\pi(x)\le \frac{x}{\log x-1.1}\qquad (x\ge 60184).
\]

The exact source compatibility record is `N3-SRC-008` in `SOURCE_LEDGER.md`.

### Proof

Let

\[
L=\log n,
\qquad
b=\log 2+1.1.
\]

When `n>=120368`, both Dusart hypotheses hold at `n` and `n/2`, because

\[
n\ge5393,
\qquad
n/2\ge60184.
\]

Therefore

\[
\pi(n)-\pi(n/2)
\ge
n\left(
\frac1{L-1}-\frac1{2(L-b)}
\right).
\]

It remains to prove

\[
\frac1{L-1}-\frac1{2(L-b)}\ge\frac1{3L}.
\]

All denominators are positive. Multiplication by

\[
6L(L-1)(L-b)
\]

reduces the assertion to

\[
Q(L):=L^2+(5-4b)L-2b\ge0.
\]

Since `log 2<0.7`, one has `b<1.8`, and hence

\[
Q(L)>L^2-2.2L-3.6.
\]

The polynomial on the right is increasing for `L>=4` and equals `3.6` at `L=4`. Since `120368>e^4`, the desired inequality follows for every `n>=120368`.

This proves N3-ANA-010.

## N3-ANA-011, explicit address, menu, and profile capacity threshold

Result class: **proved theorem**.

### Statement

For every integer `n>=120368`, define

\[
X_n=\lfloor\sqrt{n!}\rfloor,
\qquad
V_n=v_2(n!),
\]

\[
r_n=\lceil4\log n\rceil,
\qquad
M_n=\lceil16(\log n)^2\rceil,
\qquad
e_t=r_n+t
\]

for `1<=t<=M_n`. Let

\[
U_t(n)=
\left\{
 u\in\mathbb Z_{>0}:
 u\mid n!,\ u\text{ odd},\ u>1,\ 2^{e_t}u\le X_n
\right\}.
\]

Then all of the following hold.

1. Every address is legal:
   \[
   e_{M_n}\le\lfloor V_n/2\rfloor-1.
   \]
2. Every menu satisfies
   \[
   |U_t(n)|
   \ge
   2^{\pi(n)-\pi(n/2)-1}-1
   \ge
   2^{n/(3\log n)-1}-1.
   \]
3. The formal profile-capacity inequality holds:
   \[
   \prod_{t=1}^{M_n}(|U_t(n)|+1)\,2^{r_n}\ge X_n+1.
   \]

Thus the three explicit thresholds requested by Nova 1 may all be taken equal to

\[
n_3=n_4=n_5=120368.
\]

### Proof of the address inequality

Legendre's identity gives

\[
V_n=v_2(n!)=n-s_2(n),
\]

where `s_2(n)` is the binary digit sum. Since

\[
s_2(n)\le\lfloor\log_2n\rfloor+1
\le\frac{\log n}{\log2}+1,
\]

we have

\[
V_n\ge n-\frac{\log n}{\log2}-1.
\]

Writing `L=log n`, the ceiling bounds give

\[
e_{M_n}=r_n+M_n
\le16L^2+4L+2.
\]

It is enough to prove the stronger inequality

\[
2e_{M_n}\le V_n-3.
\]

A sufficient condition is

\[
n\ge32L^2+\left(8+\frac1{\log2}\right)L+8.
\tag{1}
\]

At `n=120368`, we have `L<12` and `1/log2<2`, so the right side of (1) is less than

\[
32\cdot12^2+10\cdot12+8=4736<120368.
\]

The difference between the left side `n` and the right side of (1) has derivative

\[
1-\frac{64\log n+8+1/\log2}{n}.
\]

For `n>=120368`, this derivative is positive. Indeed, at the threshold, `log n<12` and `1/log2<2`, while the function

\[
n-64\log n-10
\]

is increasing for `n>64`. Therefore (1) holds for every `n>=120368`, proving the address inequality.

### Proof of the menu bound

By N3-ANA-010,

\[
m_n:=\pi(n)-\pi(n/2)\ge\frac{n}{3\log n}.
\]

The imported theorem `N1-STR-009`, at branch `nova/factorial-structure` and commit `fa11f4b2cb86a2dd791df189ada12757be791804`, proves that every legal address `e` satisfies

\[
|U_e(n)|\ge2^{m_n-1}-1.
\]

The address inequality just proved applies to every `e_t`, so

\[
|U_t(n)|
\ge2^{m_n-1}-1
\ge2^{n/(3\log n)-1}-1.
\]

### Proof of profile capacity

For `n>=120368`, the inequality `n>=12 log n` holds. Hence

\[
m_n-1
\ge
\frac{n}{3\log n}-1
\ge
\frac{n}{4\log n}.
\]

Because `M_n>=16(log n)^2`,

\[
M_n(m_n-1)\ge4n\log n.
\]

The imported menu theorem therefore gives

\[
\prod_{t=1}^{M_n}(|U_t(n)|+1)\,2^{r_n}
\ge
2^{M_n(m_n-1)+r_n}
\ge
2^{4n\log n}.
\]

On the other hand,

\[
X_n+1
\le\sqrt{n!}+1
\le2\sqrt{n!},
\]

and `n!<=n^n`, so

\[
\log_2(X_n+1)
\le1+\frac{n\log n}{2\log2}.
\]

Since `log2>1/2`,

\[
1+\frac{n\log n}{2\log2}
<1+n\log n
<4n\log n.
\]

Thus the profile-capacity inequality follows.

## Boundary and status audit

- The theorem is uniform for every integer `n>=120368`.
- No finite verification below `120368` is required or claimed.
- Floors and ceilings are included explicitly.
- The menus count exact odd divisors of `n!`, not smooth-number surrogates.
- The capacity inequality counts formal profiles only.
- No injectivity of profile sums is claimed.
- No additive window occupancy, maximum-gap theorem, or representation theorem follows.
- Nova 2 has separately disproved the first frozen occupancy construction by a power-of-two lattice obstruction. This capacity theorem does not repair that obstruction.

## Verification

Run

```text
python3 tracks/nova3-analytic-density/proofs/prime_interval_capacity_sanity.py
```

The verifier checks the exact prime count, exact 2-adic valuation, legal address condition, and conservative capacity inequality for every integer from `120368` through `1000000`. Those computations are a finite certificate only; the proof above supplies the asymptotic uniformity.