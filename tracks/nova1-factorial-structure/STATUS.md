# Nova 1 Status

## Track

Factorial Structure and Reduction

## Branch

`nova/factorial-structure`

## Overall state

`LATTICE_REPAIR_CHECKPOINT_READY_FOR_AUDIT`

The factorial half-range theorem remains open.

## Current objective

Prove or disprove quotient downward-window occupancy for the repaired marker-three valuation rainbow construction `N1-CON-003`.

## Imported cross-track results

### Nova 2 obstruction

The first preferred route was rejected at:

- branch: `nova/additive-occupancy`
- exact commit: `45c74a5fa747551422ffcad7d3ddf22788fbe622`
- theorem: `N2-ADD-115`
- disproved model: `N2-OBS-107`

Every old main sum was divisible by `2^(r_n+1)`, while the old correction radius was `2^r_n-1`.

### Nova 3 prime interval theorem

The explicit prime interval input was accepted from:

- branch: `nova/analytic-density`
- exact commit: `e60069f797af878711e7a9d4abb1fb6188a1f724`
- theorems: `N3-ANA-010`, `N3-ANA-011`

For every `n>=120368`,

\[
\pi(n)-\pi(n/2)\ge\frac{n}{3\log n}.
\]

Nova 1 separately translated this theorem to the repaired marker-three menus.

## Proved results

| ID | Result label | Statement | Location |
|---|---|---|---|
| N1-STR-003 | proved theorem | Legendre valuation budgets, quotient bands, dyadic bands, and factorial 2-adic multiplicity | `proofs/VALUATION_BUDGET_LEMMAS.md` |
| N1-STR-004 | proved theorem | Independent valuation boxes produce unique legal divisors | `FACTORIAL_DIVISOR_ATLAS.md` |
| N1-STR-005 | proved theorem | Allocated valuation budgets preserve divisor legality | `FACTORIAL_DIVISOR_ATLAS.md` |
| N1-STR-006 | proved theorem | Marker signatures enforce numerical distinctness | `proofs/DISTINCTNESS_AND_CORRECTION.md` |
| N1-STR-007 | proved theorem | Complement pairing preserves legality, range, and distinctness | `proofs/COMPLEMENT_PAIRING_LEMMA.md` |
| N1-COR-001 | proved theorem | Binary powers form a disjoint correction palette | `proofs/DISTINCTNESS_AND_CORRECTION.md` |
| N1-RED-002 | proved theorem | Downward-window occupancy plus binary correction gives exact coverage | `proofs/DISTINCTNESS_AND_CORRECTION.md` |
| N1-OBS-002 | proved theorem | Downward-window counting capacity inequality | `proofs/COUNTING_CAPACITY_OBSTRUCTION.md` |
| N1-STR-008 | proved theorem | `O((log n)^2)` layers require geometric-mean menu size `exp(Omega(n/log n))` | `proofs/MENU_ENTROPY_REQUIREMENT.md` |
| N1-STR-009 | proved theorem | High-prime subset products supply exponentially many cores per admissible layer | `proofs/HIGH_PRIME_MENU_CAPACITY.md` |
| N1-STR-014 | proved theorem | Marker-three layers are legal and numerically distinct from each other and the palette | `proofs/MARKER_THREE_LATTICE_REPAIR.md` |
| N1-STR-015 | proved theorem | Exact main support lattice is `3Z`, and the palette attains all residues modulo `3` | `proofs/MARKER_THREE_LATTICE_REPAIR.md` |
| N1-RED-004 | proved theorem | Quotient `W_n`-window occupancy implies exact factorial half-range coverage | `proofs/MARKER_THREE_LATTICE_REPAIR.md` |
| N1-STR-016 | proved theorem | Odd positional digits have maximum downward gap one | `proofs/MARKER_THREE_LATTICE_REPAIR.md` |
| N1-STR-017 | proved theorem | Repaired construction covers an unconditional `exp(O((log n)^2))` initial interval | `proofs/MARKER_THREE_LATTICE_REPAIR.md` |
| N1-STR-018 | proved theorem | Every repaired layer has at least `2^(pi(n)-pi(n/2)-1)` legal high-prime cores for `n>=120368` | `proofs/MARKER_THREE_MENU_CAPACITY.md` |
| N1-CAP-002 | proved theorem | Repaired menus pass the necessary profile-capacity gate for every `n>=120368` | `proofs/MARKER_THREE_MENU_CAPACITY.md` |

