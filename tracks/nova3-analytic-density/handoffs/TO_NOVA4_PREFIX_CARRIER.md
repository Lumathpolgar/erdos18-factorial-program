# Nova 3 to Nova 4: Prefix Residue Carrier Audit

## Handoff ID

`N3-HO-N4-004`

## Source branch

`nova/analytic-density`

## Files

- proof: `tracks/nova3-analytic-density/proofs/PREFIX_RESIDUE_CARRIER_MASS.md`
- verifier: `tracks/nova3-analytic-density/proofs/prefix_residue_carrier_sanity.py`
- registry addendum: `tracks/nova3-analytic-density/THEOREMS_CHECKPOINT_009.md`

## Results requiring separate verdicts

### N3-ANA-029

Verify that the low-state prefix sumset is exactly

\[
[0,3\cdot2^{j-1}-2]\cap\mathbb Z
\]

for every `j>=1`, and therefore surjective modulo `2^j`.

Check the interval-overlap induction carefully.

### N3-ANA-030

Verify the absolute transformed-tilt envelope

\[
\delta_n
=
\max\left\{
\frac{16M_n\log L_n}{L_n},
\frac{32(n\log n+\log14)}{2^{M_n}}
\right\},
\]

and safe depth

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

Check:

\[
R_n=M_n-O(\log n),
\]

and the uniform event-mass bound

\[
P(\mathcal C_{n,q,j})
\le
\frac{2e^2}{k_n}
\left(
\frac{3e^2}{k_n+1}
\right)^{j-1}
\]

for every post-prefix target and every `j<=R_n`.

### N3-ANA-031

Return a separate verdict on the inference restriction:

> exact residue support of a fixed carrier does not establish quantitative prefix mixing when the carrier's total tilted probability is `exp(-Theta((log n)^3))`.

Confirm that the theorem does not claim concentration of the complete transformed prefix law.

## Verification

Run

```text
python3 tracks/nova3-analytic-density/proofs/prefix_residue_carrier_sanity.py
```

Return separate verdicts for:

- `N3-FIN-009`, exact interval and residue checks through `j=18`;
- `N3-COMP-008`, selected scale evaluations.

## Selected rows

| `n` | `M_n` | `R_n` | excluded top scales | `log10` carrier-mass ceiling |
|---:|---:|---:|---:|---:|
| 120368 | 2190 | 2149 | 41 | `-7379.3651` |
| 200000 | 2384 | 2342 | 42 | `-8558.5329` |
| 500000 | 2756 | 2711 | 45 | `-10985.7758` |
| 1000000 | 3054 | 3007 | 47 | `-13090.4309` |

## Adversarial checks

1. Verify that the first-coordinate carrier is `{0,1}`, not `{0,1,3}`.
2. Verify the indexing `2^{t-2}` for transformed layers.
3. Confirm that the three translated intervals overlap without a one-point gap.
4. Confirm that the full interval, not merely all residues, is obtained.
5. Check the factor of two from the transformed tilt.
6. Check that `m_n>=3` is used when bounding the `3a_t` carrier weight.
7. Check denominator cardinalities `k_n` and `k_n+1` separately.
8. Check the floor in `R_n` against the inequality `delta_n m_n 2^{t-2}<=1`.
9. Do not treat computational rows as proof.
10. Do not infer complete-prefix concentration from low-carrier mass collapse.

## Claim boundary

This audit does not authorize a claim of full-prefix mixing, transformed local-window positivity, quotient occupancy, the factorial half-range theorem, or Erdős Problem 18.