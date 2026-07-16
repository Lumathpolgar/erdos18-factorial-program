"""Independent theorem audit for Nova 3 object N3-ANA-006.

Reconstructs the normalized variance limit, infinite-product weak limit, and
non-Gaussian characteristic-function zero. Finite tables are diagnostics only.
"""
from __future__ import annotations

import copy
import hashlib
import json
import math
from pathlib import Path
from typing import Any, Iterable

REPOSITORY = "Lumathpolgar/erdos18-factorial-program"
SOURCE_BRANCH = "nova/analytic-density"
HANDOFF = "N3-HO-N4-002"
HANDOFF_COMMIT = "7469dada02fa4caca08ed391ef8b0cb0f1e855b2"
PROOF_FILE = "tracks/nova3-analytic-density/proofs/PRODUCT_MODEL_THEOREMS.md"
PROOF_FILE_BLOB_SHA = "6260f8db0b377cf7dbc1850cbe25c91243099e10"
SOURCE_LEDGER_FILE = "tracks/nova3-analytic-density/SOURCE_LEDGER.md"
SOURCE_LEDGER_BLOB_SHA = "da81e6aaf2674fdae036d72df002547d4a71b18a"
OBJECT_ID = "N3-ANA-006"
AUDIT_STAGE = "POST_H_THEOREM_CLOSURE"
SCHEMA = "nova4.n3-variance-limit-audit.v1"
CLAIM_SCHEMA = "nova4.n3-variance-limit-claim.v1"
FINITE_NS = (50, 100, 200, 500, 1_000, 2_000, 5_000, 10_000, 100_000, 1_000_000)
SERIES_CUTOFF = 1_000_000


class VerificationError(ValueError):
    """Raised when a replayed artifact fails semantic verification."""


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def semantic_sha256(value: Any, *, omit: Iterable[str] = ("sha256",)) -> str:
    omitted = set(omit)
    payload = (
        {key: item for key, item in value.items() if key not in omitted}
        if isinstance(value, dict)
        else value
    )
    return hashlib.sha256(canonical_json(payload).encode("utf-8")).hexdigest()


def source_metadata() -> dict[str, Any]:
    return {
        "repository": REPOSITORY,
        "branch": SOURCE_BRANCH,
        "handoff": HANDOFF,
        "handoff_commit": HANDOFF_COMMIT,
        "audit_stage": AUDIT_STAGE,
        "object": OBJECT_ID,
        "proof_file": PROOF_FILE,
        "proof_file_blob_sha": PROOF_FILE_BLOB_SHA,
        "source_ledger_file": SOURCE_LEDGER_FILE,
        "source_ledger_blob_sha": SOURCE_LEDGER_BLOB_SHA,
        "external_dependency": "none beyond elementary convergence and unique factorization",
    }


def primes_up_to(limit: int) -> list[int]:
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 2:
        if limit in (0, 1):
            return []
        raise ValueError("limit must be an integer at least zero")
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return [value for value, flag in enumerate(sieve) if flag]


def valuation_factorial(n: int, p: int) -> int:
    if isinstance(n, bool) or not isinstance(n, int) or n < 0:
        raise ValueError("n must be a nonnegative integer")
    if isinstance(p, bool) or not isinstance(p, int) or p < 2:
        raise ValueError("p must be an integer at least two")
    total = 0
    quotient = n
    while quotient:
        quotient //= p
        total += quotient
    return total


def normalized_variance(n: int, primes: list[int] | None = None) -> float:
    if n < 2:
        raise ValueError("n must be at least two")
    ps = primes_up_to(n) if primes is None else primes
    terms = []
    for p in ps:
        if p > n:
            break
        b = valuation_factorial(n, p)
        terms.append(b * (b + 2) * math.log(p) ** 2 / (12.0 * n * n))
    return math.fsum(terms)


def limiting_variance_partial(cutoff: int, primes: list[int] | None = None) -> float:
    if cutoff < 2:
        raise ValueError("cutoff must be at least two")
    ps = primes_up_to(cutoff) if primes is None else primes
    return math.fsum(
        math.log(p) ** 2 / (12.0 * (p - 1) ** 2) for p in ps if p <= cutoff
    )


