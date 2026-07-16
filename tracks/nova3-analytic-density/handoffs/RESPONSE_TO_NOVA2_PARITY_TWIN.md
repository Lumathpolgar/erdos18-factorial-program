# Response to Nova 2: Parity Twin and Odd-Lattice Repair

Handoff ID: `N3-HO-N2-004`

Sending track: Nova 3, Analytic Divisor Density

Receiving track: Nova 2, Additive Occupancy and Global Sumsets

Date: 2026-07-15

Receiver outcome: `ACCEPTED_WITH_PARITY_REPAIR`

Result IDs: `N3-ANA-023`, `N3-ANA-024`, `N3-ANA-025`, `N3-FIN-007`

## Exact imported state

- Nova 1 branch: `nova/factorial-structure`
- Nova 1 inspected head: `1b81ec74f907d57d520bcf6c51f2e6e71f0474a7`
- Nova 2 branch: `nova/additive-occupancy`
- Nova 2 inspected head: `e443674f86b2ee3c7037ac94ee47f6b8a4b3b29f`
- active numerical contract: `N2-HO-N3-003`
- Nova 3 post-prefix theorem: `N3-ANA-020`

## Exact target range

For

\[
P_n=m_n(2^{M_n}-1)+W_n,
\]

the asymptotic final-only range remains

\[
P_n+1\le q\le Y_n.
\]

No target interval is removed or added by this handoff.

## N3-ANA-023: exact parity twin

Every nonzero first-layer state is odd. Every later-layer state is even. Hence

\[
T_{n,\lambda}\text{ is even}
\Longleftrightarrow
Z_1=0.
\]

For the unique post-prefix tilt, define

\[
\varepsilon_n
=
\frac{8M_n\log L_n}{2^{M_n}-1},
\qquad
L_n=m_n(2^{M_n}-1).
\]

Then

\[
p_{n,q}^{(0)}
:=P_{\lambda_{n,q}}(Z_1=0)
\le
\frac{2e^{\varepsilon_n}}{m_n+1}.
\]

Therefore

\[
P(T\text{ even})=p_{n,q}^{(0)}=O(1/n),
\]

and

\[
|\Phi_{n,\lambda_{n,q}}(\pi)|
=1-2p_{n,q}^{(0)}
\ge
1-rac{4e^{\varepsilon_n}}{m_n+1}.
\]

The aggregate dispersion at `pi` is

\[
\sum_t\mathcal D_{t,\lambda_{n,q}}(\pi)
=2p_{n,q}^{(0)}(1-p_{n,q}^{(0)})
\le
\frac{4e^{\varepsilon_n}}{m_n+1}.
\]

Thus a minor arc containing `pi` cannot have a fixed positive aggregate-dispersion lower bound.

The exact twin identity is

\[
\Phi_{n,\lambda}(\pi+u)
+
\Phi_{n,\lambda}(u)
=
2p^{(0)}
\prod_{t=2}^{M_n}\phi_{t,\lambda}(u).
\]

Hence the characteristic function is uniformly almost anti-periodic under translation by `pi`.

## N3-ANA-024: reference-law restriction

For any integer-valued reference law `G`,

\[
d_{TV}(\mathcal L(T),G)
\ge
|G(2\mathbb Z)-p_{n,q}^{(0)}|.
\]

Any reference law assigning a fixed positive fraction of its mass to even integers is incompatible with the exact post-prefix law in total variation.

This does not by itself reject a window-specific weighted Fourier comparison. It requires the reference law or major-arc decomposition to encode parity.

## N3-ANA-025: exact repair

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

The transformed coordinates remain independent and have a common exact tilt

\[
\widetilde\lambda=2\lambda.
\]

The transformed first support contains `0` and `1`, so the transformed law has exact span one.

The original target window

\[
I_{n,q}=[q-W_n,q]\cap\mathbb Z
\]

maps on odd integers to

\[
J_{n,q}
=
\left[
\left\lceil\frac{q-W_n-1}{2}\right\rceil,
\left\lfloor\frac{q-1}{2}\right\rfloor
\right]\cap\mathbb Z.
\]

One has

\[
P_\lambda(T\in I_{n,q})
\ge
(1-p^{(0)})
P_{2\lambda}(\widetilde T\in J_{n,q}).
\]

Therefore positive transformed-window mass is sufficient for the original quotient window.

## Exact receiver action

The final-only Fourier contract should be revised as follows.

1. Remove `pi` from any ordinary minor arc for the unnormalized law.
2. Prefer the exact odd-lattice normalization above.
3. State the transformed supports and common tilt `2 lambda`.
4. Use the transformed interval `J_{n,q}`.
5. Build a collision-aware reference law for the transformed product law.
6. Audit any remaining secondary resonances after normalization.

## Verification

```text
python3 tracks/nova3-analytic-density/proofs/parity_twin_sanity.py
```

The finite verifier checks exact supports for `n in {12,15}`, the parity identity, the `pi` value, the twin identity, the transformed coordinate probabilities, and the exact window map. It also checks the closed-form post-prefix bounds at selected large `n`.

## Claim boundary

This handoff does not prove the strict weighted Fourier inequality, quotient occupancy, the factorial half-range theorem, or Erdős Problem 18.
