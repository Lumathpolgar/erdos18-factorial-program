"""Independent Nova 3 scale-convergence and high-prime tail evidence.

All reported transcendental values use Decimal arithmetic at fixed precision. The
artifact is computational evidence only and does not certify an asymptotic theorem.
"""
from __future__ import annotations

import csv
import json
from decimal import Decimal, localcontext
from hashlib import sha256
from math import fsum, isqrt, log, sqrt
from pathlib import Path
from typing import Any, Iterable

SCHEMA = "nova4.n3-scale-evidence.v1"
SOURCE = {
    "repository": "Lumathpolgar/erdos18-factorial-program",
    "branch": "nova/analytic-density",
    "commit": "0ce88b28dc2e6641093526f5777bb31f658e3515",
    "handoff": "N3-HO-N4-001",
    "request": "C",
    "objects": ["N3-ANA-006", "N3-ANA-008"],
}
N_VALUES = (50, 100, 200, 500, 1000, 2000, 5000, 10000)
Y_GRID = (2, 3, 5, 7, 10, 20, 25, 50)
TRACKED_PRIMES = (2, 3, 5, 7)
PRECISION = 80
DIGITS = 50


class ScaleEvidenceError(ValueError):
    pass


def _canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def semantic_sha(value: dict[str, Any]) -> str:
    payload = dict(value)
    payload.pop("sha256", None)
    return sha256(_canonical_bytes(payload)).hexdigest()


def _require_int(name: str, value: object, minimum: int = 0) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ScaleEvidenceError(f"{name} must be an integer at least {minimum}")
    return value


def primes_up_to(n: int) -> list[int]:
    n = _require_int("n", n)
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
    n = _require_int("n", n)
    p = _require_int("p", p, minimum=2)
    total = 0
    quotient = n
    while quotient:
        quotient //= p
        total += quotient
    return total


def _fmt(value: Decimal) -> str:
    return format(value, f".{DIGITS}E")


def _contributions(n: int, primes: Iterable[int]) -> dict[int, Decimal]:
    result: dict[int, Decimal] = {}
    with localcontext() as ctx:
        ctx.prec = PRECISION
        for p in primes:
            b = valuation_factorial(n, p)
            logp = Decimal(p).ln()
            result[p] = Decimal(b * (b + 2)) * logp * logp / Decimal(12)
    return result


def scale_row(n: int, primes: list[int] | None = None) -> dict[str, Any]:
    n = _require_int("n", n, minimum=2)
    ps = list(primes) if primes is not None else primes_up_to(n)
    if not ps or ps[-1] > n:
        raise ScaleEvidenceError("invalid prime list")
    with localcontext() as ctx:
        ctx.prec = PRECISION
        contributions = _contributions(n, ps)
        variance = sum(contributions.values(), Decimal(0))
        square_sum = sum((v * v for v in contributions.values()), Decimal(0))
        log_tau = sum(
            (Decimal(valuation_factorial(n, p) + 1).ln() for p in ps), Decimal(0)
        )
        n_dec = Decimal(n)
        ratio = log_tau / (n_dec / n_dec.ln())
        variance_ratio = variance / (n_dec * n_dec)
        effective_dimension = variance * variance / square_sum
        shares = {
            str(p): _fmt(contributions.get(p, Decimal(0)) / variance)
            for p in TRACKED_PRIMES
        }
        tracked = sum(
            (contributions.get(p, Decimal(0)) for p in TRACKED_PRIMES), Decimal(0)
        ) / variance
        return {
            "n": n,
            "prime_count": len(ps),
            "log_tau_over_n_over_log_n": _fmt(ratio),
            "variance_over_n_squared": _fmt(variance_ratio),
            "variance_shares": shares,
            "tracked_prime_share_total": _fmt(tracked),
            "effective_dimension": _fmt(effective_dimension),
            "variance": _fmt(variance),
            "log_tau": _fmt(log_tau),
        }


