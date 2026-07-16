# Nova 2 Theorem Registry

## Proved theorems

| ID | Result label | Statement summary | Location |
|---|---|---|---|
| N2-ADD-101 through N2-ADD-106 | proved theorems | Capacity, lattice, repeated-label, approximation, and endpoint caveats | `models/TOY_COUNTEREXAMPLES.md` |
| N2-ADD-108 through N2-ADD-113 | proved theorems | Exact positivity and weighted-Fourier sufficient conditions | `models/TOY_SUFFICIENT_CONDITIONS.md` |
| N2-ADD-115 | proved theorem | Original valuation-tagged model fails its first required window | `proofs/VALUATION_TAGGED_LATTICE_OBSTRUCTION.md` |
| N2-ADD-116 | proved theorem | Exact lattice quotient normalization | `proofs/LATTICE_QUOTIENT_NORMALIZATION.md` |
| N2-ADD-118 | proved theorem | Three-power fallback has an exponential binary-spine prefix | `proofs/QUOTIENT_BINARY_SPINE_PREFIX.md` |
| N2-ADD-119 | proved theorem | Translated carrier blocks preserve downward-window density | `proofs/MARKER_THREE_CARRIER_BLOCK_REDUCTION.md` |
| N2-ADD-121 | proved theorem | Unique-parent stream emits exact odd factorial divisors in order | `proofs/MARKER_THREE_STREAMING_N46_AUDIT.md` |
| N2-ADD-122 | proved theorem | Exact carrier growth factors into prefix count and packing utilization | `proofs/EFFECTIVE_CARRIER_ENTROPY_FACTORIZATION.md` |
| N2-ADD-123 | proved theorem | Average internal gaps give a two-sided utilization sandwich and exact success or failure criteria | `proofs/AVERAGE_GAP_UTILIZATION_CRITERION.md` |
| N2-ADD-124 | proved theorem | Odd-core parity gives the sharp lower bounds `U_t>=2K_t-1` and `F_t/F_(t-1)>(D_t+2K_t)/(D_t+1)` | `proofs/PARITY_SPAN_COUNT_THRESHOLD_CRITERION.md` |
| N2-ADD-125 | proved theorem | Divisor complement symmetry gives the exact identity `U_t c_(tau_n+1-K_t)=C_n` | `proofs/DIVISOR_COMPLEMENT_QUANTILE_SPAN.md` |
| N2-ADD-126 | proved theorem | Certified lower-tail divisor counts and the divisor median give factorial-specific carrier-span lower bounds | `proofs/DIVISOR_COMPLEMENT_QUANTILE_SPAN.md` |
| N2-ADD-127 | proved theorem | Rankin weighted divisor moments give `U_t >= (K_t/Z_n(sigma))^(1/sigma)` for every `sigma>0` | `proofs/RANKIN_SMOOTH_DIVISOR_SPAN.md` |
| N2-ADD-128 | proved theorem | The Rankin, parity, and median span bounds combine into an explicit sufficient carrier product | `proofs/RANKIN_SMOOTH_DIVISOR_SPAN.md` |
| N2-OBS-109 | proved obstruction theorem | The first blocking gap, even together with `D` and `K`, cannot uniformly control utilization | `proofs/AVERAGE_GAP_UTILIZATION_CRITERION.md` |
| N2-OBS-110 | proved obstruction theorem | Count, threshold, and oddness alone cannot improve the parity-span lower bound by a fixed factor | `proofs/PARITY_SPAN_COUNT_THRESHOLD_CRITERION.md` |

## Accepted imported theorems

### N1-OBS-003

Source proof commit: `ac676b0fc9007117da1f1d9eaeec3e3cf65dd1e7`.

Sequential success requires

\[
\prod_{t=1}^{L}(1+K_t)
\ge
\frac{Y_n+1}{W_n+1}.
\]

Outcome: `ACCEPTED_WITH_RESTRICTIONS`. This is only a necessary prefix-count condition.

### N1-STR-023, N1-STR-024, and N1-STR-025

Latest inspected source: `nova/factorial-structure@8c7ee8f64af56a8d082f1fa3adabb0b0309f6e27`.

- `N1-STR-023`: exact meet-in-the-middle divisor stream. `ACCEPTED`.
- `N1-STR-024`: normalized count surplus. `ACCEPTED_WITH_RESTRICTIONS`.
- `N1-STR-025`: independent reconstruction of N2-ADD-122. `ACCEPTED`.

## Conditional theorems

### N2-ADD-114

Fixed legal disjoint labels, correction coverage, and a strict collision-aware weighted Fourier comparison for every target imply

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)=O((\log n)^2).
\]

### N2-ADD-117

The preserved three-power fallback reduces the theorem to four-point quotient occupancy and conditionally gives

\[
H_{n!}(X_n+1)\le M_n+r_n+3.
\]

### N2-ADD-120

For marker-three, connect from zero across core gaps at most

\[
D_t=\left\lfloor\frac{E_{t-1}+W_n+1}{2^{t-1}}\right\rfloor.
\]

If `E_L+W_n>=Y_n`, then

\[
H_{n!}(X_n+1)\le L+r_n.
\]

This remains a sequential sufficient condition subject to Phase 12P.

## Effective utilization package

Put

\[
F_t=E_t+W_n+1,
\quad
s_t=2^{t-1},
\quad
\eta_t=\frac{U_t}{K_tD_t},
\quad
\phi_t=\frac{s_tD_t}{F_{t-1}}.
\]

