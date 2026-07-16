"""Independent verification of Dusart Theorem 6.9 usage in N3-ANA-010.

This module intentionally reconstructs only the explicit prime-counting input and
its algebraic transfer to the upper-half prime interval. It does not import the
Nova 3 proof implementation.
"""

from __future__ import annotations

from decimal import Decimal, localcontext
from fractions import Fraction
import hashlib
import json
from math import isqrt
from pathlib import Path
from typing import Any, Iterable

REPOSITORY = "Lumathpolgar/erdos18-factorial-program"
SOURCE_BRANCH = "nova/analytic-density"
HANDOFF = "N3-HO-N4-002"
HANDOFF_COMMIT = "7469dada02fa4caca08ed391ef8b0cb0f1e855b2"
SOURCE_LEDGER_COMMIT = "697e7ed8bdb03f54b2389b2fcdd8b685dadcebc4"
PROOF_FILE = "tracks/nova3-analytic-density/proofs/EXPLICIT_PRIME_INTERVAL_AND_CAPACITY.md"
PROOF_FILE_BLOB_SHA = "e36daf98db86da16bd5ed8c6c82f43530d745f66"
OBJECT_ID = "N3-ANA-010"
REQUEST_ID = "F"

ARXIV_ID = "1002.0442"
ARXIV_VERSION = "v1"
PRIMARY_TITLE = "Estimates of Some Functions Over Primes without R.H."
PRIMARY_AUTHOR = "Pierre Dusart"
PRIMARY_THEOREM = "Theorem 6.9"
PRIMARY_EQUATION = "(6.6)"
PRIMARY_PDF_PAGE = 9
LOWER_SOURCE_THRESHOLD = 5_393
UPPER_SOURCE_THRESHOLD = 60_184
DERIVED_INTEGER_THRESHOLD = 120_368
DECIMAL_PRECISION = 80

SCHEMA = "nova4.n3-dusart-source-audit.v1"
CLAIM_SCHEMA = "nova4.n3-dusart-prime-interval-claim.v1"


class VerificationError(ValueError):
    """Raised when a replayed artifact fails semantic verification."""


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def semantic_sha256(value: Any, *, omit: Iterable[str] = ("sha256",)) -> str:
    omitted = set(omit)
    if isinstance(value, dict):
        payload = {k: v for k, v in value.items() if k not in omitted}
    else:
        payload = value
    return hashlib.sha256(canonical_json(payload).encode("utf-8")).hexdigest()


def _fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def exp_lower_at_seven_tenths() -> Fraction:
    """Four-term positive Taylor lower bound for exp(7/10)."""
    x = Fraction(7, 10)
    return Fraction(1) + x + x * x / 2 + x * x * x / 6


def e_upper_bound() -> Fraction:
    """Elementary rational upper bound e < 11/4.

    For k>=3, k! >= 2*3^(k-2), so the tail is at most 1/4.
    """
    return Fraction(11, 4)


def polynomial_lower_at_four() -> Fraction:
    """Value at L=4 of L^2 - (11/5)L - 18/5."""
    L = Fraction(4)
    return L * L - Fraction(11, 5) * L - Fraction(18, 5)


def algebra_certificate() -> dict[str, Any]:
    exp_lower = exp_lower_at_seven_tenths()
    e_upper = e_upper_bound()
    q_lower = polynomial_lower_at_four()
    if exp_lower <= 2:
        raise AssertionError("Taylor lower bound does not prove log(2)<7/10")
    if e_upper >= 3:
        raise AssertionError("e upper bound does not prove e<3")
    if q_lower <= 0:
        raise AssertionError("polynomial lower bound is not positive")
    return {
        "ln2_upper": "7/10",
        "ln2_proof": {
            "exp_7_over_10_taylor_lower": _fraction_text(exp_lower),
            "greater_than_two": True,
        },
        "b_definition": "log(2)+11/10",
        "b_upper": "9/5",
        "e_upper": _fraction_text(e_upper),
        "threshold_exceeds_e4": {
            "e4_upper": "81",
            "threshold": DERIVED_INTEGER_THRESHOLD,
            "threshold_greater_than_81": DERIVED_INTEGER_THRESHOLD > 81,
            "conclusion": "L=log(n)>4 for n>=120368",
        },
        "normalized_difference": (
            "1/(L-1)-1/(2*(L-b))-1/(3*L)"
            " = Q(L)/(6*L*(L-1)*(L-b))"
        ),
        "Q": "L^2+(5-4*b)*L-2*b",
        "Q_lower": "L^2-(11/5)*L-18/5",
        "Q_lower_derivative": "2*L-11/5",
        "Q_lower_increasing_for_L_at_least_4": True,
        "Q_lower_at_4": _fraction_text(q_lower),
        "all_denominators_positive": True,
        "conclusion": "source lower bound minus source upper bound is at least n/(3*log(n))",
    }


