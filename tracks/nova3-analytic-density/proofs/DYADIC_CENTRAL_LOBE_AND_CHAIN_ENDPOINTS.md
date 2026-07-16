# Dyadic Central Lobe and Full-Menu Chain Endpoints

## Scope

This file continues the exact odd-lattice normalized marker-three law and the transformed dyadic factorization.

Imported heads:

- Nova 1: `nova/factorial-structure@8c7ee8f64af56a8d082f1fa3adabb0b0309f6e27`
- Nova 2: `nova/additive-occupancy@591e4e51a00627ac48c0aa05fae4a955dccb9d14`

The factorial half-range theorem and Erdős Problem 18 remain open.

## Frozen notation

For `n>=120368`, put

\[
\rho_n=\lceil4\log n\rceil,
\qquad
M_n=\lceil16(\log n)^2\rceil,
\]

\[
W_n=\left\lfloor\frac{2^{\rho_n}-3}{3}\right\rfloor.
\]

For each exact post-prefix target `q`, let

\[
J_{n,q}
=
\left[
\left\lceil\frac{q-W_n-1}{2}\right\rceil,
\left\lfloor\frac{q-1}{2}\right\rfloor
\right]\cap\mathbb Z,
\]

and let

\[
N_{n,q}=|J_{n,q}|.
\]

The transformed interval kernel is

\[
\widetilde K_{n,q}(\theta)
=
\sum_{x\in J_{n,q}}e^{ix\theta}.
\]

For the transformed product law, write

\[
\widetilde\Phi_{n,q}(\theta)
=
\prod_{t=1}^{M_n}
\widetilde\phi_{t,n,q}(\theta).
\]

The transformed common tilt is

\[
\widetilde\lambda_{n,q}=2\lambda_{n,q}.
\]

For the dyadic ladder define

\[
\theta_j
=
\frac{2\pi}{2^j}
=
\frac{\pi}{2^{j-1}}.
\]

## N3-ANA-032: exact central-lobe depth cutoff

Result class: **proved theorem**.

For every transformed target window,

\[
2^{\rho_n-3}
<
N_{n,q}
<
2^{\rho_n-2}.
\]

Consequently:

1. if `1<=j<=rho_n-3`, then
   \[
   \theta_j>\frac{2\pi}{N_{n,q}},
   \]
   so the dyadic point lies beyond the first positive zero of the interval kernel;
2. if `j>=rho_n-2`, then
   \[
   0<\theta_j<\frac{2\pi}{N_{n,q}},
   \]
   so the dyadic point lies inside the kernel's central lobe.

Thus only

\[
\rho_n-3=O(\log n)
\]

dyadic ladder points require separate secondary-frequency treatment. The remaining `M_n-rho_n+2` dyadic points lie inside the central kernel lobe and must be handled with the zero-frequency analysis rather than as distinct minor arcs.

### Proof

By `N3-ANA-028`, the transformed window length is one of

\[
\frac{2^{\rho_n-1}-1}{3},
\qquad
\frac{2^{\rho_n-1}-2}{3},
\qquad
\frac{2^{\rho_n-1}+1}{3}.
\]

For the present range, each lies strictly between `2^(rho_n-3)` and `2^(rho_n-2)`.

A consecutive interval of length `N` has kernel

\[
\widetilde K(\theta)
=e^{ic\theta}
\frac{\sin(N\theta/2)}{\sin(\theta/2)}
\]

for a real center `c`. Its first positive zero is `2pi/N`.

The two ladder classifications follow from comparing `2^j` with `N`. `QED`

## Selected full-menu coordinate

For every secondary dyadic scale

\[
1\le j\le\rho_n-3,
\]

select one transformed prefix coordinate:

- for `j=1`, select the first transformed coordinate
  \[
  \widetilde Z_1=(Z_1-1)/2;
  \]
- for `j>=2`, select transformed layer `t=j`.

The positive states in the selected coordinate are indexed by legal odd cores `u`.

For `j=1`, the phase is

\[
e^{i\pi(u-1)/2}.
\]

For `j>=2`, the selected layer has numerical state `2^(j-2)u`, and its phase at `theta_j` is

\[
e^{i\theta_j2^{j-2}u}
=e^{i\pi u/2}.
\]

In both cases multiplication of the odd core by `3` reverses the phase:

\[
\chi_j(3u)=-\chi_j(u).
\]

## Exact 3-adic chains

Write every legal positive odd core uniquely as

\[
u=3^e v,
\qquad
3\nmid v.
\]

For each fixed `v`, legality under the factorial exponent bound and the numerical cutoff gives a consecutive exponent interval

\[
e=0,1,\ldots,E_v.
\]

Let `w_{j,q}(3^e v)` be the unnormalized tilted weight of that positive state.

For `j=1`, apart from a constant independent of `e`,

\[
w_{1,q}(3^e v)
=
\exp\left(
\frac{\widetilde\lambda_{n,q}}{2}
3^e v
\right).
\]

For `j>=2`,

\[
w_{j,q}(3^e v)
=
\exp\left(
\widetilde\lambda_{n,q}
2^{j-2}3^e v
\right).
\]

