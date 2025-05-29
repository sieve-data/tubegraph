---
title: The classification of finite simple groups and sporadic groups
videoId: mH0oCDa74tE
---

From: [[3blue1brown]] <br/> 

The classification of finite simple groups is considered one of the most monumental achievements in the history of mathematics <a class="yt-timestamp" data-t="16:26">00:16:26</a>. This complex field delves into the fundamental building blocks of [[introduction_to_group_theory|group theory]] itself, revealing patterns and irregularities in the mathematical universe. At its heart is the [[the_monster_group_and_its_significance_in_mathematics|Monster Group]], a mathematical object whose immense size, approximately 8 x 10^53, reflects something profoundly peculiar and fundamental about symmetry <a class="yt-timestamp" data-t="00:16:43">00:16:43</a>.

## What is a Group?

[[introduction_to_group_theory|Group theory]] is a field dedicated to codifying the idea of [[group_theory_and_symmetries|symmetry]] <a class="yt-timestamp" data-t="00:00:52">00:00:52</a>. When an object is symmetric, it means certain actions can be applied to it that leave it looking exactly the same <a class="yt-timestamp" data-t="00:00:56">00:00:56</a>.
*   **Examples of Symmetry:**
    *   A face: can be reflected about a central line and appear unchanged <a class="yt-timestamp" data-t="00:00:56">00:00:56</a>.
    *   A snowflake: can be rotated by 60 or 120 degrees, or flipped along various axes, while remaining the same <a class="yt-timestamp" data-t="00:01:08">00:01:08</a>.

A collection of all such actions that leave an object unchanged is called a group <a class="yt-timestamp" data-t="00:01:20">00:01:20</a>. Mathematicians always include the "do-nothing" action as part of the group <a class="yt-timestamp" data-t="00:01:41">00:01:41</a>. For instance:
*   The group of [[symmetries_and_dihedral_groups|symmetries]] of a snowflake (D6) includes 12 distinct actions <a class="yt-timestamp" data-t="00:01:46">00:01:46</a>.
*   The simple group of [[symmetries_and_dihedral_groups|symmetries]] for a face (C2) has two elements <a class="yt-timestamp" data-t="00:01:56">00:01:56</a>.

Different objects possess different forms of [[group_theory_and_symmetries|symmetry]], leading to a vast "zoo of groups" <a class="yt-timestamp" data-t="00:02:03">00:02:03</a>.

### Groups and Structure Preservation

When describing [[group_actions_in_mathematical_objects|symmetries]] or actions, there's always an implicit structure being preserved <a class="yt-timestamp" data-t="00:02:12">00:02:12</a>.
*   **Cube Rotations:** There are 24 rotations that leave a cube looking the same, forming a group <a class="yt-timestamp" data-t="00:02:17">00:02:17</a>.
*   **Cube Rotations and Reflections:** Including reflections, which means the orientation of the cube is not preserved, results in a larger group of 48 actions <a class="yt-timestamp" data-t="00:02:27">00:02:27</a>.
*   **Looser Structures:** If faces are allowed to rotate and shuffle, the resulting group of [[group_actions_in_mathematical_objects|symmetries]] becomes much larger and more complicated, reflecting a looser sense of preserved structure <a class="yt-timestamp" data-t="00:02:38">00:02:38</a>.

The loosest sense of structure involves a collection of points where any way to shuffle them is considered a [[group_theory_and_symmetries|symmetry]] <a class="yt-timestamp" data-t="00:03:08">00:03:08</a>. These are known as [[permutation_groups_and_polynomial_equations|permutation groups]].

### [[permutation_groups_and_polynomial_equations|Permutation Groups]]

[[permutation_groups_and_polynomial_equations|Permutation groups]] are unconstrained by underlying properties, making them capable of becoming very large <a class="yt-timestamp" data-t="00:03:18">00:03:18</a>.
*   **Example (6 Objects):** The total number of permutations for six objects is 6!, or 720 <a class="yt-timestamp" data-t="00:03:41">00:03:41</a>.
*   **Example (12 Objects):** For 12 objects, the number of permutations grows to about 479 million <a class="yt-timestamp" data-t="00:03:59">00:03:59</a>.
*   **Example (101 Objects):** Shuffling 101 objects results in a group size of roughly 9 x 10^159, a number vastly larger than the number of atoms in the observable universe multiplied by itself <a class="yt-timestamp" data-t="00:04:17">00:04:17</a>.

These permutation groups are denoted as S-sub-n (Sn) and are crucial in [[introduction_to_group_theory|group theory]] because they encompass all other groups in a certain sense <a class="yt-timestamp" data-t="00:04:37">00:04:37</a>.

### Applications of [[introduction_to_group_theory|Group Theory]]

