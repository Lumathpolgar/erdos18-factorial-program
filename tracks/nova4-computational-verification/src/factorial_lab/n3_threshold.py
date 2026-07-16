"""Exact finite sweep for Nova 3 request G.

All discrete quantities are exact. Logarithmic margins are screened over the full
range in binary64 and the retained minima are reevaluated with 80-digit Decimal
arithmetic. The finite sweep is not an asymptotic proof or an occupancy theorem.
"""
from __future__ import annotations
from decimal import Decimal, localcontext
import hashlib, heapq, json, math
from pathlib import Path
from typing import Any, Iterable
from .logcert import certified_log_parameter_tables, certified_log_parameters

REPOSITORY="Lumathpolgar/erdos18-factorial-program"
SOURCE_BRANCH="nova/analytic-density"
HANDOFF="N3-HO-N4-002"
HANDOFF_COMMIT="7469dada02fa4caca08ed391ef8b0cb0f1e855b2"
PROOF_FILE="tracks/nova3-analytic-density/proofs/EXPLICIT_PRIME_INTERVAL_AND_CAPACITY.md"
PROOF_FILE_BLOB_SHA="e36daf98db86da16bd5ed8c6c82f43530d745f66"
SANITY_FILE="tracks/nova3-analytic-density/proofs/prime_interval_capacity_sanity.py"
SANITY_FILE_BLOB_SHA="519c900b616a33d95f3b2a8a8dec10d04a0a24f5"
N1_PROOF_FILE="tracks/nova1-factorial-structure/proofs/HIGH_PRIME_MENU_CAPACITY.md"
N1_PROOF_COMMIT="fa11f4b2cb86a2dd791df189ada12757be791804"
N1_PROOF_BLOB_SHA="4255e76ff18f675ae80a0192381070d9a934fc97"
REQUEST_ID="G"
OBJECT_ID="N3-ANA-011"
N_MIN=120_368
N_MAX=1_000_000
DECIMAL_PRECISION=80
FINALIST_COUNT=64
SCREEN_TOLERANCE="1e-9"
SCHEMA="nova4.n3-threshold-sweep.v1"
CLAIM_SCHEMA="nova4.n3-threshold-sweep-claim.v1"

class VerificationError(ValueError):
    pass

def canonical_json(v:Any)->str:
    return json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=True)

def semantic_sha256(v:Any,*,omit:Iterable[str]=("sha256",))->str:
    omitted=set(omit)
    payload={k:x for k,x in v.items() if k not in omitted} if isinstance(v,dict) else v
    return hashlib.sha256(canonical_json(payload).encode()).hexdigest()

def source_metadata()->dict[str,Any]:
    return {"repository":REPOSITORY,"branch":SOURCE_BRANCH,"handoff":HANDOFF,
            "handoff_commit":HANDOFF_COMMIT,"request":REQUEST_ID,"object":OBJECT_ID,
            "proof_file":PROOF_FILE,"proof_file_blob_sha":PROOF_FILE_BLOB_SHA,
            "sanity_file":SANITY_FILE,"sanity_file_blob_sha":SANITY_FILE_BLOB_SHA,
            "imported_n1":{"commit":N1_PROOF_COMMIT,"file":N1_PROOF_FILE,
                           "blob_sha":N1_PROOF_BLOB_SHA,"object":"N1-STR-009"}}

