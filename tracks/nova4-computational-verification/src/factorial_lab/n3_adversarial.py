"""Semantic adversarial audit for Nova 3 request H and N3-ANA-011.

The verifier freezes the exact theorem contract. It rejects rehashed artifacts that
weaken hypotheses, strengthen conclusions, change endpoint semantics, or promote a
finite sweep into an asymptotic proof.
"""
from __future__ import annotations

from copy import deepcopy
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
PROOF_FILE = "tracks/nova3-analytic-density/proofs/EXPLICIT_PRIME_INTERVAL_AND_CAPACITY.md"
PROOF_FILE_BLOB_SHA = "e36daf98db86da16bd5ed8c6c82f43530d745f66"
SANITY_FILE = "tracks/nova3-analytic-density/proofs/prime_interval_capacity_sanity.py"
SANITY_FILE_BLOB_SHA = "519c900b616a33d95f3b2a8a8dec10d04a0a24f5"
N1_PROOF_FILE = "tracks/nova1-factorial-structure/proofs/HIGH_PRIME_MENU_CAPACITY.md"
N1_PROOF_COMMIT = "fa11f4b2cb86a2dd791df189ada12757be791804"
N1_PROOF_BLOB_SHA = "4255e76ff18f675ae80a0192381070d9a934fc97"
REQUEST_G_AUDIT_SHA = "e26653648c2cc9ebc30b03f01904dbb5bcca65737ead57abc9cdbc0b2f218bb0"
REQUEST_G_CLAIM_SHA = "e41f7e639c605ed4e70e4ac2cc6afe20d83ef8bf4f22e991fe0986449b9c1e88"
REQUEST_ID = "H"
OBJECT_ID = "N3-ANA-011"
THRESHOLD = 120_368
SCHEMA = "nova4.n3-threshold-adversarial-audit.v1"
CLAIM_SCHEMA = "nova4.n3-ana-011-final-claim.v1"
CONTRACT_SCHEMA = "nova4.n3-ana-011-contract.v1"

MUTATIONS = (
    "lower_threshold_without_supplement",
    "larger_address_range_without_proof",
    "remove_menu_unit_correction",
    "profiles_as_distinct_sums",
    "ceil_half_endpoint_without_analysis",
    "finite_sweep_as_asymptotic_proof",
)

FIXTURE_NAMES = {
    "lower_threshold_without_supplement": "corrupt_rehashed_lower_threshold.json",
    "larger_address_range_without_proof": "corrupt_rehashed_address_range.json",
    "remove_menu_unit_correction": "corrupt_rehashed_unit_correction.json",
    "profiles_as_distinct_sums": "corrupt_rehashed_profile_injectivity.json",
    "ceil_half_endpoint_without_analysis": "corrupt_rehashed_ceil_endpoint.json",
    "finite_sweep_as_asymptotic_proof": "corrupt_rehashed_finite_asymptotic.json",
}

REJECTION_REASONS = {
    "lower_threshold_without_supplement": (
        "n/2 must be at least 60184; 120367/2=60183.5 is outside the frozen source hypothesis"
    ),
    "larger_address_range_without_proof": (
        "N1-STR-009 is proved only through floor(v2(n!)/2)-1; no extension proof is supplied"
    ),
    "remove_menu_unit_correction": (
        "the lower half of subset products includes the unit, while U_e(n) requires u>1"
    ),
    "profiles_as_distinct_sums": (
        "the product counts formal profiles only; injectivity and numerical distinctness are not proved"
    ),
    "ceil_half_endpoint_without_analysis": (
        "pi(n/2)=pi(floor(n/2)); at n=120417 the ceil endpoint 60209 is prime and changes the count"
    ),
    "finite_sweep_as_asymptotic_proof": (
        "the 879633-point sweep is a finite certificate; uniformity beyond it comes from the proof"
    ),
}


class VerificationError(ValueError):
    """Raised when a contract or audit fails semantic verification."""


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def semantic_sha256(value: Any, *, omit: Iterable[str] = ("sha256",)) -> str:
    omitted = set(omit)
    if isinstance(value, dict):
        payload = {k: v for k, v in value.items() if k not in omitted}
    else:
        payload = value
    return hashlib.sha256(canonical_json(payload).encode("utf-8")).hexdigest()


