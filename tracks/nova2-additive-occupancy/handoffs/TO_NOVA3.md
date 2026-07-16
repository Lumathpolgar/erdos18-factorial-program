# Handoff to Nova 3

Handoff ID: `N2-HO-N3-001`

Sending track: Nova 2, Additive Occupancy and Global Sumsets

Receiving track: Nova 3, Analytic Divisor Density

Date: 2026-07-15

Result status: `conditional theorem`

Theorem or object IDs: `N2-ADD-114`, `N2-REQ-N3-001`, `N2-REQ-N3-002`

## Exact analytic theorem requested

Assume Nova 1 supplies fixed pairwise disjoint labels `A_{i,n}` and positive base weights. For target `x`, define the exponential tilt

\[
\mu_{i,n,\theta}(a)=
\frac{w_{i,n}(a)e^{\theta a}}
{\sum_{b\in A_{i,n}\cup\{0\}}w_{i,n}(b)e^{\theta b}}.
\]

For every target in a declared bulk range, prove the following with absolute, explicit constants.

1. A real parameter `theta_{n,x}` exists with the tilted mean within a stated distance of the midpoint of
   \[
   I_{n,x}=[x-R_n,x]\cap\mathbb Z.
   \]
2. The variance satisfies
   \[
   0<v_-(n,x)\le\sigma_{n,x}^2\le v_+(n,x),
   \]
   with a lower bound strong enough for the local theorem.
3. The lattice span is one, or the exact inaccessible residue classes are identified.
4. A major arc
   \[
   \mathfrak M_{n,x}=\{|t|\le T_{n,x}/\sigma_{n,x}\}
   \]
   admits a frozen comparison
   \[
   |\phi_{n,x}(t)-\psi_{n,x}(t)|\le E_{\rm maj}(n,x,t).
   \]
5. On the minor arc
   \[
   \mathfrak m_{n,x}=[-\pi,\pi]\setminus\mathfrak M_{n,x},
   \]
   prove
   \[
   |\phi_{n,x}(t)-\psi_{n,x}(t)|\le E_{\rm min}(n,x,t).
   \]
6. With
   \[
   K_{n,x}(t)=\sum_{m\in I_{n,x}}e^{-imt},
   \]
   prove the strict inequality
   \[
   \int_{\mathfrak M_{n,x}}E_{\rm maj}|K_{n,x}|dt
   +
   \int_{\mathfrak m_{n,x}}E_{\rm min}|K_{n,x}|dt
   <2\pi Q_{n,x}(I_{n,x}).
   \]

Here `Q_{n,x}` must be a lattice probability law with characteristic function `psi_{n,x}` and an explicit positive lower bound for `Q_{n,x}(I_{n,x})`.

## Exact target type

The theorem must be uniform for every target in the declared bulk range. An average, almost-all, weak-convergence, or finite statement is insufficient.

## Endpoint requirement

N2-ADD-106 proves variance collapse near Bernoulli support endpoints. State the exact target range where the variance lower bound holds and the exact width of the excluded endpoint regimes. Do not claim the bulk theorem there.

## Weakest sufficient conclusion

Nova 3 does not need a pointwise local limit theorem if the weighted window error above is strictly smaller than the reference window mass.

## Dependencies

- `proofs/CANDIDATE_OCCUPANCY_THEOREM.md`
- `models/FOURIER_LOCAL_LIMIT.md`
- `models/TARGET_DEPENDENT_TILT.md`
- `models/TOY_COUNTEREXAMPLES.md`

## Verification command

No code command yet. Every displayed inequality must be checked uniformly in `n` and `x`, with the major and minor arc domains explicitly partitioning `[-pi,pi]`.

## Known failure modes

- hidden lattice periodicity;
- variance collapse;
- one large label violating a Lindeberg condition;
- a minor-arc estimate only away from additional resonant rational points;
- an error term larger than the reference window mass;
- a central theorem silently extrapolated to endpoints.

## What is not claimed

No factorial characteristic-function estimate has been proved on this branch.

## Requested next action

For the first frozen Nova 1 label family, prove the six numbered analytic clauses or return the first rigorous obstruction, including the exact failed inequality and parameter range.
