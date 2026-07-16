# Nova 1 Open Requirements

## Global quotient requirement

### N1-REQ-N2-002

Result label: **conditional theorem** request.

For

\[
X_n=\lfloor\sqrt{n!}\rfloor,
\qquad
Y_n=\left\lfloor\frac{X_n}{3}\right\rfloor,
\]

\[
r_n=\lceil4\log n\rceil,
\qquad
M_n=\lceil16(\log n)^2\rceil,
\qquad
W_n=\left\lfloor\frac{2^{r_n}-3}{3}\right\rfloor,
\]

and

\[
B_t(n)=
\{2^{t-1}u:u\text{ odd},\ 3u\mid n!,\ 2^{t-1}u\le Y_n\},
\]

prove that an absolute `n_0` exists such that every

\[
W_n+1\le q\le Y_n
\]

has a legal rainbow sum in

\[
[q-W_n,q].
\]

At most one nonzero term may be selected from each layer. The global occupancy theorem remains open.

## Connected-prefix count requirement

### N1-REQ-N2-003

Result label: **conditional theorem** request.

For executed layers define

\[
P_n=\prod_{t=1}^{L}(1+K_t),
\qquad
Q_n=\left\lceil\frac{Y_n+1}{W_n+1}\right\rceil.
\]

`N1-OBS-003` proves the necessary gate

\[
P_n\ge Q_n.
\]

`N1-STR-024` defines

\[
\Gamma_n=(P_n/Q_n)^{1/L}
\]

and proves `P_n>=Q_n` exactly when `Gamma_n>=1`.

This remains necessary but not sufficient. `N1-STR-025` shows packing utilization can consume almost all count surplus.

## Effective carrier-utilization requirement

### N1-REQ-N2-006

Result label: **conditional theorem** request.

Imported and independently reconstructed source:

- source branch: `nova/additive-occupancy`;
- source commit: `2ab09dd980f7116b82530368e3d98bb53240bf0c`;
- source theorem: `N2-ADD-122`;
- Nova 1 theorem: `N1-STR-025`.

Let

\[
F_0=W_n+1,
\qquad
F_t=F_{t-1}+2^{t-1}U_t,
\]

and

\[
b_t=\frac{F_t/F_{t-1}}{1+K_t}.
\]

Then

\[
\frac{F_L}{W_n+1}
=
P_n\prod_{t=1}^{L}b_t.
\]

Put

\[
R_n=\frac{Y_n+1}{W_n+1},
\qquad
\widetilde\Gamma_n=(P_n/R_n)^{1/L},
\]

\[
\mathcal B_n=\left(\prod_tb_t\right)^{1/L},
\qquad
\Delta_n=\left(\frac{F_L}{Y_n+1}\right)^{1/L}.
\]

Then

\[
\Delta_n=\widetilde\Gamma_n\mathcal B_n,
\]

and endpoint success is equivalent to `Delta_n>=1`.

Accepted outcomes are:

1. a **proved theorem** giving a uniform lower bound `Delta_n>=1` for enough exact layers;
2. a **proved theorem** giving `Delta_n<1` eventually or infinitely often, retiring the sequential engine;
3. a **conditional theorem** reducing `Delta_n>=1` to an explicit factorial-divisor spacing theorem;
4. an exact counterexample with replayable certificate.

## Factorial-specific internal-span requirement

### N1-REQ-N2-007

Result label: **conditional theorem** request.

Imported and independently reconstructed source:

- source branch: `nova/additive-occupancy`;
- exact source commit: `47ed3938d8900c82b245a3592502ac957330bbc6`;
- source results: `N2-ADD-124`, `N2-OBS-110`;
- Nova 1 results: `N1-STR-026`, `N1-OBS-004`.

For every positive odd-core prefix,

\[
U_t\ge2K_t-1.
\]

This gives the parity-only sufficient product

\[
\prod_{t=1}^{L}
\frac{D_t+2K_t}{D_t+1}
\ge
R_n.
\]

The bound is optimal if only oddness, `K_t`, and `D_t` are supplied. Therefore the next valid theorem must use factorial-specific information and control one of

\[
A_t=\frac{U_t}{2K_t-1},
\qquad
\eta_t=\frac{U_t}{K_tD_t},
\]

or an equivalent internal average-gap statistic.

Accepted outcomes are:

