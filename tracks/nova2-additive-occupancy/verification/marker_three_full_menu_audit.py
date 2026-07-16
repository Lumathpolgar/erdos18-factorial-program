#!/usr/bin/env python3
"""Exact full-menu carrier audit for the marker-three construction.

This script generates every odd core u with 3u | n!, certifies the
logarithmic parameters r_n and M_n using rational bounds, and runs the
N2-ADD-120 connected-core recursion. It is intended for finite exact
certificates only. It does not prove an asymptotic occupancy theorem.
"""

from __future__ import annotations

import argparse
import bisect
import csv
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "nova2.marker-three-full-menu-audit.v1"
SOURCE_NOVA1_COMMIT = "ebb47ba436af554366d0f285119a769f31f9e561"


class AuditError(ValueError):
    """Raised when a requested exact audit cannot be certified."""


def _ceil_fraction(value: Fraction) -> int:
    return -((-value.numerator) // value.denominator)


def _atanh_log_bounds(
    numerator: int, denominator: int, terms: int
) -> tuple[Fraction, Fraction]:
    if numerator < denominator or numerator > 2 * denominator:
        raise AuditError("log ratio must lie in [1, 2]")
    if numerator == denominator:
        return Fraction(0), Fraction(0)
    z = Fraction(numerator - denominator, numerator + denominator)
    z2 = z * z
    power = z
    partial = Fraction(0)
    for j in range(terms):
        partial += power / (2 * j + 1)
        power *= z2
    lower = 2 * partial
    tail = 2 * power / ((2 * terms + 1) * (1 - z2))
    return lower, lower + tail


def natural_log_bounds(n: int, terms: int) -> tuple[Fraction, Fraction]:
    if n < 1:
        raise AuditError("n must be positive")
    if n == 1:
        return Fraction(0), Fraction(0)
    exponent = n.bit_length() - 1
    scale = 1 << exponent
    ln2_lower, ln2_upper = _atanh_log_bounds(2, 1, terms)
    ratio_lower, ratio_upper = _atanh_log_bounds(n, scale, terms)
    return (
        exponent * ln2_lower + ratio_lower,
        exponent * ln2_upper + ratio_upper,
    )


def certified_log_parameters(n: int) -> tuple[int, int]:
    for terms in (8, 12, 16, 24, 32, 48, 64, 96):
        lower, upper = natural_log_bounds(n, terms)
        r_values = (_ceil_fraction(4 * lower), _ceil_fraction(4 * upper))
        m_values = (
            _ceil_fraction(16 * lower * lower),
            _ceil_fraction(16 * upper * upper),
        )
        if r_values[0] == r_values[1] and m_values[0] == m_values[1]:
            return r_values[0], m_values[0]
    raise AuditError(f"could not certify r_n and M_n for n={n}")


def primes_up_to(n: int) -> list[int]:
    sieve = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        sieve[0] = 0
    if n >= 1:
        sieve[1] = 0
    for p in range(2, math.isqrt(n) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return [p for p in range(2, n + 1) if sieve[p]]


def factorial_valuations(n: int) -> dict[int, int]:
    values: dict[int, int] = {}
    for p in primes_up_to(n):
        total = 0
        quotient = n
        while quotient:
            quotient //= p
            total += quotient
        values[p] = total
    return values


def odd_core_valuations(n: int) -> dict[int, int]:
    values = factorial_valuations(n)
    values.pop(2, None)
    if values.get(3, 0) < 1:
        raise AuditError("n! has no factor 3")
    values[3] -= 1
    if values[3] == 0:
        del values[3]
    return values


def divisor_count(values: dict[int, int]) -> int:
    count = 1
    for exponent in values.values():
        count *= exponent + 1
    return count


def odd_core_divisors(n: int, max_divisors: int) -> list[int]:
    values = odd_core_valuations(n)
    expected = divisor_count(values)
    if expected > max_divisors:
        raise AuditError(
            f"n={n} requires {expected} odd cores, above cap {max_divisors}"
        )
    divisors = [1]
    for prime, exponent in sorted(values.items()):
        old = divisors
        divisors = []
        power = 1
        for _ in range(exponent + 1):
            divisors.extend(value * power for value in old)
            power *= prime
    divisors.sort()
    if len(divisors) != expected:
        raise AuditError("odd-core divisor count mismatch")
    return divisors


def audit_n(n: int, max_divisors: int) -> dict[str, Any]:
    if n < 3:
        raise AuditError("n must be at least 3")
    factorial = math.factorial(n)
    x_endpoint = math.isqrt(factorial)
    quotient_endpoint = x_endpoint // 3
    r_value, layer_budget = certified_log_parameters(n)
    window = ((1 << r_value) - 3) // 3
    v2_factorial = factorial_valuations(n)[2]

    if r_value - 1 > v2_factorial:
        raise AuditError(
            f"binary correction palette is not legal at n={n}: "
            f"r_n-1={r_value - 1} > v_2(n!)={v2_factorial}"
        )

    legal_layer_count = min(
        layer_budget,
        v2_factorial + 1,
        max(1, quotient_endpoint.bit_length()),
    )
    cores = odd_core_divisors(n, max_divisors=max_divisors)

    carrier_endpoint = 0
    rows: list[dict[str, Any]] = []
    for t in range(1, legal_layer_count + 1):
        scale = 1 << (t - 1)
        core_bound = quotient_endpoint // scale
        menu_size = bisect.bisect_right(cores, core_bound)
        gap_threshold = (carrier_endpoint + window + 1) // scale

        previous = 0
        connected_max = 0
        first_blocking_gap: dict[str, int] | None = None
        for index in range(menu_size):
            core = cores[index]
            gap = core - previous
            if gap <= gap_threshold:
                connected_max = core
                previous = core
                continue
            first_blocking_gap = {
                "left_core": previous,
                "right_core": core,
                "gap": gap,
            }
            break

        carrier_endpoint += scale * connected_max
        rows.append(
            {
                "t": t,
                "scale": scale,
                "core_bound": core_bound,
                "menu_size": menu_size,
                "gap_threshold": gap_threshold,
                "connected_max_core": connected_max,
                "carrier_endpoint": carrier_endpoint,
                "first_blocking_gap": first_blocking_gap,
            }
        )
        if carrier_endpoint + window >= quotient_endpoint:
            break

    occupied_through = carrier_endpoint + window
    return {
        "n": n,
        "r": r_value,
        "M": layer_budget,
        "v2_factorial": v2_factorial,
        "legal_layer_count": legal_layer_count,
        "X": x_endpoint,
        "Y": quotient_endpoint,
        "W": window,
        "odd_core_divisor_count": len(cores),
        "layers_used": len(rows),
        "carrier_endpoint": carrier_endpoint,
        "occupied_through": occupied_through,
        "margin": occupied_through - quotient_endpoint,
        "reaches_full_endpoint": occupied_through >= quotient_endpoint,
        "term_bound": r_value + len(rows),
        "rows": rows,
    }


def audit_range(
    n_min: int,
    n_max: int,
    max_divisors: int,
) -> dict[str, Any]:
    if n_min > n_max:
        raise AuditError("n_min must not exceed n_max")
    audits = [audit_n(n, max_divisors=max_divisors) for n in range(n_min, n_max + 1)]
    payload: dict[str, Any] = {
        "schema": SCHEMA,
        "result_id": "N2-FIN-202",
        "result_class": "finite certificate",
        "source": {
            "repository": "Lumathpolgar/erdos18-factorial-program",
            "nova1_branch": "nova/factorial-structure",
            "nova1_commit": SOURCE_NOVA1_COMMIT,
            "nova1_construction": "N1-CON-003",
            "nova1_handoff": "N1-HO-N2-002",
            "nova2_theorems": ["N2-ADD-119", "N2-ADD-120"],
        },
        "range": {
            "n_min": n_min,
            "n_max": n_max,
            "all_reach_full_endpoint": all(
                audit["reaches_full_endpoint"] for audit in audits
            ),
        },
        "audits": audits,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["canonical_payload_sha256"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    return payload


def write_csv(path: Path, payload: dict[str, Any]) -> None:
    fields = [
        "n",
        "r",
        "M",
        "v2_factorial",
        "legal_layer_count",
        "layers_used",
        "odd_core_divisor_count",
        "X",
        "Y",
        "W",
        "carrier_endpoint",
        "occupied_through",
        "margin",
        "reaches_full_endpoint",
        "term_bound",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for audit in payload["audits"]:
            writer.writerow({field: audit[field] for field in fields})


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n-min", type=int, default=12)
    parser.add_argument("--n-max", type=int, default=45)
    parser.add_argument("--max-divisors", type=int, default=20_000_000)
    parser.add_argument("--json-output", type=Path)
    parser.add_argument("--csv-output", type=Path)
    args = parser.parse_args()

    try:
        payload = audit_range(
            n_min=args.n_min,
            n_max=args.n_max,
            max_divisors=args.max_divisors,
        )
    except (AuditError, MemoryError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, indent=2))
        return 1

    rendered = json.dumps(payload, indent=2, sort_keys=True)
    print(rendered)
    if args.json_output is not None:
        args.json_output.write_text(rendered + "\n", encoding="utf-8")
    if args.csv_output is not None:
        write_csv(args.csv_output, payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
