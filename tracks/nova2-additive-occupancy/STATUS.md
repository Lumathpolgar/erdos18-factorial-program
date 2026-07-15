# Nova 2 Status

## Track

Additive Occupancy and Global Sumsets

## Branch

`nova/additive-occupancy`

## Overall state

`FIRST_SUBSTANTIVE_CHECKPOINT_PUSHED`

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

## Conditional theorem

- N2-ADD-114: fixed legal labels, a disjoint correction palette, and a strict weighted Fourier window inequality imply
  \[
  H_{n!}(\lfloor\sqrt{n!}\rfloor+1)=O((\log n)^2).
  \]

The implication is proved. Its factorial structural and analytic hypotheses remain open.

## Disproved models and retired shortcuts

- Raw profile capacity as a coverage criterion.
- All-support-in-a-proper-lattice architectures without residue repair.
- Ordinary convolution extraction with overlapping numerical labels.
- Local-limit claims whose error is not smaller than the target atom or window mass.
- A single bulk tilted local theorem extending uniformly to both support endpoints.
- Target-dependent probability spaces treated as one shared random universal object.

## Model ranking

1. Target-dependent exponential tilt with lattice-aware Fourier window control.
2. Deterministic restricted-sumset growth.
3. Uniform rainbow convolution.
4. Fixed-law Fourier or local-limit route as a standalone architecture.

## Exact open blockers

1. No frozen factorial labels from Nova 1 satisfy the full structural contract.
2. No uniform tilt, variance, major-arc, or minor-arc theorem from Nova 3 is available.
3. No certified finite falsification harness from Nova 4 is available.
4. The source-level Phase 12M through 12P package statements are not stored in the repository.
5. Finite exceptions below the eventual `n_0` remain open.

## Handoffs issued

- `handoffs/TO_NOVA1.md`
- `handoffs/TO_NOVA3.md`
- `handoffs/TO_NOVA4.md`

## Next theorem target

Instantiate N2-ADD-114 for the first fixed factorial label family by proving a target-uniform bulk tilt and the strict major-minor arc inequality, while Nova 1 supplies deterministic endpoint coverage.
