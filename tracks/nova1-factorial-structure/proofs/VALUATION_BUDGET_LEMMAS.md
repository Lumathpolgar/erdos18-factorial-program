# Proofs: Factorial Valuation Budget Lemmas

## N1-STR-003

Result label: **proved theorem**.

### Statement

For every prime `p <= n`,

\[
v_p(n!)=\sum_{j\ge1}\left\lfloor\frac n{p^j}\right\rfloor
=\frac{n-s_p(n)}{p-1}.
\]

Moreover,

\[
\frac n{p-1}-\lfloor\log_p n\rfloor-1
\le v_p(n!)\le\frac n{p-1}.
\]

If `p>sqrt(n)`, then `v_p(n!)=floor(n/p)`. Therefore every prime in

\[
B_q(n)=\{p:\max(\sqrt n,n/(q+1))<p\le n/q\}
\]

has valuation exactly `q`.

### Proof

The exponent of `p` in `n!` is the number of factors of `p` contributed by the integers from `1` to `n`. Multiples of `p` contribute at least one factor, multiples of `p^2` contribute one additional factor, and so on. Hence

\[
v_p(n!)=\sum_{j\ge1}\left\lfloor\frac n{p^j}\right\rfloor.
\]

Write the base-`p` expansion

\[
n=a_0+a_1p+\cdots+a_Lp^L,
\qquad 0\le a_i<p.
\]

Then

\[
\sum_{j\ge1}\left\lfloor\frac n{p^j}\right\rfloor
=\sum_{i=1}^La_i(1+p+\cdots+p^{i-1})
=\sum_{i=1}^La_i\frac{p^i-1}{p-1}
=\frac{n-s_p(n)}{p-1}.
\]

Since `s_p(n)>=1` for `n>=1`, the upper bound follows. Also the expansion has at most `floor(log_p n)+1` digits, each at most `p-1`, so

\[
s_p(n)\le(p-1)(\lfloor\log_p n\rfloor+1).
\]

Substitution gives the lower bound.

If `p>sqrt(n)`, then `p^2>n`, so every term with `j>=2` vanishes and

\[
v_p(n!)=\left\lfloor\frac np\right\rfloor.
\]

Finally, if `n/(q+1)<p<=n/q`, then

\[
q\le n/p<q+1,
\]

and therefore `floor(n/p)=q`. The additional restriction `p>sqrt(n)` ensures the one-term Legendre formula applies. This proves the quotient-band statement.

## Dyadic corollary

Result label: **proved theorem**.

If

\[
n/2^{k+1}<p\le n/2^k
\]

and `p>sqrt(n)`, then

\[
2^k\le n/p<2^{k+1}.
\]

Taking floors yields

\[
2^k\le v_p(n!)\le2^{k+1}-1.
\]

## Factorial-specific marker corollary

Result label: **proved theorem**.

For `p=2`, the digit-sum formula gives

\[
v_2(n!)=n-s_2(n)\ge n-\lfloor\log_2n\rfloor-1.
\]

For any fixed `A>0`,

\[
A(\log n)^2=o(n),
\]

so `A(log n)^2<=v_2(n!)` for all sufficiently large `n`.

For the lcm core,

\[
v_2(\operatorname{lcm}(1,\ldots,n))
=\max\{e:2^e\le n\}=\lfloor\log_2n\rfloor.
\]

Thus a construction requiring `Theta((log n)^2)` distinct 2-adic valuations is available in `n!` and unavailable in `L_n`.