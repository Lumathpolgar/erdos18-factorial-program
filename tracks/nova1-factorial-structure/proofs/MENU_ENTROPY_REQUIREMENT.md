# Proof: Menu Entropy Requirement

## N1-STR-008

Result label: **proved theorem**.

### Statement

Let `X_n=floor(sqrt(n!))`. Consider a rainbow construction with `M_n` labeled layers. Layer `i` has at most `c_i(n)` nonzero choices, and a legal representation selects at most one term from each layer. Suppose a correction mechanism has residual width `R_n`, and every integer `0<=x<=X_n` lies within downward distance `R_n` of an attainable rainbow sum.

Then

\[
\sum_{i=1}^{M_n}\log(c_i(n)+1)
\ge
\log(X_n+1)-\log(R_n+1).
\]

If, for fixed constants `A,B>0`,

\[
M_n\le A(\log n)^2
\]

and

\[
R_n\le n^B,
\]

then for all sufficiently large `n`,

\[
\frac1{M_n}
\sum_{i=1}^{M_n}\log(c_i(n)+1)
\ge
\frac{n}{3A\log n}.
\]

Consequently the geometric mean of the layer-state counts satisfies

\[
\left(
\prod_{i=1}^{M_n}(c_i(n)+1)
\right)^{1/M_n}
\ge
\exp\left(\frac{n}{3A\log n}\right),
\]

and at least one layer satisfies

\[
c_i(n)+1
\ge
\exp\left(\frac{n}{3A\log n}\right).
\]

### Proof

The number of formal rainbow profiles is at most

\[
P_n=\prod_{i=1}^{M_n}(c_i(n)+1).
\]

The number of distinct attainable sums is no larger than `P_n`. By the downward-window counting lemma,

\[
P_n(R_n+1)\ge X_n+1.
\]

Taking logarithms gives the first inequality.

Stirling's formula gives

\[
\log(n!)=n\log n-n+O(\log n),
\]

so

\[
\log(X_n+1)
=\frac12n\log n-\frac12n+O(\log n).
\]

Also `log(R_n+1)<=B log n+O(1)`. Therefore, for sufficiently large `n`,

\[
\log(X_n+1)-\log(R_n+1)
\ge\frac13n\log n.
\]

Dividing by `M_n<=A(log n)^2` yields

\[
\frac1{M_n}
\sum_i\log(c_i(n)+1)
\ge\frac{n}{3A\log n}.
\]

Exponentiating gives the geometric-mean statement. The maximum layer-state count is at least the geometric mean, proving the final claim.

## Corollary: polynomial menus are impossible

Result label: **disproved route**.

If every layer has at most `n^C` choices for a fixed constant `C`, then

\[
\sum_{i=1}^{M_n}\log(c_i(n)+1)
=O((\log n)^3),
\]

which is `o(n log n)`. Therefore no `O((log n)^2)`-layer rainbow system with polynomial-size menus and polynomial correction width can cover the factorial half-range.

## Corollary: analytic density must be near divisor-entropy scale

Result label: **proved theorem** as a necessary condition.

Any surviving Nova 1 route with `O((log n)^2)` selected layers must ask Nova 3 for menus of exponential size in `n/log n` on average. Requests for merely polynomially many divisors per layer are structurally insufficient before any additive analysis begins.

This theorem does not assert that menus of the required size exist in the required scale windows, nor that they yield additive coverage.