# Proof: Fixed-Family Capacity Obstruction

## N1-OBS-002

Result label: **proved theorem**.

### Downward-window counting lemma

Let `S` be a finite set of attainable integer sums. Let `R>=0` and `X>=0` be integers. Suppose that for every integer `x` with

\[
0\le x\le X
\]

there exists `s in S` such that

\[
x-R\le s\le x.
\]

Then

\[
|S|(R+1)\ge X+1.
\]

### Proof

A fixed attainable sum `s` can serve only the targets

\[
x\in[s,s+R]\cap\mathbb Z,
\]

of which there are at most `R+1`. The union of these target sets over `s in S` contains all `X+1` integers from `0` through `X`. Therefore

\[
X+1\le\sum_{s\in S}(R+1)=|S|(R+1).
\]

No disjointness of the target intervals is needed.

## Rainbow-profile corollary

Result label: **proved theorem**.

Suppose a construction has `M` labeled layers, and layer `i` permits at most `c_i` nonzero choices plus the zero choice. If at most one element is selected from each layer, then the number of attainable sums satisfies

\[
|S|\le\prod_{i=1}^M(c_i+1).
\]

Consequently, downward-window coverage of `[0,X]` with width `R` requires

\[
\sum_{i=1}^M\log(c_i+1)
\ge\log(X+1)-\log(R+1).
\]

This is only a necessary condition. Collisions between profiles can make the actual attainable set smaller.

## Factorial half-range consequence

Result label: **disproved route**.

Let

\[
X_n=\lfloor\sqrt{n!}\rfloor.
\]

Stirling's formula gives

\[
\log X_n=\frac12\log(n!)+O(1)
=\frac12n\log n-\frac12n+O(\log n).
\]

Assume a construction has only

\[
M_n=O((\log n)^2)
\]

available binary choices, so `|S_n|<=2^{M_n}`, and a correction width

\[
R_n=\exp(O((\log n)^2)).
\]

Then

\[
\log(|S_n|(R_n+1))=O((\log n)^2),
\]

while

\[
\log(X_n+1)=\Theta(n\log n).
\]

Therefore

\[
|S_n|(R_n+1)<X_n+1
\]

for all sufficiently large `n`. Uniform downward-window coverage is impossible.

The same conclusion holds for a fixed ternary family with at most `3^{M_n}` profiles.

## Route decision

Result label: **disproved route**.

The original fixed-family versions of:

1. `N1-CON-001`, with one frozen divisor per 2-adic address;
2. `N1-CON-002`, with one frozen complement pair per slot;

cannot prove the factorial half-range theorem with only `O((log n)^2)` total available slots and quasipolynomial or smaller correction width.

A surviving architecture must distinguish:

- **available choices**, which must carry at least `Theta(n log n)` logarithmic profile capacity in total; and
- **selected terms**, which must remain `O((log n)^2)`.

Large menus per labeled layer can satisfy the necessary capacity inequality while preserving a polylogarithmic selected-term count.

## Capacity is not coverage

Even when

\[
\sum_i\log(c_i+1)
\ge\log(X_n+1)-\log(R_n+1),
\]

uniform coverage does not follow. The sum map may have collisions, shell gaps, or residue obstructions. The inequality is a mandatory gate, not a sufficient theorem.