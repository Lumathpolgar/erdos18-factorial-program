# Nova 3 Status

## Track

Analytic Divisor Density

## Branch

`nova/analytic-density`

## Baseline

- Starting branch head: `c79cddee6e8940e27ff256c29a85a3fc93766f7b`
- Main head inspected: `68ace6c9c3b67636e298a406fee3bfe8e072741d`
- Merge base: `cd5576d4f7934e26e9d4ef3b065c2ad4cee36c67`
- Startup relation: branch was already divergent, four commits ahead of the merge base and twelve commits behind main
- No rebase, force-push, merge into main, or edit to another Nova branch was performed

## Overall state

`FIRST_SUBSTANTIVE_CHECKPOINT_COMPLETE`

The main problem and the direct factorial half-range theorem remain open.

## Proved results

| ID | Result class | Statement | Proof location |
|---|---|---|---|
| N3-ANA-004 | proved theorem | Exact independent exponent model, moments, saddle parameter, and exponential tilt | `proofs/PRODUCT_MODEL_THEOREMS.md` |
| N3-ANA-005 | proved theorem | Exact uniform local-count ceiling by conditioning on one prime exponent | `proofs/PRODUCT_MODEL_THEOREMS.md` |
| N3-ANA-006 | proved theorem | Full uniform log-divisor model converges to a non-Gaussian infinite convolution | `proofs/PRODUCT_MODEL_THEOREMS.md` |
| N3-ANA-008 | proved theorem | High-prime tail central limit theorem after a cutoff tending to infinity | `proofs/PRODUCT_MODEL_THEOREMS.md` |

## Conditional result

| ID | Result class | Statement | Dependency |
|---|---|---|---|
| N3-ANA-009 | conditional theorem | Coarse central-window lower bound for the high-prime tail when `Delta >= K M_{n,y}` | Classical Berry-Esseen inequality, audited as N3-SRC-003 |

## Disproved estimate

| ID | Result class | Statement | Proof location |
|---|---|---|---|
| N3-ANA-007 | disproved estimate | No fixed-`n` characteristic function can satisfy a uniform bound below one on every sufficiently large frequency | `proofs/PRODUCT_MODEL_THEOREMS.md` |

The desired full-vector Gaussian local-limit route is also disproved by N3-ANA-006.

## Finite certificate and computational evidence

- Result class: finite certificate
- Range: every integer `2<=n<=12`
- Verified: divisor uniqueness, exact `tau(n!)`, complement symmetry, exact log-mean and variance formulas, and the local-count ceiling on a deterministic window grid
- Command: `python3 tracks/nova3-analytic-density/proofs/scale_sanity.py`

The same script prints larger convergence tables through `n=10000`. Those tables are result class `computational evidence`, not asymptotic proof.

## Candidate theorem contracts

| Candidate | Current disposition |
|---|---|
| Local logarithmic divisor count | open; exact tilted-window lower bound missing |
| Tilted local limit | open in fine windows; coarse substitute proved conditionally |
| Characteristic-function minor arc | unrestricted form disproved; bounded-frequency form open |

## Preferred route

Condition on or enumerate low-prime exponent coordinates, then use a growing high-prime tail as the diffuse tilted factor. This is recorded in `PREFERRED_ROUTE.md`.

## Source audit

Accepted external inputs:

- Robbins' explicit Stirling bounds
- Prime number theorem
- Berry-Esseen inequality for independent summands

Rejected for direct exact-factorial lower bounds:

- Ford's count of integers having a divisor in an interval
- almost-all friable divisor Gaussian laws
- ultrafriable arithmetic-progression estimates with common prime-power caps

Method-only source:

- weighted Bernoulli local-limit characteristic-function methods

Full legal directions are in `SOURCE_LEDGER.md`.

## Exact blockers

1. No uniform tilted lower-window theorem for the exact factorial divisor model in the widths required by additive occupancy.
2. No bounded-frequency phase-dispersion theorem for a high-prime band.
3. Nova 1 has not frozen a structural target band and minimum count.
4. Nova 2 has not frozen a probability measure, Fourier variable, inversion cutoff, and required main-term scale.
5. The archived Phase 12L and Phase 12P source packages are not inside the repository, so their small-divisor lemmas cannot be reconstructed beyond the repository summaries.
6. The branch was already divergent from main. A fast-forward update was impossible, while rebasing would require prohibited history rewriting.

## Handoffs

- `handoffs/TO_NOVA1.md`
- `handoffs/TO_NOVA2.md`
- `handoffs/TO_NOVA4.md`

## Next theorem target

`N3-NEXT-001`: after Nova 2 supplies an exact bounded inversion range, prove an averaged high-prime minor-arc estimate under a compact tilt, or prove a resonance obstruction showing that the requested error cannot be below the intended local main term.
