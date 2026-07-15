# Preferred Additive Route

## Ranking

### Rank 1: Target-dependent exponential tilt with lattice-aware Fourier window control

**Result label: conditional theorem.**

This route moves the mean toward each requested target and asks only for positive mass in a correction window. It directly addresses the fixed-law tail problem. The proof engine is the strict Fourier comparison lemma N2-ADD-110, not a visual or weak Gaussian approximation.

Required supplement: deterministic lower and upper endpoint regimes because tilted variance collapses near support endpoints.

Required precondition: the fixed structural labels must pass N2-ADD-115. No analytic model is opened until the support lattice, attained residues, and correction radius are compatible.

### Rank 2: Deterministic restricted-sumset growth

**Result label: conditional theorem.**

This route would give the cleanest all-target result if a strong labeled covering theorem could be verified. It is ranked second because current additive inverse and growth theorems do not automatically preserve one choice per label, numerical distinctness, interval location, or factorial divisor legality.

### Rank 3: Uniform rainbow convolution

**Result label: heuristic.**

This is a useful benchmark and may work for specially balanced packets. It is ranked below tilting because one fixed mean leaves the endpoint windows in large-deviation tails.

### Rank 4: Fixed-law Fourier or local-limit theorem

**Result label: heuristic as a standalone route.**

Fourier analysis is essential as a proof tool, but a fixed-law local theorem is generally central rather than half-range uniform. It is retained inside Rank 1, not selected as an independent final architecture.

## Structural compatibility gate

Before tilting, moment computation, or Fourier inversion, every fixed label family must pass all of the following.

1. Compute the common support lattice `g_n Z` of the final main sumset.
2. Determine the exact attained residues if the support is not a single lattice coset.
3. Compare the correction radius `R_n` with every unresolved downward residue gap.
4. Test the first requested target directly.
5. Test the minimum nonzero main sum and the top endpoint.
6. Verify that the correction palette is numerically disjoint from every main label.
7. Verify that the full construction remains final-only and does not impose sequential interval growth.

N2-ADD-115 proves that if the main support is contained in `g_n Z` and the target range contains `R_n+1` with `R_n<g_n-1`, then all-target downward-window occupancy is impossible.

## First frozen instantiation outcome

Nova 1 handoff `N1-HO-N2-001`, imported from branch `nova/factorial-structure` at commit

`b939574eb88a08bb03abda5bbe6ff2ca97444e08`,

failed the structural gate.

Its addresses satisfy

\[
e_t=r_n+t\ge r_n+1,
\]

so its entire main sumset lies in

\[
2^{r_n+1}\mathbb Z.
\]

Its correction radius is only

\[
2^{r_n}-1.
\]

The first requested target `x=2^{r_n}` has window `[1,2^{r_n}]`, which is disjoint from the main support. The exact model is therefore `REJECTED` before analytic evaluation.

Proof: `proofs/VALUATION_TAGGED_LATTICE_OBSTRUCTION.md`.

Response: `handoffs/RESPONSE_TO_NOVA1.md`.

## Selected architecture after structural acceptance

For each `n`, Nova 1 supplies:

1. fixed pairwise numerically disjoint main labels
   \[
   A_{1,n},...,A_{k_n,n}\subseteq D(n!);
   \]
2. a numerically disjoint correction palette `C_n`;
3. a correction radius `R_n` and term cost `ell_n`;
4. exact common span and residue data;
5. deterministic endpoint coverage where the tilted variance theorem is not valid.

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

The characteristic function is the additive numerical-value characteristic function

\[
\phi_{n,x}(t)=\mathbb E e^{itS_{n,x}},
\]

not a characteristic function of `log d`. Integer-valued inversion takes place on the bounded torus `[-pi,pi]`. Every resonance inside that torus must be included in the major arcs or controlled explicitly.

N2-ADD-110 then gives positive main-window mass. Pairwise disjoint supports give deterministic extraction. N2-ADD-112 adds the correction residual and proves the target representation.

## Nova 3 compatibility ruling

Nova 3 handoff `N3-HO-N2-001` was inspected at exact commit

`0ce88b28dc2e6641093526f5777bb31f658e3515`.

The following restrictions are accepted:

- a full uniform-divisor Gaussian model for `log d` is unavailable;
- unbounded-frequency pointwise decay is not a valid Fourier contract;
- logarithmic divisor estimates do not transfer automatically to additive numerical sums;
- the exact fixed layer law must be frozen before moments and resonances can be audited.

These restrictions are compatible with the selected route because its inversion domain is bounded and periodic. The high-prime logarithmic CLT is not imported as an additive occupancy theorem.

## Why this route survives the historical no-go results

- It is not independently decoded across CRT coordinates.
- It does not infer coverage from raw profile count.
- It does not use a magnitude-separated high-prime shell atlas without a residue audit.
- It does not require partial sumsets to cover intervals.
- It is not a one-choice sequential ladder in the Phase 12P sense.
- It tests final occupancy only after all labels are globally convolved.
- It rejects structurally impossible supports before probabilistic modeling.

## Frozen bulk theorem target

Find absolute constants `K,L,c_0,n_0` and sequences `R_n`, `sigma_{n,x}` such that:

- `k_n<=K(log n)^2`;
- every residual in `[0,R_n]` uses at most `L(log n)^2` correction divisors;
- the fixed main support and correction palette pass the structural compatibility gate;
- for every bulk target, the tilted variance satisfies `sigma_{n,x}>=c_0` and the weighted Fourier error is strictly below the explicit reference window mass;
- all terms are numerically distinct;
- the deterministic endpoint regimes and bulk regime cover every integer `0<=x<=X_n`.

## Exact blockers

1. The first frozen factorial label system was rejected by an exact lattice obstruction.
2. No revised Nova 1 label family yet passes the structural compatibility gate.
3. No uniform additive-value tilt and variance theorem is available.
4. No major-arc or minor-arc inequality has been proved for an accepted factorial layer system.
5. No finite search has tested a repaired candidate against exact target-window minima.

## Next theorem target

Receive or construct a versioned repair of the Nova 1 labels with an exact span and residue theorem. Only then freeze the additive numerical-value law and request the bounded-torus Fourier estimate from Nova 3.