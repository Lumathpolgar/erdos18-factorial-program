from __future__ import annotations

import copy
import hashlib
import json
import math
from pathlib import Path
from typing import Any, Iterable

OBJECT_008 = "N3-ANA-008"
OBJECT_009 = "N3-ANA-009"
SCHEMA_AUDIT = "nova4.n3-high-prime-limit-audit.v1"
SCHEMA_CLAIM_008 = "nova4.n3-ana-008-final-claim.v1"
SCHEMA_CLAIM_009 = "nova4.n3-ana-009-final-claim.v1"

FROZEN_SOURCE = {
    "repository": "Lumathpolgar/erdos18-factorial-program",
    "branch": "nova/analytic-density",
    "handoff": "N3-HO-N4-002",
    "handoff_commit": "7469dada02fa4caca08ed391ef8b0cb0f1e855b2",
    "proof_file": "tracks/nova3-analytic-density/proofs/PRODUCT_MODEL_THEOREMS.md",
    "proof_file_blob_sha": "6260f8db0b377cf7dbc1850cbe25c91243099e10",
    "source_ledger_file": "tracks/nova3-analytic-density/SOURCE_LEDGER.md",
    "source_ledger_blob_sha": "da81e6aaf2674fdae036d72df002547d4a71b18a",
    "external_sources": {
        "N3-SRC-002": "prime number theorem",
        "N3-SRC-003": "Berry-Esseen inequality for independent summands",
    },
    "audit_stage": "POST_N3_ANA_006_CLOSURE",
}


class VerificationError(ValueError):
    pass


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")


def semantic_sha256(value: dict[str, Any]) -> str:
    body = copy.deepcopy(value)
    body.pop("sha256", None)
    return hashlib.sha256(canonical_bytes(body)).hexdigest()