def source_metadata() -> dict[str, Any]:
    return {
        "repository": REPOSITORY,
        "branch": SOURCE_BRANCH,
        "handoff": HANDOFF,
        "handoff_commit": HANDOFF_COMMIT,
        "request": REQUEST_ID,
        "object": OBJECT_ID,
        "proof_file": PROOF_FILE,
        "proof_file_blob_sha": PROOF_FILE_BLOB_SHA,
        "sanity_file": SANITY_FILE,
        "sanity_file_blob_sha": SANITY_FILE_BLOB_SHA,
        "imported_n1": {
            "commit": N1_PROOF_COMMIT,
            "file": N1_PROOF_FILE,
            "blob_sha": N1_PROOF_BLOB_SHA,
            "object": "N1-STR-009",
        },
        "request_G": {
            "audit_sha256": REQUEST_G_AUDIT_SHA,
            "claim_sha256": REQUEST_G_CLAIM_SHA,
            "range": [120_368, 1_000_000],
        },
    }


def _e_upper_bound() -> Fraction:
    """Elementary e < 11/4 bound used to prove log(2)>1/2."""
    return Fraction(11, 4)


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for d in range(3, isqrt(n) + 1, 2):
        if n % d == 0:
            return False
    return True


def proof_certificate() -> dict[str, Any]:
    exp12_comparison = 8**12 > THRESHOLD * 3**12
    e_upper = _e_upper_bound()
    ln2_lower_half = e_upper < 4
    threshold_rhs_upper = 32 * 12**2 + 10 * 12 + 8
    address_base_positive = THRESHOLD > threshold_rhs_upper
    derivative_base_lower = THRESHOLD - 64 * 12 - 10

    endpoint_n = 120_417
    endpoint_floor = endpoint_n // 2
    endpoint_ceil = (endpoint_n + 1) // 2
    endpoint_ceil_prime = _is_prime(endpoint_ceil)

    if not all(
        (
            exp12_comparison,
            ln2_lower_half,
            address_base_positive,
            derivative_base_lower > 0,
            endpoint_ceil == 60_209,
            endpoint_ceil_prime,
        )
    ):
        raise AssertionError("elementary proof certificate failed")

    return {
        "prime_interval_dependency": {
            "accepted_object": "N3-ANA-010",
            "statement": "pi(n)-pi(n/2)>=n/(3*log(n)) for every integer n>=120368",
            "source_lower_threshold": 5_393,
            "source_upper_threshold": 60_184,
            "derived_integer_threshold": THRESHOLD,
        },
        "address_uniformity": {
            "definitions": {
                "r_n": "ceil(4*log(n))",
                "M_n": "ceil(16*log(n)^2)",
                "e_M": "r_n+M_n",
                "V_n": "v2(n!)",
            },
            "ceiling_upper": "e_M<=16*L^2+4*L+2",
            "legendre_lower": "V_n>=n-L/log(2)-1",
            "sufficient_condition": "n>=32*L^2+(8+1/log(2))*L+8",
            "log_threshold_upper_proof": {
                "e_lower": "e>8/3",
                "eight_over_three_power_12_exceeds_threshold": exp12_comparison,
                "conclusion": "log(120368)<12",
            },
            "ln2_lower_proof": {
                "e_upper": f"{e_upper.numerator}/{e_upper.denominator}",
                "e_upper_less_than_4": ln2_lower_half,
                "conclusion": "log(2)>1/2 and 1/log(2)<2",
            },
            "base_rhs_upper": threshold_rhs_upper,
            "base_margin_lower": THRESHOLD - threshold_rhs_upper,
            "derivative_control": {
                "function": "n-64*log(n)-10",
                "base_lower": derivative_base_lower,
                "increasing_for_n_greater_than_64": True,
            },
            "conclusion": "e_M<=floor(V_n/2)-1 for every integer n>=120368",
        },
        "menu_transfer": {
            "imported_object": "N1-STR-009",
            "definition_match": {
                "odd_divisor": True,
                "unit_excluded": True,
                "size_condition": "2^e*u<=floor(sqrt(n!))",
                "address_hypothesis": "0<=e<=floor(V_n/2)-1",
            },
            "high_prime_subset_products": "2^m_n",
            "strict_lower_half_count": "2^(m_n-1)",
            "unit_is_in_lower_half": True,
            "menu_lower_bound": "2^(m_n-1)-1",
            "floor_sqrt_step": (
                "legal address gives 2^e*sqrt(O_n)<=sqrt(n!)/2; "
                "sqrt(n!)/2<=floor(sqrt(n!)) for n!>=4"
            ),
        },
        "profile_capacity": {
            "formal_profile_lower_exponent": "M_n*(m_n-1)+r_n",
            "n_at_least_12_log_n": True,
            "exponent_lower": "4*n*log(n)",
            "required_bit_upper": "1+n*log(n)/(2*log(2))",
            "ln2_greater_than_half": True,
            "conclusion": "formal profile count is at least X_n+1",
            "injectivity_proved": False,
            "distinct_numerical_sums_proved": False,
            "additive_occupancy_proved": False,
        },
        "endpoint_witness": {
            "n": endpoint_n,
            "floor_n_over_2": endpoint_floor,
            "ceil_n_over_2": endpoint_ceil,
            "ceil_endpoint_is_prime": endpoint_ceil_prime,
            "conclusion": "pi(ceil(n/2))=pi(floor(n/2))+1 at this n",
        },
    }


