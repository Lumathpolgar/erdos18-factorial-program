#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from factorial_lab.n3_scale import (
    ScaleEvidenceError,
    build_evidence,
    verify_evidence,
    write_csvs,
    write_json,
)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Generate and replay Nova 3 scale evidence")
    sub = parser.add_subparsers(dest="cmd", required=True)
    generate = sub.add_parser("generate")
    generate.add_argument("--output-json", required=True)
    generate.add_argument("--scale-csv", required=True)
    generate.add_argument("--tail-csv", required=True)
    generate.add_argument("--proxy-prime-limit", type=int, default=1_000_000)
    verify = sub.add_parser("verify")
    verify.add_argument("path")
    args = parser.parse_args(argv)
    try:
        if args.cmd == "generate":
            evidence = build_evidence(proxy_prime_limit=args.proxy_prime_limit)
            write_json(evidence, args.output_json)
            write_csvs(evidence, args.scale_csv, args.tail_csv)
            result = {
                "status": "PASS",
                "sha256": evidence["sha256"],
                "scale_rows": len(evidence["scale_rows"]),
                "tail_rows": len(evidence["high_prime_tail_rows"]),
                "theorem_path_rows": len(evidence["theorem_path_rows"]),
            }
        else:
            result = verify_evidence(
                json.loads(Path(args.path).read_text(encoding="utf-8"))
            )
        print(json.dumps(result, sort_keys=True, indent=2))
        return 0
    except (ScaleEvidenceError, KeyError, TypeError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
