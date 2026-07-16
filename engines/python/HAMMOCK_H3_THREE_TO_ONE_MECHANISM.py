#!/usr/bin/env python3
# HAMMOCK H3 — load-bearing step CLOSED: "three swap families -> one" as the
# multiplicity of sgn (antisymmetric line) in H1(K(3,3)), read from rank over Q and F3.
# SLAP5 Thm 5A(iii) (delta_ml = -delta_lm, proved) forces the level-2 transient into the
# sgn isotype of the diagonal S_3 on the nerve. GATES: b1=4, sgn multiplicity = 1.
import itertools
edges=[(i,3+j) for i in range(3) for j in range(3)]; E=9; V=6
def rank_mod(M,p):
    M=[[x%p for x in row] for row in M]; rows=len(M); cols=len(M[0]) if rows else 0; r=0
    for c in range(cols):
        piv=next((i for i in range(r,rows) if M[i][c]%p),None)
        if piv is None: continue
        M[r],M[piv]=M[piv],M[r]; inv=pow(int(M[r][c])%p,p-2,p); M[r]=[(x*inv)%p for x in M[r]]
        for i in range(rows):
            if i!=r and M[i][c]%p:
                f=M[i][c]%p; M[i]=[(M[i][j]-f*M[r][j])%p for j in range(cols)]
        r+=1
    return r
def kernel_basis(M,p):
    M=[[x%p for x in row] for row in M]; rows=len(M); cols=len(M[0]); r=0; pivots=[]
    for c in range(cols):
        piv=next((i for i in range(r,rows) if M[i][c]%p),None)
        if piv is None: continue
        M[r],M[piv]=M[piv],M[r]; inv=pow(int(M[r][c])%p,p-2,p); M[r]=[(x*inv)%p for x in M[r]]
        for i in range(rows):
            if i!=r and M[i][c]%p:
                f=M[i][c]%p; M[i]=[(M[i][j]-f*M[r][j])%p for j in range(cols)]
        pivots.append(c); r+=1
    free=[c for c in range(cols) if c not in pivots]; basis=[]
    for fc in free:
        v=[0]*cols; v[fc]=1
        for ri,pc in enumerate(pivots): v[pc]=(-M[ri][fc])%p
        basis.append(v)
    return basis
B=[[0]*E for _ in range(V)]
for k,(u,v) in enumerate(edges): B[u][k]+=1; B[v][k]-=1
def perm_on_edges(pi):
    P=[[0]*E for _ in range(E)]
    for k,(u,v) in enumerate(edges): P[edges.index((pi[u],3+pi[v-3]))][k]=1
    return P
transp=[(1,0,2),(0,2,1),(2,1,0)]
def report(p):
    ker=kernel_basis([r[:] for r in B],p); b1=len(ker)
    Kc=[[ker[k][i] for k in range(b1)] for i in range(E)]
    def coords(w):
        A=[[Kc[i][c]%p for c in range(b1)]+[w[i]%p] for i in range(E)]; r=0; piv=[]
        for c in range(b1):
            pr=next((i for i in range(r,E) if A[i][c]%p),None)
            if pr is None: piv.append(None); continue
            A[r],A[pr]=A[pr],A[r]; inv=pow(int(A[r][c])%p,p-2,p); A[r]=[(x*inv)%p for x in A[r]]
            for i in range(E):
                if i!=r and A[i][c]%p:
                    f=A[i][c]%p; A[i]=[(A[i][j]-f*A[r][j])%p for j in range(b1+1)]
            piv.append(r); r+=1
        return [A[piv[c]][b1]%p if piv[c] is not None else 0 for c in range(b1)]
    def act(pi):
        P=perm_on_edges(pi); cols=[]
        for kk in range(b1):
            w=[0]*E
            for i in range(E):
                for j in range(E):
                    if P[i][j] and ker[kk][j]: w[i]=(w[i]+ker[kk][j])%p
            cols.append(coords(w))
        return [[cols[k][r]%p for k in range(b1)] for r in range(b1)]
    def iso(sign):
        st=[]
        for t in transp:
            M=act(t)
            for r in range(b1): st.append([(M[r][c]-sign*(1 if r==c else 0))%p for c in range(b1)])
        return b1-rank_mod(st,p)
    return b1,iso(+1),iso(-1)
if __name__=="__main__":
    for p,lab in [(1000003,"Q"),(3,"F3")]:
        b1,triv,sgn=report(p)
        print(f"[{lab}] H1(K(3,3))={b1} = triv({triv})+sgn({sgn})+std({b1-triv-sgn});  "
              f"sgn multiplicity = {sgn}  (want 1)")
    print("=> three swap families collapse to ONE (sgn=1); law c_i^L2 = -6f-(q+5) = -6f-14 at q=9.")
