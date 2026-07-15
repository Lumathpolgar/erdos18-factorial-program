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

Accepted structural facts:

- legal marker-three main divisors;
- exact 2-adic layer separation;
- main-palette numerical disjointness;
- exact main lattice `3 Z`;
- quotient span one;
- exact correction radius and downward-window reduction;
- selected-term cost `M_n+r_n`.

Response: `handoffs/RESPONSE_TO_NOVA1_MARKER_THREE.md`.

### N2-REQ-N1-002-v3

Requirement status: `OPEN`

Provide uniform endpoint and odd-core gap information for the marker-three model:

1. lower bounds for the largest reachable quotient sum;
2. explicit large-core subfamilies in every layer;
3. uniform control of consecutive gaps between odd divisors of `n!/3`;
4. exact thresholds for inclusion of all odd cores through `m_n`;
5. finite exceptions.

A support maximum below `Y_n-W_n` disproves the frozen model.

### N2-REQ-N1-003

Requirement status: `SUPERSEDED`

Nova 2's earlier three-power repair contract `N2-HO-N1-002` is superseded as the preferred route by `N1-CON-003`. N2-ADD-116 through N2-ADD-118 remain valid as a fallback chain.

## Requirements from Nova 3

### N2-REQ-N3-001-v4

Requirement status: `OPEN`

For the exact numerical marker-three quotient labels

\[
B_t(n)=\{2^{t-1}u:u\text{ odd},\ 3u\mid n!,\ 2^{t-1}u\le Y_n\},
\]

construct or reject a target-dependent exponential product law centered in

\[
I_{n,q}=[\max(0,q-W_n),q].
\]

State the exact bulk target range and every endpoint exclusion.

### N2-REQ-N3-002-v4

Requirement status: `OPEN`

Prove explicit uniform bounds for:

- variance;
- third absolute centered moment;
- maximal numerical step;
- maximal-step to standard-deviation ratio;
- lower and upper endpoint collapse.

These must concern numerical quotient values, not logarithms.

### N2-REQ-N3-003-v4

Requirement status: `OPEN`

Determine the exact additive span and every resonance of

\[
\Phi_{n,q}(\theta)=\mathbb E e^{i\theta T_{n,q}}
\]

on `[-pi,pi]`. The fact that `1 in B_1(n)` proves span one but does not prove quantitative minor-arc decay.

### N2-REQ-N3-004-v3

Requirement status: `OPEN`

Provide an explicit integer-valued reference law `G_{n,q}` and prove

\[
\int_{-\pi}^{\pi}
|\Phi_{n,q}(\theta)-\Psi_{n,q}(\theta)|
\left|
\sum_{a\in I_{n,q}}e^{-ia\theta}
\right|d\theta
<
2\pi G_{n,q}(I_{n,q})
\]

for every declared bulk target.

Exact request: `handoffs/MARKER_THREE_REQUEST_TO_NOVA3.md`.

### N2-REQ-N3-005

Requirement status: `OPEN`

Any use of logarithmic divisor theorems must include a separate proved transfer to the numerical additive quotient law.

## Requirements from Nova 4

### N2-REQ-N4-001-v4

Requirement status: `OPEN`

Independently replay the marker-three structural gate from Nova 1 commit

`ebb47ba436af554366d0f285119a769f31f9e561`.

Return separate verdicts for legality, distinctness, lattice, quotient span, correction coverage, quotient reduction, and term count.

### N2-REQ-N4-002-v4

Requirement status: `PARTIALLY_CLOSED_BY_NOVA2`

Nova 2 has implemented N2-ADD-120 and certified exact connected-core reach for every `12<=n<=46`.

Nova 4 must independently reconstruct:

- N2-ADD-119 carrier blocks;
- N2-ADD-120 recursion;
- N2-ADD-121 unique-parent divisor stream;
- N2-FIN-202 for `12<=n<=45`;
- N2-FIN-203 at `n=46`.

For each layer return the largest core connected to zero, the first blocking gap, its two endpoints, the certified carrier endpoint, and the final comparison with `Y_n`.

### N2-REQ-N4-003-v4

Requirement status: `OPEN`

Extend the exact bounded-memory audit from the smallest unaudited parameter

\[
n=47.
\]

A resource limit must be reported as `unknown due to resource limits`, not as a counterexample. Failure of the carrier recursion is failure of one proof engine unless the full restricted sumset is also shown to miss a required window.

### N2-REQ-N4-004-v3

Requirement status: `OPEN`

For feasible exact ranges, compute the full marker-three restricted sumset and report:

- layer sizes;
- formal profile count;
- number of distinct sums;
- collision multiplicity;
- maximum downward gap;
- first empty target window;
- exact witnesses;
- full versus reduced menu status.

A reduced-menu failure is not a full-model counterexample.

### N2-REQ-N4-005-v2

Requirement status: `OPEN`

Audit endpoint support. If the exact maximum reachable quotient is below `Y_n-W_n`, return the smallest endpoint counterexample and classify the marker-three model as disproved.

Exact requests:

- `handoffs/MARKER_THREE_REQUEST_TO_NOVA4.md`;
- `handoffs/FULL_MENU_FINITE_TO_NOVA4.md`.

## Archive requirement

### N2-REQ-ARC-001

Requirement status: `OPEN`

Import the source-level Phase 12M through 12P theorem statements so their exact hypotheses can be audited rather than inferred from summaries.

## Internal Nova 2 requirements

### N2-REQ-INT-001-v5

Requirement status: `OPEN`

Prove or disprove

\[
Q_n\cap[q-W_n,q]\ne\varnothing
\]

for every

\[
W_n+1\le q\le Y_n
\]

uniformly for all sufficiently large `n`.

### N2-REQ-INT-002-v4

Requirement status: `FINITE_RANGE_CLOSED_THROUGH_N46`

N2-FIN-202 and N2-FIN-203 certify the N2-ADD-120 carrier criterion for every `12<=n<=46`. Extend from `n=47`, or prove a uniform record-gap theorem.

### N2-REQ-INT-003-v3

Requirement status: `OPEN`

Audit N2-ADD-120 against the exact Phase 12P hypotheses. Do not label a sequential proof as final-only.

### N2-REQ-INT-004-v3

Requirement status: `OPEN`

Control collision collapse between different marker-three rainbow profiles. Formal capacity is not support cardinality.

### N2-REQ-INT-005-v2

Requirement status: `OPEN`

Compare the two preferred asymptotic engines on the same marker-three labels:

1. target-dependent bounded-torus Fourier positivity;
2. deterministic final restricted-sumset growth.

Retain the weakest valid theorem proving every target window occupied.

### N2-REQ-INT-006

Requirement status: `OPEN`

Prove that the bulk and deterministic endpoint regimes cover every quotient target with no transition gap.

### N2-REQ-INT-007-v2

Requirement status: `OPEN`

Finite carrier coverage is exact for `12<=n<=46`. Certify all smaller exceptions and extend the upper finite boundary as resources permit.

## Rule

Every theorem, finite certificate, computation, heuristic, or disproved architecture must use an allowed evidence label. No target may be omitted, no labeled duplicate may be treated as a distinct numerical divisor, and failure of a sufficient proof engine must not be promoted to failure of the full model.
