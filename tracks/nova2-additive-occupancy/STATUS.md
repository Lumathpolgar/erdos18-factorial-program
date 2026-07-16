# Nova 2 Status

## Track and branch

- Track: Additive Occupancy and Global Sumsets
- Branch: `nova/additive-occupancy`
- Overall state: `MARKER_THREE_CERTIFIED_N12_N55_AVERAGE_GAP_UTILIZATION_OPEN`

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
- `N2-OBS-109`: first-blocking-gap non-identifiability.

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

## Retired sequential statistic

Nova 1 finite evidence gives `g_t/D_t<1.108` across blocked layers for `51<=n<=55`.

N2-OBS-109 proves that even fixing identical values of `D`, `K`, and the first blocking gap `g=D+2` permits utilization factors ranging from a quantity tending to zero to a quantity tending to one. Therefore first external blocking gaps cannot control sequential utilization.

The missing statistic is the internal connected-prefix span or average internal gap:

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

| `n` | count surplus | utilization root | endpoint surplus |
|---:|---:|---:|---:|
| 51 | 120.322026488584 | 0.008311064676932 | 1.000004144206103 |
| 52 | 97.645052132052 | 0.010241184816549 | 1.000001025305911 |
| 53 | 124.609364763243 | 0.008025094814707 | 1.000001967025492 |
| 54 | 92.273264366777 | 0.010837378971591 | 1.000000334888580 |
| 55 | 98.919733584849 | 0.010109209300122 | 1.000000290721510 |

These values are finite and non-monotone. They do not establish an asymptotic trend.

## Preferred proof engines

1. Final-only target-dependent numerical tilt and aggregate phase dispersion.
2. Deterministic final restricted-sumset growth.
3. Connected-core recursion, now requiring average internal-gap control and a Phase 12P audit.
4. Preserved three-power fallback.

## Cross-track requests

### Nova 1

Prove pointwise or averaged lower or upper bounds for `eta_t=U_t/(K_tD_t)` under the exact factorial-divisor thresholds. First-blocking-gap estimates are no longer accepted as a substitute.

### Nova 3

Continue aggregate odd-core phase dispersion, collision-aware reference laws, and the strict weighted Fourier inequality.

### Nova 4

Independently reconstruct N2-OBS-109 and N2-ADD-123, replay the finite certificates through `n=55`, and extend from `n=56`.

## Exact open blockers

1. Uniform marker-three quotient occupancy through `Y_n`.
2. An average internal-gap lower bound forcing `Delta_n>=1`, or an upper bound forcing `Delta_n<1` and retiring the sequential engine.
3. Exact finite extension from `n=56`.
4. Uniform endpoint-window coverage.
5. Target-local collision multiplicity or additive-energy control.
6. Aggregate numerical phase dispersion and strict weighted Fourier positivity.
7. Phase 12P compatibility.
8. Remaining finite exceptions.

## Claim boundary

Exact coverage through `n=55`, N2-ADD-123, and N2-OBS-109 do not prove asymptotic occupancy, the factorial half-range theorem for all sufficiently large `n`, or Erdos Problem 18.

## Next theorem target

Prove or refute a uniform bound for the average internal-gap factors `eta_t` in the complete factorial-divisor connected prefixes. This is now the exact sequential frontier.