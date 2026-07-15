# Nova 3 Status

## Track and branch

- Track: Analytic Divisor Density
- Branch: `nova/analytic-density`
- Main head inspected at startup: `68ace6c9c3b67636e298a406fee3bfe8e072741d`
- Merge base: `cd5576d4f7934e26e9d4ef3b065c2ad4cee36c67`
- No merge to `main`, force push, rebase, or edit to another Nova branch

## Overall state

`FOURTH_SUBSTANTIVE_CHECKPOINT_COMPLETE`

The factorial half-range theorem and Erdős Problem 18 remain open.

## New cross-track result

Nova 1 issued repaired marker-three audit `N1-HO-N3-002` from:

- branch: `nova/factorial-structure`
- exact commit: `9febe46f2298d2726eeffa139676136963790019`

Nova 3 returns:

- outcome: `ACCEPTED_WITH_PROOF_REPAIR`
- response: `handoffs/RESPONSE_TO_NOVA1_MARKER_THREE.md`
- theorems: N3-ANA-014, N3-ANA-015, N3-ANA-016

Both requested capacity statements hold for every integer

\[
n\ge120368.
\]

## New proved theorem N3-ANA-014

For

\[
U_t^{(3)}(n)=
\{u\ge1:u\text{ odd},\ 3u\mid n!,\ 3\cdot2^{t-1}u\le X_n\},
\]

and every `1<=t<=M_n`,

\[
M_n-1\le v_2(n!),
\]

\[
|U_t^{(3)}(n)|
\ge2^{h_n-1}
\ge2^{n/(3\log n)-1}.
\]

The exact proof uses

\[
H_n\mid\frac{n!}{\lfloor n/2\rfloor!}
\]

and proves

\[
9\,2^{2M_n-2}<\lfloor n/2\rfloor!.
\]

Proof: `proofs/MARKER_THREE_REPAIRED_CAPACITY_AUDIT.md`.

## New proved theorem N3-ANA-015

For every `n>=120368`,

\[
2^{r_n}
\prod_{t=1}^{M_n}
(|U_t^{(3)}(n)|+1)
\ge X_n+1.
\]

This is formal profile capacity only.

## New disproved proof step N3-ANA-016

The claim that every prime in `(n/2,n]` divides

\[
\binom n{\lfloor n/2\rfloor}
\]

is false for odd `n`.

For every prime `p`, take `n=2p-1`. Then

\[
p\in(n/2,n],
\qquad
v_p\binom{2p-1}{p-1}=0.
\]

This invalidates the suggested shortcut, not the repaired menu theorem.

## Existing analytic frontier

| ID | Class | Current conclusion |
|---|---|---|
| N3-ANA-004 | proved theorem | Exact divisor exponent product and tilt model |
| N3-ANA-005 | proved theorem | Uniform logarithmic local-count ceiling |
| N3-ANA-006 | proved theorem | Full model has a non-Gaussian limit |
| N3-ANA-007 | disproved estimate | Unrestricted pointwise minor-arc decay is false |
| N3-ANA-008 | proved theorem | Zero-tilt high-prime CLT |
| N3-ANA-009 | conditional theorem | Coarse high-prime window positivity |
| N3-ANA-010 | proved theorem | Explicit upper-half prime count for `n>=120368` |
| N3-ANA-011 | proved but superseded model | Old-address formal capacity |
| N3-ANA-012 | proved theorem | Compact-tilt top-prime coarse logarithmic windows |
| N3-ANA-013 | disproved estimate | Gaussian behavior fails at unit tilt |
| N3-ANA-014 | proved theorem | Repaired marker-three menu count and address legality |
| N3-ANA-015 | proved theorem | Repaired marker-three formal capacity |
| N3-ANA-016 | disproved estimate | Central-binomial divisibility shortcut is false |

## Exact finite certificate N3-FIN-004

At `n=120368`:

- top-prime count: `5254`;
- prime-count margin: greater than `1824.21`;
- `M_n=2190`;
- `r_n=47`;
- exact 2-adic address slack: `118171`;
- exact formal-capacity margin: `10575208` bits;
- repaired squared cutoff passes in exact integer arithmetic.

Command:

```text
python3 tracks/nova3-analytic-density/proofs/marker_three_capacity_sanity.py
```

Selected larger rows through `n=1000000` are N3-COMP-003 computational evidence only.

## Cross-track state

### Nova 1

The repaired marker-three capacity request is closed. Nova 1 must replace the invalid central-binomial step with the quotient-factorial proof.

### Nova 2

Nova 2 has frozen two numerical quotient requests:

- `N2-HO-N3-002`, a four-point quotient-window law for a three-power repair;
- `N2-HO-N3-003`, a marker-three numerical-value law with window radius `W_n`.

The latest Nova 1 marker-three construction has changed beyond the exact commit imported by the Nova 2 marker-three request. Before analytic work begins, the receiving model must freeze one exact current structural commit and state which deterministic prefix remains protected.

No logarithmic theorem will be substituted for the numerical additive law.

### Nova 4

Independent reconstruction is required for N3-ANA-014 through N3-ANA-016 and N3-FIN-004.

## Exact blockers

1. Nova 2 has multiple repaired quotient contracts and must identify the active one against a current Nova 1 commit.
2. The active contract must freeze the exact numerical labels, target range beyond the deterministic prefix, tilt parameterization, and endpoint handoff.
3. Constant-width numerical windows require a local torus estimate whose error is smaller than the reference mass, not merely Berry-Esseen distribution distance.
4. Fine logarithmic windows below `K_A log n` remain open.
5. Phase 12L and Phase 12P source packages remain outside the repository.
6. The branch remains divergent from `main`.

## Handoffs

- `handoffs/RESPONSE_TO_NOVA1.md`
- `handoffs/RESPONSE_TO_NOVA1_MARKER_THREE.md`
- `handoffs/TO_NOVA1_COMPACT_TILT.md`
- `handoffs/TO_NOVA2.md`
- `handoffs/TO_NOVA2_COMPACT_TILT.md`
- `handoffs/TO_NOVA4.md`
- `handoffs/TO_NOVA4_COMPACT_TILT.md`

## Next theorem target

`N3-NEXT-004`: audit Nova 2's competing repaired quotient requests against the latest Nova 1 construction. Freeze the one active numerical-value law, or return a precise version-mismatch obstruction before attempting any bounded-torus local theorem.