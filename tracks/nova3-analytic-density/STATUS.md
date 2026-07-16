# Nova 3 Status

## Track and branch

- Track: Analytic Divisor Density
- Branch: `nova/analytic-density`
- Main baseline inspected: `68ace6c9c3b67636e298a406fee3bfe8e072741d`
- Merge base: `cd5576d4f7934e26e9d4ef3b065c2ad4cee36c67`
- No merge to `main`, force push, rebase, or edit to another Nova branch

## Overall state

`EIGHTH_SUBSTANTIVE_CHECKPOINT_COMPLETE`

The factorial half-range theorem and Erdős Problem 18 remain open.

## Current cross-track sources

### Nova 1

- branch: `nova/factorial-structure`
- inspected head: `1b81ec74f907d57d520bcf6c51f2e6e71f0474a7`
- active construction: `N1-CON-003`
- exact finite marker-three coverage reaches `12<=n<=52`
- numerical label definitions remain unchanged

### Nova 2

- branch: `nova/additive-occupancy`
- inspected head: `e443674f86b2ee3c7037ac94ee47f6b8a4b3b29f`
- active request: `N2-HO-N3-003`
- deterministic quotient-window prefix:
  \[
  P_n=m_n(2^{M_n}-1)+W_n
  \]
- exact asymptotic final-only range:
  \[
  P_n+1\le q\le Y_n
  \]

## Closed numerical foundation

### N3-ANA-017 through N3-ANA-022

Closed:

- active contract compatibility;
- unique finite centering tilt;
- exact additive span one;
- exact modulus-one resonance set `{0}`;
- exact deterministic-to-analytic transition;
- uniform post-prefix tilt compression;
- binary-anchor failure;
- collision-aware atom identity.

The exact post-prefix tilt bound is

\[
-\frac{8M_n\log L_n}{L_n}
<\lambda_{n,q}<
\frac{16(n\log n+\log14)}{2^{M_n}},
\qquad
L_n=m_n(2^{M_n}-1).
\]

## Parity checkpoint

### N3-ANA-023

The unnormalized law has an asymptotically exact parity twin:

\[
P(T\text{ even})
=p^{(0)}_{n,q}
\le
\frac{2e^{\varepsilon_n}}{m_n+1},
\]

\[
\Phi(\pi)=2p^{(0)}_{n,q}-1,
\]

\[
|\Phi(\pi)|
\ge
1-
\frac{4e^{\varepsilon_n}}{m_n+1}
\to1,
\]

where

\[
\varepsilon_n
=
\frac{8M_n\log L_n}{2^{M_n}-1}.
\]

The exact twin identity is

\[
\Phi(\pi+u)+\Phi(u)
=
2p^{(0)}
\prod_{t=2}^{M_n}\phi_t(u).
\]

### N3-ANA-024

Every integer reference law `G` satisfies

\[
d_{TV}(\mathcal L(T),G)
\ge
|G(2\mathbb Z)-p^{(0)}|.
\]

A parity-blind reference law cannot approximate the post-prefix law in total variation.

### N3-ANA-025

Condition on `Z_1!=0` and define

\[
\widetilde Z_1=(Z_1-1)/2,
\qquad
\widetilde Z_t=Z_t/2
\quad(t>=2).
\]

Then

\[
\widetilde T=(T-1)/2
\]

under the odd conditional law. The transformed coordinates remain independent, share common tilt `2 lambda`, and have exact span one.

The transformed target window is

\[
J_{n,q}
=
\left[
\left\lceil\frac{q-W_n-1}{2}\right\rceil,
\left\lfloor\frac{q-1}{2}\right\rfloor
\right]\cap\mathbb Z.
\]

Positive transformed-window mass implies positive original-window mass.

## New transformed dyadic checkpoint

### N3-ANA-026, exact finite-prefix factorization

For

\[
\theta_j=\frac{\pi}{2^{j-1}},
\qquad
1\le j\le M_n-1,
\]

one has

\[
\widetilde\phi_{j+1}(\theta_j)
=2p_{j+1}^{(0)}-1,
\]

\[
\widetilde\phi_t(\theta_j)=1
\qquad(t>=j+2),
\]

and therefore

\[
\widetilde\Phi(\theta_j)
=
\left(
\prod_{t=1}^{j}
\widetilde\phi_t(\theta_j)
\right)
(2p_{j+1}^{(0)}-1).
\]

