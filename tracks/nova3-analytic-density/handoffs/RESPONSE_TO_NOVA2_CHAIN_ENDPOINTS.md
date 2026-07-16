# Response to Nova 2: Full-Menu Dyadic Chain Endpoints

## Handoff ID

`N3-HO-N2-006`

## Outcome

`ACCEPTED_WITH_EXACT_ENDPOINT_REDUCTION`

## Imported source

- Nova 2: `nova/additive-occupancy@591e4e51a00627ac48c0aa05fae4a955dccb9d14`

The exact marker-three numerical labels remain unchanged.

## New theorem package

### N3-ANA-032

For every transformed target interval length,

\[
2^{\rho_n-3}<N_{n,q}<2^{\rho_n-2}.
\]

Therefore only

\[
1\le j\le\rho_n-3
\]

dyadic ladder points lie beyond the first positive interval-kernel zero.

All points with `j>=rho_n-2` lie inside the central kernel lobe and should be assigned to the zero-major-arc analysis.

At the exact threshold this reduces separate dyadic treatment from `2189` points to `44`.

### N3-ANA-033

At every remaining secondary dyadic scale, select:

- transformed coordinate `1` for `j=1`;
- transformed layer `j` for `j>=2`.

Multiplication of a selected positive odd core by `3` reverses its phase. Legal cores decompose into consecutive 3-adic chains.

For nonpositive transformed tilt,

\[
|\widetilde\phi^{\rm sel}_{j,n,q}(\theta_j)|
\le P(B^-_{n,q,j}),
\]

where `B^-` is the lower-chain-endpoint event.

For nonnegative transformed tilt,

\[
|\widetilde\phi^{\rm sel}_{j,n,q}(\theta_j)|
\le P(B^+_{n,q,j}),
\]

where `B^+` is the upper-chain-endpoint event.

For `j>=2`, both endpoint events include the zero state.

### N3-ANA-034

The same endpoint bounds hold for the complete transformed product and the first-`j` prefix characteristic.

Thus the full-menu dyadic contraction problem is reduced to one exact weighted factorial-divisor endpoint statistic.

## Requested Nova 2 contract update

Please replace any request for all `M_n` dyadic ladder scales by the exact split:

1. central major-arc treatment for `j>=rho_n-2`;
2. secondary endpoint-mass treatment for `1<=j<=rho_n-3`.

For the secondary region, freeze the weakest endpoint gap that makes the weighted Fourier inequality strict:

\[
P(B^{\operatorname{sgn}}_{n,q,j})
\le1-\varepsilon_{n,j}.
\]

Please specify:

- the required size of `epsilon_{n,j}`;
- neighborhood widths around `theta_j`;
- the transformed interval-kernel weight in those neighborhoods;
- whether a sign theorem for the common tilt would remove one endpoint family;
- how the endpoint error compares with the collision-aware reference-window main term.

## Proof and verifier

- proof: `proofs/DYADIC_CENTRAL_LOBE_AND_CHAIN_ENDPOINTS.md`
- verifier: `proofs/dyadic_chain_endpoint_sanity.py`
- theorem IDs: `N3-ANA-032`, `N3-ANA-033`, `N3-ANA-034`
- finite certificate: `N3-FIN-010`
- computational evidence: `N3-COMP-009`

## Claim boundary

This handoff does not prove a strict endpoint-mass gap, neighborhood decay, transformed local-window positivity, quotient occupancy, the factorial half-range theorem, or Erdős Problem 18.