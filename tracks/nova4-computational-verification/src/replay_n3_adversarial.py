#!/usr/bin/env python3
from __future__ import annotations

import argparse

from factorial_lab.n3_adversarial import (
    load_json,
    verify_audit,
    verify_claim,
    verify_contract,
    verify_fixture_directory,
)

parser = argparse.ArgumentParser()
sub = parser.add_subparsers(dest="command", required=True)
for name in ("verify", "verify-claim", "verify-contract"):
    child = sub.add_parser(name)
    child.add_argument("path")
child = sub.add_parser("verify-fixtures")
child.add_argument("directory")
args = parser.parse_args()

if args.command == "verify":
    verify_audit(load_json(args.path))
elif args.command == "verify-claim":
    verify_claim(load_json(args.path))
elif args.command == "verify-contract":
    verify_contract(load_json(args.path))
else:
    verify_fixture_directory(args.directory)
print("PASS")
