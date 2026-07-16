"""Bounded characteristic-function recurrence evidence for Nova 3.

The exhaustive finite scan uses IEEE 754 binary64 arithmetic to rank every integer
q in an explicit range. Retained finalists are reevaluated with Decimal arithmetic
at a fixed precision and independently cross-checked by direct averaging over the
exact divisor exponent vectors. The numerical artifact is computational evidence,
not a proof of an unbounded limsup statement.
"""
from __future__ import annotations

from decimal import Decimal, ROUND_HALF_EVEN, localcontext
from hashlib import sha256
from heapq import heappush, heapreplace
from itertools import product
import cmath
import csv
import json
import math
from pathlib import Path
from typing import Any, Iterable

SCHEMA = "nova4.n3-characteristic-recurrence-evidence.v1"
CANDIDATE_SCHEMA = "nova4.n3-characteristic-recurrence-candidate.v1"
SOURCE = {
    "repository": "Lumathpolgar/erdos18-factorial-program",
    "branch": "nova/analytic-density",
    "handoff": "N3-HO-N4-002",
    "handoff_commit": "7469dada02fa4caca08ed391ef8b0cb0f1e855b2",
    "proof_commit": "ff57005b975c4917341306bd0eceb6d05a9b18f6",
    "proof_file": "tracks/nova3-analytic-density/proofs/PRODUCT_MODEL_THEOREMS.md",
    "request": "D",
    "object": "N3-ANA-007",
}
N_VALUES = tuple(range(3, 13))
Q_MIN = 1_000
Q_MAX = 2_000_000
BLOCKS = (
    (1_000, 9_999),
    (10_000, 99_999),
    (100_000, 999_999),
    (1_000_000, 2_000_000),
)
TOP_K = 8
PRECISION = 80
OUTPUT_DIGITS = 60
ANCHOR_PRIME = 2


class RecurrenceEvidenceError(ValueError):
    pass


def _canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def semantic_sha(value: dict[str, Any]) -> str:
    payload = dict(value)
    payload.pop("sha256", None)
    return sha256(_canonical_bytes(payload)).hexdigest()


