# Transformed Dyadic Resonance Ladder

## Scope

This file continues the exact odd-lattice normalization from `N3-ANA-025`.

It studies the numerical marker-three quotient law after conditioning on the odd component, subtracting one, and dividing by two. It does not use logarithmic divisor size as a surrogate.

Current imported heads inspected for this checkpoint:

- Nova 1 branch `nova/factorial-structure`, commit `1b81ec74f907d57d520bcf6c51f2e6e71f0474a7`;
- Nova 2 branch `nova/additive-occupancy`, commit `e443674f86b2ee3c7037ac94ee47f6b8a4b3b29f`.

The active structural labels and numerical supports remain those of the marker-three construction. The factorial half-range theorem and Erdős Problem 18 remain open.

## Frozen notation

For every integer `n>=120368`, put

\[
\rho_n=\lceil4\log n\rceil,
\qquad
M_n=\lceil16(\log n)^2\rceil,
\]

\[
X_n=\lfloor\sqrt{n!}\rfloor,
\qquad
Y_n=\left\lfloor\frac{X_n}{3}\right\rfloor,
\]

\[
W_n=\left\lfloor\frac{2^{\rho_n}-3}{3}\right\rfloor.
\]

Let `m_n` be the largest odd integer at most `n`, and define

\[
L_n=m_n(2^{M_n}-1),
\qquad
P_n=L_n+W_n.
\]

The exact final-only target range is

\[
P_n+1\le q\le Y_n.
\]

For the original marker-three law, the quotient layers are

\[
B_t(n)=
\{2^{t-1}u:
 u\text{ odd},\ 3u\mid n!,\ 2^{t-1}u\le Y_n\}.
\]

By `N3-ANA-025`, after conditioning on `Z_1\ne0`, define

\[
\widetilde Z_1=\frac{Z_1-1}{2},
\qquad
\widetilde Z_t=\frac{Z_t}{2}
\quad(t\ge2),
\]

and

\[
\widetilde T=\sum_{t=1}^{M_n}\widetilde Z_t.
\]

The transformed coordinates remain independent and share the exact common tilt

\[
\widetilde\lambda_{n,q}=2\lambda_{n,q}.
\]

The transformed supports are

\[
\widetilde B_1(n)
=
\left\{\frac{u-1}{2}:
 u\text{ odd},\ 3u\mid n!,\ u\le Y_n\right\},
\]

and, for `t>=2`,

\[
\widetilde B_t(n)
=
\{0\}
\cup
\{2^{t-2}u:
 u\text{ odd},\ 3u\mid n!,\ 2^{t-1}u\le Y_n\}.
\]

Write

\[
\widetilde\phi_{t,n,q}(\theta)
=
\mathbb E e^{i\theta\widetilde Z_t},
\qquad
\widetilde\Phi_{n,q}(\theta)
=
\prod_{t=1}^{M_n}
\widetilde\phi_{t,n,q}(\theta).
\]

For one transformed layer define

\[
\widetilde{\mathcal D}_{t,n,q}(\theta)
=
\sum_{a,b}
\mathbb P(\widetilde Z_t=a)
\mathbb P(\widetilde Z_t=b)
\sin^2\left(\frac{(a-b)\theta}{2}\right).
\]

Then exactly

\[
|\widetilde\phi_{t,n,q}(\theta)|^2
=
1-2\widetilde{\mathcal D}_{t,n,q}(\theta).
\]

## Legal low-state block

Let

\[
k_n=\frac{m_n+1}{2}.
\]

For every odd integer

\[
1\le u\le m_n,
\]

one has `3u|n!`.

Indeed, `u<=n` implies `u|n!`, and

\[
v_3(u)\le\log_3 n
<\left\lfloor\frac n3\right\rfloor
\le v_3(n!)
\]

throughout the present range, leaving at least one additional factor of `3`.

Also

\[
m_n2^{M_n-1}<L_n<P_n<Y_n.
\]

Hence every layer contains all of its small odd-core states:

\[
2^{t-1}u\in B_t(n)
\qquad
(1\le t\le M_n,
\ 1\le u\le m_n,
\ u\text{ odd}).
\]

Consequently:

1. the first transformed support contains the consecutive block
   \[
   0,1,\ldots,k_n-1;
   \]
2. every transformed layer `t>=2` contains
   \[
   0
   \quad\text{and}\quad
   2^{t-2}u
   \quad
   (u=1,3,\ldots,m_n).
   \]

This low-state block is used only for explicit probability bounds. It is not treated as the full menu.

## Uniform lower tilt bound

From `N3-ANA-020`, every post-prefix target satisfies

\[
\lambda_{n,q}
>
-\frac{8M_n\log L_n}{L_n}.
\]

Therefore

\[
\widetilde\lambda_{n,q}
>
-\frac{16M_n\log L_n}{L_n}.
\]

For `t>=2`, set

\[
\eta_{n,t}
=
\frac{16M_n\log L_n}{2^{M_n}-1}
2^{t-2}.
\]

