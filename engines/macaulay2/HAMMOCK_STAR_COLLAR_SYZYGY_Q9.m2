-- ============================================================================
--  THE HAMMOCK THEOREM — H3: DIRECT COLLAR-SYZYGY MEASUREMENT of the type-(i)
--  star at q = 9 (the G2 scope reserve).  Claude el Hamaquero, 15 Jul 2026.
--
--  BOMBPROOF: every q=9 number is GATED at q=3 against values independently
--  precomputed in a separate engine (Python: exact F3 linear algebra + the CI
--  Hilbert series), and by TWO routes (transfer identity AND direct kernel).
--
--  REDUCTION.  The type-(i) B3 star = (B3 block on 6 vars) x (trivial pair w).
--  Radicality/Letter-Hilbert => block ideal is a complete intersection:
--     g1=e1(a)+e1(b), g2=e2(a)-e2(b), g3=e3(a)+e3(b), a={y0,y1,y2},b={y3,y4,y5}.
--  Star ring Rs = k[y0..y5,w]/(g1,g2,g3); the 8 ambient vars restrict to
--  x=(y0,...,y5, w, -w).  Runs in 7 variables (light on 8 GB), NOT 9^8 = 43M.
--
--  MEASURED (transfer identity, exact by rank-nullity, light):
--    Syz_star(e') = A_star(q+e') - HF_R(q+e') + 8*HF_R(e'),  e' = q+f, A-degree 2q+f
--  CROSS-CHECK at q=3 only (heavier): direct kernel of the 1x8 map [x_i^q].
--
--  q=3 GATES (precomputed; if any fails -> STOP, do not trust q=9):
--    A_star(3) census = {1,6,20,43,64,67,49,23,6}         (total 279)
--    HF_R(0..9)       = {1,6,20,49,99,176,286,435,629,874}
--    Syz_star(3) f0..3 = {155, 380, 785, 1414}            (transfer AND kernel)
-- ============================================================================

R  = ZZ/3[y_0,y_1,y_2,y_3,y_4,y_5,w];
g1 = y_0+y_1+y_2+y_3+y_4+y_5;
g2 = (y_0*y_1+y_0*y_2+y_1*y_2) - (y_3*y_4+y_3*y_5+y_4*y_5);
g3 = y_0*y_1*y_2 + y_3*y_4*y_5;
Rs = R/ideal(g1,g2,g3);

-- census ring and helpers, computed ONCE per q
AstarRing = (q) -> Rs/(ideal(y_0^q,y_1^q,y_2^q,y_3^q,y_4^q,y_5^q, w^q));
censusOf  = (A,top) -> apply(toList(0..top), d -> hilbertFunction(d,A));
hfrList   = (top) -> apply(toList(0..top), d -> hilbertFunction(d,Rs));
-- transfer: Syz_star(e'=q+f) = A_star(2q+f) - HF_R(2q+f) + 8*HF_R(q+f)
syzTransfer = (A,q,fmax) -> apply(toList(0..fmax),
      f -> hilbertFunction(2*q+f,A) - hilbertFunction(2*q+f,Rs) + 8*hilbertFunction(q+f,Rs));
syzKernel = (q,fmax) -> (
      M := matrix{{(y_0)^q,(y_1)^q,(y_2)^q,(y_3)^q,(y_4)^q,(y_5)^q,(w)^q,-(w)^q}};
      K := kernel M;
      apply(toList(0..fmax), f -> hilbertFunction(q+f,K)) );

stdio << "=========================================================" << endl;
stdio << " H3 - type-(i) star collar syzygy (block+pair, 7 vars)" << endl;
stdio << "=========================================================" << endl;

A3   = AstarRing 3;
cen3 = censusOf(A3, 8);
hfr3 = hfrList 9;
syz3T= syzTransfer(A3,3,3);
syz3K= syzKernel(3,3);
stdio << "q=3 A_star census : " << cen3  << "  want {1,6,20,43,64,67,49,23,6}" << endl;
stdio << "q=3 HF_R 0..9     : " << hfr3  << "  want {1,6,20,49,99,176,286,435,629,874}" << endl;
stdio << "q=3 Syz(transfer) : " << syz3T << "  want {155,380,785,1414}" << endl;
stdio << "q=3 Syz(kernel)   : " << syz3K << "  want {155,380,785,1414}" << endl;

gate = (cen3=={1,6,20,43,64,67,49,23,6}) and (hfr3=={1,6,20,49,99,176,286,435,629,874})
        and (syz3T=={155,380,785,1414}) and (syz3K=={155,380,785,1414});
stdio << "GATE PASS: " << gate << endl << endl;

if not gate then stdio << "*** q=3 GATE FAILED -- STOP. Do not trust q=9. ***" << endl
else (
    A9   = AstarRing 9;
    cen9 = censusOf(A9, 32);
    syz9 = syzTransfer(A9,9,14);
    stdio << "--- q=3 gates pass; q=9 direct measurement ---" << endl;
    stdio << "q=9 A_star total  = " << (sum cen9) << "  want 33129 = P_star(9)" << endl;
    stdio << "q=9 A_star census = " << cen9 << endl << endl;
    stdio << "q=9 collar syzygy Syz_star(e'=9+f), f=0..14 (level 2 opens at f=q=9):" << endl;
    stdio << syz9 << endl << endl;
    stdio << " Law under test: c_i^{L2}(f) = -6f-(q+5) = -6f-14 at q=9 (vs level-1 -(7f+6))." << endl;
    stdio << " The measured collar syzygy at the SECOND rung is the direct per-degree data" << endl;
    stdio << " the scope reserve asked for; with saturation A_star(9)=P_star(9) it tests the" << endl;
    stdio << " 'three-families-to-one' step. Isolating c_central from the swap stratum needs" << endl;
    stdio << " the exact c_swap(f) bookkeeping (campaign s73/fourth-relay), NOT in the project" << endl;
    stdio << " files here -- that final subtraction is stated, not fabricated." << endl;
    );
stdio << "=========================================================" << endl;
