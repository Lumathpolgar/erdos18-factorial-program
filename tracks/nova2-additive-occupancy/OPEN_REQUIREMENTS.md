# Nova 2 Open Requirements

## Nova 1 requirements

### N2-REQ-N1-001-v5

Status: `STRUCTURAL_INPUT_ACCEPTED`.

Frozen marker-three source:

- branch: `nova/factorial-structure`;
- commit: `ebb47ba436af554366d0f285119a769f31f9e561`;
- construction: `N1-CON-003`.

Accepted facts include legality, exact 2-adic separation, numerical palette disjointness, exact lattice `3 Z`, quotient span one, correction reduction, and term cost `M_n+r_n`.

### N2-REQ-N1-002-v5

Status: `OPEN_EFFECTIVE_UTILIZATION`.

The count-only entropy condition from `N1-OBS-003` is necessary but not sufficient. Under `N2-ADD-122`, define

\[
a_t=\frac{2^{t-1}U_t}{F_{t-1}},
\qquad
b_t=\frac{1+a_t}{1+K_t}.
\]

The exact sequential requirement is

\[
\left(\prod_t(1+K_t)\right)
\left(\prod_tb_t\right)
\ge
\frac{Y_n+1}{W_n+1}.
\]

Provide one of:

1. pointwise lower bounds for `b_t`;
2. averaged lower bounds for `prod b_t`;
3. lower bounds for average-gap utilization `eta_t=U_t/(K_tD_t)`;
4. a uniform upper bound proving the effective product fails and retiring N2-ADD-120.

Exact inspected source:

`nova/factorial-structure@a6bdab1b917f3b3688f5a0c86e80c8a026bfbc07`.

Response:

`handoffs/RESPONSE_TO_NOVA1_N53_EFFECTIVE_ENTROPY.md`.

### N2-REQ-N1-003-v2

Status: `OPEN`.

Provide target-local collision-energy or maximum-fiber upper bounds for sums in `[q-W_n,q]`. Raw profile count is not numerical support cardinality.

## Nova 3 requirements

### N2-REQ-N3-001-v5

Status: `PARTIALLY_CLOSED`.

Tilt existence, uniqueness, span one, exact resonances, and post-prefix tilt compression are accepted with restrictions.

### N2-REQ-N3-002-v5

Status: `OPEN`.

Prove uniform numerical variance, third-moment, maximal-step, and endpoint-collapse bounds for the exact marker-three quotient law.

### N2-REQ-N3-003-v5

Status: `OPEN`.

Prove aggregate phase dispersion

\[
\mathcal D_{t,\lambda}(\theta)
=
\sum_{a,b}p_t(a)p_t(b)
\sin^2\left(\frac{(a-b)\theta}{2}\right)
\]

strong enough to control the complete characteristic function on required minor arcs.

### N2-REQ-N3-004-v4

Status: `OPEN`.

Construct a collision-aware integer reference law or a target-local energy bound and prove the strict weighted Fourier inequality for every declared target.

### N2-REQ-N3-005

Status: `OPEN`.

No logarithmic divisor theorem transfers to numerical additive sums without a separate proved bridge.

## Nova 4 requirements

### N2-REQ-N4-001-v4

Status: `OPEN`.

Independently replay the marker-three structural gate from commit `ebb47ba436af554366d0f285119a769f31f9e561`.

### N2-REQ-N4-002-v6

Status: `PARTIALLY_CLOSED_BY_NOVA2_AND_NOVA1`.

Independently reconstruct:

- `N2-ADD-119`, `N2-ADD-120`, `N2-ADD-121`, and `N2-ADD-122`;
- `N2-FIN-202` for `12<=n<=45`;
- `N2-FIN-203` at `n=46`;
- accepted Nova 1 finite certificates through `n=53`;
- the dual-partition replay at `n=53`.

### N2-REQ-N4-003-v6

Status: `OPEN`.

Extend exact complete-core certification from

\[
n=54.
\]

Resource limits must remain fail-closed and are not counterexamples.

### N2-REQ-N4-004-v4

Status: `OPEN`.

For feasible ranges, compute full restricted sumsets and report support size, collision multiplicity, maximum downward gap, first empty window, and exact witnesses. Reduced-menu failure is not full-model failure.

### N2-REQ-N4-005-v3

Status: `OPEN`.

Audit endpoint-window support. Total maximum support above `Y_n` does not prove every downward window occupied.

## Archive requirement

### N2-REQ-ARC-001

Status: `OPEN`.

Import source-level Phase 12M through 12P statements so exact hypotheses can be audited.

## Internal Nova 2 requirements

### N2-REQ-INT-001-v5

Status: `OPEN`.

Prove or disprove

\[
Q_n\cap[q-W_n,q]\ne\varnothing
\]

for every required quotient target, uniformly for all sufficiently large `n`.

### N2-REQ-INT-002-v6

Status: `FINITE_RANGE_CLOSED_THROUGH_N53`.

Exact complete-core carrier coverage is established for every `12<=n<=53`. Extend from `n=54` only as a finite auxiliary program.

### N2-REQ-INT-003-v5

Status: `OPEN`.

Prove the effective carrier condition `widetilde Gamma_n B_n>=1`, or upper-bound the utilization product strongly enough to retire the sequential engine. Separately audit Phase 12P.

### N2-REQ-INT-004-v4

Status: `OPEN`.

Upper-bound target-local collision multiplicity or additive energy.

### N2-REQ-INT-005-v3

Status: `OPEN`.

Compare the two final-only engines on identical labels:

1. collision-aware bounded-torus Fourier positivity;
2. deterministic final restricted-sumset growth.

### N2-REQ-INT-006

Status: `OPEN`.

Prove the bulk and deterministic endpoint regimes cover every target with no transition gap.

### N2-REQ-INT-007-v4

Status: `OPEN`.

Certify smaller exceptions and extend the upper finite boundary from `n=54`, clearly separated from the asymptotic theorem program.

## Rule

Every result must use an allowed evidence label. Failure of a sufficient proof engine must not be promoted to failure of the complete marker-three model.
