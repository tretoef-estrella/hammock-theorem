
# The supporting lemmas

The proof of the Hammock Theorem is a chain: each link lives in its own standalone write-up, so that no step is trusted "by reference." This index maps every standalone in the repository to the role it plays in the proof.

Each write-up is self-contained; only what the dimension-six proof consumes is used here. The Sofa Theorem ($k=2$) is the strongest independent cross-calibration, and is public with its own DOI.

---

## The eleven key theorems

These are the load-bearing links, in the order the proof consumes them.

| # | File | Role |
|---|------|------|
| 1 | [object-formal-definition.md](supporting/object-formal-definition.md) | the arrangement, the ideal, the truncated quotient, fixed formally |
| 2 | [odd-symmetric-theorem.md](key/odd-symmetric-theorem.md) | $E=\bigcap_J I_J$, radical; $R$ the reduced CI coordinate ring |
| 3 | [star-architecture-theorem.md](key/star-architecture-theorem.md) | complete flat classification (words $B_j$, $Z_j$); Pattern Lemma |
| 4 | [floor-crosscut-theorem.md](key/floor-crosscut-theorem.md) | $A_3\ge P_3$; every floor coefficient by Möbius crosscut |
| 5 | [ds-import-note.md](key/ds-import-note.md) | the one imported ingredient: $P_3$ = the [DS] rank quantity |
| 6 | [recognition-theorem.md](key/recognition-theorem.md) | window census independent of tower level |
| 7 | [unified-annihilator-law.md](key/unified-annihilator-law.md) | top zone as annihilator, $\bar\alpha_c=105\binom{c-9}{3}$, explicit pinch |
| 8 | [covering-lemma.md](key/covering-lemma.md) | lifting polynomials $X_J$ exist; even alternating cycles |
| 9 | [slack-species-derivation.md](key/slack-species-derivation.md) | slack composes stratum-by-stratum; not a fit |
| 10 | [central-defect-law.md](key/central-defect-law.md) | codim-2 defect as Čech $H^1$ of the nerve $K(3,3)$ |
| 11 | [level-2-mechanism.md](key/level-2-mechanism.md) | three swap families collapse to one; $\mathrm{mult}(\mathrm{sgn})=1$ |
| — | [ledger-collar-budget.md](key/ledger-collar-budget.md) | the quartic identity collapsing the tower to the collar budget |

---

## The further supporting standalones

Consumed inside the links above, each self-contained.

### The floor and the flat lattice
- [letter-hilbert.md](supporting/letter-hilbert.md) — the letter series $H(B_m)$, $H(Z_m)$ closed for every size (feeds the CI Hilbert function).
- [third-coefficient.md](supporting/third-coefficient.md) — the codim-2 stratum coefficients, with the confinement lemma making the list provably complete at each order.
- [radicality-theorem.md](supporting/radicality-theorem.md) — the divisibility injection $\bigoplus_J \mathcal{O}(V_J)$ with kernel $E$, underpinning both the annihilator upper bound and the diagonal pattern.

### Recognition and the census threshold
- [threshold-parameter.md](supporting/threshold-parameter.md) — the census threshold formally bounded, $\mathrm{reg}\le (2k+1)!!$.
- [g1-onset-structural.md](supporting/g1-onset-structural.md) — G1 closed at $k=3$: the Hilbert-series numerator ($\deg Q - d = 8$) makes the census law a theorem for all $e\ge 9$.
- [slap1-hilbert.md](supporting/slap1-hilbert.md) · [slap2-regularity.md](supporting/slap2-regularity.md) — the Hilbert and regularity lemmas feeding the threshold.

### The collar: crude ceiling and slack
- [cascade-collapse.md](supporting/cascade-collapse.md) — the crude Koszul ceilings as one closed graded Euler characteristic for all collar levels at once (Theorem 4.1).
- [unified-slack-law-dim6.md](supporting/unified-slack-law-dim6.md) — the complete dimension-six slack law, both branches, every $q$.
- [gluing-defect-theorem.md](supporting/gluing-defect-theorem.md) — the codim-1 Gluing Law: $\mathrm{slack}_{\mathrm{swap}}=\binom{k}{2}\binom{f+k-1}{k-1}$ per swap flat.
- [slap4-vanishing.md](supporting/slap4-vanishing.md) — swap-divisibility (the degree-$12=k(k+1)$ Swap Ramp).
- [slap5-ceiling.md](supporting/slap5-ceiling.md) — the antisymmetry $\delta_{ml}=-\delta_{lm}$ (5A(iii)) that forces the $\mathrm{sgn}$ selection a priori.

### The eigenvector closure and G2
- [eigenvector-law.md](supporting/eigenvector-law.md) — branch-2 closed by the eigenvectors of the $2\times 2$ swap ($t^2-1$ over $\mathbb{F}_3$).
- [monodromy-matrix-supplement.md](supporting/monodromy-matrix-supplement.md) — the branch-2 constants traced to flat multiplicities ($350=630-280$, $903=98+840-35$).
- [cardano-g2-closure-audit.md](supporting/cardano-g2-closure-audit.md) — the G2 ceiling identity closed under hostile audit, 4/4 byte-exact, two-tower cross-check.

---

## How the paper rests on its theorems

The proof consumes, in order: the object definition → the flat classification and completeness (Pattern Lemma **and** exhaustive enumeration) and the Möbius table → the letter series → the floor → Recognition and the census threshold → the annihilator pinch with the explicit surjection and Covering Lemma → the crude ceiling → the slack chain, derived coefficient-by-coefficient with the level-2 collapse fused → the collar budget, with the Ledger certified in exact rational arithmetic. The Sofa Theorem is the $k=2$ cross-calibration.

The end-to-end map from every number to its exact script is the [reviewer evidence dossier](../verification/HAMMOCK_REVIEWER_EVIDENCE_DOSSIER.md).
