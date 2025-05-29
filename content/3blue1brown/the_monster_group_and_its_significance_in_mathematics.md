---
title: The monster group and its significance in mathematics
videoId: mH0oCDa74tE
---

From: [[3blue1brown]] <br/> 

The Monster Group is a number of immense size, roughly 8x10 to the 53, which is comparable to the number of atoms in the planet Jupiter <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. Despite its seemingly arbitrary nature, it is considered by mathematicians to reflect something fundamental <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. This peculiar number represents the size of what is known as the Monster Group <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

## Introduction to Group Theory: The Codification of Symmetry

To understand the Monster Group, one must first grasp the concept of [[introduction_to_group_theory | group theory]] <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. This field of mathematics is dedicated to codifying the idea of symmetry <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

### Group Actions

When something is symmetric, it means certain [[group_actions_in_mathematical_objects | actions]] can be performed on it that leave it looking completely the same <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   For example, a face is symmetric if it can be reflected about a line <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   A snowflake is symmetric in more ways, allowing rotations (e.g., 60 or 120 degrees) and flips along various axes <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
*   A collection of all such actions that leave an object unchanged is called a group <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. The "do-nothing" action is always considered part of the group <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. For instance, the group of symmetries of a snowflake (D6) includes 12 distinct actions <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

These actions always imply an implicit structure being preserved <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. For a cube, there are 24 rotations that preserve its appearance, forming a group <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. If reflections are allowed (meaning orientation is not preserved), the group grows to 48 actions <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

### Permutation Groups

The loosest sense of structure involves a collection of points where any way to shuffle them (any permutation) is considered a symmetry <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. These "permutation groups" can become very large <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   For six objects, there are 6! or 720 possible permutations <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
*   For 12 points, the number of permutations is about 479 million <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
*   Shuffling 101 objects results in a group with a size of approximately 9x10 to the 159, known as S_101 <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

The permutation groups, denoted as S_n, are crucial in group theory, as they encompass all other groups in a certain sense <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

### Early Applications of Group Theory

One of the earliest applications of [[introduction_to_group_theory | group theory]] was in understanding solutions to polynomial equations <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. While formulas exist for quadratic, cubic, and quartic equations, mathematicians struggled to find one for degree 5 polynomials <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. Group theory revealed that no such formula exists for degree 5 polynomials using only basic arithmetic operations and radicals <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. This impossibility is linked to the inner structure of the permutation group S5 <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

Group theory also applies to physics, notably through Noether's theorem, which states that every conservation law corresponds to some kind of symmetry or group <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

## Groups as Abstract Mathematical Objects

Mathematicians often discuss groups not just as specific actions, but as abstract objects in themselves, where elements are represented symbolically <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
*   What defines a group is how its elements combine with each other, often through composition (applying one action after another) <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. This combination defines a type of "multiplication" that gives the group its structure <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
*   An **isomorphism** is a one-to-one mapping between two groups that preserves their composition (multiplication) <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>. If an isomorphism exists, the groups are considered "the same" <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. For example, the rotations of a cube are isomorphic to the permutation group of four objects <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.

Understanding groups as abstractions is key to appreciating their role in revealing unexpected connections between distinct mathematical objects <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

## The Classification of Finite Simple Groups

A fundamental question in group theory is: "What are all the groups up to isomorphism?" <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>. This means identifying all the fundamental ways something can be symmetric <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>. To make this tractable, mathematicians focus on **finite groups** <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>.

Similar to how numbers can be broken down into prime factors, finite groups can be decomposed into "smaller groups" <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>. The groups that cannot be broken down further are called **simple groups** <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>. The impossibility of a quintic formula is related to the specific kind of simple group involved in the decomposition of S5 <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.

The classification of all [[infinite_and_finite_simple_groups | finite simple groups]] was a monumental achievement in mathematics, taking many decades, tens of thousands of pages, hundreds of minds, and significant help from computers <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>. By 2004, a definitive answer was reached <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.

The answer, however, is "absurd" <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>:
1.  **18 distinct infinite families of simple groups**: Examples include cyclic groups with prime order (symmetries of regular polygons without flips) <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a> and permutation groups (with a slight constraint for n>=5) <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>.
2.  **26 sporadic groups**: These groups do not fit into the infinite families <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>. Their existence implies a "patched together" fundamental structure for symmetry itself, which is considered bizarre <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>.

## The Monster Group

The largest of these sporadic groups is known as the **Monster Group** <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>. Its size is the number mentioned at the start: approximately 8x10 to the 53 <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>. The second largest is called the "Baby Monster group" <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>. Together with the Baby Monster, 19 of the sporadic groups are considered "children of the Monster" and are known as the "happy family," while the remaining six are called "pariahs" <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.

The Monster Group is peculiar not just because of its size, but because it is a fundamental building block of mathematics that "abruptly stops" at this immense magnitude <a class="yt-timestamp" data-t="00:18:36">[00:18:36]</a>.

### What Does the Monster Act On?

If one wonders what object the Monster Group describes the symmetries of, the answer lies in a space of 196,883 dimensions <a class="yt-timestamp" data-t="00:18:52">[00:18:52]</a>. Even describing one element of this group requires about 4 GB of data, which is computationally complex even when compared to much larger groups like S_101 <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>.

### Why the Sporadic Groups?

No one fully understands why the sporadic groups, especially the Monster, exist <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>. Despite their fundamental nature in mathematics and potentially physics, much about them remains mysterious <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>.

In the 1970s, mathematician John McKay observed that the number 196,883 (or one more than it) appeared in the series expansion of a fundamental function related to modular forms and elliptic functions, a completely unrelated field of mathematics <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>. This perceived coincidence was playfully termed "moonshine" by John Conway <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>. More numerical coincidences led to the **Monstrous Moonshine Conjecture**, which was proved by Richard Borcherds in 1992 <a class="yt-timestamp" data-t="00:20:33">[00:20:33]</a>. This proof established a deep and unexpected connection between disparate areas of mathematics <a class="yt-timestamp" data-t="00:20:40">[00:20:40]</a>. The "moonshine" also implies a connection between the Monster Group and string theory <a class="yt-timestamp" data-t="00:20:53">[00:20:53]</a>.

The Monster Group serves as a reminder that fundamental objects in the universe are not necessarily simple or clean; they exist by logical necessity, regardless of how easily humans can comprehend them <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>.