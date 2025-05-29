---
title: Group theory and the idea of symmetry
videoId: mH0oCDa74tE
---

From: [[3blue1brown]] <br/> 

[[introduction_to_group_theory | Group theory]] is a field of mathematics dedicated to codifying the idea of [[symmetries_and_group_actions | symmetry]] <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. While seemingly abstract, it reveals fundamental structures underlying various mathematical and physical phenomena <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

## Understanding Symmetry through Actions
When something is described as symmetric, it means that certain actions can be applied to it, leaving it looking exactly the same <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   **Reflection**: A face is symmetric because it can be reflected about a line and remain unchanged <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   **Rotation**: A snowflake has more symmetries, including rotations (e.g., 60 or 120 degrees) and flips along various axes, all of which preserve its appearance <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

A collection of all such actions that leave an object unchanged is called a **group** <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. The "do-nothing" action (identity) is always included as part of the group <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. For instance, the group of symmetries of a snowflake (D6) includes 12 distinct actions <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>, while the simple group of symmetries for a face (C2) has two elements <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

### Preserving Structure
When describing symmetric actions, there is always an implicit structure that is being preserved <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   A cube has 24 rotations that leave it looking the same <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. If reflections are allowed, the group expands to 48 actions, implying that the orientation of the cube is no longer a preserved structure <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   Loosening the preserved structure (e.g., allowing faces to rotate and shuffle independently) results in a much larger and more complex group <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. The larger size of the group reflects a looser sense of preserved structure <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

## [[the_concept_of_simple_groups_and_permutation_groups | Permutation Groups]]
The loosest sense of structure involves a collection of points where any way of shuffling them (any permutation) is considered a symmetry <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. These "permutation groups" are unconstrained by underlying properties and can become very large <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   For six objects, there are 6! (720) possible permutations <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
*   For 12 points, the number of permutations grows to about 479 million <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
*   Permutation groups of `n` objects are denoted as `S_n` <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. For example, `S_101` has a size of approximately 9x10^159 <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
These groups are fundamental in [[introduction_to_group_theory | group theory]], in a sense encompassing all other groups <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

## Applications of Group Theory
[[introduction_to_group_theory | Group theory]] has numerous applications beyond simply classifying symmetries:

### Polynomial Equations
One of the earliest applications of [[introduction_to_group_theory | group theory]] was in understanding the solutions to polynomial equations <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   Formulas exist for quadratic, cubic, and quartic (degree 2, 3, and 4) polynomials <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   Mathematicians struggled to find a formula for degree 5 polynomials <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. [[introduction_to_group_theory | Group theory]] revealed that no such formula exists, if limited to the four basic operations and radicals <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. This impossibility is linked to the inner structure of the [[the_concept_of_simple_groups_and_permutation_groups | permutation group]] `S_5` <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

### Physics and Conservation Laws
The nature of symmetry itself can reveal non-obvious facts about other objects of study <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. In physics, Noether's theorem states that every conservation law (e.g., conservation of momentum, conservation of energy) corresponds to a specific symmetry, or a group <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. These groups represent actions that leave the laws of physics unchanged <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

## Groups as Abstractions
While initial examples of groups involve specific actions on objects, mathematicians typically define groups more abstractly <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   **Analogy to Numbers**: Just as the number "3" is an abstraction not tied to a specific triplet of things, group elements are abstractions not necessarily tied to specific actions <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
*   **Group Operation (Multiplication)**: What defines a group is how its elements combine with each other, often called "multiplication" <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. This combination signifies applying one action after another <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. A multiplication table can capture the inner structure of a group, abstracted away from any specific object it might act on <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   **Formal Definition**: Formally, a group is a set with a binary operation (multiplication) that satisfies four specific axioms <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>. These axioms arise naturally from the properties observed when composing actions <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>. Understanding the relationship between abstract groups and symmetric actions, similar to numbers and counts, can make the study of [[introduction_to_group_theory | group theory]] more grounded <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.

## Isomorphism: The "Sameness" of Groups
Two groups are considered "the same" if their multiplication tables are identical, meaning there's a one-to-one mapping between their elements that preserves their composition (multiplication) <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. This concept is called **isomorphism**, and it is perhaps the most important idea in [[introduction_to_group_theory | group theory]] <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.
*   For example, the symmetries of a cube (which act on eight corners) are isomorphic to the [[the_concept_of_simple_groups_and_permutation_groups | permutation group]] of four objects <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. This means anything true about one group is true for the other <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>. The connection is revealed by how cube rotations permute its four diagonals <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.

