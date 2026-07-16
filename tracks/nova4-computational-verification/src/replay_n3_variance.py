#!/usr/bin/env python3
from __future__ import annotations

import argparse

from factorial_lab.n3_variance_limit import load_json, verify_audit, verify_claim


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    audit_parser = sub.add_parser("verify")
    audit_parser.add_argument("path")

    claim_parser = sub.add_parser("verify-claim")
    claim_parser.add_argument("path")
    claim_parser.add_argument("--audit", required=True)

    args = parser.parse_args()
    if args.command == "verify":
        verify_audit(load_json(args.path))
        print("PASS: N3-ANA-006 variance-limit audit verified")
    else:
        audit = load_json(args.audit)
        verify_claim(load_json(args.path), audit)
        print("PASS: N3-ANA-006 final theorem claim verified")


if __name__ == "__main__":
    main()
