---
title: Group theory and symmetries
videoId: mH0oCDa74tE
---

From: [[3blue1brown]] <br/> 

The YouTube math community collaborated on videos about their favorite numbers over one million, and one choice was roughly 8x10^53 <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. This seemingly arbitrary number is peculiar and reflects something fundamental, agreed upon even by alien civilizations or super-intelligent AIs <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. This number is the size of the monster group, which requires understanding [[introduction_to_group_theory | group theory]] <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

[[introduction_to_group_theory | Group theory]] is a field dedicated to codifying the idea of symmetry <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

## The Concept of Symmetry and Groups

When a face is symmetric, it means it can be reflected about a line and remain unchanged <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. This is a statement about an action that can be taken <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. A snowflake is also symmetric in more ways, allowing rotations (e.g., 60 or 120 degrees) and flips along various axes, all leaving it unchanged <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

A collection of all such actions, including the "do-nothing" action, is called a group <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>, <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. For example, the group of [[symmetries_and_dihedral_groups | symmetries]] of a snowflake includes 12 distinct actions and is called D6 <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. The group of [[symmetries_and_dihedral_groups | symmetries]] for a face has two elements and is called C2 <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. There is a "zoo of groups" categorizing ways something can be symmetric <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

### Preserved Structure and Permutation Groups

When describing these symmetric actions, there is always an implicit structure being preserved <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   A cube has 24 rotations that preserve its appearance, forming a group <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   Allowing reflections, which means orientation is not preserved, results in a larger group of 48 actions <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   If faces are allowed to be shuffled and rotated more freely, a much larger and more complicated group of actions forms <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. The size of this group reflects the looser sense of structure preserved <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

The loosest sense of structure involves a collection of points where any way they can be shuffled (any permutation) is considered a symmetry <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. These "permutation groups" are unconstrained by underlying properties and can become quite large <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. For example, there are 6! (720) possible permutations of six objects <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. In contrast, if these points were corners of a hexagon and only permutations preserving distances were considered, it would return the 12 snowflake [[symmetries_and_dihedral_groups | symmetries]] <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. Increasing the number of points to 12 results in about 479 million permutations <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

A group's largeness alone is not inherently interesting <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. For instance, shuffling 101 objects yields a group of approximately 9x10^159 actions <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. These are called S-sub-n permutation groups and are very important in [[introduction_to_group_theory | group theory]], encompassing all other groups in a certain sense <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

## Applications of Group Theory

[[introduction_to_group_theory | Group theory]] is remarkably useful <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

### Polynomial Equations
One of its earliest applications was realizing that the structure of [[permutation_groups_and_polynomial_equations | permutation groups]] provides insight into solutions for polynomial equations <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. While formulas exist for quadratic, cubic, and quartic equations, mathematicians struggled to find a formula for degree 5 polynomials <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. It turns out that thinking about the group that permutes the roots of such a polynomial reveals that no quintic formula can exist using only basic arithmetic operations and radicals <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. This impossibility is due to the inner structure of the [[permutation_groups_and_polynomial_equations | permutation group]] S5 <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

### Physics and Conservation Laws
A recurring theme in mathematics is that the nature of symmetry itself can reveal non-obvious facts about other studied objects <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. In physics, Noether's theorem states that every conservation law (like conservation of momentum or energy) corresponds to a type of symmetry, a certain group <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. This means groups are fundamental and universal <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.

## Groups as Abstractions: From Actions to Abstract Structures

While initially described as a collection of actions, groups are typically defined more abstractly <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>, <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. Just as the number 3 is an abstraction rather than a specific triplet of things, mathematicians think of group elements as abstract objects represented by symbols, independent of specific actions on specific objects <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.

What defines a group are the ways its elements combine, which is a form of "multiplication" <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. In the context of actions, combining means applying one action after another <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. For example, flipping a snowflake then rotating it is equivalent to a single, different flip <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. All possible combinations define a "multiplication" that gives a group its structure <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. A multiplication table can capture this inner structure symbolically, abstracting it from any specific object it might act on <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

The formal definition of a group is a set of things with a binary operation (multiplication) satisfying four special rules or axioms <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>. These axioms arise from the obvious properties of composing actions <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>. Understanding that groups relate to symmetric actions in the same way numbers relate to counts can make the abstract definition more grounded for students <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.

### Isomorphism: When Groups Are "The Same"

An example of this abstraction's desirability is comparing the [[group_actions_in_mathematical_objects | symmetries of a cube]] and the [[permutation_groups_and_polynomial_equations | permutation group]] of four objects <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. Though they initially feel different, these two groups are "the same" because their multiplication tables are identical <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. This means anything true about one group is true about the other <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.

