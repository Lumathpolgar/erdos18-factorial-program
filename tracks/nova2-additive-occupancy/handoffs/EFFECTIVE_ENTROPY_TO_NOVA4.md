# Effective Carrier Entropy Handoff to Nova 4

Handoff ID: `N2-HO-N4-005`

Result status: **proved theorem plus finite-certificate intake**.

## Frozen sources

Nova 2:

- branch: `nova/additive-occupancy`;
- theorem: `N2-ADD-122`;
- proof: `proofs/EFFECTIVE_CARRIER_ENTROPY_FACTORIZATION.md`;
- sanity check: `verification/effective_carrier_entropy_sanity.py`.

Nova 1 finite source:

- branch: `nova/factorial-structure`;
- exact inspected commit: `a6bdab1b917f3b3688f5a0c86e80c8a026bfbc07`;
- results: `N1-STR-023`, `N1-STR-024`, `N1-FIN-006`, `N1-FIN-007`, `N1-FIN-008`.

## Exact theorem to reconstruct

For `F_t=E_t+W_n+1`, `s_t=2^{t-1}`, connected maximum `U_t`, and positive prefix count `K_t`, define

\[
a_t=\frac{s_tU_t}{F_{t-1}},
\qquad
b_t=\frac{1+a_t}{1+K_t}.
\]

Then

\[
\frac{F_L}{W_n+1}
=
\left(\prod_t(1+K_t)\right)
\left(\prod_tb_t\right).
\]

Exact endpoint success is equivalent to

\[
\left(\prod_t(1+K_t)\right)
\left(\prod_tb_t\right)
\ge
\frac{Y_n+1}{W_n+1}.
\]

Return separate verdicts for:

1. exact algebraic factorization;
2. bounds `0<b_t<=1`;
3. relation to average-gap utilization;
4. count surplus versus true endpoint surplus;
5. finite values at `n=51,52,53`.

## Finite boundary

Accepted exact certificates give

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le22
\qquad(12\le n\le53).
\]

The smallest unaudited finite parameter is `n=54`.

Independently replay the meet-in-the-middle stream, dual-partition agreement at `n=53`, and extend from `n=54`. Resource limits must remain fail-closed.

## Claim boundary

Count surplus alone is not a sufficient endpoint theorem. Finite success through `n=53` does not prove uniform occupancy or Erdos Problem 18.
