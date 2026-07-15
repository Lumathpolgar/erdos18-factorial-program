# Proof: Complement-Pairing Lemma

## N1-STR-007

Result label: **proved theorem**.

### Statement

Let `Q=R^2` be a square divisor of `n!`. Let `X>=R`. Let `z_1,...,z_m` be distinct divisors of `R` satisfying

\[
1<z_i\le X/R.
\]

Define

\[
a_i=R/z_i,
\qquad
b_i=Rz_i.
\]

Then:

1. `a_i` and `b_i` are positive divisors of `n!`;
2. `a_i<R<b_i<=X`;
3. the `2m` integers `a_1,...,a_m,b_1,...,b_m` are pairwise distinct;
4. selecting at most one of `0,a_i,b_i` from each pair uses at most `m` distinct divisors;
5. if a fixed prime `q` divides `R` and does not divide any `z_i`, then every `a_i` and `b_i` is divisible by `q`.

### Proof

Because `z_i|R`, the quotient `R/z_i` is an integer. For every prime `p`, write

\[
v_p(R)=A_p,
\qquad
v_p(z_i)=u_{p,i},
\qquad 0\le u_{p,i}\le A_p.
\]

Then

\[
v_p(a_i)=A_p-u_{p,i},
\qquad
v_p(b_i)=A_p+u_{p,i}.
\]

Both exponents lie between `0` and `2A_p=v_p(Q)`, so both numbers divide `Q`, hence divide `n!`.

Since `z_i>1`,

\[
a_i=R/z_i<R<Rz_i=b_i.
\]

The upper hypothesis gives `b_i<=X`.

If `a_i=a_j`, then `R/z_i=R/z_j`, so `z_i=z_j` and `i=j`. If `b_i=b_j`, then `Rz_i=Rz_j`, so again `i=j`. A low term cannot equal a high term because every low term is less than `R` and every high term is greater than `R`. Thus all `2m` terms are pairwise distinct.

A three-choice selection uses no more than one term from each pair, so it uses at most `m` divisors, all drawn from a pairwise distinct family.

Finally, if `q|R` and `q` does not divide `z_i`, then

\[
v_q(a_i)=v_q(R)>=1,
\qquad
v_q(b_i)=v_q(R)>=1.
\]

Hence every pair term is divisible by `q`.

## Marked multi-cloud corollary

Result label: **proved theorem**.

For clouds indexed by `j`, suppose

\[
Q_j=R_j^2\mid n!,
\]

all multipliers are odd, and the values

\[
E_j=v_2(R_j)
\]

are pairwise distinct. Then every term in cloud `j` has 2-adic valuation `E_j`. Therefore terms from different clouds are numerically distinct. If additionally `5|R_j` and every multiplier is coprime to `5`, then every cloud term is divisible by `5` and cannot equal a pure power of `2` from the binary correction palette.

## Restricted-sum identity

Result label: **proved theorem**.

If a selection chooses either the low or the high term from a specified subcollection `T` of pairs, then relative to choosing all low terms in `T`, the sum changes by a subset sum of

\[
\Delta_i=b_i-a_i
=R\left(z_i-z_i^{-1}\right),
\]

where the final expression is shorthand for the integer `Rz_i-R/z_i`.

This identity is exact. It does not imply that the increments cover an interval.

## Falsification note

Result label: **disproved route** for any construction that assumes complement pairing alone yields density.

The lemma proves legality, range, distinctness, and term cost only. It does not prove:

- that suitable multipliers exist at all required scales;
- that the increments have gcd one;
- that restricted subset sums avoid residue obstructions;
- that shell gaps are absent;
- that every target is approximated within the correction width.