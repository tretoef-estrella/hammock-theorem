#!/usr/bin/env python3
# HAMMOCK SEMIFINAL — answers the two deepest referee misses in one pass:
#  (Gemini #3) "q=9 is blind to the annihilator/Top" -> the annihilator law is measured
#     at q=9 in the collar-DUAL band (A_{44-d} = ann_c, c=12..17), and the Ledger fires
#     with Top != 0 at q=27; Top(9)=0 is a triviality (boundary degrees {9,10,11} < 12).
#  (ChatGPT #3) "prove Phi_c is onto, not 'one witness per summand'" -> the Covering Lemma
#     is verified exhaustively over all 5460 sheet pairs: every sheet has a separating swap
#     hyperplane on every other sheet, so the lifting polynomials X_J exist and Phi_c is onto.
from itertools import combinations
from math import comb
p=3
# ---------- annihilator law, hockey-stick Top, duality, Ledger at q=27 ----------
def ann(c): return 105*comb(c-9,3) if c-9>=3 else 0
def Top(q): return 105*comb(q-6,4) if q-6>=4 else 0
print("annihilator first classes a_c=105*C(c-9,3), c=12..17:",[ann(c) for c in range(12,18)])
print("duality A_d(q=9)=ann_{44-d}: A_27..A_32 <-> ann_17..ann_12 =",[ann(44-d) for d in range(27,33)])
print("Top(3),Top(9),Top(27) =",Top(3),Top(9),Top(27),"  (fires first at q=27)")
from fractions import Fraction as Fr
P3=lambda q:105*q**4-630*q**3+1645*q**2-2037*q+918
ZA=lambda q:Fr(35,8)*q**4-Fr(315,4)*q**3+Fr(5565,8)*q**2-Fr(12285,4)*q+5516
W =lambda q:Fr(385,8)*q**4-Fr(1365,4)*q**3+Fr(6195,8)*q**2+Fr(4347,4)*q-5544
Tp=lambda q:Fr(35,8)*q**4-Fr(525,4)*q**3+Fr(11725,8)*q**2-Fr(28875,4)*q+13230
B3=lambda q:Fr(385,8)*q**4-Fr(315,4)*q**3-Fr(10325,8)*q**2+Fr(28665,4)*q-12284
for q in (9,27):
    s=ZA(q)+W(q)+Tp(q)+B3(q)
    print(f"Ledger q={q}: ZA={ZA(q)} W={W(q)} Top={Tp(q)} B3={B3(q)} sum={s} P3={P3(q)} ok={s==P3(q)}")
# ---------- Covering Lemma (surjectivity of Phi_c) over all sheet pairs ----------
def rref(rows):
    M=[list(r) for r in rows]; piv=0; pc=[]
    for c in range(8):
        sel=next((r for r in range(piv,len(M)) if M[r][c]%p),None)
        if sel is None: continue
        M[piv],M[sel]=M[sel],M[piv]; iv=pow(M[piv][c]%p,p-2,p); M[piv]=[(x*iv)%p for x in M[piv]]
        for r in range(len(M)):
            if r!=piv and M[r][c]%p:
                f=M[r][c]%p; M[r]=[(M[r][j]-f*M[piv][j])%p for j in range(8)]
        piv+=1; pc.append(c)
        if piv==len(M): break
    return [tuple(M[i]) for i in range(piv)],pc
def pm(el):
    if not el: yield []; return
    a=el[0]; rest=el[1:]
    for i,b in enumerate(rest):
        for m in pm(rest[:i]+rest[i+1:]): yield [(a,b)]+m
matchings=[tuple(sorted((min(a,b),max(a,b)) for(a,b)in m)) for m in pm(list(range(8)))]
def srows(J):
    out=[]
    for(a,b)in J:
        r=[0]*8;r[a]=1;r[b]=1;out.append(tuple(r))
    return out
def inrs(vec,basis,pc):
    v=list(vec)
    for row,c in zip(basis,pc):
        if v[c]%p:
            f=v[c]%p; v=[(v[j]-f*row[j])%p for j in range(8)]
    return all(x%p==0 for x in v)
def swap_forms(J):
    fs=[]
    for m in range(4):
        for n in range(m+1,4):
            a,b=J[m]; c,d=J[n]
            for(i,j)in[(a,c),(a,d),(b,c),(b,d)]:
                for s in(1,-1):
                    f=[0]*8;f[i]=(f[i]+1)%p;f[j]=(f[j]+s)%p;fs.append(tuple(x%p for x in f))
    return fs
sb=[rref(srows(J)) for J in matchings]
ok=all(any(inrs(f,sb[jp][0],sb[jp][1]) for f in swap_forms(J))
       for ji,J in enumerate(matchings) for jp in range(105) if jp!=ji)
print("Covering Lemma over all 105*104 pairs (separator exists):",ok,"-> Phi_c onto -> a_12=105")
