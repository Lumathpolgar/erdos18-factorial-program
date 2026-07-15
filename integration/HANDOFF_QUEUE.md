# Handoff Queue

## Status values

- `DRAFT`
- `READY_FOR_REVIEW`
- `UNDER_REVIEW`
- `NEEDS_REPAIR`
- `ACCEPTED`
- `REJECTED`
- `SUPERSEDED`

## Active queue

| Handoff ID | From | To | Object | Status | Link |
|---|---|---|---|---|---|
| H-001 | Integration | Nova 1 | Reconstruct the factorial half-range reduction requirements | DRAFT | Pending launch |
| H-002 | Integration | Nova 2 | Formulate global rainbow occupancy models for factorial layers | DRAFT | Pending launch |
| H-003 | Integration | Nova 3 | Build the factorial divisor scale and density map | DRAFT | Pending launch |
| H-004 | Integration | Nova 4 | Build exact computation and fail-closed verification baseline | DRAFT | Pending launch |

## Queue entry template

```text
Handoff ID:
From:
To:
Object IDs:
Status:
Sending commit:
Review issue or PR:
Date sent:
Date resolved:
Resolution:
Restrictions:
```

## Rules

- Every accepted handoff must point to an immutable commit.
- The receiver records acceptance explicitly.
- A repaired handoff receives a new version.
- Rejected or superseded handoffs remain visible.
- No theorem enters a final proof chain solely because it appears in this queue.
