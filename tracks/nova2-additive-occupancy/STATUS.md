# Nova 2 Status

## Track

Additive Occupancy and Global Sumsets

## Branch

`nova/additive-occupancy`

## Overall state

`MARKER_THREE_FULL_MENU_CERTIFIED_N12_N45_ASYMPTOTIC_OCCUPANCY_OPEN`

## Baseline

- Startup branch head: `71370633b1e6726bf6f9e3b334d42cfc34512c06`
- Startup main head: `68ace6c9c3b67636e298a406fee3bfe8e072741d`
- Merge base: `cd5576d4f7934e26e9d4ef3b065c2ad4cee36c67`
- `docs/HANDOFF_PROTOCOL.md` was absent; `docs/CROSS_TRACK_HANDOFF_PROTOCOL.md` was used.

## Permanent obstruction record

Nova 1 handoff `N1-HO-N2-001` at commit

`b939574eb88a08bb03abda5bbe6ff2ca97444e08`

remains `REJECTED`.

Every main sum in that model lies in `2^{r_n+1} Z`, while the first required window is `[1,2^{r_n}]`. This is N2-ADD-115 and N2-OBS-107.

The one-power and two-power consecutive-binary repairs also fail exactly. They are N2-OBS-108.

## Superseded fallback route

Nova 2 proved:

- N2-ADD-116: exact lattice quotient normalization;
- N2-ADD-117: conditional three-power repair;
- N2-ADD-118: exponential deterministic prefix for that repair.

These results remain valid, but the route is no longer preferred after Nova 1 supplied the marker-three construction.

## Current preferred structural model

Nova 1 handoff `N1-HO-N2-002` was imported from:

- branch: `nova/factorial-structure`;
- exact commit: `ebb47ba436af554366d0f285119a769f31f9e561`;
- construction: `N1-CON-003`.

Outcome: `ACCEPTED_WITH_RESTRICTIONS`.

Response:

`handoffs/RESPONSE_TO_NOVA1_MARKER_THREE.md`

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

Nova 1 proves downward one-density through

\[
m_n(2^{M_n}-1),
\]

where `m_n` is the largest odd integer at most `n`.

Nova 2 proved:

- N2-ADD-119: translated carrier-block lemma;
- N2-ADD-120: connected-core recursion sufficient for complete marker-three quotient occupancy.

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

## Exact finite milestone N2-FIN-202

Nova 2 generated every odd core and ran the exact connected-core recursion for every

\[
12\le n\le45.
\]

Result:

- all 34 completed cases reach the full quotient endpoint `Y_n`;
- two layers suffice for `12<=n<=14`;
- three layers suffice for `15<=n<=19`;
- four layers suffice for `20<=n<=25`;
- five layers suffice for `26<=n<=38`;
- six layers suffice for `39<=n<=45`;
- every completed case satisfies the exact finite bound
  \[
  H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le22.
  \]

At `n=45`, the full odd-core menu contains `18,627,840` values and six layers reach the endpoint. At `n=46`, the exact core count is `27,941,760`, above the declared `20,000,000` generation cap. The status at `n=46` is resource-limited, not failure.

Artifacts:

- `proofs/MARKER_THREE_FINITE_FULL_MENU_AUDIT.md`;
- `verification/marker_three_full_menu_audit.py`;
- `verification/data/marker_three_full_menu_n12_n45.manifest.json`;
- `verification/data/marker_three_full_menu_n12_n45.csv`.

## Preferred proof engines

1. Final-only target-dependent tilt plus bounded-torus Fourier window positivity for the marker-three numerical quotient law.
2. Deterministic final restricted-sumset theorem for the same labels.
3. Connected-core carrier recursion as a finite certificate and possible sequential theorem, subject to Phase 12P.
4. The three-power valuation-tagged route as a preserved conditional fallback.

## Cross-track requests

### Nova 3

`N2-HO-N3-003` freezes the exact marker-three numerical quotient law, target windows, moments, resonances, and weighted Fourier inequality.

File:

`handoffs/MARKER_THREE_REQUEST_TO_NOVA3.md`

### Nova 4

`N2-HO-N4-002` requests structural replay, connected-core recursion, exact full quotient reachability where feasible, deterministic-prefix replay, and endpoint support auditing.

Nova 2 has independently completed the full-menu finite carrier audit through `n=45`; Nova 4 should now reconstruct N2-FIN-202 and extend it with a bounded-memory or streaming generator.

File:

`handoffs/MARKER_THREE_REQUEST_TO_NOVA4.md`

## Exact open blockers

1. Prove or disprove marker-three quotient occupancy uniformly through `Y_n`.
2. Replace the finite connected-core evidence by a uniform theorem or exact obstruction.
3. Extend exact finite certification beyond `n=45` without materializing every odd core.
4. Prove endpoint support near `Y_n` or produce an exact endpoint deficit.
5. Control collisions between different rainbow profiles.
6. Prove the numerical target-dependent tilt, moment, resonance, and weighted Fourier package.
7. Audit the sequential carrier theorem against the exact Phase 12P hypotheses.
8. Handle all remaining finite exceptions.

## Claim boundary

The marker-three construction passes the structural gate and every completed full-menu finite carrier audit. It does not yet prove the asymptotic factorial half-range theorem or solve Erdős Problem 18.

## Next theorem target

Develop a streaming sorted odd-divisor generator that can certify the connected component without storing the complete menu, beginning at `n=46`. In parallel, formulate and prove the weakest uniform divisor-gap statement that forces

\[
E_{M_n}+W_n\ge Y_n.
\]

The final-only Fourier route remains active so failure of the sequential engine does not terminate the full model.
