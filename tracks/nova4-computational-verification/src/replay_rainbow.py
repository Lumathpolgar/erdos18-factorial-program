"""Standalone replay for Nova 1 reduced-rainbow Study B artifacts."""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
from factorial_lab.n1_rainbow import RainbowCertificationError, audit_range, first_failure_certificate, verify_audit, verify_failure, write_csv, write_json

def _print(x:object)->None: print(json.dumps(x,sort_keys=True,indent=2,ensure_ascii=False))

def do_audit(a:argparse.Namespace)->int:
    result=audit_range(a.n_min,a.n_max);write_json(result,a.output_json);write_csv(result,a.output_csv);failure=first_failure_certificate(result);write_json(failure,a.output_failure)
    _print({"status":"PASS","output_json":a.output_json,"output_csv":a.output_csv,"output_failure":a.output_failure,"sha256":result["sha256"],"case_count":len(result["cases"]),"first_failure":result["first_failure"]});return 0

def do_verify(a:argparse.Namespace)->int:
    _print(verify_audit(json.loads(Path(a.path).read_text())));return 0

def do_failure(a:argparse.Namespace)->int:
    _print(verify_failure(json.loads(Path(a.path).read_text())));return 0

def parser()->argparse.ArgumentParser:
    p=argparse.ArgumentParser(description=__doc__);s=p.add_subparsers(dest="command",required=True)
    q=s.add_parser("audit");q.add_argument("--n-min",type=int,default=20);q.add_argument("--n-max",type=int,default=80);q.add_argument("--output-json",required=True);q.add_argument("--output-csv",required=True);q.add_argument("--output-failure",required=True);q.set_defaults(func=do_audit)
    q=s.add_parser("verify");q.add_argument("path");q.set_defaults(func=do_verify)
    q=s.add_parser("verify-failure");q.add_argument("path");q.set_defaults(func=do_failure)
    return p

def main(argv:list[str]|None=None)->int:
    a=parser().parse_args(argv)
    try:return a.func(a)
    except (RainbowCertificationError,ValueError,AssertionError) as e: print(f"FAIL: {e}",file=sys.stderr);return 1

if __name__=="__main__":raise SystemExit(main())
