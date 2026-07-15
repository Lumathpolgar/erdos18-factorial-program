# Nova 2: Additive Occupancy and Global Sumsets

## Branch

`nova/additive-occupancy`

## Mission

Develop a genuinely global non-greedy additive mechanism that turns structured divisor families of `n!` into uniform coverage of every target in the required half-range with polylogarithmically many distinct terms.

## Primary target

Given structured, labeled families `A_1,...,A_k subseteq D(n!)`, prove a uniform occupancy theorem strong enough to imply

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)=O((\log n)^2).
\]

Intermediate partial sums need not cover intervals. Only the final construction must cover every target.

## Required baseline work

- Reconstruct the failures of the Phase 12M through 12P additive architectures.
- Identify exactly which hypotheses caused each no-go theorem.
- Reconstruct the factorial-specific layer proposals supplied by Nova 1.
- Separate profile capacity, collision control, anti-concentration, and maximum-gap control.

## Research program

### N2-A: Rainbow convolution model

For measures supported on labeled divisor layers, study the convolution

\[
\mu_1*\cdots*\mu_k.
\]

Determine conditions ensuring every correction window in the target interval receives positive mass.

### N2-B: Fourier and local-limit route

Seek minor-arc decay, major-arc control, lattice-span conditions, and a local central limit theorem uniform enough for pointwise or short-window positivity.

### N2-C: Additive combinatorial route

Study sumset growth, restricted sumsets, inverse theorems, and structural anti-concentration. Any use of Cauchy-Davenport, Freiman theory, Littlewood-Offord theory, or entropy inequalities must match the integer setting and restricted selection rules.

### N2-D: Tilting and target-dependent measures

Allow an exponential tilt depending on the target `x` if the resulting proof remains uniform in `x` and produces an actual deterministic representation.

### N2-E: Correction-window bridge

Prove exact occupancy of intervals of width `R(n)` that Nova 1's correction palette can finish. Track the full term count and distinctness.

## Forbidden shortcuts

- More profiles than targets does not imply coverage.
- Small variance or a Gaussian-looking histogram does not imply positivity at every point.
- An almost-all theorem is insufficient.
- Random selection experiments are not a probabilistic proof.
- Fourier estimates must account for lattice periodicity and common divisors.
- The same numerical divisor may not be selected from two labels.

## Deliverables

- `tracks/nova2-additive-occupancy/STATUS.md`
- `tracks/nova2-additive-occupancy/THEOREMS.md`
- `tracks/nova2-additive-occupancy/MODELS.md`
- `tracks/nova2-additive-occupancy/OPEN_REQUIREMENTS.md`
- exact handoffs requesting structural or analytic inputs
- proofs or counterexamples for every promoted occupancy claim

## Initial milestone

Given at least two candidate factorial layer systems, produce for each:

- the support and term budget;
- the expected or deterministic sum range;
- collision and lattice obstructions;
- the strongest occupancy theorem currently provable;
- the exact missing Fourier, anti-concentration, or density estimate.

## Acceptance criteria

Nova 2 succeeds when it supplies either:

1. a uniform global occupancy theorem closing the half-range target;
2. a precise additive bridge that combines with accepted Nova 1 and Nova 3 results;
3. a rigorous obstruction eliminating a proposed global sumset architecture.
