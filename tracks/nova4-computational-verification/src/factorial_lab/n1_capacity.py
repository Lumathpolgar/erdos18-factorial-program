"""Exact finite audit for Nova 1 capacity predicates in N1-HO-N4-001.

The capacity predicate C_n is checked without constructing n! as a floating-point
number.  For integer K and X=floor(sqrt(n!)),

    2^K >= X + 1  <=>  2^(2K) > n!.

For n >= 13 in the frozen finite range, the stronger exact certificate

    2K >= n * bit_length(n)

implies 2^(2K) >= 2^(n bit_length(n)) > n^n >= n!, because n <
2^bit_length(n).  Small n are decided by exact integer factorial and isqrt.
"""

from __future__ import annotations

import csv
import hashlib
import json
from array import array
from decimal import Decimal, localcontext, ROUND_CEILING, ROUND_FLOOR
from fractions import Fraction
from math import factorial, isqrt
from pathlib import Path
from typing import Any

from .logcert import certified_log_parameter_tables, natural_log_bounds


NOVA1_BRANCH = "nova/factorial-structure"
NOVA1_COMMIT = "fa11f4b2cb86a2dd791df189ada12757be791804"
NOVA1_HANDOFF = "N1-HO-N4-001"
SCHEMA = "nova4.n1-capacity-audit.v1"


class CapacityCertificationError(ValueError):
    """Raised when a claimed capacity audit cannot be certified."""


def _require_int(name: str, value: Any, *, minimum: int | None = None) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CapacityCertificationError(f"{name} must be an integer")
    if minimum is not None and value < minimum:
        raise CapacityCertificationError(f"{name} must be at least {minimum}")
    return value


