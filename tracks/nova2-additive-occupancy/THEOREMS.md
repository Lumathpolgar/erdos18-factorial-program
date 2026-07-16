# Nova 2 Theorem Registry

## Proved theorems

| ID | Result label | Statement summary | Location |
|---|---|---|---|
| N2-ADD-101 | proved theorem | Profile count alone does not imply coverage | `models/TOY_COUNTEREXAMPLES.md` |
| N2-ADD-102 | proved theorem | A common gcd confines sums to a proper lattice | `models/TOY_COUNTEREXAMPLES.md` |
| N2-ADD-103 | proved theorem | Ordinary convolution may use an illegal repeated divisor | `models/TOY_COUNTEREXAMPLES.md` |
| N2-ADD-104 | proved theorem | Pointwise approximation error must be below the reference atom | `models/TOY_COUNTEREXAMPLES.md` |
| N2-ADD-105 | proved theorem | Window approximation error must be below reference window mass | `models/TOY_COUNTEREXAMPLES.md` |
| N2-ADD-106 | proved theorem | Tilted Bernoulli variance ceiling | `models/TOY_COUNTEREXAMPLES.md` |
| N2-ADD-108 | proved theorem | Positive collision-free mass gives a legal representation | `models/TOY_SUFFICIENT_CONDITIONS.md` |
| N2-ADD-109 | proved theorem | Sampled-catalogue failure bound | `models/TOY_SUFFICIENT_CONDITIONS.md` |
| N2-ADD-110 | proved theorem | Strict weighted Fourier discrepancy implies occupancy | `models/TOY_SUFFICIENT_CONDITIONS.md` |
| N2-ADD-111 | proved theorem | Discretized-Gaussian window lower bound | `models/TOY_SUFFICIENT_CONDITIONS.md` |
| N2-ADD-112 | proved theorem | Main-window occupancy plus corrections gives exact coverage | `models/TOY_SUFFICIENT_CONDITIONS.md` |
| N2-ADD-113 | proved theorem | Positive point mass gives targetwise extraction | `models/TOY_SUFFICIENT_CONDITIONS.md` |
| N2-ADD-115 | proved theorem | The original valuation-tagged model fails its first window | `proofs/VALUATION_TAGGED_LATTICE_OBSTRUCTION.md` |
| N2-ADD-116 | proved theorem | Quotient normalization converts correction width to downward-gap width | `proofs/LATTICE_QUOTIENT_NORMALIZATION.md` |
| N2-ADD-118 | proved theorem | The three-power fallback covers an exponential binary-spine prefix | `proofs/QUOTIENT_BINARY_SPINE_PREFIX.md` |
| N2-ADD-119 | proved theorem | Translated carrier blocks preserve downward-window density | `proofs/MARKER_THREE_CARRIER_BLOCK_REDUCTION.md` |
| N2-ADD-121 | proved theorem | Unique-parent streaming emits exact odd factorial divisors in order | `proofs/MARKER_THREE_STREAMING_N46_AUDIT.md` |
| N2-ADD-122 | proved theorem | Exact carrier growth factors into prefix cardinality and packing utilization | `proofs/EFFECTIVE_CARRIER_ENTROPY_FACTORIZATION.md` |

## Accepted imported theorems

### N1-OBS-003

Source proof commit: `ac676b0fc9007117da1f1d9eaeec3e3cf65dd1e7`.

For connected-prefix counts `K_t`, sequential success requires

\[
\prod_{t=1}^{L}(1+K_t)\ge\frac{Y_n+1}{W_n+1}.
\]

For `n>=120368`, the required geometric mean is at least `exp(n/(85 log n))`. Outcome: `ACCEPTED_WITH_RESTRICTIONS` as a necessary condition only.

### N1-STR-023 and N1-STR-024

Inspected source: `nova/factorial-structure@a6bdab1b917f3b3688f5a0c86e80c8a026bfbc07`.

- `N1-STR-023`: disjoint-coordinate meet-in-the-middle product streams recover exact divisor order with heap size `O(sqrt(tau(D_n)))`. Outcome: `ACCEPTED`.
- `N1-STR-024`: the normalized count surplus `Gamma_n` exactly tests the necessary count gate. Outcome: `ACCEPTED_WITH_RESTRICTIONS`; by N2-ADD-122 it is not sufficient without packing utilization.

## Conditional theorems

### N2-ADD-114

Fixed legal disjoint labels, correction coverage, and a strict weighted Fourier comparison for every target imply

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)=O((\log n)^2).
\]

Proof: `proofs/CANDIDATE_OCCUPANCY_THEOREM.md`.

