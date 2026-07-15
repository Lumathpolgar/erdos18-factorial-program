# Nova 1 Construction Registry

## N1-CON-003: Marker-three valuation rainbow

Result label: **heuristic** as a complete half-range route.

Rank: preferred.

Path: `constructions/MARKER_THREE_VALUATION_RAINBOW.md`

### Definition

Use

\[
M_n=\lceil16(\log n)^2\rceil
\]

full-menu layers

\[
A_t^{(3)}(n)=
\{3\cdot2^{t-1}u:
 u\text{ odd},\ 3u\mid n!,\ 3\cdot2^{t-1}u\le X_n\}.
\]

Select at most one main term per layer. Use the binary palette

\[
\{1,2,4,\ldots,2^{r_n-1}\},
\qquad
r_n=\lceil4\log n\rceil.
\]

### Proved components

- factorial-specific `Theta((log n)^2)` address budget;
- divisor legality;
- cross-layer numerical distinctness;
- main-palette disjointness through the fixed marker `3`;
- exact main support lattice `3Z`;
- all residues modulo `3` supplied by the palette;
- exact quotient-window correction reduction;
- exact `M_n+r_n` selected-term cost;
- odd-digit one-gap theorem;
- unconditional initial interval of size `exp(O((log n)^2))`;
- high-prime menu-capacity lower bound;
- globally nonsequential final selection rule.

### Open component

Uniform downward-window occupancy of the quotient rainbow sumset with radius

\[
W_n=\left\lfloor\frac{2^{r_n}-3}{3}\right\rfloor
\]

through `floor(X_n/3)`.

### Primary risks

- endpoint support deficit;
- collision concentration;
- quotient additive shell gaps;
- an unrecognized bounded-torus resonance;
- a proof that secretly becomes sequential.

### Finite evidence

Exact reduced-parameter checks for every `7<=n<=14` find quotient maximum downward distance at most one.

Paths:

- `verification/marker_three_sanity.py`
- `verification/MARKER_THREE_FINITE_REPORT.md`

Result label: **computational evidence**.

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
- uniform downward-window occupancy;
- an exact structural lattice audit at the level now required by Nova 2.

### Primary risks

- insufficient menu entropy;
- correlated switch increments;
- residue obstructions;
- shell gaps;
- reintroduction of a sequential decoder.

## N1-CON-001: Original full-menu valuation tags

Result label: **disproved route**.

Path: `constructions/VALUATION_TAGGED_ADDRESS_PACKETS.md`

The frozen addresses were

\[
e_t=r_n+t.
\]

Every main sum was therefore divisible by `2^(r_n+1)`, while the correction radius was only `2^r_n-1`. Nova 2 proved that the first requested target window contains no main sum.

Exact imported result:

- branch: `nova/additive-occupancy`
- commit: `45c74a5fa747551422ffcad7d3ddf22788fbe622`
- theorem: `N2-ADD-115`
- disproved model: `N2-OBS-107`

The file remains as a permanent failed-route record. It must not be used as the active preferred construction.

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
3. exact common support lattice;
4. exact attained residue classes;
5. correction radius compared with every residue gap;
6. direct first-target coverage;
7. endpoint support audit;
8. number of available choices;
9. maximum number of selected terms;
10. numerical distinctness across all selected layers and palettes;
11. necessary profile-capacity audit;
12. collision-loss audit;
13. sequential-obstruction audit;
14. exact missing additive and analytic statements;
15. finite test plan;
16. asymptotic failure condition.
