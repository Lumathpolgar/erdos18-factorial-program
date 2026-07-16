"""Independent exact finite audit for Nova 3 product moments and local ceilings.

The finite combinatorial identities are checked with exact integers and Fractions.
Decimal logarithms are used only as a secondary numerical replay of the requested
floating-tolerance claims. Window membership is certified without floating logs.
"""
from __future__ import annotations

from bisect import bisect_left, bisect_right
from decimal import Decimal, localcontext
from fractions import Fraction
from hashlib import sha256
import json
from math import factorial
from pathlib import Path
from typing import Any, Iterable

SCHEMA = "nova4.n3-moment-local-audit.v1"
CLAIM_SCHEMA = "nova4.n3-local-ceiling-claim.v1"
SOURCE = {
    "repository": "Lumathpolgar/erdos18-factorial-program",
    "branch": "nova/analytic-density",
    "commit": "0ce88b28dc2e6641093526f5777bb31f658e3515",
    "handoff": "N3-HO-N4-001",
    "objects": ["N3-ANA-004", "N3-ANA-005"],
}
WIDTHS = (Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(1), Fraction(2))


class AnalyticAuditError(ValueError):
    pass


def _canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def semantic_sha(value: dict[str, Any]) -> str:
    payload = dict(value)
    payload.pop("sha256", None)
    return sha256(_canonical_bytes(payload)).hexdigest()


def primes_up_to(n: int) -> list[int]:
    if isinstance(n, bool) or not isinstance(n, int) or n < 0:
        raise AnalyticAuditError("n must be a nonnegative integer")
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    p = 2
    while p * p <= n:
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
        p += 1
    return [i for i, flag in enumerate(sieve) if flag]


def valuation_factorial(n: int, p: int) -> int:
    total = 0
    quotient = n
    while quotient:
        quotient //= p
        total += quotient
    return total


def factorial_factorization(n: int) -> list[tuple[int, int]]:
    return [(p, valuation_factorial(n, p)) for p in primes_up_to(n)]


def tau_from_factors(factors: Iterable[tuple[int, int]]) -> int:
    result = 1
    for _, exponent in factors:
        result *= exponent + 1
    return result


def enumerate_divisor_vectors(factors: list[tuple[int, int]]) -> list[tuple[int, tuple[int, ...]]]:
    rows: list[tuple[int, tuple[int, ...]]] = [(1, ())]
    for p, exponent in factors:
        next_rows: list[tuple[int, tuple[int, ...]]] = []
        power = 1
        for a in range(exponent + 1):
            for value, vector in rows:
                next_rows.append((value * power, vector + (a,)))
            power *= p
        rows = next_rows
    rows.sort(key=lambda row: row[0])
    values = [value for value, _ in rows]
    if len(values) != len(set(values)):
        raise AnalyticAuditError("duplicate exact divisors generated")
    return rows


def _atanh_log_bounds(numerator: int, denominator: int, terms: int) -> tuple[Fraction, Fraction]:
    if numerator < denominator or numerator > 2 * denominator:
        raise AnalyticAuditError("ratio must lie in [1,2]")
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


def natural_log_bounds_int(n: int, terms: int = 24) -> tuple[Fraction, Fraction]:
    if n < 1:
        raise AnalyticAuditError("log input must be positive")
    if n == 1:
        return Fraction(0), Fraction(0)
    exponent = n.bit_length() - 1
    scale = 1 << exponent
    ln2_lo, ln2_hi = _atanh_log_bounds(2, 1, terms)
    ratio_lo, ratio_hi = _atanh_log_bounds(n, scale, terms)
    return exponent * ln2_lo + ratio_lo, exponent * ln2_hi + ratio_hi


def certified_floor_delta_over_log_prime(delta: Fraction, q: int) -> int:
    if delta < 0:
        raise AnalyticAuditError("delta must be nonnegative")
    if delta == 0:
        return 0
    for terms in (8, 12, 16, 24, 32, 48, 64, 96):
        lo, hi = natural_log_bounds_int(q, terms)
        for k in range(0, 16):
            if k * hi <= delta and (k + 1) * lo > delta:
                return k
    raise AnalyticAuditError(f"could not certify floor(delta/log({q}))")


