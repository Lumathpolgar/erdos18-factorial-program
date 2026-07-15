# Response to Nova 1 Handoff

Handoff ID: `N2-HO-N1-002`

Responding to: `N1-HO-N2-001`

Sending track: Nova 2, Additive Occupancy and Global Sumsets

Receiving track: Nova 1, Factorial Structure and Reduction

Date: 2026-07-15

Receiver outcome: **REJECTED**

Result status: **proved theorem** and **disproved model**

Theorem or object IDs: `N2-ADD-115`, `N2-OBS-107`, `N1-CON-001`, `N1-REQ-N2-001-A`

## Exact source audited

- branch: `nova/factorial-structure`
- commit: `b939574eb88a08bb03abda5bbe6ff2ca97444e08`
- file: `tracks/nova1-factorial-structure/handoffs/TO_NOVA2.md`

No later Nova 1 revision is included in this decision.

## Exact decision

The requested theorem is false.

The frozen construction sets

\[
e_t=r_n+t,
\qquad 1\le t\le M_n.
\]

Therefore every nonzero main term is divisible by

\[
2^{r_n+1}.
\]

Consequently every final rainbow sum lies in

\[
2^{r_n+1}\mathbb Z.
\]

The requested correction radius is only

\[
2^{r_n}-1.
\]

At the first requested target

\[
x=2^{r_n},
\]

the required downward window is

\[
[1,2^{r_n}],
\]

which contains no multiple of `2^{r_n+1}`. The empty sum is `0` and lies outside the window.

Thus

\[
[1,2^{r_n}]\cap\mathcal R_n=\varnothing.
\]

This failure occurs for all sufficiently large admissible `n`, since the valuation-budget side condition eventually holds and `2^{r_n}<=X_n` eventually holds.

## Proof file

`tracks/nova2-additive-occupancy/proofs/VALUATION_TAGGED_LATTICE_OBSTRUCTION.md`

## Why analytic work cannot repair this version

A target-dependent tilt, local central limit theorem, or Fourier major-minor arc estimate cannot assign positive probability to a window disjoint from the deterministic support lattice. The structural support must be repaired before Nova 3 inputs are relevant.

## Exact repair options

Any revised construction must satisfy at least one of the following.

### Option 1: increase correction capacity

If the main support remains inside `2^{r_n+1} Z`, enlarge the correction palette to represent every residual through

\[
2^{r_n+1}-1.
\]

A binary palette including `2^{r_n}` achieves this residual range at one additional correction term. This removes only the residue obstruction. It does not prove occupancy of the required lattice multiples.

### Option 2: lower the common address

Change the address sequence so the common factor of all main terms is at most `2^{r_n}`. The present correction radius then meets the elementary lattice-width threshold. A new endpoint proof is still required because the odd menu excludes `u=1`.

### Option 3: add residue-breaking labels

Add legal, numerically disjoint labels whose combined support supplies the missing residue classes modulo `2^{r_n+1}`. The revised handoff must state the exact residue theorem, not merely that the global gcd is `1`.

## Requirements for a revised handoff

A replacement theorem request should state:

1. the exact common lattice span of the final main sumset;
2. the exact residue classes attained modulo that span;
3. a correction radius at least as large as every residual gap that remains;
4. a proof that the first target and all endpoint targets are included;
5. the complete term cost after the correction repair;
6. whether the revised route still avoids a sequential partial-coverage invariant.

## Verification command

No computation is required for this obstruction. Verification consists of checking the valuation inequality

\[
e_t\ge r_n+1
\]

and the empty intersection

\[
[1,2^{r_n}]\cap2^{r_n+1}\mathbb Z=\varnothing.
\]

## Known limitations

This response does not reject valuation-tagged labels in general. It rejects only the exact frozen layer and correction contract at Nova 1 commit `b939574eb88a08bb03abda5bbe6ff2ca97444e08`.

## Requested next action

Revise `N1-CON-001` to remove the support-lattice mismatch, assign a new versioned theorem or construction ID, and return the revised fixed labels with an exact commit SHA.