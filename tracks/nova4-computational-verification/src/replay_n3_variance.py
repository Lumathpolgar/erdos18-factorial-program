#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from factorial_lab.n3_variance_limit import (
    VerificationError,
    load_json,
    verify_audit,
    verify_claim,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    audit_parser = sub.add_parser("verify")
    audit_parser.add_argument("path")

    claim_parser = sub.add_parser("verify-claim")
    claim_parser.add_argument("path")
    claim_parser.add_argument("--audit", required=True)

    fixture_parser = sub.add_parser("verify-fixtures")
    fixture_parser.add_argument("directory")
    fixture_parser.add_argument("--audit", required=True)

    args = parser.parse_args()
    if args.command == "verify":
        verify_audit(load_json(args.path))
        print("PASS: N3-ANA-006 variance-limit audit verified")
        return

    audit = load_json(args.audit)
    if args.command == "verify-claim":
        verify_claim(load_json(args.path), audit)
        print("PASS: N3-ANA-006 final theorem claim verified")
        return

    fixture_paths = sorted(Path(args.directory).glob("*.json"))
    if len(fixture_paths) != 5:
        raise VerificationError(
            f"expected five N3-ANA-006 corruption fixtures, found {len(fixture_paths)}"
        )
    for fixture_path in fixture_paths:
        try:
            verify_claim(load_json(fixture_path), audit)
        except VerificationError:
            continue
        raise VerificationError(f"corrupted fixture was accepted: {fixture_path}")
    print("PASS: all five N3-ANA-006 corruption fixtures rejected")


if __name__ == "__main__":
    main()
