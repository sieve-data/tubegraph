---
title: Incompleteness of Mathematics
videoId: HeQX2HjkcNo
---

From: [[veritasium]] <br/> 

Mathematics contains fundamental "holes" which mean that we will never know everything with certainty. There will always be true statements that cannot be proven <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. While the exact statements are unknown, an example could be the Twin Prime Conjecture <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

Twin primes are prime numbers separated by a single number, such as 11 and 13, or 17 and 19 <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. As numbers increase, primes become less frequent, and twin primes are even rarer <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. The Twin Prime Conjecture posits that there are infinitely many twin primes <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. As of now, this conjecture remains unproven, and it is possible that it may never be proven due to the inherent incompleteness of mathematical systems <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. In any system of mathematics where basic arithmetic can be performed, there will always be true statements that are impossible to prove <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Undecidability in Systems

### Conway's Game of Life
The concept of [[Undecidability in Mathematical Systems | undecidability]] can be illustrated through Conway's Game of Life, a "zero-player game" created in 1970 by mathematician John Conway, who passed away in 2020 <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. The game is played on an infinite grid of square cells, each either live or dead, governed by two simple rules <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>:
*   A dead cell with exactly three living neighbors comes to life <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   A living cell with less than two or more than three neighbors dies <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

Once an initial arrangement of cells is set, these rules are automatically applied to generate successive generations <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. Despite the simple rules, the game exhibits a wide variety of behaviors: some patterns are stable, others oscillate, some "travel" (like a glider), many fizzle out, but a few grow infinitely <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

The ultimate fate of a pattern in Conway's Game of Life is [[Undecidability in Mathematical Systems | undecidable]] <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. This means there is no possible algorithm guaranteed to determine, in a finite amount of time, whether a pattern will reach a steady state, die out, or grow indefinitely <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. Even running the simulation for millions of generations won't guarantee an answer for its infinite future <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

### Other Undecidable Systems
Conway's Game of Life is not unique in being undecidable; many other systems share this property <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. These include Wang tiles, certain aspects of quantum physics, airline ticketing systems, and even games like Magic: The Gathering <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. The root of this [[Undecidability in Mathematical Systems | undecidability]] often lies in self-reference <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.

## Historical Context and Set Theory

The realization of incompleteness emerged from a "revolt in mathematics" that began around 150 years ago <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. For two millennia, Euclid's Elements were considered the bedrock of mathematics <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. However, in the early 19th century, non-Euclidean geometries were discovered by Lobashevsky and Gauss, prompting a re-examination of mathematics' foundations <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. Issues like the poorly defined concept of a "limit" in calculus also contributed to this upheaval <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

### Georg Cantor and the Nature of Infinity
In 1874, German mathematician Georg Cantor published a paper that launched [[History of Set Theory and Mathematical Foundations | set theory]], a new branch of mathematics <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. A set is simply a well-defined collection of things <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. Cantor pondered whether there were more natural numbers (positive integers like 1, 2, 3...) or real numbers (numbers including fractions, pi, e, square root of two, representable as infinite decimals) between zero and one <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

Using his [[Mathematical Paradoxes of Infinity | diagonalization proof]], Cantor demonstrated that not all infinities are the same size <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. By imagining an infinite list matching natural numbers to real numbers between zero and one, he showed that it's always possible to construct a new real number not on the list <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. This new number is constructed by taking the first digit of the first number and adding one, the second digit of the second number and adding one, and so on, creating a number that differs from every number on the list in at least one decimal place <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. This proved there are more real numbers than natural numbers, classifying them as "countable" and "uncountable" infinities, respectively <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

### The Formalist-Intuitionist Debate
Cantor's work, showing that infinity was far more complex than imagined, fractured mathematics into a debate between intuitionists and formalists <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.

