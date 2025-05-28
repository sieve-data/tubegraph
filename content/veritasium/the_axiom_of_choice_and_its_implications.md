---
title: The axiom of choice and its implications
videoId: _cr46G2K5Fo
---

From: [[veritasium]] <br/> 

The axiom of choice is a fundamental rule in mathematics that, while seemingly intuitive, leads to profound and often counterintuitive consequences, including the existence of line segments with no length and the ability to duplicate a sphere into two identical spheres without adding any material <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Despite creating such paradoxes, it has been foundational for over a hundred years of mathematics <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## The Problem of Choice in Mathematics

In mathematics, truly picking something at random is not possible because formulas always yield the same result <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. Computers, for instance, generate "random" numbers using algorithms based on factors like current local time <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. Therefore, selecting anything in mathematics generally requires following a rule <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

For sets like positive integers or prime numbers, a rule like "always choose the smallest thing" works easily <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. However, this method fails for [[infinity_and_countability_in_mathematics | real numbers]], which include all positive, negative, whole, fractional, and irrational numbers (like pi or the square root of two) <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. It's impossible to choose the smallest real number, even after a specific number like one, due to the infinite density of numbers between any two points <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. This difficulty in specifying the order of real numbers presents a significant challenge, as there are infinite options, yet no clear way to pick one <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

## Georg Cantor and the Nature of Infinity

The mission to resolve this issue began with [[georg_cantor_and_the_development_of_set_theory | Georg Cantor]] in 1870, who aimed to put the real numbers into a definitive order <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. [[georg_cantor_and_the_development_of_set_theory | Cantor]], a German mathematician, challenged the long-held understanding of infinity, which was heavily influenced by Galileo's 1638 work <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

Galileo had shown that even though square numbers appear more sparse than natural numbers, they are in fact the same size because a one-to-one mapping can be drawn between every natural number and its square <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. From this, Galileo concluded that terms like "more than" or "less than" do not apply to infinity in the normal sense, and that infinity is a single concept of "foreverness" <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

### Cantor's Diagonalization Proof

In 1874, [[georg_cantor_and_the_development_of_set_theory | Cantor]] questioned whether there could be different sizes of infinite sets <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. He compared the set of natural numbers to the set of real numbers between zero and one <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

[[georg_cantor_and_the_development_of_set_theory | Cantor]] assumed a one-to-one mapping was possible and imagined an infinite list pairing natural numbers with real numbers <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. He then constructed a new real number by taking the first digit of the first number and adding one, the second digit of the second number and adding one, and so on (subtracting one if the digit was eight or nine to avoid duplicates) <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. This newly constructed number would differ from every number on the list in at least one decimal place (the digit on the diagonal), proving it could not be on the original list <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

This proof, known as [[infinity_and_countability_in_mathematics | Cantor's Diagonalization Proof]], revealed that there are more real numbers between zero and one than there are natural numbers extending to infinity <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. [[georg_cantor_and_the_development_of_set_theory | Cantor]] distinguished between:
*   **[[infinity_and_countability_in_mathematics | Countable infinities]]**: Sets that can be perfectly paired with natural numbers (e.g., square numbers, integers, rational numbers) <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
*   **[[infinity_and_countability_in_mathematics | Uncountable infinities]]**: Bigger infinities that cannot be matched one-to-one with natural numbers (e.g., real numbers, complex numbers) <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

[[georg_cantor_and_the_development_of_set_theory | Cantor's]] findings shocked the mathematical community, with his work being labeled a "horror" <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

## Cantor's Well-Ordering Theorem

Undeterred, [[georg_cantor_and_the_development_of_set_theory | Cantor]] pursued a grander goal: to show that even uncountably infinite sets could be placed in a "well-order" <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. For a set to be well-ordered, it must have a clear starting point, and every subset within it must also have a clear starting point <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

Natural numbers are well-ordered (starting point: one). Integers, though infinite in both directions, can be well-ordered (e.g., zero, then one, negative one, two, negative two, based on absolute value) <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

In his next book, [[georg_cantor_and_the_development_of_set_theory | Cantor]] published his **well-ordering theorem**, claiming that *every* set, including uncountably infinite ones like the real numbers, could be well-ordered <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>. The major problem was that he couldn't actually prove it <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. [[georg_cantor_and_the_development_of_set_theory | Cantor's]] confidence stemmed from his religious beliefs, as he felt God was speaking through him <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.

Without mathematical proof, his claim led to renewed attacks and ostracization, particularly from his former teacher, Leopold Kronecker, who called him a "scientific charlatan" <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. This pressure took a severe toll on [[georg_cantor_and_the_development_of_set_theory | Cantor]], leading to numerous nervous breakdowns and a retreat from mathematics <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.

## Ernst Zermelo and the Axiom of Choice

At the 1904 International Congress of Mathematicians, Julius König announced he had proven [[georg_cantor_and_the_development_of_set_theory | Cantor's]] well-ordering theorem wrong <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>. However, Ernst Zermelo, a German mathematician interested in [[georg_cantor_and_the_development_of_set_theory | Cantor's]] work, quickly found a contradiction in König's proof <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.

Within a month, Zermelo published a flawless article titled "Proof That Every Set Can Be Well-Ordered" <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. His breakthrough was realizing that [[georg_cantor_and_the_development_of_set_theory | Cantor]] (and other mathematicians) had been unconsciously relying on a mechanism: the assumption that one could make an infinite number of choices at once from any set, including uncountable infinite sets <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>. This assumption was not explicitly permitted in the mathematical rule book, which is built on axioms <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.

Zermelo formalized this assumption into a new axiom: the **axiom of choice** <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>.

> "The axiom of choice can be said in the sense that if you have infinitely many sets and each set is not empty, then there is a way to choose one element from each of the sets." <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>

While this seems obvious for finite sets or infinite sets with a clear rule (like "smallest"), it becomes crucial when no such natural rule exists for infinitely many uncountable sets <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>. The axiom allows for these choices to be made all at once, without specifying *how* each element is chosen <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.

### Well-Ordering the Real Numbers

Zermelo used the axiom of choice to well-order the real numbers. He chose a number (X1) from the set of all real numbers, then chose another (X2) from the remaining numbers, and so on <a class="yt-timestamp" data-t="00:12:58">[00:12:58]</a>. Though it appears sequential, the axiom makes all choices simultaneously from all possible subsets <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.

To index these numbers, Zermelo used "omega numbers" (e.g., omega, omega plus one), which extend past the natural numbers to account for the larger cardinality of the real numbers <a class="yt-timestamp" data-t="00:13:47">[00:13:47]</a>. These omega numbers describe order, not quantity <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>. By continuously choosing and labeling, Zermelo could prove that a first real number exists, and every subset of real numbers also has a first number, thus successfully well-ordering the real numbers <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>.

This well-ordering doesn't resemble our familiar numerical order (e.g., a billion could come before 0.2), but it proves that such an order *exists* <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>. Therefore, [[georg_cantor_and_the_development_of_set_theory | Cantor's]] well-ordering theorem and Zermelo's axiom of choice are equivalent <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.

