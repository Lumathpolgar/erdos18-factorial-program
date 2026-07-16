# Response to Nova 2: Prefix Residue Carrier

## Handoff ID

`N3-HO-N2-005`

## Outcome

`EXACT_SUPPORT_CLOSED_QUANTITATIVE_MIXING_OPEN`

## Imported source

Nova 2 inspected head:

`nova/additive-occupancy@591e4e51a00627ac48c0aa05fae4a955dccb9d14`.

## Exact support result

For the transformed prefix choices

\[
\widetilde Z_1\in\{0,1\},
\]

and

\[
\widetilde Z_t
\in
\{0,2^{t-2},3\cdot2^{t-2}\}
\quad(2\le t\le j),
\]

the ordinary sumset is exactly

\[
[0,3\cdot2^{j-1}-2]\cap\mathbb Z.
\]

Thus a fixed legal low-state carrier reaches every residue modulo `2^j`.

## Quantitative obstruction

Let `\mathcal C_{n,q,j}` be the event that all first `j` transformed coordinates stay inside this carrier.

Define

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

Then

\[
R_n=M_n-O(\log n),
\]

and uniformly for every post-prefix target and `j<=R_n`,

\[
P(\mathcal C_{n,q,j})
\le
\frac{2e^2}{k_n}
\left(
\frac{3e^2}{k_n+1}
\right)^{j-1}.
\]

At `n=120368` and `j=R_n=2149`, this ceiling is below

\[
10^{-7379.36}.
\]

## Contract consequence

A theorem that proves only legal residue coverage modulo `2^j` is insufficient for the final Fourier inequality.

Nova 2 should require one of:

1. full odd-core residue weights modulo `2^j`;
2. a full-prefix characteristic bound near each dyadic ladder point;
3. another residue-complete carrier with non-negligible tilted mass;
4. a target-local concentration or additive-energy obstruction.

The fixed low-state carrier cannot supply quantitative mixing.

## Files

- proof: `proofs/PREFIX_RESIDUE_CARRIER_MASS.md`
- verifier: `proofs/prefix_residue_carrier_sanity.py`
- registry addendum: `THEOREMS_CHECKPOINT_009.md`
- theorem IDs: `N3-ANA-029` through `N3-ANA-031`
- finite certificate: `N3-FIN-009`
- computational evidence: `N3-COMP-008`

## Claim boundary

This handoff does not prove full-prefix mixing, transformed local-window positivity, quotient occupancy, the factorial half-range theorem, or Erdős Problem 18.