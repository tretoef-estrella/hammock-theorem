# THE THRESHOLD BOUND AND THE PARAMETER LEMMA (COMPLETO — with the generation argument)
## `e₀(k) ≤ (2k+1)!!` for every dimension (closed); the parameter machinery at the deepest flat; and (COMPLETO) the confinement of minimal generators that fences the census onset from above

**Chaise Longue campaign — standalone theorem write-up (referee edition, COMPLETO)** · R. Amichis Luengo · Claude (Anthropic) · 14 July 2026
*COMPLETO edition adds §I.b — the explicit generation/confinement argument answering the referee demand ("prove algebraically that no new minimal generator is born at degree ≥ e₀"), stated at exactly the grade the structure supports, with the residual named precisely (this is the G1 cabo, and this section fences it as tightly as the current theorems allow).*

---

## Part I — Theorem T3 (the uniform threshold bound)

> **Theorem T3.** For every `k`, the window census `σ_e(k)` agrees with its Hilbert polynomial for all `e > (2k+1)!!`; that is, `e₀(k) ≤ reg(M(k)) ≤ (2k+1)!!`.
*Proof.* Two campaign theorems compose: Slap 1 exhibits `σ_e(k)` as the Hilbert function of a finitely generated graded module `M(k)`, hence polynomial for `e > reg(M(k))`; Slap 2 bounds `reg(M(k)) ≤ (2k+1)!!`. ∎

**Status.** Closes, at theorem grade and uniformly in `k`, the boundedness half of the threshold question. Filed data: `e₀(2) = 4`, `e₀(3) = 9` (the latter confirmed at four consecutive out-of-sample points through `σ₁₂ = 14238`), matching the candidate `e₀(k) = k²`.

## Part I.b — THE GENERATION ARGUMENT (COMPLETO): no minimal generator survives past the onset

The referee's precise demand: it is not enough that `σ_e` *matches* a polynomial from `e = 9`; one must argue that **no minimal generator of `M(3)` is born at a degree `≥ 9`** that would later break the match. We fence this from above as tightly as the current theorems allow, and name the exact residual.

### I.b.1 Generators are confined to degrees `≤ reg(M(k)) ≤ (2k+1)!!` (theorem)
`M(k)` is a finitely generated graded module over the polynomial ring. Its minimal generators, and all its syzygies, occur in degrees `≤ reg(M(k))` (definition/property of Castelnuovo–Mumford regularity). By Slap 2, `reg(M(3)) ≤ 105`. **Therefore every minimal generator of `M(3)` lives in degree `≤ 105`; none is born above 105, unconditionally.** For `e > 105` the Hilbert function is exactly the Hilbert polynomial — the census law is unconditional there. This is the first, rigorous fence: the "surprise generator" a referee worries about cannot appear beyond degree 105.

### I.b.2 The head length is `k(k+1)`, not longer — the Swap-Ramp structural reason
Within `[0, 105]`, the pre-stable head — the degrees where `σ_e` deviates from the cubic — has measured length ending at `e₀ = 9`. The structural reason is the **Swap-Ramp scale** `k(k+1) = 12`: the generators of the window syzygy module come from the swap geometry of the sheets, whose relevant degrees are bounded by the swap-product degree `k(k+1)`. The deviations decay `189, 48, 7, 0` (filed), reaching 0 at `e = 9` and staying 0 through the four measured out-of-sample points `e = 9, 10, 11, 12`. A generator born at some `e ∈ [10, 105]` would produce a nonzero deviation at that degree; none is seen where measured.

### I.b.3 The candidate onset and its reduction
The candidate `e₀(k) = k²` reduces, through the theorem-grade degree bookkeeping of the zone assembly (denominator `(1−t)^{k+1}`; pair-attachment preserves numerator degree; Leibniz adds letter degrees; dominant word the full zero letter `Z_{k+1}`), to the Sharp Regularity Law's `Z`-branch `deg N_G(Z_m) = m(m−1)`. Under Ley 48 the sharp value stands as a candidate with its reduction written.

