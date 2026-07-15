# Nova 1 Status

## Track and branch

- Track: Factorial Structure and Reduction
- Branch: `nova/factorial-structure`
- Overall state: `FULL_CORE_FINITE_EXTENSION_CONNECTED_PREFIX_ENTROPY_OPEN`

The factorial half-range theorem remains open.

## Current objective

Prove or disprove quotient downward-window occupancy for the repaired marker-three valuation rainbow construction `N1-CON-003`.

The immediate sequential subproblem is now exact:

> Prove that enough complete odd-core prefixes remain connected from zero to satisfy the connected-prefix entropy requirement `N1-OBS-003`, or prove that they cannot.

## Imported cross-track results

### Nova 2 original obstruction

- branch: `nova/additive-occupancy`
- exact commit: `45c74a5fa747551422ffcad7d3ddf22788fbe622`
- theorem: `N2-ADD-115`
- disproved model: `N2-OBS-107`

The original valuation-tagged route remains a **disproved route**.

### Nova 2 marker-three carrier intake

The repaired construction was accepted with restrictions at:

- branch: `nova/additive-occupancy`
- exact commit: `b15278e21f91e0e188b1c7c3e9a10e58a1db20fe`
- outcome: `ACCEPTED_WITH_RESTRICTIONS`
- results: `N2-ADD-119`, `N2-ADD-120`

The latest imported complete-menu certificate is:

- branch: `nova/additive-occupancy`
- exact commit: `82603c631a106c3bff4676bdeeb9cc791fc98f3c`
- result: `N2-FIN-202`
- classification: **finite certificate**
- range: every `12<=n<=45`

Nova 2 independently accepted the exact lattice, quotient span, correction reduction, distinctness, and term cost. Its connected-core recursion is a sufficient sequential engine, not the full final-only theorem.

### Nova 3 inputs

Prime-interval capacity input:

- branch: `nova/analytic-density`
- exact commit: `e60069f797af878711e7a9d4abb1fb6188a1f724`
- results: `N3-ANA-010`, `N3-ANA-011`

Numerical-law foundation:

- branch: `nova/analytic-density`
- exact head inspected: `003b9c0e1179314d6c119c8a356e0f41231e3ad6`
- results: `N3-ANA-017`, `N3-ANA-018`, `N3-ANA-019`
- outcome: `ACCEPTED_WITH_RESTRICTIONS`

The exact numerical tilt exists, the additive span is one, and the only torus resonance is zero. A target-independent minor-arc gap over all tilts is a **disproved route** because the law freezes at the tilt endpoints.

## Proved results

| ID | Result label | Statement | Location |
|---|---|---|---|
| N1-STR-003 | proved theorem | Exact Legendre budgets, quotient bands, dyadic bands, and 2-adic multiplicity | `proofs/VALUATION_BUDGET_LEMMAS.md` |
| N1-STR-004 | proved theorem | Valuation boxes produce unique legal divisors | `FACTORIAL_DIVISOR_ATLAS.md` |
| N1-STR-005 | proved theorem | Allocated valuation budgets preserve legality | `FACTORIAL_DIVISOR_ATLAS.md` |
| N1-STR-006 | proved theorem | Marker signatures enforce distinctness | `proofs/DISTINCTNESS_AND_CORRECTION.md` |
| N1-STR-007 | proved theorem | Complement pairing preserves legality and distinctness | `proofs/COMPLEMENT_PAIRING_LEMMA.md` |
| N1-COR-001 | proved theorem | Binary correction palette gives exact residual representation | `proofs/DISTINCTNESS_AND_CORRECTION.md` |
| N1-RED-002 | proved theorem | Downward-window occupancy plus correction gives exact coverage | `proofs/DISTINCTNESS_AND_CORRECTION.md` |
| N1-OBS-002 | proved theorem | Downward-window counting-capacity inequality | `proofs/COUNTING_CAPACITY_OBSTRUCTION.md` |
| N1-STR-008 | proved theorem | Polylogarithmic layers require geometric-mean menu size `exp(Omega(n/log n))` | `proofs/MENU_ENTROPY_REQUIREMENT.md` |
| N1-STR-009 | proved theorem | High-prime subset products supply exponentially many legal cores | `proofs/HIGH_PRIME_MENU_CAPACITY.md` |
| N1-STR-014 | proved theorem | Marker-three legality and numerical distinctness | `proofs/MARKER_THREE_LATTICE_REPAIR.md` |
| N1-STR-015 | proved theorem | Exact main lattice `3Z` and all correction residues | `proofs/MARKER_THREE_LATTICE_REPAIR.md` |
| N1-RED-004 | proved theorem | Quotient `W_n`-window occupancy implies the factorial half-range bound | `proofs/MARKER_THREE_LATTICE_REPAIR.md` |
| N1-STR-016 | proved theorem | Odd positional digits have maximum downward gap one | `proofs/MARKER_THREE_LATTICE_REPAIR.md` |
| N1-STR-017 | proved theorem | Unconditional `exp(O((log n)^2))` initial interval | `proofs/MARKER_THREE_LATTICE_REPAIR.md` |
| N1-STR-018 | proved theorem | Every repaired layer has exponentially many high-prime cores for `n>=120368` | `proofs/MARKER_THREE_MENU_CAPACITY.md` |
| N1-CAP-002 | proved theorem | Formal profile-capacity gate holds for `n>=120368` | `proofs/MARKER_THREE_MENU_CAPACITY.md` |
| N1-STR-019 | proved theorem | Reserved odd factorial core is multiplicatively 3-dense | `proofs/QUOTIENT_ENDPOINT_SUPPORT.md` |
| N1-STR-020 | proved theorem | Total quotient support crosses `floor(X_n/3)` | `proofs/QUOTIENT_ENDPOINT_SUPPORT.md` |
| N1-RED-006 | proved theorem | Coarse deterministic residual contraction | `proofs/QUOTIENT_ENDPOINT_SUPPORT.md` |
| N1-STR-021 | proved theorem | Factorial arithmetic blocks are legal connected submenus | `proofs/FACTORIAL_BLOCK_CARRIER_OBSTRUCTION.md` |
| N1-COL-001 | proved theorem | Exponential carry collisions prove profile noninjectivity | `proofs/RAINBOW_CARRY_COLLISIONS.md` |
| N1-OBS-003 | proved theorem | Successful connected-core carrier requires geometric-mean connected-prefix size at least `exp(n/(85 log n))` | `proofs/CONNECTED_PREFIX_ENTROPY_REQUIREMENT.md` |

