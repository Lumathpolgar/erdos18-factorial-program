# Nova 3 Theorem Registry Addendum: Checkpoint 010

The factorial half-range theorem and Erdős Problem 18 remain open.

## N3-ANA-032, exact dyadic central-lobe cutoff

- Class: `proved theorem`
- For every transformed target interval length `N_{n,q}`:
  \[
  2^{\rho_n-3}<N_{n,q}<2^{\rho_n-2}.
  \]
- Therefore dyadic points
  \[
  \theta_j=2\pi/2^j
  \]
  satisfy:
  - `1<=j<=rho_n-3`: beyond the first positive interval-kernel zero;
  - `j>=rho_n-2`: inside the interval kernel's central lobe.
- Consequence: only `rho_n-3=O(log n)` dyadic scales require separate secondary-frequency treatment.
- Proof: `proofs/DYADIC_CENTRAL_LOBE_AND_CHAIN_ENDPOINTS.md`

## N3-ANA-033, exact selected-layer 3-adic chain contraction

- Class: `proved theorem`
- At every secondary dyadic scale, select:
  - transformed coordinate `1` when `j=1`;
  - transformed layer `t=j` when `j>=2`.
- Multiplying a positive odd core by `3` reverses the selected phase.
- Legal odd cores decompose into consecutive 3-adic exponent chains.
- If the transformed tilt is nonpositive:
  \[
  |\widetilde\phi^{\rm sel}_{j,n,q}(\theta_j)|
  \le P(B^-_{n,q,j}),
  \]
  where `B^-` is the lower 3-adic endpoint event, including zero for `j>=2`.
- If the transformed tilt is nonnegative:
  \[
  |\widetilde\phi^{\rm sel}_{j,n,q}(\theta_j)|
  \le P(B^+_{n,q,j}),
  \]
  where `B^+` is the upper 3-adic endpoint event, including zero for `j>=2`.
- Proof: `proofs/DYADIC_CENTRAL_LOBE_AND_CHAIN_ENDPOINTS.md`

## N3-ANA-034, full-product endpoint-mass reduction

- Class: `proved theorem and exact criterion`
- For every `1<=j<=rho_n-3`:
  \[
  |\widetilde\Phi_{n,q}(\theta_j)|
  \le P(B^-_{n,q,j})
  \quad\text{when }\widetilde\lambda_{n,q}\le0,
  \]
  and
  \[
  |\widetilde\Phi_{n,q}(\theta_j)|
  \le P(B^+_{n,q,j})
  \quad\text{when }\widetilde\lambda_{n,q}\ge0.
  \]
- The same inequalities hold for the first-`j` prefix characteristic.
- Consequence: the complete dyadic full-menu problem is reduced to a weighted lower- or upper-endpoint statistic on one selected factorial-divisor layer.
- Boundary: no strict endpoint-mass gap is yet proved.
- Proof: `proofs/DYADIC_CENTRAL_LOBE_AND_CHAIN_ENDPOINTS.md`

## N3-FIN-010

- Exact transformed supports for `n in {12,15,18}`.
- Checks:
  - transformed interval central-lobe cutoff;
  - consecutive 3-adic chains;
  - exact phase alternation under multiplication by `3`;
  - nonpositive-tilt lower-endpoint bound;
  - nonnegative-tilt upper-endpoint bound.
- Verifier: `proofs/dyadic_chain_endpoint_sanity.py`

## N3-COMP-009

Selected scale counts:

| `n` | `rho_n` | `M_n` | secondary dyadic scales | dyadic points inside central lobe |
|---:|---:|---:|---:|---:|
| 120368 | 47 | 2190 | 44 | 2145 |
| 200000 | 49 | 2384 | 46 | 2337 |
| 500000 | 53 | 2756 | 50 | 2705 |
| 1000000 | 56 | 3054 | 53 | 3000 |

These rows are computational evidence for the exact formulas.

## Promotion rule

N3-ANA-032 through N3-ANA-034 do not prove a strict dyadic contraction. Promotion to a transformed weighted Fourier theorem requires a target-uniform bound on the sign-appropriate 3-adic endpoint mass, a neighborhood-stable version, and comparison with the collision-aware reference-window main term.