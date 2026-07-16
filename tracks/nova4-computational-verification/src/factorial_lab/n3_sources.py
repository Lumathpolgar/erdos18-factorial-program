"""Independent compatibility audit for restricted Nova 3 external sources.

This module does not attempt to reprove the cited analytic number theory papers.
It freezes their exact scope as reconstructed from the primary sources, then
checks whether the scope legally transfers to deterministic divisor questions
for the single sequence n!.
"""
from __future__ import annotations

from hashlib import sha256
import json
from math import factorial
from pathlib import Path
from typing import Any

SCHEMA = "nova4.n3-restricted-source-audit.v1"
CLAIM_SCHEMA = "nova4.n3-source-compatibility-claim.v1"
SOURCE = {
    "repository": "Lumathpolgar/erdos18-factorial-program",
    "branch": "nova/analytic-density",
    "handoff": "N3-HO-N4-002",
    "handoff_commit": "7469dada02fa4caca08ed391ef8b0cb0f1e855b2",
    "source_ledger_commit": "697e7ed8bdb03f54b2389b2fcdd8b685dadcebc4",
    "request": "E",
}


class SourceAuditError(ValueError):
    pass


def _canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def semantic_sha(value: dict[str, Any]) -> str:
    payload = dict(value)
    payload.pop("sha256", None)
    return sha256(_canonical_bytes(payload)).hexdigest()


