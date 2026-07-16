#!/usr/bin/env python3
# HAMMOCK HARDENING H3 (partial) — independent reconstruction of the type-(i) star.
# KEY REDUCTION: the type-(i) B3 star does NOT need the 8-variable / q^8 ambient (43M at q=9).
# It factors as (B3 block on 6 vars: 6 sheets) x (trivial pair: 1 free coord). Radicality /
# Letter-Hilbert give the block ideal as a COMPLETE INTERSECTION of degrees 1,2,3:
#   g1=e1(a)+e1(b), g2=e2(a)-e2(b), g3=e3(a)+e3(b),   a={y0,y1,y2}, b={y3,y4,y5}.
# Block graded census via per-degree rank of the multiplication map mod m^[q]=(y_i^q);
# star census = trivial-pair convolution;  A_star_total = q * B(q).
# VALIDATED at q=3 against the log's star census. This reduces the q=9 star measurement
# from an 8-variable 43M computation to a light 6-variable CI computation.
from itertools import combinations, product
from collections import defaultdict
def esym(vars_, j):
    t=defaultdict(int)
    for S in combinations(vars_,j):
        e=[0]*6
        for v in S: e[v]+=1
        t[tuple(e)]=(t[tuple(e)]+1)%3
    return {k:v for k,v in t.items() if v}
A=[0,1,2]; B=[3,4,5]
def addp(p,qq,s=1):
    r=defaultdict(int)
    for k,v in p.items(): r[k]=(r[k]+v)%3
    for k,v in qq.items(): r[k]=(r[k]+s*v)%3
    return {k:v%3 for k,v in r.items() if v%3}
gens=[(1,addp(esym(A,1),esym(B,1),1)),(2,addp(esym(A,2),esym(B,2),-1)),(3,addp(esym(A,3),esym(B,3),1))]
def block_HF(q):
    monsby=defaultdict(list)
    for m in product(range(q),repeat=6): monsby[sum(m)].append(m)
    HF={}
    for d in sorted(monsby):
        md=monsby[d]; idx={m:i for i,m in enumerate(md)}; piv={}; rank=0
        for (dg,g) in gens:
            if d-dg<0: continue
            for beta in monsby[d-dg]:
                vv=defaultdict(int)
                for mono,c in g.items():
                    e=tuple(beta[i]+mono[i] for i in range(6))
                    if all(x<q for x in e): vv[e]=(vv[e]+c)%3
                vv={idx[k]:v for k,v in vv.items() if v and k in idx}
                while vv:
                    lead=max(vv)
                    if lead in piv:
                        pv=piv[lead]; cc=vv[lead]
                        for k,val in pv.items():
                            nv=(vv.get(k,0)-cc*val)%3
                            if nv: vv[k]=nv
                            elif k in vv: del vv[k]
                    else: break
                if vv:
                    lead=max(vv); ivv=1 if vv[lead]==1 else 2
                    piv[lead]={k:(val*ivv)%3 for k,val in vv.items()}; rank+=1
        HF[d]=len(md)-rank
    return HF
def star_from_block(HF,q):
    top=max(d for d in HF if HF[d]>0)
    star=[sum(HF.get(d-i,0) for i in range(q)) for d in range(top+q)]
    while star and star[-1]==0: star.pop()
    return star
if __name__=="__main__":
    for q in (3,):   # q=9 is a light M2 / longer-Python run; q=3 validates the method here
        HF=block_HF(q); B=sum(HF.values()); star=star_from_block(HF,q)
        print(f"q={q}: block B(q)={B} (law 6q^3-9q^2+4q={6*q**3-9*q**2+4*q}); "
              f"A_star={sum(star)} (law 6q^4-9q^3+4q^2={6*q**4-9*q**3+4*q**2})")
        print(f"      star census = {star}")
        print(f"      log census  = [1, 6, 20, 43, 64, 67, 49, 23, 6]  match={star==[1,6,20,43,64,67,49,23,6]}")
