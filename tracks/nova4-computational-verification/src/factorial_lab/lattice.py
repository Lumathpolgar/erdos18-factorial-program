"""Exact lattice, residue, and finite-window falsification tools.

This module deliberately runs cheap structural gates before any convolution or
optimization.  It uses exact integers and rational interval bounds throughout.
"""

from __future__ import annotations

import json
import re
from bisect import bisect_right
from functools import reduce
from math import gcd
from pathlib import Path
from typing import Any, Iterable

from .arithmetic import is_divisor_of_factorial


class LatticeCertificateError(ValueError):
    """Raised when a lattice artifact is malformed or its claims do not replay."""


class LatticeResourceLimit(RuntimeError):
    """Raised when exact finite support exceeds the declared deterministic limit."""


_SHA_RE = re.compile(r"^[0-9a-f]{40}$")


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


def _require_list(name: str, value: Any) -> list[Any]:
    if not isinstance(value, list):
        raise LatticeCertificateError(f"{name} must be an array")
    return value


def _validate_source(source: dict[str, Any]) -> None:
    for field in ("repository", "branch", "commit"):
        if not isinstance(source.get(field), str) or not source[field]:
            raise LatticeCertificateError(f"source.{field} must be a nonempty string")
    if not _SHA_RE.fullmatch(source["commit"]):
        raise LatticeCertificateError("source.commit must be an exact 40-character SHA")


def reachable_residues(layers: list[list[int]], modulus: int) -> set[int]:
    modulus = _require_int("modulus", modulus, minimum=2)
    residues = {0}
    for terms in layers:
        choices = {term % modulus for term in terms}
        residues = residues | {(left + right) % modulus for left in residues for right in choices}
    return residues


def _first_residue_window_failure(
    residues: set[int], modulus: int, radius: int, target_min: int, target_max: int
) -> int | None:
    if radius + 1 >= modulus:
        return None
    start = max(target_min, radius + 1)
    stop = min(target_max, start + modulus - 1)
    for target in range(start, stop + 1):
        window_residues = {(target - offset) % modulus for offset in range(radius + 1)}
        if residues.isdisjoint(window_residues):
            return target
    return None


def _first_gcd_window_failure(g: int, radius: int, target_min: int, target_max: int) -> int | None:
    if g < 2 or radius >= g - 1:
        return None
    target = max(target_min, radius + 1)
    residue = target % g
    if residue <= radius:
        target += radius + 1 - residue
    return target if target <= target_max else None


def _exact_reachable_sums(
    layers: list[list[int]], correction_terms: list[int], target_max: int, max_states: int
) -> set[int]:
    reachable = {0}
    for terms in layers:
        additions = {subtotal + term for subtotal in reachable for term in terms if subtotal + term <= target_max}
        reachable |= additions
        if len(reachable) > max_states:
            raise LatticeResourceLimit(
                f"exact support exceeded max_states={max_states}; status is unknown due to resource limits"
            )
    for term in correction_terms:
        reachable |= {subtotal + term for subtotal in reachable if subtotal + term <= target_max}
        if len(reachable) > max_states:
            raise LatticeResourceLimit(
                f"exact support exceeded max_states={max_states}; status is unknown due to resource limits"
            )
    return reachable


def _first_exact_window_failure(
    reachable: set[int], radius: int, target_min: int, target_max: int
) -> int | None:
    ordered = sorted(reachable)
    for target in range(target_min, target_max + 1):
        index = bisect_right(ordered, target) - 1
        if index < 0 or ordered[index] < target - radius:
            return target
    return None


