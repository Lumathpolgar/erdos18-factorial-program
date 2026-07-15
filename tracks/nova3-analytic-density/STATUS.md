# Nova 3 Status

## Track

Analytic Divisor Density

## Branch

`nova/analytic-density`

## Baseline

- Starting branch head: `c79cddee6e8940e27ff256c29a85a3fc93766f7b`
- Main head inspected: `68ace6c9c3b67636e298a406fee3bfe8e072741d`
- Merge base: `cd5576d4f7934e26e9d4ef3b065c2ad4cee36c67`
- Startup relation: branch was already divergent, four commits ahead of the merge base and twelve commits behind main
- No rebase, force-push, merge into main, or edit to another Nova branch was performed

## Overall state

`THIRD_SUBSTANTIVE_CHECKPOINT_COMPLETE`

The main problem and the direct factorial half-range theorem remain open.

## New analytic result

The compact nonzero-tilt coarse-window node is closed for the exact top-prime divisor family.

For

\[
\mathcal P_n=\{p\text{ prime}:n/2<p\le n\},
\]

every prime has valuation one in `n!`. Under the exponential tilt

\[
\mathbb P_\theta(A_p=1)=\frac{p^\theta}{1+p^\theta},
\]

N3-ANA-012 proves a uniform Gaussian approximation and logarithmic-window lower bound for every fixed compact range

\[
|\theta|\le\theta_0<1.
\]

The admissible coarse-window width is

\[
\Delta\ge K_A\log n,
\]

with explicit constants depending only on the fixed displacement bound `A` and a universal Berry-Esseen constant.

N3-ANA-013 proves that this tilt restriction is structural: at `theta=1` and `theta=-1`, the normalized law converges to zero in probability rather than to a Gaussian.

## Proved results

| ID | Result class | Statement | Proof location |
|---|---|---|---|
| N3-ANA-004 | proved theorem | Exact independent exponent model, moments, saddle parameter, and exponential tilt | `proofs/PRODUCT_MODEL_THEOREMS.md` |
| N3-ANA-005 | proved theorem | Exact uniform local-count ceiling by conditioning on one prime exponent | `proofs/PRODUCT_MODEL_THEOREMS.md` |
| N3-ANA-006 | proved theorem | Full uniform log-divisor model converges to a non-Gaussian infinite convolution | `proofs/PRODUCT_MODEL_THEOREMS.md` |
| N3-ANA-008 | proved theorem | High-prime tail central limit theorem after a cutoff tending to infinity | `proofs/PRODUCT_MODEL_THEOREMS.md` |
| N3-ANA-010 | proved theorem | `pi(n)-pi(n/2)>=n/(3 log n)` for every integer `n>=120368` | `proofs/EXPLICIT_PRIME_INTERVAL_AND_CAPACITY.md` |
| N3-ANA-011 | proved theorem | Legal Nova 1 addresses, explicit menu lower bounds, and formal profile capacity for every `n>=120368` | `proofs/EXPLICIT_PRIME_INTERVAL_AND_CAPACITY.md` |
| N3-ANA-012 | proved theorem | Uniform compact-tilt Gaussian approximation, coarse-window positivity, and weighted distinct subset-product count for `(n/2,n]` | `proofs/COMPACT_TILT_TOP_PRIME_BAND.md` |

## Conditional result

| ID | Result class | Statement | Dependency |
|---|---|---|---|
| N3-ANA-009 | conditional theorem | Coarse central-window lower bound for the full high-prime logarithmic tail when `Delta>=K M_{n,y}` | Berry-Esseen, N3-SRC-003 |

## Disproved estimates and rejected transfers

