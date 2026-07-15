# Nova 2 Status

## Track

Additive Occupancy and Global Sumsets

## Branch

`nova/additive-occupancy`

## Overall state

`MARKER_THREE_CERTIFIED_N12_N50_CONNECTED_PREFIX_ASYMPTOTICS_OPEN`

## Baseline

- Startup branch head: `71370633b1e6726bf6f9e3b334d42cfc34512c06`
- Startup main head: `68ace6c9c3b67636e298a406fee3bfe8e072741d`
- Merge base: `cd5576d4f7934e26e9d4ef3b065c2ad4cee36c67`
- `docs/CROSS_TRACK_HANDOFF_PROTOCOL.md` governs this track.

## Permanent obstruction record

Nova 1 handoff `N1-HO-N2-001` at commit

`b939574eb88a08bb03abda5bbe6ff2ca97444e08`

remains rejected by N2-ADD-115 and N2-OBS-107. The one-power and two-power repairs remain rejected by N2-OBS-108.

N2-ADD-116 through N2-ADD-118 preserve an exact normalized fallback route, but marker-three is preferred.

## Preferred marker-three model

Structural source:

- branch: `nova/factorial-structure`;
- commit: `ebb47ba436af554366d0f285119a769f31f9e561`;
- construction: `N1-CON-003`;
- Nova 2 outcome: `ACCEPTED_WITH_RESTRICTIONS`.

The quotient layers are

\[
B_t(n)=\{2^{t-1}u:u\text{ odd},\ 3u\mid n!,\ 2^{t-1}u\le Y_n\},
\]

where

\[
Y_n=\left\lfloor\frac{\lfloor\sqrt{n!}\rfloor}{3}\right\rfloor,
\qquad
W_n=\left\lfloor\frac{2^{r_n}-3}{3}\right\rfloor.
\]

Accepted structural facts:

- exact main lattice `3 Z`;
- quotient span one;
- exact 2-adic layer separation;
- main-palette numerical disjointness;
- exact correction reduction;
- term cost at most `M_n+r_n`.

## Deterministic theorem package

Nova 2 proved:

- N2-ADD-119: translated carrier-block lemma;
- N2-ADD-120: connected-core recursion sufficient for complete marker-three quotient occupancy;
- N2-ADD-121: unique-parent increasing odd-divisor stream and exact record-gap compression.

The exact layer threshold is

\[
D_t(E_{t-1})
=
\left\lfloor
\frac{E_{t-1}+W_n+1}{2^{t-1}}
\right\rfloor.
\]

If `E_L+W_n>=Y_n`, then

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
\le L+r_n.
\]

The sequential engine still requires a Phase 12P compatibility audit before asymptotic promotion.

## Connected-prefix entropy intake

Nova 1 theorem `N1-OBS-003` was imported from proof commit

`ac676b0fc9007117da1f1d9eaeec3e3cf65dd1e7`

with outcome `ACCEPTED_WITH_RESTRICTIONS`.

If `K_t` is the number of positive cores in the complete zero-connected prefix, carrier success requires

\[
\prod_{t=1}^{L}(1+K_t)
\ge
\frac{Y_n+1}{W_n+1}.
\]

For every `n>=120368`, success within the frozen layer budget requires geometric-mean connected-prefix size at least

\[
\exp\left(\frac{n}{85\log n}\right).
\]

This is a necessary condition for N2-ADD-120 only. It neither proves nor disproves the complete connected-prefix growth.

## Exact finite milestones

### N2-FIN-202

Nova 2 materialized every complete truncated odd-core menu and certified full endpoint reach for every

\[
12\le n\le45.
\]

### N2-FIN-203

Nova 2's bounded-memory stream independently certified `n=46`. Six main layers give

\[
H_{46!}(\lfloor\sqrt{46!}\rfloor+1)
\le22.
\]

### N2-FIN-204

Nova 1 finite certificate `N1-FIN-005` was accepted from verifier commit

`fd2819255ac17dbba6cc70ed8a78ded387e7cac0`

and report commit

`42e2ac49001215602be7a0808f38648a4557b771`.

Its independent `n=46` record matches N2-FIN-203 exactly, and the same verifier certifies `n=47,48,49,50`.

Therefore exact complete-core carrier coverage is established for every

\[
12\le n\le50,
\]

with

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
\le22.
\]

The smallest unaudited finite parameter is `n=51`.

Detailed intake:

`proofs/CONNECTED_PREFIX_ENTROPY_AND_N50_INTAKE.md`.

## Collision boundary

Nova 1 theorem `N1-COL-001` proves exponentially large profile fibers. Nova 2 accepts this with restrictions: raw profile count is not support cardinality, but the collision lower bound does not itself disprove window occupancy.

The next relevant quantity is target-local collision multiplicity or additive energy.

## Preferred proof engines

1. Final-only target-dependent numerical tilt and aggregate bounded-torus phase dispersion.
2. Deterministic final restricted-sumset theorem.
3. Complete connected-core recursion, subject to the entropy requirement and Phase 12P.
4. Three-power valuation-tagged fallback.

## Cross-track requests

### Nova 1

Active response:

`handoffs/RESPONSE_TO_NOVA1_CONNECTED_PREFIX.md`.

Requested inputs:

- connected-prefix lower or upper bounds under exact thresholds;
- target-local collision-energy upper bounds.

### Nova 3

Active exact numerical law: `N2-HO-N3-003`.

Nova 3's aggregate phase-dispersion and collision-aware reference-law frontier remains active.

### Nova 4

Active reconstruction requests include N2-FIN-202, N2-FIN-203, N2-ADD-121, and the accepted N1-FIN-005 extension through `n=50`.

## Exact open blockers

1. Prove or disprove marker-three quotient occupancy uniformly through `Y_n`.
2. Prove the connected-prefix product requirement is attainable, or upper-bound it strongly enough to retire the sequential engine.
3. Extend exact finite certification from `n=51`.
4. Prove endpoint-window coverage uniformly, not merely total support reach.
5. Upper-bound target-local collision multiplicity or additive energy.
6. Prove aggregate numerical phase dispersion and the strict weighted Fourier inequality.
7. Audit N2-ADD-120 against Phase 12P.
8. Handle the remaining finite exceptions.

## Claim boundary

Exact carrier coverage through `n=50` is finite. It does not prove asymptotic occupancy, the factorial half-range theorem for all sufficiently large `n`, or Erdős Problem 18.

## Next theorem target

Determine whether complete zero-connected prefixes can satisfy

\[
\left(\prod_{t=1}^{L}(1+K_t)\right)^{1/L}
\ge
\exp\left(\frac{n}{85\log n}\right)
\]

uniformly across enough layers, or prove a contrary upper bound. In parallel, continue Nova 3's final-only aggregate phase-dispersion route.