## Counterintuitive Implications

While Zermelo's proof was flawless, the axiom of choice soon led to disturbing results. Mathematicians, who had unknowingly relied on it for decades <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>, found its consequences highly counterintuitive <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>.

### Vitali Set and Non-Measurable Sets

One of the first disturbing results came from Giuseppe Vitali in 1905, who used the axiom of choice to construct a set of numbers that defied standard notions of length <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>.

Vitali's construction involves:
1.  Dividing every real number between zero and one into an infinite number of "bins" or "groups" <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>. Two numbers X and Y go into the same bin if their difference (X - Y) is a rational number <a class="yt-timestamp" data-t="00:18:32">[00:18:32]</a>. This ensures each real number falls into exactly one bin <a class="yt-timestamp" data-t="00:20:07">[00:20:07]</a>.
2.  Using the axiom of choice to select exactly one "representative" number from each group, forming the **Vitali set** <a class="yt-timestamp" data-t="00:20:13">[00:20:13]</a>. The axiom means you don't know *which* representative number is chosen, only that one exists <a class="yt-timestamp" data-t="00:20:31">[00:20:31]</a>.
3.  Creating infinite copies of the Vitali set, each shifted by a different rational number between negative one and positive one <a class="yt-timestamp" data-t="00:20:53">[00:20:53]</a>. This means each original representative now covers every other number in its group within the span of zero and one <a class="yt-timestamp" data-t="00:21:07">[00:21:07]</a>.
4.  Merging all these infinite sets. There will be no overlap between points, and they collectively cover every real number between zero and one <a class="yt-timestamp" data-t="00:21:31">[00:21:31]</a>.

The problem arises when trying to determine the "size" or "length" of the Vitali set. If you add the "size" of the Vitali set to itself infinitely many times (representing the merged sets), the total length must be between one and three (since it covers [0,1] but extends to [-1,2]) <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>. However, there is no number whose infinite sum yields a value between one and three; an infinite sum of zero is zero, and an infinite sum of any small positive value is infinity <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>. This contradiction implies that the Vitali set itself must be **unmeasurable** <a class="yt-timestamp" data-t="00:22:44">[00:22:44]</a>.

Non-measurable sets defy consistent definitions of size, length, area, or even probability <a class="yt-timestamp" data-t="00:22:54">[00:22:54]</a>, challenging the fundamental mathematical idea that everything can be quantified <a class="yt-timestamp" data-t="00:23:02">[00:23:02]</a>.

### The [[the_banachtarski_paradox | Banach-Tarski Paradox]]

In 1924, Stefan Banach and Alfred Tarski used the axiom of choice to prove the [[the_banachtarski_paradox | Banach-Tarski Paradox]] <a class="yt-timestamp" data-t="00:23:19">[00:23:19]</a>. This paradox states that a single solid ball can be split into just five pieces, which can then be reassembled by careful rotation and movement into two identical balls, each the same size as the original <a class="yt-timestamp" data-t="00:23:27">[00:23:27]</a>. This process can be repeated to create an infinite number of balls from one <a class="yt-timestamp" data-t="00:23:41">[00:23:41]</a>.

