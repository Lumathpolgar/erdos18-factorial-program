#!/usr/bin/env python3
import argparse
from factorial_lab.n3_threshold import build_audit,build_claim,load_json,verify_audit,verify_claim,write_json
p=argparse.ArgumentParser();s=p.add_subparsers(dest='cmd',required=True)
a=s.add_parser('generate');a.add_argument('--audit',required=True);a.add_argument('--claim',required=True)
a=s.add_parser('verify');a.add_argument('path')
a=s.add_parser('verify-claim');a.add_argument('path');a.add_argument('--audit')
x=p.parse_args()
if x.cmd=='generate':
    audit=build_audit();claim=build_claim(audit);write_json(x.audit,audit);write_json(x.claim,claim);print(audit['sha256']);print(claim['sha256'])
elif x.cmd=='verify':verify_audit(load_json(x.path));print('PASS')
else:verify_claim(load_json(x.path),load_json(x.audit) if x.audit else None);print('PASS')
