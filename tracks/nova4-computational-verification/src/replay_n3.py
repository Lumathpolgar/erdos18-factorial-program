#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
from factorial_lab.n3_moments import (
    AnalyticAuditError, audit_range, first_tight_claim,
    verify_audit, verify_local_ceiling_claim, write_json,
)

def main(argv=None):
    parser=argparse.ArgumentParser(description="Replay Nova 3 finite analytic audits")
    sub=parser.add_subparsers(dest="cmd",required=True)
    a=sub.add_parser("audit");a.add_argument("--n-min",type=int,default=2);a.add_argument("--n-max",type=int,default=12);a.add_argument("--output",required=True);a.add_argument("--tight-certificate",required=True)
    v=sub.add_parser("verify");v.add_argument("path")
    c=sub.add_parser("verify-local-claim");c.add_argument("path")
    args=parser.parse_args(argv)
    try:
        if args.cmd=="audit":
            audit=audit_range(args.n_min,args.n_max);write_json(audit,args.output);write_json(first_tight_claim(audit),args.tight_certificate)
            result={"status":"PASS","sha256":audit["sha256"],**audit["totals"]}
        elif args.cmd=="verify":
            result=verify_audit(json.loads(Path(args.path).read_text()))
        else:
            result=verify_local_ceiling_claim(json.loads(Path(args.path).read_text()))
        print(json.dumps(result,sort_keys=True,indent=2));return 0
    except (AnalyticAuditError,KeyError,TypeError,ValueError) as exc:
        print(f"FAIL: {exc}",file=sys.stderr);return 1

if __name__=="__main__": raise SystemExit(main())
