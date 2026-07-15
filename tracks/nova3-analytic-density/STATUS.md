# Nova 3 Status

## Track and branch

- Track: Analytic Divisor Density
- Branch: `nova/analytic-density`
- Main head inspected at startup: `68ace6c9c3b67636e298a406fee3bfe8e072741d`
- Merge base: `cd5576d4f7934e26e9d4ef3b065c2ad4cee36c67`
- No merge to `main`, force push, rebase, or edit to another Nova branch

## Overall state

`FIFTH_SUBSTANTIVE_CHECKPOINT_COMPLETE`

The factorial half-range theorem and Erdős Problem 18 remain open.

## Repaired marker-three capacity checkpoint

Nova 1 request:

- branch: `nova/factorial-structure`
- commit: `9febe46f2298d2726eeffa139676136963790019`
- handoff: `N1-HO-N3-002`

Outcome:

`ACCEPTED_WITH_PROOF_REPAIR`.

Closed:

- N3-ANA-014, repaired menu lower bound and address legality;
- N3-ANA-015, repaired formal profile capacity;
- N3-ANA-016, central-binomial shortcut obstruction.

Response:

`handoffs/RESPONSE_TO_NOVA1_MARKER_THREE.md`.

## Marker-three numerical-law checkpoint

Nova 2 request:

- branch: `nova/additive-occupancy`
- commit: `fb73e6906105c983bacbd46a96ef8d5d87567fae`
- handoff: `N2-HO-N3-003`

Outcome:

`ACCEPTED_WITH_RESTRICTIONS`.

### N3-ANA-017, contract compatibility

Nova 2 pins Nova 1 commit `ebb47ba436af554366d0f285119a769f31f9e561`. The latest inspected Nova 1 head is `9febe46f2298d2726eeffa139676136963790019`.

The three later commits add endpoint-support artifacts only. They do not alter the marker-three numerical labels. The active model is therefore compatible after upgrading its endpoint dependency.

The older Nova 2 handoff `N2-HO-N3-002` concerns a different three-power repair and is not the active law for Nova 1 `N1-CON-003`.

### N3-ANA-018, exact tilt and resonance foundations

For the numerical exponential family

\[
P_\lambda(Z_t=b)
=
\frac{e^{\lambda b}}
{1+\sum_{a\in B_t(n)}e^{\lambda a}},
\]

the mean is continuous and strictly increasing from zero to the sum of layer maxima.

For every

\[
W_n<q\le Y_n,
\]

there is a unique finite tilt with mean

\[
q-W_n/2\in[q-W_n,q].
\]

The exact additive span is one, and the only exact torus resonance in `[-pi,pi]` is zero.

An explicit all-frequency bound is

\[
|\Phi_{n,\lambda}(\theta)|
\le
\exp\left(-2p_0(\lambda)p_1(\lambda)\sin^2(\theta/2)\right).
\]

### N3-ANA-019, endpoint-uniform minor-arc obstruction

No fixed `rho<1` can bound nonzero torus frequencies uniformly over all finite tilts.

For every fixed `theta`,

\[
\sup_{\lambda\in\mathbb R}
|\Phi_{n,\lambda}(\theta)|=1.
\]

The law freezes at zero as `lambda->-infinity` and at the layer maxima as `lambda->+infinity`.

Therefore the final analytic bulk must provide compact tilt or an equivalent direct phase-dispersion lower bound.

Proof:

`proofs/MARKER_THREE_NUMERICAL_LAW_FOUNDATIONS.md`.

Response:

`handoffs/RESPONSE_TO_NOVA2_MARKER_THREE.md`.

## Current theorem frontier

| IDs | State |
|---|---|
| N3-ANA-004 through N3-ANA-010 | Exact product, local ceiling, distribution, minor-arc obstruction, high-prime CLT, coarse windows, explicit prime interval |
| N3-ANA-011 | Old-address capacity proved but structural model superseded |
| N3-ANA-012 | Compact-tilt top-prime logarithmic coarse windows proved |
| N3-ANA-013 | Unit-tilt Gaussian route disproved |
| N3-ANA-014 and N3-ANA-015 | Repaired marker-three capacity proved |
| N3-ANA-016 | Invalid central-binomial shortcut disproved |
| N3-ANA-017 and N3-ANA-018 | Active numerical contract, centering, span, and exact resonances proved |
| N3-ANA-019 | Uniform all-tilt minor-arc gap disproved |

## Verification

```text
python3 tracks/nova3-analytic-density/proofs/scale_sanity.py
python3 tracks/nova3-analytic-density/proofs/prime_interval_capacity_sanity.py
python3 tracks/nova3-analytic-density/proofs/compact_tilt_sanity.py
python3 tracks/nova3-analytic-density/proofs/marker_three_capacity_sanity.py
python3 tracks/nova3-analytic-density/proofs/marker_three_numerical_law_sanity.py
```

New finite records:

- N3-FIN-004, exact repaired capacity audit at `n=120368`;
- N3-FIN-005, exact marker-three supports and span for `n in {12,15}`;
- N3-COMP-004, numerical tilt and sampled torus checks.

## Cross-track state

### Nova 1

The repaired capacity request is closed. Nova 1 must replace its invalid central-binomial proof step with the quotient-factorial proof.

Nova 1 endpoint theorems N1-STR-019, N1-STR-020, and N1-RED-006 are compatible with the active marker-three law.

### Nova 2

The active law is `N2-HO-N3-003`.

Closed clauses:

- structural version compatibility;
- tilt existence and uniqueness;
- exact additive span;
- exact resonance set;
- an explicit target-dependent all-frequency bound.

Open clauses:

- exact final analytic target interval after all deterministic prefixes and contraction results;
- uniform variance and third-moment bounds there;
- compact tilt or direct quantitative phase dispersion;
- reference lattice law;
- strict weighted Fourier inequality.

### Nova 4

Independent reconstruction is required through N3-ANA-019 and N3-FIN-005.

## Exact blockers

1. Nova 1 and Nova 2 must freeze the exact transition from deterministic coverage to analytic responsibility.
2. That range must imply compact tilt or an equivalent probability lower bound for enough active numerical coordinates.
3. Constant-width windows require a local torus error smaller than order `1/sigma`; distribution-distance Berry-Esseen is not enough.
4. Fine top-prime logarithmic windows remain open but are secondary to the numerical marker-three contract.
5. Phase 12L and Phase 12P source packages remain unavailable.
6. The branch remains divergent from `main`.

## Handoffs

- `handoffs/RESPONSE_TO_NOVA1.md`
- `handoffs/RESPONSE_TO_NOVA1_MARKER_THREE.md`
- `handoffs/RESPONSE_TO_NOVA2_MARKER_THREE.md`
- `handoffs/TO_NOVA1_COMPACT_TILT.md`
- `handoffs/TO_NOVA2.md`
- `handoffs/TO_NOVA2_COMPACT_TILT.md`
- `handoffs/TO_NOVA4.md`
- `handoffs/TO_NOVA4_COMPACT_TILT.md`

## Next theorem target

`N3-NEXT-005`: after Nova 1 and Nova 2 freeze the exact remaining quotient targets, prove a compact bound on the numerical tilt or a direct phase-dispersion lower bound. If neither is true, return the smallest exact target family where the variance or minor-arc coefficient collapses.