*   **Intuitionists** believed Cantor's work was nonsense, viewing math as a human construct and infinite sets as not real <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>. Henri Poincaré famously called set theory a "disease" <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>, and Leopold Kronecker labeled Cantor a "scientific charlatan" <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.
*   **Formalists**, led informally by David Hilbert, believed mathematics could be placed on secure logical foundations through [[History of Set Theory and Mathematical Foundations | set theory]] <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. Hilbert, a hugely influential mathematician, was convinced a rigorous system based on set theory could resolve all mathematical issues <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. He famously declared, "No one shall expel us from the paradise that Cantor has created" <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.

### Russell's Paradox
In 1901, Bertrand Russell uncovered a serious problem within Cantor's [[History of Set Theory and Mathematical Foundations | set theory]] with what became known as [[Mathematical Paradoxes of Infinity | Russell's Paradox]] <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. Sets can contain other sets, or even themselves <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. Russell posed the question about R: the set of all sets that *don't* contain themselves <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
*   If R doesn't contain itself, then by definition, it must contain itself.
*   If R *does* contain itself, then by definition, it must *not* contain itself <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
This leads to a contradiction, where R contains itself if and only if it doesn't <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.

Russell illustrated this with the "barber paradox": In a village where the barber shaves all and only those men who do not shave themselves, who shaves the barber? If he shaves himself, he shouldn't; if he doesn't, he should <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>. While intuitionists rejoiced, mathematicians from Hilbert's school like Zermelo solved the problem by restricting the concept of a set, for example, stating that the "collection of all sets" is not a set <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. This eliminated paradoxes arising from self-reference in set theory, though self-reference itself remained a persistent issue <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

### Wang Tiles and Undecidability
The problem of [[Undecidability in Mathematical Systems | undecidability]] also manifests in Wang tiles, square tiles with colored sides <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>. The rule is that touching edges must be the same color, and tiles cannot be rotated or reflected <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>. For an arbitrary set of Wang tiles, it is undecidable whether they can tile an infinite plane without gaps <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. This problem is fundamentally the same as determining the fate of a pattern in Conway's Game of Life, stemming from self-reference <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.

## Hilbert's Program and Gödel's Breakthrough

David Hilbert aimed to secure the foundations of mathematics by developing a new system for mathematical proofs <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>. A proof system starts with axioms (basic assumed true statements) and uses rules of inference to derive new true statements <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>. Hilbert sought a formal system: a symbolic logical language with rigid rules for symbol manipulation, where mathematical statements could be translated and manipulated <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.

Bertrand Russell and Alfred North Whitehead developed such a system in their three-volume *Principia Mathematica*, published in 1913 <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>. This vast work, nearly 2,000 pages of dense notation, took 762 pages just to prove 1+1=2 <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>. Its exactness, unlike ordinary language, allows for proving properties of the formal system itself <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.

Hilbert posed three major questions about mathematics <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>:
1.  **Completeness:** Is there a way to prove every true statement? <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>
2.  **Consistency:** Is mathematics free of contradictions (i.e., can one not prove both 'a' and 'not a')? <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>
3.  **Decidability:** Is there an algorithm that can always determine whether a statement follows from the axioms? <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>

Hilbert was convinced the answer to all three was "yes" <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>. In 1930, he famously declared, "We must know, we will know" <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.

### [[Gdels Incompleteness Theorems | Gödel's Incompleteness Theorems]]
However, Hilbert's dream was already crumbling. The day before Hilbert's 1930 speech, 24-year-old logician Kurt Gödel explained his finding that a complete formal system of mathematics was impossible <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>. The following year, Gödel published his proof <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.

