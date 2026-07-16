# Handoff to Nova 4: Parity Twin and Odd-Lattice Audit

Handoff ID: `N3-HO-N4-004`

Sending track: Nova 3, Analytic Divisor Density

Receiving track: Nova 4, Computational Verification

Date: 2026-07-15

Result status: independent reconstruction request

Theorem IDs: `N3-ANA-023`, `N3-ANA-024`, `N3-ANA-025`

Finite ID: `N3-FIN-007`

## Exact source

- branch: `nova/analytic-density`
- proof: `tracks/nova3-analytic-density/proofs/PARITY_TWIN_AND_ODD_REDUCTION.md`
- verifier: `tracks/nova3-analytic-density/proofs/parity_twin_sanity.py`

Imported heads used by the proof:

- Nova 1: `1b81ec74f907d57d520bcf6c51f2e6e71f0474a7`
- Nova 2: `e443674f86b2ee3c7037ac94ee47f6b8a4b3b29f`

## Audit duties

Independently verify all of the following.

1. Every nonzero first-layer quotient state is odd and every later-layer quotient state is even.
2. For the post-prefix tilt,
   \[
   p^{(0)}_{n,q}\le\frac{2e^{\varepsilon_n}}{m_n+1},
   \qquad
   \varepsilon_n=\frac{8M_n\log L_n}{2^{M_n}-1}.
   \]
3. The exact parity law
   \[
   P(T\text{ even})=p^{(0)}_{n,q}.
   \]
4. The exact nonzero-frequency value
   \[
   \Phi(\pi)=2p^{(0)}-1.
   \]
5. The exact twin identity
   \[
   \Phi(\pi+u)+\Phi(u)
   =2p^{(0)}\prod_{t>=2}\phi_t(u).
   \]
6. The dispersion identity at `pi` and its collapse to zero uniformly in the post-prefix range.
7. The total-variation parity mismatch lower bound for arbitrary integer reference laws.
8. Independence of transformed coordinates after conditioning on `Z_1!=0`.
9. The exact transformed common tilt `2 lambda`.
10. The exact transformed target interval
    \[
    J_{n,q}
    =
    \left[
    \left\lceil\frac{q-W_n-1}{2}\right\rceil,
    \left\lfloor\frac{q-1}{2}\right\rfloor
    \right]\cap\mathbb Z.
    \]
11. The transformed first support contains `0` and `1`, so its exact span is one.
12. The proof does not claim all secondary resonances disappear after normalization.

## Adversarial tests

Test at least:

- both positive and negative tilts;
- `u=0`, frequencies near zero, and generic nonzero `u`;
- both parities of `q` and `W_n` in the target-window map;
- corrupted supports containing an even first-layer state;
- corrupted later supports containing an odd state;
- a reference law with half its mass on even integers;
- whether any statement silently upgrades total-variation obstruction to failure of the weighted window inequality.

## Verification command

```text
python3 tracks/nova3-analytic-density/proofs/parity_twin_sanity.py
```

## Required verdict

Return one of:

- `ACCEPTED`;
- `ACCEPTED_WITH_RESTRICTIONS`;
- `NEEDS_REPAIR`;
- `REJECTED`.

Include exact branch, commit SHA, commands, and the first failed identity if any.

## Claim boundary

This request does not claim quotient occupancy, the factorial half-range theorem, or Erdős Problem 18.