def _require_int(name: str, value: object, minimum: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise RecurrenceEvidenceError(f"{name} must be an integer at least {minimum}")
    return value


def primes_up_to(n: int) -> list[int]:
    n = _require_int("n", n, 0)
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    p = 2
    while p * p <= n:
        if sieve[p]:
            start = p * p
            sieve[start:n + 1:p] = b"\x00" * (((n - start) // p) + 1)
        p += 1
    return [i for i, flag in enumerate(sieve) if flag]


def valuation_factorial(n: int, p: int) -> int:
    n = _require_int("n", n, 0)
    p = _require_int("p", p, 2)
    total = 0
    q = n
    while q:
        q //= p
        total += q
    return total


def factorization(n: int) -> list[tuple[int, int]]:
    return [(p, valuation_factorial(n, p)) for p in primes_up_to(n)]


def _float_coordinate_factor(residual_cycles: float, exponent: int) -> float:
    x = math.pi * residual_cycles
    if abs(x) < 1e-12:
        return 1.0
    denominator = (exponent + 1) * math.sin(x)
    if denominator == 0.0:
        return 1.0
    value = abs(math.sin((exponent + 1) * x) / denominator)
    return min(1.0, value)


def _validate_search_config(n_values: Iterable[int], q_min: int, q_max: int, blocks: Iterable[tuple[int, int]], top_k: int) -> tuple[tuple[int, ...], tuple[tuple[int, int], ...]]:
    ns = tuple(n_values)
    bs = tuple(tuple(pair) for pair in blocks)
    if ns != tuple(sorted(set(ns))) or any(n < 3 for n in ns):
        raise RecurrenceEvidenceError("n_values must be strictly increasing integers at least 3")
    q_min = _require_int("q_min", q_min, 1)
    q_max = _require_int("q_max", q_max, q_min)
    _require_int("top_k", top_k, 1)
    if not bs or bs[0][0] != q_min or bs[-1][1] != q_max:
        raise RecurrenceEvidenceError("blocks must cover the full q range")
    expected = q_min
    for lo, hi in bs:
        if lo != expected or hi < lo:
            raise RecurrenceEvidenceError("blocks must be ordered, contiguous, and nonempty")
        expected = hi + 1
    return ns, bs


def _atan_decimal_inverse(inverse: int, precision: int) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = precision + 12
        x = Decimal(1) / Decimal(inverse)
        x2 = x * x
        term = x
        total = term
        k = 1
        threshold = Decimal(10) ** Decimal(-(precision + 6))
        while True:
            term *= -x2
            add = term / Decimal(2 * k + 1)
            total += add
            if abs(add) < threshold:
                break
            k += 1
        return +total


def decimal_pi(precision: int = PRECISION) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = precision + 8
        value = Decimal(16) * _atan_decimal_inverse(5, precision + 4) - Decimal(4) * _atan_decimal_inverse(239, precision + 4)
        ctx.prec = precision
        return +value


def decimal_sin(x: Decimal, precision: int = PRECISION) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = precision + 12
        term = x
        total = term
        k = 1
        x2 = x * x
        threshold = Decimal(10) ** Decimal(-(precision + 6))
        while True:
            term *= -x2 / Decimal((2 * k) * (2 * k + 1))
            total += term
            if abs(term) < threshold:
                break
            k += 1
        ctx.prec = precision
        return +total


def _fmt_decimal(value: Decimal) -> str:
    if value == 0:
        return "0E+0"
    return format(value, f".{OUTPUT_DIGITS}E")


def _direct_divisor_vector_average(n: int, residuals: dict[int, Decimal]) -> float:
    factors = factorization(n)
    ranges = [range(b + 1) for _, b in factors]
    total = 0j
    count = 0
    for vector in product(*ranges):
        phase = 0.0
        for (p, _), exponent in zip(factors, vector):
            phase += exponent * (2.0 * math.pi * float(residuals[p]))
        total += cmath.exp(1j * phase)
        count += 1
    return abs(total / count)


def _decimal_candidate(n: int, q: int, precision: int = PRECISION) -> dict[str, Any]:
    n = _require_int("n", n, 3)
    q = _require_int("q", q, 1)
    factors = factorization(n)
    with localcontext() as ctx:
        ctx.prec = precision + 16
        pi = decimal_pi(precision + 12)
        ln2 = Decimal(2).ln()
        residuals: dict[str, str] = {}
        coordinate_factors: dict[str, str] = {}
        residual_values: dict[int, Decimal] = {}
        phi = Decimal(1)
        max_residual = Decimal(0)
        max_scaled = Decimal(0)
        for p, b in factors:
            if p == ANCHOR_PRIME:
                residual = Decimal(0)
                coordinate = Decimal(1)
            else:
                alpha = Decimal(p).ln() / ln2
                phase_cycles = Decimal(q) * alpha
                nearest = phase_cycles.to_integral_value(rounding=ROUND_HALF_EVEN)
                residual = phase_cycles - nearest
                x = pi * residual
                coordinate = Decimal(1) if residual == 0 else abs(decimal_sin(Decimal(b + 1) * x, precision + 8) / (Decimal(b + 1) * decimal_sin(x, precision + 8)))
                phi *= coordinate
            residual_values[p] = residual
            residuals[str(p)] = _fmt_decimal(residual)
            coordinate_factors[str(p)] = _fmt_decimal(coordinate)
            max_residual = max(max_residual, abs(residual))
            max_scaled = max(max_scaled, Decimal(b + 1) * abs(residual))
        t = Decimal(2) * pi * Decimal(q) / ln2
        direct = _direct_divisor_vector_average(n, residual_values)
        direct_decimal = Decimal(str(direct))
        error = abs(phi - direct_decimal)
        ctx.prec = precision
        return {
            "n": n, "q": q, "t": _fmt_decimal(+t), "phi_abs": _fmt_decimal(+phi),
            "direct_divisor_vector_phi_abs": _fmt_decimal(+direct_decimal),
            "crosscheck_abs_error": _fmt_decimal(+error),
            "max_phase_residual_cycles": _fmt_decimal(+max_residual),
            "max_scaled_residual": _fmt_decimal(+max_scaled),
            "phase_residual_cycles": residuals,
            "coordinate_factor_abs": coordinate_factors,
            "divisor_vector_count": math.prod(b + 1 for _, b in factors),
            "decimal_precision": precision,
        }


def _scan_float(ns: tuple[int, ...], q_min: int, q_max: int, blocks: tuple[tuple[int, int], ...], top_k: int) -> dict[tuple[int, int], list[tuple[float, int]]]:
    all_primes = primes_up_to(max(ns))
    non_anchor_primes = [p for p in all_primes if p != ANCHOR_PRIME]
    alphas = {p: math.log(p) / math.log(ANCHOR_PRIME) for p in non_anchor_primes}
    valuations = {n: {p: valuation_factorial(n, p) for p in all_primes if p <= n} for n in ns}
    factor_keys = sorted({(p, b) for n in ns for p, b in valuations[n].items() if p != ANCHOR_PRIME})
    heaps: dict[tuple[int, int], list[tuple[float, int]]] = {(n, j): [] for n in ns for j in range(len(blocks))}
    block_index = 0
    for q in range(q_min, q_max + 1):
        while block_index + 1 < len(blocks) and q > blocks[block_index][1]:
            block_index += 1
        residuals = {p: q * alphas[p] - round(q * alphas[p]) for p in non_anchor_primes}
        coordinate = {(p, b): _float_coordinate_factor(residuals[p], b) for p, b in factor_keys}
        for n in ns:
            score = 1.0
            for p, b in valuations[n].items():
                if p != ANCHOR_PRIME:
                    score *= coordinate[(p, b)]
            heap = heaps[(n, block_index)]
            item = (score, -q)
            if len(heap) < top_k:
                heappush(heap, item)
            elif item > heap[0]:
                heapreplace(heap, item)
    return {key: sorted(((score, -neg_q) for score, neg_q in heap), key=lambda item: (-item[0], item[1])) for key, heap in heaps.items()}


def build_evidence(n_values: Iterable[int] = N_VALUES, *, q_min: int = Q_MIN, q_max: int = Q_MAX, blocks: Iterable[tuple[int, int]] = BLOCKS, top_k: int = TOP_K, precision: int = PRECISION) -> dict[str, Any]:
    ns, bs = _validate_search_config(n_values, q_min, q_max, blocks, top_k)
    heaps = _scan_float(ns, q_min, q_max, bs, top_k)
    block_rows = []
    best_rows = []
    for n in ns:
        n_block_rows = []
        for block_index, (lo, hi) in enumerate(bs):
            finalists = []
            for scan_score, q in heaps[(n, block_index)]:
                candidate = _decimal_candidate(n, q, precision)
                candidate["scan_phi_abs_binary64"] = format(scan_score, ".17g")
                finalists.append(candidate)
            if not finalists:
                raise RecurrenceEvidenceError("empty finalist set")
            finalists.sort(key=lambda row: (-Decimal(row["phi_abs"]), row["q"]))
            winner = dict(finalists[0])
            winner.update({"block_index": block_index, "q_block": [lo, hi], "retained_finalist_count": len(finalists)})
            block_rows.append(winner)
            n_block_rows.append(winner)
        n_block_rows.sort(key=lambda row: (-Decimal(row["phi_abs"]), row["q"]))
        best = dict(n_block_rows[0])
        best["selected_from_block_index"] = best["block_index"]
        best_rows.append(best)
    with localcontext() as ctx:
        ctx.prec = precision + 12
        pi = decimal_pi(precision + 8)
        ln2 = Decimal(2).ln()
        t_min = Decimal(2) * pi * Decimal(q_min) / ln2
        t_max = Decimal(2) * pi * Decimal(q_max) / ln2
    evidence = {
        "schema": SCHEMA,
        "result_class": "computational evidence",
        "source": SOURCE,
        "search": {
            "n_values": list(ns), "anchor_prime": ANCHOR_PRIME,
            "frequency_parameterization": "t_q = 2*pi*q/log(2)",
            "q_min": q_min, "q_max": q_max, "q_count": q_max - q_min + 1,
            "t_min": _fmt_decimal(t_min), "t_max": _fmt_decimal(t_max),
            "blocks": [list(pair) for pair in bs],
            "top_k_binary64_finalists_per_n_per_block": top_k,
            "scan_precision": "IEEE 754 binary64",
            "finalist_precision_decimal_digits": precision,
            "direct_crosscheck": "exact exponent-vector enumeration with complex binary64 phase evaluation",
        },
        "block_rows": block_rows,
        "best_rows": best_rows,
        "totals": {
            "n_count": len(ns), "block_count": len(bs), "block_winner_count": len(block_rows),
            "grid_points_per_n": q_max - q_min + 1,
            "total_n_q_scores": len(ns) * (q_max - q_min + 1),
        },
        "assessment": {
            "request_D": "ACCEPTED_AS_COMPUTATIONAL_EVIDENCE",
            "N3-ANA-007": "EVIDENCE_CONSISTENT_WITH_UNBOUNDED_RECURRENCE; FORMAL_PROOF_AUDIT_RECORDED_SEPARATELY",
        },
        "scope": "The bounded scan does not prove limsup |phi_n(t)|=1 and does not certify a global maximum outside the declared grid.",
    }
    evidence["sha256"] = semantic_sha(evidence)
    return evidence


def candidate_certificate(evidence: dict[str, Any], n: int = 12) -> dict[str, Any]:
    rows = [row for row in evidence.get("best_rows", []) if row.get("n") == n]
    if len(rows) != 1:
        raise RecurrenceEvidenceError(f"expected one best row for n={n}")
    certificate = {"schema": CANDIDATE_SCHEMA, "result_class": "computational evidence", "source": SOURCE, "evidence_sha256": evidence.get("sha256"), "candidate": rows[0]}
    certificate["sha256"] = semantic_sha(certificate)
    return certificate


def verify_candidate(certificate: dict[str, Any]) -> dict[str, Any]:
    if certificate.get("schema") != CANDIDATE_SCHEMA:
        raise RecurrenceEvidenceError("wrong candidate schema")
    if certificate.get("source") != SOURCE:
        raise RecurrenceEvidenceError("wrong frozen source metadata")
    if certificate.get("sha256") != semantic_sha(certificate):
        raise RecurrenceEvidenceError("candidate semantic checksum mismatch")
    candidate = certificate.get("candidate")
    if not isinstance(candidate, dict):
        raise RecurrenceEvidenceError("missing candidate")
    expected = _decimal_candidate(candidate["n"], candidate["q"], candidate.get("decimal_precision", PRECISION))
    for key, value in expected.items():
        if candidate.get(key) != value:
            raise RecurrenceEvidenceError(f"candidate field differs from recomputation: {key}")
    phi = Decimal(candidate["phi_abs"])
    if not (Decimal(0) <= phi <= Decimal(1)):
        raise RecurrenceEvidenceError("candidate modulus outside [0,1]")
    return {"status": "PASS", "n": candidate["n"], "q": candidate["q"], "phi_abs": candidate["phi_abs"]}


def verify_evidence(evidence: dict[str, Any]) -> dict[str, Any]:
    if evidence.get("schema") != SCHEMA:
        raise RecurrenceEvidenceError("wrong evidence schema")
    if evidence.get("source") != SOURCE:
        raise RecurrenceEvidenceError("wrong frozen source metadata")
    if evidence.get("sha256") != semantic_sha(evidence):
        raise RecurrenceEvidenceError("evidence semantic checksum mismatch")
    config = evidence.get("search")
    if not isinstance(config, dict):
        raise RecurrenceEvidenceError("missing search configuration")
    expected = build_evidence(config["n_values"], q_min=config["q_min"], q_max=config["q_max"], blocks=[tuple(pair) for pair in config["blocks"]], top_k=config["top_k_binary64_finalists_per_n_per_block"], precision=config["finalist_precision_decimal_digits"])
    if _canonical_bytes(expected) != _canonical_bytes(evidence):
        raise RecurrenceEvidenceError("evidence differs from independent recomputation")
    return {"status": "PASS", "sha256": evidence["sha256"], "n_count": evidence["totals"]["n_count"], "q_count": evidence["search"]["q_count"], "block_winner_count": evidence["totals"]["block_winner_count"]}


def write_json(value: dict[str, Any], path: str | Path) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(value, sort_keys=True, indent=2) + "\n", encoding="utf-8")


def write_csv(rows: list[dict[str, Any]], path: str | Path) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    fields = ["n", "block_index", "q_block", "q", "t", "phi_abs", "direct_divisor_vector_phi_abs", "crosscheck_abs_error", "max_phase_residual_cycles", "max_scaled_residual", "divisor_vector_count", "scan_phi_abs_binary64"]
    with target.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: json.dumps(row[key]) if isinstance(row.get(key), list) else row.get(key) for key in fields})
