# Full-Core n=56 Checkpoint

## Status

`N1-FIN-011`: **finite certificate**.

The marker-three connected-core carrier is exactly certified at `n=56` by two independent meet-in-the-middle partitions. Seven carrier layers are required, giving term bound `24`.

The factorial half-range theorem and Erdős Problem 18 remain open.

## Exact source state

- branch: `nova/factorial-structure`;
- source verifier: `verification/marker_three_mitm_prefix_u128.cpp`;
- primary partition mask: `98`;
- alternate partition mask: `33`.

## Exact conclusion

\[
H_{56!}(\lfloor\sqrt{56!}\rfloor+1)\le24.
\]

Together with earlier certificates:

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le22\quad(12\le n\le54),
\]

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le23\quad(12\le n\le55),
\]

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le24\quad(12\le n\le56).
\]

## Structural transition

At `n=56`, six layers reach only

\[
F_6/(Y_{56}+1)=0.23886288252245\ldots.
\]

The seventh layer completes the endpoint. This is a genuine finite carrier-layer transition, not a resource artifact.

## New theorem intake

Nova 1 independently reconstructed Nova 2 results `N2-ADD-124` and `N2-OBS-110` as:

- `N1-STR-026`: parity-span carrier lower bound;
- `N1-OBS-004`: optimality when only oddness, prefix count, and threshold are supplied.

The exact next sequential theorem input is factorial-specific internal span amplification `A_t=U_t/(2K_t-1)` or normalized average gap `eta_t=U_t/(K_tD_t)`.

## Evidence boundary

The 31 finite blocked layers through `n=56` retain `g_t/D_t<1.108`, but this does not control internal average spacing. No finite pattern is promoted asymptotically.