Every displayed small positive state in transformed layer `t` is at most

\[
2^{t-2}m_n,
\]

so its tilted weight is at least

\[
e^{-\eta_{n,t}}.
\]

Let

\[
p_{t,n,q}^{(0)}
=
\mathbb P_{\widetilde\lambda_{n,q}}
\{\widetilde Z_t=0\}
\qquad(t\ge2).
\]

The partition function contains the zero state and the `k_n` displayed small positive states. Thus

\[
p_{t,n,q}^{(0)}
\le
\frac1{1+k_ne^{-\eta_{n,t}}}
\le
\frac{2e^{\eta_{n,t}}}{m_n+1}.
\]

## N3-ANA-026: exact dyadic finite-prefix factorization

Result class: **proved theorem**.

For every integer

\[
1\le j\le M_n-1,
\]

define the reduced dyadic frequency

\[
\theta_j
=
\frac{\pi}{2^{j-1}}
=
\frac{2\pi}{2^j}.
\]

Then:

1. for the matching layer `t=j+1`,
   \[
   \widetilde\phi_{j+1,n,q}(\theta_j)
   =
   2p_{j+1,n,q}^{(0)}-1;
   \]
2. for every later layer `t>=j+2`,
   \[
   \widetilde\phi_{t,n,q}(\theta_j)=1;
   \]
3. the full characteristic function satisfies the exact factorization
   \[
   \widetilde\Phi_{n,q}(\theta_j)
   =
   \left(
   \prod_{t=1}^{j}
   \widetilde\phi_{t,n,q}(\theta_j)
   \right)
   \left(2p_{j+1,n,q}^{(0)}-1\right).
   \]

### Proof

Every nonzero matching-layer state has the form

\[
2^{j-1}u
\]

with `u` odd. Therefore

\[
e^{i\theta_j2^{j-1}u}
=e^{i\pi u}
=-1.
\]

The zero state has phase `1`, giving

\[
\widetilde\phi_{j+1,n,q}(\theta_j)
=p_{j+1,n,q}^{(0)}
-(1-p_{j+1,n,q}^{(0)})
=2p_{j+1,n,q}^{(0)}-1.
\]

For `t>=j+2`, every nonzero state is

\[
2^{t-2}u.
\]

Hence

\[
\theta_j2^{t-2}u
=
\pi2^{t-j-1}u
\]

is an integer multiple of `2pi`, because `t-j-1>=1`. Thus every state in every later layer has phase `1`.

Multiplication of the coordinate factors proves the theorem. `QED`

### Exact resonance classification

The transformed first support contains both `0` and `1` with positive probability. Therefore no nonzero dyadic frequency is an exact modulus-one resonance of the full transformed law.

However, every reduced dyadic frequency has an exact tail resonance: all layers after `j+1` are invisible there.

## N3-ANA-027: matching-layer near-pure sign and tail-dispersion collapse

Result class: **proved theorem and disproved route estimate**.

Define

\[
J_n
=
\min\left(
M_n-1,
\left\lfloor
1+\log_2
\frac{2^{M_n}-1}{16M_n\log L_n}
\right\rfloor
\right).
\]

Then

\[
J_n=M_n-O(\log\log n).
\]

For every

\[
1\le j\le J_n
\]

and every post-prefix target `q`, one has

\[
\eta_{n,j+1}\le1,
\]

\[
p_{j+1,n,q}^{(0)}
\le
\frac{2e}{m_n+1},
\]

and

\[
\left|
\widetilde\phi_{j+1,n,q}(\theta_j)
\right|
\ge
1-rac{4e}{m_n+1}.
\]

Moreover,

\[
\sum_{t=j+1}^{M_n}
\widetilde{\mathcal D}_{t,n,q}(\theta_j)
=
2p_{j+1,n,q}^{(0)}
(1-p_{j+1,n,q}^{(0)})
\le
\frac{4e}{m_n+1}.
\]

Thus, on all but `O(log log n)` of the dyadic layer scales, the complete transformed tail contributes only `O(1/n)` dispersion at its matching dyadic frequency.

### Proof

The definition of `J_n` is exactly the largest safe integer range for which

\[
\frac{16M_n\log L_n}{2^{M_n}-1}
2^{j-1}
\le1.
\]

The zero-probability estimate follows from the low-state partition bound.

For the matching layer,

\[
\widetilde\phi_{j+1,n,q}(\theta_j)
=2p_{j+1,n,q}^{(0)}-1.
\]

The displayed zero-probability bound is below `1/2` throughout the present range, so

\[
|2p_{j+1,n,q}^{(0)}-1|
=1-2p_{j+1,n,q}^{(0)}
\ge1-\frac{4e}{m_n+1}.
\]

Every later layer has zero dispersion at `theta_j`. For the matching two-phase layer,

\[
\widetilde{\mathcal D}_{j+1,n,q}(\theta_j)
=2p_{j+1,n,q}^{(0)}
(1-p_{j+1,n,q}^{(0)}).
\]

