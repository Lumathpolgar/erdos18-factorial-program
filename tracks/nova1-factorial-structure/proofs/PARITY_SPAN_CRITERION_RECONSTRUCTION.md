# Parity-Span Carrier Criterion Reconstruction

## Results

- `N1-STR-026`: **proved theorem**, parity-span carrier lower bound.
- `N1-OBS-004`: **proved theorem**, optimality under count-threshold information.

The factorial formulation of Erdős Problem 18 remains open. These results concern only the sequential marker-three carrier engine.

## Imported source

- source branch: `nova/additive-occupancy`;
- exact source commit: `47ed3938d8900c82b245a3592502ac957330bbc6`;
- source results: `N2-ADD-124`, `N2-OBS-110`;
- source proof: `tracks/nova2-additive-occupancy/proofs/PARITY_SPAN_COUNT_THRESHOLD_CRITERION.md`.

Nova 1 independently reconstructs the statements below.

## Setup

At an executed layer write

\[
F=F_{t-1},\qquad s=2^{t-1},\qquad D=\left\lfloor\frac Fs\right\rfloor.
\]

Let

\[
0<u_1<u_2<\cdots<u_K=U
\]

be the positive odd cores in the complete zero-connected prefix. Then

\[
F_t=F+sU.
\]

## N1-STR-026

For every executed layer with `K>=1`,

\[
U\ge 2K-1.
\]

Consequently,

\[
\eta=\frac{U}{KD}\ge\frac{2K-1}{KD},
\]

and

\[
\frac{F_t}{F}>
\frac{D+2K}{D+1}.
\]

For an `L`-layer carrier, the explicit condition

\[
\prod_{t=1}^{L}\frac{D_t+2K_t}{D_t+1}
\ge
\frac{Y_n+1}{W_n+1}
\]

is sufficient for exact endpoint coverage.

### Proof

The `K` positive cores are distinct positive odd integers. Their coordinatewise smallest possible ordered values are

\[
1,3,5,\ldots,2K-1.
\]

Hence `U>=2K-1`. Since `D=floor(F/s)`,

\[
F<s(D+1).
\]

Therefore

\[
\frac{sU}{F}>
\frac{U}{D+1}
\ge
\frac{2K-1}{D+1}.
\]

Adding one proves

\[
\frac{F_t}{F}=1+\frac{sU}{F}>
\frac{D+2K}{D+1}.
\]

Multiplication over the executed layers proves the sufficient product criterion. `QED`

## N1-OBS-004

The bound `U>=2K-1` is optimal if the only inputs are:

- oddness of the positive cores;
- connected-prefix cardinality `K`;
- threshold `D`.

For every `K>=1` and `D>=2`, the abstract prefix

\[
1,3,5,\ldots,2K-1
\]

is connected and attains equality. The floor loss is also asymptotically sharp: for fixed `D`, set

\[
F=s(D+1)-1.
\]

Then `floor(F/s)=D` and

\[
\frac{sD}{F}\to\frac{D}{D+1}
\]

as `s` tends to infinity.

Thus no uniform theorem using only oddness, `K`, and `D` can improve `N1-STR-026` by a fixed positive factor. A stronger theorem must use factorial-specific internal spacing, average gaps, or a divisor-distribution statement for the reserved odd factorial core. `QED`

## Consequence for the active route

Count surplus, parity, and the first external blocking gap are not complete proof inputs. The next exact sequential quantity is

\[
A_t=\frac{U_t}{2K_t-1},
\]

or equivalently

\[
\eta_t=\frac{U_t}{K_tD_t}.
\]

This reconstruction does not prove or disprove uniform quotient occupancy, the factorial half-range theorem, or Erdős Problem 18.
