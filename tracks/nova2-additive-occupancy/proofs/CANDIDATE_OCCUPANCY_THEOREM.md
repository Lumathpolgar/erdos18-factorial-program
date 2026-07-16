# N2-ADD-114: Fourier-Correction Occupancy Theorem

## Status

**Result label: conditional theorem.**

The abstract implication below is proved. Its factorial-specific hypotheses remain open.

## Theorem statement

There exist fixed constants `K,L>0` and `n_0>=1`. For every integer `n>=n_0`, let

\[
X_n=\lfloor\sqrt{n!}\rfloor
\]

and suppose the following data are given.

### Structural data

1. An integer `k_n` satisfying
   \[
   k_n\le K(\log n)^2.
   \]
2. Finite labeled families
   \[
   A_{1,n},...,A_{k_n,n}\subseteq\mathcal D(n!)
   \]
   whose nonzero numerical supports are pairwise disjoint.
3. A correction palette
   \[
   C_n\subseteq\mathcal D(n!)
   \]
   numerically disjoint from every `A_{i,n}`.
4. An integer correction radius `R_n>=0` such that every integer
   \[
   0\le r\le R_n
   \]
   is a sum of at most
   \[
   L(\log n)^2
   \]
   distinct elements of `C_n`.
5. Full additive span:
   \[
   \gcd\bigcup_{i=1}^{k_n}A_{i,n}=1.
   \]

### Target-dependent probabilistic data

For every integer target

\[
R_n<x\le X_n,
\]

let `mu_{i,n,x}` be a probability measure supported on `A_{i,n} union {0}`. Let independent random variables `Y_{i,n,x}` have these laws and define

\[
S_{n,x}=\sum_{i=1}^{k_n}Y_{i,n,x}.
\]

Let

\[
I_{n,x}=[x-R_n,x]\cap\mathbb Z
\]

and let

\[
\phi_{n,x}(t)=\mathbb E e^{itS_{n,x}}.
\]

For each such `x`, suppose there exists a probability distribution `Q_{n,x}` on `Z`, with characteristic function `psi_{n,x}`, satisfying

\[
Q_{n,x}(I_{n,x})>0
\]

and the strict weighted Fourier inequality

\[
\int_{-\pi}^{\pi}
|\phi_{n,x}(t)-\psi_{n,x}(t)|
\left|\sum_{m\in I_{n,x}}e^{-imt}\right|dt
<2\pi Q_{n,x}(I_{n,x}).
\tag{F}
\]

Then every integer

\[
0\le x\le X_n
\]

is a sum of at most

\[
(K+L)(\log n)^2
\]

distinct divisors of `n!`. Consequently,

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
\le (K+L)(\log n)^2
\]

for every `n>=n_0`.

## Proof

Fix `n>=n_0`.

### Targets inside the correction range

If `0<=x<=R_n`, hypothesis 4 gives a representation of `x` using at most `L(log n)^2` distinct divisors from `C_n`.

### Targets above the correction range

Fix `R_n<x<=X_n`. Write

\[
K_{n,x}(t)=\sum_{m\in I_{n,x}}e^{-imt}.
\]

Fourier inversion for integer-valued probability distributions gives

\[
\mathbb P(S_{n,x}\in I_{n,x})
=
\frac{1}{2\pi}
\int_{-\pi}^{\pi}
\phi_{n,x}(t)\overline{K_{n,x}(t)}dt
\]

and

\[
Q_{n,x}(I_{n,x})
=
\frac{1}{2\pi}
\int_{-\pi}^{\pi}
\psi_{n,x}(t)\overline{K_{n,x}(t)}dt.
\]

Therefore

\[
\left|
\mathbb P(S_{n,x}\in I_{n,x})-Q_{n,x}(I_{n,x})
\right|
\le
\frac{1}{2\pi}
\int_{-\pi}^{\pi}
|\phi_{n,x}(t)-\psi_{n,x}(t)|
|K_{n,x}(t)|dt.
\]

By `(F)`, the right side is strictly smaller than `Q_{n,x}(I_{n,x})`. Hence

\[
\mathbb P(S_{n,x}\in I_{n,x})>0.
\]

The product support is finite, so there exists a tuple

\[
(a_1,...,a_{k_n}),
\qquad
 a_i\in A_{i,n}\cup\{0\},
\]

with positive product weight and sum

\[
s=\sum_i a_i\in I_{n,x}.
\]

Delete the zero coordinates. Because the nonzero label supports are pairwise numerically disjoint, the remaining `a_i` are distinct divisors of `n!`. Their number is at most `k_n`.

Set

\[
r=x-s.
\]

Since `s in [x-R_n,x]`, we have `0<=r<=R_n`. Hypothesis 4 represents `r` using at most `L(log n)^2` distinct elements of `C_n`. The correction palette is numerically disjoint from all main labels, so combining the main and correction selections preserves global distinctness.

The total number of selected divisors is at most

\[
k_n+L(\log n)^2
\le(K+L)(\log n)^2.
\]

This holds for every integer `0<=x<=X_n`, proving the theorem. `square`

## Effective constants

The implication is effective once `K`, `L`, `n_0`, the label families, the correction palettes, and the strict inequality `(F)` are effective.

## Boundary treatment

- Lower endpoint: covered directly by the correction palette.
- Upper endpoint `X_n`: included because the target range in `(F)` is `R_n<x<=X_n`.
- Finite exceptions `n<n_0`: not handled by this theorem and must be discharged separately.

## Distinctness mechanism

Distinctness follows from two explicit disjointness conditions:

1. `A_{i,n} cap A_{j,n}=emptyset` for `i!=j`;
2. `C_n cap A_{i,n}=emptyset` for every `i`.

No labeled duplicate is accepted.

## Lattice assumption

Span one is included as a mandatory structural diagnostic. The proof of the implication uses only `(F)`, but a factorial application is not accepted without proving span one or replacing it by a complete residue-correction theorem. This prevents the Fourier hypothesis from hiding an inaccessible-residue failure.

## Major-minor arc sufficient form

Let

\[
[-\pi,\pi]=\mathfrak M_{n,x}\cup\mathfrak m_{n,x}.
\]

It is sufficient to prove explicit functions `E_maj` and `E_min` such that

\[
|\phi_{n,x}(t)-\psi_{n,x}(t)|\le E_{\rm maj}(t)
\quad(t\in\mathfrak M_{n,x}),
\]

\[
|\phi_{n,x}(t)-\psi_{n,x}(t)|\le E_{\rm min}(t)
\quad(t\in\mathfrak m_{n,x}),
\]

and

\[
\int_{\mathfrak M_{n,x}}E_{\rm maj}(t)|K_{n,x}(t)|dt
+
\int_{\mathfrak m_{n,x}}E_{\rm min}(t)|K_{n,x}(t)|dt
<2\pi Q_{n,x}(I_{n,x}).
\]

## What is not claimed

- The factorial structural hypotheses are not yet proved.
- The Fourier inequality `(F)` is not yet proved for a factorial divisor model.
- This theorem does not claim that one fixed untilted law works for every target.
- This theorem does not derive `(F)` from a central limit theorem without an explicit error bound.
- This theorem does not handle `n<n_0`.

## Dependencies

- N2-ADD-108: collision-free deterministic extraction.
- N2-ADD-110: Fourier comparison implies positive window mass.
- N2-ADD-112: correction-window bridge.

## Next proof obligation

Construct fixed factorial labels and a correction palette for which a target-dependent exponential tilt satisfies the major-minor arc sufficient form uniformly over the bulk target range, with deterministic endpoint coverage outside that range.
