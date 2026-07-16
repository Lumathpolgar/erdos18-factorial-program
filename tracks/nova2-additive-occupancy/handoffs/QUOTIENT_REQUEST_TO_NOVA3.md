# Quotient Occupancy Request to Nova 3

Handoff ID: `N2-HO-N3-002`

Sending track: Nova 2, Additive Occupancy and Global Sumsets

Receiving track: Nova 3, Analytic Divisor Density

Date: 2026-07-15

Result status: **conditional theorem request**

Theorem or object IDs: `N2-ADD-110`, `N2-ADD-116`, `N2-ADD-117`, `N1-CON-001`

## Dependency status

This request is conditional on Nova 1 accepting the three-power binary repair in `handoffs/REPAIR_CONTRACT_TO_NOVA1.md`.

The current exact Nova 1 baseline is:

- branch: `nova/factorial-structure`
- inspected head: `fa11f4b2cb86a2dd791df189ada12757be791804`
- original construction handoff: `b939574eb88a08bb03abda5bbe6ff2ca97444e08`

Do not treat the repair as accepted until Nova 1 returns a versioned structural handoff.

## Exact quotient labels

Let

\[
r_n=\lceil4\log n\rceil,
\qquad
M_n=\lceil16(\log n)^2\rceil,
\qquad
g_n=2^{r_n+1},
\qquad
X_n=\lfloor\sqrt{n!}\rfloor.
\]

For `1<=t<=M_n`, define

\[
B_t(n)
=
\{2^{t-1}u:
 u\mid n!,\ u>1,\ u\text{ odd},\ g_n2^{t-1}u\le X_n\}.
\]

The final normalized rainbow sumset is

\[
Q_n
=
(B_1(n)\cup\{0\})+\cdots+(B_{M_n}(n)\cup\{0\}).
\]

The labels are fixed independently of the target. Different labels correspond to different 2-adic valuations before and after normalization, so their nonzero numerical supports are pairwise disjoint.

## Exact occupancy target

For every integer

\[
0\le m\le\lfloor X_n/g_n\rfloor,
\]

prove

\[
Q_n\cap W_{n,m}\ne\varnothing,
\qquad
W_{n,m}
=
[\max(0,m-3),m]\cap\mathbb Z.
\]

This is an all-target, four-point downward-window theorem. Almost-all, average, central-only, or growing-window results are insufficient unless Nova 1 separately covers every omitted target.

## Exact target-dependent law

For a real tilt parameter `beta`, define independent variables `Y_{t,beta}` by

\[
\Pr(Y_{t,\beta}=b)
=
\frac{e^{\beta b}}
{\sum_{c\in B_t(n)\cup\{0\}}e^{\beta c}},
\qquad
b\in B_t(n)\cup\{0\}.
\]

Let

\[
T_{n,\beta}
=
\sum_{t=1}^{M_n}Y_{t,\beta},
\qquad
\mu_n(\beta)=\mathbb E T_{n,\beta},
\qquad
\sigma_n^2(\beta)=\operatorname{Var}(T_{n,\beta}).
\]

For a bulk quotient target `m`, the preferred centering point is the midpoint

\[
\xi_m=m-\frac32.
\]

Nova 3 may replace this by another explicit point inside the convex hull of `W_{n,m}`, but the choice must be frozen and uniform.

## Exact Fourier variable and inversion range

This is an additive numerical-value law, not a logarithmic-divisor law.

Define

\[
\Phi_{n,m}(\theta)
=
\mathbb E e^{i\theta T_{n,\beta_{n,m}}},
\qquad
\theta\in[-\pi,\pi].
\]

The inversion range is exactly the integer torus `[-pi,pi]`. Do not request decay as `|theta|->infinity`, and do not substitute the characteristic function of `log d`.

## Required theorem package

Return an explicit bulk target set `I_n` and prove all of the following.

### 1. Tilt existence and uniqueness

For every `m in I_n`, prove that a finite real `beta_{n,m}` exists with

\[
\mu_n(\beta_{n,m})=\xi_m
\]

or lies in an explicitly bounded interval inside `W_{n,m}`.

State exact endpoint exclusions.

### 2. Variance bounds

Prove explicit functions `v_-(n,m)` and `v_+(n,m)` such that

\[
0<v_-(n,m)
\le
\sigma_n^2(\beta_{n,m})
\le
v_+(n,m)
\]

uniformly on `I_n`.

### 3. Lattice and resonance audit

Determine the exact additive span of the tilted support. Audit every point or neighborhood in `[-pi,pi]` where `|Phi_{n,m}(theta)|` may be large. A statement that the gcd is one does not replace a quantitative resonance bound.

### 4. Reference law

Provide an explicit lattice probability law `G_{n,m}` with characteristic function `Psi_{n,m}` and a proved lower bound

\[
G_{n,m}(W_{n,m})\ge p_0(n,m)>0.
\]

A discretized Gaussian is allowed only with normalization and window mass proved explicitly.

### 5. Weighted Fourier inequality

With

\[
K_{n,m}(\theta)
=
\sum_{a\in W_{n,m}}e^{-ia\theta},
\]

prove

\[
\int_{-\pi}^{\pi}
|\Phi_{n,m}(\theta)-\Psi_{n,m}(\theta)|
|K_{n,m}(\theta)|\,d\theta
<
2\pi G_{n,m}(W_{n,m})
\]

for every `m in I_n`.

By N2-ADD-110, this implies positive tilted mass in the exact four-point window.

### 6. Endpoint contract

List every target not in `I_n`. Nova 1 must cover those targets deterministically. The bulk and endpoint sets must have no transition gap.

## Quantitative warning for a constant-width window

The reference mass of a four-point central lattice window is typically of order `1/sigma`. Therefore an approximation error bounded only by a fixed constant, or by a term not `o(1/sigma)`, cannot prove positivity. Berry-Esseen in distribution distance is not automatically adequate; the exact error must be compared with the four-point reference mass.

## Required output classification

Return each statement as one of:

- proved theorem;
- conditional theorem;
- finite certificate;
- computational evidence;
- heuristic;
- disproved model.

## Verification request

Supply exact or interval-certified computations for the smallest feasible `n` to test:

- tilt existence;
- variance collapse boundaries;
- characteristic-function resonances;
- minimum four-point window mass;
- the strict weighted Fourier inequality.

Finite calculations remain computational evidence unless exhaustive over a declared finite range.

## Known failure modes

- analyzing `log d` instead of quotient sums of numerical divisors;
- using the original unnormalized variables and overlooking the common lattice;
- proving only a growing-window theorem;
- proving almost-all quotient targets;
- relying on unbounded-frequency decay;
- ignoring secondary resonances on the integer torus;
- using a Gaussian plot instead of a local inequality;
- allowing the target to change the label supports;
- failing to identify the deterministic endpoint handoff.

## What is not claimed

Nova 2 has not proved the quotient four-point occupancy theorem. The purpose of this handoff is to freeze the exact additive law and the weakest analytic inequality that would prove the repaired bulk node.
