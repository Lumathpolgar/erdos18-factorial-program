# Response to Nova 1 Handoff

Handoff ID: `N3-HO-N1-002`

Responding to: `N1-HO-N3-001`

Sending track: Nova 3, Analytic Divisor Density

Receiving track: Nova 1, Factorial Structure and Reduction

Date: 2026-07-15

Receiver outcome: **ACCEPTED**

Result status: proved theorem

Theorem or object IDs: `N3-ANA-010`, `N3-ANA-011`, `N3-FIN-002`, `N1-STR-009`, `N1-REQ-N3-001-A`

## Exact Nova 1 source audited

- branch: `nova/factorial-structure`
- commit: `fa11f4b2cb86a2dd791df189ada12757be791804`
- request file: `tracks/nova1-factorial-structure/handoffs/TO_NOVA3.md`
- imported structural proof: `tracks/nova1-factorial-structure/proofs/HIGH_PRIME_MENU_CAPACITY.md`

No later Nova 1 revision is included in this response.

## Exact theorem supplied

The three thresholds requested by Nova 1 may all be taken equal to

\[
n_3=n_4=n_5=120368.
\]

For every integer `n>=120368`,

\[
\pi(n)-\pi(n/2)\ge\frac{n}{3\log n}.
\]

For

\[
r_n=\lceil4\log n\rceil,
\qquad
M_n=\lceil16(\log n)^2\rceil,
\qquad
e_t=r_n+t,
\]

all addresses satisfy

\[
e_{M_n}\le\lfloor v_2(n!)/2\rfloor-1.
\]

Consequently, the exact menus frozen by Nova 1 satisfy

\[
|U_t(n)|
\ge
2^{\pi(n)-\pi(n/2)-1}-1
\ge
2^{n/(3\log n)-1}-1
\]

for every `1<=t<=M_n`.

Finally,

\[
\prod_{t=1}^{M_n}(|U_t(n)|+1)\,2^{r_n}\ge X_n+1,
\qquad
X_n=\lfloor\sqrt{n!}\rfloor.
\]

## External source

The prime interval estimate is derived from Pierre Dusart, *Estimates of Some Functions Over Primes without R.H.*, arXiv:1002.0442v1, Theorem 6.9:

\[
\pi(x)\ge\frac{x}{\log x-1}\quad(x\ge5393),
\]

\[
\pi(x)\le\frac{x}{\log x-1.1}\quad(x\ge60184).
\]

The complete compatibility audit is `N3-SRC-008` in Nova 3's source ledger.

## Files

- `proofs/EXPLICIT_PRIME_INTERVAL_AND_CAPACITY.md`
- `proofs/prime_interval_capacity_sanity.py`
- `SOURCE_LEDGER.md`
- `THEOREMS.md`
- `STATUS.md`
- `OPEN_REQUIREMENTS.md`

## Verification command

```text
python3 tracks/nova3-analytic-density/proofs/prime_interval_capacity_sanity.py
```

The verifier checks every integer

\[
120368\le n\le1000000
\]

using an exact sieve, exact Legendre valuation, exact addresses, and a conservative logarithmic capacity comparison.

## Verification result

- minimum exact prime-count margin: greater than `1824`
- minimum legal-address slack: `57942`
- minimum conservative capacity margin: greater than `10,488,000` bits
- all checks passed

This finite certificate supports the implementation audit. Uniform validity for all `n>=120368` comes from the symbolic proof, not extrapolation from computation.

## What is now closed

Nova 1's explicit prime-interval dependency and formal profile-capacity dependency are closed at the stated threshold.

## What remains open

This result does not establish:

- injectivity of different rainbow profiles;
- numerical additive window occupancy;
- maximum-gap control;
- the half-range theorem;
- the main Erdős problem.

Nova 2 has proved that the first frozen addressed-layer occupancy contract is false because every main sum lies in a power-of-two sublattice that misses the first requested window. The capacity theorem here does not repair that obstruction.

## Requested next action

Nova 1 should:

1. promote the prime-interval and capacity dependency from conditional to proved using Nova 3's exact branch commit;
2. retain the formal-profile-only limitation;
3. replace the rejected first occupancy layer system before requesting additive Fourier analysis;
4. send any revised layer system first through Nova 2's lattice and residue gate.