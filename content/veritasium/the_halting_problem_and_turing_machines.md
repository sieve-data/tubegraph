---
title: The Halting Problem and Turing Machines
videoId: HeQX2HjkcNo
---

From: [[veritasium]] <br/> 

Mathematics contains fundamental limitations, implying that not all true statements can be proven, and certain problems are inherently undecidable <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. This means there will always be true statements that cannot be proven <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. An example of such a potentially unprovable statement is the Twin Prime Conjecture, which posits an infinite number of twin primes (prime numbers separated by one number, like 11 and 13) <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Undecidability in Systems

The concept of undecidability extends beyond abstract mathematical conjectures to various systems.

### Conway's Game of Life
[[conways_game_of_life_and_undecidability | Conway's Game of Life]], created by mathematician John Conway in 1970, is played on an infinite grid of square cells, each either live or dead <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. The game has two simple rules:
1.  Any dead cell with exactly three live neighbors comes to life <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
2.  Any living cell with less than two or more than three live neighbors dies <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

Once an initial arrangement of cells is set, these rules are applied automatically to generate subsequent generations <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. Despite the simplicity of its rules, the game can exhibit complex behaviors, including stable patterns, oscillating loops, patterns that travel across the grid (like gliders), and patterns that grow indefinitely <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

A surprising aspect of [[conways_game_of_life_and_undecidability | Conway's Game of Life]] is that the ultimate fate of a pattern—whether it will eventually reach a steady state or grow without limit—is undecidable <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. This means there is no algorithm guaranteed to answer this question in a finite amount of time <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. Even running a pattern for millions of generations doesn't guarantee a definitive answer about its long-term behavior <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

### Other Undecidable Systems
Many other systems are also undecidable, including [[wang_tiles | Wang tiles]], [[quantum_mechanics_and_deterministic_universe | quantum physics]], airline ticketing systems, and even the card game Magic: The Gathering <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. This pervasive nature of undecidability in mathematics stems from a deeper issue related to self-reference, which became apparent during a period of upheaval in mathematics in the late 19th and early 20th centuries <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

## Hilbert's Program and the Quest for Certainty

At the end of the 19th century, a major debate emerged among mathematicians regarding the foundations of their field <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>. David Hilbert, a leading formalist, believed that mathematics could be placed on absolutely secure logical foundations using formal systems of proof based on set theory <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. Hilbert envisioned a formal system where mathematical statements could be translated into symbolic logic with rigid manipulation rules <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. He posed three central questions about mathematics <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>:
1.  **Completeness**: Is there a way to prove every true statement in mathematics? <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>
2.  **Consistency**: Is mathematics free of contradictions? <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>
3.  **Decidability**: Is there an algorithm that can always determine whether a statement follows from the axioms? <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>

Hilbert was convinced that the answer to all three questions was "yes" <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>.

However, Hilbert's dream of a complete, consistent, and decidable mathematics was shattered. [[gdels_incompleteness_theorems | Kurt Gödel's incompleteness theorems]] proved that any consistent formal system of mathematics capable of basic arithmetic cannot be complete (there will always be true statements that cannot be proven within the system) and cannot prove its own consistency <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>. This left only the third question: decidability <a class="yt-timestamp" data-t="00:21:13">[00:21:13]</a>.

## Alan Turing and the Halting Problem

In 1936, Alan Turing devised a way to answer Hilbert's question about decidability by inventing the theoretical concept of the modern computer: the **Turing machine** <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>.

### The Turing Machine
A Turing machine is a simple yet powerful theoretical computer <a class="yt-timestamp" data-t="00:22:45">[00:22:45]</a>. It takes input from an infinitely long tape of square cells, each containing a zero or a one <a class="yt-timestamp" data-t="00:22:57">[00:22:57]</a>. A read/write head interacts with one digit at a time, performing tasks like overwriting a value, moving left or right, or halting <a class="yt-timestamp" data-t="00:23:04">[00:23:04]</a>. The machine operates based on a program, which is a set of internal instructions determining its actions based on the digit read and its internal state <a class="yt-timestamp" data-t="00:23:19">[00:23:19]</a>. Despite its simplicity, a Turing machine, with its arbitrarily large memory and program, can execute any computable algorithm, making it equivalent in power to any modern computer <a class="yt-timestamp" data-t="00:23:43">[00:23:43]</a>.

### The Halting Problem
Turing realized that the question of whether a statement follows from axioms (decidability) was similar to what became known as the **Halting Problem** <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>. The Halting Problem asks: Is it possible to determine beforehand if a given Turing machine program will halt (finish running) or run forever (get stuck in an infinite loop) on a particular input? <a class="yt-timestamp" data-t="00:24:04">[00:24:04]</a>

If the Halting Problem could be solved, it would be possible to solve other major unsolved mathematical questions, like the Twin Prime Conjecture <a class="yt-timestamp" data-t="00:24:33">[00:24:33]</a>. One could write a Turing machine to systematically generate all theorems derivable from axioms and halt if it finds the Twin Prime Conjecture (or a proof of its falsity) <a class="yt-timestamp" data-t="00:24:37">[00:24:37]</a>.

### Turing's Proof of Undecidability
Turing proved that the Halting Problem is undecidable. He did this by assuming that a machine `H` *could* exist, which could determine if any Turing machine would halt or not on a particular input <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>. `H` would simulate the machine and its input, outputting "halts" or "never halts" <a class="yt-timestamp" data-t="00:25:16">[00:25:16]</a>.

Turing then designed a new machine, `H+`, by modifying `H` <a class="yt-timestamp" data-t="00:25:30">[00:25:30]</a>:
*   If `H` outputs "halts", `H+` goes into an infinite loop <a class="yt-timestamp" data-t="00:25:37">[00:25:37]</a>.
*   If `H` outputs "never halts", `H+` immediately halts <a class="yt-timestamp" data-t="00:25:45">[00:25:45]</a>.

The crucial step is to give `H+` its *own* code as both program and input <a class="yt-timestamp" data-t="00:25:54">[00:25:54]</a>. Now, `H` must determine the behavior of `H+` when `H+` is processing its own code <a class="yt-timestamp" data-t="00:26:02">[00:26:02]</a>.
*   If `H` concludes that `H+` *never halts*, then `H+` (by its own rules) *immediately halts* <a class="yt-timestamp" data-t="00:26:16">[00:26:16]</a>.
*   If `H` concludes that `H+` *will halt*, then `H+` (by its own rules) *goes into an infinite loop* <a class="yt-timestamp" data-t="00:26:28">[00:26:28]</a>.

In both cases, the output of `H` is contradicted by the actual behavior of `H+` <a class="yt-timestamp" data-t="00:26:38">[00:26:38]</a>. This contradiction proves that a machine like `H` cannot exist <a class="yt-timestamp" data-t="00:26:47">[00:26:47]</a>. There is no general way to tell if a Turing machine will halt or not on a given input <a class="yt-timestamp" data-t="00:26:53">[00:26:53]</a>.

## Implications of Undecidability and Turing Completeness

Turing's proof means that mathematics is undecidable <a class="yt-timestamp" data-t="00:27:02">[00:27:02]</a>. There is no algorithm that can always determine whether a statement is derivable from the axioms <a class="yt-timestamp" data-t="00:27:02">[00:27:02]</a>. This suggests that problems like the Twin Prime Conjecture might be fundamentally unsolvable <a class="yt-timestamp" data-t="00:27:08">[00:27:08]</a>.

### Turing Completeness
Turing designed his machines to be the most powerful computers possible <a class="yt-timestamp" data-t="00:28:24">[00:28:24]</a>. Systems capable of performing any computation a Turing machine can are called **Turing complete** <a class="yt-timestamp" data-t="00:28:30">[00:28:30]</a>. While powerful, every Turing complete system comes with an inherent "catch"—its own analog of the Halting Problem, an undecidable property <a class="yt-timestamp" data-t="00:28:43">[00:28:43]</a>.
*   [[wang_tiles | Wang tiles]] are Turing complete; their halting problem is whether they will tile the plane <a class="yt-timestamp" data-t="00:28:55">[00:28:55]</a>.
*   Complex [[quantum_mechanics_and_deterministic_universe | quantum systems]] are Turing complete; their halting problem is the spectral gap question (determining the energy difference between ground and first excited states) <a class="yt-timestamp" data-t="00:29:01">[00:29:01]</a>.
*   [[conways_game_of_life_and_undecidability | Conway's Game of Life]] is Turing complete; its halting problem is whether a pattern halts (stabilizes or dies out) <a class="yt-timestamp" data-t="00:29:07">[00:29:07]</a>.

Many other systems are Turing complete, including airline ticketing systems, Magic: The Gathering, PowerPoint slides, Excel spreadsheets, and nearly every programming language <a class="yt-timestamp" data-t="00:29:13">[00:29:13]</a>. A Turing complete system can simulate any other Turing complete system, including itself <a class="yt-timestamp" data-t="00:29:25">[00:29:25]</a>.

> [!NOTE]
> The concept of Turing completeness allows for phenomena like [[conways_game_of_life_and_undecidability | Conway's Game of Life]] running on itself, demonstrating its ability to simulate complex computational processes <a class="yt-timestamp" data-t="00:29:36">[00:29:36]</a>.

## Legacy

Alan Turing's ideas had a profound impact on the world. During World War II, he led the team at Bletchley Park that built machines to crack Nazi codes, an effort estimated to have shortened the war by two to four years <a class="yt-timestamp" data-t="00:50:49">[00:50:49]</a>. After the war, Turing and John von Neumann designed ENIAC, the first true programmable electronic computer, based on Turing's designs <a class="yt-timestamp" data-t="00:51:04">[00:51:04]</a>.

Turing's work on computability, derived from his concept of the Turing machine and his efforts to answer Hilbert's question about decidability, directly led to the invention of all modern computers <a class="yt-timestamp" data-t="00:31:46">[00:31:46]</a>. Thus, the paradoxes arising from self-reference ultimately led to revolutionary technological advancements <a class="yt-timestamp" data-t="00:32:07">[00:32:07]</a>.

Even though it means we will never know everything with certainty and some true statements cannot be proven, this realization transformed the concept of infinity, changed the course of a world war, and led directly to the invention of modern computing <a class="yt-timestamp" data-t="00:32:14">[00:32:14]</a>.