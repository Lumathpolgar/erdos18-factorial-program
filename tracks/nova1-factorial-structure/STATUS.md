# Nova 1 Status

## Track and branch

- Track: Factorial Structure and Reduction
- Branch: `nova/factorial-structure`
- Overall state: `OVERFLOW_SAFE_FULL_CORE_CERTIFIED_THROUGH_N57_FACTORIAL_SPAN_OPEN`

The factorial half-range theorem and Erdos Problem 18 remain open.

## Current objective

Prove or disprove quotient downward-window occupancy for `N1-CON-003`, the marker-three valuation rainbow.

The exact sequential frontier is factorial-specific internal span or normalized average-gap control. Connected-prefix count, parity, and the first external blocking gap are insufficient as complete proof inputs.

## Imported cross-track results

### Nova 2 original obstruction

- branch: `nova/additive-occupancy`
- exact commit: `45c74a5fa747551422ffcad7d3ddf22788fbe622`
- theorem: `N2-ADD-115`
- disproved model: `N2-OBS-107`

The original valuation-tagged route remains a **disproved route**.

### Nova 2 marker-three carrier package

- branch: `nova/additive-occupancy`
- effective-factor source commit: `2ab09dd980f7116b82530368e3d98bb53240bf0c`
- parity-span source commit: `47ed3938d8900c82b245a3592502ac957330bbc6`
- results: `N2-ADD-119`, `N2-ADD-120`, `N2-ADD-121`, `N2-ADD-122`, `N2-ADD-124`, `N2-OBS-110`

Nova 2 accepts the carrier engine as a sufficient sequential method with restrictions. Count surplus alone is not sufficient, and parity-span information is optimal without factorial-specific spacing.

### Nova 3 inputs

- branch: `nova/analytic-density`
- prime-interval source commit: `e60069f797af878711e7a9d4abb1fb6188a1f724`
- results: `N3-ANA-010`, `N3-ANA-011`
- numerical-law head inspected: `003b9c0e1179314d6c119c8a356e0f41231e3ad6`
- numerical results: `N3-ANA-017`, `N3-ANA-018`, `N3-ANA-019`
- outcome: `ACCEPTED_WITH_RESTRICTIONS`

A target-independent minor-arc gap over all tilts remains a **disproved route**.

## Proved theorems

| ID | Result label | Statement | Location |
|---|---|---|---|
| N1-STR-003 | proved theorem | Exact Legendre budgets, quotient bands, dyadic bands, and 2-adic multiplicity | `proofs/VALUATION_BUDGET_LEMMAS.md` |
| N1-STR-004 | proved theorem | Valuation boxes produce unique legal divisors | `FACTORIAL_DIVISOR_ATLAS.md` |
| N1-STR-005 | proved theorem | Allocated valuation budgets preserve legality | `FACTORIAL_DIVISOR_ATLAS.md` |
| N1-STR-006 | proved theorem | Marker signatures enforce numerical distinctness | `proofs/DISTINCTNESS_AND_CORRECTION.md` |
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
| N1-STR-023 | proved theorem | Meet-in-the-middle product streams recover exact divisor order | `proofs/MEET_IN_THE_MIDDLE_CONNECTED_PREFIX_STREAM.md` |
| N1-STR-024 | proved theorem | Layer-normalized count surplus meets the count gate exactly when `Gamma_n>=1` | `proofs/NORMALIZED_CONNECTED_PREFIX_SURPLUS.md` |
| N1-STR-025 | proved theorem | Exact carrier growth factors into count surplus and packing utilization | `proofs/EFFECTIVE_CARRIER_FACTORIZATION_RECONSTRUCTION.md` |
| N1-STR-026 | proved theorem | Every positive odd-core prefix satisfies `U_t>=2K_t-1` | `proofs/PARITY_SPAN_CRITERION_RECONSTRUCTION.md` |
| N1-OBS-004 | proved theorem | The parity-span lower bound is optimal from oddness, count, and threshold alone | `proofs/PARITY_SPAN_CRITERION_RECONSTRUCTION.md` |
| N1-STR-027 | proved theorem | Overflow-safe truncation and exact checkpoint continuation preserve the required product stream | `proofs/OVERFLOW_SAFE_CHECKPOINTED_MITM_STREAM.md` |

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
| N1-CMP-006 | computational evidence | Non-monotone count surplus at `n=51,52,53` | `verification/connected_prefix_normalized_n51_n53.csv` |
| N1-CMP-007 | computational evidence | Non-monotone count surplus through `n=54` | `verification/connected_prefix_normalized_n51_n54.csv` |
| N1-CMP-008 | computational evidence | Effective count and utilization factors through `n=55` | `verification/effective_carrier_n51_n55.csv` |
| N1-CMP-009 | computational evidence | Parity and factorial-span diagnostics through `n=56` | `verification/parity_span_effective_n51_n56.csv` |
| N1-CMP-010 | computational evidence | Effective, span, and blocking-gap diagnostics through `n=57` | `verification/effective_carrier_n51_n57.csv` |
| N1-FIN-005 | finite certificate | Exact carrier coverage for `46<=n<=50` | `verification/FULL_CORE_N46_N50_REPORT.md` |
| N1-FIN-006 | finite certificate | Exact streaming certificate at `n=51` | `verification/FULL_CORE_N51_REPORT.md` |
| N1-FIN-007 | finite certificate | Exact meet-in-the-middle certificate at `n=52` | `verification/FULL_CORE_N52_REPORT.md` |
| N1-FIN-008 | finite certificate | Exact dual-partition certificate at `n=53` | `verification/FULL_CORE_N53_REPORT.md` |
| N1-FIN-009 | finite certificate | Exact runtime-aware certificate at `n=54` | `verification/FULL_CORE_N54_REPORT.md` |
| N1-FIN-010 | finite certificate | Exact effective-carrier certificate at `n=55` | `verification/FULL_CORE_N55_REPORT.md` |
| N1-FIN-011 | finite certificate | Exact seven-layer certificate at `n=56` | `verification/FULL_CORE_N56_REPORT.md` |
| N1-FIN-012 | finite certificate | Exact overflow-safe dual-partition certificate at `n=57` | `verification/FULL_CORE_N57_REPORT.md` |
| N2-FIN-202 | finite certificate | Imported carrier coverage for `12<=n<=45` | Nova 2 commit `82603c631a106c3bff4676bdeeb9cc791fc98f3c` |