This proves the tail formula and bound.

Finally,

\[
\log_2(16M_n\log L_n)
=O(\log\log n),
\]

because `M_n` and `log L_n` are both of order `(log n)^2`. Hence

\[
M_n-J_n=O(\log\log n).
\]

`QED`

### Disproved route estimate

The following proposed mechanism is false:

> Outside a zero major arc, a positive proportion of all `M_n` transformed layers always contributes a fixed amount of phase dispersion.

At every `theta_j`, the complete tail after the first `j` layers contributes at most `O(1/n)` dispersion for all `j<=J_n`.

This does not prove that the full characteristic function is large at `theta_j`. Any decay must come from the first `j` transformed coordinates.

## N3-ANA-028: exact transformed-window dyadic kernel classification

Result class: **proved theorem**.

For a target `q`, let

\[
J_{n,q}
=
\left[
\left\lceil\frac{q-W_n-1}{2}\right\rceil,
\left\lfloor\frac{q-1}{2}\right\rfloor
\right]
\cap\mathbb Z
\]

be the transformed target interval, and let

\[
N_{n,q}=|J_{n,q}|.
\]

Then:

### Case 1: `rho_n` odd

One has

\[
W_n=\frac{2^{\rho_n}-5}{3},
\]

and for every target parity,

\[
N_{n,q}
=
\frac{2^{\rho_n-1}-1}{3}.
\]

This integer is odd.

### Case 2: `rho_n` even and `q` even

One has

\[
W_n=\frac{2^{\rho_n}-4}{3},
\]

and

\[
N_{n,q}
=
\frac{W_n}{2}
=
2\frac{2^{\rho_n-2}-1}{3}.
\]

Thus

\[
v_2(N_{n,q})=1.
\]

### Case 3: `rho_n` even and `q` odd

One has

\[
N_{n,q}
=
\frac{W_n}{2}+1
=
\frac{2^{\rho_n-1}+1}{3}.
\]

This integer is odd.

Consequently,

\[
v_2(N_{n,q})\in\{0,1\}
\]

for every transformed target window.

### Dyadic kernel consequence

Let

\[
\widetilde K_{n,q}(\theta)
=
\sum_{x\in J_{n,q}}e^{ix\theta}.
\]

At a reduced dyadic frequency

\[
\theta=\frac{2\pi a}{2^d},
\qquad
a\text{ odd},
\]

one has

\[
\widetilde K_{n,q}(\theta)=0
\quad\Longleftrightarrow\quad
2^d\mid N_{n,q}.
\]

Therefore:

1. for every `d>=2`, the transformed interval kernel never vanishes at a reduced dyadic frequency of denominator `2^d`;
2. at `theta=pi`, the kernel vanishes exactly when `rho_n` and `q` are both even.

### Proof

The formulas for `W_n` follow from the two residues of powers of `2` modulo `3`.

If `rho_n` is odd, the original interval contains an even number `W_n+1` of consecutive integers, so exactly half are odd.

If `rho_n` is even, then `W_n` is even and the original interval has odd length. When `q` is even, both endpoints are even and the odd count is `W_n/2`. When `q` is odd, both endpoints are odd and the odd count is `W_n/2+1`.

The displayed parity and valuation claims follow directly.

For a consecutive interval of `N` integers, its Fourier kernel differs by a unit-modulus phase from

\[
1+e^{i\theta}+\cdots+e^{i(N-1)\theta}.
\]

At a reduced dyadic frequency of denominator `2^d`, this geometric sum vanishes exactly when `2^d|N`.

Since `v_2(N_{n,q})<=1`, no denominator `2^d` with `d>=2` divides the transformed window length. `QED`

## Combined route consequence

The odd-lattice normalization removes the forced original `pi` twin, but the transformed law retains an exact dyadic finite-prefix skeleton.

At frequency `theta_j`:

1. every layer after `j+1` is exactly invisible;
2. the matching layer is almost a pure sign for `j<=J_n`;
3. the complete tail dispersion is only `O(1/n)`;
4. the transformed interval kernel does not cancel the point for `j>=2`.

A successful transformed Fourier theorem must therefore control the prefix product

\[
\prod_{t=1}^{j}
\widetilde\phi_{t,n,q}(\theta_j)
\]

and neighborhoods of the dyadic ladder frequencies. It cannot obtain a uniform minor-arc bound merely by accumulating dispersion from later layers.

The nonvanishing of a kernel at isolated points is not itself an integral obstruction. The next theorem must be neighborhood-sensitive and matched to the exact weighted inversion inequality.

## Claim boundary

This checkpoint does not prove:

- transformed local-window positivity;
- a transformed weighted Fourier inequality;
- target-local collision control;
- quotient occupancy;
- the factorial half-range theorem;
- Erdős Problem 18.

It proves the exact dyadic resonance skeleton and removes a false many-tail-layers mechanism from the active route.