The mechanism relies on a graph analogy: a graph with infinite branching can be split into five sections (a middle, and four identical rotated sections) <a class="yt-timestamp" data-t="00:24:28">[00:24:28]</a>. By shifting these sections (e.g., rotating the "left" section to the "right"), the original graph can be perfectly recreated twice, with a small missing part that is then added back <a class="yt-timestamp" data-t="00:24:39">[00:24:39]</a>.

Applying this to a ball:
1.  Imagine rotations as "moves" on the ball's surface, with the rule that one cannot immediately reverse a move <a class="yt-timestamp" data-t="00:25:33">[00:25:33]</a>.
2.  Each rotation is by an irrational portion of a circle to prevent returning to the same point <a class="yt-timestamp" data-t="00:25:47">[00:25:47]</a>.
3.  Points are colored based on the sequence of rotations used to reach them <a class="yt-timestamp" data-t="00:25:58">[00:25:58]</a>. This creates a countably infinite collection of points <a class="yt-timestamp" data-t="00:26:09">[00:26:09]</a>.
4.  Since a ball's surface has uncountably infinite points, the axiom of choice is used to select unique starting points to cover the entire surface, even if the exact choices cannot be specified <a class="yt-timestamp" data-t="00:26:16">[00:26:16]</a>.
5.  Once every point is "colored," they are split into five groups: one for starting points and four based on the final rotation used <a class="yt-timestamp" data-t="00:26:49">[00:26:49]</a>.
6.  These groups, treated like the graph sections, can then be rotated and combined to form two identical copies of the original ball <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>.

The key to this paradox is that the five pieces are not simple, measurable shapes; they are **non-measurable**, just like the Vitali set <a class="yt-timestamp" data-t="00:28:06">[00:28:06]</a>. While the original and duplicated balls have definite volumes, the intermediate step violates our understanding of size <a class="yt-timestamp" data-t="00:28:14">[00:28:14]</a>. This is what allows the paradox to occur <a class="yt-timestamp" data-t="00:28:22">[00:28:22]</a>.

## The Crisis and Resolution

The axiom of choice plunged mathematics into a crisis for over 30 years <a class="yt-timestamp" data-t="00:29:20">[00:29:20]</a>. Some mathematicians, like Lebesgue, dismissed theorems involving the axiom as "equivalence between two false statements" <a class="yt-timestamp" data-t="00:28:54">[00:28:54]</a>.

The resolution came in the mid-20th century:
*   In 1938, Austrian mathematician Kurt Gödel proved that if the other accepted axioms of set theory are true, then the axiom of choice is also true <a class="yt-timestamp" data-t="00:29:37">[00:29:37]</a>.
*   In 1963, Paul Cohen proved there is also a world where all other set theory axioms hold true, *except* for the axiom of choice <a class="yt-timestamp" data-t="00:29:47">[00:29:47]</a>.

This meant the axiom of choice is **independent** of the other axioms; it can neither be proven nor disproven from them <a class="yt-timestamp" data-t="00:30:38">[00:30:38]</a>. Its role is analogous to the parallel postulate in geometry <a class="yt-timestamp" data-t="00:29:57">[00:29:57]</a>. Just as choosing different versions of the parallel postulate leads to different valid geometries (flat, spherical, hyperbolic), choosing to include or exclude the axiom of choice leads to different valid mathematical systems <a class="yt-timestamp" data-t="00:30:01">[00:30:01]</a>. As long as the other axioms are consistent, adding choice won't introduce contradictions <a class="yt-timestamp" data-t="00:30:43">[00:30:43]</a>.

## Current Status and Use

After Gödel and Cohen's work, the debates largely subsided <a class="yt-timestamp" data-t="00:30:58">[00:30:58]</a>. Today, the axiom of choice is almost universally accepted <a class="yt-timestamp" data-t="00:31:12">[00:31:12]</a>.

Its widespread acceptance stems from its utility:
*   **Simplifies Proofs**: It allows mathematicians to replace lengthy explicit proofs with more concise arguments, extending finite case proofs to any infinite case in a single line, reducing multi-page proofs to half a page <a class="yt-timestamp" data-t="00:31:24">[00:31:24]</a>.
*   **Essential for Theorems**: Many general theorems cannot be proven without using the axiom of choice somewhere <a class="yt-timestamp" data-t="00:31:45">[00:31:45]</a>.

While some mathematicians still prefer proofs without choice (even if harder, as they provide additional information by spelling out steps for infinite cases) <a class="yt-timestamp" data-t="00:31:53">[00:31:53]</a>, its inclusion is considered crucial for progress in modern mathematics <a class="yt-timestamp" data-t="00:32:30">[00:32:30]</a>. The question is not whether the axiom of choice is "right," but whether it is "right for what you want to do" in your mathematical system <a class="yt-timestamp" data-t="00:32:38">[00:32:38]</a>.