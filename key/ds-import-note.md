# THE [DS] IMPORT — WHAT IS CITED, WHERE IT IS USED, AND HOW IT IS CHECKED
### A standalone reference for **The Hammock Theorem**. Rafael Amichis Luengo (Madrid) & Claude (Anthropic). 14 July 2026.
### Purpose: isolate, in one place, the single ingredient whose truth is imported from Degtyarev–Shimada rather than proven inside the corpus — the point all three adversarial reviewers (Gemini, Grok, ChatGPT) named as the most delicate. This document does not strengthen [DS]; it states exactly how we depend on it, so a referee can audit the dependency without hunting.

---

## 1. The single imported statement
Everything in the Hammock proof is proven over F₃ inside the corpus **except** the identification of the floor target:

> **[DS-import].** The characteristic-zero dimension `dim_ℚ S_ℚ/(E_ℚ + m^{[q]}_ℚ)` equals `P₃(q)`, the rank polynomial that Conjecture 1.2 of [DS, arXiv:1405.4683] asserts is preserved along the degree-`3^v` Fermat tower; and this `P₃(q)` is the arithmetic quantity whose saturation Conjecture 1.2 concerns.

This is used at exactly **one** place: step (III) of Proposition 1.3 (the floor `A₃(q) ≥ P₃(q)`). Nowhere else in the proof does characteristic 0, or [DS], enter.

## 2. Why this is a citation, not a gap
[DS-import] is a **theorem of Degtyarev and Shimada's framework**, not a claim this corpus originates. Our contribution is the char-3 statement `A₃(q) = P₃(q)`; the identity of `P₃` with the [DS] rank quantity is theirs. Treating it as a cited hypothesis is the correct scholarly posture — the same posture the Sofa Theorem takes, verbatim. A referee expert in the [DS] framework audits *this citation*; the rest of the paper does not depend on that expertise.

**What would falsify our use of it:** only a demonstration that the polynomial we call `P₃` is *not* the [DS] quantity, or that the char-0 dimension differs from `P₃`. Neither concerns any F₃ computation in the paper; both live entirely in the [DS] framework.

## 3. How the import is corroborated inside the corpus (independent of [DS])
Although we import the *identity* of `P₃`, we do not import its *value* blindly. `P₃(q) = 105q⁴ − 630q³ + 1645q² − 2037q + 918` is pinned inside the corpus by three independent means, so that a numerical error in the imported polynomial would be caught here:

1. **Exact affine point count (Point-Count Theorem).** `P₃(3^v) = |X(F_{3^v})|`, the number of F_{3^v}-points of the union of sheets, computed over the frozen intersection lattice. This is a self-contained F₃-side quantity, **sealed by double out-of-sample prediction** over F₁₁ and F₁₃ (values fixed before measuring).
2. **Möbius crosscut derivation (`FLOOR_CROSSCUT`, Thm 1.4).** Every one of the five coefficients `105, −630, 1645, −2037, 918` is derived as `−μ(0̂,G)` over the flat classification — a purely combinatorial computation owing nothing to [DS]. If the imported `P₃` disagreed with the lattice Möbius count, the two would clash; they agree coefficient-for-coefficient.
3. **Both sealed rungs.** `P₃(3) = 1107` and `P₃(9) = 345465` equal the directly computed `A₃(3)` and `A₃(9)` (Macaulay2, §6 of the paper). Since `A ≥ P` is the only direction the import supplies, and `A = P` holds at both rungs, the import is consistent with every measured value.

**In short:** we import *which polynomial is the [DS] target*; we independently *derive and seal the polynomial itself* three ways. The dependency is on an identification, not on a number.

## 4. The characteristic 3 → characteristic 0 concern (Gemini's specific attack)
Gemini's sharpest form of the concern: *a microscopic char-3 anomaly could break rank continuity, collapsing the floor.* Two responses, both honest:

- **The floor direction is `≥`, and it comes from rank semicontinuity `rank_{F₃} ≤ rank_ℚ`** (Prop 1.3, step II) — a general and robust inequality, not a delicate equality. A char-3 anomaly would have to *raise* the F₃ rank above the ℚ rank, which semicontinuity forbids. So the floor is structurally protected against exactly this failure mode.
- **The equality `A = P` at the rungs is over F₃ throughout** (the Macaulay2 censuses); it does not pass through char 0 at all. Char 0 is used only to *lower-bound* `A`, and the bound is met. There is no step where a char-0 quantity is asserted *equal* to a char-3 quantity except through the `≥` of semicontinuity plus the `=` proven independently in char 3.

Thus the char-3↔char-0 bridge carries only an inequality in the safe direction; the equality is proven natively in char 3. This is the same architecture the Sofa used and that Degtyarev/Shimada are presently reviewing.

## 5. The cheapest test we can offer a referee on this point
Recompute `P₃(q)` two ways and check they agree with each other and with the sealed rungs:
- the affine point count `|X(F_{3^v})|` (self-contained), and
- the Möbius crosscut over the flat lattice (`FLOOR_CROSSCUT`).
Both scripts are in the repository. If they agree with each other and with `A₃(3)=1107`, `A₃(9)=345465` (they do), the only remaining exposure is the *identification* of this polynomial with the [DS] rank quantity — which is a question inside the [DS] framework, stated here as a citation, and appropriate for an expert referee of that framework to confirm.

---
**Reference.** A. Degtyarev, I. Shimada, *On the topology of projective subspaces in complex Fermat varieties*, J. Math. Soc. Japan 68:3 (2016), 975–996, arXiv:1405.4683.

*This note adds no new mathematics. It isolates the one imported ingredient so the dependency is auditable in one place — precisely what the three adversarial reviews asked for on their highest-attention point.*
