# Response to Nova 4 Lattice Harness

Handoff response ID: `N2-RSP-N4-001`

Sending track: Nova 2, Additive Occupancy and Global Sumsets

Receiving track: Nova 4, Computation, Falsification, and Verification

Date: 2026-07-15

## Imported source

- repository: `Lumathpolgar/erdos18-factorial-program`
- branch: `nova/computational-verification`
- commit: `2f2a355f59f230751b8e798e7a5df0769e8bf6d9`
- draft PR: `#4`

## Outcome

`ACCEPTED_WITH_RESTRICTIONS`

## Accepted components

Nova 4 implemented an exact lattice-first audit layer containing:

- exact gcd and residue checks;
- fail-closed lattice certificates;
- exact rational certification of
  
  \[
  r_n=\lceil4\log n\rceil,
  \qquad
  M_n=\lceil16(\log n)^2\rceil;
  \]
- independent replay machinery for N2-ADD-115 and N2-OBS-107;
- corrupted-certificate fixtures for false gcd claims, correction collisions, numerical duplicates, and illegal factorial divisors;
- command-line integration and unit tests.

These components are accepted as verification infrastructure and as an independent replay of the original frozen lattice obstruction.

## Restrictions

The imported implementation does not yet satisfy the current quotient request `N2-HO-N4-001-v3`.

Specifically:

1. `n2_audit.py` freezes Nova 2 commit
   
   `45c74a5fa747551422ffcad7d3ddf22788fbe622`,
   
   rather than the current quotient-normalized contract.
2. It implements N2-ADD-115 and N2-OBS-107 only.
3. It does not implement N2-ADD-116, the exact lattice quotient equivalence.
4. It does not replay N2-OBS-108, the one-power and two-power repair failures.
5. It does not construct the normalized labels `B_t(n)` or final quotient sumset `Q_n`.
6. It does not scan four-point quotient windows.
7. It returns no later quotient counterexample and no finite quotient success certificate.

Therefore no conclusion about the three-power repaired model is imported from Nova 4 at this checkpoint.

## Independent Nova 2 result after intake

Nova 2 proved N2-ADD-118 in

`proofs/QUOTIENT_BINARY_SPINE_PREFIX.md`.

Under the frozen valuation-budget condition, the normalized final sumset meets every four-point quotient window through

\[
3\cdot2^{M_n}.
\]

Thus a full-family counterexample cannot occur before

\[
m=3\cdot2^{M_n}+1.
\]

At the first exactly certified admissible parameter `n=1892`, this protected quotient endpoint has 275 decimal digits.

## Required Nova 4 revision

Nova 4 should update the source metadata to the current Nova 2 head and add:

1. quotient normalization by `g_n=2^{r_n+1}`;
2. N2-OBS-108 regression replay;
3. exact binary-spine witness verification for N2-ADD-118;
4. a declared full-family or reduced-menu quotient cutoff;
5. the first empty four-point window after the proved prefix, if computationally accessible;
6. a clear `unknown due to resource limits` result when the exact full-family search cannot reach the first possible counterexample region.

A reduced-menu failure must not be reported as a failure of the full valuation-tagged model.

## Claim boundary

This response accepts Nova 4's lattice infrastructure. It does not accept a quotient-gap result because none has yet been produced. The repaired route is neither globally proved nor disproved by the imported Nova 4 commit.