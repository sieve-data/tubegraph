---
title: Cantors Diagonalization Proof
videoId: _cr46G2K5Fo
---

From: [[veritasium]] <br/> 

The issue of mathematically choosing a number highlights a fundamental problem in mathematics: it is impossible to truly pick things at random, as formulas always yield the same result <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. The only way to select something in math is to follow a defined rule, such as "always choose the smallest thing" <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This works for sets like whole positive integers (smallest is one) or prime numbers (smallest is two) <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

However, this method fails for real numbers, which include positive, negative, whole, fractions, and irrationals like pi or the square root of two <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. Since real numbers stretch to negative infinity, choosing the smallest is impossible <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. Even attempting to choose the smallest number after one leads to an infinite sequence (1.01, 1.0001, etc.), demonstrating that there is no clear "next" number <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. If the order of real numbers cannot be definitively specified, mathematical selection becomes problematic <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

## Historical Context of Infinity

For centuries, the understanding of infinity was heavily influenced by Galileo's 1638 book <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. Galileo posed the question of whether there are more natural numbers or more square numbers <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. Intuitively, square numbers appear more sparse <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. However, Galileo realized he could create a one-to-one mapping between every natural number and its square, concluding that the two sets must be exactly the same size <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

From this counterintuitive result, Galileo inferred that terms like "more than" or "less than" do not apply to infinity in their usual sense, suggesting infinity is a single concept of "foreverness" <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. This perspective prevailed for centuries and is still how many people understand infinity today <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

## [[georg_cantor_and_the_development_of_set_theory | Georg Cantor]]'s Challenge to Infinity

Two hundred years after Galileo, [[georg_cantor_and_the_development_of_set_theory | Georg Cantor]] challenged this prevailing view <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. In 1874, he wondered if there could be two infinite sets that didn't perfectly map to each other, implying different "sizes" of infinity <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. He set out to compare the set of natural numbers with the set of real numbers between zero and one <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

### The Diagonalization Proof

[[georg_cantor_and_the_development_of_set_theory | Cantor]] began by assuming that these two sets *could* be perfectly mapped one-to-one <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. He imagined an infinite list where each natural number was paired with a unique real number between zero and one <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. Since there's no smallest real number, the real numbers on the list would be in any order <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

Assuming such a complete infinite list exists, [[georg_cantor_and_the_development_of_set_theory | Cantor]] then constructed a *new* real number not on the list <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>:
1.  He took the first digit of the first number on his list and added one to it <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
2.  He took the second digit of the second number and added one to it <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
3.  He continued this process down the list, always adding one to the *n*-th digit of the *n*-th number <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
4.  If a digit was an eight or a nine, he subtracted one instead of adding to avoid duplicates <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

The newly constructed real number, by design, could not appear anywhere on the original list <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. It differed from the first number in its first decimal place, from the second number in its second decimal place, and so on, down the "diagonal" <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. This method is why it's called [[georg_cantor_and_the_development_of_set_theory | Cantor]]'s Diagonalization Proof <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

The proof demonstrated that there must be more real numbers between zero and one than there are natural numbers extending to infinity <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

### Countable vs. Uncountable Infinities

[[georg_cantor_and_the_development_of_set_theory | Cantor]]'s work revealed that infinity comes in different "sizes" <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>:
*   **Countable Infinities**: Sets like square numbers, integers, or rational numbers that can be perfectly paired with the natural numbers (i.e., they can be "counted" 1, 2, 3, etc.) <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
*   **Uncountable Infinities**: Bigger infinities, such as the set of all real numbers or complex numbers, which cannot be matched one-to-one with the natural numbers <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

This groundbreaking result shocked the mathematical community, as it challenged the long-held belief that all infinities were the same <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. His work was dismissed by some as "a horror and a grave disease" <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

## The Well-Ordering Theorem and the Axiom of Choice

[[georg_cantor_and_the_development_of_set_theory | Cantor]]'s next ambition was to show that even uncountably infinite sets could be "well-ordered," meaning they could be placed in a definitive order <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. A set is well-ordered if it has a clear starting point, and every subset within it also has a clear starting point <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. While natural numbers are clearly well-ordered, and [[georg_cantor_and_the_development_of_set_theory | Cantor]] devised ways to well-order integers (e.g., 0, 1, -1, 2, -2...) <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>, he struggled to prove that the uncountably infinite set of real numbers could be well-ordered <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

Despite failing to prove it, [[georg_cantor_and_the_development_of_set_theory | Cantor]] published his well-ordering theorem, confident in its truth due to his religious beliefs <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. This lack of mathematical proof led to further ostracization from the mathematical community, notably from his former teacher Leopold Kronecker <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. The stress contributed to [[georg_cantor_and_the_development_of_set_theory | Cantor]]'s nervous breakdowns <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.

