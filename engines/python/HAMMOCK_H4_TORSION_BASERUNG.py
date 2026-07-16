#!/usr/bin/env python3
# HAMMOCK HARDENING H4 — TORSION CERTIFICATE at the base rung + independent A3(3).
# G_3 = mult-by-(e1,e3,e5,e7) into S/m^[3] (ambient 3^8=6561), 0/1 coefficients.
# A3(3)=6561-rank(G_3). Compare rank over F3 vs over Q (proxy prime): equal ranks
# => no 3-torsion rank-drop; floor tight; A3(3) re-derived independently of Macaulay2.
from itertools import combinations
from collections import defaultdict
N=8; Q=3; pow3=[Q**i for i in range(N)]; AMB=Q**N
def decode(idx):
    e=[]
    for i in range(N): e.append(idx%Q); idx//=Q
    return e
def encode(e): return sum(e[i]*pow3[i] for i in range(N))
esupp={j:list(combinations(range(N),j)) for j in (1,3,5,7)}
def image_vectors(mod):
    for idx in range(AMB):
        e=decode(idx); free=set(i for i in range(N) if e[i]<=1)
        for j in (1,3,5,7):
            vec=defaultdict(int)
            for T in esupp[j]:
                if all(t in free for t in T):
                    e2=e[:]
                    for t in T: e2[t]+=1
                    vec[encode(e2)]=(vec[encode(e2)]+1)%mod
            vec={k:v for k,v in vec.items() if v}
            if vec: yield vec
def modrank(mod):
    piv={}; rank=0
    for v in image_vectors(mod):
        vv=dict(v)
        while vv:
            lead=max(vv)
            if lead in piv:
                pv=piv[lead]; c=vv[lead]
                for k,val in pv.items():
                    nv=(vv.get(k,0)-c*val)%mod
                    if nv: vv[k]=nv
                    elif k in vv: del vv[k]
            else: break
        if vv:
            lead=max(vv); ivv=pow(vv[lead],mod-2,mod)
            piv[lead]={k:(val*ivv)%mod for k,val in vv.items()}; rank+=1
    return rank
r3=modrank(3); rp=modrank(1000003)
print(f"rank_F3={r3}  rank_Q={rp}  A3(3)=6561-rank_F3={AMB-r3}  equal_ranks={r3==rp}")
