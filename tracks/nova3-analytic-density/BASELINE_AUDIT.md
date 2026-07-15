# Nova 3 Baseline and Transfer Audit

## Audit metadata

- Track: Nova 3, Analytic Divisor Density
- Branch: `nova/analytic-density`
- Starting branch head: `c79cddee6e8940e27ff256c29a85a3fc93766f7b`
- Main head inspected: `68ace6c9c3b67636e298a406fee3bfe8e072741d`
- Merge base with main: `cd5576d4f7934e26e9d4ef3b065c2ad4cee36c67`
- Branch relation at startup: four commits ahead of the merge base and twelve commits behind `main`
- Audit date: 2026-07-15
- Status: `PROVED` for the elementary identities and transfer-direction statements below; `OPEN` where an archived source package is required.

The requested file `docs/HANDOFF_PROTOCOL.md` does not exist in the repository. The active protocol is `docs/CROSS_TRACK_HANDOFF_PROTOCOL.md`. This audit uses the active file and records the mismatch rather than silently changing the startup list.

## Frozen definitions and endpoint conventions

For a positive integer `N`,

\[
\mathcal D(N)=\{d\in\mathbb Z_{>0}:d\mid N\}.
\]

For an integer `x\ge 0`,

\[
\lambda_N(x)=\min\{|S|:S\subseteq\mathcal D(N),\ \sum_{d\in S}d=x\},
\]

with `lambda_N(x)=infinity` when no representation exists and `lambda_N(0)=0`.

For real `X\ge 1`,

\[
H_N(X)=\max_{0\le x<X,\ x\in\mathbb Z}\lambda_N(x).
\]

Thus

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
\]

covers every integer target

\[
0\le x\le \lfloor\sqrt{n!}\rfloor.
\]

For practical `N`, `h(N)=H_N(N)`.

## Current proof chain

The direct open node is

\[
\tag{INT-002}
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)=O((\log n)^2).
\]

The archived conditional Track B node is

\[
\tag{HIST-001}
\text{INT-002}\Longrightarrow h(n!)=O((\log n)^3).
\]

The implication remains conditional until reconstructed under the current endpoint convention. Nova 3 supplies only analytic inputs to INT-002. A divisor-count estimate, central limit theorem, or characteristic-function estimate is not itself an additive representation theorem.

## Exact factorial valuation model

Write

\[
N_n=n!,\qquad b_p(n)=v_p(n!)=\sum_{j\ge1}\left\lfloor\frac{n}{p^j}\right\rfloor.
\]

Every divisor of `n!` is represented uniquely by

\[
d(a)=\prod_{p\le n}p^{a_p},\qquad 0\le a_p\le b_p(n),
\]

and

\[
\log d(a)=\sum_{p\le n}a_p\log p.
\]

The exact number of admissible vectors is

\[
\tau(n!)=\prod_{p\le n}(b_p(n)+1).
\]

For every prime `p\le n`, summing the geometric series before inserting floor errors gives

\[
b_p(n)=\frac{n}{p-1}+O\!\left(\frac{\log n}{\log p}\right),
\]

where the displayed error is absolute and follows because at most `floor(log n/log p)` floor terms occur.

For `p>\sqrt n`, no higher prime power contributes and

\[
b_p(n)=\left\lfloor\frac np\right\rfloor.
\]

Hence, for every integer `k<\sqrt n`,

\[
\frac{n}{k+1}<p\le\frac nk\quad\Longrightarrow\quad b_p(n)=k.
\]

These are exact factorial-divisor statements, not smooth-number approximations.

## Phase 12L ceiling and transfer audit

The repository record freezes the Phase 12L orbit-step ceiling as

\[
S_{j+1}\le 2S_j\bigl(D_m(2S_j)+1\bigr),
\]

where the historical divisor-count function belongs to the `L_m` model. The record also states that the resulting maximum-gap greedy orbit needs superlogarithmically many steps and therefore cannot prove the historical `O(\log m)` local theorem.

### What transfers

- The logical distinction between an average divisor count and a maximum-gap guarantee transfers unchanged.
- Any greedy recurrence whose next reachable endpoint is bounded by the number of legal divisors below a current scale must be re-audited with the exact factorial count replacing `D_m`.
- A superlogarithmic lower bound proved solely from a general recurrence and an upper bound valid for the factorial divisor set would transfer after all parameters are translated.

### What does not transfer automatically

- The function `D_m` counts divisors of `L_m`, not divisors of `n!`.
- The valuation cap in `L_m` is `floor(log_p m)`, while the factorial cap is approximately `n/(p-1)` for fixed `p`.
- The Phase 12L asymptotic conclusion cannot be imported until its proof is reconstructed with factorial counts. The archived package containing the full proof is not present in this repository, so only the displayed ceiling and route conclusion are currently auditable.

## Phase 12P ceiling and transfer audit

The repository record freezes the Phase 12P conclusion as follows: smooth-number counting limits the number of useful choices per shared-core layer, and a one-choice sequential ladder needs

\[
\Omega(\log m\log\log m)
\]

layers in the historical `L_m` architecture.

### What transfers

- If a factorial layer `A` is proved to satisfy `A\subseteq B`, where `B` is a smooth or ultrafriable set covered by a known upper bound, then `|A|\le|B|` is legal.
- An upper bound on layer capacity can therefore obstruct a factorial sequential architecture when the containment and all scale parameters are explicit.
- The conclusion that one-choice sequential decoding may waste raw profile entropy is a valid design warning.

### What does not transfer automatically

- An upper bound for a smooth superset does not give a lower bound for factorial divisors.
- Factorial exponent multiplicity may permit nonseparable multi-coordinate or convolution mechanisms absent from the historical shared-core ladder.
- The exact Phase 12P small-divisor counting lemma and its constants are not reproduced in the repository record. They remain `OPEN` for source-package reconstruction and cannot be cited as a frozen factorial theorem.

## Forbidden inference directions

The following directions are invalid unless separately proved.

1. `factorial divisors subset smooth numbers` plus a smooth-number lower bound does not imply a factorial-divisor lower bound.
2. A smooth-number upper bound may upper-bound factorial divisors only after proving containment in the same parameter range.
3. A theorem about integers having some divisor in an interval does not count divisors of the fixed integer `n!` in that interval.
4. A theorem true for almost all integers does not imply anything for the sparse deterministic sequence `n!` without a sequence-specific argument.
5. `tau(n!)` large does not imply every logarithmic window contains a divisor.
6. Mean logarithmic spacing does not control the maximum logarithmic gap.
7. Weak convergence or a central limit theorem does not imply positivity in shrinking windows.
8. A nonlattice statement does not by itself give quantitative minor-arc decay.
9. Numerical agreement for finite `n` does not establish a uniform asymptotic range.
10. A bound for divisors of `L_m` does not transfer to `n!`, or conversely, merely because one integer divides another for selected parameter choices.

## Independent first-checkpoint requirement

The first analytic checkpoint will not depend on progress from Nova 1 or Nova 2. It will establish exact moment formulas, a local-count ceiling, a non-Gaussian limit obstruction for the full uniform-divisor model, and a corrected high-prime Gaussian route. Incoming construction-specific requests can then be matched to these proved facts.