def high_prime_tail_row(
    n: int, y: int, primes: list[int] | None = None
) -> dict[str, Any]:
    n = _require_int("n", n, minimum=2)
    y = _require_int("y", y, minimum=1)
    ps = list(primes) if primes is not None else primes_up_to(n)
    tail = [p for p in ps if p > y]
    if not tail:
        raise ScaleEvidenceError("empty high-prime tail")
    with localcontext() as ctx:
        ctx.prec = PRECISION
        variance = Decimal(0)
        maximum_half_span = Decimal(0)
        maximizing_prime = None
        for p in tail:
            b = valuation_factorial(n, p)
            logp = Decimal(p).ln()
            variance += Decimal(b * (b + 2)) * logp * logp / Decimal(12)
            half_span = Decimal(b) * logp / Decimal(2)
            if half_span > maximum_half_span:
                maximum_half_span = half_span
                maximizing_prime = p
        b_scale = variance.sqrt()
        ratio = maximum_half_span / b_scale
        supplied = Decimal(2) * maximum_half_span / b_scale
        return {
            "n": n,
            "y": y,
            "tail_prime_count": len(tail),
            "theorem_hypothesis_2y_le_sqrt_n": 4 * y * y <= n,
            "maximizing_prime": maximizing_prime,
            "B_squared": _fmt(variance),
            "B": _fmt(b_scale),
            "M": _fmt(maximum_half_span),
            "M_over_B": _fmt(ratio),
            "supplied_script_span_over_B": _fmt(supplied),
            "supplied_script_to_theorem_ratio": _fmt(supplied / ratio),
        }


def supplied_script_scale_row(n: int, primes: list[int]) -> dict[str, float]:
    log_tau = fsum(log(valuation_factorial(n, p) + 1) for p in primes)
    contributions = {
        p: valuation_factorial(n, p)
        * (valuation_factorial(n, p) + 2)
        * log(p) ** 2
        / 12.0
        for p in primes
    }
    variance = fsum(contributions.values())
    square_sum = fsum(value * value for value in contributions.values())
    return {
        "log_tau_over_n_over_log_n": log_tau / (n / log(n)),
        "variance_over_n_squared": variance / (n * n),
        "share_2": contributions.get(2, 0.0) / variance,
        "share_3": contributions.get(3, 0.0) / variance,
        "effective_dimension": variance * variance / square_sum,
    }


def supplied_script_tail_ratio(n: int, y: int, primes: list[int]) -> float:
    variance = 0.0
    maximum_span = 0.0
    for p in primes:
        if p <= y:
            continue
        b = valuation_factorial(n, p)
        logp = log(p)
        variance += b * (b + 2) * logp * logp / 12.0
        maximum_span = max(maximum_span, b * logp)
    if variance <= 0.0:
        raise ScaleEvidenceError("empty supplied-script high-prime tail")
    return maximum_span / sqrt(variance)


def limit_proxy(prime_limit: int = 1_000_000) -> dict[str, Any]:
    prime_limit = _require_int("prime_limit", prime_limit, minimum=2)
    ps = primes_up_to(prime_limit)
    with localcontext() as ctx:
        ctx.prec = PRECISION
        total = sum(
            (
                Decimal(p).ln() ** 2
                / (Decimal(12) * Decimal((p - 1) ** 2))
                for p in ps
            ),
            Decimal(0),
        )
    return {
        "prime_limit": prime_limit,
        "prime_count": len(ps),
        "truncated_variance_limit_constant": _fmt(total),
        "classification": "computational evidence proxy, not a certified full infinite sum",
    }


