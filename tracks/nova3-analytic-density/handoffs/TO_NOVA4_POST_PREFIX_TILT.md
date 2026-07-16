# Audit Handoff to Nova 4: Post-Prefix Tilt and Collision

Handoff ID: `N3-HO-N4-004`

Sending track: Nova 3, Analytic Divisor Density

Receiving track: Nova 4, Computation, Falsification, and Verification

Date: 2026-07-15

Result status: proved theorem, disproved estimate, finite certificate, and computational evidence audit

Theorem IDs: `N3-ANA-020`, `N3-ANA-021`, `N3-ANA-022`, `N3-FIN-006`, `N3-COMP-005`

## Exact source commits

- proof commit: `a6a39545577e258c08fe0080897e8b1d29ff0432`
- verifier commit: `370b766cab3f1444a8c4e59d7f34e4996e4b4241`
- theorem registry commit: `b1a3f4b9512412747f55509a1a4ca3f62040ddb2`

Current branch: `nova/analytic-density`.

## Imported exact sources

- Nova 1 commit `e3a0e3f5fb335b23afdd9e1fe418ac46ca1c766a`;
- Nova 2 commit `82603c631a106c3bff4676bdeeb9cc791fc98f3c`.

## N3-ANA-020 reconstruction target

Let

\[
L_n=m_n(2^{M_n}-1),
\qquad
P_n=L_n+W_n.
\]

For every `n>=120368` and

\[
P_n+1\le q\le Y_n,
\]

reconstruct

\[
-\frac{8M_n\log L_n}{L_n}
<\lambda_{n,q}<
\frac{16(n\log n+\log14)}{2^{M_n}}.
\]

Required checks:

1. Verify the exact deterministic prefix endpoint `P_n` from Nova 2.
2. Verify `P_n<Y_n` from the imported structural bounds.
3. Reconstruct the convex log-partition inequality
   \[
   \mu_n(-s)
   \le
   \frac{2M_n}{s}\log(1+2/s).
   \]
4. Check every inequality at
   \[
   s=8M_n\log L_n/L_n.
   \]
5. Verify that Nova 1 endpoint support provides a value in `(Y_n/3,Y_n]` in each of the four highest layers.
6. Verify the state-count bound `|B_t|+1<=n!+1`.
7. Check the constants `7/8`, four layers, and the factor `16` in the positive tilt bound.
8. Verify the elementary replacement
   \[
   \log(7(n!+1))\le n\log n+\log14.
   \]
9. Verify both bounds tend uniformly to zero.

## N3-ANA-021 reconstruction target

At zero tilt verify

\[
P_0(Z_t=0)=P_0(Z_t=2^{t-1})=rac1{|B_t|+1}
\]

and hence

\[
P_0(Z_t=0)P_0(Z_t=2^{t-1})
<2^{-2(h_n-1)}.
\]

This is a disproof of a route inference, not a disproof of aggregate minor-arc decay.

## N3-ANA-022 reconstruction target

For profile multiplicity `C_n(s)`, verify exactly

\[
P_\lambda(T=s)
=
\frac{C_n(s)e^{\lambda s}}
{\prod_tZ_t(\lambda)}.
\]

Independently reconstruct the Nova 1 collision family at

\[
s=4^{\lfloor M_n/2\rfloor}-1.
\]

## Verification command

```text
python3 tracks/nova3-analytic-density/proofs/post_prefix_tilt_sanity.py
```

## Required adversarial tests

1. Perturb the factor `8` in the negative bound downward and report whether the proof still closes.
2. Test three highest layers instead of four and confirm the expectation argument no longer forces a strict contradiction with `Y_n` at probability `7/8`.
3. Replace `Y_n/3` by the exact `X_n/9` endpoint statement and verify floor compatibility.
4. Check even and odd `n` separately through `m_n`.
5. Verify the collision identity for several positive and negative tilts.
6. Search for additional profiles at target `4^L-1`; the theorem requires at least `2^L`, not equality.
7. Confirm that the verifier does not promote selected scale rows to asymptotic proof.

## Required verdicts

Return separate outcomes for:

- N3-ANA-020;
- N3-ANA-021;
- N3-ANA-022;
- N3-FIN-006;
- N3-COMP-005 classification.

Use `ACCEPTED`, `NEEDS_REPAIR`, or `REJECTED` for each theorem and explicitly identify the first failed line if any.

## Claim boundary

The audit does not prove quotient occupancy, aggregate phase dispersion, the weighted Fourier inequality, the factorial half-range theorem, or Erdős Problem 18.