def canonical_contract() -> dict[str, Any]:
    contract: dict[str, Any] = {
        "schema": CONTRACT_SCHEMA,
        "source": source_metadata(),
        "theorem": {
            "object": OBJECT_ID,
            "decision": "ACCEPTED",
            "integer_threshold": THRESHOLD,
            "threshold_finite_supplement": False,
            "address_legal_max": "floor(v2(n!)/2)-1",
            "address_extension_proof_supplied": False,
            "menu_definition": "u|n!, u odd, u>1, 2^e*u<=floor(sqrt(n!))",
            "menu_lower_bound": "2^(m_n-1)-1",
            "menu_unit_excluded": True,
            "profile_object": "formal profiles",
            "profile_injectivity": False,
            "distinct_numerical_sums": False,
            "half_endpoint": "floor(n/2)",
            "half_endpoint_analysis": "pi(n/2)=pi(floor(n/2)) for integer n",
            "request_G_finite_only": True,
            "uniform_theorem_source": "analytic proof, not finite sweep",
            "scope": {
                "address_legality": True,
                "menu_cardinality": True,
                "formal_profile_capacity": True,
                "additive_occupancy": False,
                "factorial_half_range": False,
                "erdos18_solved": False,
            },
        },
    }
    contract["sha256"] = semantic_sha256(contract)
    return contract


def corrupted_contract(kind: str) -> dict[str, Any]:
    if kind not in MUTATIONS:
        raise ValueError(f"unknown mutation: {kind}")
    value = deepcopy(canonical_contract())
    theorem = value["theorem"]
    if kind == "lower_threshold_without_supplement":
        theorem["integer_threshold"] = THRESHOLD - 1
    elif kind == "larger_address_range_without_proof":
        theorem["address_legal_max"] = "floor(v2(n!)/2)"
    elif kind == "remove_menu_unit_correction":
        theorem["menu_lower_bound"] = "2^(m_n-1)"
    elif kind == "profiles_as_distinct_sums":
        theorem["profile_object"] = "distinct numerical sums"
        theorem["profile_injectivity"] = True
        theorem["distinct_numerical_sums"] = True
    elif kind == "ceil_half_endpoint_without_analysis":
        theorem["half_endpoint"] = "ceil(n/2)"
        theorem["half_endpoint_analysis"] = "none"
    elif kind == "finite_sweep_as_asymptotic_proof":
        theorem["request_G_finite_only"] = False
        theorem["uniform_theorem_source"] = "finite sweep"
    value["mutation"] = kind
    value["sha256"] = semantic_sha256(value)
    return value


