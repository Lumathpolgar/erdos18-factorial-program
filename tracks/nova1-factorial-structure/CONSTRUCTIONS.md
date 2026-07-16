# Nova 1 Construction Registry

## N1-CON-003: Marker-three valuation rainbow

Result label: **conditional theorem** as the current open half-range route.

Rank: preferred.

Path: `constructions/MARKER_THREE_VALUATION_RAINBOW.md`.

### Definition

Let

\[
X_n=\lfloor\sqrt{n!}\rfloor,
\qquad
r_n=\lceil4\log n\rceil,
\qquad
M_n=\lceil16(\log n)^2\rceil,
\]

\[
W_n=\left\lfloor\frac{2^{r_n}-3}{3}\right\rfloor.
\]

For `1<=t<=M_n`, define

\[
U_t(n)=
\{u\ge1:u\text{ odd},\ 3u\mid n!,\ 3\cdot2^{t-1}u\le X_n\},
\]

\[
A_t^{(3)}(n)=\{3\cdot2^{t-1}u:u\in U_t(n)\},
\qquad
B_t(n)=\{2^{t-1}u:u\in U_t(n)\}.
\]

Select at most one main term from each layer. Use the correction palette

\[
C_n=\{1,2,4,\ldots,2^{r_n-1}\}.
\]

### Proved structural components

- factorial-specific `Theta((log n)^2)` layer budget;
- divisor legality;
- exact 2-adic layer separation;
- main-palette numerical disjointness;
- exact main support lattice `3Z`;
- all correction residues modulo `3`;
- exact quotient-window correction theorem;
- exact `M_n+r_n` selected-term cost;
- unconditional `exp(O((log n)^2))` initial interval;
- exponential high-prime menu capacity;
- multiplicative 3-density of the reserved odd core;
- total quotient endpoint support;
- exact unique-parent and meet-in-the-middle divisor streams;
- exact layer-normalized entropy surplus identity.

### Finite certificates

The complete connected-core carrier is exactly certified for

\[
12\le n\le53.
\]

In this range,

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le22.
\]

Recent certificates:

| ID | `n` | method | layers | term bound |
|---|---:|---|---:|---:|
| N1-FIN-006 | 51 | unique-parent stream | 6 | 22 |
| N1-FIN-007 | 52 | meet-in-the-middle stream | 6 | 22 |
| N1-FIN-008 | 53 | dual-partition meet-in-the-middle stream | 6 | 22 |

Normalized finite surplus values are

\[
\Gamma_{51}=120.322026489,
\quad
\Gamma_{52}=97.645052132,
\quad
\Gamma_{53}=124.609364763.
\]

The finite sequence is non-monotone. No asymptotic conclusion is drawn.

### Exact open component

Prove or disprove that, for all sufficiently large `n`, every quotient target

\[
W_n+1\le q\le\left\lfloor\frac{X_n}{3}\right\rfloor
\]

has a rainbow sum in

\[
[q-W_n,q].
\]

### Primary risks

- final downward endpoint-window gaps;
- collision concentration;
- quotient additive shell gaps;
- insufficient normalized connected-prefix entropy;
- failure of compact phase dispersion;
- a proof that silently becomes sequential when claiming a final-only result.

## N1-CON-002: Marked complement-pair menu clouds

Result label: **conditional theorem** as a secondary route.

Rank: secondary.

Path: `constructions/MARKED_COMPLEMENT_PAIR_CLOUDS.md`.

### Proved components

- divisor legality under the stated valuation budgets;
- low/high and cross-slot distinctness;
- fixed-marker palette separation;
- polylogarithmic selected-term cost;
- necessary menu-capacity gate.

### Open components

- construction of sufficiently large square-center and multiplier menus;
- exact lattice-first audit;
- uniform downward-window occupancy;
- collision and shell-gap control.

## N1-CON-001: Original valuation-tagged addresses

Result label: **disproved route**.

Path: `constructions/VALUATION_TAGGED_ADDRESS_PACKETS.md`.

The original addresses were

\[
e_t=r_n+t.
\]

Every main sum was divisible by `2^(r_n+1)`, while the correction radius was only `2^r_n-1`. Nova 2 theorem `N2-ADD-115` disproved this frozen route at exact commit

`45c74a5fa747551422ffcad7d3ddf22788fbe622`.

The construction remains only as a permanent failed-route record.

## Other disproved routes

| Result label | Route |
|---|---|
| disproved route | Fixed addressed divisor pool |
| disproved route | Fixed complement-pair pool |
| disproved route | Polynomial-size menus |
| disproved route | Independent prime-power atoms |
| disproved route | One factorial arithmetic block per carrier layer |

## Construction acceptance checklist

Every future revision must include:

1. exact divisor formulas;
2. exact valuation legality;
3. exact common support lattice;
4. attained residue classes;
5. correction radius versus residue gaps;
6. direct first-target coverage;
7. total endpoint-support audit;
8. downward endpoint-window audit;
9. available choice counts;
10. selected-term count;
11. numerical distinctness;
12. necessary profile-capacity audit;
13. collision-loss audit;
14. sequential-obstruction audit;
15. exact missing additive and analytic statements;
16. finite test plan;
17. asymptotic failure condition;
18. exact result labels;
19. replayable certificates with fail-closed resource boundaries.
