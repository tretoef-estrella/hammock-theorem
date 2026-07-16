#!/usr/bin/env python3
# HAMMOCK HARDENING H1 — INDEPENDENT FLAT ENUMERATOR (over F3), k=3, n=8.
# Generates ALL flats of codim<=3 by REAL intersection of the 105 sheets over F3,
# classifies each by (codim, star-size), and confirms the counts equal the
# STAR_ARCHITECTURE list. INDEPENDENT of every sealed anchor -> breaks the
# "completeness would break anchors (circular)" objection with exhaustive enumeration.
# Expected: codim1 star2->630; codim2 star6/4/3 ->280/315/210; codim3 star24/15/6 ->35/28/210.
from itertools import combinations
from collections import defaultdict
p=3
def inv(a): return pow(a,p-2,p)
def rref(rows):
    M=[list(r) for r in rows]; piv=0
    for c in range(8):
        sel=next((r for r in range(piv,len(M)) if M[r][c]%p),None)
        if sel is None: continue
        M[piv],M[sel]=M[sel],M[piv]; iv=inv(M[piv][c]%p)
        M[piv]=[(x*iv)%p for x in M[piv]]
        for r in range(len(M)):
            if r!=piv and M[r][c]%p:
                f=M[r][c]%p; M[r]=[(M[r][j]-f*M[piv][j])%p for j in range(8)]
        piv+=1
        if piv==len(M): break
    return tuple(tuple(M[i]) for i in range(piv)),piv
def perfect_matchings(el):
    if not el: yield []; return
    a=el[0]; rest=el[1:]
    for i,b in enumerate(rest):
        for m in perfect_matchings(rest[:i]+rest[i+1:]): yield [(a,b)]+m
matchings=list(perfect_matchings(list(range(8)))); assert len(matchings)==105
def sheet_cons(m):
    rows=[]
    for (a,b) in m:
        r=[0]*8; r[a]=1; r[b]=1; rows.append(tuple(r))
    return rows
sheets=[rref(sheet_cons(m))[0] for m in matchings]
def stack(A,B): return rref(list(A)+list(B))
fbr={5:set(),6:set(),7:set()}
for i in range(105):
    for j in range(i+1,105):
        b,rk=stack(sheets[i],sheets[j])
        if rk==5: fbr[5].add(b)
for F in list(fbr[5]):
    for S in sheets:
        b,rk=stack(F,S)
        if rk==6: fbr[6].add(b)
for F in list(fbr[6]):
    for S in sheets:
        b,rk=stack(F,S)
        if rk==7: fbr[7].add(b)
def star_size(F):
    base=len(F); return sum(1 for S in sheets if stack(F,S)[1]==base)
for c,rk in [(1,5),(2,6),(3,7)]:
    bystar=defaultdict(int)
    for F in fbr[rk]: bystar[star_size(F)]+=1
    print(f"codim {c} (dim {4-c}): {len(fbr[rk])} flats ; by star-size: {dict(sorted(bystar.items()))}")
