# Nova 1 Baseline Audit

## Audit identity

- Track: Nova 1, Factorial Structure and Reduction
- Working branch: `nova/factorial-structure`
- Remote repository: `Lumathpolgar/erdos18-factorial-program`
- Exact branch baseline commit: `3f854b637198fce9ae6503a64622373c9f774ea3`
- Baseline commit message: `Initialize Nova 1 open requirements`
- Main branch head observed during audit: `68ace6c9c3b67636e298a406fee3bfe8e072741d`
- Branch relation observed during audit: the working branch was four commits ahead of, and twelve commits behind, `main`, with merge base `cd5576d4f7934e26e9d4ef3b065c2ad4cee36c67`.
- History policy: no force update, no modification of `main`, and no import from another Nova branch.

## Repository-path discrepancy

The startup prompt requires `docs/HANDOFF_PROTOCOL.md`, but that path does not exist at the audited baseline. The repository README instead names `docs/CROSS_TRACK_HANDOFF_PROTOCOL.md`, which was read and is used for handoff formatting. This discrepancy is recorded rather than silently repaired.

## Frozen definitions

Let

\[
\mathcal D(N)=\{d\in\mathbb Z_{>0}:d\mid N\}.
\]

For every integer `x >= 0`,

\[
\lambda_N(x)=\min\left\{|S|:S\subseteq\mathcal D(N),\ \sum_{d\in S}d=x\right\},
\]

with `lambda_N(x)=infinity` if no such set exists. The empty set represents `0`, so `lambda_N(0)=0`.

For every real `X >= 1`,

\[
H_N(X)=\max_{0\le x<X,\ x\in\mathbb Z}\lambda_N(x).
\]

When `N` is practical,

\[
h(N)=H_N(N).
\]

All representations use numerically distinct positive divisors. Labeled copies of the same integer are not legal distinct terms.

For the factorial program,

\[
N_n=n!,\qquad X_n=\lfloor\sqrt{n!}\rfloor,
\]

and

\[
v_p(n!)=\sum_{j\ge1}\left\lfloor\frac{n}{p^j}\right\rfloor.
\]

## Frozen target and current sufficient theorem

The main objective is to prove that absolute constants `C`, `K`, and `n_0` exist such that

\[
h(n!)\le K(\log n)^C
\]

for every integer `n >= n_0`.

The current sufficient local theorem is

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)=O((\log n)^2),
\]

meaning that absolute constants `K_0` and `n_0` exist such that every integer

\[
0\le x\le\lfloor\sqrt{n!}\rfloor
\]

is a sum of at most `K_0(log n)^2` numerically distinct positive divisors of `n!` for all `n >= n_0`.

## Current dependency chain

1. **Local half-range node, open:** prove
   \[
   H_{n!}(\lfloor\sqrt{n!}\rfloor+1)=O((\log n)^2).
   \]
2. **Factorial local-to-global node, conditional theorem:** reconstruct the archived Track B implication under the frozen `H_N` endpoint convention.
3. **Global node, conditional theorem:** the audited intended conclusion is
   \[
   h(n!)=O((\log n)^3).
   \]
4. **Final acceptance node:** all integration gates, finite exceptions, imported-result audits, and two independent end-to-end reconstructions must pass.

No step in this chain is permission to state that Erdős Problem 18 is solved.

## Track B status

Result label: **conditional theorem**.

Track B contains a completed conditional reduction architecture with factorial reduction, packet, scaled-core, descent, boundary, dense-quotient, and clean-room audit components. Its merge gate is intentionally closed because its local input theorem has not been proved. The direct factorial program may use only a newly frozen and reconstructed implication that matches the current definition of `H_N`; it may not silently substitute the historical `L_m` cube-root theorem.

## Phase 12K through 12P obstruction ledger

### Phase 12K

Result label: **disproved route**.

A uniform multiplicative entry mesh at scale `exp(-c m/log m)` cannot start near the certified Sylvester-prefix endpoint because the required windows become shorter than integer granularity.