The idea of isomorphism allows mathematicians to ask a more sophisticated question: "What are all the groups *up to isomorphism*?" <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a> This asks for all the *ways* something can be symmetric, not just all the symmetric things <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.

## The Classification of Finite [[the_concept_of_simple_groups_and_permutation_groups | Simple Groups]]
To make the classification of groups tractable, the focus is typically on finite groups <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>.
*   **[[the_concept_of_simple_groups_and_permutation_groups | Simple groups]]** are analogous to prime numbers or atoms; they are the "building blocks" of finite groups and cannot be broken down further <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.
*   The proof for the impossibility of a quintic formula involves showing that the [[the_concept_of_simple_groups_and_permutation_groups | permutation group]] on 5 elements decomposes into a different kind of [[the_concept_of_simple_groups_and_permutation_groups | simple group]] than what polynomial solutions built from radicals would imply <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>. Understanding these "atomic" [[the_concept_of_simple_groups_and_permutation_groups | simple groups]] is crucial <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>.

The task of [[the_classification_of_finite_simple_groups | classifying all finite simple groups]] breaks down into two steps:
1.  Find all the [[the_concept_of_simple_groups_and_permutation_groups | simple groups]] (like creating a periodic table) <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>.
2.  Find all the ways to combine them (like doing chemistry) <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>.

Mathematicians successfully completed the first step. By 2004, after decades of work by hundreds of minds, tens of thousands of pages of advanced math, and significant computer assistance, a definitive answer was reached <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>. This is considered one of the most monumental achievements in math history <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>.

### The "Absurd" Answer: Sporadic Groups
The classification revealed an "absurd" answer <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>:
*   **18 infinite families** of [[the_concept_of_simple_groups_and_permutation_groups | simple groups]] <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>. Examples include cyclic groups of prime order (symmetries of regular polygons without flips) and certain constrained [[the_concept_of_simple_groups_and_permutation_groups | permutation groups]] <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>.
*   **26 sporadic groups**: These [[the_concept_of_simple_groups_and_permutation_groups | simple groups]] don't fit into any of the 18 infinite families <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>. Their existence makes the fundamental structure of symmetry seem "patched together" and bizarre <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>.

### The Monster Group
The largest of the sporadic groups is known as the **Monster group** <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>. Its size is approximately 8x10^53 <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.
*   For scale, this is roughly the number of atoms in the planet Jupiter <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.
*   The second largest is called the **Baby Monster group** <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.
*   19 of the sporadic groups, including the Baby Monster, are in some sense "children" of the Monster, forming what Robert Gries called the "happy family" <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>. The remaining six are called "pariahs" <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>.
*   What the Monster group "acts on" is a 196,883-dimensional object <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>. Describing just one element of this group can take about 4 GB of data <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>, despite much larger [[the_concept_of_simple_groups_and_permutation_groups | permutation groups]] having smaller computational descriptions <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>.

The existence of the sporadic groups, especially the Monster, remains a mystery, though they are deeply fundamental to mathematics and possibly physics <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>.

### Monstrous Moonshine
In the 1970s, mathematician John McKay noticed a number very similar to 196,883 (one greater, 196,884) appearing in the series expansion of a fundamental function related to modular forms and elliptic functions <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>. This seemed like a crazy coincidence, playfully dubbed "moonshine" by John Conway <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>.
*   After more numerical coincidences, this led to the **monstrous moonshine conjecture** <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>.
*   This conjecture was proven by Richard Borcherds in 1992, establishing a profound connection between disparate areas of mathematics <a class="yt-timestamp" data-t="00:20:40">[00:20:40]</a>. Borcherds later won a Fields Medal, partly for this proof <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>.
*   Related to moonshine, there is also a connection between the Monster and string theory <a class="yt-timestamp" data-t="00:20:53">[00:20:53]</a>.

The Monster group serves as a reminder that fundamental mathematical objects are not always simple or aesthetically "clean," existing by logical necessity rather than human preference <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>.