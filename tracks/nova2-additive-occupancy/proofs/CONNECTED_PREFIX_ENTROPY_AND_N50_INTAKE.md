# Connected-Prefix Entropy and n=50 Intake

## Result IDs

- imported theorem: `N1-OBS-003`
- imported finite certificate: `N1-FIN-005`
- Nova 2 intake certificate: `N2-FIN-204`

## Frozen Nova 1 sources

- branch: `nova/factorial-structure`
- handoff head: `471c7122cb2ac96402d133b5af91c97a2f00a23c`
- handoff: `N1-HO-N2-004`
- handoff file: `tracks/nova1-factorial-structure/handoffs/TO_NOVA2_CONNECTED_PREFIX.md`

Connected-prefix theorem:

- proof commit: `ac676b0fc9007117da1f1d9eaeec3e3cf65dd1e7`
- proof: `tracks/nova1-factorial-structure/proofs/CONNECTED_PREFIX_ENTROPY_REQUIREMENT.md`

Finite extension:

- verifier commit: `fd2819255ac17dbba6cc70ed8a78ded387e7cac0`
- report commit: `42e2ac49001215602be7a0808f38648a4557b771`
- verifier: `tracks/nova1-factorial-structure/verification/marker_three_full_core_u128.cpp`
- report: `tracks/nova1-factorial-structure/verification/FULL_CORE_N46_N50_REPORT.md`
- summary data: `tracks/nova1-factorial-structure/verification/full_core_n46_n50_summary.csv`
- layer data: `tracks/nova1-factorial-structure/verification/full_core_n46_n50_layers.csv`

## Decision on N1-OBS-003

Outcome: `ACCEPTED_WITH_RESTRICTIONS`.

Let `K_t` be the number of positive cores in the complete zero-connected prefix at layer `t`, and put

\[
F_t=E_t+W_n+1.
\]

Because the connected prefix has `K_t` positive gaps, each at most

\[
D_t=\left\lfloor\frac{F_{t-1}}{2^{t-1}}\right\rfloor,
\]

its maximum core satisfies

\[
u_t^*\le K_tD_t.
\]

Therefore

\[
F_t
=F_{t-1}+2^{t-1}u_t^*
\le F_{t-1}(1+K_t).
\]

Iteration gives

\[
F_L\le(W_n+1)\prod_{t=1}^{L}(1+K_t).
\]

If the N2-ADD-120 recursion reaches `Y_n`, then necessarily

\[
\prod_{t=1}^{L}(1+K_t)
\ge
\frac{Y_n+1}{W_n+1}.
\]

For every `n>=120368`, Nova 1 further proves the necessary geometric-mean bound

\[
\left(\prod_{t=1}^{L}(1+K_t)\right)^{1/L}
\ge
\exp\left(\frac{n}{85\log n}\right).
\]

The algebra is exact. The restriction is interpretive: this is a necessary condition for the sequential connected-core engine. It neither proves nor disproves that the complete factorial core menus contain prefixes of this size. It does not constrain the final-only Fourier or restricted-sumset engines.

## Audit of N1-FIN-005

Outcome: `ACCEPTED` as an imported finite certificate.

The Nova 1 verifier:

1. certifies `r_n` and `M_n` using rational logarithm bounds;
2. computes factorial valuations and `floor(sqrt(n!))` exactly;
3. reserves one factor of `3` and removes all powers of two;
4. recursively generates every odd core at most `Y_n`;
5. sorts the complete truncated core set;
6. rejects duplicate cores and resource-cap overflow;
7. applies the exact N2-ADD-120 thresholds and endpoints;
8. returns failure if the occupied endpoint does not reach `Y_n`.

The implementation is restricted to `12<=n<=50` by its unsigned 128-bit endpoint contract. This is a fail-closed implementation boundary.

## Exact independent overlap at n=46

Nova 1 independently recomputed the case already frozen by Nova 2 as N2-FIN-203. The following fields match exactly:

- `Y_46=24,726,553,787,403,193,575,874,580,719`;
- `W_46=21,844`;
- total odd-core count `27,941,760`;
- generated odd cores at most `Y_46`: `24,567,748`;
- six layers used;
- every layer scale and core cutoff;
- every gap threshold;
- every connected maximum core;
- all five first blocking gaps;
- absence of a layer-six blocking gap;
- every carrier endpoint;
- final occupied endpoint
  `24,938,550,582,416,882,103,407,947,983`;
- margin
  `211,996,795,013,688,527,533,367,264`.

The layer-by-layer overlap is exact:

| layer | threshold | connected maximum | connected count | carrier endpoint |
|---:|---:|---:|---:|---:|
| 1 | 21,845 | 49,786,217 | 34,440 | 49,786,217 |
| 2 | 24,904,031 | 377,630,859,375 | 460,959 | 755,311,504,967 |
| 3 | 188,827,881,703 | 9,327,107,601,883,071 | 3,095,862 | 37,309,185,719,037,251 |
| 4 | 4,663,648,214,882,387 | 329,182,348,809,878,825,625 | 10,245,320 | 2,633,496,099,664,749,642,251 |
| 5 | 164,593,506,229,046,854,006 | 13,250,220,558,903,267,737,706,909 | 19,665,818 | 212,006,162,438,551,948,552,952,795 |
| 6 | 6,625,192,576,204,748,392,280,457 | 772,704,513,124,322,817,339,217,917 | 22,618,189 | 24,938,550,582,416,882,103,407,926,139 |

This exact overlap independently reconstructs N2-FIN-203 and validates the imported verifier on the shared boundary.

## N2-FIN-204: combined finite extension

Nova 1 certifies every

\[
46\le n\le50
\]

with complete truncated odd-core menus. All five cases reach the full quotient endpoint in six main layers.

Exact endpoint summary:

| `n` | total odd cores | cores at most `Y_n` | occupied margin | term bound |
|---:|---:|---:|---:|---:|
| 46 | 27,941,760 | 24,567,748 | 211,996,795,013,688,527,533,367,264 | 22 |
| 47 | 55,883,520 | 48,966,794 | 3,183,554,256,429,150,696,157,116,324 | 22 |
| 48 | 58,544,640 | 52,400,981 | 3,617,231,946,186,390,762,696,518,337 | 22 |
| 49 | 75,271,680 | 66,785,773 | 4,316,935,435,794,948,182,570,601,486 | 22 |
| 50 | 88,957,440 | 78,715,976 | 4,464,352,838,980,829,594,210,082,828 | 22 |

Combining N2-FIN-202 and the accepted N1-FIN-005 gives exact complete-core carrier coverage for every

\[
12\le n\le50.
\]

Consequently

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
\le22
\qquad(12\le n\le50).
\]

This is a finite theorem assembled from exact certificates. It is not an asymptotic occupancy theorem.

## New exact boundary

The smallest unaudited parameter is now

\[
n=51.
\]

The highest-value sequential theorem target is no longer merely a divisor stream. It is a quantitative lower or upper bound for the complete connected-prefix cardinalities `K_t` under the exact N2-ADD-120 thresholds.

A proof of sufficiently large connected prefixes would promote the carrier engine. A uniform upper bound below N1-OBS-003 would retire that sequential engine. Either outcome leaves the final-only marker-three route logically separate.

## Claim boundary

This intake does not prove success at `n=51`, does not prove the connected-prefix entropy lower bound is attainable, does not remove the Phase 12P audit, and does not solve Erdős Problem 18.