Transfer to `n!`: the integer-granularity objection transfers to any argument demanding nonempty integer windows of length below one. The specific Sylvester-prefix location and lcm complementary-scale parameters do not transfer automatically.

### Phase 12L

Result label: **disproved route**.

The maximum-gap greedy orbit obeys an orbit-step ceiling and requires superlogarithmically many steps. Fixed-power greedy growth therefore cannot prove the historical `O(log m)` local theorem.

Transfer to `n!`: the warning transfers to any factorial route whose proof is the same maximum-gap greedy recurrence after parameter renaming. It does not rule out globally optimized, non-greedy, or factorial-multiplicity constructions.

### Phase 12M

Result label: **disproved route** for the separable and independently decoded architectures; raw profile capacity alone remains only a heuristic resource.

A marked-layer atlas can have many formal profiles, but independently decoded CRT atlases and separable recursive constructions do not have sufficient effective capacity.

Transfer to `n!`: the logical obstruction transfers. Raw divisor or profile count cannot be treated as uniform additive coverage, and independent coordinate counts cannot be multiplied without proving that the sum map preserves useful occupancy. Factorial valuations may create new coupled architectures not present for `L_m`.

### Phase 12N

Result label: **disproved route**.

The magnitude-separated high-prime atlas fails at its first post-correction target on an infinite family. A disjoint correction palette repairs that first local defect, but an additive shell gap remains.

Transfer to `n!`: the shell-gap test transfers to any magnitude-separated packet architecture with the same lower-shell/upper-shell geometry. The exact high-prime family does not automatically transfer because `n!` has larger prime-power multiplicities.

### Phase 12O

Result label: **finite certificate**.

A mixed-scale shared-core construction repairs the earlier shell gap and passes exact interval-extension tests on the tested finite range.

Transfer to `n!`: the design principle and verifier ideas may transfer after legality and valuation audits. The finite success does not imply an asymptotic factorial theorem.

### Phase 12P

Result label: **disproved route**.

A one-choice sequential shared-core ladder requires at least `Omega(log m log log m)` layers in the historical setting because each layer has a smooth-number information ceiling.

Transfer to `n!`: the conclusion transfers only to factorial constructions satisfying the same sequential one-choice and effective-choice hypotheses. A factorial route must either violate those hypotheses through genuine global coupling or accept and account for the larger layer cost. Merely renaming layers as packets does not avoid the obstruction.

## Assumptions forbidden in this track

Nova 1 may not assume any of the following without a separate proof:

1. the historical theorem
   \[
   H_{L_m}(\lfloor L_m^{1/3}\rfloor+1)=O(\log m);
   \]
2. that many divisors imply interval coverage;
3. that many valuation profiles imply many distinct sums;
4. that average spacing controls the maximum additive gap;
5. that pairwise disjoint labels imply numerically distinct divisors;
6. that prime powers of the same prime are independent coordinates;
7. that a finite successful pattern persists asymptotically;
8. that an almost-all-target theorem covers every target;
9. that probabilistic existence gives a deterministic representation for every target;
10. that an `L_m` construction transfers unchanged to `n!`, or conversely;
11. that a correction palette is free in term count or automatically disjoint from main terms;
12. that recursive subproblems have polylogarithmic total cost merely because each recursion level does;
13. that complement pairing preserves legality, range, or distinctness without checking every valuation and numerical collision;
14. that a sequential construction escapes Phase 12P because it uses factorial divisors;
15. that the archived Track B implication matches the current endpoint convention without reconstruction.

## Baseline conclusion

Result label: **proved theorem** as an audit statement about the repository baseline.

The open mathematical node remains the direct factorial half-range theorem. Nova 1's valid contribution must therefore be one of the following: a proved structural theorem, a conditional reduction with exact frozen inputs, a finite certificate with no asymptotic promotion, or a disproved route that permanently removes a false architecture.