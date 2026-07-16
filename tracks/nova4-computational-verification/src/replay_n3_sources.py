#!/usr/bin/env python3
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys

from factorial_lab.n3_sources import (
    SourceAuditError,
    build_audit,
    compatibility_claim,
    verify_audit,
    verify_claim,
    write_json,
)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Replay Nova 3 restricted-source compatibility audit")
    sub = parser.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("generate")
    g.add_argument("--output", required=True)
    g.add_argument("--claim", required=True)
    v = sub.add_parser("verify")
    v.add_argument("path")
    c = sub.add_parser("verify-claim")
    c.add_argument("path")
    args = parser.parse_args(argv)
    try:
        if args.cmd == "generate":
            audit = build_audit()
            claim = compatibility_claim(audit)
            write_json(audit, args.output)
            write_json(claim, args.claim)
            result = {"status": "PASS", "sha256": audit["sha256"], "claim_sha256": claim["sha256"]}
        elif args.cmd == "verify":
            result = verify_audit(json.loads(Path(args.path).read_text(encoding="utf-8")))
        else:
            result = verify_claim(json.loads(Path(args.path).read_text(encoding="utf-8")))
        print(json.dumps(result, sort_keys=True, indent=2))
        return 0
    except (SourceAuditError, KeyError, TypeError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
