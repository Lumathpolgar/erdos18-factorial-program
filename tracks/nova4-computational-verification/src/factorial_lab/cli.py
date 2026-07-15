"""Standalone replay interface for Nova 4 artifacts."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .certificates import CertificateError, load_certificate, verify_representation_certificate
from .dataset import generate_dataset, verify_dataset, write_dataset


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
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except (CertificateError, ValueError, RuntimeError, AssertionError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
