# Nova 1 Status

## Track

Factorial Structure and Reduction

## Branch

`nova/factorial-structure`

## Overall state

`FIRST_STRUCTURAL_CHECKPOINT_READY_FOR_AUDIT`

The factorial half-range theorem remains open.

## Current objective

Prove or disprove uniform downward-window occupancy for the frozen full-menu valuation-tagged rainbow construction.

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
| N1-STR-009 | proved theorem | High-prime subset products supply at least `2^(pi(n)-pi(n/2)-1)-1` cores per admissible address | `proofs/HIGH_PRIME_MENU_CAPACITY.md` |

## Conditional results

| ID | Result label | Statement | Open dependency |
|---|---|---|---|
| N1-RED-003 | conditional theorem | Frozen rainbow downward occupancy implies `H_{n!}(floor(sqrt(n!))+1)=O((log n)^2)` | Nova 2 occupancy theorem |
| N1-CAP-001 | conditional theorem | Frozen menus pass the necessary capacity gate | Explicit prime-interval lower bound from Nova 3 |
| HIST-001 | conditional theorem | Half-range theorem implies `h(n!)=O((log n)^3)` | Current-notation Track B reconstruction |

## Disproved routes

| ID | Result label | Route eliminated | Proof |
|---|---|---|---|
| N1-DIS-001 | disproved route | Treating prime powers of one prime as independent coordinates | `FACTORIAL_DIVISOR_ATLAS.md` |
| N1-DIS-002 | disproved route | A fixed pool of `O((log n)^2)` binary or ternary divisor choices | `proofs/COUNTING_CAPACITY_OBSTRUCTION.md` |
| N1-DIS-003 | disproved route | Polynomial-size menus in `O((log n)^2)` layers with polynomial correction | `proofs/MENU_ENTROPY_REQUIREMENT.md` |
| N1-DIS-004 | disproved route | Complement pairing alone implies additive density | `proofs/COMPLEMENT_PAIRING_LEMMA.md` |

## Candidate ranking

1. `N1-CON-001`: full-menu valuation-tagged address packets, preferred.
2. `N1-CON-002`: marked complement-pair menu clouds, secondary globally nonsequential route.

The fixed-family predecessors are retired.

## Exact open blockers

1. Prove or disprove the Nova 2 rainbow occupancy handoff.
2. Audit an effective lower bound for `pi(n)-pi(n/2)` and the resulting capacity threshold.
3. Test residue classes and collision loss in the frozen menus.
4. Reconstruct the direct factorial Track B conversion under the frozen endpoint convention.
5. Handle finite exceptions only after an asymptotic theorem is available.

## Handoffs

- Nova 2: `handoffs/TO_NOVA2.md`
- Nova 3: `handoffs/TO_NOVA3.md`
- Nova 4: `handoffs/TO_NOVA4.md`

## Verification

Nova 4 has an exact finite capacity and reduced-rainbow falsification request. No finite computation is treated as an asymptotic proof.

## Next theorem target

Prove or disprove that, for the frozen layers in `PREFERRED_ROUTE.md`, every integer

\[
2^{r_n}\le x\le X_n
\]

has a rainbow sum in

\[
[x-(2^{r_n}-1),x].
\]