# Overflow-Safe Regression Replay for n=52 through n=56

## Classification

**finite certificate** regression audit.

The overflow-safe checkpointed verifier was replayed independently against the accepted mathematical outputs before promoting the `n=57` result.

| `n` | safe mask | emitted | layers | term bound | product floor ratio | outcome |
|---:|---:|---:|---:|---:|---:|---|
| 52 | 511 | 128,277,372 | 6 | 22 | 866,765,166,748 | exact match |
| 53 | 511 | 255,794,579 | 6 | 22 | 3,743,726,317,282 | exact match |
| 54 | 292 | 287,853,491 | 6 | 22 | 617,241,772,812 | exact match |
| 55 | 808 | 369,103,338 | 6 | 23 | 936,909,468,886 | exact match |
| 56 | 98 | 411,604,587 | 7 | 24 | 63,049,045,904,048,126,614 | exact match |

For every row, the overflow-safe replay reproduced all accepted:

- exact parameters `r_n`, `M_n`, `v_2(n!)`, `Y_n`, and `W_n`;
- connected-prefix counts;
- connected maxima;
- first blocking gaps;
- carrier endpoints;
- final margin;
- selected-term bound;
- connected-prefix product and requirement ratio.

The truncated half-list sizes can be smaller because half divisors above `Y_n` are removed. This does not change any product at or below `Y_n` by `N1-STR-027`.

The prior finite mathematical conclusions through `n=56` remain valid. The authoritative verifier is now `marker_three_mitm_checkpoint_u128.cpp`.
