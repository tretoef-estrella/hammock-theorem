#!/usr/bin/env python3
# ============================================================
#  THE HAMMOCK THEOREM — LEDGER IDENTITY, EXACT SYMBOLIC CERTIFICATE
#  Verifies Theorem 5.1 (the Ledger) in exact rational arithmetic:
#    (1) ZA(q) + W(q) + Top(q) + B3(q) == P3(q)  identically in q
#    (2) at q = 9 the four zones equal 5516, 133938, 0, 206011,
#        summing to A3(9) = 345465
#    (3) B3(q) as defined equals P3 - ZA - W - Top
#  No floats, no fitting: SymPy Rational throughout.
#
#  Run:  python3 HAMMOCK_LEDGER_SYMPY_CERTIFICATE.py
#  Closes the "Row 4 / SymPy check" requested by the reviewers.
# ============================================================
from sympy import symbols, Rational, expand, simplify

q = symbols('q')

# The floor polynomial (paper Thm 1.2 / 1.4)
P3 = 105*q**4 - 630*q**3 + 1645*q**2 - 2037*q + 918

# The four zone laws (paper Thm 5.1), exact rationals
ZA  = Rational(35,8)*q**4  - Rational(315,4)*q**3  + Rational(5565,8)*q**2  - Rational(12285,4)*q + 5516
W   = Rational(385,8)*q**4 - Rational(1365,4)*q**3 + Rational(6195,8)*q**2  + Rational(4347,4)*q  - 5544
Top = Rational(35,8)*q**4  - Rational(525,4)*q**3  + Rational(11725,8)*q**2 - Rational(28875,4)*q + 13230
B3  = Rational(385,8)*q**4 - Rational(315,4)*q**3  - Rational(10325,8)*q**2 + Rational(28665,4)*q  - 12284

print("="*64)
print(" HAMMOCK LEDGER — EXACT SYMBOLIC CERTIFICATE (SymPy Rational)")
print("="*64)

# (1) polynomial identity ZA + W + Top + B3 == P3
lhs = expand(ZA + W + Top + B3)
diff = expand(lhs - P3)
print("\n(1) ZA + W + Top + B3  - P3  =", diff,
      " ->", "IDENTICAL" if diff == 0 else "*** MISMATCH ***")

# (2) B3 defined as P3 - ZA - W - Top matches the stated B3
B3_def = expand(P3 - ZA - W - Top)
print("\n(2) (P3 - ZA - W - Top) - B3_stated =", expand(B3_def - B3),
      " ->", "IDENTICAL" if expand(B3_def - B3) == 0 else "*** MISMATCH ***")

# (3) numeric values at q = 9
print("\n(3) values at q = 9:")
vals = {"ZA": ZA, "W": W, "Top": Top, "B3": B3, "P3": P3}
want = {"ZA": 5516, "W": 133938, "Top": 0, "B3": 206011, "P3": 345465}
allok = True
for name in ["ZA","W","Top","B3","P3"]:
    got = vals[name].subs(q,9)
    ok = (got == want[name])
    allok = allok and ok
    print(f"    {name:4s}(9) = {int(got):>8d}   want {want[name]:>8d}   {'OK' if ok else '*** FAIL ***'}")

s9 = (ZA+W+Top+B3).subs(q,9)
print(f"    sum       = {int(s9):>8d}   want   345465   {'OK' if s9==345465 else '*** FAIL ***'}")

print("\n" + "="*64)
if diff == 0 and expand(B3_def - B3) == 0 and allok and s9 == 345465:
    print(" CERTIFICATE PASSED — Ledger identity exact, q=9 slices 4/4.")
else:
    print(" CERTIFICATE FAILED.")
print("="*64)
