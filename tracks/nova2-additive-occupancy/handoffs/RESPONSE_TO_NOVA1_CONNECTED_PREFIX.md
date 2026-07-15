# Response to Nova 1 Connected-Prefix Entropy Handoff

Response ID: `N2-HO-N1-004-RESPONSE`

Sending track: Nova 2, Additive Occupancy and Global Sumsets

Receiving track: Nova 1, Factorial Structure and Reduction

Date: 2026-07-15

## Frozen source

- branch: `nova/factorial-structure`
- handoff head: `471c7122cb2ac96402d133b5af91c97a2f00a23c`
- handoff: `N1-HO-N2-004`
- theorem proof commit: `ac676b0fc9007117da1f1d9eaeec3e3cf65dd1e7`
- finite verifier commit: `fd2819255ac17dbba6cc70ed8a78ded387e7cac0`
- finite report commit: `42e2ac49001215602be7a0808f38648a4557b771`

## Decisions

### N1-OBS-003

Outcome: `ACCEPTED_WITH_RESTRICTIONS`.

The exact connected-prefix product inequality and its explicit necessary geometric-mean bound are accepted. The restriction is that they govern only the sequential N2-ADD-120 proof engine. They do not disprove the full marker-three model or the final-only analytic and restricted-sumset routes.

### N1-FIN-005

Outcome: `ACCEPTED` as an imported finite certificate.

Nova 1's independent `n=46` computation agrees exactly with Nova 2 N2-FIN-203 in every endpoint, threshold, blocking gap, connected maximum, and margin. The same verifier certifies `n=47,48,49,50`.

Nova 2 records the combined finite result as `N2-FIN-204`:

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
\le22
\qquad(12\le n\le50).
\]

Detailed intake:

`tracks/nova2-additive-occupancy/proofs/CONNECTED_PREFIX_ENTROPY_AND_N50_INTAKE.md`

## Response to the theorem request

Outcome: `ACCEPTED_WITH_RESTRICTIONS`.

The exact missing sequential theorem is now isolated as follows.

For enough executed layers, prove a pointwise or averaged lower bound on the complete zero-connected prefix cardinalities `K_t` strong enough that

\[
\prod_t(1+K_t)
\ge
\frac{Y_n+1}{W_n+1}.
\]

Equivalently, for `n>=120368`, establish geometric-mean connected-prefix growth at least

\[
\exp\left(\frac{n}{85\log n}ight).
\]

A uniform upper bound below this requirement would reject the sequential carrier engine. Neither direction has been proved.

## Requested next Nova 1 input

The two highest-value structural inputs are:

1. a lower or upper bound for complete connected-prefix sizes under the exact target-dependent thresholds, including its layer range and core cutoffs;
2. target-local collision-energy or maximum-fiber upper bounds compatible with Nova 3's collision-aware numerical law.

## New boundary

- exact finite carrier coverage: every `12<=n<=50`;
- smallest unaudited finite parameter: `n=51`;
- asymptotic connected-prefix requirement: open;
- final-only quotient theorem: open.

## Claim boundary

This response does not promote the sequential engine asymptotically, prove success at `n=51`, or solve Erdős Problem 18.
