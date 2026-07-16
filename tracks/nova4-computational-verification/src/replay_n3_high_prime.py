#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from factorial_lab.n3_high_prime import (
    VerificationError,
    load_json,
    verify_audit,
    verify_claim_008,
    verify_claim_009,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    p_audit = sub.add_parser("verify")
    p_audit.add_argument("path")
    p_008 = sub.add_parser("verify-008")
    p_008.add_argument("path")
    p_008.add_argument("--audit", required=True)
    p_009 = sub.add_parser("verify-009")
    p_009.add_argument("path")
    p_009.add_argument("--audit", required=True)
    p_fixtures = sub.add_parser("verify-fixtures")
    p_fixtures.add_argument("directory")
    p_fixtures.add_argument("--audit", required=True)
    args = parser.parse_args()

    if args.command == "verify":
        verify_audit(load_json(args.path))
        print("PASS: N3-ANA-008/009 high-prime audit verified")
        return

    audit = load_json(args.audit)
    if args.command == "verify-008":
        verify_claim_008(load_json(args.path), audit)
        print("PASS: N3-ANA-008 final claim verified")
    elif args.command == "verify-009":
        verify_claim_009(load_json(args.path), audit)
        print("PASS: N3-ANA-009 final claim verified")
    else:
        files = sorted(Path(args.directory).glob("*.json"))
        if not files:
            raise SystemExit("no fixture files found")
        rejected = 0
        for path in files:
            value = load_json(path)
            try:
                if value.get("schema", "").endswith("008-final-claim.v1"):
                    verify_claim_008(value, audit)
                elif value.get("schema", "").endswith("009-final-claim.v1"):
                    verify_claim_009(value, audit)
                else:
                    raise VerificationError("unknown fixture schema")
            except VerificationError:
                rejected += 1
            else:
                raise SystemExit(f"fixture unexpectedly accepted: {path.name}")
        print(f"PASS: rejected {rejected} committed high-prime corruption fixtures")


if __name__ == "__main__":
    main()
