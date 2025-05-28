---
title: Undecidability in Mathematical Systems
videoId: HeQX2HjkcNo
---

From: [[veritasium]] <br/> 

There is a fundamental "hole" in mathematics, meaning we will never know everything with certainty. There will always be true statements that cannot be proven <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. No one knows exactly what these statements are, but they could include conjectures like the Twin Prime Conjecture <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. The surprising truth is that in any mathematical system capable of basic arithmetic, there will always be true statements that are impossible to prove <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

This concept of undecidability extends beyond abstract mathematics, appearing in various systems from games to quantum physics <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

## Conway's Game of Life

Conway's Game of Life, created in 1970 by mathematician John Conway, is played on an infinite grid of square cells, each either live or dead <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. It operates with only two simple rules:
1.  Any dead cell with exactly three live neighbors comes to life <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
2.  Any living cell with less than two or more than three neighbors dies <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

Once an initial arrangement of cells is set, these rules are automatically applied to generate successive generations, leading to a wide variety of behaviors <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. Despite the simple rules, it is impossible to predict the ultimate fate of a pattern—whether it will reach a steady state or grow without limit <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. The question of a pattern's ultimate fate in Conway's Game of Life is undecidable, meaning no algorithm can guarantee an answer in a finite amount of time <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. Even running the pattern for millions of generations doesn't guarantee knowing its long-term behavior <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

## The Revolt in Mathematics and Set Theory

The seeds of understanding undecidability were sown 150 years ago, following a "full-blown revolt" in mathematics <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. For two millennia, Euclid's elements were considered the bedrock of mathematics <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. However, the discovery of non-Euclidean geometries by Lobachevsky and Gauss at the turn of the 19th century, along with poorly defined concepts like "limits" in calculus, prompted mathematicians to scrutinize the foundations of their field <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.

### Cantor's Set Theory

In 1874, German mathematician Georg Cantor published a paper that launched [[history_of_set_theory_and_mathematical_foundations | set theory]], a new branch of mathematics <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. A set is defined as a well-defined collection of things <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. Cantor explored sets of numbers, such as natural numbers (positive integers like 1, 2, 3...) and real numbers (including fractions and irrational numbers like pi, e, and the square root of two, representable as infinite decimals) <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

He posed the question: Are there more natural numbers or more real numbers between zero and one? <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a> Although both are infinite, Cantor demonstrated they are not the same size <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

#### Cantor's Diagonalization Proof

To illustrate this, Cantor imagined attempting to create an infinite list matching each natural number with a real number between zero and one <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. He then devised a method to construct a *new* real number that cannot be on the list <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. This new number is created by taking the first digit of the first number on the list and adding one, the second digit of the second number and adding one, and so on, diagonally down the list <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. If a digit is 9, it rolls back to 8 <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

This newly constructed number will differ from every number on the original list in at least one decimal place (specifically, along the diagonal), proving it cannot be on the list <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. This means there are more real numbers than natural numbers, demonstrating that not all infinities are the same size <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. Cantor called these [[concept_of_countably_vs_uncountably_infinite | countable and uncountable infinities]] <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.

### The Debate: Intuitionists vs. Formalists

Cantor's work, which revealed the complexity of infinity, fueled a major debate among mathematicians at the end of the 1800s <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

*   **Intuitionists** (e.g., Henri Poincaré, Leopold Kronecker) viewed Cantor's work as "nonsense" <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>. They believed mathematics was a creation of the human mind, and infinities like Cantor's weren't "real" <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
*   **Formalists** (led informally by David Hilbert) believed that mathematics could be placed on "absolutely secure logical foundations" through Cantor's [[history_of_set_theory_and_mathematical_foundations | set theory]] <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. Hilbert was convinced a formal and rigorous system of mathematical proof, based on set theory, could resolve the issues that had arisen <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

### Russell's Paradox

