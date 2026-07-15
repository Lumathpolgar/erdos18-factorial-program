# Quotient Binary-Spine Prefix Occupancy

## Result IDs

- `N2-ADD-118`: proved theorem
- `N2-FIN-201`: finite certificate

## Purpose

The three-power repair from N2-ADD-117 reduces the remaining factorial problem to four-point occupancy of the normalized final rainbow sumset

\[
\mathcal Q_n\cap[\max(0,m-3),m]\ne\varnothing.
\]

This file proves that the repaired valuation-tagged route survives far beyond the initial quotient targets `m=0,1,2,3`. It does not prove global quotient occupancy.

## Frozen normalized model

Let

\[
r_n=\lceil4\log n\rceil,
\qquad
M_n=\lceil16(\log n)^2\rceil,
\qquad
g_n=2^{r_n+1},
\qquad
X_n=\lfloor\sqrt{n!}\rfloor,
\]

and

\[
Y_n=\left\lfloor\frac{X_n}{g_n}\right\rfloor.
\]

For `1<=t<=M_n`, define

\[
\mathcal B_t(n)
=
\left\{
2^{t-1}u:
 u\mid n!,
 u>1,
 u\text{ odd},
 2^{t-1}u\le Y_n
\right\}.
\]

The normalized final rainbow sumset is

\[
\mathcal Q_n
=
\left\{
\sum_{t=1}^{M_n}b_t:
 b_t\in\mathcal B_t(n)\cup\{0\}
\right\}.
\]

At most one numerical value is selected from each layer.

## N2-ADD-118: binary-spine prefix theorem

### Statement

Let `n>=7`. Let `J` satisfy

\[
1\le J\le M_n,
\qquad
Y_n\ge 7,
\qquad
3\cdot2^{J-1}\le Y_n.
\]

Then every odd integer

\[
3\le q\le 6\cdot2^{J-1}-3
\]

belongs to `Q_n`. Consequently,

\[
\mathcal Q_n\cap[\max(0,m-3),m]\ne\varnothing
\]

for every integer

\[
0\le m\le 6\cdot2^{J-1}=3\cdot2^J.
\]

Every constructed quotient sum uses at most `J` numerically distinct terms.

### Proof

Because `n>=7`, each of `3`, `5`, and `7` divides `n!`. The assumptions `Y_n>=7` and `3*2^{J-1}<=Y_n` imply

\[
3,5,7\in\mathcal B_1(n)
\]

and

\[
3\cdot2^{t-1}\in\mathcal B_t(n)
\qquad(2\le t\le J).
\]

Fix an odd integer

\[
3\le q\le6\cdot2^{J-1}-3.
\]

Choose

\[
d(q)=
\begin{cases}
3,&q\equiv3\pmod 6,\\
5,&q\equiv5\pmod 6,\\
7,&q\equiv1\pmod 6.
\end{cases}
\]

Then `d(q)` belongs to `B_1(n)`, and

\[
k=\frac{q-d(q)}6
\]

is a nonnegative integer. Since the largest possible value of `k` occurs when `q=6*2^{J-1}-3` and `d(q)=3`,

\[
0\le k\le2^{J-1}-1.
\]

Write the binary expansion

\[
k=\sum_{j=0}^{J-2}\varepsilon_j2^j,
\qquad
\varepsilon_j\in\{0,1\}.
\]

Then

\[
q
=d(q)+6k
=d(q)+\sum_{j=0}^{J-2}\varepsilon_j\,3\cdot2^{j+1}.
\]

The base value `d(q)` is selected from layer `1`. For every bit `epsilon_j=1`, the value

\[
3\cdot2^{j+1}
\]

is selected from layer `t=j+2`. Thus at most one term is selected from each layer. The selected numerical values are distinct because their 2-adic valuations are respectively `0,1,2,...`. Therefore `q` belongs to `Q_n` and uses at most `J` terms.

Let

\[
B=6\cdot2^{J-1}-3.
\]

For every target `3<=m<=B`, the largest odd integer not exceeding `m` lies in `[m-1,m]` and hence in the required four-point window. The final covered odd value `B` lies in every window for `m=B+1,B+2,B+3`. Targets `m=0,1,2` use the empty quotient sum `0`, and target `m=3` uses `3`. Since

