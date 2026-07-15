# Quotient Endpoint Support

## Theorem IDs

- `N1-STR-019`: odd factorial core is multiplicatively 3-dense
- `N1-STR-020`: repaired quotient support crosses the half-range endpoint
- `N1-RED-006`: deterministic coarse quotient contraction

## Result labels

All three statements in this file are **proved theorem**.

They do not prove the frozen polynomial-width quotient occupancy theorem.

## 1. Notation

Let

\[
N_n=n!,
\qquad
X_n=\lfloor\sqrt{n!}\rfloor,
\qquad
V_n=v_2(n!),
\]

and let

\[
O_n=\frac{n!}{2^{V_n}}
\]

be the odd part of `n!`.

For the marker-three construction define

\[
D_n=\frac{O_n}{3}.
\]

For `n>=3`, this is an integer because `v_3(n!)>=1`.

The repaired quotient layers are

\[
B_t(n)=
\left\{
2^{t-1}u:
 u\mid D_n,
 u\text{ odd},
 3\cdot2^{t-1}u\le X_n
\right\}.
\]

This is equivalent to the definition in `PREFERRED_ROUTE.md`.

## 2. Multiplicative density definition

A positive integer `D` is called multiplicatively `y`-dense when every real number `z` with

\[
1\le z\le D
\]

has a divisor `d|D` satisfying

\[
\frac zy<d\le z.
\]

Only the case `y=3` is used here.

## 3. Extension lemma

### Lemma N1-STR-019A

Let `D` be multiplicatively `y`-dense, let `p` be a prime satisfying

\[
p\le yD,
\]

and let `a>=1`. Then

\[
Dp^a
\]

is multiplicatively `y`-dense.

### Proof

Fix a real `z` with

\[
1\le z\le Dp^a.
\]

Let

\[
j=\min\bigl(a,\lfloor\log_p z\rfloor\bigr).
\]

Then `p^j<=z`.

If

\[
1\le z/p^j\le D,
\]

choose a divisor `d|D` with

\[
\frac{z}{yp^j}<d\le\frac z{p^j}.
\]

Then `p^j d|Dp^a` and

\[
\frac zy<p^jd\le z.
\]

It remains to consider

\[
z/p^j>D.
\]

This forces `j<a`. By the definition of `j`,

\[
z<p^{j+1}.
\]

Since `p<=yD`,

\[
z<p^{j+1}\le yp^jD.
\]

Therefore the divisor `p^jD` satisfies

\[
\frac zy<p^jD<z.
\]

This proves the extension lemma. `QED`

## 4. The odd factorial core is 3-dense

### Theorem N1-STR-019

For every integer

\[
n\ge6,
\]

the integer

\[
D_n=\frac{n!}{3\cdot2^{v_2(n!)}}
\]

is multiplicatively `3`-dense.

### Proof

Write the prime factorization

\[
D_n=3^{v_3(n!)-1}
\prod_{\substack{5\le p\le n\\p\text{ prime}}}
p^{v_p(n!)}.
\]

Because `n>=6`,

\[
v_3(n!)-1\ge1.
\]

The divisors of a power of `3` are consecutive powers of `3`, so

\[
3^{v_3(n!)-1}
\]

is multiplicatively `3`-dense.

We now adjoin the remaining prime powers in increasing prime order. At every stage the current prefix product is at least

\[
3^{v_3(n!)-1}.
\]

Also

\[
v_3(n!)\ge\left\lfloor\frac n3\right\rfloor.
\]

For every `n>=6`,

\[
n\le3^{\lfloor n/3\rfloor}.
\]

Indeed, writing `k=floor(n/3)>=2`, one has `n<=3k+2<=3^k`; the final inequality holds at `k=2` and propagates by induction.

Consequently every prime `p<=n` satisfies

\[
p\le n
\le3^{v_3(n!)}
=3\cdot3^{v_3(n!)-1}
\le3D_{\rm prefix}.
\]

The extension lemma therefore applies each time a prime power is adjoined. After all prime powers have been inserted, `D_n` is multiplicatively `3`-dense. `QED`

## 5. Range compatibility with the quotient layers

### Lemma N1-STR-020A

For every integer `n>=12`,

\[
2^{v_2(n!)}\le X_n.
\]

### Proof

Legendre's formula gives

\[
v_2(n!)\le n-1.
\]

The inequality

\[
4^{n-1}\le n!
\]

holds at `n=12` and then propagates by induction because every later factorial multiplier is at least `4`.

Hence

\[
2^{2v_2(n!)}
\le4^{n-1}
\le n!.
\]

Therefore

\[
2^{v_2(n!)}\le\sqrt{n!}.
\]

The left side is an integer, so it is at most `floor(sqrt(n!))=X_n`. `QED`

### Consequence

For `n>=12` and every `t>=1`, define

\[
Y_t=\frac{X_n}{3\cdot2^{t-1}}.
\]

Then

\[
Y_t\le D_n.
\]

Indeed,

\[
Y_t\le D_n
\Longleftrightarrow
X_n2^{V_n}
\le n!\,2^{t-1},
\]

and the latter follows from

\[
X_n\le\sqrt{n!},
\qquad
2^{V_n}\le\sqrt{n!}.
\]

## 6. Every admissible quotient layer reaches scale `X_n/9`

### Lemma N1-STR-020B

Let `n>=12`, and let `t` satisfy

\[
Y_t=\frac{X_n}{3\cdot2^{t-1}}\ge1.
\]

Then the quotient layer `B_t(n)` contains a divisor `b_t` satisfying

\[
\frac{X_n}{9}<b_t\le\frac{X_n}{3}.
\]