| ID or route | Result class | Statement |
|---|---|---|
| N3-ANA-007 | disproved estimate | No fixed-`n` logarithmic characteristic function has uniform modulus below one on every sufficiently large frequency |
| N3-ANA-013 | disproved estimate | A top-prime Gaussian theorem cannot be uniform on a fixed tilt range reaching `|theta|=1` |
| Full-vector Gaussian route | disproved estimate | Low-prime coordinates retain macroscopic variance and the normalized full model is non-Gaussian |
| Smooth-number lower-bound transfer | rejected inference | Lower bounds for a larger smooth or ultrafriable set do not transfer to exact divisors of `n!` |
| Direct log-to-additive Fourier transfer | rejected inference | A theorem for `E exp(it log d)` does not control `E exp(it d)` or a numerical rainbow sum |

## Cross-track status

### Nova 1

The explicit prime-interval and formal menu-capacity request remains closed by N3-ANA-010 and N3-ANA-011 with

\[
n_3=n_4=n_5=120368.
\]

N3-ANA-012 is available as an independent logarithmic subset-product reservoir theorem. It does not repair the rejected power-of-two additive lattice construction.

### Nova 2

Nova 2's correct future Fourier object is the exact numerical additive law on `[-pi,pi]`. No layer-specific request is active because the first Nova 1 construction failed the lattice and first-window gate.

N3-ANA-012 must not be imported as numerical additive occupancy evidence. It concerns `log d` for top-prime subset products.

### Nova 4

Independent reconstruction is required for N3-ANA-004 through N3-ANA-013 and the finite verifiers.

## Finite certificates and computational evidence

### N3-FIN-001

- Range: every integer `2<=n<=12`
- Command: `python3 tracks/nova3-analytic-density/proofs/scale_sanity.py`

### N3-FIN-002

- Range: every integer `120368<=n<=1000000`
- Command: `python3 tracks/nova3-analytic-density/proofs/prime_interval_capacity_sanity.py`

### N3-FIN-003

- Exhaustive cases: `n in {11,17,29,43}` and `theta in {-0.75,-0.25,0,0.25,0.75}`
- Verified: tilted normalization, mean, variance, and third-moment ceiling by direct subset enumeration
- Command: `python3 tracks/nova3-analytic-density/proofs/compact_tilt_sanity.py`

### N3-COMP-002

Selected rows through `n=1000000` verify the displayed variance and third-moment inequalities for `theta_0` through `0.90` and illustrate unit-tilt freezing. These rows are computational evidence only.

## Source audit

Accepted external inputs:

- Robbins explicit Stirling bounds
- prime number theorem
- Berry-Esseen inequality
- Dusart Theorem 6.9 explicit bounds for `pi(x)`

No new external theorem was imported for the compact-tilt checkpoint.

## Exact blockers

1. Nova 1 must replace the rejected power-of-two lattice construction before additive Fourier analysis is relevant.
2. A revised layer system must pass Nova 2's common-lattice, residue, correction-radius, first-target, endpoint, and distinctness gates.
3. Nova 2 must then freeze the exact numerical additive law, target-dependent weights, major arcs, minor arcs, interval kernel, reference law, and error scale.
4. Fine logarithmic windows below `K_A log n` remain open even for the top-prime band.
5. The compact-tilt theorem for the full bounded-exponent high-prime tail remains open; N3-ANA-012 treats the exact Bernoulli band `(n/2,n]`.
6. Independent Nova 4 reconstruction remains required.
7. The Phase 12L and Phase 12P source packages remain outside the repository.
8. The branch remains divergent from main, and no history rewrite is permitted.

## Handoffs

- `handoffs/TO_NOVA1.md`
- `handoffs/RESPONSE_TO_NOVA1.md`
- `handoffs/TO_NOVA2.md`
- `handoffs/TO_NOVA4.md`
- `handoffs/TO_NOVA1_COMPACT_TILT.md`
- `handoffs/TO_NOVA2_COMPACT_TILT.md`
- `handoffs/TO_NOVA4_COMPACT_TILT.md`

## Next theorem target

`N3-NEXT-003`: determine the sharpest true local theorem below logarithmic width `K_A log n` for the top-prime tilted subset-product model. Prove a bounded-frequency local estimate, or prove a resonance or spacing obstruction that prevents uniform positivity at the requested scale.