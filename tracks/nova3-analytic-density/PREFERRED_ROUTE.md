# Preferred Analytic Route

## Route decision

- Decision ID: `N3-ROUTE-004`
- Status: `PROVED` as a route ranking and obstruction decision; the final occupancy theorem remains `OPEN`
- Date: 2026-07-15

## Mandatory model distinction

Two Fourier objects remain separate:

1. logarithmic divisor size,
   \[
   \mathbb E e^{it\log d};
   \]
2. numerical additive occupancy,
   \[
   \mathbb E e^{itT_n}.
   \]

The active cross-track target is now the second object for Nova 1 marker-three construction `N1-CON-003`.

## Ranked routes

### 1. Marker-three numerical product law

Status: `ACTIVE_CROSS_TRACK_ROUTE`.

Exact source:

- Nova 2 branch: `nova/additive-occupancy`
- commit: `fb73e6906105c983bacbd46a96ef8d5d87567fae`
- handoff: `N2-HO-N3-003`

The supports are

\[
B_t(n)=
\{2^{t-1}u:u\text{ odd},\ 3u\mid n!,\ 2^{t-1}u\le Y_n\}.
\]

Closed by N3-ANA-017 and N3-ANA-018:

- structural version compatibility;
- unique finite target-dependent tilt for every `W_n<q<=Y_n`;
- exact additive span one;
- exact resonance set `{0}`;
- explicit global bound
  \[
  |\Phi_{n,\lambda}(\theta)|
  \le
  \exp(-2p_0p_1\sin^2(\theta/2)).
  \]

N3-ANA-019 proves that no minor-arc gap can be uniform over all real tilts. The next positive step must therefore use the exact post-prefix target range to prove compact tilt or direct phase dispersion.

### 2. Deterministic-to-analytic quotient decomposition

Status: `REQUIRED_INTERFACE`.

The analytic range must begin only after combining:

- Nova 2's deterministic binary-spine prefix;
- Nova 1 multiplicative 3-density;
- Nova 1 endpoint support;
- Nova 1 deterministic coarse contraction;
- any remaining deterministic transition argument.

The union of deterministic and analytic target sets must cover every required quotient without a gap.

### 3. Repaired marker-three capacity

Status: `PROVED_SUPPORTING_ROUTE`.

N3-ANA-014 and N3-ANA-015 prove legal repaired menus and formal capacity for all `n>=120368`.

The proof uses

\[
n!/H_n\ge\lfloor n/2\rfloor!
\]

rather than the false central-binomial divisibility shortcut rejected by N3-ANA-016.

Capacity does not imply occupancy.

### 4. Compact-tilt top-prime logarithmic reservoir

Status: `PROVED_INTRINSIC_COMPONENT`.

N3-ANA-012 gives a Gaussian coarse-window theorem for exact top-prime subset products under `|theta|<=theta_0<1`. N3-ANA-013 proves failure at unit tilt.

This route remains useful for intrinsic divisor density but does not transfer directly to the numerical quotient law.

### 5. Full bounded-exponent logarithmic high-prime model

Status: `SECONDARY_GENERALIZATION`.

N3-ANA-008 and N3-ANA-009 establish the zero-tilt coarse regime. Compact-tilt and fine local results remain open.

### 6. Fine top-prime logarithmic local analysis

Status: `OPEN_BUT_SECONDARY`.

Lowering the current `K_A log n` width remains a valid intrinsic problem, but the active numerical marker-three contract has higher integration priority.

## Rejected or disproved routes

### Old power-of-two address construction

Status: `DISPROVED_BY_NOVA_2`.

Its main sums lie in a sublattice missing the first target window.

### Older Nova 2 three-power repair handoff

Status: `NOT_ACTIVE_FOR_N1-CON-003`.

`N2-HO-N3-002` describes a different repaired model. The active marker-three law is `N2-HO-N3-003`.

### Uniform all-tilt minor-arc modulus gap

Status: `DISPROVED_BY_N3-ANA-019`.

The numerical law freezes at both tilt endpoints.

### Full logarithmic Gaussian model

Status: `DISPROVED_BY_N3-ANA-006`.

### Unrestricted logarithmic minor-arc decay

Status: `DISPROVED_BY_N3-ANA-007`.

### Smooth-number lower-bound transfer

Status: `REJECTED`.

## Exact current deliverable

For the active numerical marker-three law, Nova 3 now provides:

1. unique target-dependent centering;
2. exact lattice span;
3. exact resonance set;
4. an explicit target-dependent characteristic-function bound;
5. a proof that endpoint-uniform decay is impossible.

The strict weighted Fourier inequality remains open.

## Stop conditions

Abandon or weaken any proposed next step if it:

- uses logarithmic divisor weights instead of numerical quotient values;
- ignores the deterministic prefix and endpoint handoff;
- assumes span one gives a quantitative minor-arc gap;
- asks for a target-uniform decay constant over all tilts;
- uses Berry-Esseen distribution distance as a constant-width local theorem;
- treats formal profile capacity as numerical sumset coverage;
- leaves a transition gap between deterministic and analytic target ranges.

## Next theorem target

`N3-NEXT-005`: on the exact target range remaining after deterministic coverage, prove a compact bound on `lambda_{n,q}` or a direct lower bound for enough phase-dispersing coordinate probabilities. If this fails, identify the first exact target family where variance or the minor-arc coefficient collapses.