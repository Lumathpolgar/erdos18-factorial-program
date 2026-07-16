#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
from factorial_lab.n3_recurrence import (
    BLOCKS, N_VALUES, Q_MAX, Q_MIN, TOP_K, RecurrenceEvidenceError,
    build_evidence, candidate_certificate, verify_candidate, verify_evidence,
    write_csv, write_json,
)

def main(argv=None):
    parser=argparse.ArgumentParser(description="Replay Nova 3 bounded characteristic recurrence evidence")
    sub=parser.add_subparsers(dest="cmd",required=True)
    a=sub.add_parser("audit")
    a.add_argument("--output",required=True);a.add_argument("--block-csv",required=True);a.add_argument("--best-csv",required=True);a.add_argument("--candidate",required=True)
    a.add_argument("--q-min",type=int,default=Q_MIN);a.add_argument("--q-max",type=int,default=Q_MAX);a.add_argument("--top-k",type=int,default=TOP_K)
    v=sub.add_parser("verify");v.add_argument("path")
    c=sub.add_parser("verify-candidate");c.add_argument("path")
    args=parser.parse_args(argv)
    try:
        if args.cmd=="audit":
            blocks=BLOCKS if (args.q_min,args.q_max)==(Q_MIN,Q_MAX) else ((args.q_min,args.q_max),)
            evidence=build_evidence(N_VALUES,q_min=args.q_min,q_max=args.q_max,blocks=blocks,top_k=args.top_k)
            write_json(evidence,args.output);write_csv(evidence["block_rows"],args.block_csv);write_csv(evidence["best_rows"],args.best_csv);write_json(candidate_certificate(evidence,12),args.candidate)
            result={"status":"PASS","sha256":evidence["sha256"],**evidence["totals"],"q_count":evidence["search"]["q_count"]}
        elif args.cmd=="verify":
            result=verify_evidence(json.loads(Path(args.path).read_text(encoding="utf-8")))
        else:
            result=verify_candidate(json.loads(Path(args.path).read_text(encoding="utf-8")))
        print(json.dumps(result,sort_keys=True,indent=2));return 0
    except (RecurrenceEvidenceError,KeyError,TypeError,ValueError) as exc:
        print(f"FAIL: {exc}",file=sys.stderr);return 1

if __name__=="__main__": raise SystemExit(main())