def build_evidence(
    n_values: Iterable[int] = N_VALUES,
    y_grid: Iterable[int] = Y_GRID,
    *,
    proxy_prime_limit: int = 1_000_000,
) -> dict[str, Any]:
    ns = tuple(n_values)
    ys = tuple(y_grid)
    if ns != tuple(sorted(set(ns))) or any(n < 2 for n in ns):
        raise ScaleEvidenceError("n_values must be strictly increasing integers >=2")
    if ys != tuple(sorted(set(ys))) or any(y < 1 for y in ys):
        raise ScaleEvidenceError("y_grid must be strictly increasing positive integers")
    all_primes = primes_up_to(max(max(ns), proxy_prime_limit))
    scale_rows: list[dict[str, Any]] = []
    tail_rows: list[dict[str, Any]] = []
    for n in ns:
        ps = [p for p in all_primes if p <= n]
        scale_rows.append(scale_row(n, ps))
        for y in ys:
            if y < n:
                tail_rows.append(high_prime_tail_row(n, y, ps))

    proxy = limit_proxy(proxy_prime_limit)
    proxy_value = Decimal(proxy["truncated_variance_limit_constant"])
    convergence_rows = []
    theorem_path_rows = []
    for row in scale_rows:
        variance_ratio = Decimal(row["variance_over_n_squared"])
        convergence_rows.append(
            {
                "n": row["n"],
                "variance_ratio_minus_proxy": _fmt(variance_ratio - proxy_value),
                "variance_ratio_over_proxy": _fmt(variance_ratio / proxy_value),
            }
        )
        n = row["n"]
        y = max(1, isqrt(n) // 2)
        theorem_path_rows.append(
            high_prime_tail_row(n, y, [p for p in all_primes if p <= n])
        )

    scale_comparison = []
    maximum_scale_difference = Decimal(0)
    for row in scale_rows:
        n = row["n"]
        ps = [p for p in all_primes if p <= n]
        supplied = supplied_script_scale_row(n, ps)
        pairs = {
            "log_tau_over_n_over_log_n": (
                Decimal(row["log_tau_over_n_over_log_n"]),
                Decimal(str(supplied["log_tau_over_n_over_log_n"])),
            ),
            "variance_over_n_squared": (
                Decimal(row["variance_over_n_squared"]),
                Decimal(str(supplied["variance_over_n_squared"])),
            ),
            "share_2": (
                Decimal(row["variance_shares"]["2"]),
                Decimal(str(supplied["share_2"])),
            ),
            "share_3": (
                Decimal(row["variance_shares"]["3"]),
                Decimal(str(supplied["share_3"])),
            ),
            "effective_dimension": (
                Decimal(row["effective_dimension"]),
                Decimal(str(supplied["effective_dimension"])),
            ),
        }
        differences = {key: _fmt(abs(a - b)) for key, (a, b) in pairs.items()}
        maximum_scale_difference = max(
            maximum_scale_difference, *(abs(a - b) for a, b in pairs.values())
        )
        scale_comparison.append({"n": n, "absolute_differences": differences})

    supplied_points = (
        (1000, 5),
        (1000, 10),
        (1000, 20),
        (5000, 10),
        (5000, 20),
        (5000, 50),
        (10000, 10),
        (10000, 25),
        (10000, 50),
    )
    tail_comparison = []
    maximum_tail_difference = Decimal(0)
    for n, y in supplied_points:
        ps = [p for p in all_primes if p <= n]
        independent = high_prime_tail_row(n, y, ps)
        supplied = Decimal(str(supplied_script_tail_ratio(n, y, ps)))
        difference = abs(
            Decimal(independent["supplied_script_span_over_B"]) - supplied
        )
        maximum_tail_difference = max(maximum_tail_difference, difference)
        tail_comparison.append(
            {"n": n, "y": y, "absolute_difference": _fmt(difference)}
        )

    evidence = {
        "schema": SCHEMA,
        "result_class": "computational evidence",
        "source": SOURCE,
        "decimal_precision": PRECISION,
        "n_values": list(ns),
        "y_grid": list(ys),
        "tracked_primes": list(TRACKED_PRIMES),
        "scale_rows": scale_rows,
        "convergence_rows": convergence_rows,
        "high_prime_tail_rows": tail_rows,
        "theorem_path_rule": "y_n=floor(sqrt(n))/2 using integer square root",
        "theorem_path_rows": theorem_path_rows,
        "limit_proxy": proxy,
        "supplied_script_comparison": {
            "scale_rows": "same formulas for log-tau ratio, variance ratio, shares 2 and 3, and effective dimension",
            "scale_row_comparisons": scale_comparison,
            "maximum_scale_absolute_difference": _fmt(maximum_scale_difference),
            "tail_ratio": "frozen script reports b_p log(p)/B; theorem N3-ANA-008 defines M=b_p log(p)/2, so script values are exactly 2 times M/B",
            "tail_point_comparisons": tail_comparison,
            "maximum_tail_absolute_difference": _fmt(maximum_tail_difference),
            "decision": "NEEDS_REPAIR_FOR_TAIL_RATIO_LABEL",
        },
        "scope": "Finite deterministic evidence only; no convergence rate or asymptotic theorem is inferred.",
    }
    evidence["sha256"] = semantic_sha(evidence)
    return evidence


def verify_evidence(evidence: dict[str, Any]) -> dict[str, Any]:
    if evidence.get("schema") != SCHEMA:
        raise ScaleEvidenceError("wrong scale evidence schema")
    if evidence.get("source") != SOURCE:
        raise ScaleEvidenceError("wrong frozen source metadata")
    if evidence.get("sha256") != semantic_sha(evidence):
        raise ScaleEvidenceError("scale evidence semantic checksum mismatch")
    expected = build_evidence(
        evidence["n_values"],
        evidence["y_grid"],
        proxy_prime_limit=evidence["limit_proxy"]["prime_limit"],
    )
    if _canonical_bytes(expected) != _canonical_bytes(evidence):
        raise ScaleEvidenceError("scale evidence differs from independent recomputation")
    return {
        "status": "PASS",
        "sha256": evidence["sha256"],
        "scale_rows": len(evidence["scale_rows"]),
        "tail_rows": len(evidence["high_prime_tail_rows"]),
        "theorem_path_rows": len(evidence["theorem_path_rows"]),
        "tail_ratio_script_decision": evidence["supplied_script_comparison"][
            "decision"
        ],
    }


def write_json(value: dict[str, Any], path: str | Path) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(value, sort_keys=True, indent=2) + "\n", encoding="utf-8"
    )


