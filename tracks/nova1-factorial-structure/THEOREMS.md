# Nova 1 Theorem Registry

## Status rule

Every result is labeled exactly as one of:

- **proved theorem**;
- **conditional theorem**;
- **finite certificate**;
- **computational evidence**;
- **disproved route**.

No finite result is promoted to an asymptotic theorem. No formal profile count is treated as numerical occupancy.

## Structural and reduction theorems

| ID | Result label | Conclusion | Proof or source |
|---|---|---|---|
| N1-STR-003 | proved theorem | Exact Legendre budgets, quotient bands, dyadic bands, and factorial 2-adic multiplicity | `proofs/VALUATION_BUDGET_LEMMAS.md` |
| N1-STR-004 | proved theorem | Exponent boxes produce unique legal divisors | `FACTORIAL_DIVISOR_ATLAS.md` |
| N1-STR-005 | proved theorem | Allocated valuation budgets preserve divisor legality | `FACTORIAL_DIVISOR_ATLAS.md` |
| N1-STR-006 | proved theorem | Distinct marker signatures force numerical distinctness | `proofs/DISTINCTNESS_AND_CORRECTION.md` |
| N1-STR-007 | proved theorem | Square-center complement pairing gives legal bounded distinct reciprocal pairs | `proofs/COMPLEMENT_PAIRING_LEMMA.md` |
| N1-COR-001 | proved theorem | Binary powers represent every residual in `[0,2^r-1]` | `proofs/DISTINCTNESS_AND_CORRECTION.md` |
| N1-RED-002 | proved theorem | Downward main occupancy plus binary correction gives exact local coverage | `proofs/DISTINCTNESS_AND_CORRECTION.md` |
| N1-OBS-002 | proved theorem | Downward `R`-density requires `|S|(R+1)>=X+1` | `proofs/COUNTING_CAPACITY_OBSTRUCTION.md` |
| N1-STR-008 | proved theorem | Polylogarithmic layers with polynomial correction require geometric-mean menu size `exp(Omega(n/log n))` | `proofs/MENU_ENTROPY_REQUIREMENT.md` |
| N1-STR-009 | proved theorem | High-prime subset products supply exponentially many legal cores | `proofs/HIGH_PRIME_MENU_CAPACITY.md` |

## Marker-three route