def _canonical_json(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def _sha256_payload(payload: dict[str, Any]) -> str:
    return hashlib.sha256(_canonical_json(payload)).hexdigest()


def _prime_flags_and_prefix(limit: int) -> tuple[bytearray, array]:
    limit = _require_int("limit", limit, minimum=0)
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for p in range(2, isqrt(limit) + 1):
        if flags[p]:
            start = p * p
            flags[start : limit + 1 : p] = b"\x00" * (
                ((limit - start) // p) + 1
            )
    prefix = array("I", [0]) * (limit + 1)
    count = 0
    for n, flag in enumerate(flags):
        count += int(flag)
        prefix[n] = count
    return flags, prefix


def _fraction_decimal(value: Fraction, *, places: int, rounding: str) -> str:
    if places < 1:
        raise ValueError("places must be positive")
    with localcontext() as context:
        context.prec = places
        context.rounding = rounding
        result = Decimal(value.numerator) / Decimal(value.denominator)
        return format(result, "f")


def _margin_interval_for_exact_denominator(K: int, denominator: int) -> dict[str, Any]:
    """Certify K log(2)-log(denominator) by rational atanh series bounds."""
    ln2_lower, ln2_upper = natural_log_bounds(2, terms=64)
    logd_lower, logd_upper = natural_log_bounds(denominator, terms=64)
    lower = K * ln2_lower - logd_upper
    upper = K * ln2_upper - logd_lower
    return {
        "lower_decimal": _fraction_decimal(lower, places=32, rounding=ROUND_FLOOR),
        "upper_decimal": _fraction_decimal(upper, places=32, rounding=ROUND_CEILING),
        "proof": f"{K}*log(2)-log({denominator}) with 64-term rational bounds",
    }


def _margin_lower_bound_from_bit_length(n: int, K: int) -> dict[str, Any]:
    """Return a rigorous lower bound for K log2-log(X+1), X=floor sqrt(n!)."""
    bits = n.bit_length()
    twice_coefficient = 2 * K - bits * n - 2
    if twice_coefficient <= 0:
        raise CapacityCertificationError(
            f"bit-length margin certificate is not positive at n={n}"
        )
    ln2_lower, _ = natural_log_bounds(2, terms=64)
    lower = Fraction(twice_coefficient, 2) * ln2_lower
    return {
        "twice_log2_coefficient": twice_coefficient,
        "lower_decimal": _fraction_decimal(lower, places=32, rounding=ROUND_FLOOR),
        "proof": (
            "X+1 < 2^(n*bit_length(n)/2+1), hence margin > "
            "(K-n*bit_length(n)/2-1)*log(2)"
        ),
    }


def _capacity_row(
    n: int, prime_prefix: array, r_values: list[int], m_values: list[int]
) -> dict[str, Any]:
    r, M = r_values[n], m_values[n]
    V = n - n.bit_count()
    m = int(prime_prefix[n] - prime_prefix[n // 2])
    K = M * (m - 1) + r
    A = r + M <= V // 2 - 1

    if n <= 12:
        N = factorial(n)
        X = isqrt(N)
        C = (1 << K) >= X + 1
        c_method = "exact factorial and integer isqrt"
        c_slack = None
    else:
        bits = n.bit_length()
        c_slack = 2 * K - bits * n
        if c_slack < 0:
            raise CapacityCertificationError(
                f"strong exact C_n certificate is inconclusive at n={n}"
            )
        C = True
        c_method = "exact n!<=n^n bit-length domination"

    return {
        "n": n,
        "V": V,
        "m": m,
        "r": r,
        "M": M,
        "K": K,
        "A": A,
        "C": C,
        "both": A and C,
        "C_certification_method": c_method,
        "C_bit_slack": c_slack,
    }


def _success_intervals(statuses: list[bool], n_min: int) -> list[tuple[int, int]]:
    intervals: list[tuple[int, int]] = []
    start: int | None = None
    for offset, status in enumerate(statuses):
        n = n_min + offset
        if status and start is None:
            start = n
        elif not status and start is not None:
            intervals.append((start, n - 1))
            start = None
    if start is not None:
        intervals.append((start, n_min + len(statuses) - 1))
    return intervals


def _certify_c_interval_minimum(
    interval: tuple[int, int], small_rows: dict[int, dict[str, Any]],
    large_min: tuple[int, int, int] | None,
) -> dict[str, Any]:
    start, end = interval
    candidates: list[tuple[int, dict[str, Any]]] = []
    for n in range(start, min(end, 12) + 1):
        row = small_rows[n]
        denominator = isqrt(factorial(n)) + 1
        candidates.append((n, _margin_interval_for_exact_denominator(row["K"], denominator)))

    chosen_n: int | None = None
    chosen: dict[str, Any] | None = None
    for n, interval_data in candidates:
        if chosen is None or Decimal(interval_data["upper_decimal"]) < Decimal(
            chosen["upper_decimal"]
        ):
            chosen_n, chosen = n, interval_data

    comparison_notes: list[str] = []
    if end >= 13:
        if large_min is None:
            raise CapacityCertificationError("missing large-n margin certificate")
        large_n, twice_coeff, large_K = large_min
        large_bound = _margin_lower_bound_from_bit_length(large_n, large_K)
        comparison_notes.append(
            f"For every n in [{max(start,13)},{end}], the minimum certified bit-bound "
            f"coefficient occurs at n={large_n} with twice coefficient {twice_coeff}."
        )
        if chosen is None:
            return {
                "interval": [start, end],
                "minimum_certified_at_n": large_n,
                "margin": large_bound,
                "scope": "minimum of the committed rigorous lower bounds",
            }
        if Decimal(large_bound["lower_decimal"]) <= Decimal(chosen["upper_decimal"]):
            raise CapacityCertificationError(
                "large-n lower bound does not separate from small-n candidate"
            )
        comparison_notes.append(
            "That large-n lower bound exceeds the selected small-n upper bound."
        )

    if chosen_n is None or chosen is None:
        raise CapacityCertificationError("could not identify a C-success margin minimum")

    for n, interval_data in candidates:
        if n == chosen_n:
            continue
        if Decimal(interval_data["lower_decimal"]) <= Decimal(chosen["upper_decimal"]):
            raise CapacityCertificationError(
                f"small-n margin intervals do not separate at n={chosen_n} and n={n}"
            )
    comparison_notes.append(
        "All other small-n candidate lower bounds exceed the selected upper bound."
    )
    return {
        "interval": [start, end],
        "minimum_certified_at_n": chosen_n,
        "margin": chosen,
        "scope": "actual minimum over the entire finite success interval",
        "comparison_notes": comparison_notes,
    }


def audit_n1_capacity_range(n_min: int, n_max: int) -> dict[str, Any]:
    """Audit A_n and C_n exactly/certifiably on every integer in a finite range."""
    n_min = _require_int("n_min", n_min, minimum=3)
    n_max = _require_int("n_max", n_max, minimum=n_min)
    _, prime_prefix = _prime_flags_and_prefix(n_max)
    r_values, m_values = certified_log_parameter_tables(n_max)

    statuses_A = bytearray()
    statuses_C = bytearray()
    statuses_both = bytearray()
    transitions: list[dict[str, Any]] = []
    later_A: list[int] = []
    later_C: list[int] = []
    small_rows: dict[int, dict[str, Any]] = {}
    first_A = first_C = first_both = None
    seen_A = seen_C = False
    prior_pair: tuple[bool, bool] | None = None

    for n in range(n_min, n_max + 1):
        row = _capacity_row(n, prime_prefix, r_values, m_values)
        if n <= 12:
            small_rows[n] = row
        A, C, both = row["A"], row["C"], row["both"]
        statuses_A.append(int(A))
        statuses_C.append(int(C))
        statuses_both.append(int(both))
        if A and first_A is None:
            first_A = n
        if C and first_C is None:
            first_C = n
        if both and first_both is None:
            first_both = n
        if seen_A and not A:
            later_A.append(n)
        if seen_C and not C:
            later_C.append(n)
        seen_A = seen_A or A
        seen_C = seen_C or C
        pair = (A, C)
        if prior_pair is None or pair != prior_pair:
            transitions.append(row)
            prior_pair = pair

    c_intervals = _success_intervals(statuses_C, n_min)
    margin_minima: list[dict[str, Any]] = []
    for interval in c_intervals:
        interval_large_min: tuple[int, int, int] | None = None
        if interval[1] >= 13:
            for n in range(max(interval[0], 13), interval[1] + 1):
                r = r_values[n]
                M = m_values[n]
                m = int(prime_prefix[n] - prime_prefix[n // 2])
                K = M * (m - 1) + r
                twice_coeff = 2 * K - n.bit_length() * n - 2
                if twice_coeff <= 0:
                    raise CapacityCertificationError(
                        f"positive margin lower bound failed at n={n}"
                    )
                if interval_large_min is None or twice_coeff < interval_large_min[1]:
                    interval_large_min = (n, twice_coeff, K)
        margin_minima.append(
            _certify_c_interval_minimum(interval, small_rows, interval_large_min)
        )

    payload = {
        "schema": SCHEMA,
        "result_class": "exact finite theorem audit",
        "source": {
            "repository": "Lumathpolgar/erdos18-factorial-program",
            "branch": NOVA1_BRANCH,
            "commit": NOVA1_COMMIT,
            "handoff": NOVA1_HANDOFF,
            "study": "Study A exact capacity-threshold audit",
        },
        "range": {"n_min": n_min, "n_max": n_max, "count": n_max - n_min + 1},
        "definitions": {
            "V": "v_2(n!)=n-popcount(n)",
            "m": "pi(n)-pi(floor(n/2))",
            "r": "ceil(4 log n), rationally certified",
            "M": "ceil(16 (log n)^2), rationally certified",
            "K": "M*(m-1)+r",
            "A": "r+M <= floor(V/2)-1",
            "C": "2^K >= floor(sqrt(n!))+1",
        },
        "first_success": {"A": first_A, "C": first_C, "both": first_both},
        "later_failures_after_first_success": {"A": later_A, "C": later_C},
        "success_intervals": {
            "A": [list(item) for item in _success_intervals(statuses_A, n_min)],
            "C": [list(item) for item in c_intervals],
            "both": [list(item) for item in _success_intervals(statuses_both, n_min)],
        },
        "C_success_interval_minimum_margins": margin_minima,
        "transitions": transitions,
        "certification": {
            "C_integer_equivalence": "2^K >= X+1 iff 2^(2K)>n!, X=floor(sqrt(n!))",
            "small_n": "exact factorial, integer isqrt, and exact power-of-two comparison",
            "n_at_least_13": (
                "verified 2K>=n*bit_length(n); then n!<=n^n<2^(n*bit_length(n))"
            ),
            "margin_bounds": "rational atanh log bounds and exact bit-length domination",
            "timeout_semantics": "any inconclusive comparison raises and produces no pass",
        },
    }
    return {**payload, "sha256": _sha256_payload(payload)}


def verify_n1_capacity_audit(audit: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(audit, dict):
        raise CapacityCertificationError("audit must be an object")
    if audit.get("schema") != SCHEMA:
        raise CapacityCertificationError("unsupported capacity audit schema")
    source = audit.get("source")
    if not isinstance(source, dict):
        raise CapacityCertificationError("source must be an object")
    expected_source = {
        "repository": "Lumathpolgar/erdos18-factorial-program",
        "branch": NOVA1_BRANCH,
        "commit": NOVA1_COMMIT,
        "handoff": NOVA1_HANDOFF,
        "study": "Study A exact capacity-threshold audit",
    }
    if source != expected_source:
        raise CapacityCertificationError("source metadata does not match frozen handoff")
    range_data = audit.get("range")
    if not isinstance(range_data, dict):
        raise CapacityCertificationError("range must be an object")
    n_min = _require_int("range.n_min", range_data.get("n_min"), minimum=3)
    n_max = _require_int("range.n_max", range_data.get("n_max"), minimum=n_min)
    claimed_sha = audit.get("sha256")
    payload = {key: value for key, value in audit.items() if key != "sha256"}
    if claimed_sha != _sha256_payload(payload):
        raise CapacityCertificationError("capacity audit checksum mismatch")
    recomputed = audit_n1_capacity_range(n_min, n_max)
    if recomputed != audit:
        raise CapacityCertificationError("capacity audit does not match exact recomputation")
    return {
        "status": "PASS",
        "result_class": "exact finite theorem audit",
        "range": [n_min, n_max],
        "sha256": claimed_sha,
        "first_success": audit["first_success"],
        "transition_count": len(audit["transitions"]),
    }


def write_capacity_audit(audit: dict[str, Any], json_path: str | Path, csv_path: str | Path) -> None:
    json_path = Path(json_path)
    csv_path = Path(csv_path)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with json_path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(audit, handle, sort_keys=True, indent=2, ensure_ascii=False)
        handle.write("\n")
    fields = [
        "n", "V", "m", "r", "M", "K", "A", "C", "both",
        "C_certification_method", "C_bit_slack",
    ]
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in audit["transitions"]:
            writer.writerow({field: row.get(field) for field in fields})
