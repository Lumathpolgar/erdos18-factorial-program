# Nova 2 Open Requirements

## Requirements from Nova 1

### N2-REQ-N1-001

Requirement status: `OPEN`

Provide fixed factorial labels and a correction palette satisfying every structural hypothesis of N2-ADD-114:

- `A_{1,n},...,A_{k_n,n} subseteq D(n!)`;
- `k_n<=K_1(log n)^2`;
- exact divisor formulas;
- pairwise numerical disjointness;
- disjoint correction palette `C_n`;
- exact correction radius `R_n`;
- every residual `0<=r<=R_n` representable using at most `L_1(log n)^2` correction divisors;
- total support reach at least `X_n-R_n`;
- additive span one or complete residue repair;
- deterministic coverage of every endpoint regime excluded from the bulk tilt theorem;
- maximal-step data needed by the analytic theorem.

Frozen handoff: `handoffs/TO_NOVA1.md`.

## Requirements from Nova 3

### N2-REQ-N3-001

Requirement status: `OPEN`

For the frozen Nova 1 labels, prove target-dependent exponential-tilt existence and a uniform bulk variance theorem with an explicit target range.

### N2-REQ-N3-002

Requirement status: `OPEN`

Prove the lattice span or identify every inaccessible residue class.

### N2-REQ-N3-003

Requirement status: `OPEN`

Provide an explicit lattice reference law `Q_{n,x}`, major arc, minor arc, and error functions satisfying

\[
\int_{\mathfrak M}E_{\rm maj}|K_{n,x}|dt
+
\int_{\mathfrak m}E_{\rm min}|K_{n,x}|dt
<2\pi Q_{n,x}(I_{n,x})
\]

for every target in the declared bulk range.

Frozen handoff: `handoffs/TO_NOVA3.md`.

## Requirements from Nova 4

### N2-REQ-N4-001

Requirement status: `OPEN`

Build an exact or certified falsification harness for divisor legality, numerical collisions, gcd and residues, support gaps, every target window, tilt parameters, variance, and the weighted Fourier inequality.

### N2-REQ-N4-002

Requirement status: `OPEN`

Return the smallest counterexample by smallest `n`, then smallest target, then smallest violated condition.

### N2-REQ-N4-003

Requirement status: `OPEN`

Record the exact branch and commit SHA of every Nova 1 and Nova 3 input under test. Reject corrupted certificates and fail closed.

Frozen handoff: `handoffs/TO_NOVA4.md`.

## Archive requirement

### N2-REQ-ARC-001

Requirement status: `OPEN`

Import the full Phase 12M through 12P source packages or source-level theorem statements into the repository so the exact quantitative no-go hypotheses can be audited rather than inferred from index summaries.

## Internal Nova 2 requirements

### N2-REQ-INT-001

Requirement status: `OPEN`

Instantiate N2-ADD-114 for the first accepted factorial label family.

### N2-REQ-INT-002

Requirement status: `OPEN`

Prove that the selected model is genuinely final-only and does not impose a hidden sequential interval invariant covered by Phase 12P.

### N2-REQ-INT-003

Requirement status: `OPEN`

After receiving endpoint and bulk ranges, verify that their union covers every integer target from `0` through `X_n` with no transition gap.

## Rule

Every theorem, certificate, computation, heuristic, or disproved architecture must use one of the track's six allowed result labels. Requirements themselves use requirement status rather than an evidence label. No target may be omitted, and no labeled duplicate may be treated as a distinct numerical divisor.