| ID | Result label | Conclusion | Proof or source |
|---|---|---|---|
| N1-STR-014 | proved theorem | Marker-three divisors are legal, layer-distinct, and disjoint from the palette | `proofs/MARKER_THREE_LATTICE_REPAIR.md` |
| N1-STR-015 | proved theorem | Main support generates exactly `3Z`; palette sums attain every residue modulo `3` | `proofs/MARKER_THREE_LATTICE_REPAIR.md` |
| N1-RED-004 | proved theorem | Quotient occupancy in every `[q-W_n,q]` implies `H_{n!}(X_n+1)<=M_n+r_n` | `proofs/MARKER_THREE_LATTICE_REPAIR.md` |
| N1-STR-016 | proved theorem | Odd positional digits have maximum downward gap one | `proofs/MARKER_THREE_LATTICE_REPAIR.md` |
| N1-STR-017 | proved theorem | Unconditional coverage through `3m_n(2^{M_n}-1)+2` | `proofs/MARKER_THREE_LATTICE_REPAIR.md` |
| N1-STR-018 | proved theorem | For `n>=120368`, every repaired layer has at least `2^{n/(3 log n)-1}` legal high-prime cores | `proofs/MARKER_THREE_MENU_CAPACITY.md` |
| N1-CAP-002 | proved theorem | Formal profile-capacity gate holds for `n>=120368` | `proofs/MARKER_THREE_MENU_CAPACITY.md` |
| N1-STR-019 | proved theorem | `D_n=n!/(3*2^{v_2(n!)})` is multiplicatively 3-dense for `n>=6` | `proofs/QUOTIENT_ENDPOINT_SUPPORT.md` |
| N1-STR-020 | proved theorem | Three quotient-layer terms push maximum support past `floor(X_n/3)` for `n>=12` | `proofs/QUOTIENT_ENDPOINT_SUPPORT.md` |
| N1-RED-006 | proved theorem | Deterministic increasing-layer selection leaves residual below `max((2/3)^Lq,2^L)` | `proofs/QUOTIENT_ENDPOINT_SUPPORT.md` |
| N1-STR-021 | proved theorem | Explicit factorial arithmetic blocks are legal connected submenus | `proofs/FACTORIAL_BLOCK_CARRIER_OBSTRUCTION.md` |
| N1-COL-001 | proved theorem | At least `2^{floor(M_n/2)}` legal profiles collide at one quotient sum | `proofs/RAINBOW_CARRY_COLLISIONS.md` |
| N1-OBS-003 | proved theorem | Sequential carrier success requires sufficient connected-prefix entropy | `proofs/CONNECTED_PREFIX_ENTROPY_REQUIREMENT.md` |
| N1-STR-022 | proved theorem | Unique-parent streaming plus record-gap counts exactly recovers `u_t^*` and `K_t` | `proofs/STREAMING_CONNECTED_PREFIX_CERTIFIER.md` |
| N1-STR-023 | proved theorem | Meet-in-the-middle row merging exactly recovers divisor order | `proofs/MEET_IN_THE_MIDDLE_CONNECTED_PREFIX_STREAM.md` |
| N1-STR-024 | proved theorem | Layer-normalized count surplus meets the exact count gate iff `Gamma_n>=1` | `proofs/NORMALIZED_CONNECTED_PREFIX_SURPLUS.md` |
| N1-STR-025 | proved theorem | Exact carrier growth factors into connected-prefix count and packing utilization | `proofs/EFFECTIVE_CARRIER_FACTORIZATION_RECONSTRUCTION.md` |
| N1-STR-026 | proved theorem | Every positive odd-core prefix satisfies `U_t>=2K_t-1`, yielding a parity-span expansion lower bound | `proofs/PARITY_SPAN_CRITERION_RECONSTRUCTION.md` |
| N1-OBS-004 | proved theorem | The parity-span bound is optimal when only oddness, `K_t`, and `D_t` are specified | `proofs/PARITY_SPAN_CRITERION_RECONSTRUCTION.md` |

## Exact effective carrier identities

For executed layers,

\[
F_0=W_n+1,
\qquad
F_t=F_{t-1}+2^{t-1}U_t.
\]

Put

\[
P_n=\prod_{t=1}^{L}(1+K_t),
\qquad
b_t=\frac{F_t/F_{t-1}}{1+K_t}.
\]

Then `N1-STR-025` proves

\[
\frac{F_L}{W_n+1}=P_n\prod_{t=1}^{L}b_t.
\]

With

\[
R_n=\frac{Y_n+1}{W_n+1},
\quad
\widetilde\Gamma_n=(P_n/R_n)^{1/L},
\quad
\mathcal B_n=\left(\prod_tb_t\right)^{1/L},
\]

\[
\Delta_n=\left(\frac{F_L}{Y_n+1}\right)^{1/L},
\]

one has

\[
\Delta_n=\widetilde\Gamma_n\mathcal B_n.
\]

Endpoint success is equivalent to `Delta_n>=1`.

`N1-STR-026` gives the parity-only sufficient criterion

\[
\prod_{t=1}^{L}\frac{D_t+2K_t}{D_t+1}
\ge
R_n.
\]

`N1-OBS-004` proves no fixed-factor improvement is possible from oddness, count, and threshold alone. Any stronger sequential theorem must use factorial-specific internal spacing.

## Conditional results

| ID | Result label | Conclusion | Dependency |
|---|---|---|---|
| N1-RED-005 | conditional theorem | Exact quotient rainbow occupancy implies `H_{n!}(floor(sqrt(n!))+1)=O((log n)^2)` | Global quotient occupancy |
| N1-RED-001 | conditional theorem | The local half-range theorem implies `h(n!)=O((log n)^3)` | Track B reconstruction |