Then

\[
b_t=\frac{1+K_t\eta_t\phi_t}{1+K_t},
\qquad
\frac{D_t}{D_t+1}<\phi_t\le1.
\]

The exact endpoint factor is

\[
\Delta_n=\widetilde\Gamma_n\left(\prod_tb_t\right)^{1/L}.
\]

N2-ADD-123 gives the exact average-gap success and failure criteria. N2-OBS-109 rules out first external blocking gaps as a substitute for internal spacing.

N2-ADD-124 adds the sharp universal parity baseline

\[
\eta_t\ge\frac{2K_t-1}{K_tD_t}
\]

and the sufficient count-to-threshold condition

\[
\prod_{t=1}^{L}\frac{D_t+2K_t}{D_t+1}
\ge
\frac{Y_n+1}{W_n+1}.
\]

N2-OBS-110 proves this baseline is optimal among abstract odd-core carriers with only `K_t` and `D_t` specified.

For

\[
C_n=\frac{n!}{3\,2^{v_2(n!)}},
\]

let its divisors be `c_1<...<c_(tau_n)`. N2-ADD-125 proves

\[
U_t c_{\tau_n+1-K_t}=C_n.
\]

Thus the exact factorial span frontier is the complementary lower-tail order statistic. If a certified bound gives at least `tau_n-K_t+1` divisors at or below `B`, then N2-ADD-126 gives

\[
U_t\ge\frac{C_n}{B}.
\]

In particular, `K_t>tau_n/2` implies `U_t>=ceil(sqrt(C_n))`.

For every `sigma>0`, define the finite Euler product

\[
Z_n(\sigma)=\sum_{d\mid C_n}d^{-\sigma}
=\prod_{p^e\parallel C_n}\frac{1-p^{-(e+1)\sigma}}{1-p^{-\sigma}}.
\]

N2-ADD-127 proves

\[
U_t\ge\left(\frac{K_t}{Z_n(\sigma)}\right)^{1/\sigma}.
\]

N2-ADD-128 combines this bound with parity and the complement median in an explicit carrier product. This is the first factorial-specific lower bound that applies at every exact layer.

## Finite certificates

- `N2-FIN-201`: superseded-route rational-log certificate at `n=1892`.
- `N2-FIN-202`: exact complete-menu carrier coverage for `12<=n<=45`.
- `N2-FIN-203`: independent Nova 2 streaming certificate at `n=46`.
- `N2-FIN-204`: accepted Nova 1 full-core certificate for `47<=n<=50`, with exact `n=46` overlap.
- `N2-FIN-205`: accepted Nova 1 certificates for `n=51,52,53`.
- `N2-FIN-206`: accepted Nova 1 certificates `N1-FIN-009` and `N1-FIN-010` from exact source commits `dac958b62ef069310901f5063dbf8bd6cbe3c0e3` and `6b31a320fa4c4bd4c9b2395e60faa174198e022e`.

The sharp finite statements are

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le22
\qquad(12\le n\le54),
\]

and

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le23
\qquad(12\le n\le55).
\]

The smallest unaudited finite parameter is `n=56`.

## Finite utilization diagnostics

| `n` | endpoint surplus | parity-only root ratio | median-hybrid root ratio | Rankin-median root ratio |
|---:|---:|---:|---:|---:|
| 51 | 1.000004144206103 | 0.0000257773398727324 | 0.000145487587879522 | 0.000542135786332180 |
| 52 | 1.000001025305911 | 0.0000185652131315783 | 0.000123906257046752 | 0.000488608023294683 |
| 53 | 1.000001967025492 | 0.0000139117330218277 | 0.0000907853071519960 | 0.000443191288757114 |
| 54 | 1.000000334888580 | 0.00000997734788683994 | 0.0000892960011035230 | 0.000438131601230971 |
| 55 | 1.000000290721510 | 0.00000761958530584015 | 0.0000740382055592177 | 0.000374184125626777 |

The parity-only product falls below the exact endpoint scale by roughly `10^28` through `10^31`. The median-hybrid product improves this by about `10^4.5` through `10^5.9`. The Rankin-median product improves the median-hybrid bound by a further `10^3.4` through `10^4.2`, but still falls below the endpoint scale by roughly `10^19.6` through `10^20.6`. These are computational evidence only.

## Cross-track decisions

- `N1-HO-N2-009`: `ACCEPTED_WITH_RESTRICTIONS`.
- `N1-STR-025`: accepted independent reconstruction.
- `N1-FIN-009` and `N1-FIN-010`: accepted as finite certificates.
- `N1-CMP-008`: accepted only as computational evidence; N2-OBS-109 proves its first-blocking-gap statistic cannot control utilization.

## Open factorial nodes

1. Prove or disprove marker-three quotient occupancy uniformly through `Y_n`.
2. Improve the lower-tail divisor bound beyond the one-parameter Rankin moment, or prove a contrary complementary-quantile obstruction.
3. Extend exact finite certification from `n=56`.
4. Prove asymptotic endpoint-window coverage.
5. Upper-bound target-local collision multiplicity or additive energy.
6. Prove aggregate numerical phase dispersion and the strict weighted Fourier inequality.
7. Audit N2-ADD-120 against exact Phase 12P hypotheses.
8. Handle finite exceptions after an effective threshold exists.

## Promotion rule

No conditional result becomes an asymptotic factorial theorem until every structural, additive or analytic, endpoint, distinctness, and finite-exception node is proved and independently reconstructed.
