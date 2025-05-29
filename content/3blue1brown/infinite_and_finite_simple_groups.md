---
title: Infinite and finite simple groups
videoId: mH0oCDa74tE
---

From: [[3blue1brown]] <br/> 

The Monster Group is a number approximately 8x10^53, a value comparable to the number of atoms in the planet Jupiter <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. This number is considered peculiar and reflective of something fundamental in mathematics <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. It represents the size of the Monster Group <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

## Introduction to Groups and Symmetry

[[introduction_to_group_theory | Group theory]] is a field focused on codifying the idea of [[group_theory_and_symmetries | symmetry]] <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
A face is symmetric if it can be reflected about a line and remain unchanged <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. A snowflake is symmetric in multiple ways, allowing rotations (e.g., 60 or 120 degrees) and flips along various axes, all of which leave its appearance unchanged <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
A collection of all such actions that leave an object looking the same is called a group <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. Mathematicians consider the action of doing nothing to also be part of a group <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. For example, the group of symmetries of a snowflake, including the do-nothing action, contains 12 distinct actions and is called D6 <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. The simple group of symmetries for a face, having only two elements, is named C2 <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

The actions describing symmetries always preserve an implicit structure <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   A cube has 24 rotations that preserve its appearance, forming a group <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   If reflections are allowed, not preserving orientation, the group becomes larger with 48 actions <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   If components (like faces) are less rigidly attached and can be shuffled, the group of "symmetries" becomes much larger and more complicated, reflecting a looser sense of preserved structure <a class="yt-timestamp" data-t="00:02:38">[00:03:00]</a>.

### Permutation Groups

The loosest sense of structure involves a collection of points where any shuffling, or permutation, is considered a symmetry <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. These "permutation groups" are unconstrained by underlying properties and can become very large <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   For six objects, there are 6! (720) possible permutations <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
*   If these points are given structure (e.g., corners of a hexagon with distance preservation), the number of symmetries reduces to 12 (like the snowflake symmetries) <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
*   For 12 points, the number of permutations is approximately 479 million <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
*   For 101 objects, there are 101! (around 9x10^159) different actions <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
These permutation groups are known as S-sub-n and are fundamental in group theory, encompassing all other groups in a certain sense <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

### Applications of Group Theory

Early applications of group theory revealed insights into solutions for polynomial equations <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   There are formulas for quadratic, cubic, and quartic equations <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   However, mathematicians struggled to find a formula for degree 5 polynomials <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
*   [[introduction_to_group_theory | Group theory]] shows that no quintic formula (using only arithmetic operations and radicals) can exist <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. This impossibility relates to the inner structure of the permutation group S5 <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

A theme in math is that the nature of [[group_theory_and_symmetries | symmetry]] can reveal non-obvious facts about other objects <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. In physics, Noether's theorem states that every conservation law corresponds to some kind of [[group_theory_and_symmetries | symmetry]] or group <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. This means fundamental laws like conservation of momentum and energy correspond to groups <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.

## Abstracting Groups

While groups can be understood as collections of actions, mathematicians define them more abstractly <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. Similar to how the number 3 is an abstract concept rather than a specific triplet of things, group elements are abstract entities <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
What defines a group is how its elements combine <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. Combining actions means applying one after another (e.g., flipping a snowflake then rotating it results in an equivalent single action) <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. This defines a "multiplication" operation <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
A multiplication table captures the inner structure of a group, abstracted away from the specific object it acts on (like a square or polynomial roots) <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

Formally, a group is a set with a binary operation (multiplication) that satisfies four axioms <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>. These axioms derive from properties that are inherently true when thinking about composing actions <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.

### Isomorphism

Abstraction in group theory is desirable because different situations can lead to the same underlying group <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>. For instance, the symmetries of a cube and the permutation group of four objects (S4) are fundamentally the same <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. This means their multiplication tables are identical, and anything true for one is true for the other <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
This relationship is called an isomorphism, which is a one-to-one mapping between group elements that preserves composition (multiplication) <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>. An important example is how the rotations of a cube permute its four diagonals <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>. Seeing the same group in different contexts reveals unexpected connections between distinct objects <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

