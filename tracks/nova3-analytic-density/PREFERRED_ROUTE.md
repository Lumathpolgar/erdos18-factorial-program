# Preferred Analytic Route

## Route decision

- Decision ID: `N3-ROUTE-002`
- Status: `PROVED` as a route obstruction and ranking decision; the final local theorem remains `OPEN`
- Date: 2026-07-15

## Cross-track correction

Nova 2 has now frozen the distinction between two different analytic objects.

1. Logarithmic divisor size:
   \[
   \mathbb E e^{it\log d}.
   \]
2. Numerical additive occupancy:
   \[
   \mathbb E e^{itS_{n,x}},
   \qquad
   S_{n,x}=\sum_iY_{i,n,x}.
   \]

A theorem for the first object does not automatically control the second. Numerical additive inversion is periodic on `[-pi,pi]` and must include every nonzero resonance. This correction is accepted from Nova 2 branch `nova/additive-occupancy`, commit `45c74a5fa747551422ffcad7d3ddf22788fbe622`.

The first Nova 1 layer system is not eligible for Fourier analysis because Nova 2 proved that every main sum lies in a power-of-two sublattice that misses the first required window.

## Ranked analytic routes

### 1. Exact low-prime conditioning plus high-prime tilted logarithmic analysis

Status: `PREFERRED_FOR_INTRINSIC_DIVISOR_DENSITY`.

Split the exponent vector at a cutoff `y=y(n)`:

\[
S_n=S_{\le y}+S_{>y}.
\]

Treat `S_{<=y}` exactly or structurally. Apply an exponential tilt and a local or coarse-window theorem only to `S_{>y}`.

Quantitative reasons:

- the full model has bounded effective dimension;
- small primes retain a fixed share of total variance;
- after `y->infinity`, the largest high-prime coordinate becomes negligible compared with the tail standard deviation;
- N3-ANA-008 proves a high-prime central limit theorem;
- N3-ANA-009 gives coarse-window positivity when the width is at least a constant multiple of the largest remaining coordinate span.

This route remains the correct intrinsic route for logarithmic divisor density.

### 2. Structural gate followed by matched numerical additive Fourier analysis

Status: `PREFERRED_FOR_NOVA_2_OCCUPANCY_AFTER_REPAIR`.

The required sequence is now fixed.

1. Nova 1 proposes a versioned factorial divisor layer system.
2. Nova 2 checks the common lattice, attained residues, correction radius, first target, endpoints, numerical distinctness, and nonsequential selection rule.
3. Only after that gate passes, Nova 2 freezes the exact numerical law, weights, target windows, interval kernel, reference law, and all major arcs.
4. Nova 3 proves the matched bounded-torus estimate or returns a resonance obstruction.

No logarithmic density result may be substituted for this numerical additive theorem.

### 3. Explicit prime-band capacity certification

Status: `PROVED_SUPPORTING_ROUTE`.

N3-ANA-010 and N3-ANA-011 close Nova 1's explicit upper-half prime count and formal menu-capacity dependency with

\[
n_3=n_4=n_5=120368.
\]

This route certifies that the factorial divisor lattice contains enough legal formal profiles. It does not establish that profile sums are distinct or that they occupy every required window.

### 4. Direct saddle point with exact low-prime convolution

Status: `SECONDARY_FOR_LOGARITHMIC_WINDOWS`.

The exact tilted product identity is valid across the full bulk range. One may compute the low-prime distribution exactly, prove a local theorem for the high-prime tail, and convolve. This route is retained if a structural application supplies a fixed low-prime family and asks specifically about logarithmic divisor windows.

### 5. Full uniform-divisor Gaussian local limit

Status: `DISPROVED`.

N3-ANA-006 proves that

\[
\frac{\log d-\frac12\log(n!)}n
\]

converges to a non-Gaussian infinite convolution. A Gaussian local theorem for the full vector is false.

### 6. Unrestricted global minor-arc decay

Status: `DISPROVED`.

N3-ANA-007 proves

\[
\limsup_{|t|\to\infty}|\phi_n(t)|=1
\]

for every fixed `n`. Any viable Fourier theorem needs a bounded range, smoothing, averaging, or explicit major-arc removal.

### 7. Smooth-number lower-bound transfer

Status: `REJECTED`.

Divisors of `n!` form a constrained subset of smooth or ultrafriable sets. Lower bounds for a superset do not transfer to the subset.

## Immediate theorem target

The strongest independent next target is a compact-tilt extension of N3-ANA-009.

Freeze constants `A>0` and a high-prime cutoff `y=y(n)` with

\[
y\to\infty,
\qquad
2y\le\sqrt n.
\]

For saddle parameters whose coordinate biases stay in a compact interior range, prove uniformly:

1. lower and upper variance bounds;
2. a maximal-coordinate to standard-deviation ratio tending to zero;
3. a uniform third-moment bound;
4. a Berry-Esseen estimate;
5. positive mass in central windows of width at least a constant multiple of the largest tilted coordinate span.

This theorem can be proved without pretending that the currently rejected additive layer system is valid.

## Stop conditions

Abandon or weaken a proposed route if it requires:

- fixed-width logarithmic windows uniformly from the endpoints;
- unbounded pointwise minor-arc decay;
- a Gaussian theorem without conditioning out low primes;
- lower-bound transfer from a smooth superset;
- direct control of numerical additive sums from logarithmic divisor estimates;
- Fourier work before the layer lattice and residue gate passes;
- profile capacity treated as profile-sum injectivity.

## Next theorem target

`N3-NEXT-002`: prove the compact nonzero-tilt high-prime coarse-window theorem with explicit uniform constants, then hand it to Nova 4 for reconstruction.