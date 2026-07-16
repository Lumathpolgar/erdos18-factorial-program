# Preferred Route Addendum: Checkpoint 009

Decision ID: `N3-ROUTE-008`

## Active object

For each dyadic scale `j`, let

\[
S_j=\sum_{t=1}^{j}\widetilde Z_t.
\]

The active problem is the weighted distribution

\[
P(S_j\equiv r\pmod{2^j})
\]

under the exact target-dependent transformed tilt.

## Closed support statement

A fixed low-state carrier reaches every residue modulo `2^j`.

This eliminates an exact prefix lattice-hole obstruction.

## Closed mass obstruction

The same carrier has total probability at most

\[
\frac{2e^2}{k_n}
\left(
\frac{3e^2}{k_n+1}
\right)^{j-1}
\]

through `M_n-O(log n)` scales.

Therefore exact support coverage cannot substitute for quantitative residue mixing.

## Ranked next routes

### 1. Full-menu residue pairing

Construct measure-preserving or bounded-distortion maps between full odd-core menu residue classes modulo `2^d`.

### 2. Full-prefix character estimates

Bound

\[
\prod_{t=1}^{j}
\widetilde\phi_{t,n,q}(\theta_j+u)
\]

directly in neighborhoods of the dyadic ladder.

### 3. Weighted additive-energy control

Bound residue-class collision energy for the complete transformed prefix law.

### 4. Exact obstruction

If the preceding routes fail, identify a target family with full-law residue concentration, not merely concentration of a selected carrier.

## Rejected route

`FIXED_LOW_STATE_SUPPORT_IMPLIES_MIXING`

Reason: the carrier is residue complete but has `exp(-Theta((log n)^3))` total mass.

## Mandatory rule

Every future prefix theorem must quantify probability mass or Fourier weight. A statement about legal support alone is insufficient.

## Claim boundary

The active route remains open. No quotient occupancy or factorial half-range theorem is proved.