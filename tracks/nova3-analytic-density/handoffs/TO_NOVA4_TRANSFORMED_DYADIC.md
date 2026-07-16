# Nova 3 to Nova 4: Transformed Dyadic Resonance Audit

## Handoff ID

`N3-HO-N4-003`

## Audit scope

Independently reconstruct the exact transformed dyadic resonance package on branch `nova/computational-verification`.

Source branch:

`nova/analytic-density`

Primary proof:

`tracks/nova3-analytic-density/proofs/TRANSFORMED_DYADIC_RESONANCE_LADDER.md`

Primary verifier:

`tracks/nova3-analytic-density/proofs/transformed_dyadic_sanity.py`

## Current imported sources

- Nova 1: `nova/factorial-structure@1b81ec74f907d57d520bcf6c51f2e6e71f0474a7`
- Nova 2: `nova/additive-occupancy@e443674f86b2ee3c7037ac94ee47f6b8a4b3b29f`

## Results requiring separate verdicts

### N3-ANA-026

Verify the exact factorization at

\[
\theta_j=\frac{\pi}{2^{j-1}},
\qquad
1\le j\le M_n-1:
\]

\[
\widetilde\phi_{j+1}(\theta_j)
=2p_{j+1}^{(0)}-1,
\]

\[
\widetilde\phi_t(\theta_j)=1
\qquad(t>=j+2),
\]

\[
\widetilde\Phi(\theta_j)
=
\left(
\prod_{t=1}^{j}
\widetilde\phi_t(\theta_j)
\right)
(2p_{j+1}^{(0)}-1).
\]

Audit the claim that no nonzero dyadic frequency is an exact global modulus-one resonance because the transformed first support contains `0` and `1`.

### N3-ANA-027

Verify the low-state legality block and the uniform zero-state bound.

The safe depth is

\[
J_n
=
\min\left(
M_n-1,
\left\lfloor
1+\log_2
\frac{2^{M_n}-1}{16M_n\log L_n}
\right\rfloor
\right).
\]

Verify:

\[
J_n=M_n-O(\log\log n),
\]

\[
p_{j+1}^{(0)}
\le
\frac{2e}{m_n+1},
\]

\[
|\widetilde\phi_{j+1}(\theta_j)|
\ge
1-rac{4e}{m_n+1},
\]

and

\[
\sum_{t=j+1}^{M_n}
\widetilde{\mathcal D}_t(\theta_j)
\le
\frac{4e}{m_n+1}
\]

for every `j<=J_n`.

Return a separate verdict on the disproved mechanism:

> a fixed positive proportion of all transformed tail layers contributes fixed dispersion at every nonzero minor-arc frequency.

### N3-ANA-028

Verify the transformed interval length classification.

Let

\[
N_{n,q}=|J_{n,q}|.
\]

Check:

\[
v_2(N_{n,q})\in\{0,1\},
\]

with valuation one exactly when `rho_n` and `q` are both even.

At reduced dyadic frequency `2pi a/2^d`, verify

\[
\widetilde K_{n,q}(2\pi a/2^d)=0
\quad\Longleftrightarrow\quad
2^d\mid N_{n,q}.
\]

Confirm that no denominator `4` or higher dyadic frequency is an exact transformed-kernel zero.

## Finite verifier request

Run

```text
python3 tracks/nova3-analytic-density/proofs/transformed_dyadic_sanity.py
```

Return a separate verdict for `N3-FIN-008`.

The script checks:

- exact transformed supports for `n in {12,15}`;
- positive, zero, and negative transformed tilts;
- matching-layer factors;
- exact later-layer invisibility;
- finite-prefix characteristic identities;
- transformed-window lengths;
- dyadic kernel-zero classification.

## Selected scale rows to reconstruct

| `n` | `M_n` | `J_n` | excluded top scales | matching modulus floor | tail dispersion ceiling |
|---:|---:|---:|---:|---:|---:|
| 120368 | 2190 | 2165 | 24 | `0.9999261376` | `7.3863e-5` |
| 200000 | 2384 | 2359 | 24 | `0.9999484829` | `5.1517e-5` |
| 500000 | 2756 | 2730 | 25 | `0.9999849501` | `1.5050e-5` |
| 1000000 | 3054 | 3028 | 25 | `0.9999913115` | `8.6885e-6` |

These rows are computational evidence supporting the symbolic bounds. They are not substitutes for the proofs.

## Adversarial checks

1. Off-by-one errors between layer index `t`, denominator exponent `j`, and scale `2^{t-2}`.
2. Incorrect assertion that `pi*2^k` is a multiple of `2pi` when `k=0`.
3. Missing zero state in transformed layers `t>=2`.
4. Using the original tilt `lambda` instead of transformed tilt `2 lambda`.
5. Assuming every odd `u<=n` satisfies `3u|n!` without checking the spare factor of `3`.
6. Replacing `P_n<Y_n` by an unproved cutoff inequality.
7. Incorrect floor in the definition of `J_n`.
8. Claiming the transformed kernel vanishes whenever its length is even, regardless of the dyadic denominator.
9. Treating nonzero pointwise kernel values as positive-measure integral obstructions.
10. Claiming the full characteristic function is large merely because the matching and tail factors are large.

## Required response format

Return separate labels:

- `N3-ANA-026`: accepted, rejected, or accepted with correction;
- `N3-ANA-027`: accepted, rejected, or accepted with correction;
- `N3-ANA-028`: accepted, rejected, or accepted with correction;
- `N3-FIN-008`: accepted finite certificate or rejected;
- `N3-COMP-007`: accepted as computational evidence or corrected.

## Claim boundary

This audit does not authorize a claim of transformed local-window positivity, quotient occupancy, the factorial half-range theorem, or a solution of Erdős Problem 18.