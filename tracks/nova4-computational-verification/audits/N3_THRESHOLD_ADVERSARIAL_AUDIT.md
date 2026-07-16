# Independent adversarial audit of N3-ANA-011

Date: 2026-07-16

## Frozen source

- repository: `Lumathpolgar/erdos18-factorial-program`
- branch: `nova/analytic-density`
- handoff: `N3-HO-N4-002`
- handoff commit: `7469dada02fa4caca08ed391ef8b0cb0f1e855b2`
- Nova 3 proof blob: `e36daf98db86da16bd5ed8c6c82f43530d745f66`
- Nova 3 sanity-script blob: `519c900b616a33d95f3b2a8a8dec10d04a0a24f5`
- imported Nova 1 theorem: `N1-STR-009`
- Nova 1 commit: `fa11f4b2cb86a2dd791df189ada12757be791804`
- Nova 1 proof blob: `4255e76ff18f675ae80a0192381070d9a934fc97`
- request G audit SHA-256: `e26653648c2cc9ebc30b03f01904dbb5bcca65737ead57abc9cdbc0b2f218bb0`
- request G claim SHA-256: `e41f7e639c605ed4e70e4ac2cc6afe20d83ef8bf4f22e991fe0986449b9c1e88`

No later Nova 3 or Nova 1 revision is included.

## Decisions

| Object | Decision |
|---|---|
| Request H | `ACCEPTED` |
| `N3-ANA-011` | `ACCEPTED` |
| All six required semantic corruptions | `REJECTED` |
| Request G finite sweep | remains `FINITE_CERTIFICATE_ONLY` |

## Independent theorem reconstruction

### Address legality

Write `L=log n`, `V_n=v_2(n!)`,

```text
r_n = ceil(4L)
M_n = ceil(16L^2)
e_M = r_n+M_n.
```

The ceiling inequalities give

```text
e_M <= 16L^2+4L+2.
```

Legendre's identity and the binary digit-sum bound give

```text
V_n >= n-L/log(2)-1.
```

It is sufficient that

```text
n >= 32L^2+(8+1/log(2))L+8.
```

At `n=120368`, elementary rational estimates give `L<12` and `1/log(2)<2`, so the right side is less than

```text
32*12^2+10*12+8 = 4736.
```

The base margin is therefore at least `115632`. The derivative is positive throughout the theorem range because `n-64 log n-10` is increasing for `n>64` and is already greater than `119590` at the threshold. Hence

```text
e_M <= floor(V_n/2)-1
```

for every integer `n>=120368`.

### Imported menu theorem compatibility

The imported `N1-STR-009` menu has exactly the same conditions used by Nova 3:

```text
u divides n!
u is odd
u > 1
2^e u <= floor(sqrt(n!))
0 <= e <= floor(V_n/2)-1.
```

The upper-half primes have valuation one in `n!`. Their `2^m_n` subset products pair under `d -> P_n/d`, giving exactly `2^(m_n-1)` products below `sqrt(P_n)`. The unit is one of those products and the menu excludes it, so the supported lower bound is exactly

```text
|U_e(n)| >= 2^(m_n-1)-1.
```

The floor step is valid directly: a legal address gives

```text
2^e sqrt(O_n) <= sqrt(n!)/2,
```

and `sqrt(n!)/2 <= floor(sqrt(n!))` for `n!>=4`.

### Formal profile capacity

The accepted prime-interval theorem gives

```text
m_n >= n/(3 log n).
```

For `n>=120368`, `n>=12 log n`, so

```text
m_n-1 >= n/(4 log n).
```

Since `M_n>=16(log n)^2`,

```text
M_n(m_n-1) >= 4n log n.
```

The formal profile count is therefore at least

```text
2^(M_n(m_n-1)+r_n) >= 2^(4n log n).
```

Meanwhile

```text
log_2(X_n+1) <= 1+n log n/(2 log 2) < 1+n log n < 4n log n.
```

Thus the formal profile-capacity inequality holds uniformly for every integer `n>=120368`.

## Required semantic corruptions

| ID | Corruption | Result |
|---|---|---|
| H1 | lower `120368` without finite supplementation | rejected |
| H2 | enlarge the legal address maximum beyond `floor(V_n/2)-1` without proof | rejected |
| H3 | remove the `-1` caused by excluding the unit divisor | rejected |
| H4 | treat formal profiles as distinct numerical sums | rejected |
| H5 | replace `pi(floor(n/2))` by `pi(ceil(n/2))` without endpoint analysis | rejected |
| H6 | report the finite request G sweep as an asymptotic proof | rejected |

Every fixture recomputes its outer SHA-256 after the semantic mutation.

For H5, the exact endpoint witness is

```text
n = 120417
floor(n/2) = 60208
ceil(n/2) = 60209
60209 is prime.
```

Therefore `pi(ceil(n/2))=pi(floor(n/2))+1` at this `n`.

## Artifacts

```text
src/factorial_lab/n3_adversarial.py
src/replay_n3_adversarial.py
tests/test_n3_adversarial.py
tests/n3_adversarial_fixtures/*.json
data/analytic/n3_ana_011_contract.json
data/analytic/n3_ana_011_contract.schema.json
data/analytic/n3_threshold_adversarial_audit.json
data/analytic/n3_threshold_adversarial_audit.schema.json
certificates/analytic/n3_ana_011_final_claim.json
certificates/analytic/n3_ana_011_final_claim.schema.json
```

Semantic SHA-256 values:

```text
contract: 63b5e3ae60a38f892768c791765a6f4dd99073586dbeada06e66f7c02b5caf8b
audit: 785517e04e7421348cad72e6e8d20718294dc9edaa32852f3e794ea2637503a9
claim: a254a6dc271b174a8e5f809c67c22c75de5e6163f36e69a018cb0770f9b9b23c
```

## Validation

- 14 new semantic-adversary tests pass;
- canonical contract replay passes;
- full audit replay passes;
- final theorem-claim replay passes;
- all six rehashed fixtures are rejected;
- standalone audit replay completes in approximately 1.49 seconds;
- standalone claim replay completes in approximately 1.34 seconds;
- fixture-directory replay completes in approximately 1.25 seconds;
- peak resident memory is approximately 307 MiB;
- no timeout or unknown result occurred.

## Scope restriction

The accepted theorem establishes address legality, menu cardinality, and formal profile capacity. It does not establish profile injectivity, distinct numerical sums, additive occupancy, the factorial half-range theorem, or Erdős Problem 18.

## Next target

Requests A through H are complete. Independently close the three remaining Nova 3 theorem audits: `N3-ANA-006`, `N3-ANA-008`, and `N3-ANA-009`.
