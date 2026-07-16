"""Fail-closed representation certificate schema and verifier."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Mapping

from .arithmetic import is_divisor_of_factorial

SCHEMA = "erdos18.factorial.representation.v1"


class CertificateError(ValueError):
    """Raised when a certificate fails an exact verification condition."""


def _strict_int(name: str, value: object, *, minimum: int | None = None) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CertificateError(f"{name} must be an integer")
    if minimum is not None and value < minimum:
        raise CertificateError(f"{name} must be at least {minimum}")
    return value


def canonicalize_certificate(certificate: Mapping[str, Any]) -> dict[str, Any]:
    """Return a JSON-serializable canonical copy with terms sorted by value and label."""
    normalized = json.loads(json.dumps(certificate, ensure_ascii=False))
    terms = normalized.get("terms")
    if isinstance(terms, list):
        normalized["terms"] = sorted(
            terms,
            key=lambda term: (
                term.get("value") if isinstance(term, dict) else -1,
                term.get("label", "") if isinstance(term, dict) else "",
            ),
        )
    return normalized


def canonical_json_bytes(certificate: Mapping[str, Any]) -> bytes:
    normalized = canonicalize_certificate(certificate)
    text = json.dumps(
        normalized,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    )
    return (text + "\n").encode("utf-8")


def certificate_sha256(certificate: Mapping[str, Any]) -> str:
    return hashlib.sha256(canonical_json_bytes(certificate)).hexdigest()


def load_certificate(path: str | Path) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise CertificateError("certificate root must be an object")
    return value


def dump_certificate(certificate: Mapping[str, Any], path: str | Path) -> str:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    data = canonical_json_bytes(certificate)
    path.write_bytes(data)
    return hashlib.sha256(data).hexdigest()


def make_representation_certificate(
    *,
    n: int,
    target: int,
    divisors: list[int] | tuple[int, ...],
    max_terms: int | None = None,
    labels: list[str] | None = None,
    target_range: tuple[int, int] | None = None,
    producer: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    values = list(divisors)
    if labels is None:
        labels = [f"d{i}" for i in range(len(values))]
    if len(labels) != len(values):
        raise ValueError("labels and divisors must have equal length")
    certificate: dict[str, Any] = {
        "schema": SCHEMA,
        "n": n,
        "target": target,
        "max_terms": len(values) if max_terms is None else max_terms,
        "terms": [
            {"label": label, "value": value}
            for label, value in zip(labels, values, strict=True)
        ],
    }
    if target_range is not None:
        certificate["target_range"] = {
            "lower": target_range[0],
            "upper_exclusive": target_range[1],
        }
    if producer is not None:
        certificate["producer"] = dict(producer)
    return canonicalize_certificate(certificate)


def verify_representation_certificate(certificate: Mapping[str, Any]) -> dict[str, Any]:
    """Independently verify a distinct-divisor representation certificate.

    The verifier recomputes every arithmetic fact. Producer metadata, cached sums,
    solver status, labels, and claimed fingerprints are never used as proof inputs.
    """
    if not isinstance(certificate, Mapping):
        raise CertificateError("certificate root must be an object")
    if certificate.get("schema") != SCHEMA:
        raise CertificateError(f"schema must equal {SCHEMA!r}")

    n = _strict_int("n", certificate.get("n"), minimum=1)
    target = _strict_int("target", certificate.get("target"), minimum=0)
    max_terms = _strict_int("max_terms", certificate.get("max_terms"), minimum=0)

    target_range = certificate.get("target_range")
    if target_range is not None:
        if not isinstance(target_range, Mapping):
            raise CertificateError("target_range must be an object")
        lower = _strict_int("target_range.lower", target_range.get("lower"), minimum=0)
        upper = _strict_int(
            "target_range.upper_exclusive",
            target_range.get("upper_exclusive"),
            minimum=1,
        )
        if lower >= upper:
            raise CertificateError("target_range must be nonempty")
        if not lower <= target < upper:
            raise CertificateError("target lies outside target_range")

    terms = certificate.get("terms")
    if not isinstance(terms, list):
        raise CertificateError("terms must be an array")

    values: list[int] = []
    for index, term in enumerate(terms):
        if not isinstance(term, Mapping):
            raise CertificateError(f"terms[{index}] must be an object")
        value = _strict_int(f"terms[{index}].value", term.get("value"), minimum=1)
        label = term.get("label")
        if label is not None and not isinstance(label, str):
            raise CertificateError(f"terms[{index}].label must be a string")
        values.append(value)

    if len(values) != len(set(values)):
        raise CertificateError("terms contain repeated numerical divisors")
    if len(values) > max_terms:
        raise CertificateError("term count exceeds max_terms")

    illegal = [value for value in values if not is_divisor_of_factorial(value, n)]
    if illegal:
        raise CertificateError(f"terms contain values that do not divide n!: {illegal}")

    computed_sum = sum(values)
    if computed_sum != target:
        raise CertificateError(
            f"exact sum mismatch: computed {computed_sum}, certificate target {target}"
        )

    if "claimed_sum" in certificate:
        claimed_sum = _strict_int("claimed_sum", certificate["claimed_sum"], minimum=0)
        if claimed_sum != computed_sum:
            raise CertificateError("claimed_sum disagrees with recomputed exact sum")
    if "claimed_term_count" in certificate:
        claimed_count = _strict_int(
            "claimed_term_count", certificate["claimed_term_count"], minimum=0
        )
        if claimed_count != len(values):
            raise CertificateError("claimed_term_count disagrees with recomputed count")

    return {
        "status": "PASS",
        "schema": SCHEMA,
        "n": n,
        "target": target,
        "computed_sum": computed_sum,
        "term_count": len(values),
        "max_terms": max_terms,
        "values": sorted(values),
        "certificate_sha256": certificate_sha256(certificate),
    }
