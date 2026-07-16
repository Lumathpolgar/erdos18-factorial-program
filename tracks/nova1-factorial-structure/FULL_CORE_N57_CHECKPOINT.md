# Full-Core n=57 Checkpoint

## Accepted results

- `N1-STR-027`: **proved theorem**, overflow-safe truncation and exact checkpoint continuation.
- `N1-DIS-007`: **disproved route**, unrestricted unsigned-128 half-list multiplication.
- `N1-DIS-008`: **disproved route**, finite candidate `g_t/D_t<1.108`.
- `N1-FIN-012`: **finite certificate**, exact dual-partition coverage at `n=57`.
- `N1-CMP-010`: **computational evidence**, effective carrier and factorial-span diagnostics.

## Exact conclusion

\[
H_{57!}(\lfloor\sqrt{57!}\rfloor+1)\le24.
\]

Combined finite boundary:

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le24
\qquad(12\le n\le57).
\]

Seven carrier layers are required by the exact connected-core recursion because six layers reach only about `0.0873914321` of the endpoint scale.

## Verification correction

The preliminary unguarded `n=57` runs are rejected because masks `6` and `424` gave different `K_6` and `K_7`. The overflow-safe checkpointed runs agree exactly and are authoritative.

Overflow-safe overlap replays reproduce the accepted mathematical outputs at every `52<=n<=56`.

## New obstruction

The first-blocking-gap ratio at `n=57`, layer `3`, is approximately `1.1674772301`, disproving the finite `1.108` candidate.

## Open frontier

The exact sequential theorem must control factorial-specific internal span

\[
A_t=\frac{U_t}{2K_t-1}
\]

or normalized average gaps

\[
\eta_t=\frac{U_t}{K_tD_t}.
\]

Count, parity, and the first external blocking gap are insufficient as complete proof inputs.
