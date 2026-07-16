-- ============================================================================
--  THE HAMMOCK THEOREM — H3 load-bearing step, CLOSED: "three swap families -> one".
--  Claude el Hamaquero, 15 Jul 2026.  Independent Macaulay2 confirmation over F3.
--
--  The type-(i) star's nerve is K(3,3); its level-1 collar defect is H1(K(3,3))
--  (dim b1 = 4).  At level 2 the second heavy slot opens and the two-slot swap tau
--  acts; SLAP5 Thm 5A(iii) (proved: delta_{ml} = -delta_{lm}) makes the transient
--  ANTISYMMETRIC, so the surviving joint family lives in the sgn-isotype of the
--  diagonal S_3 acting on the nerve.  The load-bearing claim "three families -> one"
--  is exactly:  multiplicity of sgn in H1(K(3,3)) = 1  (not 3, not 0).
--
--  This is representation theory / linear algebra over F3 -- q-independent, tiny.
--  GATES: b1 = 4, and sgn-isotype dim = 1.  If either fails, the mechanism is wrong.
-- ============================================================================
kk = ZZ/3;

-- boundary of K(3,3): rows = vertices a0,a1,a2,b0,b1,b2 ; cols = edges e_k, k=3i+j -> (a_i,b_j)
B = matrix table(6,9, (r,k) -> ( i := k//3; j := k%3;
        if r==i then 1_kk else if r==3+j then -1_kk else 0_kk));
K = gens ker B;              -- columns = basis of H1(K(3,3)) over F3
b1 = numColumns K;

-- diagonal S_3: pi permutes {0,1,2}; on edges e_{ij} -> e_{pi(i),pi(j)}
permEdge = (pi) -> matrix table(9,9,(a,b)->(
        ib := b//3; jb := b%3; na := (pi#ib)*3 + (pi#jb);
        if a==na then 1_kk else 0_kk));
-- induced action on H1:  A with K*A = P*K  ->  A = (P*K)//K
induced = (pi) -> ( P := permEdge pi; (P*K)//K );

transp = {{1,0,2},{0,2,1},{2,1,0}};   -- (01),(12),(02)
Idb = id_(kk^b1);

-- sgn isotype = { v in H1 : tau(v) = -v for every transposition } = ker of stacked (A_t + I)
stackSgn = fold((x,y)->x||y, apply(transp, t -> induced(t) + Idb));
sgnDim = b1 - rank stackSgn;
-- triv-fixed (reference) = ker of stacked (A_t - I)
stackTriv = fold((x,y)->x||y, apply(transp, t -> induced(t) - Idb));
trivDim = b1 - rank stackTriv;

stdio << "=====================================================" << endl;
stdio << " H3 mechanism: three swap families -> one (over F3)" << endl;
stdio << "=====================================================" << endl;
stdio << "b1 = dim H1(K(3,3))        = " << b1 << "   (want 4)" << endl;
stdio << "sgn isotype dim            = " << sgnDim << "   (want 1  <- ONE joint family)" << endl;
stdio << "triv-fixed dim (reference) = " << trivDim << "   (want 1)" << endl;
stdio << "std dim (remainder)        = " << b1 - sgnDim - trivDim << "   (want 2)" << endl;
gate = (b1 == 4) and (sgnDim == 1);
stdio << "GATE (b1=4 and sgn=1): " << gate << endl;
if gate then (
    stdio << endl;
    stdio << "=> THREE swap families collapse to ONE at level 2 (sgn multiplicity = 1)." << endl;
    stdio << "   Hence the level-2 central-defect correction is +1*h_L(g), g=f-q, giving" << endl;
    stdio << "   c_i^{L2}(f) = -(7f+6) + (f-q+1) = -6f-(q+5)  [= -6f-14 at q=9]." << endl;
    stdio << "   Discriminant: m=1 -> -26 at (q=3,f=3) [filed]; m=3 -> -24; m=0 -> -27." << endl;
    ) else stdio << "*** GATE FAILED -- mechanism does NOT close; investigate (Ley 26 or bug). ***" << endl;
stdio << "=====================================================" << endl;
