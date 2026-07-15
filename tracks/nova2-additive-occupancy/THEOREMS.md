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

## Conditional theorem

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

## Cross-track decisions

- `N1-HO-N2-001`: `REJECTED` at Nova 1 commit `b939574eb88a08bb03abda5bbe6ff2ca97444e08`.
- Reason: all main sums lie in `2^{r_n+1} Z`, while the first requested window is `[1,2^{r_n}]`.
- Response: `handoffs/RESPONSE_TO_NOVA1.md`.

## Open factorial instantiation nodes

- N2-OPEN-201-v2: obtain a revised fixed factorial label family whose common lattice span and correction radius are compatible.
- N2-OPEN-202: prove a uniform target-dependent tilt and variance theorem in the bulk for an accepted additive-value layer law.
- N2-OPEN-203: prove the weighted major-minor arc inequality on the integer torus `[-pi,pi]`.
- N2-OPEN-204: cover excluded endpoint regimes deterministically.
- N2-OPEN-205: certify finite exceptions.
- N2-OPEN-206: verify that any imported theorem for `log d` has a proved transfer to additive numerical sums before use.

## Promotion rule

No conditional theorem becomes a proved factorial theorem until all structural, analytic, endpoint, and finite-exception nodes are proved and independently reconstructed.