There is no nonzero exact dyadic resonance because the transformed first support contains `0` and `1`. However, every dyadic frequency has an exact tail resonance.

### N3-ANA-027, near-pure matching layer and tail collapse

Define

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

Then

\[
J_n=M_n-O(\log\log n).
\]

Uniformly for `1<=j<=J_n`,

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
\frac{4e}{m_n+1}.
\]

Thus a many-tail-layers dispersion mechanism is false at the transformed dyadic ladder. Any decay there must come from the first `j` transformed coordinates.

### N3-ANA-028, transformed-window kernel classification

Let

\[
N_{n,q}=|J_{n,q}|.
\]

Then

\[
v_2(N_{n,q})\in\{0,1\}.
\]

More precisely, `v_2(N_{n,q})=1` exactly when `rho_n` and `q` are both even. Otherwise `N_{n,q}` is odd.

At a reduced dyadic frequency `2pi a/2^d`, the transformed interval kernel vanishes exactly when `2^d|N_{n,q}`. Therefore it never vanishes for denominator at least `4`. At `pi`, it vanishes only in the even-even case.

This does not create an integral obstruction by itself. It proves that exact kernel cancellation cannot remove the higher dyadic ladder points.

## Verification

```text
python3 tracks/nova3-analytic-density/proofs/scale_sanity.py
python3 tracks/nova3-analytic-density/proofs/prime_interval_capacity_sanity.py
python3 tracks/nova3-analytic-density/proofs/compact_tilt_sanity.py
python3 tracks/nova3-analytic-density/proofs/marker_three_capacity_sanity.py
python3 tracks/nova3-analytic-density/proofs/marker_three_numerical_law_sanity.py
python3 tracks/nova3-analytic-density/proofs/post_prefix_tilt_sanity.py
python3 tracks/nova3-analytic-density/proofs/parity_twin_sanity.py
python3 tracks/nova3-analytic-density/proofs/transformed_dyadic_sanity.py
```

### N3-FIN-008

The new verifier checks for `n in {12,15}`:

- exact transformed supports;
- matching-layer two-phase factors;
- exact invisibility of every later layer;
- the finite-prefix product identity;
- exact transformed-window lengths;
- the dyadic kernel-zero criterion.

### N3-COMP-007

Selected large rows:

| `n` | `M_n` | safe dyadic depth `J_n` | excluded top scales | matching modulus floor | tail dispersion ceiling |
|---:|---:|---:|---:|---:|---:|
| 120368 | 2190 | 2165 | 24 | `0.9999261376` | `7.3863e-5` |
| 200000 | 2384 | 2359 | 24 | `0.9999484829` | `5.1517e-5` |
| 500000 | 2756 | 2730 | 25 | `0.9999849501` | `1.5050e-5` |
| 1000000 | 3054 | 3028 | 25 | `0.9999913115` | `8.6885e-6` |

At `n=120368`, the transformed window length is

\[
23456248059221,
\]

which is odd. No nonzero dyadic kernel zero is available there.

## Cross-track outcome

### Nova 2

The final-only transformed Fourier contract must now control prefix residue mixing at the dyadic ladder frequencies and their neighborhoods. Tail accumulation alone is invalid.

### Nova 4

Independent reconstruction is required for N3-ANA-026 through N3-ANA-028 and N3-FIN-008.

## Exact remaining blockers

1. Prove prefix characteristic decay or prefix residue spreading at every relevant transformed dyadic scale.
2. Extend from exact dyadic points to neighborhoods matched to the transformed interval kernel.
3. Prove uniform transformed variance, third-moment, and maximal-step bounds.
4. Construct a collision-aware transformed reference law.
5. Prove the strict transformed weighted Fourier inequality.
6. Independently reconstruct N3-ANA-023 through N3-ANA-028.
7. Reconstruct unavailable Phase 12L and Phase 12P source packages.
8. Handle finite exceptions after an effective asymptotic theorem exists.

## Claim boundary

Compact tilt, parity normalization, exact span, dyadic factorization, and collision identities do not prove quotient occupancy, the factorial half-range theorem, or Erdős Problem 18.

## Next theorem target

`N3-NEXT-008`: prove a prefix-residue or prefix-characteristic estimate for

\[
\prod_{t=1}^{j}
\widetilde\phi_{t,n,q}(\theta)
\]

in neighborhoods of every transformed dyadic ladder frequency `theta_j`, with bounds matched to the exact transformed interval kernel. If this fails, return the first exact prefix residue concentration or target-local additive-energy obstruction.