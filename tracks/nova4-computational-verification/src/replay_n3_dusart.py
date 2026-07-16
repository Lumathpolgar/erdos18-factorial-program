#!/usr/bin/env python3
from __future__ import annotations

import argparse

from factorial_lab.n3_dusart import (
    build_audit,
    build_claim,
    dump_json,
    load_json,
    verify_audit,
    verify_claim,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Replay Nova 3 Dusart source audit")
    sub = parser.add_subparsers(dest="command", required=True)

    generate = sub.add_parser("generate")
    generate.add_argument("--audit", required=True)
    generate.add_argument("--claim", required=True)

    verify = sub.add_parser("verify")
    verify.add_argument("audit")

    verify_claim_parser = sub.add_parser("verify-claim")
    verify_claim_parser.add_argument("claim")
    verify_claim_parser.add_argument("--audit")

    args = parser.parse_args()
    if args.command == "generate":
        audit = build_audit()
        claim = build_claim(audit)
        dump_json(args.audit, audit)
        dump_json(args.claim, claim)
        print(audit["sha256"])
        print(claim["sha256"])
    elif args.command == "verify":
        verify_audit(load_json(args.audit))
        print("valid")
    elif args.command == "verify-claim":
        audit = load_json(args.audit) if args.audit else None
        verify_claim(load_json(args.claim), audit)
        print("valid")


if __name__ == "__main__":
    main()
