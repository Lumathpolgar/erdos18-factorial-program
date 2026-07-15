# Nova 2 Status

## Track

Additive Occupancy and Global Sumsets

## Branch

`nova/additive-occupancy`

## Overall state

`FIRST_FACTORIAL_INSTANTIATION_DISPROVED`

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

## Conditional theorem

- N2-ADD-114: fixed legal labels, a disjoint correction palette, and a strict weighted Fourier window inequality imply
  \[
  H_{n!}(\lfloor\sqrt{n!}\rfloor+1)=O((\log n)^2).
  \]

The implication is proved. Its factorial structural and analytic hypotheses remain open.

## First factorial instantiation decision

Nova 1 handoff `N1-HO-N2-001`, imported from branch `nova/factorial-structure` at exact commit

`b939574eb88a08bb03abda5bbe6ff2ca97444e08`,

is `REJECTED`.

For its frozen addresses `e_t=r_n+t`, every main divisor and every rainbow sum is divisible by `2^{r_n+1}`. The requested first target is `x=2^{r_n}`, with downward window `[1,2^{r_n}]`. That window contains no possible main sum. This is N2-OBS-107.

Proof: `proofs/VALUATION_TAGGED_LATTICE_OBSTRUCTION.md`.

Response: `handoffs/RESPONSE_TO_NOVA1.md`.

## Disproved models and retired shortcuts

- Raw profile capacity as a coverage criterion.
- All-support-in-a-proper-lattice architectures without sufficient residue repair.
- Ordinary convolution extraction with overlapping numerical labels.
- Local-limit claims whose error is not smaller than the target atom or window mass.
- A single bulk tilted local theorem extending uniformly to both support endpoints.
- Target-dependent probability spaces treated as one shared random universal object.
- The exact valuation-tagged layer and correction contract `N1-HO-N2-001`.

## Model ranking

1. Target-dependent exponential tilt with lattice-aware Fourier window control, after a structurally compatible label family is frozen.
2. Deterministic restricted-sumset growth.
3. Uniform rainbow convolution.
4. Fixed-law Fourier or local-limit route as a standalone architecture.

## Nova 3 inspection

Nova 3 branch `nova/analytic-density` was inspected at exact commit

`0ce88b28dc2e6641093526f5777bb31f658e3515`.

Its handoff correctly warns that results for `log d` do not automatically transfer to additive numerical divisor sums and that unbounded-frequency pointwise decay is the wrong contract. Nova 2's additive Fourier variable is on the integer torus `[-pi,pi]`. A formal restricted response is being maintained separately.

## Exact open blockers

1. Nova 1 must replace the rejected layer system with labels whose support lattice and correction radius are compatible.
2. Nova 3 must analyze the exact additive numerical-value layer law, not the logarithmic divisor model, once revised labels are frozen.
3. No certified finite falsification harness from Nova 4 is available.
4. The source-level Phase 12M through 12P package statements are not stored in the repository.
5. Finite exceptions below the eventual `n_0` remain open.

## Handoffs maintained

- `handoffs/TO_NOVA1.md`
- `handoffs/TO_NOVA3.md`
- `handoffs/TO_NOVA4.md`
- `handoffs/RESPONSE_TO_NOVA1.md`

## Next theorem target

Freeze a repaired structural compatibility contract before any new local-limit work. The revised contract must state the exact common lattice span, attained residues, correction radius, first-target coverage, and endpoint coverage. Then instantiate N2-ADD-114 on the integer additive-value characteristic function over `[-pi,pi]`.