def verify_contract(value: dict[str, Any]) -> None:
    if not isinstance(value, dict):
        raise VerificationError("contract root must be an object")
    if value.get("sha256") != semantic_sha256(value):
        raise VerificationError("contract semantic sha256 mismatch")
    expected = canonical_contract()
    if value != expected:
        kind = value.get("mutation", "unknown semantic mutation")
        reason = REJECTION_REASONS.get(kind, "contract differs from the frozen theorem semantics")
        raise VerificationError(f"rejected {kind}: {reason}")


def fixture_records() -> list[dict[str, Any]]:
    records = []
    for index, kind in enumerate(MUTATIONS, start=1):
        fixture = corrupted_contract(kind)
        rejected = False
        message = ""
        try:
            verify_contract(fixture)
        except VerificationError as exc:
            rejected = True
            message = str(exc)
        if not rejected:
            raise AssertionError(f"corruption was accepted: {kind}")
        records.append(
            {
                "id": f"H{index}",
                "mutation": kind,
                "fixture": FIXTURE_NAMES[kind],
                "fixture_sha256": fixture["sha256"],
                "outer_hash_recomputed": True,
                "expected": "REJECTED",
                "rejected": True,
                "reason": REJECTION_REASONS[kind],
                "verifier_message": message,
            }
        )
    return records


def build_audit() -> dict[str, Any]:
    audit: dict[str, Any] = {
        "schema": SCHEMA,
        "result_class": "semantic adversarial theorem audit",
        "source": source_metadata(),
        "proof_reconstruction": proof_certificate(),
        "canonical_contract": canonical_contract(),
        "adversarial_tests": fixture_records(),
        "decision": {
            "request_H": "ACCEPTED",
            "N3_ANA_011": "ACCEPTED",
            "all_six_required_corruptions_rejected": True,
            "scope_restrictions_enforced": True,
            "request_G_remains_finite_certificate_only": True,
        },
        "scope": {
            "proved": [
                "address legality for every integer n>=120368",
                "menu cardinality lower bound for every addressed layer",
                "formal profile capacity at least X_n+1",
            ],
            "not_proved": [
                "formal-profile injectivity",
                "distinct numerical sums",
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
            "integer_threshold": THRESHOLD,
            "conclusions": audit["scope"]["proved"],
            "exclusions": audit["scope"]["not_proved"],
            "all_six_required_corruptions_rejected": True,
            "finite_sweep_is_not_asymptotic_proof": True,
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
    _require_equal(audit.get("sha256"), semantic_sha256(audit), "audit semantic sha256")
    _require_equal(audit, build_audit(), "full semantic audit")


def verify_claim(claim: dict[str, Any], audit: dict[str, Any] | None = None) -> None:
    _require_equal(claim.get("schema"), CLAIM_SCHEMA, "claim schema")
    _require_equal(claim.get("source"), source_metadata(), "claim source metadata")
    _require_equal(claim.get("sha256"), semantic_sha256(claim), "claim semantic sha256")
    audit = build_audit() if audit is None else audit
    verify_audit(audit)
    _require_equal(claim, build_claim(audit), "full semantic claim")


def verify_fixture_directory(directory: str | Path) -> None:
    root = Path(directory)
    for kind in MUTATIONS:
        path = root / FIXTURE_NAMES[kind]
        value = load_json(path)
        _require_equal(value, corrupted_contract(kind), f"fixture {kind}")
        try:
            verify_contract(value)
        except VerificationError:
            continue
        raise VerificationError(f"corrupted fixture was accepted: {path}")


def load_json(path: str | Path) -> dict[str, Any]:
    value = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise VerificationError("JSON root must be an object")
    return value


def write_json(path: str | Path, value: dict[str, Any]) -> None:
    Path(path).write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_fixtures(directory: str | Path) -> None:
    root = Path(directory)
    root.mkdir(parents=True, exist_ok=True)
    for kind in MUTATIONS:
        write_json(root / FIXTURE_NAMES[kind], corrupted_contract(kind))