## Finite certificates and computational evidence

| ID | Result label | Scope | Source |
|---|---|---|---|
| N1-CMP-003 | computational evidence | Reduced quotient audit for `7<=n<=14` | `verification/MARKER_THREE_FINITE_REPORT.md` |
| N1-CMP-004 | finite certificate | Endpoint-support and coarse-contraction checks | `verification/ENDPOINT_SUPPORT_FINITE_REPORT.md` |
| N1-CMP-005 | finite certificate | Block and collision checks | `verification/BLOCK_COLLISION_FINITE_REPORT.md` |
| N1-CMP-006 | computational evidence | Count surplus at `n=51,52,53` is non-monotone | `verification/connected_prefix_normalized_n51_n53.csv` |
| N1-CMP-007 | computational evidence | Count surplus through `n=54` and finite blocking-gap audit | `verification/connected_prefix_normalized_n51_n54.csv` |
| N1-CMP-008 | computational evidence | Exact count, utilization, and endpoint factors through `n=55` | `verification/effective_carrier_n51_n55.csv` |
| N1-CMP-009 | computational evidence | Seven-layer effective and parity-span diagnostics at `n=56`; 31 finite blocked layers retain `g_t/D_t<1.108` | `verification/effective_carrier_n51_n56.csv` |
| N2-FIN-202 | finite certificate | Imported complete-menu carrier coverage for `12<=n<=45` | Nova 2 commit `82603c631a106c3bff4676bdeeb9cc791fc98f3c` |
| N1-FIN-005 | finite certificate | Exact complete-core coverage for `46<=n<=50` | `verification/FULL_CORE_N46_N50_REPORT.md` |
| N1-FIN-006 | finite certificate | Exact streaming coverage at `n=51` | `verification/FULL_CORE_N51_REPORT.md` |
| N1-FIN-007 | finite certificate | Exact meet-in-the-middle coverage at `n=52` | `verification/FULL_CORE_N52_REPORT.md` |
| N1-FIN-008 | finite certificate | Exact dual-partition coverage at `n=53` | `verification/FULL_CORE_N53_REPORT.md` |
| N1-FIN-009 | finite certificate | Exact runtime-aware dual-partition coverage at `n=54` | `verification/FULL_CORE_N54_REPORT.md` |
| N1-FIN-010 | finite certificate | Exact effective-carrier coverage at `n=55` | `verification/FULL_CORE_N55_REPORT.md` |
| N1-FIN-011 | finite certificate | Exact seven-layer dual-partition coverage at `n=56` | `verification/FULL_CORE_N56_REPORT.md` |

The sharp exact finite statements are

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

No conclusion is asserted for `n>=57`.

## Disproved routes

| ID | Result label | Claim rejected | Proof or source |
|---|---|---|---|
| N1-DIS-001 | disproved route | Prime powers of one prime behave as independent coordinates | `FACTORIAL_DIVISOR_ATLAS.md` |
| N1-DIS-002 | disproved route | A fixed pool of polylogarithmically many binary or ternary choices covers the half-range | `proofs/COUNTING_CAPACITY_OBSTRUCTION.md` |
| N1-DIS-003 | disproved route | Polynomial-size menus with polynomial correction cover the half-range | `proofs/MENU_ENTROPY_REQUIREMENT.md` |
| N1-DIS-004 | disproved route | Complement pairing alone implies additive density | `proofs/COMPLEMENT_PAIRING_LEMMA.md` |
| N1-DIS-005 | disproved route | Original addresses `e_t=r_n+t` satisfy the old correction request | Nova 2 `N2-ADD-115` |
| N1-DIS-006 | disproved route | One factorial arithmetic block per layer reaches `Y_n` within `M_n` layers | `proofs/FACTORIAL_BLOCK_CARRIER_OBSTRUCTION.md` |

## Promotion rule

No conditional theorem becomes a **proved theorem** until every named dependency is proved and independently reconstructed. No **finite certificate** or **computational evidence** is promoted to an asymptotic theorem.