def source_threshold_record() -> dict[str, Any]:
    threshold = max(LOWER_SOURCE_THRESHOLD, 2 * UPPER_SOURCE_THRESHOLD)
    if threshold != DERIVED_INTEGER_THRESHOLD:
        raise AssertionError("unexpected source-derived threshold")
    return {
        "lower_bound": {
            "statement": "pi(x)>=x/(log(x)-1)",
            "threshold": LOWER_SOURCE_THRESHOLD,
            "applied_at": "x=n",
        },
        "upper_bound": {
            "statement": "pi(x)<=x/(log(x)-1.1)",
            "threshold": UPPER_SOURCE_THRESHOLD,
            "applied_at": "x=n/2",
        },
        "derived_integer_threshold": threshold,
        "threshold_reason": "n/2>=60184 and n>=5393",
        "predecessor": {
            "n": threshold - 1,
            "n_over_2": "120367/2",
            "n_over_2_decimal": "60183.5",
            "upper_source_hypothesis_holds": False,
        },
        "minimal_from_unsupplemented_source_hypotheses": True,
        "not_claimed_global_minimum": True,
    }


def primes_up_to(limit: int) -> list[int]:
    if not isinstance(limit, int) or isinstance(limit, bool) or limit < 0:
        raise ValueError("limit must be a nonnegative integer")
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return [i for i, flag in enumerate(sieve) if flag]


def prime_count_table(limit: int) -> list[int]:
    primes = set(primes_up_to(limit))
    table = [0] * (limit + 1)
    count = 0
    for value in range(limit + 1):
        if value in primes:
            count += 1
        table[value] = count
    return table


def decimal_threshold_witness(n: int = DERIVED_INTEGER_THRESHOLD) -> dict[str, Any]:
    if n < 2:
        raise ValueError("n must be at least 2")
    table = prime_count_table(n)
    half_floor = n // 2
    pi_n = table[n]
    pi_half = table[half_floor]
    exact_count = pi_n - pi_half
    with localcontext() as ctx:
        ctx.prec = DECIMAL_PRECISION
        dn = Decimal(n)
        L = dn.ln()
        ln2 = Decimal(2).ln()
        b = ln2 + Decimal(11) / Decimal(10)
        source_lower = dn * (
            Decimal(1) / (L - Decimal(1))
            - Decimal(1) / (Decimal(2) * (L - b))
        )
        target = dn / (Decimal(3) * L)
        q_value = L * L + (Decimal(5) - Decimal(4) * b) * L - Decimal(2) * b
        return {
            "n": n,
            "floor_n_over_2": half_floor,
            "pi_n": pi_n,
            "pi_floor_n_over_2": pi_half,
            "exact_upper_half_prime_count": exact_count,
            "log_n": str(+L),
            "b": str(+b),
            "source_derived_lower_bound": str(+source_lower),
            "target_n_over_3logn": str(+target),
            "source_margin_over_target": str(+(source_lower - target)),
            "exact_margin_over_target": str(+(Decimal(exact_count) - target)),
            "Q_at_log_n": str(+q_value),
            "source_hypotheses_hold": n >= LOWER_SOURCE_THRESHOLD
            and Decimal(n) / Decimal(2) >= Decimal(UPPER_SOURCE_THRESHOLD),
            "endpoint_identity": "pi(n/2)=pi(floor(n/2)) for integer n",
        }