def verify_label_family_certificate(
    certificate: dict[str, Any], *, max_exact_states: int = 2_000_000
) -> dict[str, Any]:
    """Verify an explicit finite label family and run lattice gates first."""
    certificate = _require_dict("certificate", certificate)
    if certificate.get("schema") != "nova4.label-family.v1":
        raise LatticeCertificateError("unsupported label-family schema")
    source = _require_dict("source", certificate.get("source"))
    _validate_source(source)
    n = _require_int("n", certificate.get("n"), minimum=1)
    interval = _require_dict("target_interval", certificate.get("target_interval"))
    target_min = _require_int("target_interval.min", interval.get("min"), minimum=0)
    target_max = _require_int("target_interval.max", interval.get("max"), minimum=target_min)
    radius = _require_int("correction_radius", certificate.get("correction_radius"), minimum=0)
    layers_raw = _require_list("layers", certificate.get("layers"))
    corrections = [
        _require_int(f"correction_terms[{index}]", term, minimum=1)
        for index, term in enumerate(_require_list("correction_terms", certificate.get("correction_terms", [])))
    ]
    if not layers_raw and not corrections:
        raise LatticeCertificateError("at least one layer or correction term is required")

    layers: list[list[int]] = []
    seen: dict[int, str] = {}
    for layer_index, raw in enumerate(layers_raw):
        layer = _require_dict(f"layers[{layer_index}]", raw)
        layer_id = layer.get("id")
        if not isinstance(layer_id, str) or not layer_id:
            raise LatticeCertificateError(f"layers[{layer_index}].id must be nonempty")
        if layer.get("max_select", 1) != 1:
            raise LatticeCertificateError(f"layers[{layer_index}] must use max_select=1")
        terms = [
            _require_int(f"layers[{layer_index}].terms[{term_index}]", term, minimum=1)
            for term_index, term in enumerate(_require_list(f"layers[{layer_index}].terms", layer.get("terms")))
        ]
        if len(terms) != len(set(terms)):
            raise LatticeCertificateError(f"duplicate numerical term within layer {layer_id}")
        for term in terms:
            if term > target_max:
                raise LatticeCertificateError(f"main term {term} exceeds the stated target range")
            if not is_divisor_of_factorial(term, n):
                raise LatticeCertificateError(f"main term {term} does not divide {n}!")
            if term in seen:
                raise LatticeCertificateError(
                    f"duplicate numerical term {term} across {seen[term]} and {layer_id}"
                )
            seen[term] = layer_id
        layers.append(terms)

    if len(corrections) != len(set(corrections)):
        raise LatticeCertificateError("duplicate numerical correction term")
    for term in corrections:
        if term > target_max:
            raise LatticeCertificateError(f"correction term {term} exceeds the stated target range")
        if not is_divisor_of_factorial(term, n):
            raise LatticeCertificateError(f"correction term {term} does not divide {n}!")
        if term in seen:
            raise LatticeCertificateError(f"correction term {term} collides with main layer {seen[term]}")
        seen[term] = "correction_palette"

    main_terms = [term for layer in layers for term in layer]
    main_gcd = reduce(gcd, main_terms, 0)
    final_gcd = reduce(gcd, main_terms + corrections, 0)
    claimed = _require_dict("claimed", certificate.get("claimed", {}))
    if "main_gcd" in claimed and claimed["main_gcd"] != main_gcd:
        raise LatticeCertificateError("claimed.main_gcd does not match recomputation")

    gcd_failure = _first_gcd_window_failure(final_gcd, radius, target_min, target_max)
    moduli = _require_list("residue_moduli", certificate.get("residue_moduli", list(range(2, 65))))
    residue_reports: list[dict[str, Any]] = []
    residue_failures: list[tuple[int, int]] = []
    for index, raw_modulus in enumerate(moduli):
        modulus = _require_int(f"residue_moduli[{index}]", raw_modulus, minimum=2)
        if modulus > 4096:
            raise LatticeCertificateError("residue modulus exceeds deterministic limit 4096")
        main_residues = reachable_residues(layers, modulus)
        final_layers = layers + [[term] for term in corrections]
        final_residues = reachable_residues(final_layers, modulus)
        failure = _first_residue_window_failure(final_residues, modulus, radius, target_min, target_max)
        residue_reports.append(
            {
                "modulus": modulus,
                "main_reachable_residues": sorted(main_residues),
                "final_reachable_residues": sorted(final_residues),
                "first_certified_failure": failure,
            }
        )
        if failure is not None:
            residue_failures.append((failure, modulus))

    exact_support = _exact_reachable_sums(layers, corrections, target_max, max_exact_states)
    exact_failure = _first_exact_window_failure(exact_support, radius, target_min, target_max)

    candidates: list[dict[str, Any]] = []
    if gcd_failure is not None:
        candidates.append({"target": gcd_failure, "condition": 4, "kind": "common_gcd"})
    for target, modulus in residue_failures:
        candidates.append(
            {"target": target, "condition": 4, "kind": "residue", "modulus": modulus}
        )
    if exact_failure is not None:
        candidates.append({"target": exact_failure, "condition": 8, "kind": "exact_window"})
    smallest = min(candidates, key=lambda item: (item["target"], item["condition"])) if candidates else None

    if "first_failure_target" in claimed:
        recomputed_target = None if smallest is None else smallest["target"]
        if claimed["first_failure_target"] != recomputed_target:
            raise LatticeCertificateError("claimed.first_failure_target does not match recomputation")

    return {
        "status": "PASS",
        "result_class": "disproved finite claim" if smallest else "finite certificate",
        "n": n,
        "target_interval": {"min": target_min, "max": target_max},
        "correction_radius": radius,
        "main_term_count": len(main_terms),
        "correction_term_count": len(corrections),
        "main_gcd": main_gcd,
        "final_gcd": final_gcd,
        "gcd_gate_first_failure": gcd_failure,
        "residue_reports": residue_reports,
        "exact_reachable_count": len(exact_support),
        "exact_first_window_failure": exact_failure,
        "smallest_failure": smallest,
    }


def load_lattice_certificate(path: str | Path) -> dict[str, Any]:
    try:
        with Path(path).open("r", encoding="utf-8") as handle:
            value = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        raise LatticeCertificateError(f"could not load lattice certificate: {exc}") from exc
    return _require_dict("certificate", value)


def write_json(value: dict[str, Any], path: str | Path) -> None:
    with Path(path).open("w", encoding="utf-8") as handle:
        json.dump(value, handle, sort_keys=True, indent=2, ensure_ascii=False)
        handle.write("\n")
