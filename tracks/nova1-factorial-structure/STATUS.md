# Nova 1 Status

## Track and branch

- Track: Factorial Structure and Reduction
- Branch: `nova/factorial-structure`
- Overall state: `BLOCK_CARRIER_OBSTRUCTION_AND_COLLISION_CHECKPOINT`

The factorial half-range theorem remains open.

## Current objective

Prove or disprove quotient downward-window occupancy for the repaired marker-three valuation rainbow construction `N1-CON-003`.

## Imported cross-track results

### Nova 2 original obstruction

The first preferred route was rejected at:

- branch: `nova/additive-occupancy`
- exact commit: `45c74a5fa747551422ffcad7d3ddf22788fbe622`
- theorem: `N2-ADD-115`
- disproved model: `N2-OBS-107`

Every old main sum was divisible by `2^(r_n+1)`, while the old correction radius was only `2^r_n-1`.

### Nova 2 marker-three intake

The repaired marker-three construction was accepted with restrictions at:

- branch: `nova/additive-occupancy`
- exact commit: `b15278e21f91e0e188b1c7c3e9a10e58a1db20fe`
- outcome: `ACCEPTED_WITH_RESTRICTIONS`
- theorems: `N2-ADD-119`, `N2-ADD-120`

Nova 2 independently accepted the exact lattice, quotient span, correction reduction, distinctness, and term cost. Its carrier-block recursion is a sufficient sequential proof engine, not the full final-only theorem.

### Nova 3 prime interval theorem

The explicit prime interval input was accepted from:

- branch: `nova/analytic-density`
- exact commit: `e60069f797af878711e7a9d4abb1fb6188a1f724`
- theorems: `N3-ANA-010`, `N3-ANA-011`

For every `n>=120368`,

\[
\pi(n)-\pi(n/2)\ge\frac{n}{3\log n}.
\]

Nova 1 translated this input to the repaired marker-three menus.

## Proved results

| ID | Result label | Statement | Location |
|---|---|---|---|
| N1-STR-003 | proved theorem | Exact Legendre budgets, quotient bands, dyadic bands, and factorial 2-adic multiplicity | `proofs/VALUATION_BUDGET_LEMMAS.md` |
| N1-STR-004 | proved theorem | Independent valuation boxes produce unique legal divisors | `FACTORIAL_DIVISOR_ATLAS.md` |
| N1-STR-005 | proved theorem | Allocated valuation budgets preserve divisor legality | `FACTORIAL_DIVISOR_ATLAS.md` |
| N1-STR-006 | proved theorem | Marker signatures enforce numerical distinctness | `proofs/DISTINCTNESS_AND_CORRECTION.md` |
| N1-STR-007 | proved theorem | Complement pairing preserves legality and distinctness | `proofs/COMPLEMENT_PAIRING_LEMMA.md` |
| N1-COR-001 | proved theorem | Binary powers form a disjoint correction palette | `proofs/DISTINCTNESS_AND_CORRECTION.md` |
| N1-RED-002 | proved theorem | Downward-window occupancy plus binary correction gives exact coverage | `proofs/DISTINCTNESS_AND_CORRECTION.md` |
| N1-OBS-002 | proved theorem | Downward-window counting-capacity inequality | `proofs/COUNTING_CAPACITY_OBSTRUCTION.md` |
| N1-STR-008 | proved theorem | `O((log n)^2)` layers require geometric-mean menus of size `exp(Omega(n/log n))` | `proofs/MENU_ENTROPY_REQUIREMENT.md` |
| N1-STR-009 | proved theorem | High-prime subset products supply exponentially many legal cores | `proofs/HIGH_PRIME_MENU_CAPACITY.md` |
| N1-STR-014 | proved theorem | Marker-three layers are legal and numerically distinct from each other and the palette | `proofs/MARKER_THREE_LATTICE_REPAIR.md` |
| N1-STR-015 | proved theorem | Exact main support lattice is `3Z`, and the palette attains all residues modulo `3` | `proofs/MARKER_THREE_LATTICE_REPAIR.md` |
| N1-RED-004 | proved theorem | Quotient `W_n`-window occupancy implies exact factorial half-range coverage | `proofs/MARKER_THREE_LATTICE_REPAIR.md` |
| N1-STR-016 | proved theorem | Odd positional digits have maximum downward gap one | `proofs/MARKER_THREE_LATTICE_REPAIR.md` |
| N1-STR-017 | proved theorem | Repaired construction covers an unconditional `exp(O((log n)^2))` initial interval | `proofs/MARKER_THREE_LATTICE_REPAIR.md` |
| N1-STR-018 | proved theorem | Every repaired layer has exponentially many legal high-prime cores for `n>=120368` | `proofs/MARKER_THREE_MENU_CAPACITY.md` |
| N1-CAP-002 | proved theorem | Repaired menus pass the necessary profile-capacity gate for every `n>=120368` | `proofs/MARKER_THREE_MENU_CAPACITY.md` |
| N1-STR-019 | proved theorem | The reserved odd factorial core is multiplicatively `3`-dense for every `n>=6` | `proofs/QUOTIENT_ENDPOINT_SUPPORT.md` |
| N1-STR-020 | proved theorem | Three distinct quotient-layer terms push total support past `floor(X_n/3)` for every `n>=12` | `proofs/QUOTIENT_ENDPOINT_SUPPORT.md` |
| N1-RED-006 | proved theorem | Deterministic quotient selection leaves residual below `max((2/3)^L q,2^L)` after `L` layers | `proofs/QUOTIENT_ENDPOINT_SUPPORT.md` |
| N1-STR-021 | proved theorem | Explicit factorial arithmetic blocks are legal connected submenus under the exact carrier threshold | `proofs/FACTORIAL_BLOCK_CARRIER_OBSTRUCTION.md` |
| N1-COL-001 | proved theorem | At least `2^floor(M_n/2)` legal profiles collide at one quotient sum for `n>=120368` | `proofs/RAINBOW_CARRY_COLLISIONS.md` |

