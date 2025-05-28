---
title: Gdels Incompleteness Theorems
videoId: HeQX2HjkcNo
---

From: [[veritasium]] <br/> 

At its core, mathematics contains a fundamental "hole" that implies we will never know everything with certainty <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. This means there will always be true statements that cannot be proven <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. While the exact nature of these unprovable truths remains unknown, they could be propositions such as the Twin Prime Conjecture <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>, which postulates an infinite number of twin primes (prime numbers separated by only one number, like 11 and 13) <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

This inherent [[incompleteness_of_mathematics | incompleteness of mathematics]] is a consequence of Kurt Gödel's groundbreaking work.

## Historical Context and Hilbert's Dream

For centuries, Euclid's *Elements* were considered the unshakeable foundation of mathematics <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. However, the discovery of non-Euclidean geometries in the 19th century and the poorly defined concept of limits in calculus spurred mathematicians to re-examine the field's foundations <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.

Adding to this upheaval was Georg Cantor's revolutionary work on set theory, which revealed that not all infinities are the same size <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. His [[Cantors Diagonalization Proof | diagonalization proof]] demonstrated that there are more real numbers than natural numbers, classifying infinities as "countable" and "uncountable" <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. This complexity led to a significant debate between "intuitionists," who rejected Cantor's infinities as unreal, and "formalists," who believed mathematics could be established on secure logical foundations through set theory <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.

David Hilbert, a highly influential formalist, championed the idea that a more formal and rigorous system of mathematical proof, grounded in set theory, could resolve all emerging issues in mathematics <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. His famous declaration, "No one shall expel us from the paradise that Cantor has created," underscored his confidence <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.

However, Bertrand Russell's paradox, which demonstrated a contradiction within naive set theory (e.g., the set of all sets that do not contain themselves leads to a logical inconsistency) <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>, exposed a flaw in Hilbert's initial framework. This was resolved by restricting the concept of a set to exclude self-referential paradoxes <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.

Formal systems of proof, which begin with axioms (basic assumed truths) and use rules of inference to derive new statements <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>, were envisioned to create a symbolic logical language with rigid manipulation rules <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. Russell and Alfred North Whitehead's monumental *Principia Mathematica* (1913) was an attempt to realize such a system <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.

Hilbert posed three fundamental questions about mathematics within this formalist framework:
1.  **Completeness**: Is there a way to prove every true statement? <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>
2.  **Consistency**: Is mathematics free of contradictions (i.e., can it simultaneously prove A and not A)? <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>
3.  **Decidability**: Is there an algorithm that can always determine whether a statement follows from the axioms? <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>

Hilbert was convinced the answer to all three was "yes" <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>.

## Gödel's First Incompleteness Theorem

In 1930, Kurt Gödel, a 24-year-old logician, delivered a crushing blow to Hilbert's dream by answering the first question: no, a complete formal system of mathematics is impossible <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>.

Gödel's proof worked by assigning a unique number (a Gödel number) to every basic symbol, number, statement, and even proof within a mathematical system <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>. This allowed him to translate logical and mathematical statements into numerical ones, enabling mathematics to "talk about itself."

The core of his proof involved constructing a self-referential statement, which, when translated into its Gödel number, stated: "There is no proof for the statement with Gödel number G," where G *is* the Gödel number of that very statement <a class="yt-timestamp" data-t="00:19:36">[00:19:36]</a>.

Consider the implications of this statement:
*   **If the statement is false:** This means there *is* a proof for it. But if it's proven true, then the statement "there is no proof for G" becomes true, leading to a contradiction (it's proven, but it says it's unprovable). This would imply the mathematical system is inconsistent <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>.
*   **If the statement is true:** This means there is *no* proof for it. In this case, the system contains a true statement that cannot be proven <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>. This means the mathematical system is incomplete <a class="yt-timestamp" data-t="00:20:33">[00:20:33]</a>.

Since a consistent system cannot prove a false statement, the only logical conclusion is that the statement "this card is unprovable" must be true, and thus, unprovable. Therefore, any basic mathematical system capable of fundamental arithmetic will always contain true statements that have no proof <a class="yt-timestamp" data-t="00:20:40">[00:20:40]</a>. This means truth and provability are not the same <a class="yt-timestamp" data-t="00:21:22">[00:21:22]</a>.

## Gödel's Second Incompleteness Theorem

Gödel's second theorem further dashed Hilbert's hopes by proving that any consistent formal system of mathematics cannot prove its own consistency <a class="yt-timestamp" data-t="00:21:44">[00:21:44]</a>.

Taken together, Gödel's two [[incompleteness_of_mathematics | incompleteness of mathematics]] theorems state that the best one can hope for is a consistent yet incomplete system of mathematics <a class="yt-timestamp" data-t="00:21:56">[00:21:56]</a>. Such a system cannot prove its own consistency, meaning a contradiction could theoretically arise in the future, revealing the system was inconsistent all along <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>.

## Implications for Decidability

The third question Hilbert posed was about [[undecidability_in_mathematical_systems | decidability in mathematical systems]]: whether an algorithm could always determine if a statement followed from the axioms <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>. In 1936, Alan Turing addressed this question by inventing the theoretical construct of the Turing machine, which would later become the basis for modern computers <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>.

Turing developed the "halting problem": can one determine beforehand if a given Turing machine program will halt (finish) or run forever in an infinite loop? <a class="yt-timestamp" data-t="00:24:10">[00:24:10]</a> Turing proved that no general algorithm can solve the halting problem. This means that mathematics is [[undecidability_in_mathematical_systems | undecidable]] <a class="yt-timestamp" data-t="00:26:53">[00:26:53]</a>: there is no algorithm that can always determine whether a statement is derivable from the axioms <a class="yt-timestamp" data-t="00:27:02">[00:27:02]</a>. Consequently, problems like the Twin Prime Conjecture might be fundamentally unsolvable <a class="yt-timestamp" data-t="00:27:08">[00:27:08]</a>.

The concept of undecidability extends beyond pure mathematics, appearing in systems like Conway's Game of Life (where the ultimate fate of a pattern is undecidable) <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>, Wang tiles (determining if a set of tiles can tile the plane) <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>, and even quantum mechanics (determining the spectral gap of a many-body system) <a class="yt-timestamp" data-t="00:27:20">[00:27:20]</a>. Many of these systems are "Turing complete," meaning they can perform any computation a Turing machine can, and thus inherit their own version of the halting problem <a class="yt-timestamp" data-t="00:28:36">[00:28:36]</a>.

## Legacy

While Gödel's theorems showed that mathematics is fundamentally incomplete and cannot prove its own consistency, and Turing proved its undecidability, these realizations did not lead to the collapse of mathematics. Instead, the effort to grapple with these limits transformed our understanding of infinity, led to the invention of the modern computer, and even had a direct impact on shortening World War II through code-breaking <a class="yt-timestamp" data-t="00:32:22">[00:32:22]</a>. The paradoxes of self-reference, initially seen as flaws, became the unexpected foundation for computational theory <a class="yt-timestamp" data-t="00:32:07">[00:32:07]</a>.