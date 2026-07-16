# CHAISE LONGUE — THE UNIFIED ANNIHILATOR LAW (COMPLETO — with the explicit surjection)
### 14 Jul 2026 · Constructor: Bisel · Pending P0 · COMPLETO edition: adds §5, the perfectly-defined map and its surjectivity, answering the referee demand ("when you write 'the pinch closes', where exactly is surjectivity proven?").

> **Theorem (Unified Annihilator Law).** Fix k ≥ 1 and q = 3^v admitting a SEP transverse frame over F_q (Slap 4 scope; guaranteed q ≥ q₀(k); all q for k ≤ 2). Then for every c < q:
> **ᾱ_c(k) = (2k+1)!! · C(c − k², k),**
> with the convention C(m, k) = 0 for m < k. In particular the vanishing below k(k+1) (Slap 4) and the first-class dimension (2k+1)!! at c = k(k+1) are the m < k and m = k cases of one formula. Geometrically: **the annihilator in the stable window is EXACTLY the direct sum of one-sheet-supported classes** — one copy of O(V_J)_{c−k(k+1)} per sheet, glued to nothing.

**Pillars (Ley 44):** (i) Radicality (twice: kernel identification and witness membership); (iii) Two-Column/Bridge. Consumes: Slap 4 (Twisted-Witness + swap divisibility), Swap Ramp Lemma (b_J ⊆ (Π_J)), Slap 2's direct-sum mechanism. Anchors it explains: k=1 mantel 3(c−1) ✓; k=2 Sofá 15·C(c−4,2) SEALED ∀c; k=3 Macaulay q=9 head 105,420,…,5880 ✓ — and the q=9 deviations at c=18,19 EXPLAINED (collar-contaminated, outside the window).

---

## Proof

Write N = (2k+1)!!, Π_J = ∏_{p<p′∈J, ε=±}(w_p + εw_{p′}) the swap product of the sheet V_J (degree k(k+1); Swap Ramp), and note C(c−k², k) = dim O(V_J)_{c−k(k+1)}.

### 1. Upper bound (nobody else fits) — a corollary of Slap 4.
Let x ∈ (C_q)_c. By the Twisted-Witness Lemma and SEP separation (Slap 4), x̄_J := x|_{V_J} vanishes on all k(k+1) swap hyperplanes of every sheet, hence Π_J | x̄_J in the UFD O(V_J): x̄_J = Π_J·h_J with h_J ∈ O(V_J)_{c−k(k+1)}. The assignment x ↦ (h_J)_J is linear, and its kernel is exactly E: if all h_J = 0 then x vanishes on every sheet, so x ∈ ∩I_J = E (Radicality); conversely E maps to 0. Hence
> ᾱ_c = dim (C_q)_c/E_c ≤ Σ_J dim O(V_J)_{c−k(k+1)} = N·C(c−k², k). ∎

### 2. Lower bound (all one-sheet classes exist) — the witness trick.
Fix a sheet J₀ and let A_{J₀} := ∩_{J≠J₀} I_J. **Claim: every x ∈ (A_{J₀})_c lies in (C_q)_c.** Witnesses: y_{ij} := c^{J₀}_{ij}·x. Then, by Frobenius linearity over F_q,
x·g_i^q − Σ_j ℓ_j^q y_{ij} = x·(g_i − Σ_j c^{J₀}_{ij}ℓ_j)^q = x·m_i^q,
where m_i is a linear form vanishing on V_{J₀}. The product x·m_i^q vanishes on V_{J₀} (via m_i) and on every other sheet (via x ∈ A_{J₀}) — hence on all of X, hence lies in E by **Radicality**. ∎(Claim)
The classes so obtained have dimension dim(A_{J₀})_c − dim E_c = dim(b_{J₀})_c, where b_{J₀} = image of A_{J₀} in O(V_{J₀}). Sums over distinct sheets are DIRECT mod E. So ᾱ_c ≥ Σ_J dim(b_J)_c.

