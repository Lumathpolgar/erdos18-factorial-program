# Marker-Three Carrier-Block Reduction

## Result IDs

- `N2-ADD-119`: proved theorem
- `N2-ADD-120`: conditional theorem

## Imported construction

This file audits and uses the marker-three valuation rainbow imported from:

- repository: `Lumathpolgar/erdos18-factorial-program`
- branch: `nova/factorial-structure`
- exact commit: `ebb47ba436af554366d0f285119a769f31f9e561`
- construction: `N1-CON-003`
- handoff: `N1-HO-N2-002`

The prior handoff `N1-HO-N2-001` remains rejected. The construction in this file is a new object, not a repair silently applied to the rejected labels.

## Frozen marker-three objects

For an integer `n`, write

\[
X_n=\lfloor\sqrt{n!}\rfloor,
\qquad
r_n=\lceil4\log n\rceil,
\qquad
M_n=\lceil16(\log n)^2\rceil,
\]

\[
R_n=2^{r_n}-1,
\qquad
W_n=\left\lfloor\frac{R_n-2}{3}\right\rfloor,
\qquad
Y_n=\left\lfloor\frac{X_n}{3}\right\rfloor.
\]

For `1<=t<=M_n`, let

\[
U_t(n)=
\left\{
 u\ge1:
 u\text{ odd},\ 3u\mid n!,\ 3\cdot2^{t-1}u\le X_n
\right\},
\]

and

\[
B_t(n)=\{2^{t-1}u:u\in U_t(n)\}.
\]

Let

\[
Q_n=
\left\{
\sum_{t=1}^{M_n}b_t:
 b_t\in B_t(n)\cup\{0\}
\right\}.
\]

The Nova 1 quotient reduction asks for

\[
Q_n\cap[q-W_n,q]\ne\varnothing
\]

for every integer

\[
W_n+1\le q\le Y_n.
\]

## Structural intake decision

The following parts of `N1-HO-N2-002` pass the Nova 2 structural gate.

1. Every main divisor has exact form `3*2^(t-1)*u` with odd `u` and is legal under the stated valuation side condition.
2. Different layers have different exact 2-adic valuations.
3. Main terms are divisible by `3`, while correction terms are pure powers of two.
4. The main support lattice is exactly `3 Z` because the first layer contains `3`.
5. The quotient support has span one because `1 in B_1(n)`.
6. The binary palette represents every residual in `[0,R_n]`.
7. A quotient downward window of radius `W_n` is sufficient because `2+3W_n<=R_n`.
8. The term cost is at most `M_n+r_n`.

Accordingly, `N1-HO-N2-002` is accepted with restrictions. The restrictions are the unproved global quotient occupancy, endpoint reach, collision collapse, finite exceptions, and any hidden use of a forbidden sequential architecture.

## Downward density convention

For an integer `W>=0`, a set

\[
S\subseteq\mathbb Z_{\ge0}
\]

is downward `W`-dense through `E` if

\[
S\cap[\max(0,q-W),q]\ne\varnothing
\]

for every integer `0<=q<=E`.

This definition concerns the final set under discussion. It does not by itself assert exact interval coverage.

## N2-ADD-119: translated carrier-block lemma

### Statement

Let `W,E,a` be nonnegative integers. Let

\[
S\subseteq[0,E]\cap\mathbb Z
\]

be downward `W`-dense through `E`, and assume

\[
0,E\in S.
\]

Let

\[
0=u_0<u_1<\cdots<u_k
\]

be integers such that

\[
a(u_{i+1}-u_i)\le E+W+1
\]

for every `0<=i<k`. Define

\[
T=\bigcup_{i=0}^k(a u_i+S).
\]

Then `T` is downward `W`-dense through

\[
E+a u_k,
\]

and contains that endpoint exactly.

### Proof

Each translate `a u_i+S` is downward `W`-dense on

\[
[a u_i,a u_i+E]
\]

and contains both endpoints of that interval.

Write

\[
L_i=a u_i,
\qquad
H_i=a u_i+E.
\]

The hypothesis gives

\[
L_{i+1}\le H_i+W+1.
\]

Every target `q<=H_i+W` after the end of the `i`th block can use the exact point `H_i`. If

\[
L_{i+1}=H_i+W+1,
\]

then the only next target is exactly `L_{i+1}`, which belongs to the next block. If the inequality is strict, the two covered target ranges overlap.

Thus no downward gap larger than `W` occurs between consecutive translated blocks. Induction proves downward `W`-density through `H_k=E+a u_k`. The point `H_k` belongs to the last translate because `E in S`. `QED`

## Layer form of N2-ADD-119

Fix a layer `t` and let

\[
a_t=2^{t-1}.
\]

Suppose the rainbow sumset from layers `1,...,t-1` is downward `W_n`-dense through `E_{t-1}` and contains both `0` and `E_{t-1}`.

Choose an ordered core chain

\[
0=u_{t,0}<u_{t,1}<\cdots<u_{t,k_t},
\qquad
u_{t,i}\in U_t(n)\text{ for }i>0,
\]

