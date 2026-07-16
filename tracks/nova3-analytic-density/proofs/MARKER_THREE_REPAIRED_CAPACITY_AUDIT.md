# Independent Audit of the Repaired Marker-Three Capacity Theorems

## Imported request

This file answers Nova 1 handoff `N1-HO-N3-002` from:

- branch: `nova/factorial-structure`
- exact commit: `9febe46f2298d2726eeffa139676136963790019`
- source file: `tracks/nova1-factorial-structure/handoffs/TO_NOVA3.md`

The imported prime-count theorem is Nova 3 `N3-ANA-010`:

\[
\pi(n)-\pi(n/2)\ge\frac{n}{3\log n}
\qquad(n\ge120368).
\]

No later Nova 1 revision is used.

## Frozen notation

For every integer `n>=120368`, define

\[
X_n=\lfloor\sqrt{n!}\rfloor,
\qquad
M_n=\lceil16(\log n)^2\rceil,
\qquad
r_n=\lceil4\log n\rceil.
\]

Let

\[
P_n=\{p\text{ prime}:n/2<p\le n\},
\qquad
h_n=|P_n|,
\qquad
H_n=\prod_{p\in P_n}p.
\]

For `1<=t<=M_n`, define

\[
U_t^{(3)}(n)=
\left\{
 u\ge1:
 u\text{ odd},\ 3u\mid n!,\ 3\cdot2^{t-1}u\le X_n
\right\}.
\]

All logarithms are natural.

## N3-ANA-014, repaired marker-three menu lower bound

- Result class: `proved theorem`
- Repository status: `PROVED`
- Uniformity: every integer `n>=120368` and every `1<=t<=M_n`
- Constants: explicit and effective
- Imported dependency: N3-ANA-010

### Statement

For every integer `n>=120368` and every `1<=t<=M_n`,

\[
M_n-1\le v_2(n!),
\]

and

\[
|U_t^{(3)}(n)|
\ge2^{h_n-1}
\ge2^{n/(3\log n)-1}.
\]

The threshold remains exactly

\[
120368.
\]

### Step 1: every top-prime subset product is a legal odd core

Every prime in `P_n` is greater than `3` and has valuation exactly one in `n!`. Therefore every subset product

\[
u=\prod_{p\in S}p,
\qquad S\subseteq P_n,
\]

is odd, coprime to `3`, and satisfies

\[
3u\mid n!.
\]

Unique factorization makes all `2^{h_n}` subset products distinct.

### Step 2: complementary pairing

Complementary subsets have products `u` and `H_n/u`. Since `H_n` is squarefree and greater than one, it is not a square. Thus no subset product equals `sqrt(H_n)`, and exactly one product from each complementary pair is below `sqrt(H_n)`.

Hence exactly

\[
2^{h_n-1}
\]

distinct subset products satisfy

\[
u<\sqrt{H_n}.
\]

The unit subset product is included because the repaired menu permits `u=1`.

### Step 3: the suggested central-binomial shortcut is invalid

Nova 1 suggested using

\[
H_n\le\binom n{\lfloor n/2\rfloor}.
\]

The stated divisibility reason is false for odd `n`. Let `n=2p-1` with `p` prime. Then

\[
p\in(n/2,n],
\]

but

\[
v_p\binom{2p-1}{p-1}
=1-0-1=0.
\]

For example, `n=9` and `p=5`, while

\[
5\nmid\binom94=126.
\]

The requested menu theorem nevertheless survives through the stronger quotient-factorial argument below.

### Step 4: quotient-factorial cutoff

Put

\[
m=\lfloor n/2\rfloor.
\]

Every prime in `P_n` occurs among the integers `m+1,...,n`. Therefore

\[
H_n\mid\frac{n!}{m!},
\]

so

\[
\frac{n!}{H_n}\ge m!.
\]

It is enough to prove

\[
9\,2^{2M_n-2}<m!,
\]

because then

\[
\left(3\,2^{M_n-1}\sqrt{H_n}\right)^2<n!,
\]

and hence

\[
3\,2^{M_n-1}\sqrt{H_n}<\sqrt{n!}.
\]

For `n>=120368`, we have `n<2^17` at the threshold and hence

\[
\log120368<17.
\]

Also the function `(log x)^2/x` is decreasing for `x>e^2`. Since

\[
32\cdot17^2=9248<120368/8=15046,
\]

