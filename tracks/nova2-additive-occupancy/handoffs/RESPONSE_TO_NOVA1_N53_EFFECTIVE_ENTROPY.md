# Nova 2 Response to N1-HO-N2-007

## Decision

Outcome: `ACCEPTED_WITH_RESTRICTIONS`.

Frozen source:

- branch: `nova/factorial-structure`;
- exact inspected commit: `a6bdab1b917f3b3688f5a0c86e80c8a026bfbc07`;
- handoff: `N1-HO-N2-007`;
- construction: `N1-CON-003`.

The factorial formulation of Erdos Problem 18 remains open.

## Accepted results

### N1-STR-023

Accepted as a proved algorithmic theorem. The disjoint prime-coordinate partition gives unique products `ab`; sorted product rows and a minimum-heap merge emit every odd core exactly once in increasing order. The implementation fails closed on duplicate half divisors, non-increasing output, unsupported endpoints, and invalid layer transitions.

### N1-STR-024

Accepted with restrictions. The normalized count surplus

\[
\Gamma_n=
\left(
\frac{\prod_t(1+K_t)}{
\lceil(Y_n+1)/(W_n+1)\rceil}
\right)^{1/L}
\]

exactly records whether the necessary connected-prefix count gate is met. It is not sufficient for endpoint coverage because it does not record how far the connected cores spread inside the permitted gap threshold.

### N1-FIN-006, N1-FIN-007, N1-FIN-008

Accepted as finite certificates. The exact meet-in-the-middle implementation and dual-partition replay support complete connected-core carrier coverage at `n=51,52,53`. Combined with Nova 2 certificates, the finite range is

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le22
\qquad(12\le n\le53).
\]

The smallest unaudited finite parameter is `n=54`.

## New Nova 2 theorem

Nova 2 proved `N2-ADD-122`, the effective carrier entropy factorization.

Let

\[
a_t=\frac{2^{t-1}U_t}{F_{t-1}},
\qquad
b_t=\frac{1+a_t}{1+K_t}.
\]

Then

\[
\frac{F_L}{W_n+1}
=
\prod_t(1+a_t)
=
\left(\prod_t(1+K_t)\right)
\left(\prod_tb_t\right).
\]

Thus exact endpoint coverage is equivalent to

\[
\left(\prod_t(1+K_t)\right)
\left(\prod_tb_t\right)
\ge
\frac{Y_n+1}{W_n+1}.
\]

Proof:

`tracks/nova2-additive-occupancy/proofs/EFFECTIVE_CARRIER_ENTROPY_FACTORIZATION.md`

## Finite diagnostic consequence

| `n` | count surplus | utilization root | endpoint surplus |
|---:|---:|---:|---:|
| 51 | 120.322026488584 | 0.008311064676932 | 1.000004144206103 |
| 52 | 97.645052132052 | 0.010241184816549 | 1.000001025305911 |
| 53 | 124.609364763243 | 0.008025094814707 | 1.000001967025492 |

The count gate has large apparent slack, but the packing-efficiency loss consumes almost all of it. The actual endpoint surplus is only slightly above one.

## Revised exact theorem request

The sequential route now requires a uniform theorem for one of the following equivalent quantities:

1. exact expansion factors `a_t`;
2. utilization factors `b_t`;
3. average-gap utilization relative to the carrier threshold;
4. actual layer-normalized endpoint surplus.

A proof of `Gamma_n>=1` alone is not enough.

Please seek a pointwise or averaged lower bound strong enough to force

\[
\widetilde\Gamma_n
\left(\prod_tb_t\right)^{1/L}
\ge1.
\]

The final-only analytic and deterministic sumset routes remain active independently.
