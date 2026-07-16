# Nova 1 Status

## Track and branch

- Track: Factorial Structure and Reduction
- Branch: `nova/factorial-structure`
- Overall state: `FULL_CORE_CERTIFIED_THROUGH_N55_EFFECTIVE_UTILIZATION_OPEN`

The factorial half-range theorem remains open.

## Current objective

Prove or disprove quotient downward-window occupancy for `N1-CON-003`, the marker-three valuation rainbow.

The immediate sequential subproblem is to prove a uniform lower bound on the exact effective carrier product, including both connected-prefix count and packing utilization, or a contrary upper bound that retires the sequential engine.

## Imported cross-track results

### Nova 2 original obstruction

- branch: `nova/additive-occupancy`
- exact commit: `45c74a5fa747551422ffcad7d3ddf22788fbe622`
- theorem: `N2-ADD-115`
- disproved model: `N2-OBS-107`

The original valuation-tagged route remains a **disproved route**.

### Nova 2 marker-three package

- branch: `nova/additive-occupancy`
- exact accepted head: `2ab09dd980f7116b82530368e3d98bb53240bf0c`
- results: `N2-ADD-119`, `N2-ADD-120`, `N2-ADD-121`, `N2-ADD-122`, `N2-FIN-202`, `N2-FIN-203`, `N2-FIN-204`

Nova 2 accepts the carrier engine as a sufficient sequential method with restrictions. `N2-ADD-122` proves that count surplus alone is only a necessary gate because the exact endpoint product also contains packing-utilization factors.

### Nova 3 inputs

Prime-interval capacity:

- branch: `nova/analytic-density`
- exact commit: `e60069f797af878711e7a9d4abb1fb6188a1f724`
- results: `N3-ANA-010`, `N3-ANA-011`

Numerical-law foundation:

- exact head inspected: `003b9c0e1179314d6c119c8a356e0f41231e3ad6`
- results: `N3-ANA-017`, `N3-ANA-018`, `N3-ANA-019`
- outcome: `ACCEPTED_WITH_RESTRICTIONS`

A target-independent minor-arc gap over all tilts remains a **disproved route**.

## Proved theorems

