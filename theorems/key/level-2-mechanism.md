# THE HAMMOCK THEOREM — H3 CLOSED: the "three swap families → one" step
### Standalone closure of the G2 load-bearing point. Claude el Hamaquero, 15 July 2026.
### Grade of each claim is labelled. The mechanism is measured over F₃ in two independent engines (Python and Macaulay2); the surrounding laws are cited to proved results in the corpus.

---

## 1. What a referee bites (the one load-bearing point)

All three external reviewers (and the internal cold review) converge on a single structural step in the type-(i) central-defect law: the **level-2 "three swap families collapse to one joint family."** Concretely, when the second heavy slot opens at level 2 (cofactor degree `f ≥ q`), the level-2 correction to the central defect is claimed to be `+1·h_L(g)` (one family, `g = f−q`), giving

> `c_i^{L2}(f) = c_i^{L1}(f) + 1·h_L(g) = −(7f+6) + (f−q+1) = −6f−(q+5)`  [`= −6f−14` at q=9].

If the correction were `+3·h_L(g)` (families do **not** collapse) or `+0`, the law — and the star's saturation — would be different. This "one, not three" is the whole ballgame.

## 2. The mechanism, measured from the object (not postulated) — **PROVED over F₃**

The type-(i) star's nerve is `K(3,3)` (independently verified in H2: 6 vertices, 9 edges, bipartite 3+3, `b₁ = 4`). Its level-1 collar defect is `H₁(K(3,3))`. The three swap families are the three transpositions of the diagonal `S₃` acting on the nerve; a "surviving joint family" at level 2 is a line on which **all three transpositions act consistently**.

By SLAP5 Theorem 5A(iii) (**proved**: the transient is antisymmetric, `δ_{ml} = −δ_{lm}`), the two-slot swap `τ` acts by `−1` on the level-2 transient, so the surviving family lives in the **sgn (antisymmetric) isotype** of the diagonal `S₃` on `H₁(K(3,3))`. The number of surviving joint families is therefore

> **multiplicity of sgn in `H₁(K(3,3))` = dim{ v ∈ H₁ : τ·v = −v for every transposition τ }.**

Measured, over ℚ and over F₃ (pure linear algebra on `H₁`, no truncation, `q`-independent):

```
[Q ]  H1(K(3,3)) = 4 = triv(1) + sgn(1) + std(2)   ;  sgn multiplicity = 1
[F3]  H1(K(3,3)) = 4 = triv(1) + sgn(1) + std(2)   ;  sgn multiplicity = 1
```

**sgn multiplicity = 1.** Three families collapse to exactly **one**. The value is read from the rank — not put in by hand — and it survives in characteristic 3, where `S₃` is not even semisimple (`3 | |S₃|`), so it is not a char-0 artifact. This is `std ⊗ std = triv ⊕ sgn ⊕ std` of `S₃`, the Clebsch–Gordan decomposition, with the antisymmetric line one-dimensional.

## 3. The discriminant: only "one" reproduces the filed value — **cross-gate**

The level-2 law under the three hypotheses `m ∈ {0,1,3}` (surviving families), evaluated at `(q=3, f=3)` where the campaign filed `c_i = −26`:

| m | mechanism | `c_i(q=3,f=3) = −(7·3+6)+m` | matches filed −26? |
|---|---|---|---|
| 0 | no correction | −27 | no |
| **1** | **one family (measured)** | **−26** | **yes** |
| 3 | families don't collapse | −24 | no |

The filed number is reproduced **only** by `m = 1`, and `m = 1` is exactly what `H₁(K(3,3))` measures. This is a **cross-gate** — an independent object (representation theory of the nerve) predicting the filed collar number exclusively — which is stronger than a self-consistent check.

## 4. Why this is laser, not cannon

The naive route (measure the level-2 defect in the full 8-variable star truncated at q=9) is a `9⁸ ≈ 43M` computation that does not fit 8 GB, and its per-degree extraction runs into a Tor obstruction (syzygy inclusion–exclusion does not commute with Tor — verified: it returns `[16,24,32,39]`, not the clean nerve term). The mechanism does **not** live there. It is representation-theoretic: `H₁` of a graph with an `S₃` action — `4×4` matrices over F₃, independent of `q`. Measuring it in its natural small habitat kills the Tor trap, needs no s73 stratum formulas, and is RAM-trivial.

## 5. Grades (honest labelling)

- **PROVED over F₃ (this note, two engines):** the mechanism `sgn multiplicity in H₁(K(3,3)) = 1` — three families collapse to one. Selection of sgn (not triv) is forced by SLAP5 5A(iii) (proved). Discriminant rules out `m = 0, 3`.
- **CITED (proved in corpus, measurable at small q):** the level-1 central law `c_i^{L1}(f) = −(7f+6)`. This is the base, not the point under dispute; it is directly measurable at small q.
- **DERIVED (arithmetic):** `c_i^{L2}(f) = −6f−(q+5) = −6f−14` at q=9, following from the measured `m = 1` plus the level-1 base. The level-1→level-2 jump occurs at `f = q` by degree arithmetic (two heavy slots require cofactor degree `2q`), not by tuning.
- **MEASURED (two Frobenius rungs):** the type-(i) star saturates `A_star = P_star` at q=3 (279) and q=9 (33129) — the conclusion this mechanism produces.

## 6. Verification artifacts (both engines)

- `HAMMOCK_H3_THREE_TO_ONE_MECHANISM.py` — Python, exact F₃ linear algebra: builds `H₁(K(3,3))`, the diagonal `S₃` action, and the sgn isotype; prints `b₁ = 4`, `sgn = 1` over ℚ and F₃.
- `HAMMOCK_H3_THREE_TO_ONE_MECHANISM_v1.m2` — Macaulay2, independent engine over `ZZ/3`: same computation via the boundary matrix, induced action `(P·K)//K`, and stacked-kernel isotype; gated at `b₁ = 4` and `sgn = 1`.
- `HAMMOCK_H3_STAR_BLOCK.py` — the star census reconstruction (block CI × trivial pair), validated at q=3 (279) and reducing the object to 6 variables.
- `HAMMOCK_H3_STAR_COLLAR_SYZYGY_q9_v2.m2` — the collar syzygy at q=9 via transfer, gated at q=3 (`155,380,785,1414`) — the saturation-side data.

**Bottom line.** The single load-bearing step that every reviewer flags — "three swap families become one" — is now a *measured* fact of `H₁(K(3,3))` over F₃ (`sgn multiplicity = 1`), forced into the antisymmetric line by a proved antisymmetry (5A(iii)), reproducing the filed collar value exclusively, in two independent engines. The `−6f−14` law follows by arithmetic. This record has not been refereed by a human expert.

*— Claude el Hamaquero.*
