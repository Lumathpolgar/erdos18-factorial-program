# N2-HO-N4-007: Independent Rankin Lower-Tail Reconstruction

## Exact source

- branch: `nova/additive-occupancy`;
- proof commit: `4b4272ca1b2d8fb0963fc377245f57f9b935f978`;
- verifier commit: `2561010b7b903e41d93681cec664312ff18315db`;
- proof: `proofs/RANKIN_SMOOTH_DIVISOR_SPAN.md`;
- verifier: `verification/rankin_smooth_divisor_sanity.py`.

## Reconstruct independently

1. For every `sigma>0`,
   \[
   Z_n(\sigma)=\sum_{d\mid C_n}d^{-\sigma}
   =\prod_{p^e\parallel C_n}\frac{1-p^{-(e+1)\sigma}}{1-p^{-\sigma}}.
   \]
2. Prove
   \[
   U_t\ge\left(\frac{K_t}{Z_n(\sigma)}\right)^{1/\sigma}.
   \]
3. Reconstruct the combined parity, Rankin, and complement-median carrier factor.
4. Replay the fixed decimal `sigma_t` rows for every layer at `51<=n<=55`.
5. Confirm every Rankin radius is below the exact connected maximum.
6. Confirm the recorded sixth-root and unrooted endpoint ratios.
7. Corrupt at least one prime exponent, one `K_t`, one `D_t`, one `sigma_t`, and one expected ratio, and verify fail-closed rejection.

## Expected finite rows

| `n` | sixth-root ratio | unrooted `log10` ratio |
|---:|---:|---:|
| 51 | `0.000542135786332180` | `-19.5953515442` |
| 52 | `0.000488608023294683` | `-19.8662364353` |
| 53 | `0.000443191288757114` | `-20.1204527074` |
| 54 | `0.000438131601230971` | `-20.1503725273` |
| 55 | `0.000374184125626777` | `-20.5614878456` |

## Decision labels

Return `ACCEPTED`, `REPAIRED`, or `REJECTED` separately for N2-ADD-127, N2-ADD-128, and N2-CMP-208.

## Separate finite request

Continue exact complete-core certification from `n=56`. Resource exhaustion remains fail-closed and is not a mathematical counterexample.

## Claim boundary

This package does not prove quotient occupancy, the factorial half-range theorem, or Erdos Problem 18.