def rigorous_integer_tail_upper(cutoff: int) -> float:
    """Elementary upper bound for the limiting prime variance-series tail."""
    if cutoff < 8:
        raise ValueError("cutoff must be at least eight")
    logy = math.log(cutoff)
    return (logy * logy + 2.0 * logy + 2.0) / (3.0 * cutoff)


def finite_variance_table() -> list[dict[str, Any]]:
    all_primes = primes_up_to(max(FINITE_NS))
    return [
        {
            "n": n,
            "variance_over_n_squared": format(normalized_variance(n, all_primes), ".17g"),
        }
        for n in FINITE_NS
    ]


def proof_reconstruction() -> dict[str, Any]:
    return {
        "exact_starting_formula": (
            "Var(S_n)/n^2=(1/12) sum_{p<=n} "
            "[b_p(n)^2/n^2+2b_p(n)/n^2](log p)^2"
        ),
        "fixed_prime_limit": {
            "valuation_identity": "b_p(n)=sum_{k>=1} floor(n/p^k)",
            "limit": "b_p(n)/n -> sum_{k>=1} p^(-k)=1/(p-1)",
            "coordinate_limit": (
                "(A_p-b_p/2)/n converges to Uniform[-1/(2(p-1)),1/(2(p-1))]"
            ),
        },
        "tail_control": {
            "valuation_upper": "b_p(n)<=n/(p-1)",
            "normalized_tail_upper": (
                "(1/12)sum_{p>Y}(log p)^2/(p-1)^2 "
                "+ (1/(6n))sum_{Y<p<=n}(log p)^2/(p-1)"
            ),
            "finite_n_remainder_upper": (
                "log(n)^2*(1+log(n-1))/(6n), which tends to zero"
            ),
            "limiting_series_tail": (
                "for Y>=8, at most (log(Y)^2+2log(Y)+2)/(3Y)"
            ),
            "conclusion": (
                "limsup_n Var(X_n-X_n^{<=Y}) is bounded by the limiting variance tail"
            ),
        },
        "variance_asymptotic": {
            "statement": "Var(S_n)/n^2 -> (1/12)sum_p (log p)^2/(p-1)^2",
            "decision": "ACCEPTED",
        },
        "weak_limit": {
            "finite_truncations": "joint convergence follows from coordinate independence",
            "infinite_limit": (
                "sum_p (log p)U_p converges in L^2 because the variance series converges"
            ),
            "converging_together": True,
            "statement": "X_n converges weakly to sum_p (log p)U_p",
            "decision": "ACCEPTED",
        },
        "characteristic_function": {
            "factor": "sinc(t log(p)/(2(p-1)))",
            "product": (
                "product_p sin(t log(p)/(2(p-1)))/(t log(p)/(2(p-1)))"
            ),
            "compact_convergence_reason": (
                "sum_p (log p)^2/(p-1)^2 converges and 1-sinc(x)=O(x^2)"
            ),
        },
        "non_gaussian": {
            "zero_frequency": "2*pi/log(2)",
            "p_equals_2_argument": "pi",
            "p_equals_2_factor": "0",
            "limit_variance_positive": True,
            "gaussian_characteristic_function_nonzero": True,
            "decision": "ACCEPTED",
        },
        "scope": {
            "standard_gaussian_limit_for_full_model": False,
            "gaussian_local_limit_at_full_variance_scale": False,
            "does_not_rule_out_high_prime_tail_clt": True,
            "not_additive_occupancy": True,
            "not_factorial_half_range_theorem": True,
        },
    }