def source_metadata() -> dict[str, Any]:
    return {
        "repository": REPOSITORY,
        "branch": SOURCE_BRANCH,
        "handoff": HANDOFF,
        "handoff_commit": HANDOFF_COMMIT,
        "source_ledger_commit": SOURCE_LEDGER_COMMIT,
        "proof_file": PROOF_FILE,
        "proof_file_blob_sha": PROOF_FILE_BLOB_SHA,
        "request": REQUEST_ID,
        "object": OBJECT_ID,
        "primary_source": {
            "author": PRIMARY_AUTHOR,
            "title": PRIMARY_TITLE,
            "arxiv_id": ARXIV_ID,
            "version": ARXIV_VERSION,
            "theorem": PRIMARY_THEOREM,
            "equation": PRIMARY_EQUATION,
            "pdf_page": PRIMARY_PDF_PAGE,
        },
    }


def build_audit() -> dict[str, Any]:
    audit: dict[str, Any] = {
        "schema": SCHEMA,
        "result_class": "primary-source theorem audit",
        "source": source_metadata(),
        "decision": {
            "request_F": "ACCEPTED",
            "N3_ANA_010": "ACCEPTED",
            "source_thresholds_confirmed": True,
            "algebra_confirmed": True,
        },
        "source_thresholds": source_threshold_record(),
        "algebra": algebra_certificate(),
        "finite_threshold_witness": decimal_threshold_witness(),
        "scope": {
            "theorem_statement": "pi(n)-pi(n/2)>=n/(3*log(n)) for every integer n>=120368",
            "threshold_is_source_coverage_threshold_without_finite_supplement": True,
            "not_a_claim_of_smallest_possible_theorem_threshold": True,
            "not_additive_occupancy": True,
        },
    }
    audit["sha256"] = semantic_sha256(audit)
    return audit


def build_claim(audit: dict[str, Any] | None = None) -> dict[str, Any]:
    audit = build_audit() if audit is None else audit
    claim: dict[str, Any] = {
        "schema": CLAIM_SCHEMA,
        "result_class": "prime interval theorem certificate",
        "source": source_metadata(),
        "evidence_sha256": audit["sha256"],
        "claim": {
            "object": OBJECT_ID,
            "decision": "ACCEPTED",
            "integer_threshold": DERIVED_INTEGER_THRESHOLD,
            "inequality": "pi(n)-pi(n/2)>=n/(3*log(n))",
            "source_lower_threshold": LOWER_SOURCE_THRESHOLD,
            "source_upper_threshold": UPPER_SOURCE_THRESHOLD,
            "upper_source_argument_at_threshold": UPPER_SOURCE_THRESHOLD,
            "predecessor_covered_without_supplement": False,
            "algebra_Q_lower_at_4": _fraction_text(polynomial_lower_at_four()),
            "finite_threshold_prime_count": audit["finite_threshold_witness"][
                "exact_upper_half_prime_count"
            ],
        },
    }
    claim["sha256"] = semantic_sha256(claim)
    return claim


def _require_equal(actual: Any, expected: Any, label: str) -> None:
    if actual != expected:
        raise VerificationError(f"{label} mismatch: {actual!r} != {expected!r}")


def verify_audit(audit: dict[str, Any]) -> None:
    _require_equal(audit.get("schema"), SCHEMA, "schema")
    _require_equal(audit.get("source"), source_metadata(), "source metadata")
    claimed_hash = audit.get("sha256")
    _require_equal(claimed_hash, semantic_sha256(audit), "semantic sha256")
    expected = build_audit()
    _require_equal(audit, expected, "full semantic audit")


def verify_claim(claim: dict[str, Any], audit: dict[str, Any] | None = None) -> None:
    _require_equal(claim.get("schema"), CLAIM_SCHEMA, "claim schema")
    _require_equal(claim.get("source"), source_metadata(), "claim source metadata")
    _require_equal(claim.get("sha256"), semantic_sha256(claim), "claim semantic sha256")
    audit = build_audit() if audit is None else audit
    verify_audit(audit)
    expected = build_claim(audit)
    _require_equal(claim, expected, "full semantic claim")


def load_json(path: str | Path) -> dict[str, Any]:
    value = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise VerificationError("JSON root must be an object")
    return value


def dump_json(path: str | Path, value: dict[str, Any]) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")