## Conditional results

| ID | Result label | Statement | Open dependency |
|---|---|---|---|
| N1-RED-005 | conditional theorem | Quotient rainbow occupancy implies `H_{n!}(floor(sqrt(n!))+1)=O((log n)^2)` | Global quotient occupancy |
| HIST-001 | conditional theorem | Half-range theorem implies `h(n!)=O((log n)^3)` | Current-notation Track B reconstruction |

## Finite certificates and computational evidence

| ID | Result label | Scope | Location |
|---|---|---|---|
| N1-CMP-003 | computational evidence | Reduced exact quotient checks for `7<=n<=14` | `verification/MARKER_THREE_FINITE_REPORT.md` |
| N1-CMP-004 | finite certificate | 3-density, endpoint crossing, and coarse contraction checks | `verification/ENDPOINT_SUPPORT_FINITE_REPORT.md` |
| N1-CMP-005 | finite certificate | Factorial blocks, one-block ceiling, and carry collisions | `verification/BLOCK_COLLISION_FINITE_REPORT.md` |
| N1-FIN-005 | finite certificate | Complete truncated odd-core carrier reaches `Y_n` for every `46<=n<=50` in six layers | `verification/FULL_CORE_N46_N50_REPORT.md` |
| N2-FIN-202 | finite certificate | Imported complete-menu carrier reaches `Y_n` for every `12<=n<=45` | Nova 2 commit `82603c631a106c3bff4676bdeeb9cc791fc98f3c` |

Together, the complete-core carrier is exactly certified for every `12<=n<=50`. This is not an asymptotic theorem.

## Disproved routes

| ID | Result label | Route eliminated | Proof |
|---|---|---|---|
| N1-DIS-001 | disproved route | Treating prime powers of one prime as independent coordinates | `FACTORIAL_DIVISOR_ATLAS.md` |
| N1-DIS-002 | disproved route | Fixed binary or ternary pools in `O((log n)^2)` layers | `proofs/COUNTING_CAPACITY_OBSTRUCTION.md` |
| N1-DIS-003 | disproved route | Polynomial-size menus with polynomial correction | `proofs/MENU_ENTROPY_REQUIREMENT.md` |
| N1-DIS-004 | disproved route | Complement pairing alone implies additive density | `proofs/COMPLEMENT_PAIRING_LEMMA.md` |
| N1-DIS-005 | disproved route | Original addresses `e_t=r_n+t` | Nova 2 `N2-ADD-115` |
| N1-DIS-006 | disproved route | One factorial arithmetic block per carrier layer reaches the endpoint | `proofs/FACTORIAL_BLOCK_CARRIER_OBSTRUCTION.md` |

## Closed structural gates for N1-CON-003

- divisor legality;
- layer and palette distinctness;
- exact common lattice;
- attained residue classes;
- first-target coverage;
- selected-term cost;
- formal profile capacity;
- total endpoint support;
- one-block carrier ceiling;
- profile-map noninjectivity;
- exact finite complete-core carrier coverage through `n=50`.

## Exact open blockers

1. Prove or disprove connected prefixes of geometric-mean size `exp(Omega(n/log n))` under the exact carrier thresholds.
2. Prove or disprove the full quotient downward-window theorem.
3. Prove downward endpoint-window occupancy, not only total endpoint reach.
4. Upper-bound target-local collision multiplicity or additive energy.
5. Prove compact numerical tilt or quantitative phase dispersion on the exact unresolved target range.
6. Prove the strict weighted bounded-torus Fourier inequality.
7. Reconstruct Track B under the frozen endpoint convention.
8. Handle finite exceptions after an effective asymptotic threshold exists.

## Verification

```text
python tracks/nova1-factorial-structure/verification/structural_sanity.py
python tracks/nova1-factorial-structure/verification/marker_three_sanity.py
python tracks/nova1-factorial-structure/verification/endpoint_support_sanity.py
python tracks/nova1-factorial-structure/verification/block_collision_sanity.py

g++ -O3 -std=c++17 \
  tracks/nova1-factorial-structure/verification/marker_three_full_core_u128.cpp \
  -o marker_three_full_core_u128
```

## Next theorem target

Prove a uniform lower bound on the complete zero-connected prefix cardinalities `K_t` strong enough to meet `N1-OBS-003`. A general upper bound below that threshold is equally valid and would retire the sequential carrier engine.

In parallel, the final-only route must bound target-local collision energy and establish compact phase dispersion on the unresolved quotient targets.