### Proof

By Theorem `N1-STR-019`, `D_n` is multiplicatively `3`-dense. Since

\[
1\le Y_t\le D_n,
\]

there is a divisor `u_t|D_n` with

\[
\frac{Y_t}{3}<u_t\le Y_t.
\]

Set

\[
b_t=2^{t-1}u_t.
\]

Then `b_t in B_t(n)`, and multiplication of the preceding inequalities by `2^{t-1}` gives

\[
\frac{X_n}{9}<b_t\le\frac{X_n}{3}.
\]

`QED`

## 7. Endpoint support theorem

### Theorem N1-STR-020

Let

\[
Q_n=\left\lfloor\frac{X_n}{3}\right\rfloor.
\]

For every integer `n>=12`, the repaired quotient rainbow sumset has maximum attainable value strictly larger than `Q_n`.

More precisely, there are pairwise numerically distinct legal choices

\[
b_1\in B_1(n),
\qquad
b_2\in B_2(n),
\qquad
b_3\in B_3(n)
\]

such that

\[
b_1+b_2+b_3>\frac{X_n}{3}\ge Q_n.
\]

Consequently, if

\[
S_n^{\max}
=
\max\Sigma_{\rm rb}(B_1(n),\ldots,B_{M_n}(n)),
\]

then

\[
S_n^{\max}\ge Q_n+1.
\]

### Proof

For `n>=12`, one has `X_n>=12`, so

\[
Y_t=\frac{X_n}{3\cdot2^{t-1}}\ge1
\]

for `t=1,2,3`.

Apply Lemma `N1-STR-020B` in these three layers. It gives

\[
b_t>\frac{X_n}{9}
\]

for each `t=1,2,3`. Therefore

\[
b_1+b_2+b_3>\frac{X_n}{3}.
\]

The terms are numerically distinct because their exact 2-adic valuations are `0`, `1`, and `2`. Thus their sum is a legal rainbow sum. Since it is an integer strictly exceeding `Q_n`, it is at least `Q_n+1`. `QED`

## 8. What endpoint theorem is closed

The theorem proves the exact structural endpoint-support condition

\[
S_n^{\max}
\ge
\left\lfloor\frac{X_n}{3}\right\rfloor-W_n
\]

with room to spare, because in fact

\[
S_n^{\max}>\left\lfloor\frac{X_n}{3}\right\rfloor.
\]

Therefore the target range in `N1-RED-005` does not extend beyond the total attainable support.

## 9. What endpoint theorem is not closed

The theorem does not prove that the interval

\[
[Q_n-W_n,Q_n]
\]

contains a rainbow sum.

The three-term witness may overshoot `Q_n`. Maximum support and downward endpoint occupancy are different statements.

This distinction is mandatory. The remaining endpoint window is part of the full quotient occupancy theorem.

## 10. Deterministic coarse contraction

### Theorem N1-RED-006

Fix `n>=12` and an integer

\[
0\le q\le Q_n.
\]

There is a deterministic one-choice-per-layer procedure using the quotient layers in increasing order such that, after `L` layers, the nonnegative residual `rho_L` satisfies

\[
\rho_L
<
\max\left\{
\left(\frac23\right)^Lq,
2^L
\right\}.
\]

### Proof

Start with `rho_0=q`.

At layer `t`, if

\[
\rho_{t-1}<2^{t-1},
\]

choose zero.

Otherwise apply multiplicative 3-density to

\[
Y=\frac{\rho_{t-1}}{2^{t-1}}.
\]

The upper bound `rho_{t-1}<=q<=X_n/3` ensures `Y<=D_n`, and the branch condition ensures `Y>=1`. Choose `u|D_n` with

\[
Y/3<u\le Y
\]

and select

\[
b_t=2^{t-1}u.
\]

Then

\[
\rho_{t-1}/3<b_t\le\rho_{t-1},
\]

so

\[
0\le\rho_t=\rho_{t-1}-b_t<\frac23\rho_{t-1}.
\]

An induction gives the displayed bound. `QED`

## 11. Limitation of coarse contraction

With

\[
M_n=\lceil16(\log n)^2\rceil,
\]

the proved bound is only

\[
\rho_{M_n}
<
\max\left\{
Q_n(2/3)^{M_n},
2^{M_n}
\right\}.
\]

This does not imply

\[
\rho_{M_n}\le W_n=O(n^{4\log2}).
\]

The first term still has logarithm of order `n log n`, while the contraction subtracts only order `(log n)^2` from that logarithm.

Thus multiplicative 3-density closes endpoint reach and supplies a deterministic coarse reduction, but it cannot by itself close the polynomial-width additive window.

## 12. Historical obstruction audit

The endpoint proof uses only three jointly legal layers and does not impose a partial interval-coverage invariant.

The coarse contraction theorem is sequential. It is recorded as a limited deterministic bound, not as the preferred proof architecture. No claim is made that it escapes a Phase 12P-type information ceiling.

## 13. Dependencies

- `PREFERRED_ROUTE.md`
- `proofs/MARKER_THREE_LATTICE_REPAIR.md`
- `proofs/VALUATION_BUDGET_LEMMAS.md`

## 14. Verification request

Nova 4 should independently verify for finite `n` that:

1. `D_n` has maximum consecutive divisor ratio at most `3`;
2. each of `B_1,B_2,B_3` contains an element in `(X_n/9,X_n/3]`;
3. the three selected terms are legal and distinct;
4. their sum exceeds `floor(X_n/3)`;
5. endpoint reach is not mistakenly reported as endpoint-window occupancy.
