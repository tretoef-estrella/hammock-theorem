# THE MONODROMY MATRIX — EXPLICIT OPERATOR OF THE K(3,3) SLOT ACTION
### Supplement to the Eigenvector Law (P0 pack) for **The Hammock Theorem**. R. Amichis Luengo & Claude (Anthropic). 14 July 2026.
### Purpose: the adversarial reviews asked, on G2, for *"the exact construction, the matrix, the operator, and the demonstration that only those two modes exist."* The Eigenvector Law derives the mechanism; this supplement writes the operator as a literal matrix, proves the eigenstructure by characteristic polynomial, and shows there is no third mode. No new mathematics — this is the requested explicit form.

---

## 1. The space and the operator, concretely
Fix a type-(i) codimension-2 star in dimension six (`k = 3`): six sheets forming the word `B₃`, nerve `K(3,3)` (Eigenvector Law §1). At collar level 2 a syzygy class on a sheet carries data in **two heavy slots** `{v, w}` — the two pair-coordinates whose Frobenius exponent has reached `≥ q`. The relevant local space is the 2-dimensional slot space
```
    U = ⟨ v*, w* ⟩   over  F₃,
```
where `v*, w*` are the coordinate functionals reading the two heavy slots.

**The monodromy operator** `τ : U → U` is transport of slot data around a generating 4-cycle of the nerve `K(3,3)`. By Lemma 2.1 of the Eigenvector Law, `τ` **exchanges the two slots**. In the ordered basis `(v*, w*)` its matrix is therefore literally
```
          ⌈ 0  1 ⌉
    τ  =  |      |          (entries in F₃).
          ⌊ 1  0 ⌋
```
This is the operator, written out. Everything below is linear algebra of this one `2×2` matrix over `F₃`.

## 2. Exactly two eigenlines — by characteristic polynomial
The characteristic polynomial is
```
    det(τ − t·I) = t² − 1 = (t − 1)(t + 1)   over  F₃.
```
Because `char F₃ = 3 ≠ 2`, the roots `t = +1` and `t = −1` are **distinct**. A `2×2` matrix with two distinct eigenvalues is diagonalizable with **exactly two eigenlines** — no more, no fewer, and no Jordan block. Explicitly:
```
    eigenvalue +1 :  eigenvector (1, 1) = (v + w)*   [symmetric]
    eigenvalue −1 :  eigenvector (1, −1) = (v − w)*   [antisymmetric]
```
**There is no third mode**, and this is not an assumption but a count of roots of a degree-2 polynomial over a field where `2 ≠ 0`. (Over `F₂` the two roots would collide and the argument would fail — which is exactly why the mechanism is stated for characteristic `≠ 2`, and why `F₃` is safe.)

*Why the reviewers' worry is answered.* Gemini's concern was that "only two modes" might hide a third, unnoticed collision channel. The characteristic polynomial `t²−1` has degree 2 over a field; it has at most 2 roots, and here exactly 2 distinct ones. A third eigenline is impossible for dimensional reasons — `dim U = 2`. The completeness is forced by linear algebra, not by enumeration of cases that could miss one.

## 3. Which line is "visible" at each level — the occupancy projector
Level structure enters through **how many slots are occupied** (carry exponent `≥ q`):

- **Level 1** (one heavy slot, say `v`): the glued data factor through the projector onto the occupied slot,
```
          ⌈ 1  0 ⌉
    Π₁ =  |      |.
          ⌊ 0  0 ⌋
```
The `τ`-invariant data visible through `Π₁` is one-dimensional — it is the symmetric eigenline `(v+w)*` seen through the single slot. This is the **single unit of overlap** counted as the `−1` in the level-1 Central Defect Law (D3). One occupied slot ⟹ one visible eigenline.

- **Level 2** (both slots occupied): the projector is the identity `I` on `U`; **both** eigenlines are visible. The antisymmetric line `(v−w)*` now joins, and the overlap grows `1 → 2` — the mechanism of Theorem E2 (the double charge `29 → 28`).

The transition `Π₁ → I` as the second slot opens at `f = q` is the **Interruptor**, here realized as the rank of the occupancy projector jumping from 1 to 2. It is a corollary of the monomial disjointness of heavy classes (D1): below `f = q` only one slot can carry weight `≥ q` (total pair-weight `< 2q`), at `f = q` the second can open.

## 4. The two eigenvalues are the two defect coefficients
The payoff is that the **eigenstructure of this single matrix produces both previously-missing coefficients** of the branch-2 slack polynomial:

- the **symmetric** eigenline (`+1`) is pinned at level 1 and gives the `−1` of D3 → propagates to the branch-1 head and the `−6f` of E1;
- the **antisymmetric** eigenline (`−1`) joins at level 2 and gives the extra `−1` of E2 (the `29 → 28` drop) and the `q`-dependent shift `−(q+5)` in E1.

Their combined correction to the crude assembly is `805 − 280q` (Eigenvector Law, Theorem E), reconstructing branch 2 coefficient-for-coefficient — **all six, including the two that resisted every earlier method** (`350q` and `903`). The two eigenvectors of `[[0,1],[1,0]]` were, literally, the last two numbers of the dimension-six slack law.

## 5. The falsifiable check on the matrix itself
A referee can test the operator without trusting the mechanism narrative:
1. **Trace and determinant.** `tr τ = 0`, `det τ = −1`; any correct `2×2` presentation must have these. `t² − (tr)t + det = t² − 1`. ✓
2. **The 4-cycle composition.** Pick one explicit 4-cycle of `K(3,3)` (four sheets, four swap flats) and compose the four sheet-to-sheet slot identifications by hand; the result is the swap `(v w)`, i.e. `[[0,1],[1,0]]`. This is a finite check on ≤ 4 sheets and is the cheapest audit of Lemma 2.1.
3. **Independence of the cycle.** Any other generating 4-cycle gives a conjugate transposition, same characteristic polynomial `t²−1`, same eigenlines up to the shared basis — verifying that the mechanism does not depend on the arbitrary cycle choice.

---

**Attack surface.** (A) The claim `τ = [[0,1],[1,0]]` — recompute the 4-cycle composition on an explicit star (§5.2). (B) The occupancy projector `Π₁ → I` at `f = q` — verify against the monomial disjointness of D1 (the Interruptor). (C) That the two eigenvalues map to the two missing coefficients — trace the `805 − 280q` bookkeeping in the Eigenvector Law §5. All three are finite and explicit.

*This supplement writes down the operator the reviews asked to see. The eigenstructure — exactly two lines, no third mode — is the factorization of `t²−1` over `F₃`, and nothing weaker or stronger is claimed.*
