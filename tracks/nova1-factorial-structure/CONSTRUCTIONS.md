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
 u\text{ odd},
 3u\mid n!,
 3\cdot2^{t-1}u\le X_n\}.
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
- necessary formal profile capacity for every `n>=120368`;
- multiplicative 3-density of the reserved odd factorial core;
- total quotient support crossing `floor(X_n/3)` with three distinct terms;
- globally nonsequential final occupancy request.

### Exact endpoint result

For every `n>=12`, the first three quotient layers contain terms

\[
X_n/9<b_t\le X_n/3
\]

with exact 2-adic valuations `0`, `1`, and `2`. Their sum is greater than `X_n/3`. Therefore the final quotient target is inside the total support.

This does not prove a sum in the final downward window.

### Open component

Uniform downward-window occupancy of the quotient rainbow sumset with radius

\[
W_n=\left\lfloor\frac{2^{r_n}-3}{3}\right\rfloor
\]

through `floor(X_n/3)`.

### Primary risks

- downward endpoint-window deficit despite total support crossing the endpoint;
- collision concentration;
- quotient additive shell gaps;
- an unrecognized bounded-torus resonance;
- a proof that secretly becomes sequential.

### Finite evidence

- reduced-parameter quotient checks for every `7<=n<=14` find maximum downward distance at most one;
- multiplicative 3-density is checked for every `6<=n<=20`;
- endpoint crossing is checked for every `12<=n<=20`;
- coarse contraction is exhaustively checked for all quotient targets with `12<=n<=14` and `1<=L<=6`.

Paths:

- `verification/marker_three_sanity.py`
- `verification/MARKER_THREE_FINITE_REPORT.md`
- `verification/endpoint_support_sanity.py`
- `verification/ENDPOINT_SUPPORT_FINITE_REPORT.md`

Result labels: **computational evidence** and **finite certificate**.

## N1-CON-002: Marked complement-pair menu clouds

Result label: **heuristic** as a complete half-range route.

Rank: secondary.

Path: `constructions/MARKED_COMPLEMENT_PAIR_CLOUDS.md`

### Definition

Use `O((log n)^2)` square-center slots with distinct 2-adic center tags. Each slot carries a large menu of reciprocal pairs

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

- analytic construction of large center and multiplier menus;
- uniform downward-window occupancy;
- exact lattice-first audit at the level required by Nova 2.

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

Every main sum was divisible by `2^(r_n+1)`, while the correction radius was only `2^r_n-1`. Nova 2 proved the first requested target window contains no main sum.

Exact imported result:

- branch: `nova/additive-occupancy`
- commit: `45c74a5fa747551422ffcad7d3ddf22788fbe622`
- theorem: `N2-ADD-115`
- disproved model: `N2-OBS-107`

The file remains as a permanent failed-route record.

## Other retired constructions

### Fixed addressed divisor pool

Result label: **disproved route**.

A single divisor in each of `O((log n)^2)` addresses supplies only `exp(O((log n)^2))` profiles.

### Fixed complement-pair pool

Result label: **disproved route**.

One ternary pair state in each of `O((log n)^2)` slots has the same fatal capacity deficit.

### Polynomial menus

Result label: **disproved route**.

Polynomial choices per layer supply only `O((log n)^3)` profile entropy, below the required `Theta(n log n)`.

### Independent prime-power atoms

Result label: **disproved route**.

Powers of one prime share one valuation coordinate and are not independent binary atoms.

## Construction acceptance checklist

Every future revision must include:

1. exact divisor formulas;
2. exact valuation legality;
3. exact common support lattice;
4. exact attained residue classes;
5. correction radius compared with every residue gap;
6. direct first-target coverage;
7. total endpoint-support audit;
8. downward endpoint-window audit;
9. number of available choices;
10. maximum selected-term count;
11. numerical distinctness across layers and palettes;
12. necessary profile-capacity audit;
13. collision-loss audit;
14. sequential-obstruction audit;
15. exact missing additive and analytic statements;
16. finite test plan;
17. asymptotic failure condition.