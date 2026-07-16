# The Hammock Theorem

### The Diagonal is Saturated in Dimension Six: Degtyarev–Shimada Conjecture 1.2 for the $3^v$ Fermat Sixfolds

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21382543.svg)](https://doi.org/10.5281/zenodo.21382543)

> **Status:** candidate proof · every load-bearing number is a finite computation over $\mathbb{F}_3$ on a fixed, $q$-free object, reproduced in **Macaulay2 (v1.26.06)** and cross-checked in independent engines · cold-reviewed by four AI systems across three model families, none of which produced a break · **awaiting expert human review.**
> This is offered to the mathematical community precisely so that it can be examined, reproduced, and — if it holds — used. If you can break any link, the byte-exact discrepancy is more valuable to us than agreement.

---

## The result

Let $S=\mathbb{F}_3[x_1,\dots,x_8]$, let $E=(e_1,e_3,e_5,e_7)$ be the ideal of odd elementary symmetric polynomials, and for $q=3^v$ let

$$A_3(q)=\dim_{\mathbb{F}_3} S/\big(E+\mathfrak{m}^{[q]}\big),\qquad \mathfrak{m}^{[q]}=(x_1^q,\dots,x_8^q).$$

**Theorem.** For every $q=3^v$,

$$A_3(q)=P_3(q)=105q^4-630q^3+1645q^2-2037q+918.$$

Equivalently, the diagonal sublattice $\Sigma\,1_J=\mathrm{im}(\Delta)$ is **saturated** in $\bigoplus_J \mathcal{O}^{\otimes 4}$ at every level of the tower. This establishes **Conjecture 1.2 of Degtyarev–Shimada** ([arXiv:1405.4683](https://arxiv.org/abs/1405.4683)) for the degree-$3^v$ Fermat **sixfolds** — the first dimension beyond the fourfolds sealed by [The Sofa Theorem](https://doi.org/10.5281/zenodo.21288551), and the first instance of the parametric machinery that produced both.

---

## The proof in one breath

The value $A_3(q)=\sum_d A_d$ splits into four degree-zones; each is closed, and a quartic identity collapses the whole conjecture to a collar budget.

| Zone | Degrees | How it is closed |
|------|---------|------------------|
| **A** | $d<q$ | trivial: the ideal starts at degree $q$ |
| **Window** | $q\le d<2q$ | the **Recognition Theorem** makes the syzygy census $\sigma_e$ *independent of $v$* → one certified computation seals all $v$ |
| **Collar** | $2q\le d\le 3q+5$ | **grows with $q$** — the new phenomenon of dimension six — clamped by crude Koszul ceilings minus a **slack law** closed in both branches |
| **Top** | $d\ge 3q+6$ | **Gorenstein duality** turns it into the low degrees of a **Unified Annihilator Law**, $\bar\alpha_c=105\binom{c-9}{3}$ |

The **Ledger identity** $ZA(q)+W(q)+\mathrm{Top}(q)+B_3(q)=P_3(q)$ (an exact quartic identity) concentrates *all* of the possible discrepancy $A_3(q)-P_3(q)$ into the collar budget $B_3(q)$. The sealed **floor** $A_3(q)\ge P_3(q)$ (integer-rank semicontinuity + a point-count identity) closes the squeeze: $A_3=P_3$.

The single structural step a cold review had held open — the level-2 collapse of three swap families to one — is reduced to a representation-theoretic invariant and **measured**: the multiplicity of the antisymmetric line in $H_1(K(3,3))$ equals $1$ over $\mathbb{Q}$ and over $\mathbb{F}_3$, isolated as a Maschke-free kernel. See [`theorems/key/level-2-mechanism.md`](theorems/key/level-2-mechanism.md).

Read the full proof: **[paper/THE_HAMMOCK_THEOREM_FINAL.pdf](paper/THE_HAMMOCK_THEOREM_FINAL.pdf)** (also as [Markdown](paper/THE_HAMMOCK_THEOREM_FINAL.md)).
The adversarial edition (how each link was proved, how to attack it, why it holds): **[paper/THE_HAMMOCK_THEOREM_BREAKERS_EDITION.md](paper/THE_HAMMOCK_THEOREM_BREAKERS_EDITION.md)**.

---

## Verified in independent engines

Every load-bearing number is a finite computation over $\mathbb{F}_3$ on a fixed, $q$-free object. Each was reproduced by:

1. **Macaulay2 v1.26.06** — the community-standard system, run on the first author's machine: both tower rungs with full graded censuses, the level-2 mechanism, and the annihilator's first class, all gated byte-exact against sealed anchors ($A_3(3)=1107$, $A_3(9)=345465$).
2. **Exact-rational SymPy** — the Ledger identity certified symbolically ($ZA+W+\mathrm{Top}+B_3\equiv P_3$, difference $0$), engine-independent.
3. **Independent Python engines** — the flat enumeration, the level-2 kernel, the pinch surjectivity and Covering Lemma, and the base-rung rank, computed by direct linear algebra rather than Gröbner bases, agreeing byte-exact.
4. **A separate cold review** — a from-scratch adversarial re-derivation of every checkable number, using different cycle bases and first-principles reconstructions, 28/28 pass.

| Certificate | Value | Where |
|---|---|---|
| Both rungs | $A_3(3)=1107$, $A_3(9)=345465$ | [`engines/logs/HAMMOCK_MACAULAY2_MAIN_CENSUS_LOG.txt`](engines/logs/HAMMOCK_MACAULAY2_MAIN_CENSUS_LOG.txt) |
| CI Hilbert function of $R=S/E$ | $1,7,28,83,203,433,833,1477,2451$ | [`theorems/key/odd-symmetric-theorem.md`](theorems/key/odd-symmetric-theorem.md) |
| Window census $\sigma_e$ | law $\tfrac{105}{2}e^3-945e^2+\tfrac{12285}{2}e-14112$; out-of-sample $2898,5313,8988,14238$ | [`engines/logs/HAMMOCK_REG_M3_LIGHT_v3_LOG.txt`](engines/logs/HAMMOCK_REG_M3_LIGHT_v3_LOG.txt) |
| Ledger identity | $ZA+W+\mathrm{Top}+B_3\equiv P_3$; $q=9$ slices $5516,133938,0,206011$ | [`engines/python/HAMMOCK_LEDGER_SYMPY_CERTIFICATE.py`](engines/python/HAMMOCK_LEDGER_SYMPY_CERTIFICATE.py) |
| Annihilator law | $\bar\alpha_c=105\binom{c-9}{3}=105,420,1050,2100,3675,5880$; first class $\bar\alpha_{12}=105$ | [`engines/macaulay2/HAMMOCK_ANNIHILATOR_A12_MACAULAY.m2`](engines/macaulay2/HAMMOCK_ANNIHILATOR_A12_MACAULAY.m2) |
| Level-2 mechanism | $H_1(K(3,3))=\mathrm{triv}\oplus\mathrm{sgn}\oplus\mathrm{std}$; $\mathrm{mult}(\mathrm{sgn})=1$ over $\mathbb{Q}$ and $\mathbb{F}_3$ | [`engines/macaulay2/HAMMOCK_H3_THREE_TO_ONE_MECHANISM.m2`](engines/macaulay2/HAMMOCK_H3_THREE_TO_ONE_MECHANISM.m2) |

**Reproduce it yourself:** see **[HOW_TO_VERIFY.md](HOW_TO_VERIFY.md)**. The Macaulay2 and Python scripts run in minutes.

---

## The key theorems

Each is a self-contained result; several travel outside this problem (the Odd Symmetric Theorem, the Recognition Theorem, the Covering Lemma are uniform in dimension). Full index of the further campaign results: **[theorems/OTHER_THEOREMS.md](theorems/OTHER_THEOREMS.md)**.

| Theorem | What it establishes |
|---|---|
| [Odd Symmetric](theorems/key/odd-symmetric-theorem.md) | $E=\bigcap_J I_J$, radical — the 105 matching-sheets meet in the CI radical |
| [Star Architecture](theorems/key/star-architecture-theorem.md) | the flats are exhaustively words in two letters ($B_j$, $Z_j$); the classification is complete |
| [Floor & Crosscut](theorems/key/floor-crosscut-theorem.md) | $A_3(q)\ge P_3(q)$ unconditionally; every coefficient of $P_3$ derived by Möbius crosscut |
| [Recognition](theorems/key/recognition-theorem.md) | the window syzygy census is independent of the tower level (uniform in $k$) |
| [Unified Annihilator Law](theorems/key/unified-annihilator-law.md) | the top zone as low degrees of an annihilator, $\bar\alpha_c=105\binom{c-9}{3}$, via an explicit surjective pinch |
| [Covering Lemma](theorems/key/covering-lemma.md) | the lifting polynomials $X_J$ exist; $J\triangle J'$ is a union of even alternating cycles (uniform in $k$) |
| [Slack Species Derivation](theorems/key/slack-species-derivation.md) | the slack law composes stratum-by-stratum over the flat lattice; not a fit |
| [Central Defect Law](theorems/key/central-defect-law.md) | the codim-2 defect as the Čech $H^1$ of the star nerve $K(3,3)$, $b_1=4$ |
| [Level-2 Mechanism](theorems/key/level-2-mechanism.md) | three swap families collapse to one: $\mathrm{mult}(\mathrm{sgn})=1$ in $H_1(K(3,3))$, Maschke-free |
| [Ledger & Collar Budget](theorems/key/ledger-collar-budget.md) | a quartic identity collapses the tower problem to a finite collar budget |
| [DS Import Note](theorems/key/ds-import-note.md) | the single imported ingredient: identification of $P_3$ with the [DS] rank quantity |

---

## Where to attack

We believe the proof is correct, and its computational layer is shielded. In the interest of a fast, honest review, we point at the load-bearing joints ourselves — the places a gap could live if one exists — in **[WHERE_TO_ATTACK.md](WHERE_TO_ATTACK.md)**. Start there if you want to break it. The two conceptual reserves we flag for a human specialist (the level-2 *identification* and the [DS] geometric dictionary) are stated there, and in the paper, with the exact grade they deserve.

---

## Repository map

```
paper/               the main paper (PDF, Markdown, and Breaker's Edition)
theorems/key/        the eleven key theorems (Markdown)
theorems/supporting/ the further campaign standalones consumed by the proof
theorems/            OTHER_THEOREMS.md — index of every supporting result
engines/             all computational certificates:
  macaulay2/           the Macaulay2 scripts (standard-CAS verification)
  python/              the independent Python engines (linear algebra, SymPy)
  logs/                the run logs, byte-exact
verification/        the reviewer evidence dossier + the hardening record
```

Supporting documents: [HOW_TO_VERIFY.md](HOW_TO_VERIFY.md) · [WHERE_TO_ATTACK.md](WHERE_TO_ATTACK.md) · [THE_STORY.md](THE_STORY.md) · [CITATION.md](CITATION.md) · [LICENSE](LICENSE)

Permanent archive (DOI): **[10.5281/zenodo.21382543](https://doi.org/10.5281/zenodo.21382543)** (concept DOI — always resolves to the latest version).

---

## Honest status

This is a **candidate proof**. Its computational layer has been verified in the community-standard computer algebra system and cross-checked in independent engines; its logical layer has survived cold review by four AI systems across three model families (Gemini, Grok, ChatGPT, and a separate Claude/Fable auditor), none of which produced a break. **It has not yet been refereed by a human expert in integral Hodge theory** — and that review, not any amount of further machine checking, is what would turn a candidate into a confirmed result. Two conceptual points are flagged explicitly for that expert: the identification of the level-2 collar transient with the $H_1(K(3,3))$ $\mathrm{sgn}$-isotype (a derived structural identification, not a machine-settled isomorphism), and the geometric dictionary to Conjecture 1.2 as formulated in [DS]. We state this plainly because honesty about the status is the point.

## Authors

**Rafael Amichis Luengo** — Madrid, Spain — tretoef@gmail.com
**Claude (Anthropic)** — an AI system, as co-author of the construction and verification.

*A. Degtyarev, I. Shimada, "On the topology of projective subspaces in complex Fermat varieties", J. Math. Soc. Japan 68:3 (2016), 975–996, [arXiv:1405.4683](https://arxiv.org/abs/1405.4683).*