The resolution came in 1904 when Ernst Zermelo pinpointed a crucial, unstated assumption in [[georg_cantor_and_the_development_of_set_theory | Cantor]]'s work: the ability to make an infinite number of choices simultaneously from any set, including uncountable ones <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>. Zermelo formalized this assumption into an axiom: the Axiom of Choice <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>.

The Axiom of Choice states that if you have infinitely many non-empty sets, there is a way to choose one element from each set <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. This is obvious for finite sets or infinite sets with a clear rule (like "choose the smallest"), but it's essential for cases where no such rule exists <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>. The axiom doesn't specify *how* the choices are made, only that they are possible all at once <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.

Using the Axiom of Choice, Zermelo demonstrated how to well-order the real numbers:
1.  Choose a number (X1) from the set of all real numbers <a class="yt-timestamp" data-t="00:12:58">[00:12:58]</a>.
2.  Choose another number (X2) from the remaining reals <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.
3.  Continue this process, labeling numbers X3, X4, X5, and so on <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>.
4.  To account for the uncountable nature of real numbers, Zermelo introduced "omega numbers" (e.g., X_omega, X_omega+1), which come *after* the natural numbers in order, allowing the indexing to continue until all real numbers are ordered <a class="yt-timestamp" data-t="00:13:47">[00:13:47]</a>.

This process proves that a well-ordering of real numbers exists, even if the resulting order is counterintuitive (e.g., a billion could come before 0.2) <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>. The Axiom of Choice and [[georg_cantor_and_the_development_of_set_theory | Cantor]]'s well-ordering theorem were proven equivalent <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.

## Paradoxes and Acceptance

Despite its utility, the Axiom of Choice led to "disturbing results" <a class="yt-timestamp" data-t="00:17:49">[00:17:49]</a>:

*   **Vitali Set (1905)**: Giuseppe Vitali used the axiom to construct a set of numbers between zero and one that has no defined length or measure, challenging the fundamental idea that everything can be quantified <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>.
*   **[[the_banachtarski_paradox | Banach-Tarski Paradox]] (1924)**: Stefan Banach and Alfred Tarski demonstrated that, using the Axiom of Choice, a solid ball could be split into five pieces and reassembled into two identical balls, each the same size as the original <a class="yt-timestamp" data-t="00:23:19">[00:23:19]</a>. This infinite duplication is theoretically possible because the pieces created are non-measurable <a class="yt-timestamp" data-t="00:28:06">[00:28:06]</a>.

The mathematical community was in crisis, unsure whether to accept an axiom with such "obviously false" consequences <a class="yt-timestamp" data-t="00:29:20">[00:29:20]</a>.

The debate largely subsided after the work of [[gdels_incompleteness_theorems | Kurt Gödel]] and Paul Cohen:
*   In 1938, [[gdels_incompleteness_theorems | Kurt Gödel]] proved that if the other accepted axioms of set theory are true, then the Axiom of Choice is also true <a class="yt-timestamp" data-t="00:29:37">[00:29:37]</a>.
*   In 1963, Paul Cohen proved that there is also a world where all other axioms of set theory hold true *except* for the Axiom of Choice <a class="yt-timestamp" data-t="00:29:47">[00:29:47]</a>.

This situation is analogous to the [[the_parallel_postulate_and_noneuclidean_geometry | parallel postulate]] in geometry, where different assumptions lead to different valid geometries (spherical, flat, hyperbolic) <a class="yt-timestamp" data-t="00:29:57">[00:29:57]</a>. The Axiom of Choice can neither be proven nor disproven from the other axioms; it is an independent axiom <a class="yt-timestamp" data-t="00:30:38">[00:30:38]</a>.

Today, the Axiom of Choice is almost universally accepted <a class="yt-timestamp" data-t="00:32:12">[00:32:12]</a>. It is incredibly useful, simplifying proofs by extending finite cases to infinite ones with just a single statement <a class="yt-timestamp" data-t="00:31:22">[00:31:22]</a>. Many modern mathematical theorems cannot be proven without its use <a class="yt-timestamp" data-t="00:31:45">[00:31:45]</a>. While some mathematicians still prefer proofs without it for the additional information they provide, removing the Axiom of Choice makes progress in modern mathematics very difficult <a class="yt-timestamp" data-t="00:32:05">[00:32:05]</a>. The question is not whether the axiom is "right," but whether it is "right for what you want to do" <a class="yt-timestamp" data-t="00:32:38">[00:32:38]</a>.