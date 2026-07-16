# Independent exact threshold sweep for Nova 3 request G

Date: 2026-07-16

## Frozen source

- handoff: `N3-HO-N4-002`
- handoff commit: `7469dada02fa4caca08ed391ef8b0cb0f1e855b2`
- Nova 3 proof blob: `e36daf98db86da16bd5ed8c6c82f43530d745f66`
- Nova 3 sanity-script blob: `519c900b616a33d95f3b2a8a8dec10d04a0a24f5`
- imported Nova 1 theorem: `N1-STR-009`
- Nova 1 commit: `fa11f4b2cb86a2dd791df189ada12757be791804`
- Nova 1 proof blob: `4255e76ff18f675ae80a0192381070d9a934fc97`

## Decision

| Object | Decision |
|---|---|
| Request G | `ACCEPTED_AS_FINITE_CERTIFICATE` |
| `N3-ANA-011` over the swept interval | `CONFIRMED` |
| Final theorem decision for `N3-ANA-011` | `PENDING_REQUEST_H` |

## Exact coverage

Every one of the `879633` integers in

```text
120368 <= n <= 1000000
```

was checked. Prime counts, Legendre valuations, binary digit sums, address bounds, and capacity exponents are exact integers. The logarithmic ceilings use rigorous rational intervals. Full-range margin ranking uses binary64 only as a screening stage; the retained minima and runner-up gaps are reevaluated at 80-digit Decimal precision.

## Minimum margins

### Prime interval

The minimum of

```text
pi(n)-pi(floor(n/2))-n/(3 log n)
```

occurs at `n=120370`:

```text
exact upper-half prime count = 5254
minimum margin = 1824.164426409610584408894098652982963819708337683028937637810063...
runner-up = n=120369
gap to runner-up = 0.02605837239448723812415727036...
```

### Legendre proof lower bound

The minimum of

```text
v_2(n!) - (n-log_2(n)-1)
```

occurs at `n=131071`:

```text
v_2(131071!) = 131054
minimum margin = 0.999988993068356614813649579045292159...
runner-up = n=262143
gap = 0.000005503476318760647073161096664...
```

### Address legality

The exact minimum slack

```text
floor(v_2(n!)/2)-1-r_n-M_n
```

is `57942`, attained exactly at

```text
n = 120368, 120369, 120370, 120371.
```

At `n=120370`, `r_n=47`, `M_n=2190`, `e_M=2237`, and the legal maximum address is `60179`.

### Conservative profile capacity

The minimum of

```text
M_n*(pi(n)-pi(floor(n/2))-1)+r_n - (1 + n log_2(n)/2)
```

occurs at `n=120370`:

```text
formal profile exponent = 11504117
conservative required bits = 1015750.247298051406649289474161400978...
minimum margin = 10488366.752701948593350710525838599021...
runner-up = n=120369
gap = 9.159902697176993029690666958...
```

## Certified ceiling transitions

Within the audited interval:

```text
r_n transitions: 10, from r=47 at n=120368 to r=56 at n=936590
M_n transitions: 865, from M=2190 at n=120368 to M=3054 at n=997982
```

## Validation

- 12 new threshold-sweep tests pass.
- Full audit replay passes.
- The finite claim certificate passes.
- Legendre division and `n-bit_count(n)` agree for every audited integer.
- A rehashed false minimum-address-slack certificate is rejected.
- Wrong range and wrong frozen-source metadata are rejected.
- Generation completed in approximately 6.75 seconds.
- Peak resident memory was approximately 351132 KiB.
- No timeout or unknown result occurred.

Audit semantic SHA-256:

```text
e26653648c2cc9ebc30b03f01904dbb5bcca65737ead57abc9cdbc0b2f218bb0
```

Claim semantic SHA-256:

```text
e41f7e639c605ed4e70e4ac2cc6afe20d83ef8bf4f22e991fe0986449b9c1e88
```

## Scope restriction

This sweep is a finite certificate. It confirms the exact discrete checks and positive margins throughout the requested interval. It does not establish injectivity of formal profiles, numerical sumset occupancy, the factorial half-range theorem, or Erdős Problem 18. The final theorem-status decision for `N3-ANA-011` remains pending the adversarial semantic checks in request H.

## Next target

Run request H and reject all six specified semantic corruptions, including the profile-count versus distinct-sum conflation and the `pi(ceil(n/2))` endpoint substitution.
