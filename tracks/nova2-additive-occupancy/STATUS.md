# Nova 2 Status

## Track and branch

- Track: Additive Occupancy and Global Sumsets
- Branch: `nova/additive-occupancy`
- Overall state: `MARKER_THREE_CERTIFIED_N12_N55_RANKIN_SMOOTH_DIVISOR_OPEN`

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
- `N2-ADD-125`: exact divisor-complement order-statistic identity;
- `N2-ADD-126`: lower-tail quantile and median carrier bounds;
- `N2-ADD-127`: Rankin weighted-divisor span bound;
- `N2-ADD-128`: explicit Rankin-median carrier criterion;
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

## Universal and factorial-specific span bounds

The universal parity theorem gives

\[
U_t\ge2K_t-1.
\]

For the reserved odd core

\[
C_n=\frac{n!}{3\,2^{v_2(n!)}},
\]

write its positive divisors as

\[
1=c_1<\cdots<c_{\tau_n}=C_n.
\]

N2-ADD-125 gives the exact identity

\[
U_t c_{\tau_n+1-K_t}=C_n.
\]

Thus

\[
A_t=\frac{U_t}{2K_t-1}
=\frac{C_n}{(2K_t-1)c_{\tau_n+1-K_t}}.
\]

If at least `tau_n-K_t+1` divisors lie at or below `B`, then

\[
U_t\ge\frac{C_n}{B}.
\]

In particular,

\[
K_t>\frac{\tau_n}{2}
\quad\Longrightarrow\quad
U_t\ge\left\lceil\sqrt{C_n}\right\rceil.
\]

For every `sigma>0`, define

\[
Z_n(\sigma)
=\sum_{d\mid C_n}d^{-\sigma}
=\prod_{p^e\parallel C_n}
\frac{1-p^{-(e+1)\sigma}}{1-p^{-\sigma}}.
\]

N2-ADD-127 proves the factorial-specific bound

\[
U_t\ge
\left(\frac{K_t}{Z_n(\sigma)}\right)^{1/\sigma}.
\]

This bound applies at every layer and uses the complete exact prime-exponent profile of `C_n`.

## Retired or insufficient sequential inputs

1. First external blocking gaps are non-identifying by N2-OBS-109.
2. Prefix count and parity alone are optimal but quantitatively insufficient by N2-OBS-110 and N2-CMP-206.
3. Divisor median symmetry is stronger, but N2-CMP-207 still leaves a finite endpoint deficit of roughly `10^23` through `10^25`.
4. The one-parameter Rankin moment improves the median-hybrid product by a further `10^3.4` through `10^4.2`, but N2-CMP-208 still leaves a deficit of roughly `10^19.6` through `10^20.6`.

The missing input is now a sharper lower-tail divisor theorem than the one-parameter Rankin moment, equivalently a stronger upper bound for

\[
c_{\tau_n+1-K_t}.
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

| `n` | endpoint surplus | parity root | median-hybrid root | Rankin-median root |
|---:|---:|---:|---:|---:|
| 51 | 1.000004144206103 | 0.0000257773398727324 | 0.000145487587879522 | 0.000542135786332180 |
| 52 | 1.000001025305911 | 0.0000185652131315783 | 0.000123906257046752 | 0.000488608023294683 |
| 53 | 1.000001967025492 | 0.0000139117330218277 | 0.0000907853071519960 | 0.000443191288757114 |
| 54 | 1.000000334888580 | 0.00000997734788683994 | 0.0000892960011035230 | 0.000438131601230971 |
| 55 | 1.000000290721510 | 0.00000761958530584015 | 0.0000740382055592177 | 0.000374184125626777 |

These values are finite diagnostics only. No asymptotic trend is inferred.

## Preferred proof engines

1. Final-only target-dependent numerical tilt and aggregate phase dispersion.
2. Deterministic final restricted-sumset growth.
3. Connected-core recursion, now requiring a multi-parameter or saddle-point lower-tail divisor theorem and a Phase 12P audit.
4. Preserved three-power fallback.

## Cross-track requests

### Nova 1

Improve the Rankin lower-tail bound through a multi-parameter exponent box, a saddle-point divisor estimate, or a direct smooth-divisor counting theorem for `C_n`.

### Nova 3

Continue aggregate odd-core phase dispersion, collision-aware reference laws, and the strict weighted Fourier inequality.

### Nova 4

Independently reconstruct N2-ADD-127 and N2-ADD-128, replay N2-CMP-208, and extend exact finite certification from `n=56`.

## Exact open blockers

1. Uniform marker-three quotient occupancy through `Y_n`.
2. A lower-tail divisor theorem stronger than the one-parameter Rankin moment, or a contrary complementary-quantile obstruction retiring the sequential engine.
3. Exact finite extension from `n=56`.
4. Uniform endpoint-window coverage.
5. Target-local collision multiplicity or additive-energy control.
6. Aggregate numerical phase dispersion and strict weighted Fourier positivity.
7. Phase 12P compatibility.
8. Remaining finite exceptions.

## Claim boundary

Exact coverage through `n=55`, complement symmetry, the median theorem, and the Rankin theorem do not prove asymptotic occupancy, the factorial half-range theorem for all sufficiently large `n`, or Erdos Problem 18.

## Next theorem target

Replace the one-parameter Rankin moment by a sharper certified lower-tail count, preferably a saddle-point or multi-parameter exponent allocation for divisors of `C_n`.