### 3. The lifting polynomial X_J: b_J = (Π_J) exactly — the pinch closes.
Swap Ramp gives b_J ⊆ I(Z_J) = (Π_J). For the reverse, lift the single generator: exhibit X_J ∈ A_J with X_J|_{V_J} = ±Π_J.
**Construction.** Order J's pairs p₁ < … < p_{k+1}; fix a positive end a_p in each pair. Define
> **X_J := ∏_{p<p′} (x_{a_p} + x_{a_{p′}})·(x_{a_p} + x_{b_{p′}})** — k(k+1) global linear factors.
*Restriction:* on V_J the two factors restrict to (w_p + w_{p′}) and (w_p − w_{p′}): product ±Π_J ≠ 0. ✓
*Vanishing on every other sheet (Covering Lemma):* each factor x_u + x_v vanishes on V_{J″} iff {u,v} ∈ J″. If J″ contains NO chosen cross pair, then a₁ must be matched inside p₁: a₁b₁ ∈ J″; delete p₁ and induct: J″ = J, contradiction. Hence X_J ∈ ∩_{J″≠J} I_{J″} = A_J. ∎
(*Exhaustive machine check:* k=2 all 14, k=3 all 104; factor count k(k+1) both. The uniform structural proof is `COVERING_LEMMA`.)
Therefore (Π_J) ⊆ b_J ⊆ (Π_J): **b_J = (Π_J)**, dim(b_J)_c = C(c−k², k).

### 4. Pinch.
Lower = Σ_J C(c−k², k) = N·C(c−k², k) = Upper. ∎∎

---

## 5. THE EXPLICIT SURJECTION (COMPLETO — the perfectly-defined map and why it is onto)

A referee reading "the pinch closes" is entitled to a single, perfectly-defined linear map, together with its kernel and the proof that its image is all of the claimed target. Here it is.

### 5.1 The map
Define, on the degree-c piece of the annihilator,
> **Φ_c : (C_q)_c ⟶ ⊕_{J} O(V_J)_{c−k(k+1)},   Φ_c(x) := ( h_J )_J,   where   x|_{V_J} = Π_J · h_J.**

**Φ_c is well-defined (h_J exists and is unique).** Existence: by §1 (Slap 4 swap divisibility), Π_J divides x|_{V_J} in O(V_J). Uniqueness: O(V_J) is the coordinate ring of a linear subspace, hence an integral domain; multiplication by the nonzerodivisor Π_J is injective, so the quotient h_J = x|_{V_J} / Π_J is the unique element of O(V_J)_{c−k(k+1)} with Π_J h_J = x|_{V_J}. Linearity is immediate (restriction and division by a fixed Π_J are linear). ∎

### 5.2 The kernel is exactly E
Φ_c(x) = 0 ⟺ h_J = 0 for all J ⟺ x|_{V_J} = 0 for all J ⟺ x ∈ ∩_J I_J = E (Radicality). Hence **ker Φ_c = E_c**, and Φ_c descends to an injection
> **Φ̄_c : (C_q)_c / E_c ↪ ⊕_J O(V_J)_{c−k(k+1)}.**
This is the content of the upper bound: dim of the source ≤ dim of the target.

### 5.3 The image is everything (surjectivity, proven)
It remains to show Φ̄_c is **onto** — this is the step the phrase "the pinch closes" refers to, now made explicit. Because the target is a direct sum over sheets, it suffices to hit each summand independently and then invoke directness.