def exp_bounds(x: Fraction, terms: int) -> tuple[Fraction, Fraction]:
    if x < 0 or x > 2:
        raise AnalyticAuditError("exp audit only supports 0<=x<=2")
    term = Fraction(1)
    partial = term
    for k in range(1, terms + 1):
        term *= x / k
        partial += term
    first_omitted = term * x / (terms + 1)
    ratio_bound = x / (terms + 2)
    if ratio_bound >= 1:
        raise AnalyticAuditError("insufficient exp terms")
    tail = first_omitted / (1 - ratio_bound)
    return partial, partial + tail


def certified_floor_scaled_exp(scale: int, delta: Fraction) -> int:
    if delta == 0:
        return scale
    for terms in (12, 16, 20, 24, 32, 48, 64, 96):
        lo, hi = exp_bounds(delta, terms)
        lower_floor = (scale * lo.numerator) // lo.denominator
        upper_floor = (scale * hi.numerator) // hi.denominator
        if lower_floor == upper_floor:
            return lower_floor
    raise AnalyticAuditError(f"could not certify floor({scale}*exp({delta}))")


def _decimal_string(value: Decimal) -> str:
    return format(value, ".60E")


def exact_moment_record(n: int) -> dict[str, Any]:
    factors = factorial_factorization(n)
    rows = enumerate_divisor_vectors(factors)
    divisors = [value for value, _ in rows]
    vectors = [vector for _, vector in rows]
    tau = tau_from_factors(factors)
    if len(divisors) != tau:
        raise AnalyticAuditError(f"tau mismatch at n={n}")
    factorial_n = factorial(n)
    divisor_set = set(divisors)
    if any(factorial_n // d not in divisor_set for d in divisors):
        raise AnalyticAuditError(f"complement symmetry failed at n={n}")

    coordinate_count = 0
    for index, (p, b) in enumerate(factors):
        sum_a = sum(vector[index] for vector in vectors)
        sum_a2 = sum(vector[index] ** 2 for vector in vectors)
        expected_sum = Fraction(tau * b, 2)
        expected_second = Fraction(tau * b * (2 * b + 1), 6)
        if Fraction(sum_a) != expected_sum or Fraction(sum_a2) != expected_second:
            raise AnalyticAuditError(f"coordinate moment mismatch n={n}, p={p}")
        coordinate_count += 1

    for i in range(len(factors)):
        for j in range(i + 1, len(factors)):
            bi = factors[i][1]
            bj = factors[j][1]
            cross = sum(vector[i] * vector[j] for vector in vectors)
            if Fraction(cross, tau) != Fraction(bi * bj, 4):
                raise AnalyticAuditError(f"coordinate covariance mismatch n={n}")

    with localcontext() as ctx:
        ctx.prec = 80
        logs = [Decimal(d).ln() for d in divisors]
        empirical_mean = sum(logs, Decimal(0)) / Decimal(tau)
        empirical_variance = sum((x - empirical_mean) ** 2 for x in logs) / Decimal(tau)
        formula_mean = sum(Decimal(b) * Decimal(p).ln() / Decimal(2) for p, b in factors)
        formula_variance = sum(
            Decimal(b * (b + 2)) * (Decimal(p).ln() ** 2) / Decimal(12)
            for p, b in factors
        )
        factorial_half_log = Decimal(factorial_n).ln() / Decimal(2)
        mean_diff = abs(empirical_mean - formula_mean)
        variance_diff = abs(empirical_variance - formula_variance)
        factorial_mean_diff = abs(formula_mean - factorial_half_log)
        tolerance = Decimal("1e-50")
        if mean_diff > tolerance or variance_diff > tolerance or factorial_mean_diff > tolerance:
            raise AnalyticAuditError(f"high-precision numerical moment mismatch at n={n}")

    return {
        "n": n,
        "factorial": factorial_n,
        "factorization": [[p, b] for p, b in factors],
        "tau": tau,
        "divisor_count": len(divisors),
        "divisor_unique": True,
        "complement_symmetry": True,
        "coordinate_count": coordinate_count,
        "cross_covariances_zero": True,
        "decimal_precision": 80,
        "empirical_mean": _decimal_string(empirical_mean),
        "formula_mean": _decimal_string(formula_mean),
        "half_log_factorial": _decimal_string(factorial_half_log),
        "mean_abs_difference": _decimal_string(mean_diff),
        "empirical_variance": _decimal_string(empirical_variance),
        "formula_variance": _decimal_string(formula_variance),
        "variance_abs_difference": _decimal_string(variance_diff),
    }


def local_count(divisors: list[int], endpoint: int, delta: Fraction) -> tuple[int, int]:
    left = bisect_left(divisors, endpoint)
    if left >= len(divisors) or divisors[left] != endpoint:
        raise AnalyticAuditError("endpoint must be a divisor")
    upper = certified_floor_scaled_exp(endpoint, delta)
    right = bisect_right(divisors, upper)
    return right - left, upper


def local_ceiling_record(n: int) -> dict[str, Any]:
    factors = factorial_factorization(n)
    rows = enumerate_divisor_vectors(factors)
    divisors = [value for value, _ in rows]
    tau = len(divisors)
    windows_checked = 0
    minimum_slack: int | None = None
    maximum_actual = 0
    tight_count = 0
    first_tight: dict[str, Any] | None = None

    for q, bq in factors:
        for delta in WIDTHS:
            floor_ratio = certified_floor_delta_over_log_prime(delta, q)
            coordinate_choices = floor_ratio + 1
            numerator = tau * coordinate_choices
            if numerator % (bq + 1):
                raise AnalyticAuditError("fiber count does not divide tau")
            ceiling = numerator // (bq + 1)
            for endpoint in divisors:
                actual, upper = local_count(divisors, endpoint, delta)
                windows_checked += 1
                if actual > ceiling:
                    raise AnalyticAuditError(
                        f"local ceiling failed n={n},q={q},delta={delta},endpoint={endpoint}"
                    )
                slack = ceiling - actual
                maximum_actual = max(maximum_actual, actual)
                minimum_slack = slack if minimum_slack is None else min(minimum_slack, slack)
                if slack == 0:
                    tight_count += 1
                    if first_tight is None:
                        first_tight = {
                            "n": n,
                            "q": q,
                            "b_q": bq,
                            "delta": [delta.numerator, delta.denominator],
                            "endpoint_divisor": endpoint,
                            "upper_integer": upper,
                            "actual": actual,
                            "ceiling": ceiling,
                            "coordinate_choices": coordinate_choices,
                        }

    return {
        "n": n,
        "tau": tau,
        "widths": [[d.numerator, d.denominator] for d in WIDTHS],
        "windows_checked": windows_checked,
        "maximum_actual": maximum_actual,
        "minimum_slack": minimum_slack,
        "tight_window_count": tight_count,
        "first_tight_case": first_tight,
    }


def audit_range(n_min: int = 2, n_max: int = 12) -> dict[str, Any]:
    if n_min < 2 or n_max < n_min:
        raise AnalyticAuditError("invalid audit range")
    moment_records = [exact_moment_record(n) for n in range(n_min, n_max + 1)]
    local_records = [local_ceiling_record(n) for n in range(n_min, n_max + 1)]
    audit = {
        "schema": SCHEMA,
        "result_class": "finite certificate",
        "source": SOURCE,
        "range": {"n_min": n_min, "n_max": n_max},
        "moment_records": moment_records,
        "local_ceiling_records": local_records,
        "totals": {
            "n_count": n_max - n_min + 1,
            "divisors_enumerated": sum(record["divisor_count"] for record in moment_records),
            "local_windows_checked": sum(record["windows_checked"] for record in local_records),
            "tight_windows": sum(record["tight_window_count"] for record in local_records),
        },
        "decisions": {
            "N3-ANA-004": "ACCEPTED_FOR_ENUMERATED_RANGE",
            "N3-ANA-005": "ACCEPTED_FOR_ENUMERATED_ENDPOINTS_AND_WIDTHS",
        },
        "scope": "No asymptotic or all-real-endpoint conclusion is inferred from this finite audit.",
    }
    audit["sha256"] = semantic_sha(audit)
    return audit


def verify_audit(audit: dict[str, Any]) -> dict[str, Any]:
    if audit.get("schema") != SCHEMA:
        raise AnalyticAuditError("wrong audit schema")
    if audit.get("source") != SOURCE:
        raise AnalyticAuditError("wrong frozen source metadata")
    if audit.get("sha256") != semantic_sha(audit):
        raise AnalyticAuditError("audit semantic checksum mismatch")
    bounds = audit.get("range")
    if not isinstance(bounds, dict):
        raise AnalyticAuditError("missing range")
    expected = audit_range(bounds["n_min"], bounds["n_max"])
    if _canonical_bytes(expected) != _canonical_bytes(audit):
        raise AnalyticAuditError("audit content differs from independent recomputation")
    return {
        "status": "PASS",
        "sha256": audit["sha256"],
        "n_count": audit["totals"]["n_count"],
        "divisors_enumerated": audit["totals"]["divisors_enumerated"],
        "local_windows_checked": audit["totals"]["local_windows_checked"],
    }


def first_tight_claim(audit: dict[str, Any]) -> dict[str, Any]:
    for record in audit["local_ceiling_records"]:
        tight = record["first_tight_case"]
        if tight is not None:
            claim = {
                "schema": CLAIM_SCHEMA,
                "result_class": "finite certificate",
                "source": SOURCE,
                "claim": tight,
                "claimed_upper_bound": tight["ceiling"],
            }
            claim["sha256"] = semantic_sha(claim)
            return claim
    raise AnalyticAuditError("no tight case found")


def verify_local_ceiling_claim(claim: dict[str, Any]) -> dict[str, Any]:
    if claim.get("schema") != CLAIM_SCHEMA:
        raise AnalyticAuditError("wrong local claim schema")
    if claim.get("source") != SOURCE:
        raise AnalyticAuditError("wrong local claim source")
    if claim.get("sha256") != semantic_sha(claim):
        raise AnalyticAuditError("local claim semantic checksum mismatch")
    item = claim.get("claim")
    if not isinstance(item, dict):
        raise AnalyticAuditError("missing local claim")
    n = item["n"]
    q = item["q"]
    delta = Fraction(*item["delta"])
    endpoint = item["endpoint_divisor"]
    factors = dict(factorial_factorization(n))
    if q not in factors:
        raise AnalyticAuditError("q is not a prime coordinate")
    divisors = [value for value, _ in enumerate_divisor_vectors(factorial_factorization(n))]
    actual, upper = local_count(divisors, endpoint, delta)
    choices = certified_floor_delta_over_log_prime(delta, q) + 1
    ceiling = len(divisors) * choices // (factors[q] + 1)
    claimed_upper = claim.get("claimed_upper_bound")
    if isinstance(claimed_upper, bool) or not isinstance(claimed_upper, int):
        raise AnalyticAuditError("claimed upper bound must be an integer")
    if actual > claimed_upper:
        raise AnalyticAuditError(
            f"corrupted local ceiling: actual {actual} exceeds claimed {claimed_upper}"
        )
    if claimed_upper != ceiling:
        raise AnalyticAuditError("claimed upper bound does not equal theorem ceiling")
    expected_fields = {
        "upper_integer": upper,
        "actual": actual,
        "ceiling": ceiling,
        "coordinate_choices": choices,
        "b_q": factors[q],
    }
    for key, expected in expected_fields.items():
        if item.get(key) != expected:
            raise AnalyticAuditError(f"cached local field mismatch: {key}")
    return {"status": "PASS", "actual": actual, "ceiling": ceiling, "n": n, "q": q}


def write_json(value: dict[str, Any], path: str | Path) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(value, sort_keys=True, indent=2) + "\n", encoding="utf-8")
