# Nova 2 Status

## Track and branch

- Track: Additive Occupancy and Global Sumsets
- Branch: `nova/additive-occupancy`
- Overall state: `MARKER_THREE_CERTIFIED_N12_N53_EFFECTIVE_UTILIZATION_OPEN`

The factorial formulation of Erdos Problem 18 remains open.

## Preferred marker-three model

Frozen structural source:

- branch: `nova/factorial-structure`;
- commit: `ebb47ba436af554366d0f285119a769f31f9e561`;
- construction: `N1-CON-003`;
- Nova 2 outcome: `ACCEPTED_WITH_RESTRICTIONS`.

The exact quotient layers are

\[
B_t(n)=\{2^{t-1}u:u\text{ odd},\ 3u\mid n!,\ 2^{t-1}u\le Y_n\},
\]

with

\[
Y_n=\left\lfloor\frac{\lfloor\sqrt{n!}\rfloor}{3}\right\rfloor,
\qquad
W_n=\left\lfloor\frac{2^{r_n}-3}{3}\right\rfloor.
\]

The structural gate passes, but global quotient occupancy remains open.

## Deterministic theorem package

Nova 2 proved:

- `N2-ADD-119`: translated carrier blocks;
- `N2-ADD-120`: connected-core recursion;
- `N2-ADD-121`: exact unique-parent divisor stream;
- `N2-ADD-122`: effective carrier entropy factorization.

For `F_t=E_t+W_n+1`, scale `s_t=2^{t-1}`, connected maximum `U_t`, and connected-prefix count `K_t`, define

\[
a_t=\frac{s_tU_t}{F_{t-1}},
\qquad
b_t=\frac{1+a_t}{1+K_t}.
\]

Then exactly

\[
\frac{F_L}{W_n+1}
=
\left(\prod_t(1+K_t)\right)
\left(\prod_tb_t\right).
\]

Thus prefix cardinality is only one factor. The sequential route must also control packing utilization.

## Connected-prefix intake

Nova 1 theorem `N1-OBS-003` remains accepted with restrictions as a necessary count condition:

\[
\prod_t(1+K_t)\ge\frac{Y_n+1}{W_n+1}.
\]

Nova 1 results `N1-STR-023` and `N1-STR-024` were inspected at

`nova/factorial-structure@a6bdab1b917f3b3688f5a0c86e80c8a026bfbc07`.

Decisions:

- meet-in-the-middle exact divisor stream: `ACCEPTED`;
- normalized count surplus `Gamma_n`: `ACCEPTED_WITH_RESTRICTIONS`;
- finite certificates at `n=51,52,53`: `ACCEPTED` as finite results.

Response:

`handoffs/RESPONSE_TO_NOVA1_N53_EFFECTIVE_ENTROPY.md`.

## Exact finite range

- `N2-FIN-202`: `12<=n<=45`;
- `N2-FIN-203`: `n=46`;
- `N2-FIN-204`: `47<=n<=50`;
- `N2-FIN-205`: `51<=n<=53`.

Combined:

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le22
\qquad(12\le n\le53).
\]

The smallest unaudited finite parameter is `n=54`.

## Effective-entropy diagnostics

| `n` | count surplus | utilization root | endpoint surplus |
|---:|---:|---:|---:|
| 51 | 120.322026488584 | 0.008311064676932 | 1.000004144206103 |
| 52 | 97.645052132052 | 0.010241184816549 | 1.000001025305911 |
| 53 | 124.609364763243 | 0.008025094814707 | 1.000001967025492 |

The count surplus is large, but utilization consumes almost all of it. These values are finite diagnostics only.

## Preferred proof engines

1. Final-only target-dependent numerical tilt and aggregate phase dispersion.
2. Deterministic final restricted-sumset growth.
3. Connected-core recursion, now subject to effective utilization and Phase 12P.
4. Preserved three-power fallback.

## Cross-track requests

### Nova 1

Prove a pointwise or averaged lower bound for exact expansion or utilization factors strong enough that

\[
\widetilde\Gamma_n\mathcal B_n\ge1.
\]

### Nova 3

Continue aggregate odd-core phase dispersion, collision-aware reference laws, and the strict weighted Fourier inequality.

### Nova 4

Independently reconstruct the finite certificates through `n=53`, the effective-entropy identities, and extend from `n=54`.

## Exact open blockers

1. Uniform marker-three quotient occupancy through `Y_n`.
2. A utilization lower bound closing `widetilde Gamma_n B_n>=1`, or an upper bound retiring the sequential engine.
3. Exact finite extension from `n=54`.
4. Uniform endpoint-window coverage.
5. Target-local collision multiplicity or additive-energy control.
6. Aggregate numerical phase dispersion and strict weighted Fourier positivity.
7. Phase 12P compatibility.
8. Remaining finite exceptions.

## Claim boundary

Exact coverage through `n=53` and N2-ADD-122 do not prove asymptotic occupancy, the factorial half-range theorem for all sufficiently large `n`, or Erdos Problem 18.

## Next theorem target

Prove a uniform lower bound for the geometric mean of the utilization factors `b_t`, or equivalently enough average-gap utilization, that offsets the exact count surplus and forces true endpoint growth.
