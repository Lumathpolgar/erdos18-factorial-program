# Occupancy Model Comparison

## Common setup

Fix an integer `n>=1`, let

\[
D_n=\mathcal D(n!),\qquad X_n=\lfloor\sqrt{n!}\rfloor,
\]

and let `A_{1,n},...,A_{k,n}` be labeled finite subsets of `D_n`.

The legal final support is

\[
\Sigma^{\!*}(A_{1,n},\ldots,A_{k,n})
=
\left\{
\sum_{i=1}^k a_i:
 a_i\in A_{i,n}\cup\{0\},
 a_i=a_j\ne0\Rightarrow i=j
\right\}.
\]

A correction palette `C_n subseteq D_n` is reserved in advance and must be numerically disjoint from every main label. A width `R_n` is useful only if every integer `0<=r<=R_n` is representable by a bounded number of distinct elements of `C_n`.

No model below requires intermediate partial sums to contain intervals.

## Model 1: Uniform rainbow convolution

**Result label: heuristic.**

### Definition

For each label, let `mu_{i,n}` be the uniform probability measure on `A_{i,n} union {0}`. Let independent random variables `Y_i` have these laws and set

\[
S_n=\sum_{i=1}^{k}Y_i.
\]

The ordinary convolution is

\[
\mu_{1,n}*\cdots*\mu_{k,n}.
\]

### Exact structural assumptions

- `A_{i,n} subseteq D_n`.
- For ordinary convolution mass to imply a legal representation, the nonzero supports must be pairwise numerically disjoint:
  \[
  A_{i,n}\cap A_{j,n}=\varnothing\quad(i\ne j).
  \]
- If labels overlap, ordinary convolution must be replaced by a collision-free law on valid tuples.

### Term budget

Required:

\[
k\le K(\log n)^2.
\]

A zero choice costs no term.

### Support and numerical span

The full numerical support lies in

\[
0\le S_n\le M_n:=\sum_i\max A_{i,n}.
\]

Coverage of the factorial half-range requires `M_n>=X_n-R_n`.

### Lattice span

Let

\[
g_n=\gcd\bigcup_i A_{i,n}.
\]

If `g_n>1`, every attainable sum is divisible by `g_n`, so all other residue classes are inaccessible. A pointwise theorem for consecutive targets therefore requires `g_n=1`, or an explicit correction mechanism that covers every residue class.

### Theorem type sought

The useful conclusion is windowed and all-target:

\[
\forall x\in[R_n,X_n],\qquad
\mathbb P(S_n\in[x-R_n,x])>0.
\]

Pointwise positivity is stronger than necessary. Average, almost-all, or finite positivity is insufficient.

### Correction width

Any `R_n` accepted from Nova 1 is allowed, provided the correction palette represents every residual in `[0,R_n]` within the final term budget.

### Required input from Nova 1

- fixed pairwise disjoint divisor labels;
- exact `k`, support maxima, and total span;
- a disjoint correction palette and exact correction term cost;
- proof of divisor legality and endpoint reach.

### Required input from Nova 3

- lower bounds for every target-window probability under the fixed uniform law;
- maximal-atom and anti-concentration bounds;
- explicit lattice analysis;
- a uniform estimate strong enough near both ends of the half-range.

### Required finite falsification from Nova 4

- exact convolution or dynamic programming for feasible `n`;
- smallest empty target window;
- smallest collision witness if labels overlap;
- residue-class occupancy and minimum nonzero window mass.

### Principal weakness

A fixed law centers mass near one global mean. Endpoint windows may have exponentially smaller mass than central windows, so a central limit approximation does not provide uniform half-range occupancy.

## Model 2: Target-dependent exponential tilt

**Result label: conditional theorem route.**

### Definition

Fix positive base weights `w_{i,n}(a)` on `A_{i,n} union {0}`. For a real tilt parameter `theta`, define

\[
\mu_{i,n,\theta}(a)
=
\frac{w_{i,n}(a)e^{\theta a}}
{\sum_{b\in A_{i,n}\cup\{0\}}w_{i,n}(b)e^{\theta b}}.
\]

