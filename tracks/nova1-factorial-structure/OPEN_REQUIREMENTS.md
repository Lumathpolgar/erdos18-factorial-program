# Nova 1 Open Requirements

## Nova 2 requirement

### N1-REQ-N2-001-A

Result label: **conditional theorem** request.

For the exact layers in `handoffs/TO_NOVA2.md`, prove that an absolute integer `n_0` exists such that, for every `n>=n_0` and every integer

\[
2^{r_n}\le x\le X_n,
\]

the rainbow sumset contains a value in

\[
[x-(2^{r_n}-1),x].
\]

Frozen constants:

\[
r_n=\lceil4\log n\rceil,
\qquad
M_n=\lceil16(\log n)^2\rceil.
\]

Selection restriction: zero or one term from each addressed layer.

Full statement: `handoffs/TO_NOVA2.md`.

## Nova 3 requirement

### N1-REQ-N3-001-A

Result label: **conditional theorem** request.

Prove an explicit integer `n_3` such that, for every integer `n>=n_3`,

\[
\pi(n)-\pi(n/2)\ge\frac{n}{3\log n}.
\]

Then derive explicit thresholds for the full-menu lower bound

\[
|U_t(n)|
\ge
2^{n/(3\log n)-1}-1
\]

and the preferred-route profile-capacity inequality.

Full statement: `handoffs/TO_NOVA3.md`.

## Nova 4 requirement

### N1-REQ-N4-001

Result label: **finite certificate** and **computational evidence** request.

Perform:

1. the exact capacity-threshold audit for every integer `3<=n<=1,000,000`;
2. the reduced rainbow falsification study for every integer `20<=n<=80`;
3. fail-closed legality, distinctness, residue, collision, and term-count verification.

Full statement: `handoffs/TO_NOVA4.md`.

## Internal Nova 1 requirement

### N1-REQ-N1-001

Result label: **conditional theorem** reconstruction requirement.

Reconstruct the archived Track B implication under the current frozen definitions:

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)=O((\log n)^2)
\Longrightarrow
h(n!)=O((\log n)^3).
\]

The archived package must be inspected before this result can be promoted.

## Closed structural requirements

- Factorial valuation atlas: closed by proved theorems.
- Numerical distinctness mechanism: closed by 2-adic marker signatures.
- Correction palette: closed by binary correction theorem.
- Fixed-family capacity audit: closed as a disproved route.
- Minimum menu entropy: closed as a proved necessary condition.
- Two complete structural candidates: closed as heuristic routes with exact blockers.

## Rule

No requirement may be weakened, strengthened, or reinterpreted silently. A changed hypothesis, constant, endpoint, or conclusion receives a new versioned requirement.