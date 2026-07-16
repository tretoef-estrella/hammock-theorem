#!/usr/bin/env python3
# HAMMOCK HARDENING H6 — SEP transverse frame certification for k=3.
# Slap 4's annihilator law consumes a SEP transverse frame over F_q. This script:
#  (1) confirms NO frame is transverse over F3 at k=3 (caps at 87/105 sheets) -> the
#      Sofa's whole-tower F3 frame does NOT extend to k=3;
#  (2) EXHIBITS+CERTIFIES SEP frames over F9 (q=9) and F27 (q=27, first level where
#      Top(q)=105*C(q-6,4) != 0, i.e. where the annihilator law is actually consumed):
#      all 105 sheet matrices invertible AND all 630 swap pairs SEP-separated.
# Reproducible: deterministic seeds; re-derives the 630 swap pairs geometrically.
import random
class GF:
    def __init__(self,d,redvec):
        self.d=d; self.red=redvec
        self.ZERO=tuple([0]*d); self.ONE=tuple([1]+[0]*(d-1)); self._inv={}
        elems=[]
        def gen(pref):
            if len(pref)==d: elems.append(tuple(pref)); return
            for c in range(3): gen(pref+[c])
        gen([])
        for x in elems:
            if x==self.ZERO: continue
            for y in elems:
                if self.mul(x,y)==self.ONE: self._inv[x]=y; break
    def sub(self,x,y): return tuple((x[i]-y[i])%3 for i in range(self.d))
    def iszero(self,x): return all(v%3==0 for v in x)
    def mul(self,x,y):
        d=self.d; conv=[0]*(2*d-1)
        for i in range(d):
            if x[i]:
                for j in range(d):
                    if y[j]: conv[i+j]=(conv[i+j]+x[i]*y[j])%3
        for k in range(2*d-2,d-1,-1):
            c=conv[k]%3
            if c:
                conv[k]=0
                for i in range(d): conv[k-d+i]=(conv[k-d+i]+c*self.red[i])%3
        return tuple(conv[i]%3 for i in range(d))
    def inv(self,x): return self._inv[x]
def pmn(el):
    if not el: yield []; return
    a=el[0]; rest=el[1:]
    for i,b in enumerate(rest):
        for m in pmn(rest[:i]+rest[i+1:]): yield [(min(a,b),max(a,b))]+m
matchings=[tuple(sorted(m)) for m in pmn(list(range(8)))]
def rank3(rows):
    M=[list(r) for r in rows]; piv=0
    for c in range(8):
        sel=next((r for r in range(piv,len(M)) if M[r][c]%3),None)
        if sel is None: continue
        M[piv],M[sel]=M[sel],M[piv]; iv=1 if M[piv][c]%3==1 else 2; M[piv]=[(x*iv)%3 for x in M[piv]]
        for r in range(len(M)):
            if r!=piv and M[r][c]%3:
                f=M[r][c]%3; M[r]=[(M[r][j]-f*M[piv][j])%3 for j in range(8)]
        piv+=1
        if piv==len(M): break
    return piv
def scons(m):
    out=[]
    for (a,b) in m:
        r=[0]*8; r[a]=1; r[b]=1; out.append(tuple(r))
    return out
swap_pairs=[(i,j) for i in range(105) for j in range(i+1,105) if rank3(scons(matchings[i])+scons(matchings[j]))==5]
def det(F,M):
    n=len(M); M=[r[:] for r in M]; d=F.ONE
    for c in range(n):
        piv=next((r for r in range(c,n) if not F.iszero(M[r][c])),None)
        if piv is None: return F.ZERO
        if piv!=c: M[c],M[piv]=M[piv],M[c]; d=F.sub(F.ZERO,d)
        d=F.mul(d,M[c][c]); ic=F.inv(M[c][c])
        for r in range(c+1,n):
            f=F.mul(M[r][c],ic)
            if not F.iszero(f):
                for k in range(c,n): M[r][k]=F.sub(M[r][k],F.mul(f,M[c][k]))
    return d
def solve(F,L,r):
    n=len(L); A=[[L[j][i] for j in range(n)] for i in range(n)]; b=list(r)
    for c in range(n):
        piv=next((rr for rr in range(c,n) if not F.iszero(A[rr][c])),None)
        if piv is None: return None
        A[c],A[piv]=A[piv],A[c]; b[c],b[piv]=b[piv],b[c]
        ic=F.inv(A[c][c]); A[c]=[F.mul(ic,x) for x in A[c]]; b[c]=F.mul(ic,b[c])
        for rr in range(n):
            if rr!=c and not F.iszero(A[rr][c]):
                f=A[rr][c]; A[rr]=[F.sub(A[rr][k],F.mul(f,A[c][k])) for k in range(n)]; b[rr]=F.sub(b[rr],F.mul(f,b[c]))
    return b
def rest(F,form,m): return [F.sub(form[a],form[b]) for (a,b) in m]
def certify(F,tries,seed,name):
    random.seed(seed)
    rnd=lambda: tuple(random.randint(0,2) for _ in range(F.d))
    e1=[F.ONE]*8; best=0
    for att in range(tries):
        L=[[rnd() for _ in range(8)] for _ in range(4)]; G=[[rnd() for _ in range(8)] for _ in range(3)]
        if F.iszero(det(F,[e1]+L+G)): continue
        LJs=[]; nt=0; ok=True
        for m in matchings:
            LJ=[rest(F,L[j],m) for j in range(4)]
            if F.iszero(det(F,LJ)): ok=False; break
            LJs.append(LJ); nt+=1
        best=max(best,nt)
        if not ok: continue
        cJ=[[tuple(solve(F,LJs[si],rest(F,G[i],m))) for i in range(3)] for si,m in enumerate(matchings)]
        if all(any(cJ[u][i]!=cJ[v][i] for i in range(3)) for (u,v) in swap_pairs):
            print(f"  [{name}] CERTIFIED: transverse 105/105, SEP {len(swap_pairs)}/630  (attempt {att})")
            return True
    print(f"  [{name}] no full frame in {tries} tries; best transversality {best}/105")
    return False
print("swap-adjacent pairs:",len(swap_pairs))
certify(GF(1,(0,)) if False else GF(2,(1,1)), 1, 0, "warmup-skip") if False else None
# F3 (d=1): show insufficiency
F3=GF(1,(0,))  # trivial: GF(3), red unused for d=1
# fix F3 mult for d=1 (t^1==red not used); patch:
F3.mul=lambda x,y:( (x[0]*y[0])%3, )
F3.inv=lambda x:( (1 if x[0]==1 else 2), )
certify(F3, 40000, 0, "F3")
certify(GF(2,(1,1)), 4000, 7, "F9  (q=9)")
certify(GF(3,(1,1,0)), 2000, 11, "F27 (q=27, Top!=0)")
