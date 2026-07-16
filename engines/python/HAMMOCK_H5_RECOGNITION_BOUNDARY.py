#!/usr/bin/env python3
# HAMMOCK HARDENING H5 — Recognition boundary case (k=3, q=3): exhaustive disjointness.
# On a sheet the k+1=4 heavy families {u_m^q * mu : deg mu = e} are pairwise disjoint for
# e<q (no cancellation), collapse at e=q (collar onset), and two sheets sharing an edge
# impose the SAME shared-pair condition.
from itertools import product, combinations
q=3; nsheet=4
def fam(m,e):
    s=set()
    for mu in product(range(e+1),repeat=nsheet):
        if sum(mu)==e:
            x=list(mu); x[m]+=q; s.add(tuple(x))
    return s
for e in range(q+1):
    fs=[fam(m,e) for m in range(nsheet)]
    tot=sum(len(f) for f in fs); uni=len(set().union(*fs))
    tag="<q disjoint" if e<q else "=q collar-onset"
    print(f"e={e} ({tag}): sizes={[len(f) for f in fs]} sum={tot} union={uni} disjoint={tot==uni}")
J1=[(0,1),(2,3),(4,5),(6,7)]; J2=[(0,1),(2,4),(3,5),(6,7)]
print("shared-pair heavy family identical across two sheets:",
      fam(J1.index((0,1)),2)==fam(J2.index((0,1)),2))
