"""Exact Nova 1 Study B reduced-rainbow audit."""
from __future__ import annotations
import csv, hashlib, json
from fractions import Fraction
from math import factorial, gcd, isqrt, prod
from pathlib import Path
from typing import Any
from .arithmetic import is_divisor_of_factorial, prime_sieve
from .logcert import natural_log_bounds

SCHEMA="nova4.n1-reduced-rainbow.v1"
FAIL_SCHEMA="nova4.n1-reduced-rainbow-first-failure.v1"
SOURCE={"repository":"Lumathpolgar/erdos18-factorial-program","branch":"nova/factorial-structure","commit":"fa11f4b2cb86a2dd791df189ada12757be791804","handoff":"N1-HO-N4-001","study":"B"}
CAP=10_000_000

class RainbowCertificationError(ValueError): pass

def _int(name:str,x:Any,lo:int=0)->int:
    if isinstance(x,bool) or not isinstance(x,int) or x<lo: raise RainbowCertificationError(f"invalid {name}")
    return x

def _ceil(q:Fraction)->int: return -((-q.numerator)//q.denominator)

def certified_ceil_log(n:int)->int:
    _int("n",n,1)
    for k in (8,12,16,24,32,48,64,96):
        a,b=natural_log_bounds(n,terms=k); x,y=_ceil(a),_ceil(b)
        if x==y:return x
    raise RainbowCertificationError(f"uncertified ceil(log({n}))")

def v2_factorial(n:int)->int:
    s=0
    while n:n//=2;s+=n
    return s

def _products(ps:list[int],limit:int)->list[int]:
    out=[1]
    for p in ps: out += [x*p for x in out if x<=limit//p]
    return sorted(set(out))

def build_family(n:int,primes:list[int]|None=None)->dict[str,Any]:
    _int("n",n,2); primes=primes or prime_sieve(n)
    V=v2_factorial(n); r=max(1,min(certified_ceil_log(n),V//4)); M=max(0,min(12,V//2-r-1))
    X=isqrt(factorial(n)); T=min(X,CAP); hp=[p for p in primes if p<=n<2*p]; P=prod(hp)
    H=[x for x in _products(hp,isqrt(P)) if x>1]
    layers=[]
    for t in range(1,M+1):
        e=r+t; terms=[(1<<e)*u for u in H if (1<<e)*u<=X]
        layers.append({"layer":t,"address":e,"terms":terms,"bounded_terms":[x for x in terms if x<=T]})
    f={"n":n,"x_n":X,"target_cap":T,"v2_factorial":V,"ceil_log_n":certified_ceil_log(n),"r_star":r,"m_star":M,"high_primes":hp,"p_n":P,"high_core_menu":H,"layers":layers}
    _verify_family(f); return f

def _verify_family(f:dict[str,Any])->None:
    addresses=set(); seen=set()
    for i,L in enumerate(f["layers"],1):
        if L["layer"]!=i or L["address"]!=f["r_star"]+i or L["address"] in addresses: raise RainbowCertificationError("bad address")
        addresses.add(L["address"]); local=set()
        for x in L["terms"]:
            if x<=0 or x>f["x_n"] or x&(x-1)==0 or x in local or x in seen: raise RainbowCertificationError("illegal or duplicate term")
            if not is_divisor_of_factorial(x,f["n"]) or (x&-x).bit_length()-1!=L["address"]: raise RainbowCertificationError("term fails factorial/address check")
            local.add(x);seen.add(x)
        if L["bounded_terms"]!=[x for x in L["terms"] if x<=f["target_cap"]]: raise RainbowCertificationError("bad trimming")

def _support(f:dict[str,Any])->tuple[int,list[int]]:
    R=1; before=[]; mask=(1<<(f["target_cap"]+1))-1
    for L in f["layers"]:
        before.append(R); old=R; new=old
        for x in L["bounded_terms"]:new|=old<<x
        R=new&mask
    return R,before

def verify_witness(target:int,w:list[dict[str,int]],f:dict[str,Any])->None:
    by={L["layer"]:L for L in f["layers"]}; layers=set();terms=set();total=0
    for e in w:
        i=_int("layer",e.get("layer"),1);a=_int("address",e.get("address"));x=_int("term",e.get("term"),1)
        if i in layers or x in terms or i not in by or a!=by[i]["address"] or x not in by[i]["terms"]:raise RainbowCertificationError("invalid witness")
        layers.add(i);terms.add(x);total+=x
    if total!=target:raise RainbowCertificationError("wrong witness sum")

def _witness(target:int,f:dict[str,Any],before:list[int])->list[dict[str,int]]:
    rem=target;w=[]
    for j in range(len(f["layers"])-1,-1,-1):
        old=before[j]
        if (old>>rem)&1:continue
        x=next((x for x in f["layers"][j]["bounded_terms"] if x<=rem and (old>>(rem-x))&1),None)
        if x is None:raise RainbowCertificationError("witness reconstruction failed")
        w.append({"layer":j+1,"address":f["layers"][j]["address"],"term":x});rem-=x
    if rem:raise RainbowCertificationError("witness remainder")
    w.sort(key=lambda z:z["layer"]);verify_witness(target,w,f);return w

def _gaps(bits:int,T:int,radius:int)->dict[str,Any]:
    data=bits.to_bytes((T+8)//8,"little");run=0;prev=-1;mx=0;events=[];first=None
    for bi,b in enumerate(data):
        width=min(8,T+1-8*bi)
        if b==0:run+=width;continue
        for j in range(width):
            pos=8*bi+j
            if b>>j&1:
                if run>mx:mx=run;events.append({"gap":run,"target":pos-1,"predecessor_reachable":prev,"next_reachable":pos})
                if first is None and run>radius:first={"target":prev+radius+1,"predecessor_reachable":prev,"gap":radius+1}
                run=0;prev=pos
            else:run+=1
    if run>mx:mx=run;events.append({"gap":run,"target":T,"predecessor_reachable":prev,"next_reachable":None})
    if first is None and run>radius:first={"target":prev+radius+1,"predecessor_reachable":prev,"gap":radius+1}
    return {"maximum_downward_gap":mx,"first":first,"events":events}

def _rot(mask:int,s:int,q:int)->int:
    s%=q;full=(1<<q)-1
    return mask&full if not s else ((mask<<s)|(mask>>(q-s)))&full

def _residues(layers:list[dict[str,Any]])->dict[str,Any]:
    out={}
    for q in range(2,65):
        m=1
        for L in layers:
            old=m;m=old
            for r in {x%q for x in L["terms"]}:m|=_rot(old,r,q)
        occ=[r for r in range(q) if m>>r&1]
        out[str(q)]={"occupied_count":len(occ),"occupied_residues":occ,"missing_residues":[r for r in range(q) if not(m>>r&1)]}
    return out

def _ratio(a:int,b:int)->dict[str,int]:
    d=gcd(a,b);return {"numerator":a,"denominator":b,"reduced_numerator":a//d,"reduced_denominator":b//d}

def audit_case(n:int,primes:list[int]|None=None)->dict[str,Any]:
    f=build_family(n,primes);bits,before=_support(f);radius=(1<<f["r_star"])-1;g=_gaps(bits,f["target_cap"],radius)
    events=[]
    for e in g["events"]:events.append({**e,"predecessor_witness":_witness(e["predecessor_reachable"],f,before) if e["predecessor_reachable"]>=0 else []})
    first=g["first"]
    if first:first={**first,"window":[first["target"]-radius,first["target"]],"predecessor_witness":_witness(first["predecessor_reachable"],f,before) if first["predecessor_reachable"]>=0 else []}
    formal=prod(len(L["terms"])+1 for L in f["layers"]);bounded=prod(len(L["bounded_terms"])+1 for L in f["layers"]);distinct=bits.bit_count()
    term_gcd=0
    for L in f["layers"]:
        for x in L["terms"]:term_gcd=gcd(term_gcd,x)
    mod=1<<(f["r_star"]+1);target=1<<f["r_star"]
    lattice={"modulus":mod,"all_terms_divisible_by_modulus":all(x%mod==0 for L in f["layers"] for x in L["terms"]),"target":target,"window":[1,target],"window_contains_lattice_point":False,"target_within_audited_range":target<=f["target_cap"]}
    return {"n":n,"x_n":f["x_n"],"target_cap":f["target_cap"],"v2_factorial":f["v2_factorial"],"ceil_log_n":f["ceil_log_n"],"r_star":f["r_star"],"m_star":f["m_star"],"addresses":[L["address"] for L in f["layers"]],"high_primes":f["high_primes"],"p_n":f["p_n"],"high_core_menu_size":len(f["high_core_menu"]),"high_core_menu":f["high_core_menu"],"layer_sizes":[len(L["terms"]) for L in f["layers"]],"layer_sizes_up_to_target_cap":[len(L["bounded_terms"]) for L in f["layers"]],"formal_profile_count":formal,"target_cap_menu_profile_count":bounded,"distinct_reachable_sums_up_to_target_cap":distinct,"formal_profile_compression_ratio":_ratio(formal-distinct,formal),"target_cap_menu_compression_ratio":_ratio(bounded-distinct,bounded),"support_density":_ratio(distinct,f["target_cap"]+1),"gcd_nonzero_layer_terms":term_gcd,"independent_lattice_obstruction":lattice,"residue_occupancy":_residues(f["layers"]),"maximum_downward_gap":g["maximum_downward_gap"],"correction_radius":radius,"first_target_exceeding_radius":first,"record_gap_events":events,"first_failure":{"type":"occupancy","target":first["target"],"window":first["window"],"reason":"downward gap exceeds 2^r_star-1"} if first else None}

def _sha(x:dict[str,Any])->str:
    y={k:v for k,v in x.items() if k!="sha256"};return hashlib.sha256(json.dumps(y,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def audit_range(n_min:int=20,n_max:int=80)->dict[str,Any]:
    ps=prime_sieve(n_max);cases=[audit_case(n,ps) for n in range(n_min,n_max+1)];fail=[c for c in cases if c["first_failure"]]
    a={"schema":SCHEMA,"result_class":"computational evidence","source":SOURCE,"range":{"n_min":n_min,"n_max":n_max,"case_count":len(cases)},"method":{"arithmetic":"exact integers and rational logarithm bounds","support":"exact target-truncated zero-or-one-per-layer bitset","witnesses":"backtracking through stored pre-layer support","residues":"exact cyclic masks for moduli 2 through 64"},"cases":cases,"first_failure":{"n":fail[0]["n"],**fail[0]["first_failure"]} if fail else None,"failure_count":len(fail),"all_cases_have_occupancy_failure":len(fail)==len(cases)};a["sha256"]=_sha(a);return a

def verify_audit(a:dict[str,Any])->dict[str,Any]:
    if a.get("schema")!=SCHEMA or a.get("source")!=SOURCE:raise RainbowCertificationError("metadata mismatch")
    r=a.get("range",{});expected=audit_range(_int("n_min",r.get("n_min"),2),_int("n_max",r.get("n_max"),2))
    if a!=expected:raise RainbowCertificationError("audit mismatch")
    return {"status":"PASS","schema":SCHEMA,"case_count":len(expected["cases"]),"first_failure":expected["first_failure"],"sha256":expected["sha256"]}

def first_failure_certificate(a:dict[str,Any])->dict[str,Any]:
    first=a["first_failure"];c=next(x for x in a["cases"] if x["n"]==first["n"]);f=c["first_target_exceeding_radius"]
    z={"schema":FAIL_SCHEMA,"result_class":"disproved finite claim","source":SOURCE,"audit_sha256":a["sha256"],"claimed":{"n":c["n"],"r_star":c["r_star"],"m_star":c["m_star"],"addresses":c["addresses"],"high_primes":c["high_primes"],"high_core_menu":c["high_core_menu"],"layer_sizes":c["layer_sizes"],"gcd_nonzero_layer_terms":c["gcd_nonzero_layer_terms"],"target":f["target"],"window":f["window"],"correction_radius":c["correction_radius"],"predecessor_reachable":f["predecessor_reachable"],"predecessor_witness":f["predecessor_witness"],"independent_lattice_obstruction":c["independent_lattice_obstruction"]}};z["sha256"]=_sha(z);return z

def verify_failure(z:dict[str,Any])->dict[str,Any]:
    if z.get("schema")!=FAIL_SCHEMA or z.get("source")!=SOURCE or z.get("sha256")!=_sha(z):raise RainbowCertificationError("failure metadata/checksum mismatch")
    n=_int("n",z.get("claimed",{}).get("n"),2);expected=first_failure_certificate(audit_range(n,n))
    if z["claimed"]!=expected["claimed"]:raise RainbowCertificationError("failure claim mismatch")
    return {"status":"PASS","schema":FAIL_SCHEMA,"n":n,"target":z["claimed"]["target"],"window":z["claimed"]["window"],"sha256":z["sha256"]}

def write_json(x:dict[str,Any],path:str|Path)->None:
    p=Path(path);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False)+"\n")

def write_csv(a:dict[str,Any],path:str|Path)->None:
    p=Path(path);p.parent.mkdir(parents=True,exist_ok=True);fields=["n","x_n","target_cap","v2_factorial","r_star","m_star","high_core_menu_size","layer_sizes","layer_sizes_up_to_target_cap","formal_profile_count","distinct_reachable_sums_up_to_target_cap","gcd_nonzero_layer_terms","maximum_downward_gap","correction_radius","first_failure_target"]
    with p.open("w",newline="") as h:
        w=csv.DictWriter(h,fieldnames=fields);w.writeheader()
        for c in a["cases"]:w.writerow({k:(";".join(map(str,c[k])) if isinstance(c.get(k),list) else (c["first_target_exceeding_radius"]["target"] if k=="first_failure_target" else c[k])) for k in fields})
