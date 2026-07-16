# Nova 4 Status

Date: 2026-07-16

## Track

Computation, Falsification, and Verification

## Branch

`nova/computational-verification`

## Overall state

`NOVA3_REQUEST_H_ADVERSARIAL_AUDIT_COMPLETE`

## Active results

See `DATASETS.md`, `VERIFIER_REGISTRY.md`, and the audit directory for the complete checkpoint registry.

The newest active result is:

| ID | Result class | Exact statement | Artifact |
|---|---|---|---|
| N4-AUD-011 | `semantic adversarial theorem audit` | All six required request H corruptions are rejected and `N3-ANA-011` is independently accepted with formal-profile-only scope | `audits/N3_THRESHOLD_ADVERSARIAL_AUDIT.md` |

## Verified coverage

```text
factorial half-ranges: n = 1 through 13
representation targets: 109,947
N2 lattice transition audit: every n = 3 through 10,000
Nova 1 capacity audit: every n = 3 through 1,000,000
Nova 1 reduced-rainbow audit: every n = 20 through 80
Nova 3 moment audit: every n = 2 through 12
Nova 3 exact divisors enumerated: 1,978
Nova 3 local windows checked: 45,840
Nova 3 recurrence scores: 19,990,010
Nova 3 request G integers checked: 879,633
request H semantic corruptions rejected: 6 of 6
request H endpoint witness: n=120417, ceil(n/2)=60209 prime
new Nova 3 adversarial tests: 14 passing
```

## Accepted Nova 3 theorem audits

```text
N3-ANA-004: ACCEPTED
N3-ANA-005: ACCEPTED
N3-ANA-007: ACCEPTED
N3-ANA-010: ACCEPTED
N3-ANA-011: ACCEPTED
```

`N3-ANA-011` proves address legality, menu cardinality, and formal profile capacity for every integer `n>=120368`. It does not prove profile injectivity, distinct numerical sums, additive occupancy, the factorial half-range theorem, or Erdős Problem 18.

## Current limitations

- No asymptotic factorial half-range theorem is proved.
- `N3-ANA-006`, `N3-ANA-008`, and `N3-ANA-009` remain theorem-audit pending.
- Nova 3 request C remains computational evidence only.
- Request G remains a finite certificate rather than an asymptotic proof.
- No Track B source package is present for reconstruction.
- The `n=14` exact representation profile remains `unknown due to resource limits`.

## Next audit target

Independently reconstruct and decide `N3-ANA-006`, the variance asymptotic, then close `N3-ANA-008` and `N3-ANA-009`.