such that

\[
2^{t-1}(u_{t,i+1}-u_{t,i})
\le
E_{t-1}+W_n+1.
\]

Then the rainbow sumset from layers `1,...,t` is downward `W_n`-dense through

\[
E_t=E_{t-1}+2^{t-1}u_{t,k_t},
\]

and contains `E_t` exactly.

## Exact connected-core formulation

Set `E_0=0`. At layer `t`, define

\[
D_t(E_{t-1})
=
\left\lfloor
\frac{E_{t-1}+W_n+1}{2^{t-1}}
\right\rfloor.
\]

In the ordered set

\[
\{0\}\cup U_t(n),
\]

join consecutive core values when their difference is at most `D_t(E_{t-1})`. Let `u_t^*` be any core in the connected component of `0`, and set

\[
E_t=E_{t-1}+2^{t-1}u_t^*.
\]

Choosing the largest core in that component gives the strongest reach certified by this one-layer application.

This criterion is exact for the carrier-block proof engine. Failure of the criterion does not prove failure of the full rainbow sumset, because other interactions between layers may still bridge the gap.

## N2-ADD-120: conditional marker-three chain theorem

### Statement

Assume the structural hypotheses of `N1-CON-003`. Suppose the connected-core recursion can be executed for every `1<=t<=M_n`, producing endpoints

\[
E_t=E_{t-1}+2^{t-1}u_t^*.
\]

Then `Q_n` is downward `W_n`-dense through `E_{M_n}` and contains `E_{M_n}` exactly.

Consequently every quotient target

\[
0\le q\le E_{M_n}+W_n
\]

has a quotient rainbow sum in `[q-W_n,q]`.

If

\[
E_{M_n}+W_n\ge Y_n,
\]

then the exact hypothesis of Nova 1 theorem `N1-RED-004` holds, and therefore

\[
H_{n!}(X_n+1)
\le
M_n+r_n
=O((\log n)^2).
\]

### Proof

Apply the layer form of N2-ADD-119 inductively from `E_0=0`. This proves downward `W_n`-density through `E_{M_n}` and exact attainment of the endpoint.

For targets between `E_{M_n}+1` and `E_{M_n}+W_n`, the exact endpoint `E_{M_n}` lies in the required downward window. Thus quotient occupancy holds through `E_{M_n}+W_n`.

The final implication is exactly `N1-RED-004`. `QED`

## Recovery and extension of the known initial range

Let `m_n` be the largest odd integer at most `n`. Nova 1 proves that all odd cores

\[
1,3,5,\ldots,m_n
\]

belong to every layer for all sufficiently large `n`.

At every layer these cores form a chain with gaps at most `2`. The recursion therefore permits `u_t^*=m_n` and gives

\[
E_{M_n}=m_n(2^{M_n}-1).
\]

Hence the quotient windows are occupied through

\[
m_n(2^{M_n}-1)+W_n.
\]

This adds the exact final correction-width extension beyond the initial quotient endpoint recorded by Nova 1. It remains exponentially smaller than `Y_n` on the factorial scale.

## Why the lemma is useful

The global additive problem is reduced to an exact menu-connectivity question:

> How far from zero does the odd-core menu `U_t(n)` remain connected when consecutive gaps are tested against `D_t(E_{t-1})`?

This is weaker than enumerating the entire rainbow sumset and stronger than raw profile counting. It preserves numerical values, layer labels, downward orientation, and the actual correction radius.

It also gives Nova 4 an exact falsification target:

1. generate or certify core menus;
2. compute connected components under the exact thresholds;
3. return the first layer and core gap that stops the carrier recursion;
4. distinguish failure of this proof engine from failure of the full marker-three model.

## Phase 12P warning

N2-ADD-120 is a sequential sufficient condition. It must not be presented as a globally nonsequential proof.

A future promotion must either:

1. prove that the marker-three menu sizes and the `M_n=Theta((log n)^2)` budget lie outside the exact Phase 12P no-go range;
2. accept the resulting lower-bound cost and verify it remains within the allowed term budget; or
3. use N2-ADD-120 only as a computational lower-bound certificate while retaining a final-only Fourier or restricted-sumset theorem as the asymptotic proof engine.

## Intake outcome

- `N1-HO-N2-002`: `ACCEPTED_WITH_RESTRICTIONS`.
- `N1-CON-003`: structurally accepted and promoted to Nova 2's preferred factorial model.
- Nova 2's earlier three-power repair: `SUPERSEDED` as the preferred route, but retained as a valid conditional fallback and obstruction record.
- Global quotient occupancy: open.
- First unresolved theorem node: prove or disprove occupancy beyond the connected-core certified reach, including endpoint support near `Y_n`.

## What is not claimed

This file does not prove the factorial half-range theorem. It does not prove that the connected-core recursion reaches `Y_n`. It does not turn formal profile capacity into occupancy. It does not show that failure of the sequential carrier criterion is a counterexample to the full rainbow model.