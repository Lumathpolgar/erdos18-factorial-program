"""Independent replay of Nova 2 theorem N2-ADD-115 and obstruction N2-OBS-107."""

from __future__ import annotations

from typing import Any

from .arithmetic import valuation_of_factorial
from .lattice import LatticeCertificateError
from .logcert import certified_log_parameters, factorial_at_least


NOVA2_COMMIT = "45c74a5fa747551422ffcad7d3ddf22788fbe622"
NOVA1_FROZEN_COMMIT = "b939574eb88a08bb03abda5bbe6ff2ca97444e08"


def _require_int(name: str, value: Any, *, minimum: int | None = None) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise LatticeCertificateError(f"{name} must be an integer")
    if minimum is not None and value < minimum:
        raise LatticeCertificateError(f"{name} must be at least {minimum}")
    return value


def _require_dict(name: str, value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise LatticeCertificateError(f"{name} must be an object")
    return value


def n2_obs_107_values(n: int) -> dict[str, Any]:
    """Recompute every finite arithmetic field in the frozen obstruction."""
    n = _require_int("n", n, minimum=3)
    r, layer_count = certified_log_parameters(n)
    v2 = valuation_of_factorial(n, 2)
    radius = (1 << r) - 1
    target = radius + 1
    common_divisor = 1 << (r + 1)
    return {
        "n": n,
        "r": r,
        "layer_count": layer_count,
        "v2_factorial": v2,
        "side_condition": r + layer_count <= v2 // 2 - 1,
        "radius": radius,
        "target": target,
        "lowest_address": r + 1,
        "common_divisor": common_divisor,
        "window": [1, target],
        "target_in_half_range": factorial_at_least(n, target * target),
        "window_contains_common_lattice_point": False,
    }


def generate_n2_obs_107_certificate(n: int) -> dict[str, Any]:
    return {
        "schema": "nova4.n2-obs-107.v1",
        "result_class": "disproved finite claim",
        "source": {
            "repository": "Lumathpolgar/erdos18-factorial-program",
            "nova2_branch": "nova/additive-occupancy",
            "nova2_commit": NOVA2_COMMIT,
            "nova2_theorem": "N2-ADD-115",
            "nova2_model_obstruction": "N2-OBS-107",
            "nova1_frozen_branch": "nova/factorial-structure",
            "nova1_frozen_commit": NOVA1_FROZEN_COMMIT,
        },
        "parameters": {"n": n},
        "claimed": n2_obs_107_values(n),
    }


def verify_n2_obs_107_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    certificate = _require_dict("certificate", certificate)
    if certificate.get("schema") != "nova4.n2-obs-107.v1":
        raise LatticeCertificateError("unsupported N2-OBS-107 certificate schema")
    source = _require_dict("source", certificate.get("source"))
    frozen = {
        "repository": "Lumathpolgar/erdos18-factorial-program",
        "nova2_branch": "nova/additive-occupancy",
        "nova2_commit": NOVA2_COMMIT,
        "nova2_theorem": "N2-ADD-115",
        "nova2_model_obstruction": "N2-OBS-107",
        "nova1_frozen_branch": "nova/factorial-structure",
        "nova1_frozen_commit": NOVA1_FROZEN_COMMIT,
    }
    for key, expected in frozen.items():
        if source.get(key) != expected:
            raise LatticeCertificateError(f"source.{key} does not match frozen artifact")
    parameters = _require_dict("parameters", certificate.get("parameters"))
    n = _require_int("parameters.n", parameters.get("n"), minimum=3)
    recomputed = n2_obs_107_values(n)
    if _require_dict("claimed", certificate.get("claimed")) != recomputed:
        raise LatticeCertificateError("claimed N2-OBS-107 fields do not match recomputation")
    if not recomputed["side_condition"]:
        raise LatticeCertificateError("valuation-budget side condition is not satisfied")
    if not recomputed["target_in_half_range"]:
        raise LatticeCertificateError("failing target is outside the claimed half-range")
    if recomputed["radius"] >= recomputed["common_divisor"] - 1:
        raise LatticeCertificateError("common-gcd obstruction precondition is not satisfied")
    if recomputed["window"] != [1, recomputed["target"]]:
        raise LatticeCertificateError("window endpoints do not replay")
    if recomputed["window"][1] >= recomputed["common_divisor"]:
        raise LatticeCertificateError("window is not disjoint from the common lattice")
    return {
        "status": "PASS",
        "audit_outcome": "ACCEPTED",
        "result_class": "disproved finite claim",
        "theorem_scope": "the exact frozen N1-HO-N2-001 model only",
        "recomputed": recomputed,
    }


def audit_n2_obs_107_range(n_min: int, n_max: int) -> dict[str, Any]:
    """Audit every n in a finite range and record all truth-value transitions."""
    n_min = _require_int("n_min", n_min, minimum=3)
    n_max = _require_int("n_max", n_max, minimum=n_min)
    transitions: list[dict[str, Any]] = []
    later_failures: list[dict[str, Any]] = []
    first_side = first_target = first_both = None
    prior: tuple[bool, bool, bool] | None = None
    seen_both = False
    for n in range(n_min, n_max + 1):
        values = n2_obs_107_values(n)
        side = values["side_condition"]
        target = values["target_in_half_range"]
        both = side and target
        if side and first_side is None:
            first_side = n
        if target and first_target is None:
            first_target = n
        if both and first_both is None:
            first_both = n
        if seen_both and not both:
            later_failures.append({
                "n": n,
                "side_condition": side,
                "target_in_half_range": target,
            })
        seen_both = seen_both or both
        current = (side, target, both)
        if current != prior:
            transitions.append({
                "n": n,
                "side_condition": side,
                "target_in_half_range": target,
                "both": both,
                "r": values["r"],
                "layer_count": values["layer_count"],
                "v2_factorial": values["v2_factorial"],
            })
            prior = current
    stable_from = None
    if first_both is not None:
        last_failure = later_failures[-1]["n"] if later_failures else first_both - 1
        if last_failure + 1 <= n_max:
            stable_from = last_failure + 1
    return {
        "schema": "nova4.n2-obs-107-range-audit.v1",
        "result_class": "exact finite theorem audit",
        "source_branch": "nova/additive-occupancy",
        "source_commit": NOVA2_COMMIT,
        "n_min": n_min,
        "n_max": n_max,
        "first_side_condition_n": first_side,
        "first_target_in_half_range_n": first_target,
        "first_admissible_failure_n": first_both,
        "later_failures_after_first_admissible": later_failures,
        "stable_success_through_checked_range_from_n": stable_from,
        "transitions": transitions,
    }
