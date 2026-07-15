# Nova 2 Open Requirements

## Requirements from Nova 1

### N2-REQ-N1-001-v2

Requirement status: `OPEN`

The first fixed layer system in `N1-HO-N2-001` was rejected at Nova 1 commit `b939574eb88a08bb03abda5bbe6ff2ca97444e08` by N2-ADD-115. Its support lies in `2^{r_n+1} Z`, while its correction radius is only `2^{r_n}-1`.

Provide a revised, versioned factorial label family and correction palette satisfying every structural hypothesis of N2-ADD-114:

- `A_{1,n},...,A_{k_n,n} subseteq D(n!)`;
- `k_n<=K_1(log n)^2`;
- exact divisor formulas;
- pairwise numerical disjointness;
- disjoint correction palette `C_n`;
- exact correction radius `R_n`;
- every residual `0<=r<=R_n` representable using at most `L_1(log n)^2` correction divisors;
- total support reach at least `X_n-R_n`;
- exact common lattice span of all main sums;
- exact attained residue classes modulo that span;
- proof that `R_n` is at least every unresolved downward residue gap;
- explicit coverage of the first requested target;
- deterministic coverage of every endpoint regime excluded from the bulk tilt theorem;
- maximal-step data needed by the analytic theorem;
- confirmation that no sequential partial-interval invariant is imposed.

Original request: `handoffs/TO_NOVA1.md`.

Rejection and repair contract: `handoffs/RESPONSE_TO_NOVA1.md`.

## Requirements from Nova 3

### N2-REQ-N3-001-v2

Requirement status: `BLOCKED_ON_REVISED_LABELS`

After Nova 1 supplies an accepted fixed layer system, prove target-dependent exponential-tilt existence and a uniform bulk variance theorem for the additive numerical-value random sum

\[
S_{n,x}=\sum_i Y_{i,n,x},
\qquad
Y_{i,n,x}\in A_{i,n}\cup\{0\}.
\]

The theorem must state the exact target range and cannot use a logarithmic-divisor model without a proved transfer.

### N2-REQ-N3-002-v2

Requirement status: `BLOCKED_ON_REVISED_LABELS`

For the exact additive layer law, identify every resonance on the integer torus and prove the actual lattice span or every inaccessible residue class.

### N2-REQ-N3-003-v2

Requirement status: `BLOCKED_ON_REVISED_LABELS`

Provide an explicit lattice reference law `Q_{n,x}`, major arc set `M_{n,x}`, minor arc set `m_{n,x}`, and error functions on the bounded inversion domain `[-pi,pi]` satisfying

\[
\int_{\mathfrak M_{n,x}}E_{\rm maj}|K_{n,x}|dt
+
\int_{\mathfrak m_{n,x}}E_{\rm min}|K_{n,x}|dt
<2\pi Q_{n,x}(I_{n,x})
\]

for every target in the declared bulk range.

The characteristic function must be

\[
\phi_{n,x}(t)=\mathbb E e^{itS_{n,x}},
\]

where `S_{n,x}` is the numerical divisor sum. The Fourier variable is not applied to `log d`.

Original handoff: `handoffs/TO_NOVA3.md`.

Nova 3 source inspected: branch `nova/analytic-density`, commit `0ce88b28dc2e6641093526f5777bb31f658e3515`, handoff `N3-HO-N2-001`.

### N2-REQ-N3-004

Requirement status: `OPEN`

Any proposed use of Nova 3 theorems for logarithmic divisor size must include a separate proved compatibility theorem transferring those estimates to the additive numerical-value convolution. Without that bridge, the result is not an input to N2-ADD-114.

## Requirements from Nova 4

### N2-REQ-N4-001

Requirement status: `OPEN`

Build an exact or certified falsification harness for divisor legality, numerical collisions, gcd and residues, support gaps, every target window, tilt parameters, variance, and the weighted Fourier inequality.

The harness must run the lattice compatibility test before expensive convolution or Fourier work.

### N2-REQ-N4-002

Requirement status: `OPEN`

Return the smallest counterexample by smallest `n`, then smallest target, then smallest violated condition.

For any family with all terms divisible by `g`, explicitly test whether the correction radius is below `g-1` and whether the target range contains a missing residue block.

### N2-REQ-N4-003

Requirement status: `OPEN`

Record the exact branch and commit SHA of every Nova 1 and Nova 3 input under test. Reject corrupted certificates and fail closed.

Frozen handoff: `handoffs/TO_NOVA4.md`.

## Archive requirement

### N2-REQ-ARC-001

Requirement status: `OPEN`

Import the full Phase 12M through 12P source packages or source-level theorem statements into the repository so the exact quantitative no-go hypotheses can be audited rather than inferred from index summaries.

## Internal Nova 2 requirements

### N2-REQ-INT-001-v2

Requirement status: `BLOCKED_ON_NOVA1`

Instantiate N2-ADD-114 for the first structurally accepted factorial label family. The rejected `N1-HO-N2-001` family cannot serve as this input.

### N2-REQ-INT-002

Requirement status: `OPEN`

Prove that the selected model is genuinely final-only and does not impose a hidden sequential interval invariant covered by Phase 12P.

### N2-REQ-INT-003

Requirement status: `OPEN`

After receiving endpoint and bulk ranges, verify that their union covers every integer target from `0` through `X_n` with no transition gap.

### N2-REQ-INT-004

Requirement status: `OPEN`

For every future frozen layer family, run the following checks before analytic modeling:

1. gcd and support lattice;
2. exact residue classes;
3. first requested target;
4. correction radius versus maximum residue gap;
5. minimum nonzero main term;
6. numerical collisions;
7. total support reach.

## Rule

Every theorem, certificate, computation, heuristic, or disproved architecture must use one of the track's six allowed result labels. Requirements themselves use requirement status rather than an evidence label. No target may be omitted, and no labeled duplicate may be treated as a distinct numerical divisor.