1. a uniform lower bound for enough `A_t` or `eta_t` that forces `Delta_n>=1`;
2. a uniform upper obstruction that forces `Delta_n<1` eventually or infinitely often;
3. a conditional reduction to an explicit divisor-distribution theorem for
   \[
   D_n=\frac{n!}{3\cdot2^{v_2(n!)}};
   \]
4. an exact counterexample.

At `n=56`, the parity-only endpoint ratio has seventh root

\[
0.0000307763983342963\ldots,
\]

and misses the endpoint by about `3.82e31` before factorial-specific amplification. This is **computational evidence** only.

## Divisor gap requirement

### N1-REQ-N2-005

Result label: **conditional theorem** request.

A first external blocking gap does not determine internal average spacing. Across the 31 finite blocked layers for `51<=n<=56`,

\[
\max\frac{g_t}{D_t}
=
\frac{6963896442939750}{6290170063344679}
<1.108.
\]

This is **computational evidence** only. The maximum occurs at `n=51`, layer `4`.

The required next theorem must control internal divisor spacing, average gaps, or the full span `U_t`, not only the first gap outside the connected prefix.

## Finite complete-core requirement

### N1-REQ-N4-008

Result label: **finite certificate** request.

Current exact coverage:

- Nova 2 `N2-FIN-202`: every `12<=n<=45`;
- Nova 1 `N1-FIN-005`: every `46<=n<=50`;
- Nova 1 `N1-FIN-006` through `N1-FIN-011`: `n=51` through `n=56`.

Therefore

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

Nova 4 must independently reconstruct:

1. exact rational certification of `r_n` and `M_n`;
2. factorial valuations and `Y_n`;
3. unique half-list product representation;
4. exact sorted row merge;
5. duplicate and omission rejection;
6. all thresholds, cutoffs, connected maxima, and `K_t` values;
7. the six-layer shortfall at `n=56`;
8. the seventh-layer no-block completion;
9. both explicit partition replays, masks `98` and `33`;
10. exact effective-factor and parity-span calculations;
11. term bound `24`;
12. fail-closed resource and integer boundaries.

Current artifacts:

- `proofs/EFFECTIVE_CARRIER_FACTORIZATION_RECONSTRUCTION.md`;
- `proofs/PARITY_SPAN_CRITERION_RECONSTRUCTION.md`;
- `verification/FULL_CORE_N56_REPORT.md`;
- `verification/full_core_n56_mitm_mask98.txt`;
- `verification/full_core_n56_mitm_mask33.txt`;
- `verification/test_mitm_n56_parity.py`.

The next finite target is `n=57`. Resource exhaustion must be recorded as unknown due to resource limits, never as mathematical failure.

## Collision requirement

### N1-REQ-N2-004

Result label: **conditional theorem** request.

`N1-COL-001` proves profile injectivity is false. The next required result is a target-local upper bound on maximum fiber size, additive energy, a second moment of representation counts, or weighted collision contribution under the exact tilted numerical law.

Raw global profile counts are not occupancy evidence.

## Nova 3 numerical-law requirement

### N1-REQ-N3-003

Result label: **conditional theorem** request.

Current accepted foundation closes unique finite tilt, exact span one, the exact torus resonance set, and a first-layer characteristic-function bound. The remaining nodes are compact tilt or quantitative phase dispersion, variance and higher-moment control, a positive reference lattice law, and a strict weighted Fourier inequality.

## Internal Track B requirement

### N1-REQ-N1-001

Result label: **conditional theorem** reconstruction request.

Reconstruct

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)=O((\log n)^2)
\Longrightarrow
h(n!)=O((\log n)^3)
\]

under the current endpoint convention.

## Closed structural requirements

- factorial valuation atlas;
- numerical distinctness;
- support lattice and correction residues;
- formal profile capacity;
- total endpoint reach;
- one-block ceiling;
- profile noninjectivity;
- exact divisor streams;
- count-surplus identity;
- effective carrier factorization;
- sharp parity-span baseline;
- exact complete-core coverage through `n=56`.

## Open structural requirements

- factorial-specific internal-span or average-gap control;
- effective count-utilization lower or upper bounds;
- exact finite extension beginning at `n=57`;
- uniform quotient downward-window occupancy;
- downward endpoint-window occupancy;
- target-local collision control;
- compact numerical tilt or phase dispersion;
- strict weighted Fourier positivity;
- Track B reconstruction;
- finite exceptions after an effective asymptotic threshold.

## Rule

No requirement may be weakened, strengthened, or reinterpreted silently. Any changed hypothesis, constant, endpoint, layer definition, or conclusion receives a new versioned requirement.
