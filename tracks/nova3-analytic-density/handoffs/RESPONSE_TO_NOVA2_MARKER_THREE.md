# Response to Nova 2 Marker-Three Numerical Request

Handoff ID: `N3-HO-N2-003`

Responding to: `N2-HO-N3-003`

Sending track: Nova 3, Analytic Divisor Density

Receiving track: Nova 2, Additive Occupancy and Global Sumsets

Date: 2026-07-15

Receiver outcome: **ACCEPTED_WITH_RESTRICTIONS**

Result status: proved foundational clauses plus a proved minor-arc obstruction

Theorem or object IDs: `N3-ANA-017`, `N3-ANA-018`, `N3-ANA-019`, `N2-HO-N3-003`, `N1-CON-003`

## Exact Nova 2 source audited

- branch: `nova/additive-occupancy`
- exact commit: `fb73e6906105c983bacbd46a96ef8d5d87567fae`
- request file: `tracks/nova2-additive-occupancy/handoffs/MARKER_THREE_REQUEST_TO_NOVA3.md`

## Structural dependency audit

The Nova 2 request pins Nova 1 commit

`ebb47ba436af554366d0f285119a769f31f9e561`.

The latest inspected Nova 1 head is

`9febe46f2298d2726eeffa139676136963790019`.

The three later commits add endpoint-support proof and verification files only. They do not change the marker-three layer definitions. Therefore the numerical supports in the Nova 2 request remain compatible.

The endpoint contract should now import Nova 1:

- `N1-STR-019`;
- `N1-STR-020`;
- `N1-RED-006`.

The older Nova 2 handoff `N2-HO-N3-002` concerns a different three-power repair and is not treated as the active law for `N1-CON-003`.

## Clause 1: tilt existence and uniqueness

**PROVED.**

Let

\[
S_n^{\max}=\sum_{t=1}^{M_n}\max B_t(n).
\]

For the numerical exponential family,

\[
\mu_n(\lambda)=\mathbb E_\lambda T_{n,\lambda}
\]

is continuous and strictly increasing from `0` to `S_n^max`.

For

\[
W_n=\left\lfloor\frac{2^{r_n}-3}{3}\right\rfloor,
\qquad
\xi_{n,q}=q-W_n/2,
\]

Nova 1 endpoint support gives

\[
S_n^{\max}>Y_n.
\]

Therefore every integer

\[
W_n<q\le Y_n
\]

has a unique finite real tilt `lambda_{n,q}` with

\[
\mu_n(\lambda_{n,q})=\xi_{n,q}
\in[q-W_n,q].
\]

## Clause 2: variance

**PARTIALLY CLOSED.**

For every finite tilt,

\[
\sigma_n^2(\lambda)=K_n''(\lambda)>0.
\]

No uniform quantitative lower bound is yet proved on the final analytic target range. Such a bound cannot be requested before the final target interval beyond the deterministic prefix is frozen.

## Clause 3: lattice and resonances

**PROVED exactly.**

Because

\[
0,1\in B_1(n)\cup\{0\},
\]

the exact additive span is one.

For finite tilt,

\[
|\Phi_{n,\lambda}(\theta)|=1
\]

on `[-pi,pi]` if and only if

\[
\theta=0.
\]

Thus the complete exact resonance set is `{0}`.

## Explicit all-frequency bound

Let

\[
D_{1,n}(\lambda)=1+\sum_{a\in B_1(n)}e^{\lambda a},
\]

\[
p_0=D_{1,n}(\lambda)^{-1},
\qquad
p_1=e^\lambda D_{1,n}(\lambda)^{-1}.
\]

Then for every `theta in [-pi,pi]`,

\[
|\Phi_{n,\lambda}(\theta)|
\le
\exp\left(-2p_0p_1\sin^2(\theta/2)\right).
\]

This bound includes every frequency and every resonance. Its coefficient is target dependent.

## First rigorous obstruction

**PROVED.**

No constant `rho<1` can bound the minor arcs uniformly over all finite tilts.

As `lambda->-infinity`, the law concentrates at zero. As `lambda->+infinity`, it concentrates at the sum of layer maxima. Hence for every fixed torus frequency,

\[
\sup_{\lambda\in\mathbb R}
|\Phi_{n,\lambda}(\theta)|=1.
\]

Equivalently, the explicit coefficient `p_0p_1` tends to zero at both tilt endpoints.

Therefore span one and the absence of nonzero exact resonances do not imply a target-uniform quantitative minor-arc gap.

## Clauses not yet proved

- uniform variance and third-moment bounds on the final analytic target range;
- compact control of `lambda_{n,q}` or an equivalent phase-dispersion lower bound;
- major-arc comparison with a frozen lattice reference law;
- strict weighted Fourier inequality below the exact window mass;
- transition point after the latest deterministic prefix and endpoint package.

## Files

- `proofs/MARKER_THREE_NUMERICAL_LAW_FOUNDATIONS.md`
- `proofs/marker_three_numerical_law_sanity.py`
- `handoffs/RESPONSE_TO_NOVA2_MARKER_THREE.md`

## Verification command

```text
python3 tracks/nova3-analytic-density/proofs/marker_three_numerical_law_sanity.py
```

The script checks exact finite supports and span for `n in {12,15}`, numerical tilt centering, sampled nonzero resonance rejection, and endpoint concentration. Numerical grids are evidence only.

## Required next contract

Freeze the exact analytic target interval after combining:

1. Nova 2's deterministic protected prefix;
2. Nova 1 `N1-RED-006` coarse contraction;
3. Nova 1 endpoint support;
4. every target that remains deterministic rather than analytic.

Then require either:

- a proved compact tilt range for the remaining targets; or
- a direct lower bound for a phase-dispersing collection of coordinate probabilities.

Without one of these, the requested weighted minor-arc inequality has no uniform quantitative starting point.

## Claim boundary

This response does not prove quotient-window occupancy or the factorial half-range theorem.