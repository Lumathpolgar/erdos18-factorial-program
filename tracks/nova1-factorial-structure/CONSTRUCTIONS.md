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
- divisor legality and exact 2-adic layer separation;
- main-palette numerical disjointness;
- exact support lattice `3Z` and all correction residues modulo `3`;
- quotient-window correction theorem and exact selected-term cost;
- unconditional `exp(O((log n)^2))` initial interval;
- exponential high-prime formal menu capacity;
- multiplicative 3-density and total endpoint support;
- exact unique-parent and meet-in-the-middle divisor streams;
- count-surplus normalization;
- exact count-utilization factorization;
- sharp parity-span baseline `U_t>=2K_t-1`;
- optimality of that baseline under oddness, count, and threshold information alone.

### Finite certificates

The complete connected-core carrier is exactly certified through `n=56`.

The sharp finite bounds are

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
\qquad(12\le n\le56).
\]

Recent certificates:

| ID | `n` | method | layers | term bound |
|---|---:|---|---:|---:|
| N1-FIN-006 | 51 | unique-parent stream | 6 | 22 |
| N1-FIN-007 | 52 | meet-in-the-middle stream | 6 | 22 |
| N1-FIN-008 | 53 | dual-partition meet-in-the-middle stream | 6 | 22 |
| N1-FIN-009 | 54 | runtime-aware dual-partition stream | 6 | 22 |
| N1-FIN-010 | 55 | effective-carrier dual-partition stream | 6 | 23 |
| N1-FIN-011 | 56 | parity-span dual-partition stream | 7 | 24 |

At `n=56`, six layers reach only

\[
F_6/(Y_{56}+1)=0.23886288252245\ldots,
\]

and a seventh layer is necessary. This is an exact finite transition, not a resource artifact.

### Effective finite diagnostics

| `n` | layers | count surplus | utilization root | endpoint surplus |
|---:|---:|---:|---:|---:|
| 51 | 6 | 120.322026488584 | 0.008311064676932 | 1.000004144206103 |
| 52 | 6 | 97.645052132052 | 0.010241184816549 | 1.000001025305911 |
| 53 | 6 | 124.609364763243 | 0.008025094814707 | 1.000001967025492 |
| 54 | 6 | 92.273264366777 | 0.010837378971591 | 1.000000334888580 |
| 55 | 6 | 98.919733584849 | 0.010109209300122 | 1.000000290721510 |
| 56 | 7 | 673.791460795324 | 0.001530254006653 | 1.031072082530349 |

The layer-count transition makes raw finite trends non-comparable without the exact normalization. No asymptotic conclusion is drawn.

At `n=56`, the parity-only sufficient product misses the endpoint by approximately `3.82e31`. Factorial-specific internal spacing supplies essentially all missing expansion.

Across the 31 blocked layers for `51<=n<=56`,

\[
\max g_t/D_t<1.108.
\]

This remains **computational evidence** only. A first external blocking gap does not control internal average spacing.

### Exact computational architecture

`N1-STR-023` permits any partition of the odd prime-power coordinates. Runtime depends on both the stored half-list and the active row count.

At `n=56`:

- mask `98`: `168 x 2,995,200`, exact certificate in `23.01` seconds;
- mask `33`: `104 x 4,838,400`, exact certificate in `22.23` seconds.

The two partitions agree on every exact mathematical field after excluding partition and environment metadata.

### Exact open component

Prove or disprove that every sufficiently large quotient target

\[
W_n+1\le q\le\left\lfloor\frac{X_n}{3}\right\rfloor
\]

has a legal rainbow sum in

\[
[q-W_n,q].
\]

For the sequential engine, the next theorem must control factorial-specific internal span

\[
A_t=\frac{U_t}{2K_t-1}
\]

or normalized average gap

\[
\eta_t=\frac{U_t}{K_tD_t}.
\]

Count, parity, and first external blocking gaps are insufficient complete inputs.

### Primary risks

- final downward endpoint-window gaps;
- collision concentration and additive shell gaps;
- insufficient factorial-specific packing utilization;
- failure of a uniform internal average-gap theorem;
- failure of compact phase dispersion;
- a proof that silently becomes sequential when claiming a final-only result.

## N1-CON-002: Marked complement-pair menu clouds

Result label: **conditional theorem** as a secondary route.

Rank: secondary.

Path: `constructions/MARKED_COMPLEMENT_PAIR_CLOUDS.md`.

Proved components are divisor legality, numerical distinctness, palette separation, polylogarithmic selected-term cost, and the necessary menu-capacity gate. Open components are sufficiently large menus, lattice-first compatibility, uniform downward-window occupancy, and collision or shell-gap control.

## N1-CON-001: Original valuation-tagged addresses

Result label: **disproved route**.

Path: `constructions/VALUATION_TAGGED_ADDRESS_PACKETS.md`.

The original addresses `e_t=r_n+t` force every main sum into a lattice too coarse for the correction radius. Nova 2 theorem `N2-ADD-115` disproved the frozen route at exact commit `45c74a5fa747551422ffcad7d3ddf22788fbe622`.

## Other disproved routes

| Result label | Route |
|---|---|
| disproved route | Fixed addressed divisor pool |
| disproved route | Fixed complement-pair pool |
| disproved route | Polynomial-size menus |
| disproved route | Independent prime-power atoms |
| disproved route | One factorial arithmetic block per layer |

## Construction acceptance checklist

Every future revision must include exact divisor formulas, valuation legality, support lattice, residues, correction radius, first-target coverage, endpoint support, downward endpoint windows, menu counts, term count, numerical distinctness, profile capacity, collision loss, sequential obstruction, exact missing theorems, replayable finite tests, failure conditions, result labels, fail-closed resources, runtime-aware partition planning, exact count-utilization factorization, and factorial-specific span or average-gap accounting.
