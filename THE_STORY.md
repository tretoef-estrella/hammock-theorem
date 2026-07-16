# The Story of the Hammock Theorem
### How the Sofa's machinery was carried one dimension up — and what broke, and what held

*This document is the human story behind the mathematics. The proof stands on its own; but the path to it — and the discipline that produced it — is itself the evidence that this is serious work, not a lucky guess. It is the sister of [The Story of the Sofa Theorem](https://doi.org/10.5281/zenodo.21288551); read that one first if you want the origin.*

---

## The problem, in one image

Degtyarev and Shimada conjectured (2017) an integral Hodge statement for the Fermat varieties. The Sofa Theorem closed it for the **fourfolds**. The Hammock asks the next question up: does a single **quartic** polynomial,

$$P_3(q)=105q^4-630q^3+1645q^2-2037q+918,$$

give the dimension $A_3(q)=\dim_{\mathbb{F}_3} S/(E+\mathfrak{m}^{[q]})$, with $S=\mathbb{F}_3[x_1,\dots,x_8]$ and $E=(e_1,e_3,e_5,e_7)$ — for **every** level $q=3^v$ of the infinite tower, all at once, in **dimension six**?

Measuring $A_3(q)$ at one level is easy. Proving it for the whole tower is the wall — and dimension six raised the wall. The grade of the answer itself climbed: from the Sofa's cubic to the Hammock's quartic. One more dimension, one more degree.

## The discipline: inherited, and kept

The Hammock was not a fresh start. It inherited the Sofa's constitution — the rules built to make an amateur's intuition survive contact with rigorous mathematics — and kept them. The governing principle was the same, stated many ways: *measured is not proved.* A value confirmed at $v=1,2$ is an egg, not a law of the tower. The entire fight, again, was to show that every egg is the same egg at another scale.

An honest note on the numbers. The Sofa's story carries exact counts — hundreds of dead ends, hundreds of versions of the running master. Those are the Sofa's, logged in its graveyard. The Hammock inherited the *same* discipline and its own graveyard of named dead ends, but we do not put a Hammock-specific "N dead ends" figure here, because that number is not something we can pull byte-exact from a file — and inventing it would violate the first rule of the project. What we *can* show is the graveyard itself: the streets buried by the number that killed them ([WHERE_TO_ATTACK.md](WHERE_TO_ATTACK.md)) — among them a "law" the campaign's own constitution had raised too early, falsified the moment the raw numbers were subtracted.

The verification is real and reproducible: **Macaulay2 v1.26.06** (the community-standard system) on the first author's machine, plus exact-rational SymPy and independent Python engines. Three AI models (Gemini, Grok, ChatGPT) and a separate Claude auditor cold-reviewed the record; none produced a break.

## The turning points — the ones that did *not* exist in the Sofa

**The bala sin marcas (Frobenius).** In characteristic 3, $(a+b)^3=a^3+b^3$: the cross term carries a factor 3 and vanishes. Raising to $q=3^v$ is *linear* — the bullet passes through the sum and leaves no mark. This is why the tower is tractable at all, in six variables as in three.

**The Recognition Theorem, now uniform in dimension.** Below the threshold $q$, the syzygy census of the middle window does not depend on $v$. In the Hammock this is proved not just along the tower but **uniform in $k$** — the same mechanism seals every dimension at once.

**The collar that grows with $q$.** This is the phenomenon that did not exist in the Sofa. There, the collar was four fixed degrees. In dimension six the collar $2q\le d\le 3q+5$ **grows with the tower level** — a moving target, wider at every rung. This was the wall specific to this dimension, and closing it needed something new.

**The eigenvector mechanism.** The new idea — "strange in the good way." The collar closes by looking at the two eigenvectors of a $2\times 2$ transposition, $t^2-1$ over $\mathbb{F}_3$. The star nerve is $K(3,3)$, first Betti number $b_1=4$, and the surviving family is the antisymmetric line — the $\mathrm{sgn}$-isotype, multiplicity exactly $1$. None of this appears in the Sofa. It is the beating heart of the sixfold closure, and the one joint we flag for a human specialist.

**G1 closed with a Hilbert series.** The census onset was pinned not by luck but by structure: the reduced Hilbert-series numerator has $\deg Q = 12$, dimension $d=4$, so $\deg Q - d = 8$ — forcing the census law for **all** $e\ge 9$. And the clean fact underneath: the regularity is $\mathrm{reg}(R)=k(k+1)=12$. The floor does not merely stop stretching; it stretches by a *fixed rule*.

## What is claimed, and what is not

The mathematics is complete within the campaign's terms: every link is a pencil argument valid for all $v$, or a finite certificate on a fixed object, gated byte-exact. Both tower rungs are measured in Macaulay2 — $A_3(3)=1107$, $A_3(9)=345465=P_3(9)$. G1 is closed at $k=3$; G2's scope reserve is discharged directly (the type-(i) star saturates at both rungs, $279$ and $33129$), with one structural step — the level-2 collapse — reduced to the measured $\mathrm{sgn}$-multiplicity and flagged for expert audit.

**And yet:** this is a *candidate*, not a confirmed record. No human expert in integral Hodge theory has yet examined the pencil logic at the depth a journal referee would. Three AI models and a Claude auditor found no break; that is encouraging, not conclusive — they share a lineage, and a human's independent eye is exactly the check we have not had. We say this plainly, because a result offered with its honest status intact is the only kind worth offering.

## The metaphor

The Sofa got the cat into the water in one room. The Hammock puts the cat into a **bigger** room — one where the floor stretches with every storey. The fear was that it stretched wildly, ungovernably. The discovery was that it stretches by a fixed rule: $\mathrm{reg}=k(k+1)$. The cat of dimension six is also wet. The only way to be sure is for an expert to reach in and feel that it is.

---

*Rafael Amichis Luengo — Madrid — tretoef@gmail.com — github.com/tretoef-estrella*
