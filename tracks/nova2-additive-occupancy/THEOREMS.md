# Nova 2 Theorem Registry

## Proved theorems

| ID | Result label | Statement summary | Proof location |
|---|---|---|---|
| N2-ADD-101 | proved theorem | More legal profiles than targets does not imply coverage | `models/TOY_COUNTEREXAMPLES.md` |
| N2-ADD-102 | proved theorem | A common gcd confines all rainbow sums to a proper lattice | `models/TOY_COUNTEREXAMPLES.md` |
| N2-ADD-103 | proved theorem | Ordinary convolution mass can come only from an illegal repeated divisor | `models/TOY_COUNTEREXAMPLES.md` |
| N2-ADD-104 | proved theorem | Pointwise approximation error must be smaller than the reference atom to force positivity | `models/TOY_COUNTEREXAMPLES.md` |
| N2-ADD-105 | proved theorem | Window approximation error must be smaller than the reference window mass | `models/TOY_COUNTEREXAMPLES.md` |
| N2-ADD-106 | proved theorem | Tilted Bernoulli variance is at most `a_max min(m,A-m)` | `models/TOY_COUNTEREXAMPLES.md` |
| N2-ADD-108 | proved theorem | Positive collision-free convolution mass gives a deterministic legal representation | `models/TOY_SUFFICIENT_CONDITIONS.md` |
| N2-ADD-109 | proved theorem | `M exp(-L p_min)` controls sampled-catalogue failure over `M` targets | `models/TOY_SUFFICIENT_CONDITIONS.md` |
| N2-ADD-110 | proved theorem | Strict weighted Fourier discrepancy below reference window mass implies occupancy | `models/TOY_SUFFICIENT_CONDITIONS.md` |
| N2-ADD-111 | proved theorem | Explicit lower bound for a discretized-Gaussian window | `models/TOY_SUFFICIENT_CONDITIONS.md` |
| N2-ADD-112 | proved theorem | Main-window occupancy plus a disjoint correction palette gives exact coverage | `models/TOY_SUFFICIENT_CONDITIONS.md` |
| N2-ADD-113 | proved theorem | Positive point mass gives targetwise extraction for fixed legal labels | `models/TOY_SUFFICIENT_CONDITIONS.md` |
| N2-ADD-115 | proved theorem | A subset of `g Z` cannot meet all downward windows of radius below `g-1`; the first Nova 1 construction fails at its first requested window | `proofs/VALUATION_TAGGED_LATTICE_OBSTRUCTION.md` |
| N2-ADD-116 | proved theorem | If `S subseteq g Z` and corrections cover `[0,Lg-1]`, exact original-target coverage is equivalent to quotient downward gaps at most `L-1` | `proofs/LATTICE_QUOTIENT_NORMALIZATION.md` |
| N2-ADD-118 | proved theorem | The three-power fallback has an exponentially long binary-spine prefix with four-point occupancy through `3*2^{M_n}` | `proofs/QUOTIENT_BINARY_SPINE_PREFIX.md` |
| N2-ADD-119 | proved theorem | Translated carrier blocks preserve downward window density when scaled carrier gaps are at most the previous reach plus the correction width and one | `proofs/MARKER_THREE_CARRIER_BLOCK_REDUCTION.md` |

## Conditional theorems

### N2-ADD-114

Fixed legal pairwise-disjoint factorial labels, a disjoint correction palette, and a strict weighted Fourier comparison for every target window imply

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)=O((\log n)^2).
\]

Dependencies: N2-ADD-108, N2-ADD-110, N2-ADD-112.

Proof: `proofs/CANDIDATE_OCCUPANCY_THEOREM.md`.

### N2-ADD-117

For the normalized first valuation-tagged model, extending the correction palette through `2^{r_n+2}` reduces the factorial theorem to four-point quotient occupancy and gives the conditional bound

\[
H_{n!}(X_n+1)\le M_n+r_n+3.
\]

This remains a valid conditional fallback, but it is no longer the preferred construction after the marker-three handoff.

Proof: `proofs/LATTICE_QUOTIENT_NORMALIZATION.md`.

### N2-ADD-120

For the marker-three construction, let `E_0=0`. At layer `t`, connect consecutive cores from zero whenever their gap is at most

\[
D_t(E_{t-1})
=
\left\lfloor
\frac{E_{t-1}+W_n+1}{2^{t-1}}
\right\rfloor.
\]

If `u_t^*` lies in the connected component of zero and

\[
E_t=E_{t-1}+2^{t-1}u_t^*,
\]

then the quotient sumset is downward `W_n`-dense through `E_{M_n}` and covers required windows through `E_{M_n}+W_n`. If this reaches

