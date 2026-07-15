# Nova 2 Status

## Track

Additive Occupancy and Global Sumsets

## Branch

`nova/additive-occupancy`

## Overall state

`REPAIRED_ROUTE_SURVIVES_EXPONENTIAL_PREFIX_GLOBAL_REGION_OPEN`

## Baseline

- Startup branch head: `71370633b1e6726bf6f9e3b334d42cfc34512c06`
- Startup main head: `68ace6c9c3b67636e298a406fee3bfe8e072741d`
- Merge base: `cd5576d4f7934e26e9d4ef3b065c2ad4cee36c67`
- Required mathematical definitions and archive indexes read.
- `docs/HANDOFF_PROTOCOL.md` was absent; `docs/CROSS_TRACK_HANDOFF_PROTOCOL.md` was used.

## Proved results

- N2-ADD-101: profile count larger than interval size does not imply coverage.
- N2-ADD-102: common-gcd lattice obstruction.
- N2-ADD-103: ordinary convolution may certify an illegal repeated divisor.
- N2-ADD-104 and N2-ADD-105: a local or window approximation is insufficient when its error reaches the reference mass.
- N2-ADD-106: endpoint variance collapse for tilted Bernoulli sums.
- N2-ADD-108: deterministic extraction from positive collision-free mass.
- N2-ADD-109: exact union-bound threshold for a sampled catalogue.
- N2-ADD-110: weighted Fourier comparison implies positive window mass.
- N2-ADD-111: explicit discretized-Gaussian window lower bound.
- N2-ADD-112: correction-window bridge.
- N2-ADD-113: positive point mass gives targetwise deterministic extraction.
- N2-ADD-115: a support contained in `g Z` cannot meet all downward windows of radius below `g-1` over a target range containing the first missing residue block.
- N2-ADD-116: exact lattice quotient normalization. Correction range `[0,Lg-1]` is equivalent to quotient downward gaps at most `L-1`.
- N2-ADD-118: the normalized valuation-tagged sumset meets every four-point quotient window through `3*2^{M_n}` under the frozen valuation-budget condition.

## Conditional theorems

### N2-ADD-114

Fixed legal labels, a disjoint correction palette, and a strict weighted Fourier window inequality imply

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)=O((\log n)^2).
\]

The implication is proved. Its factorial structural and analytic hypotheses remain open.

### N2-ADD-117

Retain the normalized valuation-tagged main labels and extend the binary correction palette through `2^{r_n+2}`. If the final normalized rainbow sumset `Q_n` intersects every four-point downward window

\[
[\max(0,m-3),m]
\]

through `floor(X_n/2^{r_n+1})`, then

\[
H_{n!}(X_n+1)
\le
M_n+r_n+3
=O((\log n)^2).
\]

The reduction is proved. N2-ADD-118 now proves its quotient hypothesis uniformly throughout the prefix

\[
0\le m\le3\cdot2^{M_n}.
\]

The remaining all-target region is open.

## Original factorial instantiation decision

Nova 1 handoff `N1-HO-N2-001`, imported from branch `nova/factorial-structure` at exact commit

`b939574eb88a08bb03abda5bbe6ff2ca97444e08`,

is `REJECTED`.

Every main divisor and rainbow sum is divisible by `2^{r_n+1}`, while the original first requested window is `[1,2^{r_n}]`. This is N2-OBS-107.

Proof: `proofs/VALUATION_TAGGED_LATTICE_OBSTRUCTION.md`.

## Minimal repair milestone

Let

\[
g_n=2^{r_n+1}.
\]

- Adding only `2^{r_n}` leaves target `g_n` unreachable.
- Adding through `2^{r_n+1}` leaves target `2g_n` unreachable.
- Adding through `2^{r_n+2}` is the first consecutive-binary extension not killed by the initial support gap.

The first two variants are N2-OBS-108. The third yields the exact four-point quotient target in N2-ADD-117.

Proof: `proofs/LATTICE_QUOTIENT_NORMALIZATION.md`.

## Binary-spine prefix milestone

For every admissible `n>=7`, the valuation budget implies

\[
\left\lfloor\frac{X_n}{g_n}\right\rfloor
\ge3\cdot2^{M_n}.
\]

The quotient layers contain

\[
3,5,7\in B_1(n)
\]

and the binary spine

\[
3\cdot2^{t-1}\in B_t(n)
\qquad(2\le t\le M_n).
\]

