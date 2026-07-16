# Full-Core Meet-in-the-Middle Certificate at n=56

## Result

`N1-FIN-011`: **finite certificate**.

The factorial half-range theorem remains open. This report certifies one finite parameter only.

## Exact parameters

\[
r_{56}=17,\qquad M_{56}=260,\qquad v_2(56!)=53.
\]

\[
Y_{56}=8{,}888{,}185{,}590{,}401{,}973{,}173{,}023{,}365{,}713{,}204{,}332{,}000,
\qquad
W_{56}=43{,}689.
\]

The reserved odd core has

\[
\tau(D_{56})=503{,}193{,}600
\]

divisors.

## Runtime-aware partitions

Primary replay:

- mask: `98`;
- split: `168 x 2,995,200`;
- wall time: `23.01` seconds;
- peak resident memory: `53,560 KiB`;
- exit status: `0`.

Independent replay:

- mask: `33`;
- split: `104 x 4,838,400`;
- wall time: `22.23` seconds;
- peak resident memory: `82,888 KiB`;
- exit status: `0`.

After excluding partition and environment metadata, the two runs agree on every exact mathematical field.

## Connected-prefix certificate

The exact connected-prefix cardinalities are

\[
90{,}625,
1{,}870{,}175,
18{,}876{,}460,
95{,}201{,}963,
252{,}731{,}752,
404{,}825{,}440,
411{,}604{,}587.
\]

After six layers,

\[
\frac{F_6}{Y_{56}+1}
=
0.238862882522450053\ldots<1.
\]

Thus six layers do not certify the endpoint. The seventh layer has no blocking gap before its cutoff and completes the certificate.

The final carrier endpoint is

\[
11{,}011{,}242{,}071{,}291{,}973{,}336{,}609{,}151{,}315{,}698{,}188{,}039.
\]

After correction, the occupied endpoint exceeds `Y_56` by

\[
2{,}123{,}056{,}480{,}890{,}000{,}163{,}585{,}785{,}602{,}493{,}899{,}728.
\]

Therefore

\[
H_{56!}(\lfloor\sqrt{56!}\rfloor+1)\le24.
\]

The term bound is `r_56+7=24`.

## Effective-factor diagnostics

For seven executed layers,

\[
\widetilde\Gamma_{56}=673.791460795324\ldots,
\]

\[
\mathcal B_{56}=0.001530254006653\ldots,
\]

and

\[
\Delta_{56}=1.031072082530349\ldots.
\]

The exact identity

\[
\Delta_{56}=\widetilde\Gamma_{56}\mathcal B_{56}
\]

holds.

The parity-only sufficient product has endpoint-ratio seventh root

\[
0.0000307763983342963\ldots.
\]

Its unrooted endpoint deficit is approximately

\[
3.823626295\times10^{31}.
\]

Factorial-specific internal spacing supplies essentially all of the missing expansion. The geometric mean of

\[
A_t=\frac{U_t}{2K_t-1}
\]

is approximately

\[
2.2076043208\times10^{15},
\]

while the geometric mean of `eta_t=U_t/(K_tD_t)` is

\[
0.00148409411440612\ldots.
\]

These are finite diagnostics only.

## Blocking-gap diagnostic

The six blocked layers at `n=56` have maximum ratio

\[
\max_t\frac{g_t}{D_t}=1.069351568466\ldots
\]

at layer 6. Across all 31 blocked layers for `51<=n<=56`, the overall maximum remains

\[
\frac{6963896442939750}{6290170063344679}
=1.107107816292\ldots<1.108
\]

at `n=51`, layer 4.

A first external blocking-gap bound does not determine internal average spacing.

## Combined finite boundary

The exact certificates now give

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le22
\qquad(12\le n\le54),
\]

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le23
\qquad(12\le n\le55),
\]

and

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le24
\qquad(12\le n\le56).
\]

No asymptotic conclusion is asserted.