The precise way to state this correspondence is through an **isomorphism**, which is a one-to-one mapping between groups that preserves composition <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>. If applying two actions in one group corresponds to applying their mapped counterparts in another group, and the result also maps correctly, it's an isomorphism <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>. This is the most important idea in [[introduction_to_group_theory | group theory]] <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>. Seeing the same group arise in seemingly unrelated situations reveals unexpected connections between distinct mathematical objects <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

## The Classification of Finite Simple Groups and the Monster

Understanding groups as abstractions leads to the question: "What are all the groups up to isomorphism?" <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>. This means considering two groups the same if an isomorphism exists between them <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>. This question asks what all the fundamental ways something can be symmetric are <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.

The problem is exceedingly hard, requiring a division between [[infinite_and_finite_simple_groups | infinite groups]] (like [[symmetries_and_dihedral_groups | symmetries]] of a line or circle) and finite groups <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>. Finite groups can be broken down into a "composition of smaller groups" <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>. The ones that cannot be broken down further are called [[infinite_and_finite_simple_groups | simple groups]], analogous to prime numbers or atoms <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>. For example, the proof that no quintic formula exists involves showing that if one did, it would imply the [[permutation_groups_and_polynomial_equations | permutation group]] on 5 elements decomposes into [[infinite_and_finite_simple_groups | cyclic groups of prime order]], but its actual breakdown involves a different kind of simple group that radicals cannot produce <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>.

The task of categorizing all finite groups has two steps:
1.  Find all the [[infinite_and_finite_simple_groups | simple groups]] (like finding the periodic table) <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.
2.  Find all the ways to combine them (like doing chemistry) <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>.

Mathematicians successfully found and proved that they discovered all finite [[infinite_and_finite_simple_groups | simple groups]] <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>. This monumental achievement took decades, tens of thousands of pages, hundreds of minds, and significant computer assistance, culminating in 2004 <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.

### The Monster Group

The classification result is described as "absurd" <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>. There are 18 distinct infinite families of [[infinite_and_finite_simple_groups | simple groups]] <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>. However, there are also 26 [[the_classification_of_finite_simple_groups_and_sporadic_groups | simple groups]] that don't fit these patterns, known as **sporadic groups** <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>. This patched-together structure for a field rooted in symmetry is bizarre <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>.

The largest of these [[the_classification_of_finite_simple_groups_and_sporadic_groups | sporadic groups]] is known as the **Monster group**, named by John Conway, with a size of roughly 8x10^53 <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>. The second largest is called the Baby Monster group <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>. Robert Gries called 20 of these [[the_classification_of_finite_simple_groups_and_sporadic_groups | sporadic groups]], including the Monster and Baby Monster, the "happy family," and the remaining six "pariahs" <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.

The oddity isn't the Monster group's size, but that one of the fundamental building blocks of math abruptly stops around 8x10^53 <a class="yt-timestamp" data-t="00:18:32">[00:18:32]</a>. While groups typically describe [[symmetries_and_dihedral_groups | symmetries]] of objects, the Monster group acts on an object in 196,883 dimensions, which is impossible to visualize in 2, 3, 4, or 5 dimensions <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>. Describing just one element of this group requires about 4 GB of data, even though much larger groups can have smaller computational descriptions <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>.

### Why the Sporadic Groups? (Monstrous Moonshine)

No one fully understands why the [[the_classification_of_finite_simple_groups_and_sporadic_groups | sporadic groups]], especially the Monster, exist <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>. Despite their deep fundamental nature in math and physics, much remains mysterious <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.

In the 1970s, mathematician John McKay noticed that the number 196,883 (or one more than it) appeared in a completely unrelated context: the series expansion of a fundamental function related to modular forms and elliptic functions <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>. This seemed so outlandish that John Conway playfully called it "moonshine" <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>. After more numerical coincidences were found, it became known as the "Monstrous Moonshine Conjecture" <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>. Richard Borcherds proved this conjecture in 1992, solidifying a connection between disparate mathematical fields and earning him a Fields Medal in 1998 <a class="yt-timestamp" data-t="00:20:40">[00:20:40]</a>. This moonshine connection also links the Monster to string theory <a class="yt-timestamp" data-t="00:20:53">[00:20:53]</a>.

The Monster group, with its absurd size, serves as a reminder that fundamental objects are not necessarily simple, and the universe's answers don't prioritize human understanding <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>.