## The Classification of Finite Simple Groups

A natural question in group theory is: "What are all the groups?" <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a> More precisely, "What are all the groups up to isomorphism?" meaning groups are considered the same if an isomorphism exists between them <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>. This is asking about all the ways something can be symmetric <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.

The question is exceedingly hard <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>. Groups are divided into [[infinite_math_utility_in_finite_contexts | infinite groups]] (like symmetries of a line or circle) and finite groups <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>. Focusing on finite groups, they can be broken down into "smaller groups" in a way analogous to prime factorization for numbers or atoms for molecules <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.
Groups that cannot be broken down any further are called [[the_classification_of_finite_simple_groups_and_sporadic_groups | simple groups]] <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>. For instance, the proof that no quintic formula exists involves showing that the permutation group on 5 elements (S5) decomposes into a type of simple group (cyclic groups of prime order) that polynomial solutions from radicals would not allow <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>. Understanding these "atomic" simple groups is crucial outside of group theory <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>.

The task of categorizing all finite groups has two steps:
1.  Find all the [[the_classification_of_finite_simple_groups_and_sporadic_groups | simple groups]] <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.
2.  Find all the ways to combine them <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>.

Mathematicians have successfully found and proven that they have found all [[the_classification_of_finite_simple_groups_and_sporadic_groups | finite simple groups]] <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>. This monumental achievement took decades, tens of thousands of pages, hundreds of minds, and computer assistance, culminating by 2004 <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.

The result is considered "absurd" <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>:
*   There are 18 distinct infinite families of simple groups <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>.
    *   One family includes cyclic groups with prime order (symmetries of a regular polygon with a prime number of sides, without flips) <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>.
    *   Another is similar to permutation groups (S-sub-n), simple if acting on 5 or more elements, which relates to why quintic polynomials lack radical solutions <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>.
*   There are also 26 [[the_classification_of_finite_simple_groups_and_sporadic_groups | sporadic groups]] that do not fit into these patterns <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>. This "patched together" fundamental structure is seen as bizarre <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>.

### The Monster Group

The largest of these [[the_classification_of_finite_simple_groups_and_sporadic_groups | sporadic groups]] is named the Monster Group <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>, with its size being 8x10^53 <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>. The second largest is the Baby Monster Group <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>. Nineteen of the [[the_classification_of_finite_simple_groups_and_sporadic_groups | sporadic groups]], including the Baby Monster, are considered "children of the monster" and are called the "happy family" by Robert Gries <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>. The remaining six are called "pariahs" <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>.

The Monster Group is not just big, but its abrupt presence as a fundamental building block is strange <a class="yt-timestamp" data-t="00:18:32">[00:18:32]</a>. The Monster acts on an object in 196,883 dimensions <a class="yt-timestamp" data-t="00:18:59">[00:18:59]</a>. Describing one element of this group requires about 4 GB of data, despite other much larger groups having smaller computational descriptions <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>.

### Why the Sporadic Groups? (Monstrous Moonshine)

The existence of [[the_classification_of_finite_simple_groups_and_sporadic_groups | sporadic groups]], particularly the Monster, remains largely mysterious <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>. In the 1970s, John McKay noticed a number very similar to 196,883 (one greater) appearing in the series expansion of a fundamental function related to modular forms and elliptic functions <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>. This observation, initially deemed "moonshine" by John Conway due to its seemingly crazy nature, led to the "monstrous moonshine conjecture" after more numerical coincidences <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>.
Richard Borcherds proved this conjecture in 1992, establishing a connection between disparate areas of mathematics <a class="yt-timestamp" data-t="00:20:40">[00:20:40]</a>. This proof contributed to him winning the Fields Medal six years later <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>. Monstrous Moonshine also has a connection to string theory <a class="yt-timestamp" data-t="00:20:53">[00:20:53]</a>.

The Monster Group serves as a reminder that fundamental objects in mathematics are not necessarily simple, and the universe's answers don't prioritize human understanding <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>.