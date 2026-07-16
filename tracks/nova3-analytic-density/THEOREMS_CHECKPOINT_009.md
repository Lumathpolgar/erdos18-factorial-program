# Nova 3 Theorem Registry Addendum: Checkpoint 009

This addendum is part of the Nova 3 theorem registry and should be read with `THEOREMS.md`.

## N3-ANA-029, exact low-state interval carrier

- Class: `proved theorem`
- For the transformed prefix choices
  \[
  \widetilde Z_1\in\{0,1\},
  \]
  and
  \[
  \widetilde Z_t\in
  \{0,2^{t-2},3\cdot2^{t-2}\}
  \quad(2\le t\le j),
  \]
  the ordinary sumset is exactly
  \[
  \{0,1,\ldots,3\cdot2^{j-1}-2\}.
  \]
- Consequence: this fixed legal carrier is surjective modulo `2^j`
- Proof: `proofs/PREFIX_RESIDUE_CARRIER_MASS.md`

## N3-ANA-030, uniform low-carrier mass collapse

- Class: `proved theorem`
- Define
  \[
  \delta_n
  =
  \max\left\{
  \frac{16M_n\log L_n}{L_n},
  \frac{32(n\log n+\log14)}{2^{M_n}}
  \right\},
  \]
  and
  \[
  R_n
  =
  \min\left(
  M_n,
  \left\lfloor
  2+\log_2\frac1{\delta_nm_n}
  \right\rfloor
  \right).
  \]
- Then
  \[
  R_n=M_n-O(\log n).
  \]
- Uniformly over every post-prefix target and every `1<=j<=R_n`:
  \[
  P(\mathcal C_{n,q,j})
  \le
  \frac{2e^2}{k_n}
  \left(
  \frac{3e^2}{k_n+1}
  \right)^{j-1}.
  \]
- At `j=R_n`, the logarithm of the carrier mass is `-Theta((log n)^3)`
- Proof: `proofs/PREFIX_RESIDUE_CARRIER_MASS.md`

## N3-ANA-031, support-surjectivity inference obstruction

- Class: `proved route obstruction`
- Disproved inference: full legal residue support modulo `2^j` is enough to establish quantitative prefix mixing
- Exact reason: the residue-complete fixed carrier has total tilted probability at most `exp(-Theta((log n)^3))` through `M_n-O(log n)` scales
- Boundary: this does not prove that the complete transformed prefix law is concentrated
- Required replacement: control full-menu residue weights, full-prefix characteristic functions, or another non-negligible carrier
- Proof: `proofs/PREFIX_RESIDUE_CARRIER_MASS.md`

## N3-FIN-009

- Exact interval-carrier and residue-surjectivity checks through `j=18`
- Verifier: `proofs/prefix_residue_carrier_sanity.py`

## N3-COMP-008

Selected symbolic-bound evaluations:

| `n` | `M_n` | `R_n` | excluded top scales | `log10` carrier-mass ceiling |
|---:|---:|---:|---:|---:|
| 120368 | 2190 | 2149 | 41 | `-7379.3651` |
| 200000 | 2384 | 2342 | 42 | `-8558.5329` |
| 500000 | 2756 | 2711 | 45 | `-10985.7758` |
| 1000000 | 3054 | 3007 | 47 | `-13090.4309` |

These rows are computational evidence supporting the symbolic theorem. They are not substitutes for proof.

## Open successor

`N3-NEXT-009`: estimate the full transformed odd-core residue weights modulo `2^j`, or prove a full-prefix characteristic bound in dyadic neighborhoods. A legal-support or fixed-carrier argument is no longer sufficient.

## Claim boundary

None of N3-ANA-029 through N3-ANA-031 proves transformed local-window positivity, the strict weighted Fourier inequality, quotient occupancy, the factorial half-range theorem, or Erdős Problem 18.