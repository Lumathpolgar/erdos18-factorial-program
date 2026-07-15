# Nova 2 Open Requirements

## Requirements from Nova 1

### N2-REQ-N1-001-v5

Requirement status: `STRUCTURAL_INPUT_ACCEPTED`

Accepted source:

- branch: `nova/factorial-structure`
- exact commit: `ebb47ba436af554366d0f285119a769f31f9e561`
- construction: `N1-CON-003`
- handoff: `N1-HO-N2-002`
- Nova 2 outcome: `ACCEPTED_WITH_RESTRICTIONS`

Accepted facts include legal marker-three divisors, exact 2-adic layer separation, main-palette disjointness, exact main lattice `3 Z`, quotient span one, exact correction reduction, and term cost `M_n+r_n`.

### N2-REQ-N1-002-v4

Requirement status: `OPEN`

Provide a pointwise or averaged theorem for complete zero-connected prefix cardinalities `K_t` under the exact thresholds

\[
D_t=\left\lfloor\frac{E_{t-1}+W_n+1}{2^{t-1}}\right\rfloor.
\]

By accepted theorem `N1-OBS-003`, sequential carrier success requires

\[
\prod_{t=1}^{L}(1+K_t)
\ge
\frac{Y_n+1}{W_n+1}.
\]

For `n>=120368`, the geometric mean must be at least

\[
\exp\left(\frac{n}{85\log n}\right).
\]

A lower bound meeting this requirement would support N2-ADD-120. A uniform upper bound below it would retire that sequential engine.

Exact source:

- handoff head: `471c7122cb2ac96402d133b5af91c97a2f00a23c`;
- proof commit: `ac676b0fc9007117da1f1d9eaeec3e3cf65dd1e7`;
- Nova 2 response: `handoffs/RESPONSE_TO_NOVA1_CONNECTED_PREFIX.md`.

### N2-REQ-N1-003-v2

Requirement status: `OPEN`

Provide target-local collision-energy or maximum-fiber upper bounds for sums in `[q-W_n,q]`. Nova 1 theorem `N1-COL-001` proves large fibers exist, so raw profile count is not support cardinality.

### N2-REQ-N1-004

Requirement status: `SUPERSEDED`

The earlier three-power repair remains a valid fallback but is not the preferred route.

## Requirements from Nova 3

### N2-REQ-N3-001-v5

Requirement status: `PARTIALLY_CLOSED`

Nova 3 has proved existence and uniqueness of the numerical centering tilt, span one, exact resonance set `{0}`, and post-prefix tilt compression. The active range remains the exact final-only post-prefix interval.

### N2-REQ-N3-002-v5

Requirement status: `OPEN`

Prove explicit uniform numerical bounds for variance, third centered moment, maximal step, and endpoint collapse on the marker-three quotient law.

### N2-REQ-N3-003-v5

Requirement status: `OPEN`

Prove aggregate phase dispersion for the complete tilted odd-core menus. With

\[
\mathcal D_{t,\lambda}(\theta)
=
\sum_{a,b}p_t(a)p_t(b)
\sin^2\left(\frac{(a-b)\theta}{2}\right),
\]

establish a lower bound strong enough to control

\[
|\Phi_{n,\lambda}(\theta)|^2
\le
\exp\left(-2\sum_t\mathcal D_{t,\lambda}(\theta)\right)
\]

on the required minor arcs.

### N2-REQ-N3-004-v4

Requirement status: `OPEN`

Construct a collision-aware integer reference law or target-local energy bound and prove the strict weighted Fourier inequality for every declared bulk target.

### N2-REQ-N3-005

Requirement status: `OPEN`

No logarithmic divisor theorem may be transferred to numerical additive sums without a separate proved bridge.

Exact request: `handoffs/MARKER_THREE_REQUEST_TO_NOVA3.md`.

## Requirements from Nova 4

### N2-REQ-N4-001-v4

Requirement status: `OPEN`

Independently replay the marker-three structural gate from Nova 1 commit `ebb47ba436af554366d0f285119a769f31f9e561`.

### N2-REQ-N4-002-v5

Requirement status: `PARTIALLY_CLOSED_BY_NOVA2_AND_NOVA1`

Independently reconstruct:

- N2-ADD-119 carrier blocks;
- N2-ADD-120 recursion;
- N2-ADD-121 unique-parent stream;
- N2-FIN-202 for `12<=n<=45`;
- N2-FIN-203 at `n=46`;
- accepted Nova 1 finite certificate `N1-FIN-005` for `46<=n<=50`.

The Nova 1 `n=46` overlap matches N2-FIN-203 exactly.

### N2-REQ-N4-003-v5

Requirement status: `OPEN`

Extend exact complete-core finite certification from the smallest unaudited parameter

\[
n=51.
\]

Resource limits must remain fail-closed and must not be reported as counterexamples.

### N2-REQ-N4-004-v3

Requirement status: `OPEN`

For feasible ranges, compute full restricted sumsets and report numerical support size, collision multiplicity, maximum downward gap, first empty target window, and exact witnesses. A reduced-menu failure is not a full-model counterexample.

### N2-REQ-N4-005-v2

Requirement status: `OPEN`

Audit endpoint-window support. Total maximum support above `Y_n` is insufficient unless every required downward window is occupied.

Exact requests:

- `handoffs/MARKER_THREE_REQUEST_TO_NOVA4.md`;
- `handoffs/FULL_MENU_FINITE_TO_NOVA4.md`;
- `handoffs/STREAMING_N46_TO_NOVA4.md`.

## Archive requirement

### N2-REQ-ARC-001

Requirement status: `OPEN`

Import the source-level Phase 12M through 12P statements so their exact hypotheses can be audited rather than inferred from summaries.

## Internal Nova 2 requirements

### N2-REQ-INT-001-v5

Requirement status: `OPEN`

Prove or disprove

\[
Q_n\cap[q-W_n,q]\ne\varnothing
\]

for every `W_n+1<=q<=Y_n`, uniformly for all sufficiently large `n`.

### N2-REQ-INT-002-v5

Requirement status: `FINITE_RANGE_CLOSED_THROUGH_N50`

N2-FIN-202, N2-FIN-203, and accepted N1-FIN-005 certify complete-core carrier coverage for every `12<=n<=50`. Extend from `n=51`.

### N2-REQ-INT-003-v4

Requirement status: `OPEN`

Prove the connected-prefix product requirement is attainable under exact thresholds, or prove an upper bound retiring N2-ADD-120. Separately audit any asymptotic sequential proof against Phase 12P.

### N2-REQ-INT-004-v4

Requirement status: `OPEN`

Upper-bound target-local collision multiplicity or additive energy. Formal profile capacity is not numerical support cardinality.

### N2-REQ-INT-005-v3

Requirement status: `OPEN`

Compare the final-only engines on the same marker-three labels:

1. collision-aware target-dependent bounded-torus Fourier positivity;
2. deterministic final restricted-sumset growth.

### N2-REQ-INT-006

Requirement status: `OPEN`

Prove that bulk and deterministic endpoint regimes cover every quotient target with no transition gap.

### N2-REQ-INT-007-v3

Requirement status: `OPEN`

Exact carrier coverage is established for `12<=n<=50`. Certify smaller exceptions and extend the upper finite boundary from `n=51` only as a finite auxiliary program.

## Rule

Every theorem, finite certificate, computation, heuristic, or disproved architecture must use an allowed evidence label. Failure of a sufficient proof engine must not be promoted to failure of the full marker-three model.
