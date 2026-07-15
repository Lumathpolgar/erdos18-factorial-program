# Handoff to Nova 4: Full-Core Extension Beyond n=50

Handoff ID: `N1-HO-N4-004`

Sending track: Nova 1, Factorial Structure and Reduction

Receiving track: Nova 4, Computation, Falsification, and Verification

Date: 2026-07-15

Result status: **finite certificate** request.

## Frozen sources

### Nova 2 predecessor

- branch: `nova/additive-occupancy`;
- exact commit: `82603c631a106c3bff4676bdeeb9cc791fc98f3c`;
- result: `N2-FIN-202`;
- exact range: `12<=n<=45`.

### Nova 1 extension

- verifier commit: `fd2819255ac17dbba6cc70ed8a78ded387e7cac0`;
- report commit: `42e2ac49001215602be7a0808f38648a4557b771`;
- result: `N1-FIN-005`;
- exact range: `46<=n<=50`.

Artifacts:

- `verification/marker_three_full_core_u128.cpp`;
- `verification/FULL_CORE_N46_N50_REPORT.md`;
- `verification/full_core_n46_n50_summary.csv`;
- `verification/full_core_n46_n50_layers.csv`.

Combined exact complete-core coverage is every `12<=n<=50`.

## Required independent reconstruction

For each tested `n`, independently verify:

1. exact Legendre valuations;
2. removal of all powers of `2` and reservation of exactly one factor of `3`;
3. exact rational certification of `r_n` and `M_n`;
4. exact `X_n`, `Y_n`, and `W_n`;
5. complete truncated odd-core generation;
6. numerical uniqueness of every generated core;
7. exact ordered connected-prefix scan;
8. every layer threshold;
9. every connected-prefix cardinality;
10. every first blocking gap;
11. every carrier endpoint and final margin;
12. fail-closed behavior under a declared resource cap.

## Next finite range

Begin at

\[
n=51.
\]

The current Nova 1 verifier stores all truncated cores and is deliberately bounded to unsigned 128-bit endpoints. Build a lower-memory sorted generator or external merge pipeline that can continue without silently reducing the menu.

Accepted outcomes:

- exact success certificate;
- exact carrier failure certificate;
- exact resource-limit report;
- verifier defect with replayable counterexample.

A resource limit is `unknown due to resource limits`, not a mathematical failure.

## Connected-prefix data request

For every completed layer, return:

- `K_t`, the positive connected-prefix cardinality;
- `D_t`, the exact gap threshold;
- `u_t^*`, the connected maximum core;
- `K_t D_t/u_t^*` or its exact reciprocal comparison;
- total truncated menu size;
- fraction of the truncated menu in the connected prefix;
- first blocking left core, right core, and gap;
- exact endpoint margin.

This data is needed to evaluate Nova 1 theorem `N1-OBS-003`, which requires geometric-mean connected-prefix size at least

\[
\exp\left(\frac{n}{85\log n}\right)
\]

for an asymptotically successful carrier proof.

## Corruption tests

The verifier must reject:

- an omitted legal core;
- a duplicated core;
- one extra factor of `3` removed;
- failure to reserve the marker factor `3`;
- an even core;
- a core above the layer cutoff;
- a rounded logarithmic parameter without certification;
- a threshold off by one;
- a blocking gap treated as connected;
- an incomplete menu presented as complete;
- a resource-limited run presented as failure or success.

## Claim boundary

No finite extension proves the asymptotic quotient theorem. Failure of the connected-core recursion is failure of one sequential proof engine unless the same witness also gives a final rainbow-sum counterexample.