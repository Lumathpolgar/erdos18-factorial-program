# Average-Gap Utilization Criterion

## Results

- `N2-OBS-109`: proved obstruction theorem.
- `N2-ADD-123`: proved average-gap utilization theorem.

The factorial formulation of Erdos Problem 18 remains open. These results apply only to the sequential marker-three carrier engine.

## Frozen inputs

- Nova 2: `N2-ADD-120` and `N2-ADD-122`.
- Nova 1 branch: `nova/factorial-structure`.
- Handoff: `N1-HO-N2-009`.
- Exact handoff source commit: `6b31a320fa4c4bd4c9b2395e60faa174198e022e`.
- Imported finite objects: `N1-FIN-009`, `N1-FIN-010`, and `N1-CMP-008`.

## Setup

At an executed layer put

\[
F=F_{t-1},\qquad s=2^{t-1},\qquad D=\left\lfloor\frac{F}{s}\right\rfloor.
\]

Let

\[
0=u_0<u_1<\cdots<u_K=U
\]

be the complete zero-connected odd-core prefix. Thus every internal gap

\[
d_i=u_i-u_{i-1}\qquad(1\le i\le K)
\]

is at most `D`. Define

\[
\overline d=\frac1K\sum_{i=1}^K d_i=\frac UK,
\qquad
\eta=\frac{\overline d}{D}=\frac{U}{KD},
\qquad
\phi=\frac{sD}{F}
\]

when `K>0`. The exact utilization factor from `N2-ADD-122` is

\[
b=\frac{1+K\eta\phi}{1+K}.
\]

## N2-OBS-109: first-blocking-gap non-identifiability

For every even integer `D>=4`, set

\[
K=D,\qquad F=D,\qquad s=1,\qquad g=D+2.
\]

Consider the two odd-core prefixes

\[
u_i=2i-1
\]

and

\[
v_i=iD-1
\]

for `1<=i<=K`. In both cases append a next odd core at distance exactly `g` from the connected maximum.

Both prefixes have:

- the same threshold `D`;
- the same connected-prefix count `K=D`;
- the same first blocking gap `g=D+2`;
- the same ratio
  \[
  \frac gD=1+\frac2D\longrightarrow1.
  \]

All internal gaps are at most `D`. However their average-gap factors are

\[
\eta_{\rm dense}=\frac{2D-1}{D^2}\longrightarrow0
\]

and

\[
\eta_{\rm packed}=\frac{D^2-1}{D^2}\longrightarrow1.
\]

Because `phi=1`, their exact utilization factors are

\[
b_{\rm dense}=\frac{3D-1}{D(D+1)}\longrightarrow0
\]

and

\[
b_{\rm packed}=1-\frac1{D(D+1)}\longrightarrow1.
\]

Therefore even the triple `(D,K,g)`, including a first-blocking ratio tending to one, does not determine or uniformly lower-bound `eta` or `b`. In particular, a theorem of the form `g/D<=C` alone cannot control sequential utilization for any fixed `C>1`.

### Proof

For the first prefix the gaps are `1,2,2,...,2`. For the second they are `D-1,D,D,...,D`. Since `D` is even, every listed core is odd. The appended gap `D+2` is even and exceeds `D`, so it is the first blocking gap in both constructions. Substitution gives the displayed formulas. `QED`

## N2-ADD-123: average-gap utilization sandwich

For every executed layer with `K>0`,

\[
\frac{D}{D+1}<\phi\le1.
\]

Consequently, if certified numbers `rho` and `sigma` satisfy

\[
0\le\rho\le\eta\le\sigma\le1,
\]

then

\[
\frac{1+K\rho D/(D+1)}{1+K}
< b
\le
\frac{1+K\sigma}{1+K}.
\]

For an `L`-layer carrier define

\[
\widetilde\Gamma=
\left(
\frac{\prod_{t=1}^L(1+K_t)}{(Y_n+1)/(W_n+1)}
\right)^{1/L}.
\]

A sufficient condition for endpoint success is

\[
\widetilde\Gamma
\left(
\prod_{t=1}^L
\frac{1+K_t\rho_tD_t/(D_t+1)}{1+K_t}
\right)^{1/L}
\ge1.
\]

Conversely, a sufficient condition for endpoint failure of this sequential engine is

\[
\widetilde\Gamma
\left(
\prod_{t=1}^L
\frac{1+K_t\sigma_t}{1+K_t}
\right)^{1/L}
<1.
\]

### Proof

From `D=floor(F/s)` one has

\[
sD\le F<s(D+1),
\]

which gives

\[
\frac{D}{D+1}<\frac{sD}{F}\le1.
\]

The exact formula

\[
b=\frac{1+K\eta\phi}{1+K}
\]

is increasing in both `eta` and `phi`, proving the layerwise bounds. Multiplying the lower bounds and using the exact factorization

\[
\Delta=\widetilde\Gamma\left(\prod_tb_t\right)^{1/L}
\]

proves the success criterion. Multiplying the upper bounds proves the failure criterion. `QED`

## Consequence for the Nova 1 gap diagnostic

The finite observation

\[
\max g_t/D_t<1.108
\]

for the blocked layers through `n=55` is valid computational evidence, but `N2-OBS-109` proves that this statistic cannot imply a utilization lower bound. The required structural statistic is an internal-span or average-internal-gap bound, equivalently a bound on

\[
\eta_t=\frac{U_t}{K_tD_t}.
\]

## Claim boundary

These results neither prove nor disprove uniform marker-three quotient occupancy. They only identify the exact missing statistic for the sequential carrier engine. Final-only restricted-sumset and Fourier routes remain unaffected.