[[Gdels Incompleteness Theorems | Gödel's proof]] works by assigning a unique "Gödel number" to every basic symbol in a mathematical system, as well as to numbers themselves and sequences of symbols (like equations or proofs) <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>. This allows mathematical statements and proofs to be represented as numbers <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>.

Using this system, Gödel constructed a self-referential statement that translates to: "There is no proof for the statement with Gödel number G," where G is the Gödel number of that very statement itself <a class="yt-timestamp" data-t="00:19:36">[00:19:36]</a>.
*   If this statement is *false* (meaning there *is* a proof), then proving it leads to a contradiction: "there is no proof" has been proven, making the system inconsistent <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>.
*   If the statement is *true* (meaning there *is no* proof), then the mathematical system contains a true statement that cannot be proven, making the system incomplete <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>.

This is [[Gdels Incompleteness Theorems | Gödel's First Incompleteness Theorem]]: any basic mathematical system capable of fundamental arithmetic will always have statements within it that are true but have no proof <a class="yt-timestamp" data-t="00:20:33">[00:20:33]</a>. Truth and provability are not the same <a class="yt-timestamp" data-t="00:21:22">[00:21:22]</a>.

Gödel further published his [[Gdels Incompleteness Theorems | Second Incompleteness Theorem]], demonstrating that any consistent formal system of math cannot prove its own consistency <a class="yt-timestamp" data-t="00:21:39">[00:21:39]</a>. Combined, these theorems mean that the best one can hope for is a consistent yet incomplete system of mathematics, but even then, its consistency cannot be proven from within the system itself <a class="yt-timestamp" data-t="00:21:56">[00:21:56]</a>.

## Alan Turing and the Decidability Problem

The final of Hilbert's big questions was: Is mathematics [[Undecidability in Mathematical Systems | decidable]]? In 1936, Alan Turing addressed this by inventing the modern computer, or "Turing machine" <a class="yt-timestamp" data-t="00:22:13">[00:22:13]</a>.

A Turing machine is an abstract model of computation: it takes input from an infinitely long tape of binary cells, and a read/write head can read, overwrite, move left/right, or halt based on a set of internal instructions (a program) <a class="yt-timestamp" data-t="00:22:51">[00:22:51]</a>. Despite its simplicity, a Turing machine with arbitrarily large memory and program can execute any computable algorithm, making it as powerful as any modern computer <a class="yt-timestamp" data-t="00:23:43">[00:23:43]</a>.

### The Halting Problem
Turing realized that the problem of [[Undecidability in Mathematical Systems | decidability]] was related to the "halting problem": whether it is possible to tell beforehand if a given Turing machine program will halt (finish running) or run forever in an infinite loop for a particular input <a class="yt-timestamp" data-t="00:24:10">[00:24:10]</a>.

If the halting problem could be solved, then one could also solve the [[Undecidability in Mathematical Systems | decidability]] problem for mathematics <a class="yt-timestamp" data-t="00:24:22">[00:24:22]</a>. For example, a Turing machine could be programmed to generate all possible theorems from axioms and rules of inference; if it found the Twin Prime Conjecture, it would halt. If the conjecture was unprovable, it would never halt <a class="yt-timestamp" data-t="00:24:33">[00:24:33]</a>.

However, Turing, using a diagonalization argument similar to Cantor's and Gödel's, proved that the halting problem is unsolvable <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>. He imagined a hypothetical "halting machine" (H) that could predict if any other program would halt. He then constructed a modified machine (H+) that, if H predicted it would halt, would go into an infinite loop, and if H predicted it would *not* halt, it would immediately halt <a class="yt-timestamp" data-t="00:25:30">[00:25:30]</a>. When H+ is given its own code as input, any prediction H makes about H+ leads to a contradiction <a class="yt-timestamp" data-t="00:25:54">[00:25:54]</a>. This means a machine like H cannot exist <a class="yt-timestamp" data-t="00:26:47">[00:26:47]</a>.

Therefore, since the halting problem is undecidable, mathematics is also [[Undecidability in Mathematical Systems | undecidable]]: there is no algorithm that can always determine whether a statement is derivable from the axioms <a class="yt-timestamp" data-t="00:26:53">[00:26:53]</a>. This implies that problems like the Twin Prime Conjecture might be unsolvable <a class="yt-timestamp" data-t="00:27:08">[00:27:08]</a>.

### Undecidability in Quantum Mechanics
The problem of [[Undecidability in Mathematical Systems | undecidability]] even appears in physical systems, such as in quantum mechanics when trying to determine the "spectral gap" of a many-body system <a class="yt-timestamp" data-t="00:27:20">[00:27:20]</a>. The spectral gap is the energy difference between a system's ground state and its first excited state <a class="yt-timestamp" data-t="00:27:26">[00:27:26]</a>. This property is crucial for understanding how quantum systems behave at low temperatures <a class="yt-timestamp" data-t="00:27:44">[00:27:44]</a>. In 2015, mathematicians proved that, in general, the spectral gap question is [[Undecidability in Mathematical Systems | undecidable]] <a class="yt-timestamp" data-t="00:28:02">[00:28:02]</a>.

### Turing Completeness
Turing designed his machines to be the most powerful computers possible <a class="yt-timestamp" data-t="00:28:24">[00:28:24]</a>. Systems capable of doing everything a Turing machine can are called "Turing complete" <a class="yt-timestamp" data-t="00:28:36">[00:28:36]</a>. While powerful, every Turing complete system has its own analog of the halting problem, an undecidable property <a class="yt-timestamp" data-t="00:28:43">[00:28:43]</a>.
*   Wang tiles are Turing complete; their halting problem is whether they can tile the plane <a class="yt-timestamp" data-t="00:28:54">[00:28:54]</a>.
*   Complex quantum systems are Turing complete; their halting problem is the spectral gap question <a class="yt-timestamp" data-t="00:29:01">[00:29:01]</a>.
*   Conway's Game of Life is Turing complete; its halting problem is literally whether it halts <a class="yt-timestamp" data-t="00:29:07">[00:29:07]</a>.

Many other systems are Turing complete, including airline ticketing systems, Magic: The Gathering, PowerPoint slides, Excel spreadsheets, and nearly every programming language <a class="yt-timestamp" data-t="00:29:13">[00:29:13]</a>. A Turing complete system can simulate any other Turing complete system, including itself <a class="yt-timestamp" data-t="00:29:29">[00:29:29]</a>.

## Legacy

While David Hilbert's dream of a perfectly complete and consistent mathematics was shattered by Gödel and Turing, the search for those answers led directly to the invention of modern computational devices <a class="yt-timestamp" data-t="00:30:09">[00:30:09]</a>.

Kurt Gödel suffered from mental instability and died in 1978 <a class="yt-timestamp" data-t="00:30:16">[00:30:16]</a>. Hilbert died in 1943, his epitaph reflecting his unfulfilled dream: "We must know, we will know" <a class="yt-timestamp" data-t="00:30:31">[00:30:31]</a>. The truth is, sometimes "we don't know, sometimes we can't know" <a class="yt-timestamp" data-t="00:30:41">[00:30:41]</a>.

Alan Turing's ideas about computing were put to practical use during World War II, where he led a team at Bletchley Park that built machines to crack Nazi codes, shortening the war by two to four years <a class="yt-timestamp" data-t="00:30:49">[00:30:49]</a>. After the war, Turing and John von Neumann designed ENIAC, one of the first true programmable electronic computers <a class="yt-timestamp" data-t="00:31:07">[00:31:07]</a>. Tragically, Turing was convicted of "gross indecency" in 1952 due to his homosexuality and died by suicide in 1954 <a class="yt-timestamp" data-t="00:31:20">[00:31:20]</a>.

Turing is widely considered the most important founding figure in computer science, with all modern computers descended from his designs <a class="yt-timestamp" data-t="00:31:36">[00:31:36]</a>. His concepts of computability and the Turing machine, stemming from Hilbert's question about decidability, ultimately arose from the paradoxes of self-reference <a class="yt-timestamp" data-t="00:31:52">[00:31:52]</a>.

The realization that there is a hole at the bottom of math – that we will never know everything with certainty and that true statements may remain unprovable – did not lead to the disintegration of mathematics <a class="yt-timestamp" data-t="00:32:07">[00:32:07]</a>. Instead, thinking about these problems transformed the concept of infinity, changed the course of a world war, and directly led to the invention of modern computing devices <a class="yt-timestamp" data-t="00:32:27">[00:32:27]</a>.