**Per-sheet surjectivity.** Fix a sheet J₀ and an arbitrary target element `h ∈ O(V_{J₀})_{c−k(k+1)}` in the J₀-summand (zero in the others). We produce a preimage.
- Since b_{J₀} = (Π_{J₀}) as an ideal of O(V_{J₀}) (§3), the element `Π_{J₀}·h ∈ (b_{J₀})_c` is in the image of the restriction map `(A_{J₀})_c ↠ (b_{J₀})_c` (by definition b_{J₀} is that image). Pick `x₀ ∈ (A_{J₀})_c` with `x₀|_{V_{J₀}} = Π_{J₀}·h`.
- By §2 (the witness trick), `x₀ ∈ (A_{J₀})_c ⊆ (C_q)_c`: it is a genuine annihilator class.
- Its image under Φ_c: on sheet J₀, `x₀|_{V_{J₀}} = Π_{J₀} h`, so the J₀-coordinate of Φ_c(x₀) is `h`. On every other sheet J ≠ J₀, `x₀ ∈ A_{J₀} ⊆ I_J`, so `x₀|_{V_J} = 0` and the J-coordinate is 0.
Thus `Φ_c(x₀) = (0,…,h,…,0)` — the chosen summand element, exactly. ∎(per-sheet)

**Assembling.** Any target `(h_J)_J = Σ_{J} (0,…,h_J,…,0)`. Choosing a preimage `x_J` for each summand as above and setting `x := Σ_J x_J`, linearity gives `Φ_c(x) = (h_J)_J`. Hence **Φ̄_c is surjective**, therefore an isomorphism:
> **(C_q)_c / E_c  ≅  ⊕_J O(V_J)_{c−k(k+1)},   so   ᾱ_c = N·C(c−k², k).**

### 5.4 Why directness is legitimate (no double counting)
The sum `x = Σ_J x_J` could a priori have cross-contributions, but it does not affect the image coordinatewise: the J-coordinate of Φ_c(x) reads `x|_{V_J} = Σ_{J'} x_{J'}|_{V_J}`, and for J' ≠ J the term `x_{J'}|_{V_J} = 0` (since `x_{J'} ∈ A_{J'} ⊆ I_J`). So only the `J' = J` term survives: the coordinate is exactly `h_J`. The directness of the sheet decomposition mod E (Slap 2's restriction mechanism) is precisely this coordinatewise independence. ∎

**Summary of §5.** The map is `Φ_c(x) = (x|_{V_J}/Π_J)_J`; it is well-defined by domain-division, has kernel `E`, and is surjective because each summand is hit by an explicit witness class `x_{J₀} ∈ A_{J₀}` restricting to the desired data on `V_{J₀}` and to 0 elsewhere. Injectivity (upper bound) + surjectivity (lower bound, this section) = isomorphism = the pinch. There is no appeal to intuition: the surjection is the family of witness classes, one per summand.

---

## Consequences
1. **Top zone closed ∀k:** Top_k(q) := Σ_{c<q} ᾱ_c = N·C(q−k²+k, k+1) — closed form (hockey stick), ready for the Ledger.
2. The q=9 head data (105…5880 exact through c=17, then 8785≠8820) is fully explained by the window fence.
3. The annihilator side of the Silver Bridge's U_k is exact.

## Honest scope (Ley 42/48)
Inherits Slap 4's frame scope (SEP over F_q; all q for k ≤ 2; q ≥ q₀(k) in general). Valid in the stable window c < q; the band c ≥ q is collar (Slap 5), untouched. Pending P0.

## Attack surface
(A) §1 swap divisibility (Slap 4). (B) §2 witness membership (the Frobenius step needs c^{J₀} ∈ F_q ✓ frame scope). (C) §3 the Covering Lemma (uniform proof in `COVERING_LEMMA`; 14/14, 104/104 machine). (D) **§5 the surjection** — verify Φ_c is well-defined (domain division), ker = E (Radicality), and per-sheet surjectivity (the witness x₀ restricts to Π_{J₀}h on J₀ and 0 elsewhere). This is the perfectly-defined map the referee asked for.

**Anchors.** SLAP4 (witness + swap divisibility) · SWAP_RAMP (b_J ⊆ (Π_J)) · SLAP2 (direct-sum) · RADICALITY (kernel + membership) · COVERING_LEMMA (uniform) · k=2 Sofá 15·C(c−4,2) SEALED · k=3 Macaulay q=9 head. github.com/tretoef-estrella.
