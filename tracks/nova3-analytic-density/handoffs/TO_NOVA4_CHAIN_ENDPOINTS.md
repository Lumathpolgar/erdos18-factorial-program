# Nova 3 to Nova 4: Dyadic Central-Lobe and Chain-Endpoint Audit

## Handoff ID

`N3-HO-N4-005`

## Source branch

`nova/analytic-density`

## Primary artifacts

- proof: `tracks/nova3-analytic-density/proofs/DYADIC_CENTRAL_LOBE_AND_CHAIN_ENDPOINTS.md`
- verifier: `tracks/nova3-analytic-density/proofs/dyadic_chain_endpoint_sanity.py`

## Imported heads used by Nova 3

- Nova 1: `nova/factorial-structure@8c7ee8f64af56a8d082f1fa3adabb0b0309f6e27`
- Nova 2: `nova/additive-occupancy@591e4e51a00627ac48c0aa05fae4a955dccb9d14`

## Required verdicts

### N3-ANA-032

Verify

\[
2^{\rho_n-3}<N_{n,q}<2^{\rho_n-2}
\]

for every transformed target parity, and verify the exact first-kernel-zero split:

- secondary dyadic scales: `1<=j<=rho_n-3`;
- central-lobe dyadic scales: `j>=rho_n-2`.

Check the ladder count uses `M_n-1`, not `M_n`, total dyadic points.

### N3-ANA-033

Verify the selected-coordinate construction:

- coordinate `1` for `j=1`;
- layer `j` for `j>=2`.

Verify multiplication by `3` reverses the selected phase in both cases.

Verify every legal positive core set decomposes into consecutive 3-adic exponent chains.

Verify the sign-dependent alternating-chain inequalities:

\[
|\widetilde\phi^{\rm sel}(\theta_j)|
\le P(B^-)
\quad\text{for nonpositive tilt},
\]

\[
|\widetilde\phi^{\rm sel}(\theta_j)|
\le P(B^+)
\quad\text{for nonnegative tilt}.
\]

### N3-ANA-034

Verify transfer from the selected coordinate to the prefix characteristic and full transformed product by the modulus-one ceiling on every other factor.

Return a separate verdict on the claim that this is a full-menu weighted reduction rather than a fixed-carrier argument.

### N3-FIN-010

Run

```text
python3 tracks/nova3-analytic-density/proofs/dyadic_chain_endpoint_sanity.py
```

The verifier should check `n in {12,15,18}`, target parities, tilts `-1e-4`, `0`, and `1e-4`, exact chain reconstruction, endpoint inequalities, and selected large-scale counts.

### N3-COMP-009

Reconstruct:

| `n` | `rho_n` | `M_n` | secondary scales | central-lobe ladder points |
|---:|---:|---:|---:|---:|
| 120368 | 47 | 2190 | 44 | 2145 |
| 200000 | 49 | 2384 | 46 | 2337 |
| 500000 | 53 | 2756 | 50 | 2705 |
| 1000000 | 56 | 3054 | 53 | 3000 |

## Adversarial checks

1. Count the ladder as `j=1,...,M_n-1`.
2. Do not confuse kernel nonvanishing with being outside the central lobe.
3. Verify the first transformed coordinate separately at `j=1`.
4. Include the zero state for selected layers `j>=2`.
5. Check cutoff legality makes every 3-adic exponent set consecutive from zero.
6. Use transformed tilt `2lambda`, not the original tilt.
7. Reverse the alternating chain for nonnegative tilt.
8. Do not infer a strict contraction without a strict endpoint-mass gap.
9. Do not replace weighted endpoint probability by endpoint support count.
10. Do not claim neighborhood control from a pointwise theorem.

## Required response format

Return separate decisions for:

- `N3-ANA-032`;
- `N3-ANA-033`;
- `N3-ANA-034`;
- `N3-FIN-010`;
- `N3-COMP-009`.

Use accepted, rejected, or accepted with correction for each item.

## Claim boundary

This audit does not authorize a claim of strict dyadic contraction, transformed local-window positivity, quotient occupancy, the factorial half-range theorem, or a solution of Erdős Problem 18.