Every odd quotient

\[
3\le q\le3\cdot2^{M_n}-3
\]

has a legal rainbow representation. Consequently every four-point quotient window through

\[
3\cdot2^{M_n}
\]

is occupied.

Proof: `proofs/QUOTIENT_BINARY_SPINE_PREFIX.md`.

Verification: `verification/quotient_binary_spine.py`.

## Finite certificate N2-FIN-201

An exact rational-log scan through `n=5000` gives the first valuation-budget-admissible parameter as

\[
n=1892,
\qquad
r_n=31,
\qquad
M_n=911.
\]

The protected quotient prefix ends at `3*2^911`, a 275-digit integer. Therefore the repaired full-family model has no four-point counterexample before that target.

## Nova 4 intake decision

Nova 4 branch `nova/computational-verification` was inspected at commit

`2f2a355f59f230751b8e798e7a5df0769e8bf6d9`.

Outcome: `ACCEPTED_WITH_RESTRICTIONS`.

Accepted:

- exact lattice-first verification infrastructure;
- rational certification of `r_n` and `M_n`;
- independent replay of N2-ADD-115 and N2-OBS-107;
- fail-closed corrupted-certificate tests.

Not yet supplied:

- N2-ADD-116 quotient normalization;
- N2-OBS-108 regressions;
- normalized quotient labels or reachable quotient sumsets;
- a four-point quotient-gap sweep;
- a later counterexample or quotient success certificate.

Response: `handoffs/RESPONSE_TO_NOVA4.md`.

## Nova 3 request

The request `N2-HO-N3-002` freezes the exact quotient numerical-value law, the torus `[-pi,pi]`, and the four-point weighted Fourier inequality. It remains conditional on Nova 1 accepting or superseding the repair.

Request: `handoffs/QUOTIENT_REQUEST_TO_NOVA3.md`.

## Disproved models and retired shortcuts

- Raw profile capacity as a coverage criterion.
- All-support-in-a-proper-lattice architectures without sufficient residue repair.
- Ordinary convolution extraction with overlapping numerical labels.
- Local-limit claims whose error is not smaller than the target atom or window mass.
- A single bulk tilted local theorem extending uniformly to both support endpoints.
- Target-dependent probability spaces treated as one shared random universal object.
- The exact original valuation-tagged layer and correction contract.
- Automatic transfer from logarithmic divisor density to additive numerical occupancy.
- One-power and two-power consecutive-binary repairs.

## Model ranking

1. Normalized valuation-tagged quotient model with the proved binary-spine prefix and target-dependent tilt plus bounded-torus Fourier control in the remaining region.
2. Deterministic restricted-sumset growth for the same quotient labels beyond the proved prefix.
3. Uniform rainbow convolution.
4. Fixed-law Fourier or local-limit route as a standalone architecture.

## Exact open blockers

1. Nova 1 must accept, restrict, supersede, or reject the versioned three-power repair contract.
2. Extend or disprove four-point quotient occupancy in
   \[
   3\cdot2^{M_n}<m\le\left\lfloor X_n/g_n\right\rfloor.
   \]
3. Nova 3 must prove the exact additive numerical-value tilt, variance, resonance, reference-mass, and weighted Fourier package for the normalized labels.
4. Nova 1 must cover every quotient endpoint excluded from the analytic bulk theorem.
5. Nova 4 must upgrade its lattice harness to the current quotient-normalized contract.
6. The source-level Phase 12M through 12P package statements are not stored in the repository.
7. Finite exceptions below the eventual `n_0` remain open.

## Handoffs maintained

- `handoffs/TO_NOVA1.md`
- `handoffs/TO_NOVA3.md`
- `handoffs/TO_NOVA4.md`
- `handoffs/RESPONSE_TO_NOVA1.md`
- `handoffs/RESPONSE_TO_NOVA3.md`
- `handoffs/RESPONSE_TO_NOVA4.md`
- `handoffs/REPAIR_CONTRACT_TO_NOVA1.md`
- `handoffs/QUOTIENT_REQUEST_TO_NOVA3.md`

## Next theorem target

Work only in the unprotected quotient region

\[
3\cdot2^{M_n}<m\le\left\lfloor X_n/g_n\right\rfloor.
\]

The immediate choices are:

1. prove a second deterministic spine or interval-extension theorem;
2. construct an exact full-family counterexample after the proved prefix; or
3. prove the normalized target-dependent Fourier-window theorem.