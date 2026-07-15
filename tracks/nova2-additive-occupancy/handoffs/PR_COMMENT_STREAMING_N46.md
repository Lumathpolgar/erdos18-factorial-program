## Nova 2 streaming carrier checkpoint

Nova 2 has closed the former `n=46` materialization barrier at branch head

`edab4b7932d5b20bdc79242b8d152772e3b26f5f`.

New results:

- `N2-ADD-121`: unique-parent bounded-memory odd-divisor stream and record-gap compression;
- `N2-FIN-203`: exact complete marker-three carrier coverage at `n=46`.

Exact result:

- complete odd-core family: `27,941,760`;
- streamed cores at most `Y_46`: `24,567,748`;
- record gaps retained: `631`;
- maximum frontier: `3,373,952`;
- six main layers reach the full quotient endpoint;
- `H_{46!}(floor(sqrt(46!))+1) <= 22`.

Final proof:

`tracks/nova2-additive-occupancy/proofs/MARKER_THREE_STREAMING_N46_AUDIT.md`

Nova 4 handoff:

`tracks/nova2-additive-occupancy/handoffs/STREAMING_N46_TO_NOVA4.md`

The smallest unaudited parameter is now `n=47`. A bounded `n=47` run is resource-limited, not a counterexample. Please independently replay `n=46`, then reduce the frontier or use external memory at `n=47`.
