# Nova 2 Additive Model Registry

## Model M3: Marker-three quotient occupancy

- Model ID: `N2-MOD-M3-001`.
- Result label: `conditional theorem` as a structural reduction.
- Rank: 1.
- Source branch: `nova/factorial-structure`.
- Source commit: `ebb47ba436af554366d0f285119a769f31f9e561`.
- Source construction: `N1-CON-003`.
- Nova 2 intake: `ACCEPTED_WITH_RESTRICTIONS`.
- Response: `handoffs/RESPONSE_TO_NOVA1_MARKER_THREE.md`.

Frozen quotient labels:

\[
B_t(n)=
\{2^{t-1}u:u\text{ odd},\ 3u\mid n!,\ 2^{t-1}u\le Y_n\}.
\]

Target window:

\[
[q-W_n,q],
\qquad
W_n=\left\lfloor\frac{2^{r_n}-3}{3}\right\rfloor.
\]

Conditional conclusion:

\[
H_{n!}(X_n+1)\le M_n+r_n.
\]

Structural advantages:

- exact main lattice `3 Z`;
- quotient span one;
- original binary correction palette;
- no main-palette collision;
- lower term cost than the three-power fallback;
- a much wider quotient correction window.

Main blockers:

- uniform final quotient occupancy;
- endpoint support near `Y_n`;
- profile-to-sum collision control;
- numerical additive Fourier estimates;
- finite exceptions.

## Engine M3-F: Final-only tilted Fourier occupancy

- Engine ID: `N2-ENG-M3-F`.
- Result label: `conditional theorem`.
- Rank inside Model M3: 1.
- Fixed labels: marker-three quotient labels.
- Target-dependent object: probability weights only.
- Characteristic function:
  \[
  \Phi_{n,q}(\theta)=\mathbb E e^{i\theta T_{n,q}},
  \qquad
  \theta\in[-\pi,\pi].
  \]
- Exact request: `handoffs/MARKER_THREE_REQUEST_TO_NOVA3.md`.
- Main blocker: strict weighted Fourier error below exact target-window reference mass.

This remains the preferred asymptotic engine because it tests the final sumset and does not impose sequential interval growth.

## Engine M3-D: Deterministic final restricted-sumset theorem

- Engine ID: `N2-ENG-M3-D`.
- Result label: `conditional theorem`.
- Rank inside Model M3: 2.
- Required conclusion: every final marker-three quotient window is occupied.
- Main blocker: available additive theorems do not automatically preserve labels, numerical distinctness, interval location, or factorial legality.

## Engine M3-C: Connected-core carrier recursion

- Engine ID: `N2-ENG-M3-C`.
- Result label: `conditional theorem`.
- Rank inside Model M3: 3.
- Theorems: N2-ADD-119 and N2-ADD-120.
- Proof: `proofs/MARKER_THREE_CARRIER_BLOCK_REDUCTION.md`.

At layer `t`, core gaps are tested against

\[
D_t(E_{t-1})
=
\left\lfloor
\frac{E_{t-1}+W_n+1}{2^{t-1}}
\right\rfloor.
\]

Strengths:

- exact integer criterion;
- preserves downward orientation;
- scalable without full sumset enumeration;
- gives explicit first blocking core gap.

Restrictions:

- sequential proof architecture;
- failure does not disprove the full model;
- requires exact Phase 12P compatibility audit.

Verification request: `handoffs/MARKER_THREE_REQUEST_TO_NOVA4.md`.

## Model QV: Three-power normalized valuation-tagged fallback

- Model ID: `N2-MOD-QV-001`.
- Result label: `conditional theorem` with proved prefix.
- Rank: 4.
- Status: `SUPERSEDED_AS_PREFERRED`, preserved as a valid fallback.
- Proofs: N2-ADD-116, N2-ADD-117, N2-ADD-118.
- File: `models/VALUATION_TAGGED_QUOTIENT_MODEL.md`.

The route is retained because its normalization, repair obstruction, and binary-spine theorem are exact. Marker-three is preferred because it has smaller lattice span, fewer correction terms, and a wider target window.

## Model U: Uniform rainbow convolution

- Result label: `heuristic`.
- Rank: 5.
- Main blocker: one fixed mean leaves endpoint windows in large-deviation tails.

## Fixed-law Fourier standalone route

- Result label: `heuristic` as a standalone architecture.
- Rank: 6.
- Fourier analysis remains useful inside target-dependent models, but a single fixed law is not expected to cover both support endpoints uniformly.

## Mandatory evaluation fields

Every future candidate must record:

1. exact fixed labels;
2. divisor legality;
3. numerical disjointness;
4. term budget;
5. support range and endpoint reach;
6. common lattice and quotient normalization;
7. exact target-window orientation and width;
8. moments and maximal step;
9. additive span and every resonance;
10. collision multiplicity;
11. deterministic prefix;
12. finite or asymptotic status;
13. whether the proof is final-only or sequential;
14. exact Phase 12P compatibility when sequential;
15. exact falsification task and source SHAs.