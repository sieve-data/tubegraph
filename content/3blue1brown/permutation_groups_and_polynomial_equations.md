---
title: Permutation groups and polynomial equations
videoId: mH0oCDa74tE
---

From: [[3blue1brown]] <br/> 

[[Introduction to group theory | Group theory]] is a field focused on codifying the idea of symmetry <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. While seemingly abstract, it has surprising applications, including insights into the solvability of polynomial equations <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

## Understanding Groups and Symmetry

When something is described as symmetric, it means certain actions can be taken that leave it looking the same <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. For example, a face is symmetric because it can be reflected about a line and remain unchanged <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. A snowflake exhibits more symmetries, allowing rotations (e.g., 60 or 120 degrees) and flips along various axes without altering its appearance <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. A collection of all such actions, including the action of doing nothing, is called a group <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a> <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

Mathematicians consider groups fundamental, leading them to co-opt a generic word for this specific type of collection <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. The group of symmetries for a snowflake, including the do-nothing action, comprises 12 distinct actions and is known as D6 <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a> <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. Similarly, the group of symmetries for a face with only two elements (reflection and do-nothing) is called C2 <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

### Permutation Groups

When describing symmetries, there's always an implicit structure that is preserved <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. For instance, 24 rotations can be applied to a cube while leaving it looking the same, forming a group <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. If reflections are allowed, the group expands to 48 actions <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

The "loosest" sense of structure preservation involves a collection of points where any way of shuffling them (any permutation) is considered a symmetry <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. These are called permutation groups <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. For example, there are 6! (720) possible permutations of six objects <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. If these six points were the corners of a hexagon, constrained to preserve distances, they would only yield the 12 snowflake symmetries <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

The number of permutations grows rapidly; 12 points yield approximately 479 million permutations <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>, and 101 objects result in about 9x10^159 different actions <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. These permutation groups are denoted as S-sub-n (S_n), where 'n' is the number of objects being permuted <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>, and they play a crucial role in [[Introduction to group theory | group theory]] <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

### Abstract Definition of Groups

While initially described as "group actions," mathematicians often define groups more abstractly <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a> <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. Just as the number 3 is an abstract concept rather than a specific triplet of things, group elements are thought of as abstract entities <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. The structure of a group is defined by how its elements combine, which is analogous to a multiplication operation <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. Combining actions means applying one after the other <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. This "multiplication table" captures the inner structure of the group, abstracting it from any specific object it might act on <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

Formally, a group is a set with a binary operation (multiplication) that satisfies four axioms <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>. These axioms naturally arise from the properties of composing symmetric actions <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.

### Isomorphism

Two groups are considered "the same" if their multiplication tables look identical, meaning anything true for one group is true for the other <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a> <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>. For instance, the symmetries of a cube and the permutation group of four objects are fundamentally the same group <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. This equivalence is called an "isomorphism," a core concept in [[Introduction to group theory | group theory]] <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a> <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>. An isomorphism is a one-to-one mapping between elements of two groups that preserves their composition (multiplication) <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a> <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.

## Application to Polynomial Equations

One of the earliest and most significant applications of [[Group theory and symmetries | group theory]] emerged when mathematicians realized that the structure of permutation groups could shed light on the solutions of polynomial equations <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a> <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

### The Search for Formulas

A well-known formula exists to find the two roots of a quadratic equation (degree 2) <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. There is also a cubic formula (degree 3), which involves nesting cube roots with square roots <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>, and even a quartic formula (degree 4), though it is significantly more complex <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. For a long time, mathematicians struggled to find a similar formula for degree 5 polynomials <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

### The Impossibility of the Quintic Formula

It turns out that by considering the group that permutes the roots of a polynomial, [[Group theory and symmetries | group theory]] reveals that no general quintic formula can exist using only basic arithmetic operations and radicals (square roots, cube roots, etc.) <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a> <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a> <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>. This impossibility is directly linked to the inner structure of the permutation group S5 <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a> <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

### Simple Groups and Solvability

The proof that no quintic formula exists involves showing that if such a formula existed, the permutation group on 5 elements (S5) would decompose into a specific kind of "simple group" called cyclic groups of prime order <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a> <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a> <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>. However, the actual decomposition of S5 involves a different type of simple group (an "atom" that cannot be broken down further), one that solutions built from radicals would never allow <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a> <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.

> "If you're wondering what that proof actually looks like, it involves showing that if there were some kind of mythical quintic formula... it would imply that the permutation group on 5 elements decomposes into a special kind of simple group, known fancifully as the cyclic groups of prime order. But the actual way that this breaks down involves a different kind of simple group, a different kind of atom, one which polynomial solutions built from radicals would never allow." <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a> <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a> <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a> <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a> <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>

Incidentally, one of the 18 distinct infinite families of simple groups is very similar to the permutation groups, with a small constraint on how they shuffle 'n' items <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a> <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>. If these groups act on 5 or more elements, they are simple, which is heavily related to why polynomials of degree 5 or more have solutions that cannot be expressed using radicals <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a> <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>.

## Broader Significance of Groups

This application to [[Newtons fractal and roots of polynomial equations | polynomial equations]] is just one example of how [[Group theory and symmetries | group theory]] reveals non-obvious facts about other mathematical objects <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a> <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>. In physics, Noether's theorem states that every conservation law (like conservation of momentum or energy) corresponds to some kind of symmetry or group <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a> <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a> <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. This highlights that groups are fundamental and universal, representing a universal concept of symmetry <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. The occurrence of the same group in seemingly unrelated situations can reveal unexpected connections between distinct mathematical objects, a common theme in modern mathematics <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.