## Conditional results

| ID | Result label | Statement | Open dependency |
|---|---|---|---|
| N1-RED-005 | conditional theorem | Frozen quotient rainbow occupancy implies `H_{n!}(floor(sqrt(n!))+1)=O((log n)^2)` | Nova 2 quotient occupancy theorem |
| HIST-001 | conditional theorem | Half-range theorem implies `h(n!)=O((log n)^3)` | Current-notation Track B reconstruction |

## Computational evidence

| Object | Result label | Scope | Location |
|---|---|---|---|
| N1-CMP-003 | computational evidence | Exact reduced marker-three quotient checks for every `7<=n<=14` | `verification/MARKER_THREE_FINITE_REPORT.md` |

The tested quotient maximum downward distance is at most one. The result is finite evidence only.

## Disproved routes

| ID | Result label | Route eliminated | Proof |
|---|---|---|---|
| N1-DIS-001 | disproved route | Treating prime powers of one prime as independent coordinates | `FACTORIAL_DIVISOR_ATLAS.md` |
| N1-DIS-002 | disproved route | A fixed pool of `O((log n)^2)` binary or ternary divisor choices | `proofs/COUNTING_CAPACITY_OBSTRUCTION.md` |
| N1-DIS-003 | disproved route | Polynomial-size menus in `O((log n)^2)` layers with polynomial correction | `proofs/MENU_ENTROPY_REQUIREMENT.md` |
| N1-DIS-004 | disproved route | Complement pairing alone implies additive density | `proofs/COMPLEMENT_PAIRING_LEMMA.md` |
| N1-DIS-005 | disproved route | Old valuation tags `e_t=r_n+t` with radius `2^r_n-1` | Nova 2 `N2-ADD-115` at commit `45c74a5fa747551422ffcad7d3ddf22788fbe622` |

## Candidate ranking

1. `N1-CON-003`: marker-three valuation rainbow, preferred repaired route.
2. `N1-CON-002`: marked complement-pair menu clouds, secondary globally nonsequential route.
3. `N1-CON-001`: disproved and superseded.

## Exact open blockers

1. Prove or disprove the revised Nova 2 quotient occupancy handoff `N1-HO-N2-002`.
2. Prove endpoint support and maximum-gap control near `floor(X_n/3)`.
3. Quantify collision loss in the quotient menus.
4. Freeze the exact target-dependent numerical-value law before requesting analytic estimates.
5. Reconstruct the direct factorial Track B conversion under the frozen endpoint convention.
6. Handle finite exceptions only after an effective asymptotic threshold exists.

## Handoffs

- Nova 2: `handoffs/TO_NOVA2.md`, revised as `N1-HO-N2-002`.
- Nova 3: `handoffs/TO_NOVA3.md`, original prime interval request accepted; additive request paused until Nova 2 accepts the revised structure.
- Nova 4: `handoffs/TO_NOVA4.md`, requires a marker-three lattice and reduced-rainbow regression update.

## Verification

Run:

```text
python tracks/nova1-factorial-structure/verification/structural_sanity.py
python tracks/nova1-factorial-structure/verification/marker_three_sanity.py
```

The marker-three verifier passes all three exact check groups and exhaustively covers the reduced quotient domains for `7<=n<=14`.

## Next theorem target

Prove or disprove that, for the frozen quotient layers in `PREFERRED_ROUTE.md`, every integer

\[
W_n+1\le q\le\left\lfloor X_n/3\right\rfloor
\]

has a quotient rainbow sum in

\[
[q-W_n,q].
\]
