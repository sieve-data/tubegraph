---
title: The concept of simple groups and permutation groups
videoId: mH0oCDa74tE
---

From: [[3blue1brown]] <br/> 

[[Introduction to group theory | Group theory]] is a field of mathematics dedicated to codifying the idea of [[group_theory_and_the_idea_of_symmetry | symmetry]] <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. While seemingly abstract, it describes something fundamental that could be recognized by any intelligent civilization <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## Groups and Symmetries

When discussing symmetry, we refer to actions that leave an object looking the same <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. For instance:
*   A face is symmetric because reflecting it about a line leaves it unchanged <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   A snowflake has more symmetries, such as 60-degree rotations or flips along various axes <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

A collection of all such actions that leave an object looking the same is called a group <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. The "do-nothing" action is always considered part of the group <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. For example, the group of symmetries for a snowflake, including the do-nothing action, contains 12 distinct actions, known as D6 <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. The group of symmetries for a face is C2 <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

The size of a group reflects the "looser sense of structure" that each action preserves <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. For instance, a cube has 24 rotations that preserve its appearance; allowing reflections expands this to 48 actions <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

## Permutation Groups (S_n)

The loosest sense of structure involves considering any way to shuffle a collection of points as a symmetry, unconstrained by underlying properties <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. These are known as permutation groups <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   The number of permutations for six objects is 6!, or 720 <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
*   For 12 points, it grows to approximately 479 million <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
*   For 101 objects, the group size is around 9x10^159 <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

These permutation groups are denoted as S-sub-n <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a> and are fundamental in group theory because, in a certain sense, they "encompass all other groups" <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

### Application: Polynomial Equations

One of the earliest applications of [[introduction_to_group_theory | group theory]] was in understanding solutions to polynomial equations <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. While formulas exist for quadratic, cubic, and quartic equations, mathematicians struggled to find one for degree 5 polynomials <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. It turns out that thinking about the group that permutes the roots of such a polynomial reveals that no quintic formula can exist using only arithmetic operations and radicals <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. This impossibility is tied to the inner structure of the permutation group S5 <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

## Groups as Abstractions

Mathematicians differentiate between [[symmetries_and_group_actions | group actions]] and abstract groups <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. Just as the number 3 is an abstract concept beyond a specific triplet of things, group elements are thought of as entities in themselves, defined by how they combine with each other <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
This combination is often thought of as applying one action after another, defining a kind of "multiplication" that gives a group its structure <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. A multiplication table can capture this inner structure abstractly <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

### Isomorphism

A key idea in [[introduction_to_group_theory | group theory]] is **isomorphism** <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>. Two groups are considered "the same" if their multiplication tables are identical, meaning there's a one-to-one mapping between their elements that preserves [[composition_of_linear_transformations | composition]] <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. For example, the symmetries of a cube are isomorphic to the permutation group of four objects (S4), specifically by observing how cube rotations permute its four diagonals <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.

This abstraction allows mathematicians to ask: "What are all the groups up to isomorphism?" <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>, which is a way of asking "what are all the ways that something can be symmetric?" <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.

## Simple Groups: The "Atoms" of Symmetry

To simplify the vast landscape of groups, mathematicians focus on **finite groups** (groups with a finite number of elements) <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>. Finite groups can be broken down into a "composition of smaller groups," analogous to how numbers have prime factorizations or molecules are made of atoms <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>. The groups that cannot be broken down any further are known as **simple groups** <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.

Understanding the nature of these simple groups is crucial, as seen in the proof for the impossibility of the quintic formula. It involves showing that if a formula existed, S5 would decompose into specific "cyclic groups of prime order," but its actual decomposition involves a different kind of simple group <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>.

The task of categorizing all finite groups involves two steps:
1.  Finding all the simple groups (analogous to finding the periodic table) <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.
2.  Finding all the ways to combine them (analogous to chemistry) <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>.

### The Classification of Finite Simple Groups

[[The_classification_of_finite_simple_groups | The classification of finite simple groups]] was a monumental achievement in mathematics, taking decades of work by hundreds of brilliant minds and culminating in 2004 with definitive proof <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>.

The answer, however, was "absurd" <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>:
*   There are 18 distinct **infinite families** of simple groups <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>. Examples include cyclic groups of prime order and permutation groups (like S_n for n>=5) with a slight constraint <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>.
*   There are also 26 **[[the_sporadic_groups_and_the_monster_group | sporadic groups]]** that do not fit into these families <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>.

The largest of these sporadic groups is known as the [[the_sporadic_groups_and_the_monster_group | Monster Group]], with a size of approximately 8x10^53 <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>. Its "second largest" counterpart is the Baby Monster Group <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>. A total of 20 sporadic groups, including the Monster and Baby Monster, are part of what Robert Gries called the "happy family," while the other six are "pariahs" <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.

The existence and nature of these sporadic groups, particularly the Monster, remain mysterious <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>. The Monster group "acts on" objects in a space of 196,883 dimensions, and a single element description can take about 4 GB of data <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>. This complexity is in stark contrast to much larger groups like the permutation group on 101 elements, whose elements can be described with very little data <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>.

In the 1970s, John McKay noted a numerical coincidence between the dimensions of the Monster and a number appearing in the series expansion of a modular form, leading to the "monstrous moonshine conjecture" <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>. This conjecture, proved by Richard Borcherds in 1992 (earning him a Fields Medal), solidified an unexpected connection between seemingly disparate areas of mathematics <a class="yt-timestamp" data-t="00:20:40">[00:20:40]</a>. This "moonshine" is also related to string theory <a class="yt-timestamp" data-t="00:20:53">[00:20:53]</a>, reinforcing that fundamental objects are not always simple or clean <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>.