For a target `x`, choose `theta=theta_{n,x}` so that the mean of

\[
S_{n,x}=\sum_iY_{i,n,x}
\]

lies inside the requested correction window, preferably near `x-R_n/2`.

### Exact structural assumptions

- fixed labeled supports `A_{i,n}` independent of `x`;
- positive base weights on every allowed atom;
- pairwise numerical disjointness, or a collision-free global tuple law;
- the mean map `theta mapsto E_theta S` must contain the required target-centered mean range.

### Term budget

Required:

\[
k\le K(\log n)^2.
\]

The tilt changes probabilities, not the number of labels.

### Support and numerical span

The attainable support is independent of `theta` and remains inside `[0,M_n]`. Thus `M_n>=X_n-R_n` is still necessary.

### Lattice span

The lattice span is determined by the support, not by the tilt. The required condition is `g_n=1` or an explicit complete residue correction theorem.

### Collision assumptions

Positive ordinary convolution mass is legally extractable only when nonzero label supports are pairwise disjoint. Otherwise the distribution must assign zero mass to tuples with repeated nonzero numerical values.

### Theorem type sought

Uniform, windowed, and all-target:

\[
\forall x\in[R_n,X_n],\quad
\mathbb P_{\theta_{n,x}}(S_{n,x}\in[x-R_n,x])>0.
\]

The measure may depend on `x`; the labeled divisor families may not be silently changed with `x` unless the theorem explicitly allows that dependence.

### Correction width

The preferred theorem needs only positivity in a left correction window `[x-R_n,x]`.

### Required input from Nova 1

- pairwise disjoint fixed supports;
- a support range wide enough for all target means;
- a disjoint correction palette;
- structural conditions preventing a few labels from dominating the tilt.

### Required input from Nova 3

- existence and uniqueness or controlled selection of `theta_{n,x}`;
- variance lower bounds uniform in the declared bulk range;
- major-arc expansion and minor-arc decay under the tilt;
- an explicit local or window error smaller than an explicit reference window mass;
- separate endpoint analysis where the variance collapses.

### Required finite falsification from Nova 4

- solve the tilt equation exactly or with certified intervals;
- test variance collapse near `0` and `X_n`;
- enumerate all target windows;
- detect concentration spikes and inaccessible residues.

### Principal strength

The mean can be moved toward each requested target, avoiding the exponentially small fixed-law tails that obstruct uniform convolution.

### Principal weakness

For Bernoulli-type labels, the tilt parameter diverges and the variance tends to zero near support endpoints. Endpoint coverage cannot be inferred from a bulk local limit theorem without a separate structural regime.

## Model 3: Fixed-law Fourier or local-limit model

**Result label: conditional theorem route.**

### Definition

For a fixed product law, write

\[
\phi_n(t)=\mathbb E e^{itS_n}=\prod_i\phi_{i,n}(t),\qquad t\in[-\pi,\pi].
\]

Choose a major arc

\[
\mathfrak M_n=\{t:|t|\le T_n/\sigma_n\}
\]

and minor arc

\[
\mathfrak m_n=[-\pi,\pi]\setminus\mathfrak M_n,
\]

where `sigma_n^2=Var(S_n)`.

### Exact structural assumptions

- independent label variables with fixed laws;
- pairwise numerical disjointness or collision-free tuple support;
- lattice span exactly one;
- a Lindeberg-type maximal-step condition such as
  \[
  \max_i\|Y_i-\mathbb EY_i\|_\infty=o(\sigma_n);
  \]
- an explicit major-arc error and minor-arc integral bound.

### Term budget

Required `k<=K(log n)^2`.

### Support and numerical span

The support must reach `[0,X_n-R_n]`. A local theorem valid only for `|x-E S_n|<=o(sigma_n)` is not enough for the whole half-range.

### Lattice span and inaccessible residues

Span one is mandatory for pointwise consecutive-target statements. More generally, if the support lies in `b+gZ`, only that coset can carry mass.

### Theorem type sought

A short-window local theorem with explicit uniform error:

