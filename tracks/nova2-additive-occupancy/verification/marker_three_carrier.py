#!/usr/bin/env python3
"""Exact verifier for N2-ADD-120 marker-three carrier certificates.

The verifier consumes certified, sorted odd-core menus. It does not claim to
construct full factorial menus. Menu generation and the source commit remain
separate certificate obligations.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


SCHEMA = "nova2.marker-three-carrier.v1"


class CarrierCertificateError(ValueError):
    """Raised when a carrier certificate is malformed or inconsistent."""


def _require_int(name: str, value: Any, *, minimum: int | None = None) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CarrierCertificateError(f"{name} must be an integer")
    if minimum is not None and value < minimum:
        raise CarrierCertificateError(f"{name} must be at least {minimum}")
    return value


def _require_dict(name: str, value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise CarrierCertificateError(f"{name} must be an object")
    return value


def _require_list(name: str, value: Any) -> list[Any]:
    if not isinstance(value, list):
        raise CarrierCertificateError(f"{name} must be a list")
    return value


def _validate_cores(name: str, raw: Any, *, bound: int) -> list[int]:
    values = _require_list(name, raw)
    cores: list[int] = []
    previous = 0
    for index, raw_core in enumerate(values):
        core = _require_int(f"{name}[{index}]", raw_core, minimum=1)
        if core % 2 == 0:
            raise CarrierCertificateError(f"{name}[{index}] must be odd")
        if core <= previous:
            raise CarrierCertificateError(f"{name} must be strictly increasing")
        if core > bound:
            raise CarrierCertificateError(
                f"{name}[{index}]={core} exceeds certified layer bound {bound}"
            )
        cores.append(core)
        previous = core
    return cores


def verify_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    certificate = _require_dict("certificate", certificate)
    if certificate.get("schema") != SCHEMA:
        raise CarrierCertificateError(f"unsupported schema: {certificate.get('schema')!r}")

    source = _require_dict("source", certificate.get("source"))
    for field in ("repository", "branch", "commit", "construction"):
        value = source.get(field)
        if not isinstance(value, str) or not value:
            raise CarrierCertificateError(f"source.{field} must be a nonempty string")

    parameters = _require_dict("parameters", certificate.get("parameters"))
    n = _require_int("parameters.n", parameters.get("n"), minimum=1)
    window = _require_int("parameters.window", parameters.get("window"), minimum=0)
    endpoint = _require_int("parameters.endpoint", parameters.get("endpoint"), minimum=0)
    protected_endpoint = _require_int(
        "parameters.protected_endpoint",
        parameters.get("protected_endpoint", 0),
        minimum=0,
    )

    raw_layers = _require_list("layers", certificate.get("layers"))
    if not raw_layers:
        raise CarrierCertificateError("layers must be nonempty")

    current_endpoint = 0
    rows: list[dict[str, Any]] = []
    expected_t = 1

    for raw_layer in raw_layers:
        layer = _require_dict(f"layers[{expected_t - 1}]", raw_layer)
        t = _require_int("layer.t", layer.get("t"), minimum=1)
        if t != expected_t:
            raise CarrierCertificateError(
                f"layers must be consecutive from 1; expected {expected_t}, got {t}"
            )

        scale = 1 << (t - 1)
        layer_bound = endpoint // scale
        cores = _validate_cores(f"layers[{t - 1}].cores", layer.get("cores"), bound=layer_bound)
        gap_threshold = (current_endpoint + window + 1) // scale

        previous = 0
        connected_max = 0
        first_block: dict[str, int] | None = None
        for core in cores:
            gap = core - previous
            if gap <= gap_threshold:
                connected_max = core
                previous = core
                continue
            first_block = {
                "left_core": previous,
                "right_core": core,
                "gap": gap,
            }
            break

        current_endpoint += scale * connected_max
        rows.append(
            {
                "t": t,
                "scale": scale,
                "layer_bound": layer_bound,
                "core_count": len(cores),
                "gap_threshold": gap_threshold,
                "connected_max_core": connected_max,
                "certified_endpoint": current_endpoint,
                "first_blocking_gap": first_block,
            }
        )
        expected_t += 1

    occupied_through = current_endpoint + window
    if occupied_through < protected_endpoint:
        raise CarrierCertificateError(
            "carrier certificate does not replay the separately proved protected endpoint"
        )

    claimed = certificate.get("claimed")
    recomputed = {
        "n": n,
        "window": window,
        "endpoint": endpoint,
        "protected_endpoint": protected_endpoint,
        "carrier_endpoint": current_endpoint,
        "occupied_through": occupied_through,
        "reaches_full_endpoint": occupied_through >= endpoint,
        "rows": rows,
    }
    if claimed is not None and _require_dict("claimed", claimed) != recomputed:
        raise CarrierCertificateError("claimed result does not match exact recomputation")

    return {
        "status": "PASS",
        "result_class": "finite certificate",
        "proof_engine": "N2-ADD-120 connected-core carrier recursion",
        "model_outcome": (
            "carrier criterion reaches endpoint"
            if occupied_through >= endpoint
            else "carrier criterion remains incomplete; full model undecided"
        ),
        "recomputed": recomputed,
        "source": source,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path, help="JSON carrier certificate")
    parser.add_argument(
        "--write-result",
        type=Path,
        help="optional path for normalized verification output",
    )
    args = parser.parse_args()

    try:
        certificate = json.loads(args.certificate.read_text(encoding="utf-8"))
        result = verify_certificate(certificate)
    except (OSError, json.JSONDecodeError, CarrierCertificateError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, indent=2))
        return 1

    rendered = json.dumps(result, indent=2, sort_keys=True)
    print(rendered)
    if args.write_result is not None:
        args.write_result.write_text(rendered + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
