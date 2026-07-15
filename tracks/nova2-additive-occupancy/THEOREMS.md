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
| N2-ADD-115 | proved theorem | A subset of `g Z` cannot meet all downward windows of radius below `g-1`; applying this to the first Nova 1 layers gives an exact first-target failure | `proofs/VALUATION_TAGGED_LATTICE_OBSTRUCTION.md` |
| N2-ADD-116 | proved theorem | If `S subseteq g Z` and corrections cover `[0,Lg-1]`, exact original-target coverage is equivalent to quotient downward gaps at most `L-1` | `proofs/LATTICE_QUOTIENT_NORMALIZATION.md` |

## Conditional theorems

### N2-ADD-114

- Result label: `conditional theorem`
- Statement: fixed legal pairwise-disjoint factorial labels, a disjoint correction palette, and a strict weighted Fourier comparison for every target window imply
  \[
  H_{n!}(\lfloor\sqrt{n!}\rfloor+1)=O((\log n)^2).
  \]
- Dependencies: N2-ADD-108, N2-ADD-110, N2-ADD-112.
- Constants effective: yes, if the structural and Fourier inputs are effective.
- Distinctness mechanism: pairwise disjoint main labels and correction palette.
- Boundary treatment: lower endpoint by correction; upper endpoint included in the Fourier hypothesis; finite `n<n_0` open.
- Proof: `proofs/CANDIDATE_OCCUPANCY_THEOREM.md`.

### N2-ADD-117

- Result label: `conditional theorem`
- Source construction: Nova 1 full-menu valuation-tagged address packets, inspected at head `fa11f4b2cb86a2dd791df189ada12757be791804`.
- Normalization:
  \[
  g_n=2^{r_n+1},
  \qquad
  R_n=g_nQ_n.
  \]
- Repaired correction palette:
  \[
  C_n^+=\{2^0,2^1,\ldots,2^{r_n+2}\},
  \]
  representing `[0,4g_n-1]`.
- Exact open hypothesis:
  \[
  Q_n\cap[\max(0,m-3),m]\ne\varnothing
  \]
  for every integer
  \[
  0\le m\le\lfloor X_n/g_n\rfloor.
  \]
- Conclusion:
  \[
  H_{n!}(X_n+1)
  \le
  M_n+r_n+3
  =O((\log n)^2).
  \]
- Structural dependency: Nova 1 must accept or supersede the repair and certify the three added powers, quotient identity, and finite exceptions.
- Analytic dependency: exact additive numerical-value tilt and bounded-torus weighted Fourier theorem, or a deterministic quotient covering theorem.
- Proof: `proofs/LATTICE_QUOTIENT_NORMALIZATION.md`.

## Disproved models

| ID | Result label | Statement | Location |
|---|---|---|---|
| N2-OBS-101 | disproved model | Raw profile capacity alone forces coverage | `models/TOY_COUNTEREXAMPLES.md` |
| N2-OBS-102 | disproved model | Proper-lattice supports can cover every consecutive target | `models/TOY_COUNTEREXAMPLES.md` |
| N2-OBS-103 | disproved model | Positive ordinary convolution mass always respects numerical distinctness | `models/TOY_COUNTEREXAMPLES.md` |
| N2-OBS-104 | disproved model | A Gaussian-looking or weak local approximation forces every atom or window positive | `models/TOY_COUNTEREXAMPLES.md` |
| N2-OBS-105 | disproved model | A bulk tilted local theorem remains uniform to both support endpoints | `models/TOY_COUNTEREXAMPLES.md` |
| N2-OBS-106 | disproved model | Separate target-dependent probability spaces define one universal random object | `models/TOY_COUNTEREXAMPLES.md` |
| N2-OBS-107 | disproved model | The exact valuation-tagged occupancy request `N1-HO-N2-001` covers every target with radius `2^{r_n}-1` | `proofs/VALUATION_TAGGED_LATTICE_OBSTRUCTION.md` |
| N2-OBS-108 | disproved model | Adding only one or two consecutive binary powers above the original palette repairs the valuation-tagged initial support gap | `proofs/LATTICE_QUOTIENT_NORMALIZATION.md` |

## Cross-track decisions and contracts

### Nova 1 original handoff

- Handoff: `N1-HO-N2-001`.
- Source branch: `nova/factorial-structure`.
- Source commit: `b939574eb88a08bb03abda5bbe6ff2ca97444e08`.
- Outcome: `REJECTED`.
- Reason: all main sums lie in `2^{r_n+1} Z`, while the first requested window is `[1,2^{r_n}]`.
- Response: `handoffs/RESPONSE_TO_NOVA1.md`.

### Nova 1 repair contract

- Handoff: `N2-HO-N1-002`.
- Source head inspected: `fa11f4b2cb86a2dd791df189ada12757be791804`.
- Status: awaiting receiver decision.
- Exact proposal: retain the main labels, add correction powers through `2^{r_n+2}`, and version the quotient four-point theorem.
- Contract: `handoffs/REPAIR_CONTRACT_TO_NOVA1.md`.

### Nova 3 prior handoff

- Handoff: `N3-HO-N2-001`.
- Source branch: `nova/analytic-density`.
- Source commit: `0ce88b28dc2e6641093526f5777bb31f658e3515`.
- Outcome: `ACCEPTED_WITH_RESTRICTIONS`.
- Accepted domain: the stated results for logarithmic divisor size and the obstruction to unbounded-frequency pointwise decay.
- Prohibited transfer: no theorem for `log d` may be used as a theorem for additive numerical sums without a separate proved compatibility result.
- Response: `handoffs/RESPONSE_TO_NOVA3.md`.

### Nova 3 quotient request

- Handoff: `N2-HO-N3-002`.
- Status: conditional on Nova 1 structural acceptance.
- Exact law: target-dependent exponential tilt on the normalized numerical labels `B_t(n)`.
- Exact inversion domain: `[-pi,pi]`.
- Exact target window: `[max(0,m-3),m]`.
- Request: `handoffs/QUOTIENT_REQUEST_TO_NOVA3.md`.

## Open factorial instantiation nodes

- N2-OPEN-201-v3: obtain Nova 1 acceptance or a versioned superseding construction for the three-power quotient repair.
- N2-OPEN-202-v2: prove a uniform target-dependent tilt and variance theorem for the normalized additive-value layer law.
- N2-OPEN-203-v2: prove the weighted major-minor arc inequality for every four-point quotient window on `[-pi,pi]`.
- N2-OPEN-204-v2: cover all quotient endpoint regimes omitted by the analytic theorem.
- N2-OPEN-205: certify finite exceptions.
- N2-OPEN-206: verify that any imported theorem for `log d` has a proved transfer to additive numerical sums before use.
- N2-OPEN-207: independently prove or disprove that the final normalized rainbow sumset has maximum downward gap at most `3`.

## Promotion rule

No conditional theorem becomes a proved factorial theorem until all structural, analytic or deterministic occupancy, endpoint, and finite-exception nodes are proved and independently reconstructed.