def divisors(n: int) -> list[int]:
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise SourceAuditError("n must be a positive integer")
    small: list[int] = []
    large: list[int] = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            small.append(d)
            if d * d != n:
                large.append(n // d)
        d += 1
    return small + list(reversed(large))


def tau_interval(n: int, y: int, z: int) -> int:
    if not (0 < y < z):
        raise SourceAuditError("require 0 < y < z")
    return sum(1 for d in divisors(n) if y < d <= z)


def H(x: int, y: int, z: int) -> int:
    if x < 1:
        raise SourceAuditError("x must be positive")
    return sum(1 for m in range(1, x + 1) if tau_interval(m, y, z) > 0)


def prime_factors(n: int) -> list[int]:
    factors: list[int] = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            factors.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        factors.append(n)
    return factors


def valuation_factorial(n: int, p: int) -> int:
    if n < 0 or p < 2:
        raise SourceAuditError("invalid valuation arguments")
    total = 0
    while n:
        n //= p
        total += n
    return total


def is_y_friable(value: int, y: int) -> bool:
    return all(p <= y for p in prime_factors(value))


def expected_source_records() -> list[dict[str, Any]]:
    return [
        {
            "id": "N3-SRC-004",
            "authors": ["Kevin Ford"],
            "title": "The distribution of integers with a divisor in a given interval",
            "primary_source": "arXiv:math/0401223v5; Annals of Mathematics 168 (2008), 367-433",
            "source_object": "H(x,y,z)=#{m<=x: tau(m;y,z)>0}",
            "quantifier_scope": "ambient count over all positive integers m<=x",
            "factorial_sequence_selected": False,
            "direct_factorial_use": "REJECTED",
            "legal_use": "background comparison and warning against average-to-pointwise transfer",
            "reason_code": "AMBIENT_COUNT_NOT_FIXED_INTEGER",
        },
        {
            "id": "N3-SRC-005",
            "authors": ["Sary Drappeau", "Gerald Tenenbaum"],
            "title": "Lois de repartition des diviseurs des entiers friables",
            "primary_source": "arXiv:1604.04204v1",
            "source_object": "Gaussian divisor law for all but a quantified exceptional subset of S(x,y)",
            "quantifier_scope": "almost all y-friable integers in S(x,y), with an explicit exceptional set",
            "factorial_sequence_selected": False,
            "direct_factorial_use": "REJECTED",
            "legal_use": "methodological compatibility with independent exponent coordinates only",
            "reason_code": "EXCEPTIONAL_SET_DOES_NOT_CERTIFY_FIXED_SEQUENCE",
        },
        {
            "id": "N3-SRC-006",
            "authors": ["Cecile Dartyge", "David Feutrie", "Gerald Tenenbaum"],
            "title": "Entiers ultrafriables en progressions arithmetiques",
            "primary_source": "arXiv:2001.04435v1",
            "source_object": "U(x,y), integers m<=x with every occurring prime power <=y",
            "quantifier_scope": "arithmetic-progression distribution in the common-cap ultrafriable set U(x,y)",
            "factorial_sequence_selected": False,
            "direct_factorial_use": "REJECTED",
            "legal_use": "source-scope comparison only; no lower-bound transfer to exact factorial divisors",
            "reason_code": "COMMON_PRIME_POWER_CAP_DIFFERS_FROM_FACTORIAL_VALUATIONS",
        },
    ]


def ford_witness() -> dict[str, Any]:
    n = 5
    N = factorial(n)
    y, z = 6, 7
    aggregate = H(N, y, z)
    local = tau_interval(N, y, z)
    if aggregate != 17 or local != 0:
        raise SourceAuditError("Ford witness recomputation failed")
    return {
        "n": n,
        "factorial": N,
        "interval": [y, z],
        "H_factorial_y_z": aggregate,
        "tau_factorial_y_z": local,
        "explanation": "The ambient count is positive while the fixed factorial has no divisor in the interval.",
    }


def drappeau_tenenbaum_witness() -> dict[str, Any]:
    n = 10
    N = factorial(n)
    friable = is_y_friable(N, n)
    if not friable:
        raise SourceAuditError("factorial should be n-friable")
    return {
        "n": n,
        "factorial": N,
        "x": N,
        "y": n,
        "factorial_is_in_S_x_y": True,
        "source_nonexceptional_certificate_for_factorial": False,
        "explanation": "Membership in S(x,y) does not prove that this deterministic member lies outside the theorem's exceptional subset.",
    }


def ultrafriable_witness() -> dict[str, Any]:
    n = 10
    N = factorial(n)
    v2 = valuation_factorial(n, 2)
    required_power = 2**v2
    first_excluded_prime = 11
    if v2 != 8 or required_power != 256:
        raise SourceAuditError("unexpected n=10 factorial valuation")
    if N % required_power != 0 or N % first_excluded_prime == 0:
        raise SourceAuditError("ultrafriable witness legality failed")
    return {
        "n": n,
        "factorial": N,
        "v_2_factorial": v2,
        "required_prime_power": required_power,
        "prime_not_dividing_factorial": first_excluded_prime,
        "case_y_below_required_power": "2^8 is excluded from U(10!,y)",
        "case_y_at_least_required_power": "11 is included in U(10!,y) although 11 does not divide 10!",
        "common_y_exact_support_possible": False,
        "explanation": "No common ultrafriability parameter y makes U(10!,y) equal the divisor set of 10!.",
    }


def build_audit() -> dict[str, Any]:
    audit = {
        "schema": SCHEMA,
        "result_class": "source compatibility audit",
        "source": SOURCE,
        "sources": expected_source_records(),
        "witnesses": {
            "ford_ambient_vs_fixed": ford_witness(),
            "drappeau_tenenbaum_exceptional_scope": drappeau_tenenbaum_witness(),
            "ultrafriable_common_cap_mismatch": ultrafriable_witness(),
        },
        "decisions": {
            "request_E": "ACCEPTED",
            "N3-SRC-004": "SOURCE_SCOPE_CONFIRMED_DIRECT_FACTORIAL_USE_REJECTED",
            "N3-SRC-005": "SOURCE_SCOPE_CONFIRMED_METHOD_ONLY",
            "N3-SRC-006": "SOURCE_SCOPE_CONFIRMED_DIRECT_FACTORIAL_USE_REJECTED",
            "any_source_directly_selects_factorial_sequence": False,
        },
        "scope": "This audit classifies source compatibility. It does not reprove the cited papers or establish a factorial divisor-density theorem.",
    }
    audit["sha256"] = semantic_sha(audit)
    return audit


def verify_audit(audit: dict[str, Any]) -> dict[str, Any]:
    if audit.get("schema") != SCHEMA:
        raise SourceAuditError("wrong audit schema")
    if audit.get("source") != SOURCE:
        raise SourceAuditError("wrong frozen source metadata")
    if audit.get("sha256") != semantic_sha(audit):
        raise SourceAuditError("semantic checksum mismatch")
    expected = build_audit()
    if _canonical_bytes(expected) != _canonical_bytes(audit):
        raise SourceAuditError("audit differs from independent recomputation")
    return {
        "status": "PASS",
        "sha256": audit["sha256"],
        "source_count": len(audit["sources"]),
        "direct_factorial_sources": sum(1 for row in audit["sources"] if row["factorial_sequence_selected"]),
    }


def compatibility_claim(audit: dict[str, Any]) -> dict[str, Any]:
    claim = {
        "schema": CLAIM_SCHEMA,
        "result_class": "source compatibility certificate",
        "source": SOURCE,
        "claim": {
            "any_source_directly_selects_factorial_sequence": False,
            "source_ids": [row["id"] for row in audit["sources"]],
            "ultrafriable_witness": audit["witnesses"]["ultrafriable_common_cap_mismatch"],
        },
        "evidence_sha256": audit["sha256"],
    }
    claim["sha256"] = semantic_sha(claim)
    return claim


def verify_claim(claim: dict[str, Any]) -> dict[str, Any]:
    if claim.get("schema") != CLAIM_SCHEMA:
        raise SourceAuditError("wrong claim schema")
    if claim.get("source") != SOURCE:
        raise SourceAuditError("wrong claim source")
    if claim.get("sha256") != semantic_sha(claim):
        raise SourceAuditError("claim checksum mismatch")
    expected_audit = build_audit()
    expected = compatibility_claim(expected_audit)
    if _canonical_bytes(expected) != _canonical_bytes(claim):
        raise SourceAuditError("claim differs from independent recomputation")
    return {
        "status": "PASS",
        "sha256": claim["sha256"],
        "evidence_sha256": claim["evidence_sha256"],
    }


def write_json(value: dict[str, Any], path: str | Path) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(value, sort_keys=True, indent=2) + "\n", encoding="utf-8")
