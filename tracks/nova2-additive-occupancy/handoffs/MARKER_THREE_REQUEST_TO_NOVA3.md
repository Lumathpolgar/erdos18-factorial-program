# Marker-Three Additive Request to Nova 3

Handoff ID: `N2-HO-N3-003`

Sending track: Nova 2, Additive Occupancy and Global Sumsets

Receiving track: Nova 3, Analytic Divisor Density

Date: 2026-07-15

Result status: conditional theorem request

## Frozen structural input

Source construction:

- branch: `nova/factorial-structure`
- exact commit: `ebb47ba436af554366d0f285119a769f31f9e561`
- construction: `N1-CON-003`
- handoff: `N1-HO-N2-002`

Nova 2 intake:

- outcome: `ACCEPTED_WITH_RESTRICTIONS`
- response: `handoffs/RESPONSE_TO_NOVA1_MARKER_THREE.md`
- deterministic reduction: `proofs/MARKER_THREE_CARRIER_BLOCK_REDUCTION.md`

## Exact quotient labels

For

\[
Y_n=\left\lfloor\frac{\lfloor\sqrt{n!}\rfloor}{3}\right\rfloor,
\]

let

\[
U_t(n)=
\{u\ge1:u\text{ odd},\ 3u\mid n!,\ 2^{t-1}u\le Y_n\},
\]

\[
B_t(n)=\{2^{t-1}u:u\in U_t(n)\},
\qquad
1\le t\le M_n.
\]

The final quotient rainbow sum is

\[
T_n=\sum_{t=1}^{M_n}Z_t,
\qquad
Z_t\in B_t(n)\cup\{0\}.
\]

The fixed labels are the same for every target. Only the probability weights may depend on the target.

## Exact target windows

Let

\[
W_n=\left\lfloor\frac{2^{r_n}-3}{3}\right\rfloor.
\]

For a quotient target `q`, define

\[
I_{n,q}=[\max(0,q-W_n),q]\cap\mathbb Z.
\]

Nova 1's exact reduction proves that positive mass in every required `I_{n,q}` implies

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
\le M_n+r_n.
\]

## Target-dependent product law

For each target `q`, construct or reject an exponential-family product law

\[
\mathbb P_{n,q,\lambda}\{Z_t=b\}
=
\frac{e^{\lambda b}}{1+\sum_{a\in B_t(n)}e^{\lambda a}},
\qquad b\in B_t(n),
\]

with the zero choice carrying the remaining denominator term.

An equivalent numerically stable parameterization is allowed, but it must define the same numerical-value law and state the exact parameter conversion.

Required centering:

\[
\mathbb E T_n\in I_{n,q},
\]

preferably near the midpoint. Prove existence and uniqueness on the declared bulk range, or return the exact obstruction.

## Required moment theorem

For every target in the declared bulk range, provide explicit bounds for:

- the mean;
- the variance;
- the third absolute centered moment;
- the largest active numerical step;
- the ratio of the largest step to the standard deviation;
- the first lower and upper targets where the bounds fail.

Bounds for `log Z_t` are not substitutes for bounds for `Z_t`.

## Bounded-torus characteristic function

The required characteristic function is

\[
\Phi_{n,q}(\theta)
=
\mathbb E_{n,q}e^{i\theta T_n},
\qquad
\theta\in[-\pi,\pi].
\]

Determine:

1. the exact additive span;
2. every internal resonance on the torus;
3. explicit major arcs containing all resonances;
4. explicit minor arcs;
5. quantitative bounds on both regions.

The fact that `1 in B_1(n)` proves span one but does not prove a minor-arc estimate.

## Weighted window theorem

Provide an explicit integer-valued reference law `G_{n,q}` with characteristic function `Psi_{n,q}` and positive mass

\[
G_{n,q}(I_{n,q})>0.
\]

Prove

\[
\int_{-\pi}^{\pi}
|\Phi_{n,q}(\theta)-\Psi_{n,q}(\theta)|
\left|
\sum_{a\in I_{n,q}}e^{-ia\theta}
\right|d\theta
<
2\pi G_{n,q}(I_{n,q})
\]

for every declared bulk target.

An approximation whose error is at least the reference window mass is insufficient.

## Deterministic prefix boundary

Nova 1 already proves downward one-density through

\[
m_n(2^{M_n}-1),
\]

and Nova 2 extends required `W_n`-window occupancy through

\[
m_n(2^{M_n}-1)+W_n.
\]

Analytic work should prioritize targets beyond that boundary. Do not spend the primary proof budget reproving the known deterministic prefix.

## Required response

Return one of:

- `ACCEPTED`;
- `ACCEPTED_WITH_RESTRICTIONS`;
- `NEEDS_REPAIR`;
- `REJECTED`.

Include the exact branch, exact commit SHA, target range, endpoint exclusions, constants, and proof or obstruction location.

## Claim boundary

No logarithmic divisor-density theorem transfers automatically to this numerical additive law. Finite Fourier grids and histograms are computational evidence only.