| ID | Result label | Statement | Location |
|---|---|---|---|
| N1-STR-003 | proved theorem | Exact Legendre budgets, quotient bands, dyadic bands, and 2-adic multiplicity | `proofs/VALUATION_BUDGET_LEMMAS.md` |
| N1-STR-004 | proved theorem | Valuation boxes produce unique legal divisors | `FACTORIAL_DIVISOR_ATLAS.md` |
| N1-STR-005 | proved theorem | Allocated valuation budgets preserve legality | `FACTORIAL_DIVISOR_ATLAS.md` |
| N1-STR-006 | proved theorem | Marker signatures enforce distinctness | `proofs/DISTINCTNESS_AND_CORRECTION.md` |
| N1-STR-007 | proved theorem | Complement pairing preserves legality and distinctness | `proofs/COMPLEMENT_PAIRING_LEMMA.md` |
| N1-COR-001 | proved theorem | Binary correction palette represents every permitted residual | `proofs/DISTINCTNESS_AND_CORRECTION.md` |
| N1-RED-002 | proved theorem | Downward-window occupancy plus correction gives exact coverage | `proofs/DISTINCTNESS_AND_CORRECTION.md` |
| N1-OBS-002 | proved theorem | Downward-window counting-capacity inequality | `proofs/COUNTING_CAPACITY_OBSTRUCTION.md` |
| N1-STR-008 | proved theorem | Polylogarithmic layers require exponential geometric-mean menu size | `proofs/MENU_ENTROPY_REQUIREMENT.md` |
| N1-STR-009 | proved theorem | High-prime subset products supply exponentially many legal cores | `proofs/HIGH_PRIME_MENU_CAPACITY.md` |
| N1-STR-014 | proved theorem | Marker-three legality and numerical distinctness | `proofs/MARKER_THREE_LATTICE_REPAIR.md` |
| N1-STR-015 | proved theorem | Exact main lattice `3Z` and all correction residues | `proofs/MARKER_THREE_LATTICE_REPAIR.md` |
| N1-RED-004 | proved theorem | Quotient `W_n`-window occupancy implies the half-range bound | `proofs/MARKER_THREE_LATTICE_REPAIR.md` |
| N1-STR-016 | proved theorem | Odd positional digits have maximum downward gap one | `proofs/MARKER_THREE_LATTICE_REPAIR.md` |
| N1-STR-017 | proved theorem | Unconditional `exp(O((log n)^2))` initial interval | `proofs/MARKER_THREE_LATTICE_REPAIR.md` |
| N1-STR-018 | proved theorem | Every repaired layer has exponentially many high-prime cores for `n>=120368` | `proofs/MARKER_THREE_MENU_CAPACITY.md` |
| N1-CAP-002 | proved theorem | Formal profile-capacity gate holds for `n>=120368` | `proofs/MARKER_THREE_MENU_CAPACITY.md` |
| N1-STR-019 | proved theorem | Reserved odd factorial core is multiplicatively 3-dense | `proofs/QUOTIENT_ENDPOINT_SUPPORT.md` |
| N1-STR-020 | proved theorem | Total quotient support crosses `floor(X_n/3)` | `proofs/QUOTIENT_ENDPOINT_SUPPORT.md` |
| N1-RED-006 | proved theorem | Coarse deterministic residual contraction | `proofs/QUOTIENT_ENDPOINT_SUPPORT.md` |
| N1-STR-021 | proved theorem | Factorial arithmetic blocks are legal connected submenus | `proofs/FACTORIAL_BLOCK_CARRIER_OBSTRUCTION.md` |
| N1-COL-001 | proved theorem | Exponential carry collisions prove profile noninjectivity | `proofs/RAINBOW_CARRY_COLLISIONS.md` |
| N1-OBS-003 | proved theorem | Sequential success requires sufficient connected-prefix entropy | `proofs/CONNECTED_PREFIX_ENTROPY_REQUIREMENT.md` |
| N1-STR-022 | proved theorem | Unique-parent streaming recovers exact connected prefixes | `proofs/STREAMING_CONNECTED_PREFIX_CERTIFIER.md` |
| N1-STR-023 | proved theorem | Meet-in-the-middle product streams recover exact divisor order with `O(sqrt(tau(D_n)))` balanced heap size | `proofs/MEET_IN_THE_MIDDLE_CONNECTED_PREFIX_STREAM.md` |
| N1-STR-024 | proved theorem | Layer-normalized count surplus meets the count gate exactly when `Gamma_n>=1` | `proofs/NORMALIZED_CONNECTED_PREFIX_SURPLUS.md` |
| N1-STR-025 | proved theorem | Exact carrier growth factors into count surplus and packing utilization | `proofs/EFFECTIVE_CARRIER_FACTORIZATION_RECONSTRUCTION.md` |

## Conditional theorems

| ID | Result label | Statement | Open dependency |
|---|---|---|---|
| N1-RED-005 | conditional theorem | Quotient rainbow occupancy implies `H_{n!}(floor(sqrt(n!))+1)=O((log n)^2)` | Global quotient occupancy |
| HIST-001 | conditional theorem | Half-range theorem implies `h(n!)=O((log n)^3)` | Track B reconstruction |

## Finite certificates and computational evidence

