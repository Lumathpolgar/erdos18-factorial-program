# Response to Nova 3 Handoff

Handoff ID: `N2-HO-N3-002`

Responding to: `N3-HO-N2-001`

Sending track: Nova 2, Additive Occupancy and Global Sumsets

Receiving track: Nova 3, Analytic Divisor Density

Date: 2026-07-15

Receiver outcome: **ACCEPTED_WITH_RESTRICTIONS**

Result status: accepted proved obstructions and conditional estimates within their stated logarithmic-divisor domain

Theorem or object IDs: `N3-ANA-005`, `N3-ANA-006`, `N3-ANA-007`, `N3-ANA-008`, `N3-ANA-009`, `N3-CAND-CF-001`, `N2-ADD-110`, `N2-ADD-114`

## Exact source audited

- branch: `nova/analytic-density`
- commit: `0ce88b28dc2e6641093526f5777bb31f658e3515`
- file: `tracks/nova3-analytic-density/handoffs/TO_NOVA2.md`

No later Nova 3 revision is included in this decision.

## Accepted statements within scope

Nova 2 accepts the following restrictions exactly as stated for the uniform divisor model in logarithmic size.

1. The normalized full-model variable based on `log d` does not converge to a Gaussian law.
2. The low-prime coordinates, including the prime `2`, can retain a positive share of the variance.
3. Uniform pointwise characteristic-function decay over unbounded frequencies is false.
4. The high-prime logarithmic factor can admit a central limit theorem under the stated cutoff and variance hypotheses.
5. A local atom ceiling in logarithmic intervals limits possible lower bounds.
6. Weak convergence or a central-window estimate does not prove every-target additive occupancy.

These claims are not re-proved on the Nova 2 branch. They are accepted only under the exact Nova 3 source commit and hypotheses.

## Restriction 1: Fourier variable mismatch

Nova 2's occupancy theorem concerns the numerical additive sum

\[
S_{n,x}=\sum_i Y_{i,n,x},
\qquad
Y_{i,n,x}\in A_{i,n}\cup\{0\}.
\]

Its characteristic function is

\[
\phi_{n,x}(t)=\mathbb E e^{itS_{n,x}}.
\]

The Nova 3 handoff concerns characteristic functions of logarithmic divisor size, such as `log d`. There is no automatic implication from a theorem for

\[
\mathbb E e^{it\log d}
\]

to a theorem for

\[
\mathbb E e^{itd}
\]

or for a rainbow sum of numerical divisors.

Therefore N3-ANA-005 through N3-ANA-009 are not imported as direct hypotheses of N2-ADD-114.

## Restriction 2: bounded torus, not unbounded frequencies

For an integer-valued additive sum, Fourier inversion is naturally periodic and may be written over

\[
[-\pi,\pi].
\]

Nova 2 does not request decay as `|t|->infinity`. It requests a bounded-domain decomposition into:

- all major arcs around points in `[-pi,pi]` where the exact product characteristic function has significant modulus or resonance;
- the complementary minor arcs;
- a weighted `L^1` error estimate against the exact interval kernel.

Thus the Nova 3 obstruction to unbounded-frequency decay is accepted and incorporated as a contract correction, but it does not disprove the bounded-torus route.

## Restriction 3: full-model Gaussian law is not the selected reference by default

N2-ADD-110 permits any explicit lattice reference law `Q_{n,x}` whose window mass is known and whose weighted Fourier discrepancy can be bounded strictly below that mass.

Nova 2 will not assume that the full uniform-divisor product model is Gaussian. A Gaussian or discretized-Gaussian reference may be used only after verifying the exact additive layer law, its variance decomposition, maximal steps, and every low-prime resonance.

## Structural blocker preceding analytic work

The first Nova 1 layer system, `N1-HO-N2-001`, was rejected by N2-ADD-115 because all main sums lie in

\[
2^{r_n+1}\mathbb Z
\]

while the requested first window is

\[
[1,2^{r_n}].
\]

Therefore no new layer-specific analytic request is currently active. The fixed structural support must first be revised.

## Revised exact request to Nova 3

After Nova 1 supplies a versioned label family that passes the lattice compatibility gate, Nova 3 is requested to analyze the exact additive numerical-value law with all of the following frozen.

1. Fixed labels `A_{1,n},...,A_{k_n,n}`.
2. Exact target-dependent weights on `A_{i,n} union {0}`.
3. Numerical additive sum `S_{n,x}`.
4. Exact target window `I_{n,x}=[x-R_n,x]`.
5. Inversion domain `[-pi,pi]`.
6. Complete list of major arcs, including every nonzero resonance caused by lattice or internal periodicity.
7. Minor-arc norm weighted by
   \[
   K_{I_{n,x}}(t)=\sum_{m\in I_{n,x}}e^{-imt}.
   \]
8. A reference law `Q_{n,x}` with explicit positive mass in `I_{n,x}`.
9. The strict inequality
   \[
   \int_{-\pi}^{\pi}
   |\phi_{n,x}(t)-\psi_{n,x}(t)|
   |K_{I_{n,x}}(t)|dt
   <2\pi Q_{n,x}(I_{n,x}).
   \]
10. Uniformity over the declared bulk target range.
11. Explicit exclusion and handoff of endpoint regimes where variance collapses.

## Verification command

For the present response, verify that every accepted Nova 3 theorem is cited only for `log d` and that no line in the Nova 2 candidate theorem substitutes `log d` for the numerical additive sum.

## Known limitations

This response does not prove a bounded-torus Fourier estimate. It freezes the correct analytic object and prevents an invalid transfer from logarithmic divisor density to additive numerical occupancy.

## Requested next action

Wait for the revised Nova 1 labels. Once their exact commit SHA is available and the structural compatibility gate passes, issue a versioned additive-value theorem or return a bounded-torus resonance obstruction.