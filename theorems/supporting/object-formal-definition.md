# THE HAMMOCK OBJECT — FORMAL DEFINITION AND DICTIONARY
### A standalone reference for **The Hammock Theorem**. Rafael Amichis Luengo (Madrid, tretoef@gmail.com) & Claude (Anthropic). 14 July 2026.
### Purpose: answer, once and precisely, the question a referee asks first — *what is the object?* Every other standalone and the main paper may cite this document for the definitions it fixes.

---

## 0. One-paragraph answer
The object is a **linear subspace arrangement over the finite field F₃**, together with the graded ring theory of a specific Frobenius truncation of its coordinate ring. It is **not** a matroid, string algebra, or abstract poset; those appear only as *derived bookkeeping* (the intersection lattice of the arrangement is a poset; its Möbius function computes the floor polynomial). The primary object is concrete: 105 four-dimensional linear subspaces of `F₃⁸`, the odd-symmetric ideal cutting them out, and the Artinian quotient obtained by adjoining `q`-th powers of the variables.

---

## 1. The arrangement
Fix `n = 8` and the polynomial ring `S = F₃[x₁, …, x₈]`, standard-graded.

A **perfect matching** `J` of the complete graph `K₈` is a partition of `{1,…,8}` into four unordered pairs. There are `(8−1)!! = 7·5·3·1 = 105` of them.

To each matching `J = {{a₁,b₁}, …, {a₄,b₄}}` associate the **linear sheet**
```
    V_J = { x ∈ F₃⁸ : x_{a_i} + x_{b_i} = 0 for i = 1..4 },
```
a `4`-dimensional F₃-linear subspace (four independent linear equations in eight variables). Its ideal is `I_J = (x_{a₁}+x_{b₁}, …, x_{a₄}+x_{b₄})`.

The **Hammock arrangement** is `𝒜 = { V_J : J a perfect matching of K₈ }`, with union `X = ⋃_J V_J`.

*(General dimension: replace 8 by `n = 2k+2`; there are `(2k+1)!!` matchings, each sheet `(k+1)`-dimensional. `k = 2` is the Sofa; `k = 3` is the Hammock. Everything below is stated for `k = 3` and holds verbatim in general with `4 → k+1`, `105 → (2k+1)!!`, `28 → C(2k+2,2)` edges.)*

## 2. The odd-symmetric ideal
Let `e_j` be the `j`-th elementary symmetric polynomial in `x₁,…,x₈`. Define
```
    E = (e₁, e₃, e₅, e₇),   R = S/E.
```
**Fact (Odd Symmetric / Radicality — campaign theorem, standalone `odd-symmetric` / `RADICALITY`).** `E = ⋂_J I_J`, and `E` is radical. Hence `R` is the reduced coordinate ring of `X`, of Krull dimension `4`, multiplicity `105`, and complete-intersection Hilbert series `∏_{i=1}^{4}(1−t^{2i−1})/(1−t)^8`.

This is the sense in which the 105 sheets are "the same object" as four polynomials: the arrangement **is** the vanishing locus of the odd elementary symmetric functions. This identity is proven, not assumed (Jacobian/Serre argument; see `RADICALITY`).

## 3. The Frobenius truncation and the invariant
For `q = 3^v` let `m^{[q]} = (x₁^q, …, x₈^q)` (the `q`-th Frobenius power of the maximal ideal). Define the **Artinian quotient** and its dimension
```
    A₃(q) = dim_{F₃} S/(E + m^{[q]}).
```
This is the object of the theorem. It is finite for every `q` (the quotient is Artinian: `x_i^q = 0` in it). Its **graded census** is the Hilbert function `d ↦ dim_{F₃} [S/(E+m^{[q]})]_d`; the total `A₃(q)` is the sum.

**The Hammock Theorem.** `A₃(q) = P₃(q) = 105q⁴ − 630q³ + 1645q² − 2037q + 918` for every `q = 3^v`.

## 4. The intersection lattice (the *derived* combinatorial object)
The only poset in play is the **intersection lattice** `L(𝒜)`: all subspaces obtained as intersections of the `V_J`, ordered by reverse inclusion, with `0̂ = F₃⁸`. Its elements are the **flats**. The floor polynomial is
```
    P₃(q) = Σ_{G ∈ L(𝒜)} (−μ(0̂, G))·q^{dim G},
```
the Möbius/characteristic-polynomial count of `F₃`-points of the union (see `FLOOR_CROSSCUT`). The **classification of flats** — which subspaces actually arise as intersections, and their Möbius values — is the content of `STAR_ARCHITECTURE`, and its exhaustiveness is exactly load-bearing point (3) of the adversarial reviews. The lattice is **not geometric** (atoms enter only at rank `k+1`; lower ranks are empty — verified, and recorded in the campaign cemetery); this is why generic matroid/Möbius shortcuts do not apply and the classification must be proven directly.

## 5. What the object is NOT (to prevent category errors)
- **Not a matroid.** The intersection lattice is not geometric (§4); matroid Möbius theory does not apply off the shelf.
- **Not a hyperplane arrangement.** The sheets are codimension `k+1 = 4`, not `1`. It is a *subspace* arrangement.
- **Not a string/quiver algebra.** `R` is a reduced coordinate ring; no path algebra structure is used or claimed.
- **Not characteristic-0.** Everything primary lives over `F₃`. Characteristic 0 enters only through the imported floor identity [DS] (see `HAMMOCK_DS_IMPORT_NOTE`), and only as a *lower bound* corroborated by an `F₃` point count.

## 6. The dictionary to Degtyarev–Shimada Conjecture 1.2
Conjecture 1.2 of [DS, arXiv:1405.4683] asserts that a certain diagonal cycle sublattice is **saturated** in the direct sum of tensor powers, at every level of the degree-`3^v` Fermat tower. The algebraic restatement used here is:
```
   diagonal saturated at level v   ⟺   A_k(3^v) = P_k(3^v),
```
with `A_k` the truncated-quotient dimension of §3 and `P_k` the [DS] rank polynomial of §4. This equivalence is the geometric dictionary; it is the one ingredient we import rather than prove, and it is treated as a cited hypothesis (§ `HAMMOCK_DS_IMPORT_NOTE`, and load-bearing point (1) of the reviews). For the Fermat **sixfolds** (`k = 3`) the theorem of §3 therefore establishes Conjecture 1.2 at every tower level, *modulo* the cited dictionary — exactly the scope the Sofa established for the fourfolds.

---
*This document fixes notation only; every asserted fact carries its own standalone proof, named inline. Nothing here is new mathematics — it is the formal front matter the reviewers asked for.*
