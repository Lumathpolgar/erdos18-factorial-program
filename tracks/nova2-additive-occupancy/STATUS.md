# Nova 2 Status

## Track and branch

- Track: Additive Occupancy and Global Sumsets
- Branch: `nova/additive-occupancy`
- Overall state: `MARKER_THREE_CERTIFIED_N12_N55_FACTORIAL_SPAN_AMPLIFICATION_OPEN`

The factorial formulation of Erdos Problem 18 remains open.

## Preferred marker-three model

Frozen structural source:

- branch: `nova/factorial-structure`;
- commit: `ebb47ba436af554366d0f285119a769f31f9e561`;
- construction: `N1-CON-003`;
- Nova 2 outcome: `ACCEPTED_WITH_RESTRICTIONS`.

The structural gate passes, but global quotient occupancy remains open.

## Deterministic theorem package

Nova 2 proved:

- `N2-ADD-119`: translated carrier blocks;
- `N2-ADD-120`: connected-core recursion;
- `N2-ADD-121`: exact unique-parent divisor stream;
- `N2-ADD-122`: exact count-utilization factorization;
- `N2-ADD-123`: average internal-gap utilization sandwich;
- `N2-ADD-124`: sharp parity-span count-to-threshold criterion;
- `N2-OBS-109`: first-blocking-gap non-identifiability;
- `N2-OBS-110`: optimality of parity and count information without factorial-specific spacing.

For one layer,

\[
D_t=\left\lfloor\frac{F_{t-1}}{2^{t-1}}\right\rfloor,
\qquad
\eta_t=\frac{U_t}{K_tD_t},
\qquad
\phi_t=\frac{2^{t-1}D_t}{F_{t-1}},
\]

and

\[
b_t=\frac{1+K_t\eta_t\phi_t}{1+K_t},
\qquad
\frac{D_t}{D_t+1}<\phi_t\le1.
\]

The exact endpoint condition is

\[
\Delta_n=\widetilde\Gamma_n\left(\prod_tb_t\right)^{1/L}\ge1.
\]

## Sharp universal baseline

Because the positive cores are distinct odd integers,

\[
U_t\ge2K_t-1,
\qquad
\eta_t\ge\frac{2K_t-1}{K_tD_t}.
\]

Hence

\[
\frac{F_t}{F_{t-1}}
>
\frac{D_t+2K_t}{D_t+1}.
\]

The product condition

\[
\prod_t\frac{D_t+2K_t}{D_t+1}
\ge
\frac{Y_n+1}{W_n+1}
\]

is sufficient for endpoint coverage.

N2-OBS-110 proves this is best possible using only oddness, `K_t`, and `D_t`. Any stronger theorem must use the actual factorial-divisor distribution inside the connected prefix.

## Retired sequential statistics

1. The first external blocking gap is non-identifying by N2-OBS-109.
2. Prefix count and parity alone are quantitatively insufficient by N2-OBS-110 and N2-CMP-206.

The exact missing statistic is factorial-specific span amplification

\[
A_t=\frac{U_t}{2K_t-1},
\]

or equivalently a factorial-specific lower or upper bound for

\[
\eta_t=\frac{U_t}{K_tD_t}.
\]

## Nova 1 intake

Latest inspected source:

`nova/factorial-structure@8c7ee8f64af56a8d082f1fa3adabb0b0309f6e27`.

Decisions:

- `N1-STR-025`: `ACCEPTED` as an independent reconstruction of N2-ADD-122;
- `N1-FIN-009`: accepted finite certificate at `n=54`;
- `N1-FIN-010`: accepted finite certificate at `n=55`;
- `N1-CMP-008`: accepted as finite computational evidence only.

## Exact finite range

The sharp statements are

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le22
\qquad(12\le n\le54),
\]

and

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le23
\qquad(12\le n\le55).
\]

The term-bound transition occurs because `r_55=17`. The smallest unaudited finite parameter is `n=56`.

## Finite effective diagnostics

| `n` | endpoint surplus | parity-only root ratio |
|---:|---:|---:|
| 51 | 1.000004144206103 | 0.0000257773398727324 |
| 52 | 1.000001025305911 | 0.0000185652131315783 |
| 53 | 1.000001967025492 | 0.0000139117330218277 |
| 54 | 1.000000334888580 | 0.00000997734788683994 |
| 55 | 1.000000290721510 | 0.00000761958530584015 |

The parity-only product misses the exact endpoint scale by roughly `10^28` through `10^31` on this finite range. Actual factorial-divisor spacing supplies nearly all useful expansion. These diagnostics do not establish an asymptotic trend.

## Preferred proof engines

1. Final-only target-dependent numerical tilt and aggregate phase dispersion.
2. Deterministic final restricted-sumset growth.
3. Connected-core recursion, now requiring factorial-specific span amplification and a Phase 12P audit.
4. Preserved three-power fallback.

## Cross-track requests

### Nova 1

Prove a pointwise or averaged theorem for `A_t=U_t/(2K_t-1)` or `eta_t` under the exact factorial-divisor thresholds. Count, parity, and first-blocking-gap estimates are no longer sufficient.

### Nova 3

Continue aggregate odd-core phase dispersion, collision-aware reference laws, and the strict weighted Fourier inequality.

### Nova 4

Independently reconstruct N2-ADD-124 and N2-OBS-110, replay N2-CMP-206, and extend exact finite certification from `n=56`.

## Exact open blockers

1. Uniform marker-three quotient occupancy through `Y_n`.
2. A factorial-specific span-amplification lower bound forcing `Delta_n>=1`, or an upper bound forcing `Delta_n<1` and retiring the sequential engine.
3. Exact finite extension from `n=56`.
4. Uniform endpoint-window coverage.
5. Target-local collision multiplicity or additive-energy control.
6. Aggregate numerical phase dispersion and strict weighted Fourier positivity.
7. Phase 12P compatibility.
8. Remaining finite exceptions.

## Claim boundary

Exact coverage through `n=55` and the sharp parity-span theorem do not prove asymptotic occupancy, the factorial half-range theorem for all sufficiently large `n`, or Erdos Problem 18.

## Next theorem target

Prove or refute a uniform factorial-specific lower bound for the span amplification `U_t/(2K_t-1)` across enough exact carrier layers.