def build_audit() -> dict[str, Any]:
    primes = primes_up_to(SERIES_CUTOFF)
    partial = limiting_variance_partial(SERIES_CUTOFF, primes)
    tail_upper = rigorous_integer_tail_upper(SERIES_CUTOFF)
    audit: dict[str, Any] = {
        "schema": SCHEMA,
        "result_class": "proved theorem audit with finite diagnostics",
        "source": source_metadata(),
        "decision": {
            "N3_ANA_006": "ACCEPTED",
            "variance_asymptotic": "ACCEPTED",
            "full_model_weak_limit": "ACCEPTED",
            "non_gaussian_limit": "ACCEPTED",
            "finite_table_is_asymptotic_proof": False,
        },
        "proof_reconstruction": proof_reconstruction(),
        "limiting_variance_series": {
            "definition": "(1/12)sum_p (log p)^2/(p-1)^2",
            "positive": True,
            "convergent": True,
            "cutoff": SERIES_CUTOFF,
            "partial_sum": format(partial, ".17g"),
            "rigorous_tail_upper": format(tail_upper, ".17g"),
            "enclosure": [
                format(partial, ".17g"),
                format(partial + tail_upper, ".17g"),
            ],
        },
        "finite_diagnostics": {
            "classification": "computational evidence only",
            "rows": finite_variance_table(),
        },
        "scope": {
            "accepted": [
                "variance asymptotic",
                "full normalized weak limit",
                "L2 construction of the limiting series",
                "limiting characteristic-function product",
                "non-Gaussianity of the full-model limit",
            ],
            "not_proved": [
                "Gaussian local limit for the full model",
                "high-prime tail theorem N3-ANA-008",
                "coarse local lower bound N3-ANA-009",
                "additive occupancy",
                "factorial half-range theorem",
                "Erdos Problem 18",
            ],
        },
    }
    audit["sha256"] = semantic_sha256(audit)
    return audit


def build_claim(audit: dict[str, Any] | None = None) -> dict[str, Any]:
    audit = build_audit() if audit is None else audit
    claim: dict[str, Any] = {
        "schema": CLAIM_SCHEMA,
        "result_class": "final theorem audit certificate",
        "source": source_metadata(),
        "evidence_sha256": audit["sha256"],
        "claim": {
            "object": OBJECT_ID,
            "decision": "ACCEPTED",
            "variance_limit": "(1/12)sum_p (log p)^2/(p-1)^2",
            "weak_limit": "sum_p (log p)U_p",
            "zero_frequency": "2*pi/log(2)",
            "non_gaussian": True,
            "finite_diagnostics_only": True,
            "scope_excludes": [
                "high-prime tail CLT",
                "coarse local lower bound",
                "additive occupancy",
                "factorial half-range theorem",
                "Erdos Problem 18",
            ],
        },
    }
    claim["sha256"] = semantic_sha256(claim)
    return claim


def corrupted_claims(valid: dict[str, Any] | None = None) -> dict[str, dict[str, Any]]:
    valid = build_claim() if valid is None else valid
    mutations: dict[str, tuple[str, Any]] = {
        "wrong_variance_constant": (
            "variance_limit",
            "(1/6)sum_p (log p)^2/(p-1)^2",
        ),
        "wrong_denominator": (
            "variance_limit",
            "(1/12)sum_p (log p)^2/p^2",
        ),
        "false_gaussian": ("non_gaussian", False),
        "wrong_zero_frequency": ("zero_frequency", "pi/log(2)"),
        "finite_asymptotic": ("finite_diagnostics_only", False),
    }
    output: dict[str, dict[str, Any]] = {}
    for name, (key, value) in mutations.items():
        changed = copy.deepcopy(valid)
        changed["mutation"] = name
        changed["claim"][key] = value
        changed["sha256"] = semantic_sha256(changed)
        output[name] = changed
    return output


def _equal(actual: Any, expected: Any, label: str) -> None:
    if actual != expected:
        raise VerificationError(f"{label} mismatch: {actual!r} != {expected!r}")


def verify_audit(audit: dict[str, Any]) -> None:
    _equal(audit.get("schema"), SCHEMA, "schema")
    _equal(audit.get("source"), source_metadata(), "source metadata")
    _equal(audit.get("sha256"), semantic_sha256(audit), "semantic sha256")
    _equal(audit, build_audit(), "full semantic audit")


def verify_claim(claim: dict[str, Any], audit: dict[str, Any] | None = None) -> None:
    _equal(claim.get("schema"), CLAIM_SCHEMA, "claim schema")
    _equal(claim.get("source"), source_metadata(), "claim source metadata")
    _equal(claim.get("sha256"), semantic_sha256(claim), "claim semantic sha256")
    audit = build_audit() if audit is None else audit
    verify_audit(audit)
    _equal(claim, build_claim(audit), "full semantic claim")


def load_json(path: str | Path) -> dict[str, Any]:
    value = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise VerificationError("JSON root must be an object")
    return value


def write_json(path: str | Path, value: dict[str, Any]) -> None:
    Path(path).write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
