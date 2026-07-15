# Nova 1 Construction Registry

## N1-CON-001: Full-menu valuation-tagged address packets

Result label: **heuristic** as a complete half-range route.

Rank: preferred.

Path: `constructions/VALUATION_TAGGED_ADDRESS_PACKETS.md`

### Definition

Use

\[
M_n=\lceil16(\log n)^2\rceil
\]

labeled layers with distinct 2-adic addresses. Each layer contains all admissible odd divisor cores of `n!` below the address-dependent half-range cutoff. Select at most one term per layer.

### Proved components

- factorial-specific address budget;
- divisor legality;
- cross-layer numerical distinctness;
- disjoint binary correction palette;
- exact `M_n+r_n` selected-term cost;
- high-prime lower bound on menu sizes;
- necessary profile-capacity gate.

### Open component

Uniform downward-window occupancy of the global rainbow sumset.

### Primary risks

- collision concentration;
- inaccessible residues;
- additive shell gaps;
- a proof that secretly becomes sequential.

## N1-CON-002: Marked complement-pair menu clouds

Result label: **heuristic** as a complete half-range route.

Rank: secondary.

Path: `constructions/MARKED_COMPLEMENT_PAIR_CLOUDS.md`

### Definition

Use `O((log n)^2)` square-center slots with distinct 2-adic center tags. Each slot carries a large menu of reciprocal divisor pairs

\[
R_s/z,
\qquad
R_sz.
\]

Select zero or one term per slot globally.

### Proved components

- divisor legality;
- low/high and cross-slot numerical distinctness;
- palette disjointness through a fixed factor of `5`;
- exact polylogarithmic selected-term cost;
- globally nonsequential selection rule;
- necessary menu-capacity gate.

### Open components

- analytic construction of large center and multiplier menus across required scales;
- uniform downward-window occupancy.

### Primary risks

- insufficient menu entropy;
- correlated switch increments;
- residue obstructions;
- shell gaps;
- reintroduction of a sequential decoder.

## Retired construction: fixed addressed divisor pool

Result label: **disproved route**.

A single frozen divisor in each of `O((log n)^2)` addresses gives only `exp(O((log n)^2))` profiles, far below the factorial half-range entropy.

Proof: `proofs/COUNTING_CAPACITY_OBSTRUCTION.md`.

## Retired construction: fixed complement-pair pool

Result label: **disproved route**.

One frozen ternary pair state in each of `O((log n)^2)` slots has the same fatal capacity deficit.

Proof: `proofs/COUNTING_CAPACITY_OBSTRUCTION.md`.

## Retired construction: polynomial menus

Result label: **disproved route**.

Polynomially many choices per layer supply only `O((log n)^3)` total profile entropy. The required entropy is `Theta(n log n)`.

Proof: `proofs/MENU_ENTROPY_REQUIREMENT.md`.

## Retired shortcut: independent prime-power atoms

Result label: **disproved route**.

Prime powers of the same prime consume one shared valuation coordinate and cannot be counted as independent binary atoms.

## Construction acceptance checklist

Every future revision must include:

1. exact divisor formulas;
2. exact valuation legality;
3. number of available choices;
4. maximum number of selected terms;
5. numerical distinctness across all selected layers and palettes;
6. necessary profile-capacity audit;
7. collision-loss and residue audit;
8. correction mechanism and term cost;
9. sequential-obstruction audit;
10. exact missing additive and analytic statements;
11. finite test plan;
12. asymptotic failure condition.