For each chain the phase-weighted numerator is therefore

\[
\chi_j(v)
\sum_{e=0}^{E_v}
(-1)^e w_{j,q}(3^e v).
\]

## N3-ANA-033: exact chain-endpoint contraction

Result class: **proved theorem**.

Define the lower 3-adic endpoint event:

- for `j=1`, the selected positive odd core satisfies `3 not divide u`;
- for `j>=2`, either the selected coordinate is zero or its positive odd core satisfies `3 not divide u`.

Call this event `B^-_{n,q,j}`.

Define the upper 3-adic endpoint event:

- for `j=1`, the selected positive core `u` is legal but `3u` is not legal in the same coordinate;
- for `j>=2`, either the selected coordinate is zero or `u` is legal but `3u` is not legal.

Call this event `B^+_{n,q,j}`.

Then:

### Nonpositive transformed tilt

If

\[
\widetilde\lambda_{n,q}\le0,
\]

then

\[
|\widetilde\phi_{j,n,q}^{\rm sel}(\theta_j)|
\le
P(B^-_{n,q,j}).
\]

### Nonnegative transformed tilt

If

\[
\widetilde\lambda_{n,q}\ge0,
\]

then

\[
|\widetilde\phi_{j,n,q}^{\rm sel}(\theta_j)|
\le
P(B^+_{n,q,j}).
\]

Here `phi^sel` denotes the characteristic factor of the selected coordinate.

### Proof

On every 3-adic chain, the phases alternate because `chi_j(3u)=-chi_j(u)`.

If the tilt is nonpositive, the positive weights decrease with `e`. The alternating-sum estimate gives

\[
\left|
\sum_{e=0}^{E_v}(-1)^e w_e
\right|
\le w_0.
\]

Summing over chains bounds the positive numerator by the total lower-endpoint weight. For `j>=2`, the zero state contributes its own weight and is included in `B^-`.

If the tilt is nonnegative, the positive weights increase with `e`. Reversing each finite alternating chain gives

\[
\left|
\sum_{e=0}^{E_v}(-1)^e w_e
\right|
\le w_{E_v}.
\]

Summing over chains bounds the positive numerator by the total upper-endpoint weight. Again the zero state is included for `j>=2`.

Division by the exact selected-coordinate partition function proves both inequalities. `QED`

## N3-ANA-034: full-product dyadic reduction

Result class: **proved theorem and exact criterion**.

For every secondary dyadic scale

\[
1\le j\le\rho_n-3,
\]

the full transformed product satisfies:

\[
|\widetilde\Phi_{n,q}(\theta_j)|
\le
P(B^-_{n,q,j})
\qquad
\text{if }\widetilde\lambda_{n,q}\le0,
\]

and

\[
|\widetilde\Phi_{n,q}(\theta_j)|
\le
P(B^+_{n,q,j})
\qquad
\text{if }\widetilde\lambda_{n,q}\ge0.
\]

The same bounds hold for the first-`j` prefix characteristic.

### Proof

The selected factor belongs to the first `j` transformed coordinates. Every other characteristic factor has modulus at most one. Apply `N3-ANA-033` and multiply. `QED`

### Exact route consequence

The full-menu dyadic problem is reduced to one explicit weighted factorial-divisor statistic:

- lower 3-adic endpoint mass when the common transformed tilt is nonpositive;
- upper 3-adic endpoint mass when the common transformed tilt is nonnegative.

A target-uniform estimate

\[
P(B^{\operatorname{sgn}}_{n,q,j})
\le1-\varepsilon_{n,j}
\]

immediately gives the same contraction for the complete transformed characteristic function at `theta_j`.

Conversely, if the transformed characteristic function remains large at a secondary dyadic point, the corresponding selected layer must place comparably large mass on the appropriate 3-adic chain endpoints.

This is a full-menu weighted reduction. It does not use a fixed low-state carrier and does not replace probability mass by support cardinality.

## Zero-state term for `j>=2`

For selected layer `j>=2`, the endpoint events include the zero state. The existing low-state partition estimate gives

\[
P(\widetilde Z_j=0)
\le
\frac{2e^{\eta_{n,j}}}{m_n+1},
\]

where

\[
\eta_{n,j}
=
\frac{16M_n\log L_n}{2^{M_n}-1}
2^{j-2}.
\]

On the relevant range `j<=rho_n-3`, this term is negligible. The unresolved mass is the positive 3-adic endpoint component.

## Exact remaining theorem

Prove one of:

1. a target-uniform upper bound on the relevant lower or upper 3-adic endpoint mass;
2. a weighted average endpoint bound over all secondary dyadic scales;
3. a neighborhood version stable under `theta=theta_j+u`;
4. an exact target sequence for which the appropriate endpoint mass tends to one, obstructing the route.

The result must be compared with the transformed interval-kernel weight and the collision-aware reference main term.

## Claim boundary

This checkpoint does not prove:

- a strict endpoint-mass contraction;
- neighborhood control around the dyadic points;
- transformed local-window positivity;
- the strict weighted Fourier inequality;
- target-local collision control;
- quotient occupancy;
- the factorial half-range theorem;
- Erdős Problem 18.