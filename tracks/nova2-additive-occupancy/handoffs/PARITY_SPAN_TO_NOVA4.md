# Nova 2 to Nova 4: Parity-Span Reconstruction and Finite Deficit Replay

Handoff ID: `N2-HO-N4-007`

## Scope

Independently reconstruct `N2-ADD-124`, `N2-OBS-110`, and finite diagnostic `N2-CMP-206` without importing Nova 2 arithmetic as trusted output.

## Frozen Nova 2 source

- branch: `nova/additive-occupancy`;
- proof commit: `7bbbc03c3f1cfa14aabf88607d0559896c781d92`;
- verifier commit: `20a66db640c82dd12852f315d689b3afdb9e4a84`;
- proof: `tracks/nova2-additive-occupancy/proofs/PARITY_SPAN_COUNT_THRESHOLD_CRITERION.md`;
- verifier: `tracks/nova2-additive-occupancy/verification/parity_span_count_threshold_sanity.py`.

## Theorem to reconstruct

For an executed layer with positive odd cores

\[
0<u_1<\cdots<u_K=U,
\]

threshold

\[
D=\left\lfloor\frac Fs\right\rfloor,
\]

and update `F'=F+sU`, verify

\[
U\ge2K-1,
\]

\[
\frac{F'}F>
\frac{D+2K}{D+1},
\]

and

\[
b>
\frac{D+2K}{(D+1)(K+1)}.
\]

Verify that the product of the layer expansion bounds is a sufficient endpoint criterion.

## Optimality object

Independently check that

\[
1,3,5,\ldots,2K-1
\]

attains the minimum odd span for every `D>=2`, and that choosing

\[
F=s(D+1)-1
\]

makes the floor factor approach its lower endpoint. Decide whether any fixed-factor strengthening is possible from only oddness, `K`, and `D`.

## Finite replay

Using independent parsing of the exact Nova 1 carrier outputs for `n=51,52,53,54,55`, recompute

\[
\left(
\frac{
\prod_t(D_t+2K_t)/(D_t+1)
}{
(Y_n+1)/(W_n+1)
}
\right)^{1/6}.
\]

Expected diagnostic intervals:

- `n=51`: `(0.0000257773398727324, 0.0000257773398727325)`;
- `n=52`: `(0.0000185652131315783, 0.0000185652131315784)`;
- `n=53`: `(0.0000139117330218276, 0.0000139117330218278)`;
- `n=54`: `(0.0000099773478868399, 0.0000099773478868400)`;
- `n=55`: `(0.0000076195853058401, 0.0000076195853058402)`.

## Required decision

Return one of:

- `ACCEPTED`;
- `NEEDS_REPAIR`, with the first exact failing identity or replay row;
- `REJECTED`, with a mathematical counterexample.

Then continue exact finite carrier certification from `n=56` with fail-closed resource handling.

## Claim boundary

A successful reconstruction does not prove asymptotic quotient occupancy, the factorial half-range theorem, or Erdos Problem 18.