\[
\sup_{x\in\mathcal R_n}
\left|
\mathbb P(S_n\in[x-R_n,x])-G_{n,x}
\right|
\le\varepsilon_n,
\]

with a frozen positive reference mass `G_{n,x}` and `epsilon_n<G_{n,x}` for every target in the stated regime.

### Correction width

The Fourier kernel for a window of width `R_n` is

\[
K_{R_n}(t)=\sum_{r=0}^{R_n}e^{-irt},
\]

and satisfies

\[
|K_{R_n}(t)|\le\min(R_n+1,2/|t|)
\]

for `0<|t|<=pi`. Wider correction windows reduce the required local precision.

### Required input from Nova 1

- a fixed legal label system;
- a correction radius;
- control of maximal label size relative to total variance;
- exact support and span.

### Required input from Nova 3

- major arc: a frozen inequality comparing `phi_n(t)` with a lattice reference characteristic function;
- minor arc: a frozen integral bound weighted by the window kernel;
- variance bounds and endpoint ranges;
- no use of the phrase `Gaussian-like` without a numerical error smaller than the reference mass.

### Required finite falsification from Nova 4

- compute characteristic functions on certified meshes;
- test the declared minor-arc supremum or integral;
- compare exact probabilities with the reference approximation;
- locate the first target where approximation error exceeds main mass.

### Principal weakness

Without target-dependent centering, a local theorem is usually strongest only near one mean and is too weak in the tails or near endpoints.

## Model 4: Deterministic restricted-sumset model

**Result label: conditional theorem route.**

### Definition

Build the collision-free sumset recursively as a set operation,

\[
\Sigma^{\!*}(A_1,\ldots,A_k),
\]

but do not require any intermediate set to contain an interval. Use additive growth, entropy, inverse theorems, or direct covering arguments to prove final window intersection.

### Exact structural assumptions

Any invoked additive theorem must be restated for:

- subsets of the integers rather than a prime cyclic group unless reduction is proved;
- labeled one-per-family choices;
- forbidden repeated numerical values;
- the exact target interval and correction width.

### Term budget

Required `k<=K(log n)^2`, plus the correction palette cost.

### Support and numerical span

Necessary conditions include:

\[
\sum_i\max A_i\ge X_n-R_n
\]

and no gap in the final sumset larger than `R_n+1` over the target range.

### Lattice span and inaccessible residues

If the additive subgroup generated by all allowed nonzero values is `gZ` with `g>1`, deterministic growth cannot produce the missing residues.

### Collision assumptions

The sumset operation must explicitly delete tuples with repeated nonzero numerical values, or the labels must be pairwise disjoint.

### Theorem type sought

All-target final-window covering:

\[
\forall x\in[R_n,X_n],\qquad
\Sigma^{\!*}(A_1,\ldots,A_k)\cap[x-R_n,x]\ne\varnothing.
\]

### Correction width

The model can trade stronger deterministic growth for a wider correction palette, but every correction term and every main term must remain globally distinct.

### Required input from Nova 1

- explicit additive structure of the divisor labels;
- lower bounds on label sizes and sumset expansion;
- disjointness and correction palette;
- any small-doubling or progression structure needed by an inverse theorem.

### Required input from Nova 3

- divisor counts in the exact scales used by the deterministic construction;
- entropy or additive-energy bounds if invoked;
- exclusion of concentration in a proper progression.

### Required finite falsification from Nova 4

- exact restricted-sumset computation for feasible cases;
- smallest final support gap;
- additive energy and residue statistics;
- counterexample search for every proposed deterministic growth inequality.

### Principal strength

A deterministic theorem directly gives all-target coverage and avoids probabilistic extraction issues.

### Principal weakness

Standard sumset-growth theorems often ignore the labeled one-choice restriction, numerical collisions, or interval location. Their hypotheses may be harder to verify for factorial divisor packets than a tilted Fourier estimate.

## Comparative conclusion

The only model that directly addresses the fixed-law tail problem while preserving a final-only, globally coupled construction is Model 2, provided it is proved using the lattice-aware Fourier window criterion from Model 3 and supplemented by a deterministic endpoint or correction regime.