## Exact finite boundary

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le22
\qquad(12\le n\le54),
\]

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le23
\qquad(12\le n\le55),
\]

and

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le24
\qquad(12\le n\le57).
\]

These are finite theorems only.

At `n=57`, six layers reach only

\[
F_6/(Y_{57}+1)=0.0873914320600893\ldots,
\]

while seven layers give

\[
F_7/(Y_{57}+1)=1.0873914095218273\ldots.
\]

## Verification correction

The unrestricted unsigned-128 half-list verifier is a **disproved route**. At `n=57`, masks `6` and `424` produced different connected-prefix counts. The authoritative verifier uses endpoint truncation, division-based overflow guards, cached half-lists, and exact deterministic checkpoints.

Overflow-safe replays reproduce every accepted mathematical output at `n=52,53,54,55,56`.

## Disproved routes

| ID | Result label | Route eliminated |
|---|---|---|
| N1-DIS-001 | disproved route | Independent prime-power atoms |
| N1-DIS-002 | disproved route | Fixed binary or ternary pools |
| N1-DIS-003 | disproved route | Polynomial-size menus with polynomial correction |
| N1-DIS-004 | disproved route | Complement pairing alone implies density |
| N1-DIS-005 | disproved route | Original addresses `e_t=r_n+t` |
| N1-DIS-006 | disproved route | One factorial block per carrier layer reaches the endpoint |
| N1-DIS-007 | disproved route | Unguarded unsigned-128 half-list enumeration is an exact verifier |
| N1-DIS-008 | disproved route | The finite candidate bound `g_t/D_t<1.108` |

The exact `n=57`, layer `3` counterexample is

\[
g_3/D_3=1.1674772300983786\ldots.
\]

## Exact open blockers

1. Prove a factorial-specific lower bound for `A_t=U_t/(2K_t-1)` or `eta_t=U_t/(K_tD_t)`, or an upper obstruction retiring the sequential engine.
2. Extend exact overflow-safe certification beginning at `n=58`.
3. Prove or disprove the full quotient downward-window theorem.
4. Prove downward endpoint-window occupancy.
5. Upper-bound target-local collision multiplicity or additive energy.
6. Prove compact numerical tilt or quantitative phase dispersion.
7. Prove the strict weighted bounded-torus Fourier inequality.
8. Reconstruct Track B.
9. Handle finite exceptions after an effective asymptotic threshold exists.

## Verification

```text
g++ -O3 -std=c++20 \
  tracks/nova1-factorial-structure/verification/marker_three_mitm_checkpoint_u128.cpp \
  -o marker_three_mitm_checkpoint_u128

./marker_three_mitm_checkpoint_u128 57 6 100000000
./marker_three_mitm_checkpoint_u128 57 424 100000000
python tracks/nova1-factorial-structure/verification/test_mitm_n57_overflow_safe.py
```

## Next theorem target

Prove or refute a factorial-specific lower bound for internal span or normalized average gaps. In parallel, extend the authoritative overflow-safe dual-partition certificate from `n=58`.
