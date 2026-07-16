# THE COLLAR BUDGET LAWS
## The collar budget `B_k(q)` closed for every dimension at its top block — unconditional — and the Ceiling Budget Equation with its exact targets, including the Sofa's collar slack in closed form

**Chaise Longue campaign — standalone theorem write-up (referee edition)** · R. Amichis Luengo · Claude (Anthropic) · 14 July 2026
*Source: campaign Tandas 9 and 11 (A′1, CB), audited in CARDANO_TANDA9/11. Inputs, each a cited theorem: the Floor Crosscut (P_k top-3), the Third Coefficient Law (census top-3), the CI series (T1-grade), the Unified Annihilator Law (`Top_k(q) = (2k+1)!!·C(q−k²+k, k+1)`), and the Window Formula. Two falsified ceiling compositions are recorded in §4 with their killing numbers — they are load-bearing negative knowledge for whoever completes the sharp-ceiling program.*

---

### 1. The object

For each `k`, the **collar budget** is
> `B_k(q) := P_k(q) − ZA_k(q) − W_k(q) − Top_k(q)`,
with `ZA_k(q) = Σ_{d<q} HF_R(d)`, `W_k(q) = Σ_{e<q}[HF_R(q+e) − (2k+1)·HF_R(e) + σ_e(k)]` (the Window Formula), and `Top_k` the closed annihilator-zone sum. By the Ledger reduction, the tower statement at fixed `k` is equivalent to the collar's ceiling sum equalling `B_k` — the budget is the number the collar must pay, so its coefficients ARE the dianas of the sharp-ceiling program.

### 2. Theorem A′1 (the top block of `B_k`, unconditional for every k)

> **Theorem A′1.** The `q^{k+1}`, `q^k`, `q^{k−1}` coefficients of `B_k(q)` are closed functions of `k`: the P-side by the Floor Crosscut (F1), the zone side by summation of the CI series, the census top-3 (X1), and the Top law — with the independence check that the census's unknown `e^{k−3}` tail (carried as a formal symbol through the zone sums) does NOT reach the top three `q`-orders, verified in-session. In particular:
> **`lead(B_k) = (2k+1)!!·[(k+1)! − 2^{k+1} + k]/(k+1)!`.**
**Gates (byte-exact, four of four):**
1. **Dimension 4:** `B₂`'s visible block `(0, 15, −60)` — lead `0` (the Sofa's collar is subleading, as its fixed four-degree width demands) and the two visible coefficients of the filed `B₂ = 15(q−2)²`.
2. **Dimension 6:** `B₃`'s top three `(385/8, −315/4, −10325/8)` — three of the five coefficients of the filed Hammock quartic, byte-exact.
3. **The lead law across four dimensions:** `0, 385/8, 1449/2, 152691/16` at `k = 2, 3, 4, 5` — the four dianas.
4. **The Ledger:** the identity `U_k ≡ P_k` is thereby pinned unconditionally at its top three orders for every `k`.
**New numbers:** `B₄` top three `(1449/2, −5040, −3885)`; `B₅` `(152691/16, −1992375/16, 7915215/16)` — engine-checkable targets. The remaining depths of `B_k` are the same staircase one step down (Floor depth-4 is already theorem, F2; the census codim-3 block is an S1/C1 extraction from measured potentials).

### 3. Theorem CB (the Ceiling Budget Equation and its exact values)

