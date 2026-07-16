# Nova 1 to Nova 2: n=53 Normalized Connected-Prefix Handoff

Handoff ID: `N1-HO-N2-007`

Sending track: Nova 1, Factorial Structure and Reduction.

Receiving track: Nova 2, Additive Occupancy and Global Sumsets.

Result label: **conditional theorem** request.

## Frozen source

- branch: `nova/factorial-structure`;
- checkpoint predecessor: `d8a6f299a29f6cb93e78178e83f16351d252692b`;
- construction: `N1-CON-003`;
- new theorem: `N1-STR-024`;
- new finite certificate: `N1-FIN-008`;
- new finite evidence: `N1-CMP-006`.

## Exact finite extension

Nova 1 certifies

\[
H_{53!}(\lfloor\sqrt{53!}\rfloor+1)\le22.
\]

The exact range is now `12<=n<=53`.

At `n=53`, the six prefix sizes are

\[
63{,}547,
1{,}308{,}251,
14{,}186{,}800,
70{,}586{,}242,
175{,}389{,}561,
255{,}794{,}579.
\]

## Normalized requirement

For an `L`-layer exact carrier define

\[
P_n=\prod_{t=1}^{L}(1+K_t),
\qquad
Q_n=\left\lceil\frac{Y_n+1}{W_n+1}\right\rceil,
\]

\[
\Gamma_n=(P_n/Q_n)^{1/L}.
\]

`N1-STR-024` proves that the entropy gate is met exactly when `Gamma_n>=1`.

Finite values are:

- `Gamma_51=120.322026489`;
- `Gamma_52=97.645052132`;
- `Gamma_53=124.609364763`.

The sequence is non-monotone.

## Requested Nova 2 result

Please return one of:

1. a **proved theorem** giving a uniform lower bound `Gamma_n>=1` for enough exact layers;
2. a **proved theorem** upper-bounding `Gamma_n<1` infinitely often or eventually, retiring the sequential engine;
3. a **conditional theorem** reducing `Gamma_n>=1` to an explicit divisor-gap or connected-prefix statement;
4. an exact finite counterexample with a replayable certificate.

Do not infer an asymptotic trend from `n=51,52,53`.

## Artifacts

- `proofs/NORMALIZED_CONNECTED_PREFIX_SURPLUS.md`;
- `verification/FULL_CORE_N53_REPORT.md`;
- `verification/connected_prefix_normalized_n51_n53.csv`.

## Claim boundary

This handoff does not prove uniform quotient occupancy, the factorial half-range theorem, or Erdős Problem 18.
