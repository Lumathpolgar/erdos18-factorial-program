# Nova 2 Status

## Track

Additive Occupancy and Global Sumsets

## Branch

`nova/additive-occupancy`

## Overall state

`VALUATION_TAGGED_ROUTE_NORMALIZED_AND_REPAIRED_CONDITIONALLY`

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

## Conditional theorems

### N2-ADD-114

Fixed legal labels, a disjoint correction palette, and a strict weighted Fourier window inequality imply

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)=O((\log n)^2).
\]

The implication is proved. Its factorial structural and analytic hypotheses remain open.

### N2-ADD-117

For the normalized valuation-tagged quotient model, retain the original main labels and extend the binary correction palette through `2^{r_n+2}`. If the normalized final rainbow sumset `Q_n` intersects every four-point downward window

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

The reduction is proved. The four-point quotient occupancy hypothesis is open.

## First factorial instantiation decision

Nova 1 handoff `N1-HO-N2-001`, imported from branch `nova/factorial-structure` at exact commit

`b939574eb88a08bb03abda5bbe6ff2ca97444e08`,

is `REJECTED`.

For its frozen addresses `e_t=r_n+t`, every main divisor and every rainbow sum is divisible by `2^{r_n+1}`. The requested first target is `x=2^{r_n}`, with downward window `[1,2^{r_n}]`. That window contains no possible main sum. This is N2-OBS-107.

Proof: `proofs/VALUATION_TAGGED_LATTICE_OBSTRUCTION.md`.

Response: `handoffs/RESPONSE_TO_NOVA1.md`.

## Minimal repair milestone

The current Nova 1 head inspected is

`fa11f4b2cb86a2dd791df189ada12757be791804`.

No versioned repair had yet been issued, so Nova 2 derived the exact repair contract independently.

Let

\[
g_n=2^{r_n+1}
\]

and divide every main layer by `g_n`. The normalized final sumset is `Q_n`.

- Adding only the correction power `2^{r_n}` leaves target `g_n` unreachable.
- Adding `2^{r_n}` and `2^{r_n+1}` leaves target `2g_n` unreachable.
- Adding all three powers `2^{r_n}`, `2^{r_n+1}`, and `2^{r_n+2}` is the first consecutive-binary extension not killed by the initial support gap.

The first two repair variants are N2-OBS-108, a disproved model. The third yields the exact four-point quotient target in N2-ADD-117.

Proof: `proofs/LATTICE_QUOTIENT_NORMALIZATION.md`.

Model: `models/VALUATION_TAGGED_QUOTIENT_MODEL.md`.

Repair handoff: `handoffs/REPAIR_CONTRACT_TO_NOVA1.md`.

## Nova 3 handoff decision and new request

Nova 3 handoff `N3-HO-N2-001`, imported from branch `nova/analytic-density` at exact commit

`0ce88b28dc2e6641093526f5777bb31f658e3515`,

is `ACCEPTED_WITH_RESTRICTIONS`.

Accepted restrictions:

- the full uniform-divisor law for `log d` is not Gaussian;
- unbounded-frequency pointwise decay is not a valid contract;
- low-prime coordinates may retain macroscopic variance;
- logarithmic divisor theorems do not transfer automatically to additive numerical sums.

The new request `N2-HO-N3-002` freezes the exact quotient numerical-value law, the torus `[-pi,pi]`, and the four-point weighted Fourier inequality. It remains conditional on Nova 1 accepting or superseding the repair.

Request: `handoffs/QUOTIENT_REQUEST_TO_NOVA3.md`.

## Disproved models and retired shortcuts

- Raw profile capacity as a coverage criterion.
- All-support-in-a-proper-lattice architectures without sufficient residue repair.
- Ordinary convolution extraction with overlapping numerical labels.
- Local-limit claims whose error is not smaller than the target atom or window mass.
- A single bulk tilted local theorem extending uniformly to both support endpoints.
- Target-dependent probability spaces treated as one shared random universal object.
- The exact valuation-tagged layer and correction contract `N1-HO-N2-001`.
- Automatic transfer from logarithmic divisor density to additive numerical occupancy.
- One-power and two-power consecutive-binary repairs of the rejected valuation-tagged route.

## Model ranking

1. Normalized valuation-tagged quotient model, using target-dependent tilt plus bounded-torus Fourier control, conditional on Nova 1 accepting the three-power repair.
2. Deterministic restricted-sumset growth for the same quotient labels.
3. Uniform rainbow convolution.
4. Fixed-law Fourier or local-limit route as a standalone architecture.

## Exact open blockers

1. Nova 1 must accept, restrict, supersede, or reject the versioned three-power repair contract.
2. The normalized final rainbow sumset must be proved to have maximum downward gap at most `3` throughout the required quotient range.
3. Nova 3 must prove the exact additive numerical-value tilt, variance, resonance, reference-mass, and weighted Fourier package for the normalized labels.
4. Nova 1 must cover every quotient endpoint excluded from the analytic bulk theorem.
5. No certified finite quotient falsification harness from Nova 4 is available.
6. The source-level Phase 12M through 12P package statements are not stored in the repository.
7. Finite exceptions below the eventual `n_0` remain open.

## Handoffs maintained

- `handoffs/TO_NOVA1.md`
- `handoffs/TO_NOVA3.md`
- `handoffs/TO_NOVA4.md`
- `handoffs/RESPONSE_TO_NOVA1.md`
- `handoffs/RESPONSE_TO_NOVA3.md`
- `handoffs/REPAIR_CONTRACT_TO_NOVA1.md`
- `handoffs/QUOTIENT_REQUEST_TO_NOVA3.md`

## Next theorem target

Prove or disprove the all-target normalized theorem

\[
Q_n\cap[\max(0,m-3),m]\ne\varnothing
\]

for every `0<=m<=floor(X_n/g_n)`. The immediate subtargets are an exact quotient resonance audit, a finite maximum-gap falsification study, and deterministic coverage of every endpoint excluded from target-dependent tilting.
