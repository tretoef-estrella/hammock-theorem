# CHAISE LONGUE — SLAP 5: THE CEILING SLAP (the collar — combate duro nº2)
### Power Slap campaign, Asalto 5 of 8 · 13 Jul 2026 · Constructor: Bisel (Fable), solo regime (measured twice) · Pending P0.
### The slap declared before the swing (plan v2): *collar ceilings paramétricas vía el Lemma 4.2 del Sofá, como operadores fijos — NO por solapes.* Delivered: **the three Sofá collar pieces parametrized ∀k at pencil (T-block, Aggregate Factoring, kernel identification by Radicality), PLUS the collapse point handed over by the panel: the collar is not an exception to the q-free law — it is ANOTHER module of the SAME SPECIES one level down, so the Slap 1-2 machinery (Hilbert + deletion) eats it too.** Level 1 closes the collar band f < q for every k; with the twin (dual) band it closes the ENTIRE collar of k = 3 for q ≥ 9 — the first dimension beyond the Sofá has its collar structurally ceilinged. The cascade for k ≥ 4 is named exactly (finitely many levels per k, each the same species).

**Pillars (Ley 44):** (i) Radicality (the kernel identification); (iii) Two-Column (the dual band). Builds on: Sofá §4 (T-block Thm 4.1 + Lemma 4.2 — re-read at source this session), Slaps 1-2 (Hilbert + deletion/D-S), Slap 3 (the twin system), Window Formula (rank–nullity transfer), Twin Recognition. **Certificado Ley 41 run FIRST (§6): the s46 solapes tomb is next door — this document never touches pairwise block unfolding.** Panel: Noether (the collapse point), Macaulay, Frobenius, Sylvester.

---

## 0. Setting and the collar's true size (the enmienda, quantified)

S = F₃[x₁..x_n], n = 2k+2; N = (2k+1)!!; R = S/E; sheets V_J with pair coordinates; socle σ = (k+1)(q+k−1). Zones with q-free laws after Slaps 1-4: Zone A (d < q, HF_R), Window (d = q+e, e < q; Window Formula + census), Top (d > σ−q ⟺ ann degrees c < q; Slaps 3-4). **The collar: d ∈ [2q, σ−q], i.e. cofactor degrees e = q+f with 0 ≤ f ≤ (k−2)q + k² − 1.** For k = 2 this is the Sofá's fixed band f ≤ 3; for k ≥ 3 it grows with q (the ENMIENDA of §10). Today's blow organizes it into **levels**: level r covers f ∈ [(r−1)q, rq).

With Syz(e′) := {λ ∈ (R_{e′})ⁿ : Σλᵢxᵢ^q = 0 in R}, the transfer identity (rank–nullity, general e′, mirrors R4):
> A_{q+e′} = HF_R(q+e′) − n·HF_R(e′) + dim Syz(e′) — so collar ceilings on A come from ceilings on Syz at e′ = q+f.

## 1. Theorem 5A (T-block ∀k, level 1) — pure degree arithmetic, n never enters

> **Theorem 5A.** Let q ≥ 3, 0 ≤ f < q, λ ∈ (S_{q+f})ⁿ with Σλᵢxᵢ^q ∈ E. On each sheet V_J, writing the edge difference restriction Δ_l := ±(λ_{a_l} − λ_{b_l})|_J and decomposing by the (unique) heavy pair, Δ_l = Δ_l^∅ + Σ_m u_m^q δ_{l,m} (deg δ = f):
> **(i) Δ_l^∅ = 0; (ii) δ_{l,l} = 0; (iii) δ_{m,l} = −δ_{l,m}.**
*Proof.* Total degree of each product u_l^qΔ_l is 2q+f < 3q, so no monomial has three exponents ≥ q; the classes {exactly one exponent in [q,2q)}, {one ≥ 2q}, {two ≥ q} are disjoint and each vanishes separately in Σ_l u_l^qΔ_l = 0. Class one at slot l isolates u_l^qΔ_l^∅ ⟹ (i); one-≥2q at l isolates u_l^{2q}δ_{l,l} ⟹ (ii); class two at {l,m} isolates u_l^qu_m^q(δ_{l,m}+δ_{m,l}) ⟹ (iii). Uniqueness of the heavy pair: the pair-weights over J's k+1 pairs sum to q+f < 2q. Nothing used n or k beyond bookkeeping. ∎