def seal(value: dict[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(value)
    result["sha256"] = semantic_sha256(result)
    return result


def load_json(path: str | Path) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise VerificationError("top-level JSON value must be an object")
    return value


def dump_json(path: str | Path, value: dict[str, Any]) -> None:
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, sort_keys=True)
        handle.write("\n")


def primes_up_to(n: int) -> list[int]:
    if type(n) is not int or n < 0:
        raise ValueError("n must be a nonnegative integer")
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(n) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def valuation_factorial(n: int, p: int) -> int:
    if type(n) is not int or type(p) is not int or n < 0 or p < 2:
        raise ValueError("invalid valuation arguments")
    total = 0
    quotient = n
    while quotient:
        quotient //= p
        total += quotient
    return total


def tail_statistics(n: int, y: int, primes: Iterable[int] | None = None) -> dict[str, Any]:
    if type(n) is not int or type(y) is not int or n < 2 or y < 2 or y >= n:
        raise ValueError("invalid n,y")
    ps = list(primes) if primes is not None else primes_up_to(n)
    variance = 0.0
    half_span = 0.0
    maximizing_prime = None
    tail_prime_count = 0
    band_prime_count = 0
    band_variance = 0.0
    for p in ps:
        if p > n:
            break
        if p <= y:
            continue
        b = valuation_factorial(n, p)
        logp = math.log(p)
        contribution = b * (b + 2) * logp * logp / 12.0
        variance += contribution
        candidate = b * logp / 2.0
        if candidate > half_span:
            half_span = candidate
            maximizing_prime = p
        tail_prime_count += 1
        if p <= 2 * y:
            band_prime_count += 1
            band_variance += contribution
    if variance <= 0.0 or half_span <= 0.0 or maximizing_prime is None:
        raise ValueError("empty high-prime tail")
    standard_deviation = math.sqrt(variance)
    benchmark = n * n * math.log(y) / y
    return {
        "n": n,
        "y": y,
        "admissible_2y_le_sqrt_n": 2 * y <= math.isqrt(n),
        "tail_prime_count": tail_prime_count,
        "band_prime_count": band_prime_count,
        "variance": format(variance, ".17g"),
        "band_variance": format(band_variance, ".17g"),
        "standard_deviation": format(standard_deviation, ".17g"),
        "theorem_half_span_M": format(half_span, ".17g"),
        "full_span": format(2.0 * half_span, ".17g"),
        "maximizing_prime": maximizing_prime,
        "M_over_B": format(half_span / standard_deviation, ".17g"),
        "full_span_over_B": format(2.0 * half_span / standard_deviation, ".17g"),
        "variance_over_n2_logy_over_y": format(variance / benchmark, ".17g"),
    }


def build_diagnostics(ns: tuple[int, ...] = (10_000, 100_000, 1_000_000, 10_000_000)) -> list[dict[str, Any]]:
    if not ns or tuple(sorted(ns)) != ns:
        raise ValueError("ns must be a nonempty increasing tuple")
    primes = primes_up_to(max(ns))
    rows: list[dict[str, Any]] = []
    for n in ns:
        y = math.isqrt(n) // 2
        rows.append(tail_statistics(n, y, primes))
    return rows


def build_audit() -> dict[str, Any]:
    rows = build_diagnostics()
    phi2 = math.exp(-2.0) / math.sqrt(2.0 * math.pi)
    audit = {
        "schema": SCHEMA_AUDIT,
        "result_class": "proved theorem audits with finite diagnostics",
        "source": FROZEN_SOURCE,
        "decisions": {
            "N3_ANA_008": "ACCEPTED",
            "N3_ANA_009": "ACCEPTED_WITH_EXTERNAL_BERRY_ESSEEN_DEPENDENCY",
            "finite_table_is_asymptotic_proof": False,
            "request_C_full_span_label_is_theorem_M": False,
        },
        "N3_ANA_008": {
            "hypotheses": [
                "n tends to infinity through integers",
                "y=y(n) tends to infinity",
                "2*y <= sqrt(n) eventually",
                "independent uniform factorial exponent coordinates",
            ],
            "definitions": {
                "T_ny": "sum_{y<p<=n} (A_p-b_p/2) log p",
                "B_ny_squared": "Var(T_ny)",
                "M_ny": "max_{p>y} b_p log p / 2",
            },
            "proved_statements": [
                "B_ny^2 >> n^2 log(y)/y",
                "M_ny << n log(y)/y",
                "M_ny/B_ny << sqrt(log(y)/y)",
                "T_ny/B_ny converges weakly to N(0,1)",
            ],
            "proof_reconstruction": {
                "band": "y<p<=2y",
                "valuation_lower": "b_p>=floor(n/p)>=n/(2p) eventually",
                "prime_band_count": "pi(2y)-pi(y) >> y/log(y) by N3-SRC-002",
                "single_variance_lower": "b_p(b_p+2)(log p)^2/12 >> n^2(log y)^2/y^2",
                "variance_lower": "B_ny^2 >> n^2 log(y)/y",
                "valuation_upper": "b_p<=n/(p-1)",
                "monotonicity": "log(x)/(x-1) is decreasing for x>1",
                "half_span_upper": "M_ny << n log(y)/y",
                "ratio_upper": "M_ny/B_ny << sqrt(log(y)/y) -> 0",
                "lindeberg": "each centered summand has absolute value at most M_ny, so the Lindeberg sum is eventually zero",
            },
            "semantic_guards": {
                "M_is_half_span": True,
                "full_span_is_2M": True,
                "does_not_imply_full_model_gaussian": True,
                "requires_y_to_infinity": True,
                "requires_scale_admissibility": True,
            },
        },
        "N3_ANA_009": {
            "status_classification": "conditional theorem with accepted external dependency",
            "external_dependency": "N3-SRC-003 Berry-Esseen inequality",
            "hypotheses": [
                "all N3-ANA-008 hypotheses",
                "0<Delta<=B_ny",
                "abs(x)<=B_ny",
                "Delta>=K*M_ny",
            ],
            "explicit_constants": {
                "phi_2": "exp(-2)/sqrt(2*pi)",
                "phi_2_decimal": format(phi2, ".17g"),
                "K": "4*C_BE/phi_2",
                "lower_probability_constant": "phi_2/2",
            },
            "proved_statement": "P{T_ny in [x,x+Delta]} >= (phi_2/2)*Delta/B_ny",
            "proof_reconstruction": {
                "third_moment": "sum E|Y_p|^3 <= M_ny * B_ny^2",
                "kolmogorov_error": "at most C_BE*M_ny/B_ny",
                "standardized_interval": "left endpoint in [-1,1] and length in (0,1]",
                "normal_density_floor": "the interval lies in [-1,2], where phi>=phi(2)",
                "two_endpoint_loss": "subtract 2*C_BE*M_ny/B_ny",
                "chosen_K": "4*C_BE/phi(2)",
                "conclusion": "remaining mass at least (phi(2)/2)*Delta/B_ny",
            },
            "semantic_guards": {
                "coarse_windows_only": True,
                "does_not_reach_Delta_below_M": True,
                "does_not_give_arbitrary_x_uniformity": True,
                "does_not_prove_additive_occupancy": True,
            },
        },
        "finite_diagnostics": {
            "classification": "computational evidence only",
            "path": "y=floor(sqrt(n))/2",
            "rows": rows,
        },
        "scope_excludes": [
            "full-model Gaussian limit",
            "windows below the largest coordinate half-span",
            "formal-profile injectivity",
            "distinct numerical sums",
            "additive occupancy",
            "factorial half-range theorem",
            "Erdos Problem 18",
        ],
    }
    return seal(audit)


def build_claim_008(audit: dict[str, Any]) -> dict[str, Any]:
    return seal({
        "schema": SCHEMA_CLAIM_008,
        "result_class": "final theorem audit certificate",
        "source": FROZEN_SOURCE,
        "evidence_sha256": audit["sha256"],
        "claim": {
            "object": OBJECT_008,
            "decision": "ACCEPTED",
            "hypotheses_preserved": True,
            "M_definition": "max_{p>y} b_p log p / 2",
            "variance_lower": "B_ny^2 >> n^2 log(y)/y",
            "half_span_upper": "M_ny << n log(y)/y",
            "ratio": "M_ny/B_ny << sqrt(log(y)/y) -> 0",
            "limit": "T_ny/B_ny => N(0,1)",
            "finite_diagnostics_only": True,
            "does_not_imply_full_model_gaussian": True,
        },
    })


def build_claim_009(audit: dict[str, Any]) -> dict[str, Any]:
    return seal({
        "schema": SCHEMA_CLAIM_009,
        "result_class": "final conditional theorem audit certificate",
        "source": FROZEN_SOURCE,
        "evidence_sha256": audit["sha256"],
        "claim": {
            "object": OBJECT_009,
            "decision": "ACCEPTED_WITH_EXTERNAL_BERRY_ESSEEN_DEPENDENCY",
            "external_dependency": "N3-SRC-003",
            "parameter_range": "0<Delta<=B_ny and abs(x)<=B_ny",
            "coarse_window_condition": "Delta>=K*M_ny",
            "K": "4*C_BE/phi(2)",
            "lower_bound": "P{T_ny in [x,x+Delta]} >= (phi(2)/2)*Delta/B_ny",
            "two_endpoint_error_used": True,
            "does_not_reach_windows_below_M": True,
            "finite_diagnostics_only": True,
        },
    })


def expected_audit() -> dict[str, Any]:
    return build_audit()


def expected_claim_008(audit: dict[str, Any] | None = None) -> dict[str, Any]:
    return build_claim_008(audit or expected_audit())


def expected_claim_009(audit: dict[str, Any] | None = None) -> dict[str, Any]:
    return build_claim_009(audit or expected_audit())


def _verify_exact(actual: dict[str, Any], expected: dict[str, Any], label: str) -> None:
    if actual.get("sha256") != semantic_sha256(actual):
        raise VerificationError(f"{label} checksum mismatch")
    if actual != expected:
        raise VerificationError(f"{label} semantic mismatch")


def verify_audit(audit: dict[str, Any]) -> None:
    _verify_exact(audit, expected_audit(), "audit")


def verify_claim_008(claim: dict[str, Any], audit: dict[str, Any]) -> None:
    verify_audit(audit)
    _verify_exact(claim, expected_claim_008(audit), "N3-ANA-008 claim")


def verify_claim_009(claim: dict[str, Any], audit: dict[str, Any]) -> None:
    verify_audit(audit)
    _verify_exact(claim, expected_claim_009(audit), "N3-ANA-009 claim")


def corrupted_claims_008(claim: dict[str, Any]) -> dict[str, dict[str, Any]]:
    variants: dict[str, dict[str, Any]] = {}
    mutations = {
        "full_span_as_M": ("M_definition", "max_{p>y} b_p log p"),
        "remove_y_growth": ("hypotheses_preserved", False),
        "false_full_model_gaussian": ("does_not_imply_full_model_gaussian", False),
        "finite_asymptotic": ("finite_diagnostics_only", False),
    }
    for name, (key, value) in mutations.items():
        item = copy.deepcopy(claim)
        item["claim"][key] = value
        item["mutation"] = name
        item["sha256"] = semantic_sha256(item)
        variants[name] = item
    return variants


def corrupted_claims_009(claim: dict[str, Any]) -> dict[str, dict[str, Any]]:
    variants: dict[str, dict[str, Any]] = {}
    mutations = {
        "remove_coarse_window": ("coarse_window_condition", "Delta>0"),
        "one_endpoint_error": ("two_endpoint_error_used", False),
        "remove_external_dependency": ("external_dependency", "none"),
        "claim_fine_windows": ("does_not_reach_windows_below_M", False),
    }
    for name, (key, value) in mutations.items():
        item = copy.deepcopy(claim)
        item["claim"][key] = value
        item["mutation"] = name
        item["sha256"] = semantic_sha256(item)
        variants[name] = item
    return variants
