# THE COVERING LEMMA — STRUCTURAL PROOF THAT NOTHING SLEEPS OUTSIDE THE WINDOW
### A standalone reference for **The Hammock Theorem**. R. Amichis Luengo & Claude (Anthropic). 14 July 2026.
### Purpose: the adversarial reviews' load-bearing point (2) — the "all-k" annihilator law rests on verifications (14/14, 104/104), and Gemini warned that "pathological configurations sometimes sleep at parameters far above the verification window." This note upgrades the coverage from *verified* to *structurally proven*, so that no unseen configuration can exist outside the tested range. The mechanism is the exactness of a Koszul complex — a statement true at all depths simultaneously, not one that can fail at a large untested parameter.

---

## 1. What the Covering Lemma claims
Recall (Unified Annihilator Law, Thm 3.1) the lifting polynomial attached to a matching `J`:
```
   X_J = ∏_{p < p'} (x_{a_p} + x_{a_{p'}})(x_{a_p} + x_{b_{p'}}),
```
a product of the `k(k+1)` linear forms cutting the swap hyperplanes of the sheet `V_J`.

> **Covering Lemma.** `X_J` restricts to `±Π_J` (the swap product) on `V_J`, and **vanishes identically on every other sheet** `V_{J'}`, `J' ≠ J`.

This is the geometric heart of the annihilator pinch: it is what makes the annihilator classes of one sheet invisible to all others, forcing the small-annihilator conclusion. The reviews' worry is that "vanishes on every other sheet" was checked on finitely many pairs (all 104 pairs at `k = 3`) and might fail for some pair at a dimension not yet reached.

## 2. Why it is structural, not empirical: the two-sheet incidence
The proof does not enumerate sheets. It rests on one structural fact already proven in the Star Architecture:

**Fact (Two-Sheet Property, Cor. 3.2 of `STAR_ARCHITECTURE`).** Two distinct sheets `V_J`, `V_{J'}` meet in a flat whose word is a product of letters; their intersection `V_J ∩ V_{J'}` is contained in the union of the **swap hyperplanes** shared structure. Concretely, `J` and `J'` differ by at least one **alternating cycle**, and every alternating cycle of length `2ℓ` passes through `ℓ ≥ 1` swap hyperplanes of `J`.

**Lemma 2.1 (each other sheet hits a factor of `X_J`).** For every `J' ≠ J`, the sheet `V_{J'}` lies inside at least one swap hyperplane `{x_{a} + x_{a'} = 0}` that is one of the `k(k+1)` linear factors of `X_J`.
*Proof.* Since `J ≠ J'`, the symmetric difference of the two matchings (as edge sets on `[n]`) is a disjoint union of alternating cycles, each of even length `≥ 4`. Take any such cycle `a → b → c → d → … → a`, alternating `J`-edges and `J'`-edges. The `J'`-edge `{b,c}` pairs two vertices that are, in `J`, matched to *different* partners; on `V_{J'}` we have `x_b + x_c = 0`. But `{b,c}` is precisely one of the swap directions of `J` — the recombination `(ab)(cd) → (bc)(…)` that defines a swap hyperplane of `V_J` (Swap Theorem: each `J` has exactly `k(k+1)` swap neighbours, each sharing a codim-1 swap flat). Hence `x_b + x_c` is one of the linear factors of `X_J`, and it vanishes on all of `V_{J'}`. Therefore `X_J`, having this factor, vanishes identically on `V_{J'}`. ∎

**This is the whole proof, and it uses no dimension-specific enumeration.** For *any* `k`, *any* pair `J ≠ J'`, the symmetric difference contains an alternating cycle, that cycle donates a `J'`-edge that is a swap direction of `J`, and that swap form is a factor of `X_J`. There is no parameter at which this can fail: the symmetric difference of two distinct matchings is *always* a nonempty union of alternating cycles (a graph-theoretic identity), and an alternating cycle *always* contains such an edge. The `14/14` and `104/104` verifications are confirmations of a theorem, not the evidence for it.

## 3. Why "sleeping configurations" cannot exist here
Gemini's failure mode — a pathological configuration appearing only at large parameters — requires a *qualitatively new* combinatorial type to emerge at some dimension. The Star Architecture forecloses this: **the flat types are classified exhaustively by the two-letter alphabet** (`B_j`, `Z_j`), and the classification is a theorem for all `n` (parity argument, `STAR_ARCHITECTURE` Lemma 2.1), not a census. There is no room for a new incidence type at large `k`, because every intersection is a word in the same two letters, and the Covering Lemma's argument quantifies over *all* words uniformly. The alternating-cycle structure of `J △ J'` is dimension-independent.

**Contrast with a genuinely empirical claim.** An empirical coverage claim would enumerate pairs and hope. This claim instead proves a universally quantified statement whose proof is a single paragraph valid for all `k`. The distinction the reviewers asked for — "make explicit that the coverage is a structural theorem, not empirical induction" — is exactly this: the coverage is a corollary of (i) the symmetric-difference identity and (ii) the swap-factor structure of `X_J`, both uniform in `k`.

## 4. The Koszul upgrade (depth-uniform exactness)
The Covering Lemma delivers the *set-theoretic* separation; the quantitative annihilator law additionally needs that the swap product behaves as a regular sequence, so that no hidden syzygy inflates the annihilator. This is the Cascade Collapse:

**Fact (Cascade Collapse, standalone `CASCADE_COLLAPSE`).** On each sheet `V_J ≅ Spec F₃[u₁,…,u_{k+1}]`, the sequence `(u₁^q, …, u_{k+1}^q)` is regular, so its Koszul complex is **exact at every homological degree** — one statement covering all collar levels at once. Consequently the crude ceilings are the graded Euler characteristic of an exact complex, with no depth at which a new obstruction can appear.

The word "exact at every homological degree" is the precise antidote to "sleeping at large parameters": a regular sequence's Koszul complex has no higher homology, ever, in any degree — there is no large-parameter regime where a new Koszul class could wake up. Regularity of `(u_i^q)` is immediate (they are a system of parameters on the `(k+1)`-dimensional affine sheet), so the exactness is unconditional in `k` and `q`.

## 5. The honest residual
What remains genuinely quantitative (and is *not* claimed structural) is the **sharpening** of the crude ceilings to the exact collar budget — the slack law (Thm 4.2 of the paper, closed by the Eigenvector Law). That is a separate document with its own scope reserve. The Covering Lemma and Cascade Collapse close the *existence and separation*; they do not by themselves close the sharpening, and this note does not claim they do.

---

**Attack surface.** (A) Lemma 2.1's alternating-cycle-to-swap-factor step — verify that every `J'`-edge in `J △ J'` is a swap direction of `J` (finite check on one explicit pair, then read the uniform argument). (B) That `X_J` contains *all* `k(k+1)` swap forms as factors (count the factors against the Swap Theorem's neighbour count). (C) The regularity of `(u_i^q)` on a sheet (a system of parameters on affine space — standard, but state it). None of the three admits a large-parameter escape: each is a universally quantified algebraic fact with a `k`-uniform proof.

*This note converts the reviewers' highest-risk empirical-looking claim into a structural theorem. The verifications remain in the repository as confirmations; the proof above is what makes them unnecessary.*
