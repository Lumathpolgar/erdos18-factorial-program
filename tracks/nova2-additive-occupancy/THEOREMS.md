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

## Accepted imported theorem

### N1-OBS-003: connected-prefix entropy requirement

Source:

- branch: `nova/factorial-structure`;
- proof commit: `ac676b0fc9007117da1f1d9eaeec3e3cf65dd1e7`;
- Nova 2 outcome: `ACCEPTED_WITH_RESTRICTIONS`.

For the complete N2-ADD-120 connected prefix, let `K_t` be its number of positive cores and put `F_t=E_t+W_n+1`. Then

\[
F_t\le F_{t-1}(1+K_t),
\]

so carrier success requires

\[
\prod_{t=1}^{L}(1+K_t)
\ge
\frac{Y_n+1}{W_n+1}.
\]

For `n>=120368`, success within the frozen layer budget requires geometric-mean connected-prefix size at least

\[
\exp\left(\frac{n}{85\log n}\right).
\]

This is necessary only for the sequential carrier engine. It does not prove failure and does not constrain final-only proof engines.

Intake: `proofs/CONNECTED_PREFIX_ENTROPY_AND_N50_INTAKE.md`.

## Conditional theorems

### N2-ADD-114

Fixed legal pairwise-disjoint factorial labels, a disjoint correction palette, and a strict weighted Fourier comparison for every target window imply

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)=O((\log n)^2).
\]

Dependencies: N2-ADD-108, N2-ADD-110, N2-ADD-112.

Proof: `proofs/CANDIDATE_OCCUPANCY_THEOREM.md`.

### N2-ADD-117

For the normalized first valuation-tagged model, extending the correction palette through `2^{r_n+2}` reduces the factorial theorem to four-point quotient occupancy and conditionally gives

\[
H_{n!}(X_n+1)\le M_n+r_n+3.
\]

This is a preserved fallback, not the preferred construction.

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

If `u_t^*` lies in that connected component and

\[
E_t=E_{t-1}+2^{t-1}u_t^*,
\]

then the quotient sumset is downward `W_n`-dense through `E_{M_n}`. If `E_{M_n}+W_n>=Y_n`, then

\[
H_{n!}(X_n+1)\le M_n+r_n.
\]

This is a sequential sufficient condition and requires a Phase 12P compatibility audit before asymptotic promotion.

Proof: `proofs/MARKER_THREE_CARRIER_BLOCK_REDUCTION.md`.

## Finite certificates

### N2-FIN-201

A rational-log scan found the first parameter satisfying the superseded valuation budget at `n=1892`, with `r_n=31` and `M_n=911`.

Verification: `verification/quotient_binary_spine.py`.

### N2-FIN-202

Nova 2 generated and audited the exact full odd-core menus for every

\[
12\le n\le45.
\]

Every case reaches `Y_n` using two through six main layers and satisfies

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le22.
\]

Proof and data:

- `proofs/MARKER_THREE_FINITE_FULL_MENU_AUDIT.md`;
- `verification/marker_three_full_menu_audit.py`;
- `verification/data/marker_three_full_menu_n12_n45.manifest.json`;
- `verification/data/marker_three_full_menu_n12_n45.csv`.

### N2-FIN-203

Nova 2's N2-ADD-121 stream certifies complete marker-three carrier coverage at `n=46` without materializing the complete `27,941,760`-core family. It emits `24,567,748` cores through `Y_46`, retains `631` record gaps, and uses a maximum active frontier of `3,373,952`.

Six main layers give

\[
H_{46!}(\lfloor\sqrt{46!}\rfloor+1)\le22.
\]

Proof and data:

- `proofs/MARKER_THREE_STREAMING_N46_AUDIT.md`;
- `verification/marker_three_streaming_audit.cpp`;
- `verification/test_marker_three_streaming_audit.py`;
- `verification/data/marker_three_streaming_n46.json`.

### N2-FIN-204

Nova 2 accepted Nova 1 finite certificate `N1-FIN-005` from verifier commit `fd2819255ac17dbba6cc70ed8a78ded387e7cac0` and report commit `42e2ac49001215602be7a0808f38648a4557b771`.

The independently generated `n=46` layer record matches N2-FIN-203 in every threshold, blocking gap, connected maximum, endpoint, and margin. The same verifier certifies `n=47,48,49,50`.

Combining N2-FIN-202 and N1-FIN-005 gives

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
\le22
\qquad(12\le n\le50).
\]

This is a finite exact result assembled from audited certificates. The smallest unaudited parameter is `n=51`.

Intake: `proofs/CONNECTED_PREFIX_ENTROPY_AND_N50_INTAKE.md`.

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

### Nova 1

- `N1-HO-N2-001`: `REJECTED`.
- `N1-HO-N2-002`: `ACCEPTED_WITH_RESTRICTIONS`; marker-three promoted to primary model.
- `N1-HO-N2-004`: `ACCEPTED_WITH_RESTRICTIONS`; N1-OBS-003 accepted as a necessary sequential condition and N1-FIN-005 accepted as a finite certificate.
- Responses: `handoffs/RESPONSE_TO_NOVA1.md`, `handoffs/RESPONSE_TO_NOVA1_MARKER_THREE.md`, `handoffs/RESPONSE_TO_NOVA1_CONNECTED_PREFIX.md`.

### Nova 3

- Active exact request: `N2-HO-N3-003`.
- Frozen law: numerical marker-three quotient sums on `[-pi,pi]`.
- File: `handoffs/MARKER_THREE_REQUEST_TO_NOVA3.md`.

### Nova 4

- Active reconstruction requests: `N2-HO-N4-002` and `N2-HO-N4-004`.
- Files: `handoffs/MARKER_THREE_REQUEST_TO_NOVA4.md`, `handoffs/FULL_MENU_FINITE_TO_NOVA4.md`, `handoffs/STREAMING_N46_TO_NOVA4.md`.

## Open factorial nodes

- N2-OPEN-301: prove or disprove marker-three quotient occupancy uniformly through `Y_n`.
- N2-OPEN-302: prove the connected-prefix product requirement is attainable, or prove a uniform upper bound retiring the sequential engine.
- N2-OPEN-303: prove endpoint support near `Y_n` or produce an endpoint deficit.
- N2-OPEN-304: upper-bound target-local collision multiplicity or additive energy.
- N2-OPEN-305: prove aggregate phase dispersion and the strict numerical weighted Fourier inequality.
- N2-OPEN-306: audit N2-ADD-120 against the exact Phase 12P hypotheses.
- N2-OPEN-307: extend exact finite certification from `n=51`.

## Promotion rule

No conditional theorem becomes an asymptotic factorial theorem until every structural, additive or analytic, endpoint, distinctness, and finite-exception node is proved and independently reconstructed.
