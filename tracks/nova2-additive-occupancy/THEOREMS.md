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
| N2-ADD-121 | proved theorem | The unique-parent exponent-vector heap emits every bounded odd factorial divisor exactly once in increasing order, and record gaps suffice to replay every carrier threshold | `proofs/MARKER_THREE_STREAMING_N46_AUDIT.md` |

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

### N2-FIN-202

The exact full odd-core menus were generated and audited for every integer

\[
12\le n\le45.
\]

For every audited `n`, the connected-core carrier recursion reaches

\[
Y_n=\left\lfloor\frac{\lfloor\sqrt{n!}\rfloor}{3}\right\rfloor
\]

using between two and six legal main layers. Therefore

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
\le k_n+r_n
\le22
\]

throughout the completed range.

Proof and data:

- `proofs/MARKER_THREE_FINITE_FULL_MENU_AUDIT.md`;
- `verification/marker_three_full_menu_audit.py`;
- `verification/data/marker_three_full_menu_n12_n45.manifest.json`;
- `verification/data/marker_three_full_menu_n12_n45.csv`.

### N2-FIN-203

The N2-ADD-121 streaming generator certifies the complete marker-three carrier theorem at `n=46` without materializing the complete `27,941,760`-core family.

Exact parameters:

\[
r_{46}=16,
\qquad
M_{46}=235,
\qquad
v_2(46!)=42.
\]

The stream emits `24,567,748` cores through `Y_46`, retains `631` record gaps, and has maximum active frontier `3,373,952`. Six main layers give

\[
E_6+W_{46}
=
24{,}938{,}550{,}582{,}416{,}882{,}103{,}407{,}947{,}983
>
Y_{46}.
\]

Consequently

\[
H_{46!}(\lfloor\sqrt{46!}\rfloor+1)
\le22.
\]

This is a finite exact theorem, not an asymptotic occupancy result. The smallest unaudited parameter is now `n=47`.

Proof and data:

- `proofs/MARKER_THREE_STREAMING_N46_AUDIT.md`;
- `verification/marker_three_streaming_audit.cpp`;
- `verification/test_marker_three_streaming_audit.py`;
- `verification/data/marker_three_streaming_n46.json`.

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
- Files: `handoffs/RESPONSE_TO_NOVA4.md`, `handoffs/MARKER_THREE_REQUEST_TO_NOVA4.md`, and `handoffs/FULL_MENU_FINITE_TO_NOVA4.md`.
- Nova 2 independently completed exact carrier coverage through `n=46` in N2-FIN-202 and N2-FIN-203.

## Open factorial nodes

- N2-OPEN-301: prove or disprove marker-three quotient occupancy through `Y_n` uniformly in `n`.
- N2-OPEN-302: prove connected-core reach uniformly beyond the finite range; exact success is certified for `12<=n<=46`.
- N2-OPEN-303: prove endpoint support near `Y_n` or produce an exact endpoint deficit.
- N2-OPEN-304: control total-sum collisions beyond formal profile capacity.
- N2-OPEN-305: prove the numerical target-dependent tilt, moments, resonance decomposition, and weighted Fourier inequality.
- N2-OPEN-306: audit N2-ADD-120 against the exact Phase 12P hypotheses.
- N2-OPEN-307: extend bounded-memory finite certification from `n=47` or prove a uniform record-gap theorem.

## Promotion rule

No conditional theorem becomes a proved factorial theorem until all structural, additive or analytic, endpoint, distinctness, and finite-exception nodes are proved and independently reconstructed.
