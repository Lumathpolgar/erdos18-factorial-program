# Frozen Branch Heads

Date: 2026-07-15

Result class: `exact finite theorem audit`

## Startup baseline

| Track | Branch | Exact commit SHA | Artifacts tested at startup |
|---|---|---|---|
| Nova 1 | `nova/factorial-structure` | `f2e011d689d56af07ed01de08e00c05457ca9c80` | none, request initially queued |
| Nova 2 | `nova/additive-occupancy` | `71370633b1e6726bf6f9e3b334d42cfc34512c06` | none, request initially queued |
| Nova 3 | `nova/analytic-density` | `c79cddee6e8940e27ff256c29a85a3fc93766f7b` | none, request initially queued |
| Nova 4 | `nova/computational-verification` | `2acd1e4bb0853eda49c1a42e6080fcbaeec9dcc4` | startup registries and charter |
| Base | `main` | `68ace6c9c3b67636e298a406fee3bfe8e072741d` | shared contracts only |

## Post-build upstream intake

The upstream branches advanced while the Nova 4 checkpoint was being built. Their new handoffs were inspected and frozen as follows.

| Track | Branch | Current inspected head | Handoff inspected | Audit status |
|---|---|---|---|---|
| Nova 1 | `nova/factorial-structure` | `fa11f4b2cb86a2dd791df189ada12757be791804` | `handoffs/TO_NOVA4.md`, `N1-HO-N4-001` | received, not yet executed |
| Nova 2 | `nova/additive-occupancy` | `45c74a5fa747551422ffcad7d3ddf22788fbe622` | `handoffs/TO_NOVA4.md`, `N2-HO-N4-001-v2` | received, not yet executed |
| Nova 3 | `nova/analytic-density` | `0ce88b28dc2e6641093526f5777bb31f658e3515` | `handoffs/TO_NOVA4.md`, `N3-HO-N4-001` | received, not yet executed |

No upstream theorem or construction is marked accepted by this intake. No branch was merged, rebased, force-updated, or edited.