In 1901, Bertrand Russell identified a serious problem within Cantor's [[history_of_set_theory_and_mathematical_foundations | set theory]] <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. If sets could contain anything, including other sets or even themselves, this led to a paradox <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. Russell's Paradox specifically concerned "the set of all sets that don't contain themselves" (let's call it R) <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>:
*   If R doesn't contain itself, then by definition, it must contain itself <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   If R does contain itself, then by definition, it must *not* contain itself <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
This is a contradiction: R contains itself if and only if it doesn't <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. Russell famously explained this with the "barber analogy": a village barber shaves all and only those men who do not shave themselves. Who shaves the barber? <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>

While the intuitionists rejoiced, mathematicians like Zermelo and others from Hilbert's school solved the problem by restricting the concept of a set, eliminating self-referential paradoxes <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

### Wang Tiles

Self-reference, however, continued to pose problems. In the 1960s, mathematician Hao Wang studied square tiles with colors on each side, where touching edges must match <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>. The question was whether an arbitrary set of these tiles could tile an infinite plane without gaps <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. It turns out this problem is undecidable, just like the fate of a pattern in Conway's Game of Life, and it ultimately stems from self-reference <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

## Hilbert's Program and Gödel's Incompleteness

David Hilbert aimed to secure the foundations of mathematics by developing a new, formal system for mathematical proofs <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>. Such systems start with axioms (basic assumed truths) and use rules of inference to derive new, true statements <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>. Hilbert envisioned a symbolic logical language with rigid rules for symbol manipulation, allowing mathematical statements to be translated and proven formally <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. Bertrand Russell and Alfred North Whitehead developed such a system in their monumental *Principia Mathematica* (1913) <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.

Hilbert had three big questions about mathematics <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>:
1.  **Completeness:** Is there a way to prove every true statement? <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>
2.  **Consistency:** Is mathematics free of contradictions? <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>
3.  **Decidability:** Is there an algorithm that can always determine whether a statement follows from the axioms? <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>

Hilbert was convinced the answer to all three was yes, famously declaring, "We must know, we will know" <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>.

### [[gdels_incompleteness_theorems | Gödel's Incompleteness Theorems]]

Hilbert's dream crumbled in 1930 when 24-year-old logician Kurt Gödel presented his findings <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>.

#### [[gdels_incompleteness_theorems | Gödel's First Incompleteness Theorem]]

Gödel showed that a complete formal system of mathematics was impossible <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>. His proof involved assigning a unique "Gödel number" to every basic symbol, number, equation, and even entire proofs within a mathematical system <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>. This allows logical and mathematical statements to be represented as numbers <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>.

Using this system, Gödel constructed a self-referential statement within the mathematical system itself: "There is no proof for the statement with Gödel number g," where 'g' is the Gödel number of that very statement <a class="yt-timestamp" data-t="00:19:36">[00:19:36]</a>.
*   **If this statement is false**, then there *is* a proof for it. But proving "there is no proof" creates a contradiction, meaning the mathematical system is inconsistent <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>.
*   **If this statement is true**, then there is *no* proof for it. This means the mathematical system contains true statements that cannot be proven, making it incomplete <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>.

This is [[gdels_incompleteness_theorems | Gödel's Incompleteness Theorem]]: any basic mathematical system capable of fundamental arithmetic will always have statements within it that are true but have no proof <a class="yt-timestamp" data-t="00:20:33">[00:20:33]</a>. Truth and provability are not the same <a class="yt-timestamp" data-t="00:21:22">[00:21:22]</a>.

#### [[gdels_incompleteness_theorems | Gödel's Second Incompleteness Theorem]]

Gödel later published his [[gdels_incompleteness_theorems | second incompleteness theorem]], which showed that any consistent formal system of mathematics cannot prove its own consistency <a class="yt-timestamp" data-t="00:21:39">[00:21:39]</a>. Taken together, Gödel's theorems imply that the best one can hope for is a consistent yet incomplete system of mathematics, but such a system cannot prove its own consistency, meaning a contradiction could always arise in the future <a class="yt-timestamp" data-t="00:21:56">[00:21:56]</a>.

## Turing and Decidability

The third of Hilbert's questions, "is mathematics decidable?", was addressed by Alan Turing in 1936 <a class="yt-timestamp" data-t="00:22:13">[00:22:13]</a>. To do so, Turing invented the concept of the modern computer: the Turing machine <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>.

### The Turing Machine and the Halting Problem

A Turing machine is an abstract model of computation, powerful enough to perform any imaginable computation but simple enough to reason about <a class="yt-timestamp" data-t="00:22:45">[00:22:45]</a>. It takes an infinitely long tape of 0s and 1s as input, has a read/write head, and can perform basic tasks: overwrite, move left, move right, or halt <a class="yt-timestamp" data-t="00:22:57">[00:22:57]</a>. The program is a set of internal instructions <a class="yt-timestamp" data-t="00:23:19">[00:23:19]</a>. While simple, a Turing machine with arbitrarily large memory can execute any computable algorithm, from arithmetic to complex software <a class="yt-timestamp" data-t="00:23:43">[00:23:43]</a>.

Turing realized that Hilbert's decidability problem was related to the "halting problem": Is it possible to tell beforehand if a given Turing machine program will halt (finish running) or get stuck in an infinite loop on a particular input? <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>

If the halting problem could be solved, then many other unsolved questions, like the Twin Prime Conjecture, could also be solved <a class="yt-timestamp" data-t="00:24:22">[00:24:22]</a>. For example, a Turing machine could be programmed to generate theorems from axioms; if it generates the conjecture, it halts <a class="yt-timestamp" data-t="00:24:33">[00:24:33]</a>.

Turing then demonstrated that the halting problem is undecidable <a class="yt-timestamp" data-t="00:26:47">[00:26:47]</a>. He imagined a hypothetical machine 'H' that *could* determine if any Turing machine would halt <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>. He then designed a modified machine, 'H+', which:
*   If H outputs "halts," H+ goes into an infinite loop <a class="yt-timestamp" data-t="00:25:37">[00:25:37]</a>.
*   If H outputs "never halts," H+ immediately halts <a class="yt-timestamp" data-t="00:25:45">[00:25:45]</a>.

When H+ is given its *own* code as input, H must simulate H+'s behavior <a class="yt-timestamp" data-t="00:25:54">[00:25:54]</a>.
*   If H concludes H+ will *never halt*, H+ immediately *halts* (contradiction) <a class="yt-timestamp" data-t="00:26:16">[00:26:16]</a>.
*   If H concludes H+ *will halt*, H+ immediately goes into an infinite *loop* (contradiction) <a class="yt-timestamp" data-t="00:26:28">[00:26:28]</a>.

Since any output from H leads to a contradiction, a machine like H cannot exist <a class="yt-timestamp" data-t="00:26:47">[00:26:47]</a>. Therefore, it's impossible to tell in general if a Turing machine will halt, proving that mathematics is undecidable <a class="yt-timestamp" data-t="00:26:53">[00:26:53]</a>. This means no algorithm can always determine whether a statement is derivable from axioms <a class="yt-timestamp" data-t="00:27:02">[00:27:02]</a>.

## Undecidability in Other Systems

Undecidability is not limited to abstract mathematical systems:
*   **Quantum Mechanics:** Determining if a quantum system has a "spectral gap" (a difference in energy between its ground state and first excited state) is an undecidable problem <a class="yt-timestamp" data-t="00:27:20">[00:27:20]</a>. This implies that even a perfect microscopic description of a material's particles isn't always enough to deduce its macroscopic properties <a class="yt-timestamp" data-t="00:28:10">[00:28:10]</a>.
*   **Turing Completeness:** A system is Turing complete if it can do everything a Turing machine can <a class="yt-timestamp" data-t="00:28:30">[00:28:30]</a>. Many systems are Turing complete, and every such system comes with its own undecidable property, analogous to the halting problem <a class="yt-timestamp" data-t="00:28:43">[00:28:43]</a>.
    *   Wang tiles are Turing complete; their halting problem is whether they will tile the plane <a class="yt-timestamp" data-t="00:28:55">[00:28:55]</a>.
    *   Conway's Game of Life is Turing complete; its halting problem is literally whether a pattern halts <a class="yt-timestamp" data-t="00:29:07">[00:29:07]</a>.
    *   Other examples include airline ticketing systems, the card game [[Magic the Gathering]], PowerPoint slides, and Excel spreadsheets <a class="yt-timestamp" data-t="00:29:13">[00:29:13]</a>. Most programming languages are designed to be Turing complete <a class="yt-timestamp" data-t="00:29:19">[00:29:19]</a>.

## Legacy

While [[incompleteness_of_mathematics | mathematical incompleteness]] and undecidability proved Hilbert's dream of a perfectly complete, consistent, and decidable mathematics impossible, the pursuit of these questions led to profound discoveries <a class="yt-timestamp" data-t="00:30:09">[00:30:09]</a>.

Alan Turing's ideas about computing were put to practical use during World War II at Bletchley Park, where his team built calculating machines to crack Nazi codes, potentially shortening the war by years <a class="yt-timestamp" data-t="00:30:49">[00:30:49]</a>. After the war, Turing and John von Neumann designed ENIAC, the first true programmable electronic computer, based on Turing's designs <a class="yt-timestamp" data-t="00:31:09">[00:31:09]</a>. Turing is widely considered the most important founding figure in computer science <a class="yt-timestamp" data-t="00:31:36">[00:31:36]</a>; all modern computers are descended from his designs <a class="yt-timestamp" data-t="00:31:41">[00:31:41]</a>.

The paradoxes of self-reference, which initially appeared to be flaws, ultimately led to the invention of modern computational devices <a class="yt-timestamp" data-t="00:31:52">[00:31:52]</a>. The realization that there will always be true statements that cannot be proven, rather than leading to the disintegration of mathematics, transformed the concept of infinity, changed the course of a world war, and directly led to the invention of the devices used today <a class="yt-timestamp" data-t="00:32:18">[00:32:18]</a>.