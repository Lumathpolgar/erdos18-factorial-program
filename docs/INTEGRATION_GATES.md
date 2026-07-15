# Integration Gates

## Gate 0: Definitions frozen

Requirements:

- `h(N)`, `lambda_N(x)`, and `H_N(X)` match `COMMON_NOTATION.md`.
- Endpoint conventions are explicit.
- All asymptotic parameters are identified.

Failure keeps every downstream result provisional.

## Gate 1: Divisor legality

For every construction:

- selected integers divide `n!`;
- prime valuations do not exceed `v_p(n!)`;
- any scaled or marked family remains inside the divisor lattice.

## Gate 2: Distinctness

The proof must establish numerical distinctness of all selected divisors, including cross-layer, marker, and correction terms.

## Gate 3: Local coverage

The local theorem must cover every target in its exact stated interval. Average-case, positive-density, or almost-all coverage does not pass.

## Gate 4: Term count

The complete construction, including corrections and exceptional cases, must satisfy the claimed polylogarithmic term bound.

## Gate 5: Uniform asymptotics

All estimates must hold uniformly over the required target and parameter ranges. Transition zones and endpoint regimes must be covered.

## Gate 6: Local-to-global conversion

The conditional Track B implication must be reconstructed with the current definitions and must not import the unproved historical `L_m` theorem.

## Gate 7: Finite exceptions

All `n<n_0` cases must be covered by proof, exact computation, or a stronger known theorem.

## Gate 8: Independent proof audit

At least one Nova that did not author a critical theorem must reconstruct it. The final assembled proof requires two independent end-to-end audits.

## Gate 9: Computational audit

All supporting code must run from a clean environment, reject corrupted certificates, and reproduce published tables or finite checks.

## Gate 10: Claim-language audit

The final documents must not:

- call a conditional result unconditional;
- call finite evidence asymptotic proof;
- claim the whole problem is solved before all gates pass;
- use a percentage-complete estimate as evidence.

## Gate 11: Final theorem

The final theorem must state absolute constants `C,K,n_0` or provide a valid asymptotic formulation from which they follow, and prove

\[
h(n!)\le K(\log n)^C
\]

for every integer `n>=n_0`.

## Gate status values

Each gate is labeled:

- `NOT_STARTED`
- `IN_PROGRESS`
- `BLOCKED`
- `FAILED`
- `PASSED`

Only `PASSED` permits downstream final acceptance.
