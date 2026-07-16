"""Deterministic exact dataset generation and replay."""

from __future__ import annotations

import hashlib
import json
from bisect import bisect_right
import platform
import sys
from math import factorial, isqrt
from pathlib import Path
from time import perf_counter
from typing import Any

from .arithmetic import divisor_count_from_valuations, factorial_prime_valuations
from .certificates import (
    dump_certificate,
    make_representation_certificate,
    verify_representation_certificate,
)
from .search import certify_profile_with_bitsets, exact_profile_dp

DATASET_SCHEMA = "erdos18.factorial.half_range_profiles.v1"


def _stable_json_bytes(value: Any) -> bytes:
    return (
        json.dumps(
            value,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
            allow_nan=False,
        )
        + "\n"
    ).encode("utf-8")


def dataset_sha256(value: dict[str, Any]) -> str:
    payload = dict(value)
    payload.pop("sha256", None)
    return hashlib.sha256(_stable_json_bytes(payload)).hexdigest()


def _descending_greedy_count(ordered: tuple[int, ...], target: int) -> int | None:
    residual = target
    count = 0
    upper = len(ordered)
    while residual > 0:
        index = bisect_right(ordered, residual, 0, upper) - 1
        if index < 0:
            return None
        residual -= ordered[index]
        upper = index
        count += 1
    return count


def generate_dataset(
    n_min: int,
    n_max: int,
    *,
    certificate_dir: str | Path | None = None,
) -> dict[str, Any]:
    if n_min < 1 or n_max < n_min:
        raise ValueError("require 1 <= n_min <= n_max")
    certificate_path = Path(certificate_dir) if certificate_dir is not None else None
    records: list[dict[str, Any]] = []
    first_greedy_failure: dict[str, Any] | None = None

    for n in range(n_min, n_max + 1):
        target_limit = isqrt(factorial(n))
        started = perf_counter()
        profile = exact_profile_dp(n, target_limit)
        dp_seconds = perf_counter() - started

        started = perf_counter()
        certify_profile_with_bitsets(profile)
        bitset_seconds = perf_counter() - started

        H_value = profile.H
        hardest_targets = [
            target
            for target, value in enumerate(profile.lambda_values)
            if value == H_value
        ]
        greedy_failures: list[dict[str, int]] = []
        greedy_divisors = profile.eligible_divisors
        for target in range(target_limit + 1):
            greedy_count = _descending_greedy_count(greedy_divisors, target)
            optimal = profile.lambda_values[target]
            if greedy_count is None or greedy_count > optimal:
                failure = {
                    "target": target,
                    "optimal_terms": optimal,
                    "greedy_terms": -1 if greedy_count is None else greedy_count,
                }
                greedy_failures.append(failure)
                if first_greedy_failure is None:
                    first_greedy_failure = {"n": n, **failure}

        valuations = factorial_prime_valuations(n)
        record = {
            "n": n,
            "factorial": factorial(n),
            "target_interval": {
                "lower": 0,
                "upper_inclusive": target_limit,
                "H_argument": target_limit + 1,
            },
            "tau_factorial": divisor_count_from_valuations(valuations),
            "eligible_divisor_count": len(profile.eligible_divisors),
            "prime_valuations": [[p, valuations[p]] for p in sorted(valuations)],
            "lambda_values": list(profile.lambda_values),
            "H": H_value,
            "hardest_targets": hardest_targets,
            "greedy_suboptimal_count": len(greedy_failures),
            "first_greedy_failure": greedy_failures[0] if greedy_failures else None,
            "status": "exact finite theorem audit",
            "optimality_basis": [
                "minimum-cardinality 0/1 dynamic programming",
                "independent exact-cardinality bitset reachability",
            ],
            "runtime_seconds": {
                "dp": round(dp_seconds, 9),
                "bitset": round(bitset_seconds, 9),
            },
        }
        records.append(record)

        if certificate_path is not None:
            certificate_target = hardest_targets[0]
            certificate = make_representation_certificate(
                n=n,
                target=certificate_target,
                divisors=profile.witnesses[certificate_target],
                max_terms=H_value,
                target_range=(0, target_limit + 1),
                producer={
                    "method": "exact_profile_dp",
                    "result_class": "finite certificate",
                },
            )
            verify_representation_certificate(certificate)
            dump_certificate(
                certificate,
                certificate_path / f"n{n}_hardest_target_{certificate_target}.json",
            )

    dataset: dict[str, Any] = {
        "schema": DATASET_SCHEMA,
        "result_class": "exact finite theorem audit",
        "definition": "lambda_{n!}(x) for every integer 0 <= x <= floor(sqrt(n!))",
        "endpoint_convention": "H_{n!}(floor(sqrt(n!))+1)",
        "n_range": {"lower": n_min, "upper_inclusive": n_max},
        "arithmetic": "exact integers only",
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "records": records,
        "smallest_descending_greedy_suboptimality": first_greedy_failure,
    }
    dataset["sha256"] = dataset_sha256(dataset)
    return dataset


def write_dataset(dataset: dict[str, Any], path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(_stable_json_bytes(dataset))


def verify_dataset(dataset: dict[str, Any]) -> dict[str, Any]:
    if dataset.get("schema") != DATASET_SCHEMA:
        raise ValueError("unexpected dataset schema")
    expected_hash = dataset.get("sha256")
    if expected_hash != dataset_sha256(dataset):
        raise ValueError("dataset checksum mismatch")
    checked_targets = 0
    for record in dataset.get("records", []):
        n = record["n"]
        target_limit = record["target_interval"]["upper_inclusive"]
        profile = exact_profile_dp(n, target_limit)
        certify_profile_with_bitsets(profile)
        if list(profile.lambda_values) != record["lambda_values"]:
            raise ValueError(f"lambda profile mismatch for n={n}")
        H_value = profile.H
        if H_value != record["H"]:
            raise ValueError(f"H mismatch for n={n}")
        hardest = [
            target
            for target, value in enumerate(profile.lambda_values)
            if value == H_value
        ]
        if hardest != record["hardest_targets"]:
            raise ValueError(f"hardest target list mismatch for n={n}")
        valuations = factorial_prime_valuations(n)
        if record["prime_valuations"] != [[p, valuations[p]] for p in sorted(valuations)]:
            raise ValueError(f"prime valuation mismatch for n={n}")
        if record["tau_factorial"] != divisor_count_from_valuations(valuations):
            raise ValueError(f"divisor count mismatch for n={n}")
        if record["eligible_divisor_count"] != len(profile.eligible_divisors):
            raise ValueError(f"eligible divisor count mismatch for n={n}")
        greedy_failures = []
        for target in range(target_limit + 1):
            greedy_count = _descending_greedy_count(profile.eligible_divisors, target)
            optimal = profile.lambda_values[target]
            if greedy_count is None or greedy_count > optimal:
                greedy_failures.append({
                    "target": target,
                    "optimal_terms": optimal,
                    "greedy_terms": -1 if greedy_count is None else greedy_count,
                })
        if len(greedy_failures) != record["greedy_suboptimal_count"]:
            raise ValueError(f"greedy failure count mismatch for n={n}")
        expected_first = greedy_failures[0] if greedy_failures else None
        if expected_first != record["first_greedy_failure"]:
            raise ValueError(f"first greedy failure mismatch for n={n}")
        checked_targets += target_limit + 1
    return {
        "status": "PASS",
        "records": len(dataset.get("records", [])),
        "checked_targets": checked_targets,
        "sha256": expected_hash,
    }
