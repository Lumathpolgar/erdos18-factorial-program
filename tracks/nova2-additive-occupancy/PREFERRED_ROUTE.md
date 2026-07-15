# Preferred Additive Route

## Ranking

### Rank 1: Target-dependent exponential tilt with lattice-aware Fourier window control

**Result label: conditional theorem.**

This route moves the mean toward each requested target and asks only for positive mass in a correction window. It directly addresses the fixed-law tail problem. The proof engine is the strict Fourier comparison lemma N2-ADD-110, not a visual or weak Gaussian approximation.

Required supplement: deterministic lower and upper endpoint regimes because tilted variance collapses near support endpoints.

### Rank 2: Deterministic restricted-sumset growth

**Result label: conditional theorem.**

This route would give the cleanest all-target result if a strong labeled covering theorem could be verified. It is ranked second because current additive inverse and growth theorems do not automatically preserve one choice per label, numerical distinctness, interval location, or factorial divisor legality.

### Rank 3: Uniform rainbow convolution

**Result label: heuristic.**

This is a useful benchmark and may work for specially balanced packets. It is ranked below tilting because one fixed mean leaves the endpoint windows in large-deviation tails.

### Rank 4: Fixed-law Fourier or local-limit theorem

**Result label: heuristic as a standalone route.**

Fourier analysis is essential as a proof tool, but a fixed-law local theorem is generally central rather than half-range uniform. It is retained inside Rank 1, not selected as an independent final architecture.

## Selected architecture

For each `n`, Nova 1 supplies:

1. fixed pairwise numerically disjoint main labels
   \[
   A_{1,n},...,A_{k_n,n}\subseteq D(n!);
   \]
2. a numerically disjoint correction palette `C_n`;
3. a correction radius `R_n` and term cost `ell_n`;
4. deterministic endpoint coverage where the tilted variance theorem is not valid.

For each bulk target `x`, choose a target-dependent exponential tilt on the fixed labels so that the mean lies near the midpoint of

\[
I_{n,x}=[x-R_n,x]\cap\mathbb Z.
\]

Nova 3 proves a major-arc and minor-arc estimate strong enough to establish

\[
\int_{-\pi}^{\pi}
|\phi_{n,x}(t)-\psi_{n,x}(t)|
|K_{I_{n,x}}(t)|\,dt
<2\pi Q_{n,x}(I_{n,x}),
\]

where `Q_{n,x}` is a lattice reference law with known positive mass in the target window.

N2-ADD-110 then gives positive main-window mass. Pairwise disjoint supports give deterministic extraction. N2-ADD-112 adds the correction residual and proves the target representation.

## Why this route survives the historical no-go results

- It is not independently decoded across CRT coordinates.
- It does not infer coverage from raw profile count.
- It does not use a magnitude-separated high-prime shell atlas.
- It does not require partial sumsets to cover intervals.
- It is not a one-choice sequential ladder in the Phase 12P sense.
- It tests final occupancy only after all labels are globally convolved.

## Frozen bulk theorem target

Find absolute constants `K,L,c_0,n_0` and sequences `R_n`, `sigma_{n,x}` such that:

- `k_n<=K(log n)^2`;
- every residual in `[0,R_n]` uses at most `L(log n)^2` correction divisors;
- for every bulk target, the tilted variance satisfies `sigma_{n,x}>=c_0` and the weighted Fourier error is strictly below the explicit reference window mass;
- all terms are numerically distinct;
- the deterministic endpoint regimes and bulk regime cover every integer `0<=x<=X_n`.

## Exact blockers

1. No frozen factorial labels yet satisfy the pairwise disjointness, support reach, and endpoint requirements.
2. No uniform tilt and variance theorem is available.
3. No major-arc or minor-arc inequality has been proved for a factorial layer system.
4. The largest admissible correction radius and its exact term cost are unknown.
5. No finite search has tested the candidate inequality against exact target-window minima.

## Next theorem target

Prove the candidate abstract occupancy theorem in `proofs/CANDIDATE_OCCUPANCY_THEOREM.md`, then reduce the remaining factorial work to three frozen handoff contracts: structural packets from Nova 1, analytic Fourier control from Nova 3, and finite falsification from Nova 4.
