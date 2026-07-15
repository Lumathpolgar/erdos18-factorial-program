"""Standalone replay interface for Nova 4 artifacts."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .certificates import CertificateError, load_certificate, verify_representation_certificate
from .dataset import generate_dataset, verify_dataset, write_dataset
from .lattice import (
    LatticeCertificateError,
    LatticeResourceLimit,
    load_lattice_certificate,
    verify_label_family_certificate,
    write_json,
)
from .n2_audit import audit_n2_obs_107_range, verify_n2_obs_107_certificate


def _print(value: object) -> None:
    print(json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False))


def command_verify(args: argparse.Namespace) -> int:
    certificate = load_certificate(args.path)
    _print(verify_representation_certificate(certificate))
    return 0


def command_verify_tree(args: argparse.Namespace) -> int:
    paths = sorted(
        path
        for path in Path(args.directory).glob("*.json")
        if not path.name.endswith(".schema.json")
    )
    if not paths:
        raise CertificateError("no certificate JSON files found")
    results = []
    for path in paths:
        result = verify_representation_certificate(load_certificate(path))
        results.append({"path": str(path), **result})
    _print({"status": "PASS", "certificates": results})
    return 0


def command_generate_dataset(args: argparse.Namespace) -> int:
    dataset = generate_dataset(
        args.n_min,
        args.n_max,
        certificate_dir=args.certificate_dir,
    )
    write_dataset(dataset, args.output)
    _print(
        {
            "status": "PASS",
            "output": args.output,
            "sha256": dataset["sha256"],
            "records": len(dataset["records"]),
        }
    )
    return 0


def command_verify_dataset(args: argparse.Namespace) -> int:
    with Path(args.path).open("r", encoding="utf-8") as handle:
        dataset = json.load(handle)
    _print(verify_dataset(dataset))
    return 0


def command_verify_label_family(args: argparse.Namespace) -> int:
    certificate = load_lattice_certificate(args.path)
    _print(
        verify_label_family_certificate(certificate, max_exact_states=args.max_states)
    )
    return 0


def command_verify_n2_obs_107(args: argparse.Namespace) -> int:
    certificate = load_lattice_certificate(args.path)
    _print(verify_n2_obs_107_certificate(certificate))
    return 0


def command_audit_n2_obs_107(args: argparse.Namespace) -> int:
    audit = audit_n2_obs_107_range(args.n_min, args.n_max)
    write_json(audit, args.output)
    _print(
        {
            "status": "PASS",
            "output": args.output,
            "first_admissible_failure_n": audit["first_admissible_failure_n"],
            "later_failures": len(audit["later_failures_after_first_admissible"]),
        }
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    verify = subparsers.add_parser("verify", help="verify one representation certificate")
    verify.add_argument("path")
    verify.set_defaults(func=command_verify)

    verify_tree = subparsers.add_parser("verify-tree", help="verify all JSON certificates")
    verify_tree.add_argument("directory")
    verify_tree.set_defaults(func=command_verify_tree)

    generate = subparsers.add_parser("generate-dataset", help="generate exact profiles")
    generate.add_argument("--n-min", type=int, default=1)
    generate.add_argument("--n-max", type=int, default=12)
    generate.add_argument("--output", required=True)
    generate.add_argument("--certificate-dir")
    generate.set_defaults(func=command_generate_dataset)

    replay = subparsers.add_parser("verify-dataset", help="recompute and verify a dataset")
    replay.add_argument("path")
    replay.set_defaults(func=command_verify_dataset)

    label_family = subparsers.add_parser(
        "verify-label-family", help="run exact lattice, residue, and finite-window gates"
    )
    label_family.add_argument("path")
    label_family.add_argument("--max-states", type=int, default=2_000_000)
    label_family.set_defaults(func=command_verify_label_family)

    regression = subparsers.add_parser(
        "verify-n2-obs-107", help="replay the frozen Nova 2 lattice obstruction"
    )
    regression.add_argument("path")
    regression.set_defaults(func=command_verify_n2_obs_107)

    audit = subparsers.add_parser(
        "audit-n2-obs-107", help="audit the frozen obstruction on an exact finite n range"
    )
    audit.add_argument("--n-min", type=int, default=3)
    audit.add_argument("--n-max", type=int, required=True)
    audit.add_argument("--output", required=True)
    audit.set_defaults(func=command_audit_n2_obs_107)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except (
        CertificateError,
        LatticeCertificateError,
        LatticeResourceLimit,
        ValueError,
        RuntimeError,
        AssertionError,
    ) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