def prime_count_table(limit:int)->list[int]:
    if isinstance(limit,bool) or not isinstance(limit,int) or limit<0:raise ValueError
    sieve=bytearray(b"\x01")*(limit+1)
    if limit>=0:sieve[0]=0
    if limit>=1:sieve[1]=0
    for p in range(2,math.isqrt(limit)+1):
        if sieve[p]:
            start=p*p
            sieve[start:limit+1:p]=b"\x00"*(((limit-start)//p)+1)
    out=[0]*(limit+1); c=0
    for i,flag in enumerate(sieve):c+=int(flag);out[i]=c
    return out

def valuation_two_legendre(n:int)->int:
    total=0; x=n
    while x:
        x//=2;total+=x
    return total

def valuation_two_digit_sum(n:int)->int:
    return n-n.bit_count()

def _push_smallest(heap:list[tuple[float,int]], value:float, n:int)->None:
    item=(-value,n)
    if len(heap)<FINALIST_COUNT:heapq.heappush(heap,item)
    elif value < -heap[0][0]:heapq.heapreplace(heap,item)

def _decimal_row(n:int, pi:list[int], rvals:list[int], mvals:list[int])->dict[str,Any]:
    with localcontext() as ctx:
        ctx.prec=DECIMAL_PRECISION
        dn=Decimal(n); ln=dn.ln(); ln2=Decimal(2).ln()
        count=pi[n]-pi[n//2]
        v2=valuation_two_legendre(n)
        r=rvals[n]; m=mvals[n]; e=r+m; legal=v2//2-1
        exponent=m*(count-1)+r
        target=dn/(Decimal(3)*ln)
        required=Decimal(1)+dn*ln/(Decimal(2)*ln2)
        return {"n":n,"floor_n_over_2":n//2,"pi_n":pi[n],"pi_floor_n_over_2":pi[n//2],
                "upper_half_prime_count":count,"v2_factorial":v2,"binary_digit_sum":n.bit_count(),
                "r_n":r,"M_n":m,"e_M":e,"legal_address_max":legal,
                "address_slack":legal-e,"profile_capacity_exponent":exponent,
                "prime_target":str(+target),"prime_margin":str(+(Decimal(count)-target)),
                "legendre_lower_bound_margin":str(+(ln/ln2+Decimal(1-n.bit_count()))),
                "conservative_required_bits":str(+required),
                "capacity_margin_bits":str(+(Decimal(exponent)-required))}

def _decimal_min(finalists:list[tuple[float,int]], key:str, pi:list[int], rvals:list[int], mvals:list[int]):
    rows=[_decimal_row(n,pi,rvals,mvals) for _,n in finalists]
    rows.sort(key=lambda row:Decimal(row[key]))
    return rows[0],rows[1],str(Decimal(rows[1][key])-Decimal(rows[0][key]))

def build_audit(n_min:int=N_MIN,n_max:int=N_MAX)->dict[str,Any]:
    if n_min!=N_MIN or n_max!=N_MAX:
        raise ValueError(f"request G requires the exact range {N_MIN}..{N_MAX}")
    pi=prime_count_table(n_max)
    rvals,mvals=certified_log_parameter_tables(n_max)
    heaps={"prime":[],"legendre":[],"capacity":[]}
    address_min=10**30; address_ns=[]
    r_transitions=[];m_transitions=[];last_r=None;last_m=None
    for n in range(n_min,n_max+1):
        upper=pi[n]-pi[n//2]
        v_leg=valuation_two_legendre(n);v_digit=valuation_two_digit_sum(n)
        if v_leg!=v_digit:raise AssertionError(f"Legendre mismatch at n={n}")
        r=rvals[n];m=mvals[n]
        if r!=last_r:r_transitions.append([n,r]);last_r=r
        if m!=last_m:m_transitions.append([n,m]);last_m=m
        address=v_leg//2-1-(r+m)
        if address<0:raise AssertionError(f"illegal address at n={n}")
        if address<address_min:address_min=address;address_ns=[n]
        elif address==address_min:address_ns.append(n)
        logn=math.log(n)
        prime_margin=upper-n/(3.0*logn)
        legendre_margin=math.log2(n)+1-n.bit_count()
        exponent=m*(upper-1)+r
        capacity_margin=exponent-(1.0+0.5*n*math.log2(n))
        if prime_margin<0 or legendre_margin<0 or capacity_margin<0:
            raise AssertionError(f"negative margin at n={n}")
        _push_smallest(heaps["prime"],prime_margin,n)
        _push_smallest(heaps["legendre"],legendre_margin,n)
        _push_smallest(heaps["capacity"],capacity_margin,n)
    finalists={k:sorted((-x,n) for x,n in h) for k,h in heaps.items()}
    prime,prime_runner,prime_gap=_decimal_min(finalists["prime"],"prime_margin",pi,rvals,mvals)
    leg,leg_runner,leg_gap=_decimal_min(finalists["legendre"],"legendre_lower_bound_margin",pi,rvals,mvals)
    cap,cap_runner,cap_gap=_decimal_min(finalists["capacity"],"capacity_margin_bits",pi,rvals,mvals)
    tol=Decimal(SCREEN_TOLERANCE)
    for gap in (prime_gap,leg_gap,cap_gap):
        if Decimal(gap)<=tol:raise AssertionError("screening gap is too small")
    first= _decimal_row(n_min,pi,rvals,mvals)
    last = _decimal_row(n_max,pi,rvals,mvals)
    audit={"schema":SCHEMA,"result_class":"finite certificate","source":source_metadata(),
           "range":{"n_min":n_min,"n_max":n_max,"integer_count":n_max-n_min+1,
                    "every_integer_checked":True,"endpoint_semantics":"pi(n/2)=pi(floor(n/2))"},
           "method":{"prime_counts":"exact Eratosthenes prefix table",
                     "v2":"Legendre division cross-checked with n-bit_count(n)",
                     "ceilings":"rigorous rational log intervals and monotone transition tables",
                     "margin_screen":"full binary64 scan followed by 80-digit Decimal finalist replay",
                     "finalists_per_margin":FINALIST_COUNT,"screen_tolerance":SCREEN_TOLERANCE,
                     "finite_only":True},
           "parameter_transitions":{"r_count":len(r_transitions),"M_count":len(m_transitions),
                                    "r_first":r_transitions[0],"r_last":r_transitions[-1],
                                    "M_first":m_transitions[0],"M_last":m_transitions[-1]},
           "minima":{"prime_margin":{"row":prime,"runner_up_n":prime_runner["n"],"runner_up_margin":prime_runner["prime_margin"],"gap":prime_gap},
                     "legendre_lower_bound_margin":{"row":leg,"runner_up_n":leg_runner["n"],"runner_up_margin":leg_runner["legendre_lower_bound_margin"],"gap":leg_gap},
                     "address_slack":{"value":address_min,"minimizing_n":address_ns,"first_n":address_ns[0],"last_n":address_ns[-1]},
                     "capacity_margin_bits":{"row":cap,"runner_up_n":cap_runner["n"],"runner_up_margin":cap_runner["capacity_margin_bits"],"gap":cap_gap}},
           "boundary_rows":{"first":first,"last":last},
           "decision":{"request_G":"ACCEPTED_AS_FINITE_CERTIFICATE",
                       "N3_ANA_011":"FINITE_RANGE_CONFIRMED_THEOREM_DECISION_PENDING_REQUEST_H",
                       "all_prime_checks_pass":True,"all_legendre_checks_pass":True,
                       "all_ceiling_checks_pass":True,"all_address_checks_pass":True,
                       "all_capacity_checks_pass":True},
           "scope":{"not_asymptotic_proof":True,"not_distinct_numerical_sums":True,
                    "not_additive_occupancy":True,"not_factorial_half_range_theorem":True}}
    audit["sha256"]=semantic_sha256(audit)
    return audit

def build_claim(audit:dict[str,Any]|None=None)->dict[str,Any]:
    audit=build_audit() if audit is None else audit
    claim={"schema":CLAIM_SCHEMA,"result_class":"finite threshold sweep certificate",
           "source":source_metadata(),"evidence_sha256":audit["sha256"],
           "claim":{"range":audit["range"],"decision":audit["decision"],
                    "minima":audit["minima"],"finite_only":True}}
    claim["sha256"]=semantic_sha256(claim);return claim

def _eq(a,b,label):
    if a!=b:raise VerificationError(f"{label} mismatch: {a!r} != {b!r}")

def verify_audit(audit):
    _eq(audit.get("schema"),SCHEMA,"schema");_eq(audit.get("source"),source_metadata(),"source")
    _eq(audit.get("sha256"),semantic_sha256(audit),"sha256")
    _eq(audit,build_audit(),"full audit")

def verify_claim(claim,audit=None):
    _eq(claim.get("schema"),CLAIM_SCHEMA,"claim schema");_eq(claim.get("source"),source_metadata(),"claim source")
    _eq(claim.get("sha256"),semantic_sha256(claim),"claim sha256")
    audit=build_audit() if audit is None else audit;verify_audit(audit)
    _eq(claim,build_claim(audit),"full claim")

def load_json(path):
    v=json.loads(Path(path).read_text());
    if not isinstance(v,dict):raise VerificationError("JSON root must be object")
    return v

def write_json(path,value):
    Path(path).write_text(json.dumps(value,indent=2,sort_keys=True)+"\n")
