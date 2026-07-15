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

`SECOND_SUBSTANTIVE_CHECKPOINT_COMPLETE`

The main problem and the direct factorial half-range theorem remain open.

## New cross-track result

Nova 1's explicit prime-interval and formal menu-capacity dependency is closed.

Imported request:

- branch: `nova/factorial-structure`
- exact commit: `fa11f4b2cb86a2dd791df189ada12757be791804`
- request: `N1-HO-N3-001`

Returned result:

- handoff: `handoffs/RESPONSE_TO_NOVA1.md`
- outcome: `ACCEPTED`
- explicit thresholds:
  \[
  n_3=n_4=n_5=120368.
  \]

## Proved results

| ID | Result class | Statement | Proof location |
|---|---|---|---|
| N3-ANA-004 | proved theorem | Exact independent exponent model, moments, saddle parameter, and exponential tilt | `proofs/PRODUCT_MODEL_THEOREMS.md` |
| N3-ANA-005 | proved theorem | Exact uniform local-count ceiling by conditioning on one prime exponent | `proofs/PRODUCT_MODEL_THEOREMS.md` |
| N3-ANA-006 | proved theorem | Full uniform log-divisor model converges to a non-Gaussian infinite convolution | `proofs/PRODUCT_MODEL_THEOREMS.md` |
| N3-ANA-008 | proved theorem | High-prime tail central limit theorem after a cutoff tending to infinity | `proofs/PRODUCT_MODEL_THEOREMS.md` |
| N3-ANA-010 | proved theorem | `pi(n)-pi(n/2)>=n/(3 log n)` for every integer `n>=120368` | `proofs/EXPLICIT_PRIME_INTERVAL_AND_CAPACITY.md` |
| N3-ANA-011 | proved theorem | Legal Nova 1 addresses, explicit menu lower bounds, and formal profile capacity for every `n>=120368` | `proofs/EXPLICIT_PRIME_INTERVAL_AND_CAPACITY.md` |

## Conditional result

| ID | Result class | Statement | Dependency |
|---|---|---|---|
| N3-ANA-009 | conditional theorem | Coarse central-window lower bound for the high-prime logarithmic tail when `Delta>=K M_{n,y}` | Berry-Esseen, N3-SRC-003 |

## Disproved estimates and rejected transfers

| ID or route | Result class | Statement |
|---|---|---|
| N3-ANA-007 | disproved estimate | No fixed-`n` logarithmic characteristic function has uniform modulus below one on every sufficiently large frequency |
| Full-vector Gaussian route | disproved estimate | Low-prime coordinates retain macroscopic variance and the normalized full model is non-Gaussian |
| Smooth-number lower-bound transfer | rejected inference | Lower bounds for a larger smooth or ultrafriable set do not transfer to exact divisors of `n!` |
| Direct log-to-additive Fourier transfer | rejected inference | A theorem for `E exp(it log d)` does not control `E exp(it d)` or a numerical rainbow sum |

## Nova 2 contract audit

Nova 2 responded from:

- branch: `nova/additive-occupancy`
- exact commit: `45c74a5fa747551422ffcad7d3ddf22788fbe622`
- file: `tracks/nova2-additive-occupancy/handoffs/RESPONSE_TO_NOVA3.md`

Outcome: `ACCEPTED_WITH_RESTRICTIONS`.

The correct future Fourier object is an integer-valued numerical additive sum on the torus `[-pi,pi]`, with every resonance listed and a weighted `L^1` error against the exact interval kernel. No layer-specific analytic request is active because Nova 2 proved that the first Nova 1 layer system misses its first required window through a power-of-two lattice obstruction.

Nova 3 will not perform an unmatched logarithmic Fourier calculation and present it as additive occupancy evidence.

## Finite certificates and computational evidence

### N3-FIN-001

- Result class: finite certificate
- Range: every integer `2<=n<=12`
- Verified: divisor uniqueness, exact `tau(n!)`, complement symmetry, exact log moments, and local-count ceiling
- Command: `python3 tracks/nova3-analytic-density/proofs/scale_sanity.py`

### N3-FIN-002

- Result class: finite certificate
- Range: every integer `120368<=n<=1000000`
- Verified: exact upper-half prime counts, exact 2-adic valuations, address legality, and conservative profile capacity
- Minimum prime-count margin: greater than `1824`
- Minimum address slack: `57942`
- Minimum conservative capacity margin: greater than `10,488,000` bits
- Command: `python3 tracks/nova3-analytic-density/proofs/prime_interval_capacity_sanity.py`

Larger convergence tables printed by `scale_sanity.py` remain computational evidence only.

## Source audit

Accepted external inputs:

- Robbins explicit Stirling bounds
- prime number theorem
- Berry-Esseen inequality
- Dusart Theorem 6.9 explicit bounds for `pi(x)`

Restricted or rejected sources and inference directions remain recorded in `SOURCE_LEDGER.md`.

## Exact blockers

1. Nova 1 must replace the rejected power-of-two lattice construction before additive Fourier analysis is relevant.
2. A revised layer system must pass Nova 2's common-lattice, residue, correction-radius, first-target, endpoint, and distinctness gates.
3. After that structural gate, Nova 2 must freeze the exact numerical additive law, target-dependent weights, major arcs, minor arcs, interval kernel, reference law, and required error scale.
4. No fine tilted lower-window theorem is known for exact factorial logarithmic divisors below the largest remaining coordinate span.
5. Compact nonzero-tilt uniformity for N3-ANA-009 remains open.
6. Independent Nova 4 reconstruction of N3-ANA-004 through N3-ANA-011 remains required.
7. The Phase 12L and Phase 12P source packages remain outside the repository.
8. The branch remains divergent from main, and no history rewrite is permitted.

## Handoffs

- `handoffs/TO_NOVA1.md`
- `handoffs/RESPONSE_TO_NOVA1.md`
- `handoffs/TO_NOVA2.md`
- `handoffs/TO_NOVA4.md`

## Next theorem target

`N3-NEXT-002`: extend the high-prime coarse-window theorem to a compact nonzero exponential-tilt range with explicit uniform moment and Berry-Esseen constants. This work is independent of the currently invalid additive layer system and can later be specialized after a repaired construction passes Nova 2's structural gate.