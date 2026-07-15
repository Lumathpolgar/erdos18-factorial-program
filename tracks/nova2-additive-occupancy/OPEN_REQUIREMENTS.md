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

The accepted structural facts are:

- legal marker-three main divisors;
- exact 2-adic layer separation;
- main-palette numerical disjointness;
- exact main lattice `3 Z`;
- quotient span one;
- exact correction radius and downward-window reduction;
- selected-term cost `M_n+r_n`.

Response:

`handoffs/RESPONSE_TO_NOVA1_MARKER_THREE.md`.

### N2-REQ-N1-002-v2

Requirement status: `OPEN`

Provide exact endpoint information for the marker-three quotient model:

1. lower bounds for the largest reachable quotient sum;
2. upper bounds sufficient to detect endpoint deficit;
3. explicit large-core subfamilies in each layer;
4. exact thresholds for inclusion of all odd cores through `m_n`;
5. any structural theorem controlling gaps between admissible odd cores;
6. finite exceptions.

A support maximum below `Y_n-W_n` disproves the frozen model.

### N2-REQ-N1-003

Requirement status: `SUPERSEDED`

Nova 2's earlier three-power repair contract `N2-HO-N1-002` is superseded as the preferred route by `N1-CON-003`. N2-ADD-116 through N2-ADD-118 remain valid and preserved as a fallback chain.

## Requirements from Nova 3

### N2-REQ-N3-001-v4

Requirement status: `OPEN`

For the exact marker-three quotient labels

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

on `[-pi,pi]`.

The fact that `1 in B_1(n)` proves span one but does not prove quantitative minor-arc decay.

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

Exact request:

`handoffs/MARKER_THREE_REQUEST_TO_NOVA3.md`.

### N2-REQ-N3-005

Requirement status: `OPEN`

Any use of logarithmic divisor theorems must include a separate proved transfer to the numerical additive quotient law. Without that bridge, the result is not an occupancy input.

## Requirements from Nova 4

### N2-REQ-N4-001-v3

Requirement status: `OPEN`

Independently replay the marker-three structural gate from Nova 1 commit

`ebb47ba436af554366d0f285119a769f31f9e561`.

Return separate verdicts for legality, distinctness, lattice, quotient span, correction coverage, quotient reduction, and term count.

### N2-REQ-N4-002-v4

Requirement status: `PARTIALLY_COMPLETED_BY_NOVA2`

Implement and independently reconstruct N2-ADD-120's connected-core recursion.

At layer `t`, compute

\[
D_t=
\left\lfloor
\frac{E_{t-1}+W_n+1}{2^{t-1}}
\right\rfloor,
\]

then return:

- the largest core connected to zero;
- the first blocking core gap;
- the exact two cores bordering the gap;
- the certified endpoint `E_t`;
- the final comparison of the occupied endpoint with `Y_n`.

Nova 2 completed this exact audit with full menus for every `12<=n<=45`. Nova 4 must independently replay N2-FIN-202. Failure of this recursion outside the completed range is failure of one proof engine only.

### N2-REQ-N4-003-v3

Requirement status: `OPEN`

For feasible exact ranges, compute the full marker-three quotient restricted sumset and report:

- layer sizes;
- profile count;
- number of distinct sums;
- collision multiplicity;
- maximum downward gap;
- first empty target window;
- exact witnesses;
- full versus reduced menu status.

A reduced-menu failure is not a full-model counterexample.

### N2-REQ-N4-004-v2

Requirement status: `OPEN`

Replay the deterministic protected prefix through

\[
m_n(2^{M_n}-1)+W_n.
\]

No counterexample may be reported at or below this bound.

### N2-REQ-N4-005

Requirement status: `OPEN`

Audit endpoint support. If the exact maximum reachable quotient is below `Y_n-W_n`, return the smallest endpoint counterexample and classify the marker-three model as disproved.

### N2-REQ-N4-006

Requirement status: `OPEN`

Independently reconstruct finite certificate `N2-FIN-202`:

- exact range: `12<=n<=45`;
- complete odd-core menus, not reduced menus;
- all 34 cases reach `Y_n`;
- layer-count transitions `2,3,4,5,6` on the frozen ranges;
- exact largest completed case at `n=45`;
- exact classification of `n=46` as resource-limited.

Then implement a bounded-memory or streaming sorted odd-divisor generator capable of continuing at `n=46`, whose exact odd-core count is `27,941,760`.

Frozen artifacts:

- `proofs/MARKER_THREE_FINITE_FULL_MENU_AUDIT.md`;
- `verification/marker_three_full_menu_audit.py`;
- `verification/data/marker_three_full_menu_n12_n45.manifest.json`;
- `verification/data/marker_three_full_menu_n12_n45.csv`.

Exact request:

`handoffs/MARKER_THREE_REQUEST_TO_NOVA4.md`.

## Archive requirement

### N2-REQ-ARC-001

Requirement status: `OPEN`

Import the source-level Phase 12M through 12P theorem statements so their exact hypotheses can be audited rather than inferred from summaries.

## Internal Nova 2 requirements

### N2-REQ-INT-001-v4

Requirement status: `OPEN`

Prove or disprove

\[
Q_n\cap[q-W_n,q]\ne\varnothing
\]

for every

\[
W_n+1\le q\le Y_n.
\]

### N2-REQ-INT-002-v4

Requirement status: `FINITE_RANGE_COMPLETED_ASYMPTOTIC_OPEN`

N2-FIN-202 proves that the connected-core recursion reaches `Y_n` for every `12<=n<=45` using complete odd-core menus.

Remaining task:

- continue exact certification from `n=46` using streaming generation;
- prove a uniform connected-core reach theorem; or
- produce an exact first failure beyond the completed range.

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

Prove the bulk and deterministic endpoint regimes cover every quotient target with no transition gap.

### N2-REQ-INT-007-v2

Requirement status: `PARTIALLY_COMPLETED`

Finite marker-three coverage is certified for `12<=n<=45`. Remaining finite-exception work includes `n<12`, any gap before an eventual asymptotic threshold, and independent reconstruction.

### N2-REQ-INT-008

Requirement status: `OPEN`

Derive a uniform lower bound on the connected core at each layer strong enough to force

\[
E_{M_n}+W_n\ge Y_n.
\]

The finite data suggests terminal-layer saturation, but that observation is computational evidence only until a divisor-gap theorem is proved.

## Rule

Every theorem, certificate, computation, heuristic, or disproved architecture must use an allowed evidence label. Requirements use requirement status. No target may be omitted, no labeled duplicate may be treated as a distinct numerical divisor, and failure of a sufficient proof engine must not be promoted to failure of the full model.
