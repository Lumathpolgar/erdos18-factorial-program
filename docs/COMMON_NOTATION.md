# Common Mathematical Notation

## Core functions

For a positive integer `N`, let

\[
\mathcal D(N)=\{d\in\mathbb Z_{>0}:d\mid N\}.
\]

For an integer `x >= 0`, define the distinct-divisor representation length

\[
\lambda_N(x)=\min\left\{|S|:S\subseteq\mathcal D(N),\ \sum_{d\in S}d=x\right\},
\]

with `lambda_N(x)=infinity` if no representation exists. The empty set represents `0`, so `lambda_N(0)=0`.

For real `X >= 1`, define

\[
H_N(X)=\max_{0\le x<X,\ x\in\mathbb Z}\lambda_N(x).
\]

When `N` is practical, define

\[
h(N)=H_N(N).
\]

Every document that uses a different endpoint convention must state it explicitly and prove the conversion.

## Factorial notation

- `N_n = n!`
- `X_n = floor(sqrt(n!))`
- `v_p(n!) = sum_{j>=1} floor(n/p^j)`
- `D_n = D(n!)`, the positive divisor set of `n!`
- `tau(n!) = |D_n|`

## Historical lcm notation

- `L_m = lcm(1,2,...,m)`
- The historical local target was
  \[
  H_{L_m}(\lfloor L_m^{1/3}\rfloor+1)=O(\log m).
  \]
- This target is not assumed in the direct factorial program.

## Representation objects

A **packet** is a finite set of divisors intended to contribute at most a bounded number of selected terms.

A **layer** is a family `A_i subseteq D_n` from which a construction selects according to a stated rule.

A **rainbow sum** chooses at most one element from each of several labeled layers.

A **correction palette** is a reserved divisor family used to repair a bounded residual interval. Palette terms must remain distinct from all main construction terms.

A **window occupancy statement** asserts that every interval `[x-R,x]` or `[x,x+R]` in a stated range contains an attainable sum. The orientation and endpoints must be explicit.

## Asymptotic conventions

- All logarithms are natural unless stated otherwise.
- Constants implied by `O`, `Omega`, `Theta`, and `o` are absolute unless dependencies are displayed.
- “For large `n`” means there exists an explicitly quantified or recoverable threshold `n_0`.
- A result uniform in `x` must state the full range of `x`.

## Evidence labels

Every claimed result must carry exactly one status:

- `PROVED`
- `CONDITIONAL`
- `FINITE_CERTIFICATE`
- `COMPUTATIONAL_EVIDENCE`
- `HEURISTIC`
- `DISPROVED`
- `OPEN`

## Distinctness rule

All sums in `lambda_N`, `H_N`, and `h(N)` use distinct positive divisors. Any construction using labeled copies of the same numerical divisor is invalid unless it proves that the numerical values are distinct.
