# Nova 2 Open Requirements

## Nova 1 requirements

### N2-REQ-N1-001-v5

Status: `STRUCTURAL_INPUT_ACCEPTED`.

Frozen marker-three source:

- branch: `nova/factorial-structure`;
- commit: `ebb47ba436af554366d0f285119a769f31f9e561`;
- construction: `N1-CON-003`.

### N2-REQ-N1-002-v6

Status: `OPEN_AVERAGE_INTERNAL_GAP`.

Under N2-ADD-123, define

\[
D_t=\left\lfloor\frac{F_{t-1}}{2^{t-1}}\right\rfloor,
\qquad
\eta_t=\frac{U_t}{K_tD_t}.
\]

Provide one of:

1. pointwise lower bounds `eta_t>=rho_t` strong enough to force `Delta_n>=1`;
2. an averaged lower bound for the product of the exact utilization factors;
3. pointwise or averaged upper bounds strong enough to force `Delta_n<1` and retire N2-ADD-120;
4. an explicit divisor-spacing theorem that implies either bound.

The first external blocking gap is not an acceptable substitute. N2-OBS-109 proves that identical `(D_t,K_t,g_t)` data can coexist with utilization tending to zero or one.

Latest inspected source:

- branch: `nova/factorial-structure`;
- head inspected: `8c7ee8f64af56a8d082f1fa3adabb0b0309f6e27`;
- handoff source commit: `6b31a320fa4c4bd4c9b2395e60faa174198e022e`;
- handoff: `N1-HO-N2-009`.

### N2-REQ-N1-003-v2

Status: `OPEN`.

Provide target-local collision-energy or maximum-fiber upper bounds for sums in `[q-W_n,q]`.

## Nova 3 requirements

### N2-REQ-N3-001-v5

Status: `PARTIALLY_CLOSED`.

Tilt existence, uniqueness, span one, exact resonances, and post-prefix tilt compression are accepted with restrictions.

### N2-REQ-N3-002-v5

Status: `OPEN`.

Prove uniform numerical variance, third-moment, maximal-step, and endpoint-collapse bounds.

### N2-REQ-N3-003-v5

Status: `OPEN`.

Prove aggregate phase dispersion for the complete tilted odd-core menus on the required minor arcs.

### N2-REQ-N3-004-v4

Status: `OPEN`.

Construct a collision-aware integer reference law or target-local energy bound and prove the strict weighted Fourier inequality.

### N2-REQ-N3-005

Status: `OPEN`.

No logarithmic divisor theorem transfers to numerical additive sums without a separate proved bridge.

## Nova 4 requirements

### N2-REQ-N4-001-v4

Status: `OPEN`.

Independently replay the marker-three structural gate from commit `ebb47ba436af554366d0f285119a769f31f9e561`.

### N2-REQ-N4-002-v7

Status: `PARTIALLY_CLOSED_BY_NOVA2_AND_NOVA1`.

Independently reconstruct:

- N2-ADD-119 through N2-ADD-123;
- N2-OBS-109;
- finite certificates through `n=55`;
- the dual-partition replays at `n=53` and `n=55`.

### N2-REQ-N4-003-v7

Status: `OPEN`.

Extend exact complete-core certification from

\[
n=56.
\]

Resource limits must remain fail-closed and are not counterexamples.

### N2-REQ-N4-004-v4

Status: `OPEN`.

For feasible ranges, compute full restricted sumsets and report support size, collision multiplicity, maximum downward gap, first empty window, and exact witnesses.

### N2-REQ-N4-005-v3

Status: `OPEN`.

Audit endpoint-window support. Total maximum support above `Y_n` does not prove every required downward window is occupied.

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

### N2-REQ-INT-002-v7

Status: `FINITE_RANGE_CLOSED_THROUGH_N55`.

The sharp finite bounds are

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le22
\quad(12\le n\le54)
\]

and

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le23
\quad(12\le n\le55).
\]

Extend from `n=56` only as a finite auxiliary program.

### N2-REQ-INT-003-v6

Status: `OPEN_AVERAGE_INTERNAL_GAP`.

Use N2-ADD-123 to prove lower or upper bounds for `eta_t=U_t/(K_tD_t)`. First-blocking-gap estimates are retired by N2-OBS-109.

### N2-REQ-INT-004-v4

Status: `OPEN`.

Upper-bound target-local collision multiplicity or additive energy.

### N2-REQ-INT-005-v3

Status: `OPEN`.

Compare collision-aware bounded-torus Fourier positivity and deterministic final restricted-sumset growth on identical labels.

### N2-REQ-INT-006

Status: `OPEN`.

Prove the bulk and deterministic endpoint regimes cover every target with no transition gap.

## Rule

Every result must use an allowed evidence label. Failure of a sufficient proof engine must not be promoted to failure of the complete marker-three model.