[[introduction_to_group_theory|Group theory]] has practical applications, notably in understanding solutions to polynomial equations <a class="yt-timestamp" data-t="00:04:53">00:04:53</a>.
*   **Polynomial Formulas:** While formulas exist for quadratic, cubic, and quartic equations, mathematicians struggled to find a general formula for degree 5 (quintic) polynomials <a class="yt-timestamp" data-t="00:05:04">00:05:04</a>.
*   **Impossibility of Quintic Formula:** The structure of the [[permutation_groups_and_polynomial_equations|permutation group]] S5 reveals that no quintic formula can exist using only basic arithmetic operations and radicals <a class="yt-timestamp" data-t="00:05:34">00:05:34</a>. This impossibility is directly linked to the inner structure of S5 <a class="yt-timestamp" data-t="00:06:04">00:06:04</a>.
*   **Noether's Theorem:** In physics, Noether's theorem states that every conservation law (e.g., conservation of momentum, conservation of energy) corresponds to a specific [[group_theory_and_symmetries|symmetry]], or group <a class="yt-timestamp" data-t="00:06:23">00:06:23</a>. This demonstrates how the nature of [[group_theory_and_symmetries|symmetry]] reveals non-obvious facts about other mathematical and physical objects <a class="yt-timestamp" data-t="00:06:13">00:06:13</a>.

## Abstract Groups vs. [[Group actions in mathematical objects|Group Actions]]

While groups are often introduced through [[group_actions_in_mathematical_objects|symmetric actions]], mathematicians typically define them more abstractly <a class="yt-timestamp" data-t="00:01:27">00:01:27</a>.
*   **Abstraction:** Just as the number 3 is an abstract concept rather than a specific triplet of objects, group elements are abstract entities, not necessarily specific actions on specific objects <a class="yt-timestamp" data-t="00:07:18">00:07:18</a>.
*   **Group Multiplication:** What defines a group is how its elements combine with each other, often called "multiplication." In the context of actions, this means applying one action after another <a class="yt-timestamp" data-t="00:08:04">00:08:04</a>. For example, flipping a snowflake then rotating it is equivalent to a single flip about a diagonal line <a class="yt-timestamp" data-t="00:08:18">00:08:18</a>.
*   **Formal Definition:** A group is formally defined as a set of things with a binary operation (multiplication) that satisfies four specific axioms <a class="yt-timestamp" data-t="00:59:59">00:59:59</a>. These axioms arise from the inherent properties of composing actions <a class="yt-timestamp" data-t="00:10:19">00:10:19</a>.
*   **Isomorphism:** A core concept in [[introduction_to_group_theory|group theory]] is isomorphism, where two groups are considered "the same" if their multiplication tables are identical, even if they describe different kinds of actions <a class="yt-timestamp" data-t="00:11:07">00:11:07</a>. For instance, the [[symmetries_and_dihedral_groups|symmetries]] of a cube (rotations) are isomorphic to the [[permutation_groups_and_polynomial_equations|permutation group]] of four objects <a class="yt-timestamp" data-t="00:10:46">00:10:46</a>. This happens because cube rotations permute its four diagonals <a class="yt-timestamp" data-t="00:12:34">00:12:34</a>.

## The Classification Problem: What are All the Groups?

The abstraction of groups leads to a fundamental question: "What are all the groups up to isomorphism?" <a class="yt-timestamp" data-t="00:13:34">00:13:34</a> This asks, fundamentally, "What are all the ways that something can be symmetric?" <a class="yt-timestamp" data-t="00:13:53">00:13:53</a>

The problem is exceedingly hard <a class="yt-timestamp" data-t="00:14:05">00:14:05</a>.
*   **[[infinite_and_finite_simple_groups|Infinite and Finite Groups]]:** Groups can be infinite (e.g., [[group_theory_and_symmetries|symmetries]] of a line or circle) or finite. To simplify, mathematicians focused on classifying finite groups <a class="yt-timestamp" data-t="00:14:10">00:14:10</a>.
*   **[[infinite_and_finite_simple_groups|Simple Groups]]:** Analogous to prime numbers or atoms, finite groups can be broken down into "simple groups" – those that cannot be broken down any further <a class="yt-timestamp" data-t="00:14:25">00:14:25</a>. The proof that no quintic formula exists, for example, relies on understanding how the [[permutation_groups_and_polynomial_equations|permutation group]] on 5 elements decomposes into simple groups <a class="yt-timestamp" data-t="00:14:48">00:14:48</a>.

The task of categorizing all finite groups breaks down into two steps:
1.  Find all the simple groups (analogous to finding the periodic table of elements) <a class="yt-timestamp" data-t="00:15:45">00:15:45</a>.
2.  Find all the ways to combine them (analogous to chemistry) <a class="yt-timestamp" data-t="00:15:50">00:15:50</a>.

## The Classification of Finite [[infinite_and_finite_simple_groups|Simple Groups]]

Mathematicians successfully found and proved the completeness of the list of all finite [[infinite_and_finite_simple_groups|simple groups]] <a class="yt-timestamp" data-t="00:16:00">00:16:00</a>. This monumental effort took decades, involved thousands of pages of advanced mathematics, hundreds of researchers, and significant computer assistance, culminating in 2004 <a class="yt-timestamp" data-t="00:16:12">00:16:12</a>.