def write_csvs(
    evidence: dict[str, Any], scale_path: str | Path, tail_path: str | Path
) -> None:
    scale_target = Path(scale_path)
    tail_target = Path(tail_path)
    scale_target.parent.mkdir(parents=True, exist_ok=True)
    tail_target.parent.mkdir(parents=True, exist_ok=True)
    with scale_target.open("w", newline="", encoding="utf-8") as handle:
        fields = [
            "n",
            "prime_count",
            "log_tau_over_n_over_log_n",
            "variance_over_n_squared",
            "share_2",
            "share_3",
            "share_5",
            "share_7",
            "tracked_prime_share_total",
            "effective_dimension",
        ]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in evidence["scale_rows"]:
            writer.writerow(
                {
                    "n": row["n"],
                    "prime_count": row["prime_count"],
                    "log_tau_over_n_over_log_n": row[
                        "log_tau_over_n_over_log_n"
                    ],
                    "variance_over_n_squared": row["variance_over_n_squared"],
                    "share_2": row["variance_shares"]["2"],
                    "share_3": row["variance_shares"]["3"],
                    "share_5": row["variance_shares"]["5"],
                    "share_7": row["variance_shares"]["7"],
                    "tracked_prime_share_total": row["tracked_prime_share_total"],
                    "effective_dimension": row["effective_dimension"],
                }
            )
    with tail_target.open("w", newline="", encoding="utf-8") as handle:
        fields = [
            "n",
            "y",
            "tail_prime_count",
            "theorem_hypothesis_2y_le_sqrt_n",
            "maximizing_prime",
            "B_squared",
            "M",
            "M_over_B",
            "supplied_script_span_over_B",
            "supplied_script_to_theorem_ratio",
        ]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in evidence["high_prime_tail_rows"]:
            writer.writerow({key: row[key] for key in fields})
