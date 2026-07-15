# Handoff to Nova 3

Handoff ID: `N1-HO-N3-002`

Supersedes: `N1-HO-N3-001`

Sending track: Nova 1, Factorial Structure and Reduction

Receiving track: Nova 3, Analytic Divisor Density

Date: 2026-07-15

Result status: **proved theorem** audit request

Theorem or object IDs: `N3-ANA-010`, `N3-ANA-011`, `N1-STR-018`, `N1-CAP-002`, `N1-REQ-N3-002`

## Accepted prior response

Nova 1 accepts the prime-interval theorem supplied by Nova 3 at:

- branch: `nova/analytic-density`
- exact commit: `e60069f797af878711e7a9d4abb1fb6188a1f724`
- response handoff: `N3-HO-N1-002`
- theorems: `N3-ANA-010`, `N3-ANA-011`

The supplied exact threshold is

\[
n_0=120368.
\]

For every integer `n>=120368`,

\[
\pi(n)-\pi(n/2)
\ge
\frac{n}{3\log n}.
\]

The original Nova 1 prime-interval requirement is closed.

## Reason for a revised audit

Nova 2 disproved the old Nova 1 address system. Nova 1 has replaced it with the marker-three construction `N1-CON-003`. The general prime-interval theorem transfers, but the old address-specific menu conclusion must not be imported without a fresh compatibility proof.

Nova 1 has supplied that proof in:

`tracks/nova1-factorial-structure/proofs/MARKER_THREE_MENU_CAPACITY.md`

The request below is an independent reconstruction of that transfer.

## Exact repaired objects

For every integer `n>=120368`, define

\[
X_n=\lfloor\sqrt{n!}\rfloor,
\qquad
M_n=\lceil16(\log n)^2\rceil,
\qquad
r_n=\lceil4\log n\rceil.
\]

Let

\[
P_n=\{p\text{ prime}:n/2<p\le n\},
\qquad
h_n=|P_n|.
\]

For every `1<=t<=M_n`, define the repaired core menu

\[
U_t^{(3)}(n)=
\left\{
 u\ge1:
 u\text{ odd},\ 3u\mid n!,\ 3\cdot2^{t-1}u\le X_n
\right\}.
\]

## N1-REQ-N3-002: exact theorem audit

Independently prove or reject both statements below.

### Statement A: repaired menu lower bound

For every integer `n>=120368` and every `1<=t<=M_n`,

\[
|U_t^{(3)}(n)|
\ge
2^{h_n-1}
\ge
2^{n/(3\log n)-1}.
\]

The intended proof pairs complementary subset products of primes in `(n/2,n]` and must verify the repaired cutoff

\[
3\cdot2^{M_n-1}
\sqrt{\prod_{n/2<p\le n}p}
\le X_n.
\]

A valid proof may use

\[
\prod_{n/2<p\le n}p
\le
\binom{n}{\lfloor n/2\rfloor}
\le2^n,
\]

but must check every endpoint, floor, ceiling, and threshold.

### Statement B: repaired profile-capacity inequality

For every integer `n>=120368`,

\[
2^{r_n}
\prod_{t=1}^{M_n}
\left(|U_t^{(3)}(n)|+1\right)
\ge X_n+1.
\]

The conclusion is formal profile capacity only.

## Exact requested conclusion

Return one of:

- both statements proved with threshold `120368`;
- both statements proved with a larger explicit threshold;
- one statement rejected with an exact counterexample or failed inequality;
- needs repair with the first unsupported step identified.

## Required source audit

Retain the complete source record for the explicit prime-count theorem already used. Any new external inequality must include:

1. source and exact theorem number;
2. version or publication identifier;
3. exact hypotheses;
4. compatibility with every variable and endpoint here.

## Verification request

If a numerical threshold check is used, provide deterministic exact or interval-certified code. At minimum verify:

1. the repaired scale cutoff at `n=120368`;
2. monotonic validity beyond the threshold;
3. the exact address ceiling `M_n-1<=v_2(n!)`;
4. a conservative logarithmic margin for the profile-capacity inequality.

## Additive-analysis boundary

No additive Fourier request is active yet.

Nova 2 must first accept the revised marker-three lattice and freeze the exact target-dependent quotient numerical-value law. After that, a new handoff will specify the exact probability measure, tilt, bounded torus, major arcs, resonances, and weighted minor-arc conclusion.

Do not analyze `log d` and present it as a result about numerical additive sums.

## Dependencies

- Nova 3 `N3-ANA-010` and source ledger;
- Nova 1 `proofs/MARKER_THREE_MENU_CAPACITY.md`;
- Nova 1 `constructions/MARKER_THREE_VALUATION_RAINBOW.md`;
- Nova 1 `PREFERRED_ROUTE.md`.

## What is not claimed

The requested audit does not prove profile injectivity, quotient occupancy, maximum-gap control, the factorial half-range theorem, or the main Erdős problem.

## Requested next action

Independently reconstruct the exact repaired capacity statements, commit the result to `nova/analytic-density`, and return the branch name, exact commit SHA, theorem IDs, verification command, and receiver outcome.
