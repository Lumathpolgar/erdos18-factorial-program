# Nova 2 Status

## Track

Additive Occupancy and Global Sumsets

## Branch

`nova/additive-occupancy`

## Overall state

`MARKER_THREE_STREAMING_CERTIFIED_N12_N46_ASYMPTOTIC_OCCUPANCY_OPEN`

## Baseline

- Startup branch head: `71370633b1e6726bf6f9e3b334d42cfc34512c06`
- Startup main head: `68ace6c9c3b67636e298a406fee3bfe8e072741d`
- Merge base: `cd5576d4f7934e26e9d4ef3b065c2ad4cee36c67`
- `docs/HANDOFF_PROTOCOL.md` was absent; `docs/CROSS_TRACK_HANDOFF_PROTOCOL.md` was used.

## Permanent obstruction record

Nova 1 handoff `N1-HO-N2-001` at commit

`b939574eb88a08bb03abda5bbe6ff2ca97444e08`

remains `REJECTED`.

Every main sum in that model lies in `2^{r_n+1} Z`, while the first required window is `[1,2^{r_n}]`. This is N2-ADD-115 and N2-OBS-107. The one-power and two-power repairs also fail exactly and remain N2-OBS-108.

## Superseded fallback route

Nova 2 proved:

- N2-ADD-116: exact lattice quotient normalization;
- N2-ADD-117: conditional three-power repair;
- N2-ADD-118: exponential deterministic prefix.

These results remain valid, but the route is no longer preferred after Nova 1 supplied the marker-three construction.

## Current preferred structural model

Nova 1 handoff `N1-HO-N2-002` was imported from:

- branch: `nova/factorial-structure`;
- exact commit: `ebb47ba436af554366d0f285119a769f31f9e561`;
- construction: `N1-CON-003`.

Outcome: `ACCEPTED_WITH_RESTRICTIONS`.

The marker-three quotient layers are

\[
B_t(n)=\{2^{t-1}u:u\text{ odd},\ 3u\mid n!,\ 2^{t-1}u\le Y_n\},
\]

where

\[
Y_n=\left\lfloor\frac{\lfloor\sqrt{n!}\rfloor}{3}\right\rfloor.
\]

The correction-window radius is

\[
W_n=\left\lfloor\frac{2^{r_n}-3}{3}\right\rfloor.
\]

The structural gate passes:

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
- N2-ADD-121: unique-parent bounded-memory divisor stream and exact record-gap compression.

At layer `t`, the exact allowable core gap is

\[
D_t(E_{t-1})
=
\left\lfloor
\frac{E_{t-1}+W_n+1}{2^{t-1}}
\right\rfloor.
\]

If the recursion reaches `Y_n-W_n`, then

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
\le M_n+r_n.
\]

N2-ADD-120 is sequential and requires a Phase 12P compatibility audit before asymptotic promotion.

## Exact finite milestones

### N2-FIN-202

Nova 2 materialized every odd core and ran the exact connected-core recursion for all

\[
12\le n\le45.
\]

Every completed case reaches `Y_n`, uses between two and six main layers, and satisfies

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
\le22.
\]

### N2-FIN-203

The former `n=46` materialization barrier is closed by N2-ADD-121.

Exact parameters:

\[
r_{46}=16,
\qquad
M_{46}=235,
\qquad
v_2(46!)=42.
\]

The complete odd-core family has `27,941,760` members. The streaming audit emits the `24,567,748` cores at most `Y_46`, retains only `631` record gaps, and reaches a maximum active frontier of `3,373,952` nodes.

Six main layers give

\[
E_6+W_{46}
=
24{,}938{,}550{,}582{,}416{,}882{,}103{,}407{,}947{,}983
>
Y_{46}
\]

with margin

\[
211{,}996{,}795{,}013{,}688{,}527{,}533{,}367{,}264.
\]

Therefore

\[
H_{46!}(\lfloor\sqrt{46!}\rfloor+1)
\le22.
\]

Artifacts:

- `proofs/MARKER_THREE_STREAMING_N46_AUDIT.md`;
- `verification/marker_three_streaming_audit.cpp`;
- `verification/test_marker_three_streaming_audit.py`;
- `verification/data/marker_three_streaming_n46.json`.

The smallest unaudited parameter is now `n=47`. A bounded `n=47` run did not complete within the available execution limit and remains `unknown due to resource limits`, not failure.

## Preferred proof engines

1. Final-only target-dependent tilt plus bounded-torus Fourier window positivity for the marker-three numerical quotient law.
2. Deterministic final restricted-sumset theorem for the same labels.
3. Connected-core carrier recursion as a finite certificate and possible sequential theorem, subject to Phase 12P.
4. The three-power valuation-tagged route as a preserved conditional fallback.

## Cross-track requests

### Nova 3

`N2-HO-N3-003` freezes the exact marker-three numerical quotient law, target windows, moments, resonances, and weighted Fourier inequality.

File: `handoffs/MARKER_THREE_REQUEST_TO_NOVA3.md`.

### Nova 4

Nova 4 must independently reconstruct N2-FIN-202 and N2-FIN-203, then extend the bounded-memory audit from `n=47`.

Files:

- `handoffs/MARKER_THREE_REQUEST_TO_NOVA4.md`;
- `handoffs/FULL_MENU_FINITE_TO_NOVA4.md`.

## Exact open blockers

1. Prove or disprove marker-three quotient occupancy uniformly through `Y_n`.
2. Replace finite carrier evidence by a uniform theorem or exact obstruction.
3. Extend bounded-memory exact certification from `n=47`.
4. Prove endpoint support near `Y_n` or produce an exact endpoint deficit.
5. Control collisions between different rainbow profiles.
6. Prove the numerical target-dependent tilt, moment, resonance, and weighted Fourier package.
7. Audit the sequential carrier theorem against the exact Phase 12P hypotheses.
8. Handle all remaining finite exceptions.

## Claim boundary

The marker-three construction passes the structural gate and every completed exact carrier audit through `n=46`. This does not prove the asymptotic factorial half-range theorem or solve Erdős Problem 18.

## Next theorem target

Reduce the streaming frontier enough to certify `n=47`, or prove a uniform upper bound for the record gaps of odd divisors of `n!/3` strong enough to force

\[
E_{M_n}+W_n\ge Y_n.
\]

The final-only Fourier route remains active so failure of the sequential engine does not terminate the full model.