### N2-ADD-117

The three-power fallback reduces the theorem to four-point quotient occupancy and conditionally gives

\[
H_{n!}(X_n+1)\le M_n+r_n+3.
\]

Proof: `proofs/LATTICE_QUOTIENT_NORMALIZATION.md`.

### N2-ADD-120

For the marker-three model, connect cores from zero at layer `t` across gaps at most

\[
D_t=\left\lfloor\frac{E_{t-1}+W_n+1}{2^{t-1}}\right\rfloor.
\]

If the resulting carrier reaches `E_L+W_n>=Y_n`, then

\[
H_{n!}(X_n+1)\le L+r_n.
\]

This is a sequential sufficient condition and still requires a Phase 12P audit.

## N2-ADD-122 effective criterion

Put `F_t=E_t+W_n+1`, `s_t=2^{t-1}`, and let `U_t` and `K_t` be the connected maximum and positive prefix count. Define

\[
a_t=\frac{s_tU_t}{F_{t-1}},
\qquad
b_t=\frac{1+a_t}{1+K_t}.
\]

Then exactly

\[
\frac{F_L}{W_n+1}
=
\left(\prod_t(1+K_t)\right)
\left(\prod_tb_t\right).
\]

Thus the sequential route must control both count entropy and utilization. The exact active condition is

\[
\widetilde\Gamma_n\mathcal B_n\ge1.
\]

## Finite certificates

- `N2-FIN-201`: superseded-route rational-log certificate at `n=1892`.
- `N2-FIN-202`: exact complete-menu carrier coverage for `12<=n<=45`.
- `N2-FIN-203`: bounded-memory Nova 2 streaming certificate at `n=46`.
- `N2-FIN-204`: accepted Nova 1 full-core certificate for `47<=n<=50`, with exact `n=46` overlap.
- `N2-FIN-205`: accepted Nova 1 certificates `N1-FIN-006`, `N1-FIN-007`, and `N1-FIN-008` for `n=51,52,53` from inspected commit `a6bdab1b917f3b3688f5a0c86e80c8a026bfbc07`.

Combined exact finite result:

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le22
\qquad(12\le n\le53).
\]

The smallest unaudited finite parameter is `n=54`.

## Finite effective-entropy diagnostics

| `n` | count surplus | utilization root | endpoint surplus |
|---:|---:|---:|---:|
| 51 | 120.322026488584 | 0.008311064676932 | 1.000004144206103 |
| 52 | 97.645052132052 | 0.010241184816549 | 1.000001025305911 |
| 53 | 124.609364763243 | 0.008025094814707 | 1.000001967025492 |

These are finite diagnostics, not an asymptotic trend.

## Disproved models

`N2-OBS-101` through `N2-OBS-108` remain recorded in the cited model and proof files. They include raw-capacity, proper-lattice, repeated-divisor, weak-approximation, endpoint-uniformity, target-space, original-lattice, and one-or-two-power repair failures.

## Cross-track decisions

### Nova 1

- `N1-HO-N2-001`: `REJECTED`.
- `N1-HO-N2-002`: `ACCEPTED_WITH_RESTRICTIONS`.
- `N1-HO-N2-004`: `ACCEPTED_WITH_RESTRICTIONS`.
- `N1-HO-N2-007`: `ACCEPTED_WITH_RESTRICTIONS`.
- Latest response: `handoffs/RESPONSE_TO_NOVA1_N53_EFFECTIVE_ENTROPY.md`.

### Nova 3

The active request remains the exact numerical marker-three law, aggregate phase dispersion, collision-aware reference mass, and strict weighted Fourier inequality.

### Nova 4

Independent reconstruction is required for the carrier algorithms, finite certificates through `n=53`, effective-entropy identities, and extension from `n=54`.

## Open factorial nodes

1. Prove or disprove marker-three quotient occupancy uniformly through `Y_n`.
2. Prove a utilization lower bound strong enough that `widetilde Gamma_n B_n>=1`, or prove an upper bound retiring the sequential engine.
3. Extend exact finite certification from `n=54`.
4. Prove asymptotic endpoint-window coverage.
5. Upper-bound target-local collision multiplicity or additive energy.
6. Prove aggregate numerical phase dispersion and the strict weighted Fourier inequality.
7. Audit N2-ADD-120 against exact Phase 12P hypotheses.
8. Handle finite exceptions after an effective threshold exists.

## Promotion rule

No conditional result becomes an asymptotic factorial theorem until every structural, additive or analytic, endpoint, distinctness, and finite-exception node is proved and independently reconstructed.
