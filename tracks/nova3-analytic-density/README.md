# Nova 3: Analytic Divisor Density

## Branch

`nova/analytic-density`

## Mission

Prove the asymptotic counting and distribution estimates for divisors of `n!` that are actually sufficient for the structural and additive tracks.

## Primary questions

1. How many divisors of `n!` lie in a prescribed logarithmic interval below `sqrt(n!)`?
2. How uniformly are factorial divisors distributed across multiplicative or additive windows?
3. Which valuation profiles dominate at a target scale?
4. Can one obtain local estimates strong enough for a global convolution or occupancy theorem?

## Required baseline work

- Record exact prime valuation constraints for `n!`.
- Compare factorial divisors with smooth and ultrafriable integers without identifying the sets incorrectly.
- Reconstruct the small-divisor ceilings used in Phases 12L and 12P and state why they do or do not transfer to `n!`.
- Inventory known theorems that may apply, with exact sources and hypotheses.

## Research program

### N3-A: Logarithmic generating function

Study

\[
F_n(z)=\prod_{p\le n}\left(1+z^{\log p}+\cdots+z^{v_p(n!)\log p}\right)
\]

through an appropriate continuous, Laplace, or probabilistic formulation. Identify the saddle point for divisors near a prescribed logarithmic size.

### N3-B: Local divisor counts

Estimate

\[
\#\{d\mid n!: e^u\le d\le e^{u+\Delta}\}
\]

uniformly in the ranges requested by Nova 1 and Nova 2.

### N3-C: Valuation-profile entropy

Count admissible exponent vectors under the weighted constraint

\[
\sum_{p\le n} a_p\log p\approx u,
\qquad
0\le a_p\le v_p(n!).
\]

Determine concentration, covariance, lattice span, and effective dimension.

### N3-D: Characteristic-function estimates

For additive constructions supplied by Nova 2, estimate characteristic functions or exponential sums needed for local-limit and anti-concentration arguments.

### N3-E: Maximum-gap limitations

Distinguish carefully between average density and guaranteed gaps. Prove either a usable maximum-gap statement or a theorem explaining why the requested statement is too strong.

## Forbidden shortcuts

- A global asymptotic for `tau(n!)` does not imply local density.
- Smooth-number estimates may overcount divisors of `n!`; overcounts must be used in the correct direction.
- Mean spacing is not maximum spacing.
- A central limit theorem without a local or uniform form may be insufficient.
- External theorems must be cited with matching ranges and parameters.

## Deliverables

- `tracks/nova3-analytic-density/STATUS.md`
- `tracks/nova3-analytic-density/THEOREMS.md`
- `tracks/nova3-analytic-density/SOURCE_LEDGER.md`
- `tracks/nova3-analytic-density/OPEN_REQUIREMENTS.md`
- explicit responses to theorem requests from Nova 1 and Nova 2
- proofs, source compatibility checks, and numerical sanity checks

## Initial milestone

Produce a rigorous scale map for divisors of `n!` below `sqrt(n!)` containing:

- asymptotic total log-size of `n!`;
- valuation entropy by prime band;
- upper and lower bounds for divisor counts at representative scales;
- candidate local window widths;
- precise gaps between known estimates and the estimates needed for occupancy.

## Acceptance criteria

Nova 3 succeeds when it supplies either:

1. analytic estimates sufficient for an accepted additive occupancy theorem;
2. a new local distribution theorem for factorial divisors with explicit uniformity;
3. a rigorous impossibility or lower-bound result that redirects the program.
