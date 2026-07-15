# Toy Sufficient Conditions

All statements in this file are independent of factorial-specific structure.

## N2-ADD-108: Collision-free deterministic extraction

**Result label: proved theorem.**

### Statement

Let finite labels `A_1,...,A_k subseteq Z_{>0}` be pairwise numerically disjoint. Let `mu_i` be probability measures supported on `A_i union {0}`, and let the corresponding variables be independent. If

\[
\mathbb P\left(\sum_iY_i=x\right)>0,
\]

then `x` is a sum of at most `k` pairwise distinct positive integers, with at most one selected from each label.

### Proof

Positive mass means at least one tuple `(a_1,...,a_k)` in the finite product support has positive product weight and sum `x`. Delete its zero coordinates. Pairwise disjoint nonzero supports make the remaining values numerically distinct. `square`

### Collision-aware variant

If labels overlap, define

\[
\Omega_x^{\!*}
=
\left\{(a_1,...,a_k):
 a_i\in A_i\cup\{0\},
 \sum_i a_i=x,
 a_i=a_j\ne0\Rightarrow i=j
\right\}.
\]

If

\[
\sum_{a\in\Omega_x^{\!*}}\prod_i\mu_i(a_i)>0,
\]

then a legal representation exists. Ordinary convolution mass is not enough.

## N2-ADD-109: Union bound for a sampled catalogue

**Result label: proved theorem.**

### Statement

Let `T` be a finite target set of size `M`. Let one random valid rainbow sum `S` satisfy

\[
\mathbb P(S=x)\ge p_{\min}>0
\]

for every `x in T`. Draw `L` independent copies `S_1,...,S_L`. Then

\[
\mathbb P(\text{some }x\in T\text{ is never sampled})
\le M e^{-Lp_{\min}}.
\]

Consequently, if

\[
L>\frac{\log M}{p_{\min}},
\]

there exists a finite sampled catalogue containing a legal representation of every target.

### Proof

For fixed `x`, the miss probability is

\[
(1-\mathbb P(S=x))^L
\le(1-p_{\min})^L
\le e^{-Lp_{\min}}.
\]

Sum over all targets. `square`

### Window version

If each target window has probability at least `p_min`, the same proof gives a catalogue hitting every window.

### Limitation

The random selections must be defined on one shared probability space. This lemma does not convert target-dependent random families into one universal random construction.

## N2-ADD-110: Fourier comparison implies positive window mass

**Result label: proved theorem.**

### Statement

Let `P` and `Q` be probability distributions on `Z` with characteristic functions `phi` and `psi`. Let `I subseteq Z` be finite and define

\[
K_I(t)=\sum_{m\in I}e^{-imt}.
\]

If

\[
\Delta_I
:=
\int_{-\pi}^{\pi}
|\phi(t)-\psi(t)|\,|K_I(t)|\,dt
<2\pi Q(I),
\]

then `P(I)>0`.

### Proof

Fourier inversion gives

\[
P(I)-Q(I)
=
\frac{1}{2\pi}
\int_{-\pi}^{\pi}
(\phi(t)-\psi(t))\overline{K_I(t)}\,dt.
\]

Therefore

\[
|P(I)-Q(I)|\le\frac{\Delta_I}{2\pi}<Q(I),
\]

so `P(I)>0`. `square`

### Major-minor arc corollary

If `[-pi,pi]=M union m` and

\[
\int_M E_{\rm maj}(t)|K_I(t)|dt
+
\int_m E_{\rm min}(t)|K_I(t)|dt
<2\pi Q(I),
\]

where `|phi-psi|` is bounded by the displayed errors on the respective arcs, then `P(I)>0`.

## N2-ADD-111: Explicit discretized-Gaussian window lower bound

**Result label: proved theorem.**

### Statement

For `sigma>0` and `mu in R`, define

\[
q(m)=\frac{e^{-(m-\mu)^2/(2\sigma^2)}}
{Z},
\qquad
Z=\sum_{j\in Z}e^{-(j-\mu)^2/(2\sigma^2)}.
\]

For any nonempty finite interval `I subseteq Z`,

\[
Q(I)
\ge
\frac{|I|}{1+\sqrt{2\pi}\sigma}
\exp\left(
-\frac{\max_{m\in I}|m-\mu|^2}{2\sigma^2}
\right).
\]

### Proof

For every `m in I`, the numerator is at least the displayed exponential minimum. Also

\[
Z\le1+\int_{-\infty}^{\infty}e^{-u^2/(2\sigma^2)}du
=1+\sqrt{2\pi}\sigma.
\]

Summing over `I` proves the bound. `square`

### Use

This gives an explicit positive right side for N2-ADD-110. The Fourier error must be strictly smaller than `2pi` times this quantity.

## N2-ADD-112: Correction-window bridge

**Result label: proved theorem.**

### Statement

Let `D` be a set of legal positive integers. Let `C subseteq D` be a correction palette such that every integer `0<=r<=R` is a sum of at most `ell` distinct elements of `C`. Let `A_1,...,A_k subseteq D\C` be pairwise numerically disjoint and disjoint from `C`.

Assume that for every integer `R<=x<=X`,

\[
\Sigma^{\!*}(A_1,...,A_k)\cap[x-R,x]\ne\varnothing.
\]

Then every integer `0<=x<=X` is a sum of at most `k+ell` distinct elements of `D`.

### Proof

For `x<=R`, use the correction palette. For `x>R`, choose a main sum `s in [x-R,x]` and put `r=x-s`. Then `0<=r<=R`, so represent `r` using `C`. The main labels are pairwise disjoint and disjoint from `C`, hence all selected values are distinct. `square`

## N2-ADD-113: Pointwise mass lower bound sufficient for all targets

**Result label: proved theorem.**

### Statement

For fixed labels and a probability law supported only on legal rainbow tuples, if

\[
\inf_{0\le x\le X}\mathbb P(S=x)>0,
\]

then every target in `[0,X]` has a deterministic legal representation.

### Proof

Apply N2-ADD-108 target by target. No union bound is needed because the labels are fixed and positive mass itself is an existence certificate.

### Distinction

A union bound is needed only when proving that one random construction of the labels, one sampled catalogue, or one random auxiliary object works for all targets simultaneously.

## Combined reusable theorem

N2-ADD-110 plus N2-ADD-112 is the abstract engine selected for the preferred route: prove positive mass in every correction window by a strict lattice-Fourier comparison, then finish the residual deterministically with a disjoint palette.