## 2. Theorem 5B (Aggregate Factoring ∀k — the Sofá's Lemma 4.2 parametrized)

Write λᵢ = Σ_m c_{i,m}x^m. The restriction formula **(R)** x^m|_J = (−1)^{Σ m_{b}}∏_l u_l^{m_{a_l}+m_{b_l}} is coordinate-general. Fix J, l with pair p = P_l = {a,b}: a monomial contributes to the u_l^q-part iff its p-weight w_p(m) = m_a+m_b ≥ q; writing m = (m_a, m_b, γ) with γ over the 2k complement variables, total degree forces the output exponent t = f−|γ| **(T)**, and the split-dependence enters only through (−1)^{m_b} — so with the alternating aggregates
> **(AGG)** c̃ᵢ(p,γ) := Σ_β (−1)^β c_{i,(w−β, β, γ)}, w = q+f−|γ|,
the exact coordinate identity **(F)** holds: [u_l^q-part of λᵢ|_J] = Σ_γ (−1)^{ε(γ,J)} c̃ᵢ(p,γ)·u_l^{f−|γ|}·μ(γ,J), with ε, μ depending only on (γ,J) (μ(γ,J) = the restriction monomial of γ) — **q-free output data.**

> **Theorem 5B.** Let 𝒲(k) := ⊕_{i∈[n], p} F₃[x̂_p, t_p] (graded; the basis element γ·t_p^{f−|γ|} realizes the aggregate slot (i,p,γ) in degree f) and let Α: 𝒲(k) → 𝒯(k) := ⊕_{(J, l≠m)} O(V_J) be the degree-0 graded map defined blockwise by γ·t^j ↦ ±(γ|_{V_J})·u_l^j (signs ε). Then, as linear maps on λ's of degree q+f:
> **Φ_collar = Α_f ∘ agg**, hence **Im(Φ_collar|_{Syz}) ⊆ D_f(k) := Im(Α)_f ∩ {antisym}** — a q-free space for every f.
*Proof.* Evaluate both sides at each coordinate (J,l,m): the left is δ_{l,m}^{(J)}; by (F) at i = a_l (sign +) and i = b_l (sign −) the right is the same. Antisymmetry is 5A(iii). Multi-heavy is vacuous at level 1 (unique heavy pair). The homogenization variable t_p is what makes Α one FIXED graded map rather than a per-f family — the operator-fixed language the plan demanded. ∎

