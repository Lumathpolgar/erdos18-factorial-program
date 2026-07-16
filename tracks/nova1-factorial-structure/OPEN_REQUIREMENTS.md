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

and quotient layers

\[
B_t(n)=
\{2^{t-1}u:u\text{ odd},\ 3u\mid n!,\ 2^{t-1}u\le Y_n\},
\]

prove that an absolute `n_0` exists such that every integer

\[
W_n+1\le q\le Y_n
\]

has a legal rainbow sum in `[q-W_n,q]`, using at most one nonzero term from each layer.

The structural model is accepted with restrictions by Nova 2. Global occupancy remains open.

## Exact carrier factorization requirement

### N1-REQ-N2-006

Result label: **conditional theorem** request.

Imported and independently reconstructed sources:

- `N2-ADD-122` from `nova/additive-occupancy@2ab09dd980f7116b82530368e3d98bb53240bf0c`;
- `N2-ADD-124` and `N2-OBS-110` from `nova/additive-occupancy@47ed3938d8900c82b245a3592502ac957330bbc6`;
- Nova 1 results `N1-STR-025`, `N1-STR-026`, and `N1-OBS-004`.

For executed layers,

\[
F_t=F_{t-1}+s_tU_t,
\qquad
s_t=2^{t-1},
\qquad
P_n=\prod_{t=1}^{L}(1+K_t),
\]

\[
b_t=\frac{1+s_tU_t/F_{t-1}}{1+K_t}.
\]

Then exactly

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

Accepted outcomes are:

1. a **proved theorem** giving a uniform effective-product lower bound;
2. a **proved theorem** giving an eventual or infinite upper obstruction that retires the sequential engine;
3. a **conditional theorem** reducing the effective product to a precise factorial-divisor spacing theorem;
4. an exact counterexample with a replayable certificate.

## Factorial-specific span requirement

### N1-REQ-N2-007

Result label: **conditional theorem** request.

For every executed layer define

\[
A_t=\frac{U_t}{2K_t-1},
\qquad
\eta_t=\frac{U_t}{K_tD_t}.
\]

`N1-STR-026` proves the universal parity baseline `A_t>=1`. `N1-OBS-004` proves no fixed improvement is possible using only oddness, `K_t`, and `D_t`.

Prove one of:

1. a factorial-specific lower bound for enough `A_t` or `eta_t` to force `Delta_n>=1`;
2. an averaged internal-gap theorem for divisors of
   \[
   D_n=\frac{n!}{3\cdot2^{v_2(n!)}}
   \]
   strong enough to close the carrier;
3. a factorial-specific upper obstruction showing the required amplification fails eventually or infinitely often.

Finite data through `n=57` are **computational evidence** only. At `n=57`, the parity-only endpoint product misses by about `2.82e32`, while factorial-specific spacing restores endpoint success.

## External blocking-gap boundary

### N1-REQ-N2-005

Result label: **conditional theorem** request.

The finite candidate

\[
g_t/D_t<1.108
\]

is a **disproved route**. At `n=57`, layer `3`,

\[
D_3=2{,}911{,}465{,}312{,}076,
\qquad
g_3=3{,}399{,}069{,}458{,}070,
\]

so

\[
g_3/D_3=1.1674772300983786\ldots.
\]

A first external blocking gap does not identify the internal average spacing. Any future gap theorem must directly control `U_t`, `A_t`, `eta_t`, or an equivalent effective-product quantity.

## Finite overflow-safe carrier requirement

### N1-REQ-N4-008

Result label: **finite certificate** request.

Current exact coverage:

- Nova 2 `N2-FIN-202`: every `12<=n<=45`;
- Nova 1 `N1-FIN-005`: every `46<=n<=50`;
- Nova 1 `N1-FIN-006` through `N1-FIN-012`: every `51<=n<=57`.

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
\qquad(12\le n\le57).
\]

Nova 4 must independently reconstruct:

1. exact rational certification of `r_n` and `M_n`;
2. factorial valuations and `Y_n`;
3. endpoint-truncated half lists;
4. division-based overflow guards;
5. unique product representation and exact sorted merge;
6. deterministic checkpoint serialization and continuation;
7. duplicate, omission, stale-cache, and corrupted-checkpoint rejection;
8. every layer threshold, connected maximum, count, and blocking gap;
9. effective, parity, and factorial-span diagnostics;
10. two distinct explicit partition replays;
11. overflow-safe regression for `52<=n<=56`;
12. fail-closed resource and integer boundaries.

Authoritative artifacts:

- `proofs/OVERFLOW_SAFE_CHECKPOINTED_MITM_STREAM.md`;
- `verification/marker_three_mitm_checkpoint_u128.cpp`;
- `verification/OVERFLOW_SAFE_REGRESSION_N52_N56.md`;
- `verification/FULL_CORE_N57_REPORT.md`;
- `verification/full_core_n57_safe_mask6.txt`;
- `verification/full_core_n57_safe_mask424.txt`;
- `verification/test_mitm_n57_overflow_safe.py`.

The retired `marker_three_mitm_prefix_u128.cpp` must fail closed. The next finite target is `n=58`.

## Collision requirement

### N1-REQ-N2-004

Result label: **conditional theorem** request.

`N1-COL-001` supplies a fiber of size at least

\[
2^{\lfloor M_n/2\rfloor}.
\]

The next required result is a target-local upper bound on maximum fiber size, additive energy, representation-count second moments, or weighted collision contribution under the exact tilted numerical-value law.

## Nova 3 numerical-law requirement

### N1-REQ-N3-003

Result label: **conditional theorem** request.

Current accepted foundation:

- exact head inspected: `003b9c0e1179314d6c119c8a356e0f41231e3ad6`;
- results: `N3-ANA-017`, `N3-ANA-018`, `N3-ANA-019`;
- outcome: `ACCEPTED_WITH_RESTRICTIONS`.

Closed clauses include unique finite tilt, exact span one, exact torus resonance set `{0}`, and an explicit first-layer characteristic bound.

Open clauses are compact target-dependent tilt or direct phase dispersion, moment control, a positive reference lattice law, and a strict weighted Fourier inequality.

## Internal Track B requirement

### N1-REQ-N1-001

Result label: **conditional theorem** reconstruction request.

Reconstruct

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)=O((\log n)^2)
\Longrightarrow
h(n!)=O((\log n)^3)
\]

under the current frozen endpoint convention.

## Closed structural requirements

- factorial valuation atlas;
- numerical distinctness and correction palette;
- support lattice and residues;
- direct first-target and total endpoint reach;
- profile-capacity and prime-interval thresholds;
- one-block obstruction and profile noninjectivity;
- connected-prefix count necessity;
- unique-parent and meet-in-the-middle streams;
- exact count-utilization factorization;
- sharp parity-span baseline and optimality;
- overflow-safe truncation and exact checkpoint continuation;
- exact complete-core coverage through `n=57`.

## Open structural requirements

- factorial-specific internal span or normalized average-gap theorem;
- uniform effective-product lower or upper bound;
- exact overflow-safe finite extension from `n=58`;
- quotient maximum downward gap at most `W_n`;
- downward endpoint-window occupancy;
- target-local collision control;
- compact numerical tilt or direct phase dispersion;
- strict weighted bounded-torus Fourier inequality;
- Track B reconstruction;
- finite exceptions after an effective asymptotic threshold.

## Rule

No requirement may be weakened, strengthened, or reinterpreted silently. Any changed hypothesis, constant, endpoint, layer definition, or conclusion receives a new versioned requirement.