The answer, however, was "absurd" <a class="yt-timestamp" data-t="00:16:33">00:16:33</a>:
*   **Infinite Families:** There are 18 distinct infinite families of simple groups <a class="yt-timestamp" data-t="00:16:36">00:16:36</a>. Examples include:
    *   Cyclic groups of prime order: [[symmetries_and_dihedral_groups|symmetries]] of a regular polygon with a prime number of sides, without flips <a class="yt-timestamp" data-t="00:17:08">00:17:08</a>.
    *   Certain [[permutation_groups_and_polynomial_equations|permutation groups]]: For n >= 5 elements, these groups are simple and relate to why polynomials of degree 5 or more cannot be solved using radicals <a class="yt-timestamp" data-t="00:17:21">00:17:21</a>.
*   **Sporadic Groups:** In addition to these families, there are 26 simple groups that do not fit into any of the established patterns <a class="yt-timestamp" data-t="00:16:43">00:16:43</a>. These are known as the [[the_monster_group_and_its_significance_in_mathematics|sporadic groups]] <a class="yt-timestamp" data-t="00:16:51">00:16:51</a>. Their existence is considered bizarre, as if the universe's fundamental structure was "designed by committee" <a class="yt-timestamp" data-t="00:17:02">00:17:02</a>.

### The [[the_monster_group_and_its_significance_in_mathematics|Monster Group]]

The largest of these [[the_monster_group_and_its_significance_in_mathematics|sporadic groups]] is famously known as the [[the_monster_group_and_its_significance_in_mathematics|Monster Group]], with a size of approximately 8 x 10^53 <a class="yt-timestamp" data-t="00:17:58">00:17:58</a>. The second largest is called the "baby monster group" <a class="yt-timestamp" data-t="00:18:06">00:18:06</a>.
*   **The Happy Family:** 19 of these [[the_monster_group_and_its_significance_in_mathematics|sporadic groups]] are, in a sense, "children" of the [[the_monster_group_and_its_significance_in_mathematics|Monster Group]], forming what Robert Gries termed the "happy family" (a total of 20, including the Monster itself) <a class="yt-timestamp" data-t="00:18:11">00:18:11</a>.
*   **The Pariahs:** The remaining six sporadic groups are called "pariahs" because they don't even fit into the "happy family" pattern <a class="yt-timestamp" data-t="00:18:20">00:18:20</a>.

The sheer size of the [[the_monster_group_and_its_significance_in_mathematics|Monster Group]] is less interesting than the fact that a fundamental building block of mathematics abruptly stops at this specific, peculiar number <a class="yt-timestamp" data-t="00:18:32">00:18:32</a>.

### What Does the [[the_monster_group_and_its_significance_in_mathematics|Monster Group]] Act On?

The [[the_monster_group_and_its_significance_in_mathematics|Monster Group]] describes the [[group_actions_in_mathematical_objects|symmetries]] of an object that exists in a staggering 196,883 dimensions <a class="yt-timestamp" data-t="00:18:52">00:18:52</a>. Simply describing one element of this group requires about 4 GB of data, despite other much larger groups having simpler computational descriptions <a class="yt-timestamp" data-t="00:19:17">00:19:17</a>.

### Why the Sporadic Groups?

The reason for the existence of the [[the_monster_group_and_its_significance_in_mathematics|sporadic groups]], particularly the [[the_monster_group_and_its_significance_in_mathematics|Monster Group]], remains largely a mystery <a class="yt-timestamp" data-t="00:19:42">00:19:42</a>.
*   **Monstrous Moonshine:** In the 1970s, mathematician John McKay noticed a number strikingly similar to 196,883 appearing in the series expansion of a fundamental function related to modular forms and elliptic functions, a completely unrelated field of mathematics <a class="yt-timestamp" data-t="00:20:00">00:20:00</a>. This surprising connection was playfully dubbed "moonshine" by John Conway <a class="yt-timestamp" data-t="00:20:25">00:20:25</a>.
*   **Conjecture and Proof:** Further numerical coincidences led to the "monstrous moonshine conjecture," which was proven by Richard Borcherds in 1992 <a class="yt-timestamp" data-t="00:20:30">00:20:30</a>. This proof revealed deep, unexpected connections between vastly different areas of mathematics, earning Borcherds a Fields Medal <a class="yt-timestamp" data-t="00:20:40">00:20:40</a>.
*   **String Theory Connection:** Related to this moonshine, there is also a connection between the [[the_monster_group_and_its_significance_in_mathematics|Monster Group]] and string theory, highlighting its relevance to physics despite its seemingly random nature <a class="yt-timestamp" data-t="00:20:53">00:20:53</a>.

The existence of the [[the_monster_group_and_its_significance_in_mathematics|Monster Group]] and the [[the_monster_group_and_its_significance_in_mathematics|sporadic groups]] serves as a reminder that fundamental mathematical objects are not necessarily simple or clean; they are what they are by logical necessity <a class="yt-timestamp" data-t="00:21:09">00:21:09</a>.