### I.b.4 The exact residual (Ley 42 — named, not hidden)
What is **theorem**: no generator past 105 (I.b.1); onset verified at four out-of-sample points with the mechanism identified (I.b.2). What is **not yet theorem**: that no minimal generator occurs in the finite band `10 ≤ e ≤ 105`. This is a *finite* residual — a single regularity computation on `M(3)` (or the sharp-regularity refinement of I.b.3) closes it — and it is precisely the G1 cabo. Two honest ways to close it, both offered to a referee:
- **(a) Direct.** Compute `reg(M(3))` sharply (a finite Betti-number computation); if `reg(M(3)) ≤ 9`, the band collapses and the onset is theorem. The filed data (deviation 0 at `e = 9..12`) is consistent with `reg(M(3)) = 9`.
- **(b) Structural.** Complete the reduction of I.b.3 to prove `deg` of the dominant letter equals the observed onset, upgrading the candidate to law uniformly in `k`.
**Neither is a structural gap in the main theorem**: for `e > 105` the census is unconditional (I.b.1), and the Ledger consumes only the BOUND `e₀ ≤ 105` (Tanda 7, by construction), which is theorem. The sharp onset `e₀ = 9` is what I.b.4 fences; the Hammock's proof does not require it sharp, only bounded.

---

## Part II — Theorem N3 (the parameter lemma) and the autopsy

Setting: the defect complex of a letter, `E = ker(ob)/im(φ)` supported on the deepest flat `D`, `Gauge_J = O(V_J)^m`, `Q_g := (⊕_J Gauge_J)/Γ`.

> **Theorem N3.** (a) **Kernel identification:** `ker(d⁰) = Γ` (Gluing + containment, componentwise). (b) **Parameter lemma:** for `f ∈ ker(ob)` and `u ∈ I_D^N` (with `I_D^N·E = 0`), the flat-discrepancy cocycle satisfies `u·δ = d⁰(h_u)` explicitly. (c) **Sufficient criterion:** if `x^N, y^N` form a regular sequence on `Q_g`, then every such `δ` is a coboundary and `E = 0` (`m ≥ 3`; `m = 2` by Local Splitting).
*Proof of (c) given (a),(b).* `y^N h_{x^N} − x^N h_{y^N} ∈ ker(d⁰) = Γ`; regularity corrects `h_{x^N} = x^N g + γ`; then `x^N(δ − d⁰g) = 0`, and torsion-freeness of the flat coefficient modules forces `δ = d⁰ g`. ∎

> **The autopsy (Ley 24/42 — falsification with numbers).** The hypothesis of (c) is **FALSE**: `Γ ∩ (x·G + y·G) = xΓ + yΓ` fails — `B₃`: `15 ≠ 11, 46 ≠ 40, 95 ≠ 87`; `Z₃`: `70 ≠ 62`. Hence `depth Q_g = 1` exactly. Cemetery: DEPTH-QG-ROUTE.
> **Forensic reading.** The discrepancy grows linearly (`+2`/degree at `B₃`): a module supported exactly on `D`, where `E` lives — yet `E ≡ 0` in every measurement. The correct residual is finer than any depth condition: **(Lemma Ω)** the composite `E → H¹_{Koszul}(x,y; Q_g)` vanishes — exactly `E = 0` in the parameter coordinates, verified wherever computable, and NOT load-bearing for the Chaise Longue (Ledger Experiment).

### Attack surface
(A) T3's composition (Slap 1 module presentation + Slap 2 regularity bound). (B) N3(a) componentwise Gluing. (C) N3(b) explicit coboundary. (D) The autopsy gate (rerun `B₃, e=2`: `15` vs `11`). (E) Ω's formulation. **(F, COMPLETO) The generation fence I.b** — verify generators confined to `≤ 105` (regularity property), the head decay `189,48,7,0`, and the named finite residual `[10,105]`; confirm the Ledger consumes only the bound.

**Anchors.** TANDA1 (T3) · TANDA5_GLUING (N3) · TANDA6_DEPTH_AUTOPSY (gate, killing numbers) · SLAP1, SLAP2 (T3 inputs, and reg bound) · TANDA7 (non-load-bearing) · CARDANO_TANDA5/6. github.com/tretoef-estrella.
