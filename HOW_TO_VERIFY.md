# How to verify The Hammock Theorem

Every load-bearing number is a finite computation over $\mathbb{F}_3$ on a fixed, $q$-free object. Nothing here needs the full $9^8$ (let alone $27^8$) ambient; each certificate runs in seconds to a few minutes on a laptop. This document tells you exactly what to run and what you must get.

The primary verification is in **Macaulay2 v1.26.06** (the community-standard system). The independent Python engines require only Python 3 with `sympy` (`pip install sympy`).

---

## 0. Prerequisites

- **Macaulay2** ≥ 1.26 — [macaulay2.com](https://macaulay2.com). The scripts are pure `ZZ/3` linear algebra and Hilbert-function calls; no external packages.
- **Python 3** with `sympy` for the Ledger certificate. The other Python engines use only the standard library.

Run Macaulay2 scripts with, e.g.:
```
M2 --script engines/macaulay2/HAMMOCK_H3_THREE_TO_ONE_MECHANISM.m2
```
Run Python engines with:
```
python3 engines/python/HAMMOCK_H1_FLAT_ENUMERATOR.py
```

---

## 1. The two tower rungs (Macaulay2)

The main census run reproduces five prior sealed anchors byte-exact, then computes the sixfold rungs. See the log:
**[`engines/logs/HAMMOCK_MACAULAY2_MAIN_CENSUS_LOG.txt`](engines/logs/HAMMOCK_MACAULAY2_MAIN_CENSUS_LOG.txt)**

You must get:

| Rung | Value | Meaning |
|---|---|---|
| $A_3(3)$ | **1107** | $=P_3(3)$, sealed direct computation |
| $A_3(9)$ | **345465** | $=P_3(9)$, with full 33-degree census, confinement top $32=4\cdot 8$ |

The base rung is additionally re-derived in an independent engine (`engines/python/HAMMOCK_H4_TORSION_BASERUNG.py`): the integer multiplication matrix $G_3$ has $\mathrm{rank}_{\mathbb{F}_3}=\mathrm{rank}_{\mathbb{Q}}=5454$, so $A_3(3)=6561-5454=1107$ in both characteristics — no 3-torsion rank-drop.

---

## 2. The window census $\sigma_e$ (Macaulay2)

The census module $M(3)$ over $R=S/E$ is gated on the sealed heads and its Hilbert function is read out past the onset. Logs:
**[`engines/logs/HAMMOCK_REG_M3_LIGHT_v3_LOG.txt`](engines/logs/HAMMOCK_REG_M3_LIGHT_v3_LOG.txt)** and **[`engines/logs/HAMMOCK_REG_M3_HILBERTSERIES_v4_LOG.txt`](engines/logs/HAMMOCK_REG_M3_HILBERTSERIES_v4_LOG.txt)**.

You must get:
- Heads $\sigma_{0..8}(3)=0,0,1,7,29,90,252,636,1435$.
- Out-of-sample $\sigma_{9},\sigma_{10},\sigma_{11},\sigma_{12}=2898,5313,8988,14238$, each equal to the census cubic $\tfrac{105}{2}e^3-945e^2+\tfrac{12285}{2}e-14112$.
- Reduced Hilbert-series numerator: $\deg Q = 12 = \mathrm{reg}(R)=k(k+1)$, $\dim d=4$, so $\deg Q - d = 8$ — making $\mathrm{HF}=\mathrm{HP}$ for **all** $e\ge 9$ a theorem, with no possible high-degree deviation.

---

## 3. The Ledger identity (Python / SymPy — engine-independent)

```
python3 engines/python/HAMMOCK_LEDGER_SYMPY_CERTIFICATE.py
```
Log: **[`engines/logs/HAMMOCK_LEDGER_SYMPY_CERTIFICATE_LOG.txt`](engines/logs/HAMMOCK_LEDGER_SYMPY_CERTIFICATE_LOG.txt)**.

You must get, in exact rational arithmetic:
- $ZA+W+\mathrm{Top}+B_3-P_3 \equiv 0$ (symbolic difference exactly zero).
- $q=9$ zone slices $ZA,W,\mathrm{Top},B_3 = 5516,\,133938,\,0,\,206011$, summing to $345465$.

---

## 4. The annihilator's first class $\bar\alpha_{12}=105$ (Macaulay2)

```
M2 --script engines/macaulay2/HAMMOCK_ANNIHILATOR_A12_MACAULAY.m2
```
Log: **[`engines/logs/HAMMOCK_ANNIHILATOR_A12_MACAULAY_LOG.txt`](engines/logs/HAMMOCK_ANNIHILATOR_A12_MACAULAY_LOG.txt)**.

You must get `GATE true`: over all $105\cdot 104$ ordered sheet pairs, each sheet has a separating swap hyperplane on every other sheet, so the lifting polynomials $X_J$ exist and the pinch $\Phi_{12}$ is onto per summand, giving $\bar\alpha_{12}=105$ (one annihilator class per sheet) — measured tower-free on the fixed arrangement over $\mathbb{F}_3$.

---

## 5. The level-2 mechanism, two engines

Macaulay2:
```
M2 --script engines/macaulay2/HAMMOCK_H3_THREE_TO_ONE_MECHANISM.m2
```
Python:
```
python3 engines/python/HAMMOCK_H3_THREE_TO_ONE_MECHANISM.py
```
Log: **[`engines/logs/HAMMOCK_H3_THREE_TO_ONE_MECHANISM_LOG.txt`](engines/logs/HAMMOCK_H3_THREE_TO_ONE_MECHANISM_LOG.txt)**.

You must get, over $\mathbb{Q}$ **and** over $\mathbb{F}_3$:
- $b_1 = \dim H_1(K(3,3)) = 4$.
- $H_1(K(3,3)) = \mathrm{triv}(1)\oplus\mathrm{sgn}(1)\oplus\mathrm{std}(2)$.
- $\mathrm{mult}(\mathrm{sgn}) = 1$ — three swap families collapse to one. In Macaulay2 this prints `GATE (b1=4 and sgn=1): true`.

The $\mathrm{sgn}$-line is isolated as a **kernel**, $\ker(\sum_\tau(\tau+1))$ — needing no averaging ($1/|G|=1/6$ does not exist in $\mathbb{F}_3$) and no Maschke splitting, so the computation is valid in the non-semisimple regime. Explicit $4\times 4$ action matrices are in Appendix A of the paper.

---

## 6. The hardening shields (independent Python engines)

Each is a self-contained gated script; run any of them directly.

| Script | Checks |
|---|---|
| [`HAMMOCK_H1_FLAT_ENUMERATOR.py`](engines/python/HAMMOCK_H1_FLAT_ENUMERATOR.py) | exhaustive flat enumeration over $\mathbb{F}_3$: $630;\ 280/315/210;\ 35/28/210$; point count $\lvert X(\mathbb{F}_3)\rvert=1107$ |
| [`HAMMOCK_H2_NERVE_CECH.py`](engines/python/HAMMOCK_H2_NERVE_CECH.py) | the type-(i) star nerve is $K(3,3)$, $b_1=4$, Čech $H^1=4\,h_L$; star saturates at $q=3$ (279) |
| [`HAMMOCK_H3_STAR_BLOCK.py`](engines/python/HAMMOCK_H3_STAR_BLOCK.py) | the star as a 6-variable CI; census reconstruction validated at $q=3$ (279) |
| [`HAMMOCK_H4_TORSION_BASERUNG.py`](engines/python/HAMMOCK_H4_TORSION_BASERUNG.py) | no 3-torsion rank-drop: $\mathrm{rank}_{\mathbb{F}_3}=\mathrm{rank}_{\mathbb{Q}}=5454$, $A_3(3)=1107$ |
| [`HAMMOCK_H5_RECOGNITION_BOUNDARY.py`](engines/python/HAMMOCK_H5_RECOGNITION_BOUNDARY.py) | the four heavy families are disjoint for all $e<q$, collapse at $e=q$; shared-edge cancellation-free |
| [`HAMMOCK_H6_SEP_FRAME.py`](engines/python/HAMMOCK_H6_SEP_FRAME.py) | no $\mathbb{F}_3$ frame at $k=3$; certified SEP frames over $\mathbb{F}_9$ and $\mathbb{F}_{27}$ |
| [`HAMMOCK_FINAL_MASCHKE_AND_ANNIHILATOR.py`](engines/python/HAMMOCK_FINAL_MASCHKE_AND_ANNIHILATOR.py) | $\mathrm{sgn}$ isolated as kernel (Maschke-free); $\bar\alpha_{12}=105$ tower-free; $J\triangle J'$ = even alternating cycles (all 5460 pairs) |
| [`HAMMOCK_SEMIFINAL_ANNIHILATOR_AND_PINCH.py`](engines/python/HAMMOCK_SEMIFINAL_ANNIHILATOR_AND_PINCH.py) | pinch surjectivity over 5460 pairs; annihilator law measured at $q=9$ in the dual; Ledger fires at $q=27$ ($\mathrm{Top}=628425$) |

---

## What a full check looks like

If you want to reproduce the whole thing from scratch, in order:

1. Run §1 (Macaulay2 census) — the two rungs `1107`, `345465`.
2. Run §2 (census module) — the $\sigma$-law and its Hilbert-series bound.
3. Run §3 (SymPy Ledger) — the identity and the $q=9$ slices.
4. Run §4 and §5 (Macaulay2 annihilator + level-2) — the two `GATE true`.
5. Run §6 (the seven Python shields) — each gated.

Every number above is cross-referenced to its exact place in the paper by **[`verification/HAMMOCK_REVIEWER_EVIDENCE_DOSSIER.md`](verification/HAMMOCK_REVIEWER_EVIDENCE_DOSSIER.md)**, and the completed hardening round is summarized in **[`verification/HAMMOCK_HARDENING_COMPLETE.md`](verification/HAMMOCK_HARDENING_COMPLETE.md)**.

If any single number disagrees, that byte-exact discrepancy is exactly what we want to hear about.