\[
Y_n=\lfloor X_n/3\rfloor,
\]

then

\[
H_{n!}(X_n+1)\le M_n+r_n.
\]

This is a sequential sufficient condition and must undergo an exact Phase 12P compatibility audit before asymptotic promotion.

Proof: `proofs/MARKER_THREE_CARRIER_BLOCK_REDUCTION.md`.

## Finite certificates

### N2-FIN-201

A rigorous rational-log scan found the first parameter satisfying the old valuation budget at `n=1892`, with `r_n=31` and `M_n=911`. This certificate belongs to the superseded fallback route and remains valid as a recorded finite audit.

Verification: `verification/quotient_binary_spine.py`.

## Disproved models

| ID | Result label | Statement | Location |
|---|---|---|---|
| N2-OBS-101 | disproved model | Raw profile capacity alone forces coverage | `models/TOY_COUNTEREXAMPLES.md` |
| N2-OBS-102 | disproved model | Proper-lattice supports can cover every consecutive target | `models/TOY_COUNTEREXAMPLES.md` |
| N2-OBS-103 | disproved model | Positive ordinary convolution mass always respects numerical distinctness | `models/TOY_COUNTEREXAMPLES.md` |
| N2-OBS-104 | disproved model | A Gaussian-looking or weak local approximation forces every atom or window positive | `models/TOY_COUNTEREXAMPLES.md` |
| N2-OBS-105 | disproved model | A bulk tilted local theorem remains uniform to both support endpoints | `models/TOY_COUNTEREXAMPLES.md` |
| N2-OBS-106 | disproved model | Separate target-dependent probability spaces define one universal random object | `models/TOY_COUNTEREXAMPLES.md` |
| N2-OBS-107 | disproved model | The exact first valuation-tagged request covers every target with radius `2^{r_n}-1` | `proofs/VALUATION_TAGGED_LATTICE_OBSTRUCTION.md` |
| N2-OBS-108 | disproved model | Adding only one or two consecutive binary powers repairs the first valuation-tagged construction | `proofs/LATTICE_QUOTIENT_NORMALIZATION.md` |

## Cross-track decisions

### Nova 1 original handoff

- Handoff: `N1-HO-N2-001`.
- Source commit: `b939574eb88a08bb03abda5bbe6ff2ca97444e08`.
- Outcome: `REJECTED`.
- Response: `handoffs/RESPONSE_TO_NOVA1.md`.

### Nova 1 marker-three handoff

- Handoff: `N1-HO-N2-002`.
- Source branch: `nova/factorial-structure`.
- Source commit: `ebb47ba436af554366d0f285119a769f31f9e561`.
- Construction: `N1-CON-003`.
- Outcome: `ACCEPTED_WITH_RESTRICTIONS`.
- Response: `handoffs/RESPONSE_TO_NOVA1_MARKER_THREE.md`.
- Preferred status: promoted to Nova 2's primary factorial model.

### Nova 2 three-power repair contract

- Handoff: `N2-HO-N1-002`.
- Outcome after `N1-CON-003`: `SUPERSEDED` as the preferred architecture.
- Theorems N2-ADD-116 through N2-ADD-118 remain valid and preserved.

### Nova 3

- Prior handoff `N3-HO-N2-001`: `ACCEPTED_WITH_RESTRICTIONS` for logarithmic results only.
- New exact request: `N2-HO-N3-003`.
- Frozen law: numerical marker-three quotient sums on `[-pi,pi]`.
- File: `handoffs/MARKER_THREE_REQUEST_TO_NOVA3.md`.

### Nova 4

- Prior lattice service at commit `82358ea18277d36475db0a7ae81d6a68d7a49c59`: accepted for the old obstruction only.
- New exact request: `N2-HO-N4-002`.
- Files: `handoffs/RESPONSE_TO_NOVA4.md`, `handoffs/MARKER_THREE_REQUEST_TO_NOVA4.md`.

## Open factorial nodes

- N2-OPEN-301: prove or disprove marker-three quotient occupancy through `Y_n`.
- N2-OPEN-302: compute or prove connected-core reach under N2-ADD-120.
- N2-OPEN-303: prove endpoint support near `Y_n` or produce an exact endpoint deficit.
- N2-OPEN-304: control total-sum collisions beyond formal profile capacity.
- N2-OPEN-305: prove the numerical target-dependent tilt, moments, resonance decomposition, and weighted Fourier inequality.
- N2-OPEN-306: audit N2-ADD-120 against the exact Phase 12P hypotheses.
- N2-OPEN-307: certify finite exceptions.

## Promotion rule

No conditional theorem becomes a proved factorial theorem until all structural, additive or analytic, endpoint, distinctness, and finite-exception nodes are proved and independently reconstructed.