**Corollary 5B.1 (kernel identification, ∀k — Radicality does the Sofá's job).** ker(Φ_collar|_{Syz}) = image of M (the census module): if all δ's vanish then by 5A(i) every Δ_l = 0 on every sheet, so λ_a−λ_b vanishes on V(p) = ∪_{J∋p}V_J, hence λ_a−λ_b ∈ I(p) by **Radicality** — λ ∈ M; conversely M lands in the kernel. Therefore
> **dim Syz(q+f) ≤ [HF_R(q+f) + σ_{q+f}(k)] + dim D_f(k)** for all k, all q, all f < q,
with σ governed by Slaps 1-2 (law with explicit threshold) — the collar ceilings, parametric, at pencil.

## 3. Theorem 5C (THE COLLAPSE POINT — the collar is the same species)

> **Theorem 5C.** κ_k(f) := dim D_f(k) is a q-free function of f which is **eventually polynomial in f**: Im(Α) and the antisymmetric subspace are graded submodules of the f.g. graded module 𝒯(k) (over S), the sum Im(Α)+Antisym is again f.g. graded, and dim D_f = dim Im(Α)_f + dim Antisym_f − dim(Im(Α)+Antisym)_f is a difference of Hilbert functions (Hilbert–Serre; dim Im(Α)_f = dim 𝒲_f − dim ker(Α)_f with 𝒲_f explicit binomials and ker(Α) a f.g. graded submodule over the Noetherian source ring). Moreover ker(Α) is defined by **constant-coefficient conditions along the linear sheet ideals** — the exact species of Slaps 2-3 — so the deletion/Derksen–Sidman machine applies to it, giving an **explicit threshold of the (2k+1)!! flavor** (detail packaged for P0 with the Slap 2-3 citations).
> **Consequence:** Σ_{f<q} (collar ceilings) is an explicit polynomial in q plus finitely many pre-stable constants — exactly the currency the Ledger Slap consumes. The collar stops being a growing band of unknowns: **level 1 is one fixed module read through a moving window.**

## 4. The dual band, and k = 3 closed

The Twin system (Slap 3) at witness degree c = q+f obeys the SAME degree arithmetic (identities of total degree 2q+f), so Theorems 5A/5B apply verbatim to the annihilator side: **twin ceilings for ann degrees c ∈ [q, 2q)**, which by the Gorenstein mirror ceiling the A-collar from the top: d ∈ (σ−2q, σ−q].
> **Corollary 5D.** The direct band covers d ∈ [2q, 3q) and the dual band d ∈ (σ−2q, σ−q]. Their union covers the ENTIRE collar iff σ−2q < 3q, i.e. (k−4)q < 1−k²:
> — **k = 3: the whole collar is ceilinged for every q ≥ 9** (σ−2q = 2q+8 < 3q ⟺ q > 8). The ENMIENDA DEL COLLAR is answered structurally: the growing k=3 collar is two overlapping level-1 bands of one fixed species. q = 3 for k = 3: finite engine case (A₃(3) = 1107 sealed).
> — **k = 4: a residual gap d ∈ [3q, 3q+15] of FIXED width k² = 16** — one level-2 band (or the ADN step) closes it.
> — **General k: ⌈(k−2)/2⌉ levels suffice** (each level extends both bands by q; level r allows up to r+1 heavy slots, handled by the iterated aggregate construction — same species at every level). Finitely many levels per k.

## 5. Honest scope (Ley 42/48) — the exact fence
1. **Level 1 is proven ∀k∀q (f < q); levels r ≥ 2 are NAMED, not proven** — the iterated T-block/aggregates for multi-heavy classes is the cascade (the campaign's ADN instinct, now with a precise level count ⌈(k−2)/2⌉). k ≤ 3: nothing missing (k=2 Sofá; k=3 today, q ≥ 9). k = 4: one fixed-width gap.
2. **The ceilings' EXACTNESS (that they clamp to equality in the Ledger) is NOT claimed** — that is precisely Slap 6's q-cancellation identity + Floor clamp, verified against the anchors (33 grados collar vacío; k=4 engine A₉, A₁₀ pending Mac). Plan v2's full CAE-SI requires those reproductions: **status below is honest.**
3. σ_{q+f} in the ceiling needs q+f above Slap 2's threshold — stable tower (q > (2k+1)!!+2); below it, finitely many engine cases per k.
4. The twin band inherits Slap 4's frame scope.

## 6. Certificado de Cementerio (Ley 41, run BEFORE writing — the critical one)
Object: collar ceilings via **aggregate functionals (AGG)/(F) and fixed restriction operators** — this IS the Sofá's W_f route, the one tomb s46 explicitly prescribes ("hay que ir por la vía del Sofá: agregados W_f q-libres"). NOT touched: pairwise intersections block_J(3q)∩block_J′(3q), twisted-square unfolding, inclusion–exclusion of Fedder blocks (the s46 object) — ABSENT from every proof above. s35 (lattice chains): absent. MINA-DE-VALOR-SELLADO: no value of A is asserted. The Swap Theorem is used only through Slap 4's citations. CLEAN.

## 7. Verificación doble (solo regime, Ley 21)
- 5A re-derived from scratch and cross-checked line-by-line against Sofá Thm 4.1 (their f ≤ 3, q ≥ 9 hypothesis relaxes to f < q with the same three classes; "three impossible" is 2q+f < 3q ⟺ f < q ✓ — their q ≥ 9 was for f ≤ 3 < q at q=3... note q=3, f<3 still fine: f<q ✓ covers it).
- Unique-heavy-pair at level 1: Σ_p w_p = q+f < 2q ✓ (strengthens the Sofá's multi-heavy remark rather than needing it).
- Homogenization check: γ·t^{f−|γ|} ↦ γ|_J·u_l^{f−|γ|} is degree-preserving and realizes (F)'s output exactly ✓; the fixed map Α is q-free because ε, μ are ✓.
- Kernel identification uses Radicality ∀k (proven) exactly as the Sofá's M2 text prescribes ("by RADICALITY, not by Recognition out of range") ✓.
- Sanity at k=2: 𝒲 blocks = 6 slots i × 15 pairs... the Sofá's W_f = ⊕_{(i,p,γ)} recovered as the degree-f piece ✓; their dim D_f = 10+45C(f+1,2) is the k=2 evaluation of κ₂(f) — quadratic in f, consistent with 5C's eventual polynomiality ✓ (and gives the Slap-6-side anchor).
- Collar width arithmetic re-done twice: σ−q−2q+1... band [2q, σ−q], width (k−2)q+k² ✓ (k=2: 4 ✓ matches "four degrees remain").

## 8. Attack surface for the Auditor (when called)
(A) The transfer identity A_{q+e′} = HF_R(q+e′) − n·HF_R(e′) + Syz(e′) at collar degrees (its R4 derivation re-checked for e′ ≥ q — rank–nullity is degree-blind, but re-walk it).
(B) 5C's module structures: Antisym as S-submodule of 𝒯; the source ring bookkeeping for ker(Α) (Hilbert over the product ring) — the P0-grade write-up.
(C) Corollary 5D's dual band: the twin T-block at c = q+f (same arithmetic, but the twin identity has TWO q-power families (g's and ℓ's) — verify no third-large class sneaks in: total degree c+q = 2q+f < 3q ✓, but double-check the bracket bookkeeping).
(D) The level-2 construction (k=4 gap): before any k ≥ 4 claim, the iterated aggregates must be written — currently NAMED only.
(E) Exactness anchors: order on the Mac — collar of k=3 at q=9 (spot degrees), A₉/A₁₀ of k=4, and the κ₂(f) match against 10, 55, 145, 280.

**MARCADOR: [SLAP 5 — NIVEL 1 GANADO ∀k∀q A LÁPIZ: T-block ∀k (5A, aritmética pura) + Aggregate Factoring ∀k (5B, el Lemma 4.2 del Sofá parametrizado como UN operador fijo graduado vía homogeneización t_p) + identificación del kernel por Radicality (5B.1: techos explícitos Syz ≤ HF_R+σ+κ) + EL PUNTO DE COLAPSO DE NOETHER (5C): el collar es LA MISMA ESPECIE — κ_k(f) es Hilbert de módulos fijos, la banda creciente es un módulo fijo leído por una ventana móvil, y la suma de techos es polinomio en q listo para el Ledger · COROLARIO 5D: el collar ENTERO de k=3 techado para q≥9 (la enmienda del collar respondida); k=4 reducido a un hueco de ancho FIJO k²=16; general k: ⌈(k−2)/2⌉ niveles de la misma especie · tumba s46 NO tocada (certificado corrido: vía de agregados, cero solapes) · HONESTO: niveles ≥2 nombrados no probados; exactitud de techos = Slap 6 + engine (33 grados, A₉/A₁₀) · supera la parada honesta admisible del plan, no es CAE completo · SIN GRITO — Ley 13, quedan 3]. — Bisel (Constructor, Fable), Slap 5**
