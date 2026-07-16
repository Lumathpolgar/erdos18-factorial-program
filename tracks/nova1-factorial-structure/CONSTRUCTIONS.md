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
- exact main support lattice `3Z` and all correction residues;
- exact quotient-window correction theorem;
- unconditional `exp(O((log n)^2))` initial interval;
- exponential high-prime menu capacity;
- multiplicative 3-density of the reserved odd core;
- total quotient endpoint support;
- exact unique-parent and meet-in-the-middle divisor streams;
- layer-normalized count surplus;
- exact count-utilization factorization;
- sharp parity-span baseline `U_t>=2K_t-1`;
- overflow-safe half-list truncation and exact checkpoint continuation.

### Exact finite certificates

The complete connected-core carrier is exactly certified for

\[
12\le n\le57.
\]

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
\qquad(12\le n\le57).
\]

Recent certificates:

| ID | `n` | method | layers | term bound |
|---|---:|---|---:|---:|
| N1-FIN-006 | 51 | unique-parent stream | 6 | 22 |
| N1-FIN-007 | 52 | meet-in-the-middle stream | 6 | 22 |
| N1-FIN-008 | 53 | dual-partition stream | 6 | 22 |
| N1-FIN-009 | 54 | runtime-aware dual-partition stream | 6 | 22 |
| N1-FIN-010 | 55 | effective-carrier stream | 6 | 23 |
| N1-FIN-011 | 56 | overflow-safe-regressed seven-layer stream | 7 | 24 |
| N1-FIN-012 | 57 | overflow-safe checkpointed dual-partition stream | 7 | 24 |

At `n=57`, six layers reach only

\[
F_6/(Y_{57}+1)=0.0873914320600893\ldots,
\]

while seven layers give

\[
F_7/(Y_{57}+1)=1.0873914095218273\ldots.
\]

### Effective finite diagnostics

For the exact root-normalized count surplus, utilization, and endpoint growth:

| `n` | count surplus | utilization root | endpoint surplus |
|---:|---:|---:|---:|
| 51 | 120.322026488584 | 0.008311064676932 | 1.000004144206103 |
| 52 | 97.645052132052 | 0.010241184816549 | 1.000001025305911 |
| 53 | 124.609364763243 | 0.008025094814707 | 1.000001967025492 |
| 54 | 92.273264366777 | 0.010837378971591 | 1.000000334888580 |
| 55 | 98.919733584849 | 0.010109209300122 | 1.000000290721510 |
| 56 | 673.791460795324 | 0.001530254006653 | 1.031072082530349 |
| 57 | 604.565529127373 | 0.001673996726008 | 1.012040716416255 |

The large count surplus is mostly consumed by packing-utilization loss. No asymptotic conclusion is drawn.

At `n=57`, the parity-only endpoint product misses by approximately `2.82e32`. Factorial-specific internal spacing supplies essentially all missing expansion. The geometric mean of

\[
\eta_t=\frac{U_t}{K_tD_t}
\]

is approximately `0.00165403239908516`.

### Verification correction

`N1-DIS-007` rejects unrestricted unsigned-128 half-list multiplication as an exact verifier. At `n=57`, two unguarded coordinate partitions produced different connected-prefix counts.

The authoritative verifier is

`verification/marker_three_mitm_checkpoint_u128.cpp`.

It uses:

- endpoint-truncated half lists;
- division-based multiplication guards;
- exact cached half lists;
- deterministic checkpoint serialization and continuation;
- strict duplicate and ordering rejection.

Overflow-safe replays reproduce the accepted mathematical outputs for every `52<=n<=56`.

### Blocking-gap boundary

`N1-DIS-008` rejects the finite candidate `g_t/D_t<1.108`. At `n=57`, layer `3`,

\[
g_3/D_3=1.1674772300983786\ldots.
\]

A first external blocking gap does not control internal average spacing.

### Exact open component

Prove or disprove that, for all sufficiently large `n`, every quotient target

\[
W_n+1\le q\le\left\lfloor\frac{X_n}{3}\right\rfloor
\]

has a rainbow sum in `[q-W_n,q]`.

For the sequential engine, the immediate theorem must control factorial-specific

\[
A_t=\frac{U_t}{2K_t-1}
\]

or

\[
\eta_t=\frac{U_t}{K_tD_t},
\]

not count, parity, or first external gaps alone.

### Primary risks

- final downward endpoint-window gaps;
- collision concentration and quotient additive shell gaps;
- insufficient factorial-specific packing utilization;
- failure of a uniform internal-span or average-gap theorem;
- failure of compact phase dispersion;
- a proof that silently becomes sequential when claiming a final-only result;
- verifier arithmetic or checkpoint corruption not caught by fail-closed audits.

## N1-CON-002: Marked complement-pair menu clouds

Result label: **conditional theorem** as a secondary route.

Rank: secondary.

Path: `constructions/MARKED_COMPLEMENT_PAIR_CLOUDS.md`.

Proved components include divisor legality, low/high distinctness, fixed-marker palette separation, polylogarithmic selected-term cost, and the necessary menu-capacity gate.

Open components are sufficiently large square-center and multiplier menus, lattice-first compatibility, uniform downward-window occupancy, and collision or shell-gap control.

## N1-CON-001: Original valuation-tagged addresses

Result label: **disproved route**.

Path: `constructions/VALUATION_TAGGED_ADDRESS_PACKETS.md`.

The original addresses `e_t=r_n+t` forced every main sum into `2^(r_n+1)Z` while the correction radius was only `2^r_n-1`. Nova 2 theorem `N2-ADD-115` disproved this route at exact commit `45c74a5fa747551422ffcad7d3ddf22788fbe622`.

## Other disproved routes

| Result label | Route |
|---|---|
| disproved route | Fixed addressed divisor pool |
| disproved route | Fixed complement-pair pool |
| disproved route | Polynomial-size menus |
| disproved route | Independent prime-power atoms |
| disproved route | One factorial arithmetic block per layer |
| disproved route | Unguarded unsigned-128 MITM verifier |
| disproved route | Finite first-blocking-gap constant `1.108` |

## Construction acceptance checklist

Every future revision must include exact divisor formulas, valuation legality, support lattice, residue classes, correction radius, first-target coverage, endpoint support, endpoint-window audit, choice counts, selected-term count, numerical distinctness, profile capacity, collision loss, sequential obstruction, exact missing theorems, finite tests, asymptotic failure conditions, exact labels, replayable fail-closed certificates, runtime-aware partition planning, effective count-utilization factorization, overflow-safe arithmetic, and checkpoint integrity.