| ID | Result label | Scope | Location |
|---|---|---|---|
| N1-CMP-003 | computational evidence | Reduced quotient checks for `7<=n<=14` | `verification/MARKER_THREE_FINITE_REPORT.md` |
| N1-CMP-004 | finite certificate | 3-density, endpoint crossing, and contraction checks | `verification/ENDPOINT_SUPPORT_FINITE_REPORT.md` |
| N1-CMP-005 | finite certificate | Factorial blocks, one-block ceiling, and carry collisions | `verification/BLOCK_COLLISION_FINITE_REPORT.md` |
| N1-CMP-006 | computational evidence | Non-monotone normalized surplus at `n=51,52,53` | `verification/connected_prefix_normalized_n51_n53.csv` |
| N1-CMP-007 | computational evidence | Non-monotone normalized surplus through `n=54` and first-blocking-gap ratio below `1.108` on twenty blocked layers | `verification/connected_prefix_normalized_n51_n54.csv` |
| N1-CMP-008 | computational evidence | Effective count, utilization, and endpoint factors through `n=55`; first-blocking-gap ratio remains below `1.108` on twenty-five blocked layers | `verification/effective_carrier_n51_n55.csv` |
| N1-FIN-005 | finite certificate | Exact carrier coverage for `46<=n<=50` | `verification/FULL_CORE_N46_N50_REPORT.md` |
| N1-FIN-006 | finite certificate | Exact streaming certificate at `n=51` | `verification/FULL_CORE_N51_REPORT.md` |
| N1-FIN-007 | finite certificate | Exact meet-in-the-middle certificate at `n=52` | `verification/FULL_CORE_N52_REPORT.md` |
| N1-FIN-008 | finite certificate | Exact dual-partition meet-in-the-middle certificate at `n=53` | `verification/FULL_CORE_N53_REPORT.md` |
| N1-FIN-009 | finite certificate | Exact dual-partition runtime-aware meet-in-the-middle certificate at `n=54` | `verification/FULL_CORE_N54_REPORT.md` |
| N1-FIN-010 | finite certificate | Exact dual-partition effective-carrier certificate at `n=55` | `verification/FULL_CORE_N55_REPORT.md` |
| N2-FIN-202 | finite certificate | Imported carrier coverage for `12<=n<=45` | Nova 2 commit `82603c631a106c3bff4676bdeeb9cc791fc98f3c` |

The sharper finite conclusions are

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le22
\qquad(12\le n\le54),
\]

and

\[
H_{55!}(\lfloor\sqrt{55!}\rfloor+1)\le23.
\]

Consequently,

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le23
\qquad(12\le n\le55).
\]

These are finite theorems only.

## Disproved routes

| ID | Result label | Route eliminated |
|---|---|---|
| N1-DIS-001 | disproved route | Independent prime-power atoms |
| N1-DIS-002 | disproved route | Fixed binary or ternary pools |
| N1-DIS-003 | disproved route | Polynomial-size menus with polynomial correction |
| N1-DIS-004 | disproved route | Complement pairing alone implies density |
| N1-DIS-005 | disproved route | Original addresses `e_t=r_n+t` |
| N1-DIS-006 | disproved route | One factorial block per carrier layer reaches the endpoint |

## Exact open blockers

1. Prove a uniform lower bound on the effective product `widetilde Gamma_n * B_n`, or an upper bound that retires the sequential engine.
2. Prove or disprove a uniform divisor record-gap or average-gap bound strong enough to control utilization.
3. Extend exact finite certification beginning at `n=56`.
4. Prove or disprove the full quotient downward-window theorem.
5. Prove downward endpoint-window occupancy.
6. Upper-bound target-local collision multiplicity or additive energy.
7. Prove compact numerical tilt or quantitative phase dispersion.
8. Prove the strict weighted bounded-torus Fourier inequality.
9. Reconstruct Track B.
10. Handle finite exceptions after an effective asymptotic threshold exists.

## Verification

```text
python tracks/nova1-factorial-structure/verification/structural_sanity.py
python tracks/nova1-factorial-structure/verification/marker_three_sanity.py
python tracks/nova1-factorial-structure/verification/endpoint_support_sanity.py
python tracks/nova1-factorial-structure/verification/block_collision_sanity.py
python tracks/nova1-factorial-structure/verification/test_mitm_overlap.py
python tracks/nova1-factorial-structure/verification/test_mitm_n53_normalized.py
python tracks/nova1-factorial-structure/verification/test_mitm_n54_partition.py
python tracks/nova1-factorial-structure/verification/test_mitm_n55_effective.py
python tracks/nova1-factorial-structure/verification/plan_mitm_partition.py 55 --max-columns 3000000 --limit 10

g++ -O3 -std=c++20 \
  tracks/nova1-factorial-structure/verification/marker_three_mitm_prefix_u128.cpp \
  -o marker_three_mitm_prefix_u128

./marker_three_mitm_prefix_u128 55 9
./marker_three_mitm_prefix_u128 55 808
```

## Next theorem target

Prove or refute a uniform lower bound on the exact utilization product, preferably through a divisor average-gap or record-gap theorem that closes `N1-STR-025`. In parallel, extend the runtime-aware meet-in-the-middle audit from `n=56`.
