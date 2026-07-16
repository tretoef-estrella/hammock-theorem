# Where to attack The Hammock Theorem

We believe the proof is correct, and its computational layer is shielded — every number is a finite computation over $\mathbb{F}_3$ reproduced in Macaulay2 and independent engines. A hostile referee should therefore not spend time re-checking arithmetic; they should attack the **logic**, at the joints where a gap could live if one exists. We point at those joints ourselves. This is where we would look first.

---

## The two conceptual reserves (specialist territory — the real frontier)

These are not computation gaps. No amount of machine checking closes them; they need a human expert. The paper grades both honestly.

### 1. The level-2 identification (the sharpest joint)

We prove that the multiplicity of the antisymmetric line ($\mathrm{sgn}$) in $H_1(K(3,3))$ is exactly $1$ — measured in two engines, over $\mathbb{Q}$ and $\mathbb{F}_3$, isolated as a Maschke-free kernel. That number is a theorem.

What is **derived, not machine-settled**, is the *identification*: that the global codim-2 level-2 collar transient **is** exactly this local $H_1(K(3,3))$ with this $S_3$-action, via the Central Defect localization and the antisymmetry `SLAP5 5A(iii)`. The multiplicity being $1$ is settled; the claim that the phenomenon lives in precisely that object is a structural identification, not an unwound isomorphism in the big module.

**How to attack it:** find a homological-algebra argument that the level-2 transient is *not* canonically that object — or, conversely, supply the exact sequence / spectral sequence that transfers the local star defect to the global slack. See [`theorems/key/level-2-mechanism.md`](theorems/key/level-2-mechanism.md) and [`theorems/key/central-defect-law.md`](theorems/key/central-defect-law.md).

### 2. The Degtyarev–Shimada dictionary

The floor (Proposition 1.3) rests on the identification of the target polynomial $P_3$ with the [DS] rank quantity that Conjecture 1.2 concerns. This is a single imported ingredient, used only there, isolated and corroborated three independent ways in [`theorems/key/ds-import-note.md`](theorems/key/ds-import-note.md).

**How to attack it:** show that the hypothesis [DS] uses does not coincide exactly with ours — a change of category, a hidden hypothesis, a translation defect between the integral Hodge statement and the coordinate ring $R=S/E$. If that dictionary is perfect, the theorem stands; if not, the internal proof is still correct but proves a different statement.

---

## The load-bearing logical joints (attack the pencil, not the code)

In decreasing order of the attention they deserve:

**(i) The clamp — Theorem 4.3.** The composition "crude Koszul ceiling minus slack law" into the clamped identity, summed over the (growing) collar to equal the budget $B_3(q)$. Two naive alternative compositions were falsified on the bench and are tombstoned below with their killing numbers. Attack: make $\mathrm{Collar}(q) > B_3(q)$ at some $q$, breaking the squeeze against the floor.

**(ii) The census threshold — G1.** The census law $\sigma_e$ is proven eventually-polynomial with the onset bounded by the Hilbert-series numerator ($\deg Q - d = 8$, $\mathrm{reg}(R)=k(k+1)=12$). Attack: exhibit a minimal generator past degree $12$ that the numerator bound misses. See [`theorems/supporting/threshold-parameter.md`](theorems/supporting/threshold-parameter.md) and [`theorems/supporting/g1-onset-structural.md`](theorems/supporting/g1-onset-structural.md).

**(iii) The pinch surjectivity — Theorem 3.1.** The map $\Phi_c(x)=(x|_{V_J}/\Pi_J)_J$ is claimed onto. We upgrade this to a finite theorem (a separating swap hyperplane over all $105\cdot 104$ ordered pairs) **bridged** to the global Covering Lemma ($J\triangle J'$ = even alternating cycles, all $5460$ pairs). Attack the bridge: does the pairwise property truly force the global surjection, with no ghost syzygy in high degrees? See [`theorems/key/covering-lemma.md`](theorems/key/covering-lemma.md).

**(iv) Flat completeness — Theorem 1.4.** Every floor coefficient is a Möbius crosscut over the flat lattice; a missing flat type would shift a coefficient. Completeness is proven two ways: the Pattern Lemma (a characteristic-3 parity argument, $2s=0\Rightarrow s=0$) **and** an exhaustive geometric enumeration over $\mathbb{F}_3$. Attack: find a codimension-$\le 3$ flat type the enumeration misses. Re-run [`engines/python/HAMMOCK_H1_FLAT_ENUMERATOR.py`](engines/python/HAMMOCK_H1_FLAT_ENUMERATOR.py) — it is the cheapest global sanity check in the project.

**(v) The $q=27$ blind spot.** At $q=9$ the summed top zone is empty ($\mathrm{Top}(9)=0$, since the boundary degrees $\{9,10,11\}$ sit below the first annihilator class $c=12$), so the biggest Macaulay2 census does not exercise the summed annihilator. The law is instead measured at $q=9$ in the collar dual, and its first class $\bar\alpha_{12}=105$ directly in Macaulay2; a saturated $q=27$ census is genuinely uncomputable ($27^8$). Attack: independently verify a higher annihilator class beyond duality, or challenge the hockey-stick $\mathrm{Top}(q)=105\binom{q-6}{4}$.

---

## The graveyard (streets we walked and buried, with the datum that killed each)

A project that invents its results has no graveyard. Ours records the dead ends by the byte-exact number that falsified them — the discipline that a claimed advance is not an advance until a datum forces it.

| Tombstone | The claim it buried | The datum that killed it |
|---|---|---|
| **NAIVE-PRODUCT-MU** | the floor's $q^1$ coefficient by a naive product-of-Möbius | $-1617 \ne -2037$ |
| **NAIVE-CEILING-MINUS-SLACK** | the collar budget by a naive crude-minus-slack, wrong composition | $-966833 \ne 206011$ |
| **FLAT-COUNT-MISCOUNT-B4** | a miscount of the $B_4$ codim-3 flats | broke the $q^1$ coefficient against the sealed anchor |
| **KEPLER-VINDICATED** | a pattern the campaign's own constitution had raised to a "law" — measured at two points, sung as $\forall$ | falsified when the raw numbers were subtracted; a two-point pattern is a candidate, not a law |
| **NAIVE-IE-STAR-SYZYGY** | the star collar syzygy by naive inclusion–exclusion over the 16 star flats | gave defect $[16,24,32,39]$, not the clean nerve term (Frobenius truncation does not commute with Tor) |

The full campaign graveyard and the discipline that produced it are told in **[THE_STORY.md](THE_STORY.md)**.

---

## The bottom line

If you can break any link, the byte-exact discrepancy is worth more to us than agreement. The computational layer is shielded; the two conceptual reserves above are exactly what a human referee's independent eye is for. That review — not more machine checking — is what would turn this candidate into a confirmed result.
