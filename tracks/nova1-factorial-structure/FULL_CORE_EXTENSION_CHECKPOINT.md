# Full-Core Extension and Connected-Prefix Entropy Checkpoint

## Checkpoint status

Result status: **proved theorem** plus **finite certificate**.

The factorial half-range theorem remains open.

Current branch:

`nova/factorial-structure`

## Imported Nova 2 result

Nova 2 completed the exact full-menu carrier audit through `n=45` at:

- branch: `nova/additive-occupancy`;
- exact commit: `82603c631a106c3bff4676bdeeb9cc791fc98f3c`;
- result: `N2-FIN-202`;
- classification: **finite certificate**;
- proof: `tracks/nova2-additive-occupancy/proofs/MARKER_THREE_FINITE_FULL_MENU_AUDIT.md`.

Every `12<=n<=45` reaches the complete quotient endpoint using two through six main layers.

## New Nova 1 proved theorem

### N1-OBS-003: connected-prefix entropy requirement

Let `K_t` be the number of positive odd cores in the complete zero-connected prefix at carrier layer `t`. If

\[
F_t=E_t+W_n+1,
\]

then

\[
F_t\le F_{t-1}(1+K_t).
\]

Hence complete carrier success after `L` layers requires

\[
\prod_{t=1}^{L}(1+K_t)
\ge
\frac{Y_n+1}{W_n+1}.
\]

For every `n>=120368`, success using at most `M_n` layers therefore requires

\[
\left(\prod_{t=1}^{L}(1+K_t)\right)^{1/L}
\ge
\exp\left(\frac{n}{85\log n}\right).
\]

This is a necessary condition for the sequential connected-core engine, not a sufficient condition and not a statement about the full final-only rainbow sumset.

Proof:

`proofs/CONNECTED_PREFIX_ENTROPY_REQUIREMENT.md`

## New Nova 1 finite certificate

### N1-FIN-005

Nova 1 independently generated complete truncated odd-core menus and replayed the exact carrier recursion for every

\[
46\le n\le50.
\]

All five cases reach the complete quotient endpoint in six layers.

At `n=50`:

- `r_n=16`;
- `M_n=245`;
- `v_2(50!)=47`;
- total odd-core divisors: `88,957,440`;
- generated cores not exceeding `Y_50`: `78,715,976`;
- quotient endpoint:
  `58,132,122,695,453,537,232,069,776,546,341`;
- occupied through:
  `58,136,587,048,292,518,061,385,718,647,169`;
- exact margin:
  `4,464,352,838,980,829,594,210,082,828`;
- main layers used: `6`;
- total divisor-term bound after correction: `22`.

Verification:

- `verification/marker_three_full_core_u128.cpp`;
- `verification/FULL_CORE_N46_N50_REPORT.md`;
- `verification/full_core_n46_n50_summary.csv`;
- `verification/full_core_n46_n50_layers.csv`.

Combined with Nova 2 `N2-FIN-202`, the exact complete-core carrier is now certified for every

\[
12\le n\le50.
\]

This is finite only.

## What changed structurally

The previous checkpoint proved that one factorial arithmetic block per layer is asymptotically insufficient.

The complete-menu data now proves that this obstruction cannot be promoted to the full connected core. At `n=46`, the complete first-layer connected component exceeds the one-block envelope by a factor greater than `99`.

Thus the current structural alternatives are:

1. prove that the complete factorial divisor menu has connected prefixes of size `exp(Omega(n/log n))` under the exact thresholds;
2. prove that it cannot have those prefixes, thereby retiring the sequential engine;
3. bypass the sequential engine with the final-only numerical additive theorem.

## Exact open nodes

1. Prove or disprove a uniform connected-prefix lower bound meeting `N1-OBS-003`.
2. Extend exact complete-menu verification beyond `n=50` with a lower-memory sorted divisor generator.
3. Prove or disprove the full quotient downward-window theorem.
4. Prove the final endpoint window, not merely total endpoint support.
5. Upper-bound target-local collision energy after the exact carry-collision lower bound.
6. Complete the target-dependent numerical Fourier theorem.
7. Reconstruct Track B under current endpoints.
8. Handle finite exceptions only after an effective asymptotic threshold exists.

## Claim boundary

No asymptotic occupancy claim is made. The marker-three construction remains a **heuristic** complete route with proved structural components, a conditional reduction, exact finite certificates, and recorded disproved subroutes.