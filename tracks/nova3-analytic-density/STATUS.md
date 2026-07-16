# Nova 3 Status

## Track and branch

- Track: Analytic Divisor Density
- Branch: `nova/analytic-density`
- Main baseline inspected: `68ace6c9c3b67636e298a406fee3bfe8e072741d`
- Merge base: `cd5576d4f7934e26e9d4ef3b065c2ad4cee36c67`
- No merge to `main`, force push, rebase, or edit to another Nova branch

## Overall state

`SEVENTH_SUBSTANTIVE_CHECKPOINT_COMPLETE`

The factorial half-range theorem and Erdős Problem 18 remain open.

## Current cross-track sources

### Nova 1

- branch: `nova/factorial-structure`
- inspected head: `1b81ec74f907d57d520bcf6c51f2e6e71f0474a7`
- active construction: `N1-CON-003`
- exact finite marker-three coverage now reaches `12<=n<=52`
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

### N3-ANA-017 through N3-ANA-019

- active contract compatibility proved;
- unique finite centering tilt proved;
- exact additive span one proved;
- exact modulus-one resonance set `{0}` proved;
- all-tilt minor-arc gap disproved by endpoint freezing.

### N3-ANA-020

For every post-prefix target,

\[
-\frac{8M_n\log L_n}{L_n}
<\lambda_{n,q}<
\frac{16(n\log n+\log14)}{2^{M_n}},
\qquad
L_n=m_n(2^{M_n}-1).
\]

Thus

\[
\sup_{P_n<q\le Y_n}|\lambda_{n,q}|\to0.
\]

### N3-ANA-021

The single zero-versus-minimum-state phase coefficient is exponentially small at zero tilt. Compact tilt does not rescue that anchor.

### N3-ANA-022

Exact numerical atoms include profile collision multiplicity:

\[
P_\lambda(T=s)
=
\frac{C_n(s)e^{\lambda s}}
{\prod_tZ_t(\lambda)}.
\]

## New result N3-ANA-023: parity twin near-resonance

Every nonzero first-layer state is odd. Every later-layer state is even. Therefore

\[
T\text{ is even}
\Longleftrightarrow
Z_1=0.
\]

Put

\[
\varepsilon_n
=
\frac{8M_n\log L_n}{2^{M_n}-1}.
\]

Uniformly over the exact post-prefix target range,

\[
p^{(0)}_{n,q}
:=P(Z_1=0)
\le
\frac{2e^{\varepsilon_n}}{m_n+1}.
\]

Hence

\[
P(T\text{ even})=p^{(0)}_{n,q}=O(1/n),
\]

while

\[
\Phi(\pi)=2p^{(0)}_{n,q}-1
\]

and

\[
|\Phi(\pi)|
\ge
1-rac{4e^{\varepsilon_n}}{m_n+1}
\to1.
\]

The exact parity-twin identity is

\[
\Phi(\pi+u)+\Phi(u)
=
2p^{(0)}
\prod_{t=2}^{M_n}\phi_t(u).
\]

Thus the original zero-only major-arc plan is invalid even after compact tilt. The unnormalized law has an asymptotically exact secondary twin at `pi`.

## New obstruction N3-ANA-024: parity-blind reference laws

For every integer reference law `G`,

\[
d_{TV}(\mathcal L(T),G)
\ge
|G(2\mathbb Z)-p^{(0)}|.
\]

A reference law with a fixed positive even mass cannot approximate the post-prefix law in total variation.

This does not by itself disprove a window-specific weighted Fourier comparison. It forces parity into the reference law or major-arc decomposition.

## New theorem N3-ANA-025: exact odd-lattice normalization

Condition on `Z_1!=0` and define

\[
\widetilde Z_1=(Z_1-1)/2,
\qquad
\widetilde Z_t=Z_t/2\quad(t>=2).
\]

Then

\[
\widetilde T=(T-1)/2
\]

under the odd conditional law.

The transformed coordinates:

- remain independent;
- share the exact common tilt `2 lambda`;
- have exact additive span one because the first transformed support contains `0` and `1`.

The original target window

\[
I_{n,q}=[q-W_n,q]\cap\mathbb Z
\]

maps to

\[
J_{n,q}
=
\left[
\left\lceil\frac{q-W_n-1}{2}\right\rceil,
\left\lfloor\frac{q-1}{2}\right\rfloor
\right]\cap\mathbb Z.
\]

The exact positivity transfer is

\[
P_\lambda(T\in I_{n,q})
\ge
(1-p^{(0)})
P_{2\lambda}(\widetilde T\in J_{n,q}).
\]

This removes the forced parity twin. It does not prove that all secondary resonances disappear.

## Verification

```text
python3 tracks/nova3-analytic-density/proofs/scale_sanity.py
python3 tracks/nova3-analytic-density/proofs/prime_interval_capacity_sanity.py
python3 tracks/nova3-analytic-density/proofs/compact_tilt_sanity.py
python3 tracks/nova3-analytic-density/proofs/marker_three_capacity_sanity.py
python3 tracks/nova3-analytic-density/proofs/marker_three_numerical_law_sanity.py
python3 tracks/nova3-analytic-density/proofs/post_prefix_tilt_sanity.py
python3 tracks/nova3-analytic-density/proofs/parity_twin_sanity.py
```

### N3-FIN-007

The verifier checks:

- exact marker-three supports for `n in {12,15}`;
- first-layer odd and later-layer even structure;
- the exact value at `pi`;
- the parity-twin identity at positive, zero, and negative tilts;
- transformed coordinate probabilities under tilt `2 lambda`;
- the exact transformed target-window map.

Selected large closed-form rows:

| `n` | zero-state ceiling | lower bound for `|Phi(pi)|` |
|---:|---:|---:|
| 120368 | `1.6616e-5` | `0.9999667686` |
| 200000 | `1.0000e-5` | `0.9999800000` |
| 500000 | `4.0000e-6` | `0.9999920000` |
| 1000000 | `2.0000e-6` | `0.9999960000` |

## Cross-track outcome

### Nova 2

Handoff:

`handoffs/RESPONSE_TO_NOVA2_PARITY_TWIN.md`

Outcome:

`ACCEPTED_WITH_PARITY_REPAIR`.

The final-only Fourier contract should use the exact odd-lattice normalized law, or explicitly include both zero and `pi` major arcs with a parity-aware reference law.

### Nova 4

Independent reconstruction requested in:

`handoffs/TO_NOVA4_PARITY_TWIN.md`.

## Exact remaining blockers

1. Audit all secondary resonances of the normalized odd-lattice law.
2. Prove aggregate transformed phase dispersion outside explicit transformed major arcs.
3. Prove uniform transformed variance, third-moment, and maximal-step bounds.
4. Construct a collision-aware transformed reference law.
5. Prove the strict transformed weighted Fourier inequality.
6. Independently reconstruct N3-ANA-023 through N3-ANA-025.
7. Reconstruct unavailable Phase 12L and Phase 12P source packages.
8. Handle finite exceptions after an effective asymptotic theorem exists.

## Claim boundary

Compact tilt, parity normalization, exact span, and collision identities do not prove quotient occupancy, the factorial half-range theorem, or Erdős Problem 18.

## Next theorem target

`N3-NEXT-007`: audit the transformed odd-lattice product law for all remaining dyadic or rational secondary resonances. Prove an aggregate dispersion or weighted integral bound outside the complete transformed major-arc set, or return the first exact transformed residue concentration that blocks it.