\[
B+3=6\cdot2^{J-1},
\]

the four-point occupancy conclusion follows. `QED`

## Full-layer corollary under the Nova 1 valuation budget

Assume

\[
r_n+M_n\le\left\lfloor\frac{v_2(n!)}2\right\rfloor-1.
\]

Then

\[
v_2(n!)\ge2(r_n+M_n+1).
\]

For `n>=7`, one also has `v_3(n!)>=2`. Therefore

\[
\sqrt{n!}
\ge
2^{v_2(n!)/2}3^{v_3(n!)/2}
\ge
3\cdot2^{r_n+M_n+1}.
\]

The right side is an integer, so

\[
X_n\ge3\cdot2^{r_n+M_n+1}
\]

and hence

\[
Y_n
=
\left\lfloor\frac{X_n}{2^{r_n+1}}\right\rfloor
\ge3\cdot2^{M_n}.
\]

In particular, the hypotheses of N2-ADD-118 hold with `J=M_n`. Thus every admissible `n>=7` satisfies

\[
\mathcal Q_n\cap[\max(0,m-3),m]\ne\varnothing
\]

for all

\[
0\le m\le3\cdot2^{M_n}.
\]

Therefore no counterexample to the repaired quotient theorem can occur before

\[
m=3\cdot2^{M_n}+1.
\]

This lower bound is exact for the proved binary-spine mechanism. It is not a claim that a counterexample occurs at the next target.

## N2-FIN-201: first admissible parameter certificate

Using rigorous rational upper and lower bounds for `log n`, an exact scan of `7<=n<=5000` gives the first `n` satisfying

\[
r_n+M_n\le\left\lfloor\frac{v_2(n!)}2\right\rfloor-1
\]

as

\[
n=1892.
\]

At this value,

\[
r_n=31,
\qquad
M_n=911,
\qquad
v_2(1892!)=1886,
\qquad
v_3(1892!)=942.
\]

N2-ADD-118 certifies four-point quotient occupancy through

\[
3\cdot2^{911},
\]

a 275-digit quotient endpoint. The exact decimal value is emitted by

`verification/quotient_binary_spine.py`.

This scan is a finite certificate. The symbolic prefix theorem is the proved uniform result.

## Nova 4 intake decision

Nova 4 branch `nova/computational-verification` was inspected at commit

`2f2a355f59f230751b8e798e7a5df0769e8bf6d9`.

Outcome: `ACCEPTED_WITH_RESTRICTIONS`.

Accepted:

- an exact lattice-first harness was implemented;
- N2-ADD-115 and N2-OBS-107 can be independently replayed;
- exact logarithmic parameters are certified with rational bounds;
- corrupted lattice certificates are tested fail-closed.

Restrictions:

- the implementation freezes the older Nova 2 commit `45c74a5fa747551422ffcad7d3ddf22788fbe622`;
- it does not yet implement N2-ADD-116, N2-ADD-117, N2-OBS-108, or the normalized quotient model;
- it contains no completed exact quotient-gap sweep and returns no later four-point counterexample.

Accordingly, no Nova 4 quotient-search conclusion is imported beyond the original lattice regression.

## Decision on the repaired route

The repaired valuation-tagged route survives far beyond its first four quotient targets. Under the frozen valuation-budget condition it has a proved four-point-occupied prefix of length

\[
3\cdot2^{M_n}+1.
\]

The route is not globally certified. The unresolved region is

\[
3\cdot2^{M_n}<m\le Y_n.
\]

A valid next result must either:

1. extend deterministic quotient coverage into this region;
2. produce an exact full-family counterexample there; or
3. prove the target-dependent Fourier-window theorem for the normalized quotient law.

## What is not claimed

This theorem does not prove that every quotient target through `Y_n` is covered. It does not construct a global counterexample. It does not turn the finite Nova 4 lattice harness into an asymptotic result. It proves that the three-power repair passes an exponentially long deterministic prefix gate and that any smallest counterexample must lie strictly after that prefix.