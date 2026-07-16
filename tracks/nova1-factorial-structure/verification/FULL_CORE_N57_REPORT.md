# Full-Core Safe MITM Report at n=57

## Classification

`N1-FIN-012`: **finite certificate**.

`N1-CMP-010`: **computational evidence** for effective and span diagnostics.

The factorial half-range theorem and Erdos Problem 18 remain open.

## Exact parameters

\[
r_{57}=17,\qquad M_{57}=262,\qquad v_2(57!)=53.
\]

\[
Y_{57}=67{,}104{,}329{,}637{,}494{,}096{,}111{,}222{,}818{,}356{,}512{,}155{,}252,
\qquad W_{57}=43{,}689.
\]

The reserved odd core has `696,729,600` divisors.

## Overflow-safe dual-partition replay

Primary mask `6`:

- truncated split: `140 x 4,974,362`;
- emitted through certificate completion: `565,913,305`.

Alternate mask `424`:

- truncated split: `144 x 4,807,084`;
- emitted through certificate completion: `565,913,305`.

The two safe runs agree on every mathematical output field. Truncation removes only half divisors larger than `Y_57`, which cannot participate in a required product.

## Exact connected prefixes

\[
K_1=93{,}284,
\quad K_2=1{,}968{,}508,
\quad K_3=21{,}512{,}180,
\]

\[
K_4=115{,}705{,}564,
\quad K_5=322{,}620{,}612,
\quad K_6=543{,}303{,}166,
\quad K_7=565{,}913{,}305.
\]

After six layers,

\[
\frac{F_6}{Y_{57}+1}
=0.0873914320600893654\ldots<1.
\]

After seven layers,

\[
\frac{F_7}{Y_{57}+1}
=1.0873914095218273314\ldots>1.
\]

Thus seven layers are required by this exact carrier and seven layers suffice.

The final margin is

\[
5{,}864{,}341{,}952{,}037{,}941{,}548{,}771{,}786{,}716{,}193{,}021{,}624.
\]

Therefore

\[
H_{57!}(\lfloor\sqrt{57!}\rfloor+1)\le 17+7=24.
\]

Together with the earlier certificates,

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le24
\qquad(12\le n\le57).
\]

## Effective diagnostics

For the seven executed layers,

\[
\widetilde\Gamma_{57}=604.565529127372549\ldots,
\]

\[
\mathcal B_{57}=0.00167399672600756826\ldots,
\]

\[
\Delta_{57}=1.0120407164162547937\ldots.
\]

The exact identity

\[
\Delta_{57}=\widetilde\Gamma_{57}\mathcal B_{57}
\]

holds.

The parity-only endpoint-ratio seventh root is

\[
2.3135660491255676\times10^{-5},
\]

with unrooted deficit approximately

\[
2.8185560934224899\times10^{32}.
\]

The factorial-span amplification root relative to the parity baseline is

\[
43{,}743.7572529543457\ldots.
\]

The geometric mean of

\[
\eta_t=\frac{U_t}{K_tD_t}
\]

is

\[
0.00165403239908516155\ldots.
\]

These are finite diagnostics only.

## Record-gap counterexample

At layer `3`,

\[
\frac{g_3}{D_3}=1.1674772300983786\ldots.
\]

Thus the finite `1.108` candidate bound is false. Across the 37 blocked layers for `51<=n<=57`, the new exact maximum is attained at `n=57`, layer `3`.

## Claim boundary

This certificate proves only the finite `n=57` carrier conclusion and the combined finite range. It does not prove uniform factorial-specific span amplification, asymptotic quotient occupancy, the factorial half-range theorem for all sufficiently large `n`, or Erdos Problem 18.
