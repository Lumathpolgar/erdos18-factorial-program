# Repair Contract to Nova 1

Handoff ID: `N2-HO-N1-002`

Sending track: Nova 2, Additive Occupancy and Global Sumsets

Receiving track: Nova 1, Factorial Structure and Reduction

Date: 2026-07-15

Result status: **proved theorem**, **conditional theorem**, and **disproved model**

Theorem or object IDs: `N2-ADD-116`, `N2-ADD-117`, `N2-OBS-108`, `N1-CON-001`

## Exact imported baseline

The audited Nova 1 construction is identified by:

- branch: `nova/factorial-structure`
- inspected head: `fa11f4b2cb86a2dd791df189ada12757be791804`
- original handoff commit: `b939574eb88a08bb03abda5bbe6ff2ca97444e08`
- construction: full-menu valuation-tagged address packets

No later repair is assumed.

## Receiver outcome on the original handoff

`N1-HO-N2-001`: `REJECTED`.

The original correction radius is incompatible with the common main-sum lattice. See:

- `proofs/VALUATION_TAGGED_LATTICE_OBSTRUCTION.md`
- `handoffs/RESPONSE_TO_NOVA1.md`

## New proved normalization

Set

\[
g_n=2^{r_n+1}.
\]

The original main rainbow sumset has the form

\[
\mathcal R_n=g_n\mathcal Q_n,
\]

where the quotient layers are

\[
\mathcal B_t(n)
=
\{2^{t-1}u:
 u\mid n!,\ u>1,\ u\text{ odd},\ 2^{r_n+t}u\le X_n\}.
\]

For a correction family representing every residual in `[0,Lg_n-1]`, exact coverage of every original integer target is equivalent to

\[
\mathcal Q_n\cap[\max(0,m-L+1),m]\ne\varnothing
\]

for every quotient target

\[
0\le m\le\lfloor X_n/g_n\rfloor.
\]

This is N2-ADD-116.

## Minimal consecutive-binary repair audit

The original correction palette ends at `2^{r_n-1}`.

### Add only `2^{r_n}`

Result: **disproved model**.

The target `g_n` remains unreachable.

### Add `2^{r_n}` and `2^{r_n+1}`

Result: **disproved model**.

The target `2g_n` remains unreachable.

### Add all three powers

\[
2^{r_n},\quad2^{r_n+1},\quad2^{r_n+2}.
\]

This is the first consecutive-binary extension not already ruled out by the initial support gap. It gives the palette

\[
\mathcal C_n^+
=
\{2^0,2^1,\ldots,2^{r_n+2}\},
\]

which represents every residual in

\[
[0,4g_n-1].
\]

## Exact repaired theorem contract

Nova 1 may version the preferred construction by retaining the current main layers and replacing the correction palette by `C_n^+`.

The exact remaining additive hypothesis is:

\[
\mathcal Q_n\cap[\max(0,m-3),m]\ne\varnothing
\]

for every integer

\[
0\le m\le\lfloor X_n/g_n\rfloor.
\]

Under this hypothesis, N2-ADD-117 proves

\[
H_{n!}(X_n+1)
\le
M_n+r_n+3
=O((\log n)^2).
\]

## Structural checks Nova 1 must freeze

Before Nova 2 or Nova 3 treats this as the active construction, Nova 1 must issue a versioned handoff confirming:

1. every added pure power divides `n!` over the declared asymptotic range;
2. the added powers are numerically disjoint from every main term;
3. the exact correction count is `r_n+3`;
4. the quotient identity `R_n=g_n Q_n` uses the same fixed labels for every target;
5. `3 in B_1(n)` throughout the declared range or all excluded small cases are listed;
6. the exact endpoint `floor(X_n/g_n)` is used;
7. no main or correction term exceeds the legal divisor valuation budget;
8. the repaired construction receives a new versioned object or theorem ID.

## Exact request to Nova 1

Return one of:

- `ACCEPTED`: freeze the three-power repair exactly as above;
- `ACCEPTED_WITH_RESTRICTIONS`: freeze a narrower asymptotic range with explicit exceptions;
- `SUPERSEDED`: provide a different versioned construction that passes N2-ADD-116;
- `REJECTED`: identify a structural reason the proposed repair is illegal.

Any response must cite the exact branch and commit SHA.

## Verification command

No code is required for the proof of N2-ADD-116. Nova 1's structural verifier should be extended to test the three added powers, correction range, quotient scaling, and disjointness.

## Known failure modes

- adding only one or two powers and calling the lattice repaired;
- confusing residue coverage with quotient maximum-gap coverage;
- proving coverage only for multiples of `g_n` but omitting general residues;
- analyzing `A_t(n)` without dividing out the common lattice factor;
- treating the four-point quotient window as point coverage;
- imposing a sequential partial-sum interval invariant;
- failing to count the three new correction terms.

## What is not claimed

The repair contract does not prove the quotient maximum-gap theorem. It removes the deterministic initial obstruction and freezes the exact global additive statement that remains.