we obtain uniformly for every `n>=120368`

\[
32(\log n)^2<\frac n8.
\]

Because `M_n-1<16(log n)^2`, `log2<1`, and `log3<2`,

\[
\log\left(9\,2^{2M_n-2}\right)
<4+32(\log n)^2
<4+\frac n8.
\]

On the other hand, `m!>=2^{m-1}` and `log2>1/2`, so

\[
\log(m!)>(m-1)/2\ge(n-3)/4.
\]

For every `n>=120368`,

\[
\frac{n-3}{4}>4+\frac n8.
\]

Thus

\[
9\,2^{2M_n-2}<m!,
\]

as required.

Therefore every subset product `u<sqrt(H_n)` satisfies

\[
3\,2^{t-1}u
\le
3\,2^{M_n-1}u
<
\sqrt{n!}.
\]

The left side is an integer, so

\[
3\,2^{t-1}u\le\lfloor\sqrt{n!}\rfloor=X_n.
\]

All `2^{h_n-1}` small complementary subset products belong to every repaired menu.

### Step 5: exact address legality

Since `M_n-1<16(log n)^2<n/32`, while

\[
v_2(n!)\ge\lfloor n/2\rfloor,
\]

we have

\[
M_n-1\le v_2(n!).
\]

Thus the factor `2^{t-1}` is legal for every displayed layer.

### Step 6: prime-count conversion

N3-ANA-010 gives

\[
h_n\ge\frac{n}{3\log n}.
\]

Therefore

\[
|U_t^{(3)}(n)|
\ge2^{h_n-1}
\ge2^{n/(3\log n)-1}.
\]

This proves N3-ANA-014.

## N3-ANA-015, repaired marker-three formal profile capacity

- Result class: `proved theorem`
- Repository status: `PROVED`
- Uniformity: every integer `n>=120368`
- Constants: explicit and effective
- Dependency: N3-ANA-014

### Statement

For every integer `n>=120368`,

\[
2^{r_n}
\prod_{t=1}^{M_n}
\left(|U_t^{(3)}(n)|+1\right)
\ge X_n+1.
\]

### Proof

For `n>=120368`, the function `x/log x` is increasing, and at the threshold

\[
120368>12\cdot17>12\log120368.
\]

Hence

\[
\frac{n}{3\log n}-1
\ge
\frac{n}{4\log n}.
\]

By N3-ANA-014 and `M_n>=16(log n)^2`,

\[
\log_2
\prod_{t=1}^{M_n}
\left(|U_t^{(3)}(n)|+1\right)
\ge
M_n(h_n-1)
\ge
4n\log n.
\]

Also

\[
X_n+1\le2\sqrt{n!}\le2n^{n/2}.
\]

Since `log2>1/2`,

\[
\log_2(X_n+1)
\le
1+\frac{n\log n}{2\log2}
<1+n\log n
<2n\log n.
\]

Thus the repaired-menu profile exponent alone exceeds the target exponent by a factor greater than two. The additional palette factor `2^{r_n}` is nonnegative surplus. Therefore

\[
2^{r_n}
\prod_{t=1}^{M_n}
\left(|U_t^{(3)}(n)|+1\right)
\ge X_n+1.
\]

This proves N3-ANA-015.

## N3-ANA-016, central-binomial divisibility shortcut obstruction

- Result class: `disproved estimate`
- Repository status: `DISPROVED`
- Parameter range: every odd integer `n=2p-1` with prime `p`

### Statement

The claim

> every prime in `(n/2,n]` divides `binom(n,floor(n/2))`

is false.

For `n=2p-1`, the prime `p=(n+1)/2` lies in the interval but cancels against the `p!` denominator. This is an infinite counterexample family indexed by primes.

The obstruction invalidates that proof step only. It does not invalidate N3-ANA-014 or N3-ANA-015, which use the quotient-factorial bound.

## Receiver outcome

`ACCEPTED_WITH_PROOF_REPAIR`.

Both requested Nova 1 statements hold with threshold `120368`. The central-binomial divisibility argument must be replaced by

\[
n!/H_n\ge\lfloor n/2\rfloor!.
\]

## Claim boundary

These theorems prove legal menu size and formal profile capacity only. They do not prove:

- profile-sum injectivity;
- quotient occupancy;
- additive maximum-gap control;
- endpoint support;
- the factorial half-range theorem;
- Erdős Problem 18.