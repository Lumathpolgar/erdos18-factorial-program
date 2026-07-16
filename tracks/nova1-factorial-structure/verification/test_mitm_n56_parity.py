#!/usr/bin/env python3
from __future__ import annotations
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
import csv
getcontext().prec=70
HERE=Path(__file__).resolve().parent
PRIMARY=HERE/'full_core_n56_mitm_mask98.txt'
ALTERNATE=HERE/'full_core_n56_mitm_mask33.txt'
EFFECTIVE=HERE/'effective_carrier_n51_n56.csv'
GAPS=HERE/'blocking_gap_ratios_n51_n56.csv'
IGNORE={'mitm_partition_mask','mitm_rows','mitm_columns','maximum_heap'}
def parse(path:Path):
    fields={}; layers=[]
    for line in path.read_text().splitlines():
        if line.startswith('layer='):
            layers.append({k:v for k,v in (part.split('=',1) for part in line.split(','))})
        elif '=' in line:
            k,v=line.split('=',1);fields[k]=v
    return fields,layers
def canonical(path:Path):
    out=[]
    for line in path.read_text().splitlines():
        if '=' in line and line.split('=',1)[0] in IGNORE:continue
        out.append(line)
    return out
def decfrac(x:Fraction)->Decimal:return Decimal(x.numerator)/Decimal(x.denominator)
def root(x:Fraction,n:int)->Decimal:return (decfrac(x).ln()/Decimal(n)).exp()
pf,pl=parse(PRIMARY);af,al=parse(ALTERNATE)
assert canonical(PRIMARY)==canonical(ALTERNATE)
assert pf['n']=='56' and pf['r']=='17' and pf['M']=='260' and pf['v2_factorial']=='53'
assert pf['total_odd_core_divisor_count']=='503193600'
assert pf['emitted_until_certificate']=='411604587'
assert pf['layers_used']=='7' and pf['term_bound']=='24'
assert pf['margin']=='2123056480890000163585785602493899728'
assert [int(x['connected_count']) for x in pl]==[90625,1870175,18876460,95201963,252731752,404825440,411604587]
Y=int(pf['Y']);W=int(pf['W']);L=int(pf['layers_used']);P=int(pf['connected_prefix_product'])
Fprev=W+1;prod_b=Fraction(1,1);parity=Fraction(1,1);amps=[];etas=[]
for row in pl:
    s=int(row['scale']);D=int(row['gap_threshold']);U=int(row['connected_max_core']);K=int(row['connected_count']);E=int(row['carrier_endpoint']);F=E+W+1
    prod_b*=Fraction(F,Fprev*(K+1))
    parity*=Fraction(D+2*K,D+1)
    amps.append(Fraction(U,2*K-1));etas.append(Fraction(U,K*D));Fprev=F
R=Fraction(Y+1,W+1)
tilde=root(Fraction(P,1)/R,L);B=root(prod_b,L);Delta=root(Fraction(Fprev,Y+1),L);parity_root=root(parity/R,L)
assert abs(tilde-Decimal('673.791460795324'))<Decimal('1e-12')
assert abs(B-Decimal('0.001530254006653'))<Decimal('1e-15')
assert abs(Delta-Decimal('1.031072082530349'))<Decimal('1e-15')
assert abs(tilde*B-Delta)<Decimal('1e-60')
assert abs(parity_root-Decimal('0.0000307763983342963'))<Decimal('1e-19')
F6=int(pl[5]['carrier_endpoint'])+W+1
assert F6<Y+1 and Fprev>=Y+1
with EFFECTIVE.open() as handle:
    rows=list(csv.DictReader(handle))
assert rows[-1]['n']=='56' and rows[-1]['layers']=='7'
max_ratio=Fraction(0,1);where=None
with GAPS.open() as handle:
    for row in csv.DictReader(handle):
        ratio=Fraction(int(row['first_blocking_gap']),int(row['gap_threshold']))
        if ratio>max_ratio:max_ratio=ratio;where=(int(row['n']),int(row['layer']))
assert where==(51,4)
assert max_ratio<Fraction(1108,1000)
print('PASS exact n=56')
print('PASS alternate partition n=56')
print('PASS seven-layer transition and term bound 24')
print('PASS effective factorization through n=56')
print('PASS parity-only deficit diagnostic')
print('PASS finite first-blocking-gap ratio below 1.108 through n=56')
print('PASS all n=56 parity-span carrier checks')
