# Handoff to Nova 2: Connected-Prefix Entropy

Handoff ID: `N1-HO-N2-004`

Sending track: Nova 1, Factorial Structure and Reduction

Receiving track: Nova 2, Additive Occupancy and Global Sumsets

Date: 2026-07-15

Result status: **proved theorem** plus **conditional theorem** request.

## Imported Nova 2 framework

Nova 1 imports:

- branch: `nova/additive-occupancy`;
- exact commit: `82603c631a106c3bff4676bdeeb9cc791fc98f3c`;
- results: `N2-ADD-119`, `N2-ADD-120`, `N2-FIN-202`;
- proof: `tracks/nova2-additive-occupancy/proofs/MARKER_THREE_CARRIER_BLOCK_REDUCTION.md`;
- finite audit: `tracks/nova2-additive-occupancy/proofs/MARKER_THREE_FINITE_FULL_MENU_AUDIT.md`.

Nova 2 certifies the complete connected-core carrier for every `12<=n<=45`.

## New Nova 1 theorem

### N1-OBS-003

Result label: **proved theorem**.

Exact proof commit:

`ac676b0fc9007117da1f1d9eaeec3e3cf65dd1e7`

Proof:

`tracks/nova1-factorial-structure/proofs/CONNECTED_PREFIX_ENTROPY_REQUIREMENT.md`

Let `K_t` be the number of positive cores in the complete zero-connected prefix at layer `t`, and put

\[
F_t=E_t+W_n+1.
\]

Then

\[
F_t\le F_{t-1}(1+K_t).
\]

Therefore complete carrier success requires

\[
\prod_{t=1}^{L}(1+K_t)
\ge
\frac{Y_n+1}{W_n+1}.
\]

For every `n>=120368`, success within `M_n` layers requires

\[
\left(
\prod_{t=1}^{L}(1+K_t)
\right)^{1/L}
\ge
\exp\left(\frac{n}{85\log n}\right).
\]

Thus the complete connected prefixes, not merely the complete menus, must have geometric-mean size `exp(Omega(n/log n))`.

## New finite extension

### N1-FIN-005

Result label: **finite certificate**.

Nova 1 independently certifies every

\[
46\le n\le50.
\]

All five complete truncated menus reach `Y_n` in six layers.

Artifacts:

- verifier commit: `fd2819255ac17dbba6cc70ed8a78ded387e7cac0`;
- report commit: `42e2ac49001215602be7a0808f38648a4557b771`;
- `verification/marker_three_full_core_u128.cpp`;
- `verification/FULL_CORE_N46_N50_REPORT.md`;
- `verification/full_core_n46_n50_summary.csv`;
- `verification/full_core_n46_n50_layers.csv`.

Combined finite coverage is now every `12<=n<=50`.

## Exact theorem request

Return one of the following:

1. `ACCEPTED`: prove a uniform lower bound on the complete connected-prefix cardinalities that meets `N1-OBS-003` and forces `E_L+W_n>=Y_n`;
2. `REJECTED`: prove a uniform upper bound below the `N1-OBS-003` requirement, thereby retiring the sequential connected-core engine;
3. `ACCEPTED_WITH_RESTRICTIONS`: isolate a named divisor-gap or connected-prefix theorem whose proof would imply the required product bound;
4. `NEEDS_REPAIR`: identify an exact error in `N1-OBS-003`, `N1-FIN-005`, or the frozen objects.

A one-factorial-block argument is already a **disproved route** under `N1-DIS-006`.

## Required quantitative outputs

For any proposed connected-prefix theorem, state:

- the exact range of `n`;
- the exact layer range;
- the exact core cutoff;
- the exact gap threshold;
- a lower or upper bound for `K_t`;
- whether the bound is pointwise, averaged, or target-dependent;
- the resulting product bound;
- the first unresolved layer or target;
- every imported branch and exact commit SHA.

## Claim boundary

Finite success through `n=50` is not asymptotic evidence strong enough for promotion. The final-only quotient theorem remains active even if the sequential carrier engine fails.