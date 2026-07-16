#!/usr/bin/env python3
# HAMMOCK HARDENING H2 — independent check of the G2 level-1 nerve structure (D3).
# (a) extract a REAL type-(i) B3 star (codim-2 flat, star-size 6) from the arrangement;
# (b) verify its nerve is K(3,3): |V|=6,|E|=9, bipartite 3+3, b1=4;
# (c) two-term Cech complex C0->C1 over O(L)_f (h=f+1): confirm dim H1 = b1*h_L = 4(f+1);
# (d) brute-force point count of the 6-sheet union over F3 = A_star(3) = 279.
from itertools import combinations, product
from collections import defaultdict
p=3
def inv(a): return pow(a,p-2,p)
def rref(rows):
    M=[list(r) for r in rows]; piv=0
    for c in range(8):
        sel=next((r for r in range(piv,len(M)) if M[r][c]%p),None)
        if sel is None: continue
        M[piv],M[sel]=M[sel],M[piv]; iv=inv(M[piv][c]%p); M[piv]=[(x*iv)%p for x in M[piv]]
        for r in range(len(M)):
            if r!=piv and M[r][c]%p:
                f=M[r][c]%p; M[r]=[(M[r][j]-f*M[piv][j])%p for j in range(8)]
        piv+=1
        if piv==len(M): break
    return tuple(tuple(M[i]) for i in range(piv)),piv
def pm(el):
    if not el: yield []; return
    a=el[0]; rest=el[1:]
    for i,b in enumerate(rest):
        for m in pm(rest[:i]+rest[i+1:]): yield [(a,b)]+m
matchings=list(pm(list(range(8))))
def scons(m):
    rows=[]
    for (a,b) in m:
        r=[0]*8; r[a]=1; r[b]=1; rows.append(tuple(r))
    return rows
sheets=[rref(scons(m))[0] for m in matchings]
def stack(A,B): return rref(list(A)+list(B))
def star_of(F): base=len(F); return [i for i,S in enumerate(sheets) if stack(F,S)[1]==base]
B3=None
for i in range(105):
    for j in range(i+1,105):
        b,rk=stack(sheets[i],sheets[j])
        if rk==5:
            for S in sheets:
                b2,rk2=stack(b,S)
                if rk2==6 and len(star_of(b2))==6: B3=(b2,star_of(b2)); break
        if B3: break
    if B3: break
flat,st=B3
V=st; E=[(a,b) for a,b in combinations(range(6),2) if stack(sheets[V[a]],sheets[V[b]])[1]==5]
deg=defaultdict(int)
for a,b in E: deg[a]+=1; deg[b]+=1
print(f"star={st}  |V|=6 |E|={len(E)} b1={len(E)-6+1} degrees={[deg[s] for s in range(6)]}")
def cech_H1(h):
    piv={}; rank=0
    for (a,b) in E:
        for t in range(h):
            vv={}; vv[b*h+t]=1; vv[a*h+t]=(vv.get(a*h+t,0)-1)%p
            vv={k:v for k,v in vv.items() if v%p}
            while vv:
                lead=max(vv)
                if lead in piv:
                    pv=piv[lead]; c=vv[lead]
                    for k,val in pv.items():
                        nv=(vv.get(k,0)-c*val)%p
                        if nv: vv[k]=nv
                        elif k in vv: del vv[k]
                else: break
            if vv:
                lead=max(vv); ivv=inv(vv[lead]); piv[lead]={k:(val*ivv)%p for k,val in vv.items()}; rank+=1
    return len(E)*h-rank
for f in range(5):
    print(f"  f={f}: Cech H1={cech_H1(f+1)}  vs 4*(f+1)={4*(f+1)}")
sm=[matchings[i] for i in st]
cnt=sum(1 for x in product(range(3),repeat=8) if any(all((x[a]+x[b])%3==0 for (a,b) in J) for J in sm))
print(f"  |union|(F3)={cnt}  (A_star(3)=279)")