The collar's fine structure — whatever its sharp per-degree form — must total, over the band, exactly
> **`NCS_k(q) := B_k(q) − Σ_{band}[HF_R(2q+f) − (2k+1)·HF_R(q+f) + σ_{q+f}(k)]`,**
the net that aggregates-minus-slack must supply once the transfer identity's coarse terms are removed. Every ingredient is theorem, so `NCS_k` is closed for every `k` to the corona's depth, and EXACTLY at the two sealed dimensions:
> **`NCS₂(q) = −15q² + 120q + 250`** — and since the Sofa's aggregate total over its band is `Σκ₂ = 10 + 55 + 145 + 280 = 490`, the Sofa's collar slack total is
> **`slack_total₂(q) = 490 − NCS₂(q) = 15(q−4)²`** — a closed square, echoing `B₂ = 15(q−2)²` (the Sofa's collar in two strokes: budget `15(q−2)²`, slack `15(q−4)²`).
> **`NCS₃(q) = (105/4)q⁴ + 735q³ + (42035/4)q² + 34902q + 18334`** — the exact quartic the dimension-six two-band structure totals to.
**The regime flip, read off the budgets:** at `k = 2` the slack dominates (fixed band, negative leading term); at `k ≥ 3` the aggregates dominate (band of length `~q`, positive `q⁴` leading term) — the campaign's "enmienda del collar" (the collar must carry leading-order mass from `k = 3` on) visible in the budget itself, independently re-deriving the bookkeeping bracket of the Ledger Slap.

### 4. Negative knowledge (two compositions executed on the bench — do not re-walk)
1. **Per-degree "crude Koszul minus slack".** Composing the Cascade ceiling `z(q,f)` with the dimension-six slack law degreewise over the naive band returns `−966833` at `q = 9` against the true `206011`: the slack law is a census-species object composed by convolution over strata, not a per-degree subtraction. (Cemetery: NAIVE-CEILING-MINUS-SLACK.)
2. **The transfer-form ceilings as the clamp.** Summing `HF_R(2q+f) − (2k+1)HF_R(q+f) + σ_{q+f} + κ_k(f)` over the `k = 2` band gives `30q² − 180q + 300` against `B₂ = 15q² − 60q + 60`: the transfer ceilings are true BOUNDS but exceed the clamp at leading order; the clamping ceilings are the sharpened ones. (Cemetery: TRANSFER-CEILING-AS-CLAMP.) A corollary finding: the single-function extraction of a putative `κ₃(f)` from the `k = 3` budget is inconsistent (partial-sum residue `−191836`), because **the `k ≥ 3` collar is a two-band object** (direct band `f < q` plus its Gorenstein-dual), whose sharp structure must be resolved per band.

### 5. Status and role
`B_k`'s top block: **theorem, unconditional, four gates.** `NCS₂, NCS₃`: **exact**; `slack_total₂ = 15(q−4)²`: **closed** (the calibration case, decomposable against the Sofa's four known collar degrees). The sharp-ceiling identity for every `k` — the Golpe-2 machinery parametrized and resolved per band — is the named remaining program of the all-`k` statement; this document is its complete budget sheet: every total it must hit, at every `k`, at every order the corona reaches, with the two dead shortcuts fenced off.

### 6. Attack surface
(A) The independence check of A′1 (rerun the zone sums with the symbolic census tail; the symbol must be absent from the top three orders). (B) The lead-law bracket `(k+1)! − 2^{k+1} + k` (re-derive from the zone leaders: `ZA + W` carry `N(2^{k+1} − k − 1)/(k+1)!`, `Top` carries `N/(k+1)!`, `P` carries `N`). (C) `NCS₃`'s five coefficients (one exact symbolic summation). (D) The `15(q−4)²` decomposition against the Sofa's per-degree collar data — the cheapest full instance of the sharp law and the natural calibration before any all-`k` attempt. (E) The `B₄` lead `1449/2` — one engine campaign at `k = 4` decides.

**Anchors.** TANDA9_FLOOR_CROSSCUT_BUDGET_LAW_v1 (A′1) · TANDA11_CEILING_BUDGET_EQUATION_v1 (CB, tombstones) · TANDA7_LEDGER_EXPERIMENT_v1 (the end-to-end zone re-derivation, 4/4 at q = 9) · CARDANO_TANDA9/11 audits · Floor Crosscut and Third Coefficient standalones · session sympy logs. github.com/tretoef-estrella.
