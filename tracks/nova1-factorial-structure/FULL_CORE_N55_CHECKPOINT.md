# Full-Core n=55 Checkpoint

## Status

- `N1-FIN-010`: **finite certificate**.
- `N1-STR-025`: **proved theorem**.
- `N1-CMP-008`: **computational evidence**.
- The factorial half-range theorem remains open.

## Exact finite conclusion

The runtime-aware meet-in-the-middle carrier reaches the exact quotient endpoint for `n=55` in six layers.

\[
H_{55!}(\lfloor\sqrt{55!}\rfloor+1)\le23.
\]

The term bound increases from `22` to `23` because

\[
r_{55}=17.
\]

Thus

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le22
\qquad(12\le n\le54),
\]

while

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le23
\qquad(12\le n\le55).
\]

## Exact n=55 data

- `r_55=17`;
- `M_55=257`;
- `v_2(55!)=50`;
- total odd-core divisors: `452,874,240`;
- primary split: `156 x 2,903,040`, mask `9`;
- alternate split: `96 x 4,717,440`, mask `808`;
- emitted through certificate: `369,103,338`;
- layers used: `6`;
- term bound: `23`;
- margin: `2,071,800,017,139,336,764,535,620,107,907`.

Connected-prefix counts:

\[
90{,}622,
1{,}867{,}655,
18{,}700{,}076,
92{,}180{,}941,
236{,}519{,}444,
369{,}103{,}338.
\]

## Effective entropy correction

Imported and independently reconstructed source:

- branch: `nova/additive-occupancy`;
- exact commit: `2ab09dd980f7116b82530368e3d98bb53240bf0c`;
- theorem: `N2-ADD-122`;
- Nova 1 reconstruction: `N1-STR-025`.

At `n=55`,

\[
\widetilde\Gamma_{55}=98.919733584849\ldots,
\]

\[
\mathcal B_{55}=0.010109209300122\ldots,
\]

\[
\Delta_{55}=1.000000290721510\ldots.
\]

The large count surplus is almost entirely consumed by utilization loss.

## Gap diagnostic

The finite candidate bound survives through `n=55`:

\[
\max_{51\le n\le55}\max_{t\text{ blocked}}\frac{g_t}{D_t}
=
\frac{20891689328819250}{18870510190034037}
<1.108.
\]

This is computational evidence only.

## Next exact boundary

The smallest unaudited finite parameter is `n=56`.