## Conditional results

| ID | Result label | Statement | Open dependency |
|---|---|---|---|
| N1-RED-005 | conditional theorem | Frozen quotient rainbow occupancy implies `H_{n!}(floor(sqrt(n!))+1)=O((log n)^2)` | Nova 2 quotient occupancy theorem |
| HIST-001 | conditional theorem | Half-range theorem implies `h(n!)=O((log n)^3)` | Current-notation Track B reconstruction |

## Computational evidence

| Object | Result label | Scope | Location |
|---|---|---|---|
| N1-CMP-003 | computational evidence | Exact reduced marker-three quotient checks for every `7<=n<=14` | `verification/MARKER_THREE_FINITE_REPORT.md` |
| N1-CMP-004 | finite certificate | 3-density for `6<=n<=20`, endpoint crossing for `12<=n<=20`, and exhaustive coarse contraction for `12<=n<=14` | `verification/ENDPOINT_SUPPORT_FINITE_REPORT.md` |
| N1-CMP-005 | finite certificate | Factorial blocks, one-step carrier ceiling, carry collisions, and scale separation | `verification/BLOCK_COLLISION_FINITE_REPORT.md` |

## Disproved routes

| ID | Result label | Route eliminated | Proof |
|---|---|---|---|
| N1-DIS-001 | disproved route | Treating prime powers of one prime as independent coordinates | `FACTORIAL_DIVISOR_ATLAS.md` |
| N1-DIS-002 | disproved route | A fixed pool of `O((log n)^2)` binary or ternary divisor choices | `proofs/COUNTING_CAPACITY_OBSTRUCTION.md` |
| N1-DIS-003 | disproved route | Polynomial-size menus in `O((log n)^2)` layers with polynomial correction | `proofs/MENU_ENTROPY_REQUIREMENT.md` |
| N1-DIS-004 | disproved route | Complement pairing alone implies additive density | `proofs/COMPLEMENT_PAIRING_LEMMA.md` |
| N1-DIS-005 | disproved route | Old valuation tags `e_t=r_n+t` with radius `2^r_n-1` | Nova 2 `N2-ADD-115` at commit `45c74a5fa747551422ffcad7d3ddf22788fbe622` |
| N1-DIS-006 | disproved route | One factorial arithmetic carrier block per layer reaches the factorial endpoint | `proofs/FACTORIAL_BLOCK_CARRIER_OBSTRUCTION.md` |

## Candidate ranking

1. `N1-CON-003`: marker-three valuation rainbow, preferred repaired route.
2. `N1-CON-002`: marked complement-pair menu clouds, secondary globally nonsequential route.
3. `N1-CON-001`: disproved and superseded.

## Closed structural gates for N1-CON-003

- divisor legality;
- cross-layer and palette distinctness;
- exact common lattice;
- attained residue classes;
- first-target coverage;
- selected-term cost;
- formal profile capacity from `n>=120368`;
- maximum support reaches beyond `floor(X_n/3)`;
- explicit single-block carrier growth ceiling;
- noninjectivity of the profile-to-sum map.

## Exact open blockers

1. Prove or disprove the revised Nova 2 quotient occupancy handoff `N1-HO-N2-002`.
2. Prove downward endpoint-window occupancy in `[floor(X_n/3)-W_n,floor(X_n/3)]`; total endpoint reach is already proved.
3. Determine whether the complete connected core grows substantially faster than every single factorial arithmetic block.
4. Prove a target-local upper bound for collision multiplicity or additive energy.
5. Complete the numerical-value bounded-torus theorem requested by Nova 2.
6. Reconstruct the direct factorial Track B conversion under the frozen endpoint convention.
7. Handle finite exceptions only after an effective asymptotic threshold exists.

## Handoffs

- Nova 2: `handoffs/TO_NOVA2.md`, revised as `N1-HO-N2-002` and accepted with restrictions at exact commit `b15278e21f91e0e188b1c7c3e9a10e58a1db20fe`.
- Nova 3: `handoffs/TO_NOVA3.md`, repaired capacity reconstruction request.
- Nova 4: `handoffs/TO_NOVA4.md`, marker-three, endpoint, carrier, and collision verification request.

## Verification

Run:

```text
python tracks/nova1-factorial-structure/verification/structural_sanity.py
python tracks/nova1-factorial-structure/verification/marker_three_sanity.py
python tracks/nova1-factorial-structure/verification/endpoint_support_sanity.py
python tracks/nova1-factorial-structure/verification/block_collision_sanity.py
```

## Next theorem target

Analyze the complete connected component of the full core menu under the exact Nova 2 thresholds. A successful result must either exceed the one-block ceiling by a factorial-scale amount or prove that the entire sequential carrier engine remains too small.

In parallel, the final-only route requires a target-local collision-energy bound rather than raw profile counting.