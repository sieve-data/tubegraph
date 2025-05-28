---
title: Gdels Incompleteness Theorems
videoId: HeQX2HjkcNo
---

From: [[veritasium]] <br/> 

Gödel's Incompleteness Theorems reveal fundamental limitations within any system of mathematics that is capable of basic arithmetic. They establish that there will always be true statements that cannot be proven <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This means complete certainty is unattainable in mathematics <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## The Unprovable Nature of Truth

The existence of true but unprovable statements implies a "hole" at the bottom of mathematics <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. While the exact nature of these unprovable statements is unknown, they could be conjectures such as [[The Twin Prime Conjecture | the Twin Prime Conjecture]] <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. [[The Twin Prime Conjecture | Twin primes]] are prime numbers separated by a single number (e.g., 11 and 13) <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. The conjecture proposes that there are [[Infinity and countability in mathematics | infinitely]] many such pairs <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. Currently, this conjecture remains unproven, and it might be inherently impossible to prove or disprove <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

This concept of unprovability is linked to **undecidability**, where it is impossible to create an algorithm that can guarantee an answer to a question in a finite amount of time <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. An example of this is [[Conways Game of Life and Undecidability | Conway's Game of Life]] <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>, a system with simple rules that can generate complex, unpredictable behavior <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. Other systems, including Wang tiles, quantum physics, and even some games, also exhibit undecidability <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

## A Revolt in Mathematics: Setting the Stage

The understanding of undecidability and incompleteness emerged from a fundamental crisis in mathematics that began in the 19th century <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

### The Rise of Set Theory and Infinite Controversies

In 1874, [[Georg Cantor and the development of set theory | Georg Cantor]] introduced set theory, a new branch of mathematics dealing with collections of things <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. Cantor explored sets of numbers, such as natural numbers (positive integers) and real numbers (including fractions and irrational numbers) <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. He questioned whether there were "more" real numbers than natural numbers, despite both being [[Infinity and countability in mathematics | infinite]] <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

Through his [[Infinity and countability in mathematics | diagonalization proof]], Cantor demonstrated that not all infinities are the same size <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. He showed there are more real numbers between zero and one than there are natural numbers extending to [[Infinity and countability in mathematics | infinity]] <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. He termed these [[Infinity and countability in mathematics | countable]] and [[Infinity and countability in mathematics | uncountable]] infinities, with many more [[Infinity and countability in mathematics | uncountable]] infinities existing <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

### The Crisis of Foundations

Cantor's work, along with the discovery of non-Euclidean geometries, shattered the long-held belief in Euclid's Elements as the absolute bedrock of mathematics <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>. Concepts like "limits" in calculus were found to be poorly defined, and [[Infinity and countability in mathematics | infinity]] proved far more complex than previously imagined <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

This upheaval led to a major debate:
*   **Intuitionists** (e.g., Henri Poincaré, Leopold Kronecker) viewed Cantor's work as "nonsense" and a "disease" <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>. They believed mathematics was a human creation and that Cantor's [[Infinity and countability in mathematics | infinities]] were not "real" <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
*   **Formalists** (led by David Hilbert) believed that mathematics could be placed on secure logical foundations through set theory <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. Hilbert, a highly influential mathematician, championed Cantor's work, declaring, "No one shall expel us from the paradise that Cantor has created" <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

### Russell's Paradox

In 1901, Bertrand Russell uncovered a serious problem within Cantor's set theory, known as **Russell's Paradox** <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. This paradox arises from considering "the set of all sets that don't contain themselves" (set R) <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>:
*   If R doesn't contain itself, then by definition, it must contain itself.
*   If R does contain itself, then by definition, it must not contain itself.
This creates a self-referential contradiction <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. Russell famously illustrated this with the "barber paradox": a village barber shaves all and only those men who do not shave themselves. Who shaves the barber? <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>

While the intuitionists rejoiced, believing set theory was fatally flawed <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>, formalists like Zermelo resolved the paradox by restricting the concept of a set, excluding collections like "the set of all sets" <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. However, self-reference would reappear.

## Hilbert's Program: The Quest for Certainty

David Hilbert sought to build a new system for mathematical proofs to secure the foundations of mathematics <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>. This formal system would use symbolic logic with rigid manipulation rules <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. Bertrand Russell and Alfred North Whitehead developed such a system in their *Principia Mathematica* (1913) <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>, a vast work aiming for exactness <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.

Hilbert posed three fundamental questions about mathematics:
1.  **Completeness**: Is there a way to prove every true statement? Does every true statement have a proof? <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>
2.  **Consistency**: Is mathematics free of contradictions? Can you simultaneously prove a statement and its negation? <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>
3.  **Decidability**: Is there an algorithm that can always determine whether a statement follows from the axioms? <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>

Hilbert was convinced the answer to all three was "yes," famously declaring at a 1930 conference, "We must know, we will know" <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>.

## Gödel's Incompleteness Theorems: The Dream Crumbles

Just before Hilbert's confident declaration, a 24-year-old logician named Kurt Gödel revealed his findings <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>. He had found the answer to Hilbert's first question (completeness), and the answer was "no" <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>. A complete formal system of mathematics was impossible <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>. Gödel published his proof in 1931, garnering widespread attention <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.

### Gödel's First Incompleteness Theorem

Gödel's proof ingeniously uses logic and mathematics to analyze the system of logic and mathematics itself <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>:

1.  **Gödel Numbering**: Gödel assigned a unique numerical code (a "Gödel number") to every basic symbol, number, statement, and even entire proofs within a mathematical system <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>. This allows mathematical statements and proofs to be treated as numbers <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>.
2.  **Self-Referential Statement**: Using this numbering system, Gödel constructed a specific statement *G* that essentially says: "This statement (with Gödel number G) is unprovable within this system" <a class="yt-timestamp" data-t="00:19:36">[00:19:36]</a>.
3.  **The Paradox**:
    *   **If G is false**: This would mean "This statement is provable" is true, so there is a proof for G. But G itself states it's unprovable, leading to a contradiction. This would imply the mathematical system is inconsistent <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>.
    *   **If G is true**: This means "This statement is unprovable" is true, so there is no proof for G within the system. This implies that the mathematical system contains a true statement that cannot be proven, making it incomplete <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>.

Therefore, any mathematical system capable of basic arithmetic must either be inconsistent (contain contradictions) or incomplete (contain true statements that cannot be proven) <a class="yt-timestamp" data-t="00:20:33">[00:20:33]</a>. Truth and provability are not the same <a class="yt-timestamp" data-t="00:22:18">[00:22:18]</a>.

### Gödel's Second Incompleteness Theorem

Gödel's second theorem delivered another blow to Hilbert's program <a class="yt-timestamp" data-t="00:21:39">[00:21:39]</a>. It states that any consistent formal system of mathematics cannot prove its own consistency <a class="yt-timestamp" data-t="00:21:44">[00:21:44]</a>. This means that while a mathematical system might be consistent and incomplete, it can never provide an internal proof of its own consistency, leaving open the possibility that a contradiction could appear in the future <a class="yt-timestamp" data-t="00:21:56">[00:21:56]</a>.

## Turing and Undecidability: The Halting Problem

The third of Hilbert's questions, **decidability** (is there an algorithm that can always determine whether a statement follows from axioms?), was answered by Alan Turing in 1936 <a class="yt-timestamp" data-t="00:22:13">[00:22:13]</a>. To do this, Turing invented the concept of the modern computer, the **Turing machine** <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>.

A Turing machine is a theoretical device that can perform any computable algorithm, with an infinitely long tape for input/output and a read/write head <a class="yt-timestamp" data-t="00:22:45">[00:22:45]</a>. It can either halt (finish its program) or run forever in an infinite loop <a class="yt-timestamp" data-t="00:24:04">[00:24:04]</a>.

Turing then posed the **halting problem**: Is it possible to tell beforehand if a given Turing machine program will halt or not on a particular input? <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>

Turing proved that a universal "halting machine" (H) cannot exist. He constructed a modified machine (H+) that takes its own code as input <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>.
*   If H concludes H+ will halt, H+ is designed to go into an infinite loop.
*   If H concludes H+ will never halt, H+ is designed to halt immediately.
This creates a contradiction: whatever H predicts, H+ does the opposite <a class="yt-timestamp" data-t="00:26:16">[00:26:16]</a>. The only explanation is that a machine like H, capable of universally solving the halting problem, cannot exist <a class="yt-timestamp" data-t="00:26:47">[00:26:47]</a>.

Since the halting problem is undecidable, it follows that mathematics itself is undecidable <a class="yt-timestamp" data-t="00:26:53">[00:26:53]</a>. There is no algorithm that can always determine whether a statement is derivable from the axioms <a class="yt-timestamp" data-t="00:27:02">[00:27:02]</a>. This means problems like the [[The Twin Prime Conjecture | Twin Prime Conjecture]] might indeed be unsolvable <a class="yt-timestamp" data-t="00:27:08">[00:27:08]</a>.

## Implications and Legacy

The problem of undecidability extends beyond theoretical computation, appearing in physical systems like determining the spectral gap in quantum mechanics <a class="yt-timestamp" data-t="00:27:20">[00:27:20]</a>. Systems that are **Turing complete**—meaning they can perform any computation a Turing machine can—inherently come with their own analog of the halting problem, an undecidable property <a class="yt-timestamp" data-t="00:28:36">[00:28:36]</a>. Examples include Wang tiles, complex quantum systems, and [[Conways Game of Life and Undecidability | Conway's Game of Life]] <a class="yt-timestamp" data-t="00:28:53">[00:28:53]</a>. Most programming languages and even seemingly simple systems like spreadsheets are Turing complete <a class="yt-timestamp" data-t="00:29:13">[00:29:13]</a>.

Although Hilbert's dream of a complete, consistent, and decidable mathematics was shattered by Gödel and Turing, the attempt to find these answers led to profound discoveries <a class="yt-timestamp" data-t="00:30:09">[00:30:09]</a>. [[Infinity and countability in mathematics | Cantor]]'s work transformed the concept of [[Infinity and countability in mathematics | infinity]] <a class="yt-timestamp" data-t="00:32:27">[00:32:27]</a>. Turing's ideas about computability, stemming from Hilbert's decidability question, led directly to the invention of the modern computer <a class="yt-timestamp" data-t="00:32:33">[00:32:33]</a>. Turing applied his work during World War II, leading the team at Bletchley Park that cracked Nazi codes, shortening the war by years <a class="yt-timestamp" data-t="00:30:49">[00:30:49]</a>.

Ultimately, Gödel's Incompleteness Theorems reveal that while there is a "hole" at the bottom of math—meaning we cannot know everything with certainty and there will always be true statements that cannot be proven <a class="yt-timestamp" data-t="00:32:07">[00:32:07]</a>—the pursuit of this fundamental limit revolutionized mathematics and technology <a class="yt-timestamp" data-t="00:32:22">[00:32:22]</a>.