# Preferred Analytic Route

## Route decision

- Decision ID: `N3-ROUTE-001`
- Status: `PROVED` as a route obstruction and ranking decision; the preferred theorem remains `OPEN`
- Date: 2026-07-15

## Ranked routes

### 1. Low-prime conditioning plus high-prime tilted local analysis

Status: `PREFERRED`.

Split the exponent vector at a cutoff `y=y(n)`:

\[
S_n=S_{\le y}+S_{>y}.
\]

Treat `S_{<=y}` exactly or structurally. Apply an exponential tilt and a local or coarse-window theorem only to `S_{>y}`. The reason is quantitative:

- the full model has bounded effective dimension;
- small primes retain a fixed share of the total variance;
- after `y->infinity`, the largest high-prime coordinate becomes negligible compared with the tail standard deviation;
- `N3-ANA-008` then proves a high-prime central limit theorem;
- `N3-ANA-009` gives rigorous coarse-window positivity at width at least a constant multiple of the largest remaining coordinate span.

The next analytic target is to lower the admissible width below that coordinate span by proving a bounded-frequency characteristic-function estimate for a selected high-prime band.

### 2. Direct saddle point with exact low-prime convolution

Status: `SECONDARY`.

The exact tilted product identity is valid across the full bulk range. One may compute the low-prime distribution exactly, prove a local theorem for the high-prime tail, and convolve. This route is mathematically compatible with Route 1 but places more bookkeeping into a single theorem. It is retained if Nova 1 supplies a fixed low-prime structure that makes the convolution finite and explicit.

### 3. Full uniform-divisor Gaussian local limit

Status: `DISPROVED`.

`N3-ANA-006` proves that

\[
\frac{\log d-\frac12\log(n!)}n
\]

for a uniformly selected divisor converges to a non-Gaussian infinite convolution. The limiting characteristic function has zeros inherited from small-prime uniform coordinates. A Gaussian local theorem for the full vector is therefore false.

### 4. Unrestricted global minor-arc decay

Status: `DISPROVED`.

`N3-ANA-007` proves

\[
\limsup_{|t|\to\infty}|\phi_n(t)|=1
\]

for every fixed `n`. Any viable Fourier theorem must have a bounded frequency range, smoothing, averaging, or explicit major-arc removal.

### 5. Smooth-number lower-bound transfer

Status: `REJECTED`.

Divisors of `n!` form a constrained subset of smooth or ultrafriable sets. Lower bounds for a superset do not transfer to the subset. No source audited in this checkpoint supplies deterministic local lower bounds for the exact factorial divisor set.

## Preferred theorem target

Freeze a prime band

\[
P=(y,2y],\qquad y\to\infty,\qquad 2y\le\sqrt n,
\]

and a compact tilt range. Prove a bounded-frequency estimate sufficient to upgrade `N3-ANA-009` from windows

\[
\Delta\gg M_{n,y}
\]

to the smallest width actually requested by Nova 2. The theorem must be stated only after Nova 2 supplies the exact inversion cutoff and main-term scale.

## Why this route can support the repository target

The structural track can use low-prime exponents for deterministic control and high-prime exponents for entropy. The additive track can use the high-prime component as a diffuse convolution factor. This division directly exploits factorial valuation multiplicity and avoids the historical one-choice sequential architectures obstructed in Phases 12L and 12P.

## Exact current deliverable

The strongest current positive theorem is:

> After removing primes at most `y`, with `y->infinity` and `2y<=sqrt n`, the centered uniform logarithmic contribution of the remaining prime exponents is asymptotically Gaussian. Under Berry-Esseen, every central window of width at least `K M_{n,y}` has probability at least a constant multiple of `Delta/B_{n,y}`.

This is not yet fine enough to imply local additive occupancy. It is, however, a proved analytic regime with explicit scale and a precise next obstruction.

## Stop conditions

Abandon or weaken this route if any receiving track requires:

- fixed-width logarithmic windows uniformly from the endpoints;
- an unbounded pointwise minor-arc theorem;
- a Gaussian theorem without conditioning out low primes;
- a lower-bound transfer from a smooth superset;
- direct Fourier control of additive divisor values from logarithmic-size estimates.

## Next theorem target

`N3-NEXT-001`: Given an explicit finite inversion range from Nova 2, prove an averaged minor-arc estimate for a high-prime band under a compact exponential tilt, or prove that the requested frequency range contains unavoidable resonant sets too large for the intended main term.
