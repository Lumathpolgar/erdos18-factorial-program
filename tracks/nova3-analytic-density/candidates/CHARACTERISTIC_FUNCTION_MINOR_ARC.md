# Candidate 3: Marker-Three Aggregate Phase Dispersion

## Theorem contract

- Candidate ID: `N3-CAND-CF-001`
- Original unrestricted logarithmic form: `disproved estimate`
- Active numerical bounded-torus form: `open`
- Intended consumer: Nova 2
- Exact source law: marker-three quotient model `N2-HO-N3-003`

## Active numerical law

For

\[
B_t(n)=
\{2^{t-1}u:u\text{ odd},\ 3u\mid n!,\ 2^{t-1}u\le Y_n\},
\]

let

\[
P_\lambda(Z_t=b)
=
\frac{e^{\lambda b}}
{1+\sum_{a\in B_t(n)}e^{\lambda a}},
\qquad
b\in B_t(n)\cup\{0\}.
\]

Define

\[
T_{n,\lambda}=\sum_{t=1}^{M_n}Z_t,
\qquad
\Phi_{n,\lambda}(\theta)=E_\lambda e^{i\theta T_{n,\lambda}},
\qquad
\theta\in[-\pi,\pi].
\]

This is a numerical integer-valued law. It is not the characteristic function of `log d`.

## Exact target range

Put

\[
P_n=m_n(2^{M_n}-1)+W_n.
\]

Nova 2 covers all quotient windows through `P_n` by a deterministic small-core chain. The final-only asymptotic analytic range is

\[
P_n+1\le q\le Y_n.
\]

For each such target, N3-ANA-018 gives a unique tilt `lambda_{n,q}` centered at

\[
q-W_n/2.
\]

N3-ANA-020 proves uniformly

\[
-\frac{8M_n\log L_n}{L_n}
<\lambda_{n,q}<
\frac{16(n\log n+\log14)}{2^{M_n}},
\]

so

\[
\sup_q|\lambda_{n,q}|\to0.
\]

## Exact resonance facts

N3-ANA-018 proves:

- exact additive span one;
- exact modulus-one resonance set `{0}` on `[-pi,pi]`.

N3-ANA-019 proves that a modulus gap cannot be uniform over all real tilts.

N3-ANA-021 proves that compact tilt does not rescue the single zero-versus-minimum anchor, because at zero tilt its coefficient is exponentially small.

## Multistate identity

For one layer, write

\[
p_t(a)=P_\lambda(Z_t=a),
\qquad
\phi_{t,\lambda}(\theta)=\sum_ap_t(a)e^{ia\theta}.
\]

Then exactly

\[
|\phi_{t,\lambda}(\theta)|^2
=
\sum_{a,b}p_t(a)p_t(b)e^{i(a-b)\theta}
\]

and therefore

\[
1-|\phi_{t,\lambda}(\theta)|^2
=
2\sum_{a,b}p_t(a)p_t(b)
\sin^2\left(\frac{(a-b)\theta}{2}\right).
\]

Define the aggregate layer dispersion

\[
\mathcal D_{t,\lambda}(\theta)
=
\sum_{a,b}p_t(a)p_t(b)
\sin^2\left(\frac{(a-b)\theta}{2}\right).
\]

Then

\[
|\Phi_{n,\lambda}(\theta)|^2
=
\prod_{t=1}^{M_n}
\left(1-2\mathcal D_{t,\lambda}(\theta)\right)
\le
\exp\left(-2\sum_t\mathcal D_{t,\lambda}(\theta)\right).
\]

This is the preferred exact minor-arc starting point.

## Desired conclusion

Freeze major and minor arcs on `[-pi,pi]`. Prove a lower bound of the form

\[
\sum_{t=1}^{M_n}
\mathcal D_{t,\lambda_{n,q}}(\theta)
\ge
\mathcal G_n(\theta)
\]

uniformly for every post-prefix target and every minor-arc frequency, where

\[
\int_{\mathfrak m_n}
\exp(-\mathcal G_n(\theta))
|K_{n,q}(\theta)|\,d\theta
\]

is strictly smaller than the required reference window mass.

A pointwise constant gap is not required if an integrable or weighted estimate closes Nova 2's exact inequality.

## Candidate structural inputs

### Many common odd-core differences

Every layer contains a scaled copy of many odd cores. If the tilted mass of enough pairs `u,v` with a controlled difference remains positive, then

\[
(a-b)=2^{t-1}(u-v)
\]

produces dyadically separated phase tests across the layers.

### Residue spreading

For a modulus `m`, a lower bound on tilted mass in at least two well-separated residue classes gives a lower bound for `D_t` near frequencies with denominator `m`.

### Divisor-gap chains

Nova 1 proves multiplicative 3-density and Nova 2 uses connected core chains. A quantitative additive or residue consequence for the tilted measure could supply many phase-separated pairs.

### Collision-aware atoms

N3-ANA-022 gives

\[
P_\lambda(T=s)
=
\frac{C_n(s)e^{\lambda s}}
{\prod_tZ_t(\lambda)}.
\]

Any reference law must retain or control `C_n(s)`. Aggregate Fourier decay cannot be interpreted as profile injectivity.

## Exact missing theorem

Prove one of:

1. a uniform lower bound for `sum_t D_t(theta)` outside explicit major arcs;
2. a measure bound for frequencies where the dispersion sum is small;
3. a weighted integral bound directly matched to Nova 2's kernel;
4. an additive-energy estimate giving the required collision-aware local mass;
5. a target-local obstruction showing that the tilted odd-core measure concentrates on too few phases.

## Known failed shortcuts

- Unbounded logarithmic minor arcs fail by N3-ANA-007.
- Uniform all-tilt numerical decay fails by N3-ANA-019.
- Span one does not imply a quantitative gap.
- `lambda_{n,q}->0` does not imply fixed state probabilities.
- The single zero-versus-one pair collapses by N3-ANA-021.
- Profile injectivity fails by Nova 1 `N1-COL-001`.
- Berry-Esseen distribution distance is not a constant-width local theorem.

## Falsification duties

1. List every major arc and internal near-resonance used by the proof.
2. Keep the exact post-prefix target range.
3. Check target-uniform tilted mass, not only uniform support cardinality.
4. Compare the final integral error with the reference window mass.
5. Retain collision multiplicity or prove an upper energy bound.
6. Do not substitute logarithmic divisor phases for numerical quotient phases.
7. Distinguish failure of one carrier or anchor method from failure of the full marker-three model.

## Feed to Nova 2

The next useful handoff from Nova 2 is the weakest explicit lower bound on the aggregate dispersion sum that would make its weighted window inequality strict, together with the exact major-arc partition and reference law.