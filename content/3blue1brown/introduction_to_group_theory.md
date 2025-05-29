---
title: Introduction to group theory
videoId: mvmuCPvRoWQ
---

From: [[3blue1brown]] <br/> 

[[group_theory_and_symmetries | Group theory]] is a field of mathematics primarily concerned with studying the nature of symmetry <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>. It provides a richer interpretation of fundamental mathematical concepts, such as Euler's formula <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. This article provides an [[introduction_to_topology | introduction to the basics of group theory]] and how it frames our understanding of numbers and algebra <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>, <a class="yt-timestamp" data-t="01:24:00">[01:24:00]</a>.

## What is a Group?

A group is a collection of symmetric actions on some mathematical object <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>, such as a square, a circle, or a number line <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>.

### Symmetries of a Square

Consider a square, which is a highly symmetric shape <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>. Its symmetries are all the actions that leave it looking indistinguishable from its original state <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>. Examples include rotating it 90 degrees counterclockwise or flipping it around a vertical line <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>, <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>. Each of these actions is called a "symmetry of the square" <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>. All of these symmetries together form a [[group_actions_in_mathematical_objects | group of symmetries]] <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>.

For a square, this group consists of 8 symmetries:
*   The action of doing nothing <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>.
*   Three different rotations <a class="yt-timestamp" data-t="02:34:00">[02:34:00]</a>.
*   Four ways to flip it over <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>.

This specific group is known as the [[symmetries_and_dihedral_groups | dihedral group]] of order 8 <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>. It is an example of a [[infinite_and_finite_simple_groups | finite group]], as it consists of a limited number of actions <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>.

### Symmetries of a Circle

Unlike the square, many groups, such as the symmetries of a circle, consist of [[infinite_and_finite_simple_groups | infinitely many actions]] <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>, <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>. All possible rotations of a circle, at any angle, form a group that captures its symmetries without involving flips <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>, <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>. Each rotation can be associated with a unique point on the circle itself, determined by where a chosen arbitrary point lands after the action <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>, <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>.

## Group Arithmetic (Composition of Actions)

The core of [[group_theory_and_symmetries | group theory]] lies in understanding how symmetries interact with each other <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>. Any two actions within a group can be combined by applying one after the other, resulting in a third action that is also part of the group <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>. This concept defines a kind of "arithmetic" within the group <a class="yt-timestamp" data-t="05:05:00">[05:05:00]</a>.

*   **Square Example:** Rotating a square 90 degrees and then flipping it vertically has the same overall effect as a single flip over a diagonal line <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>, <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>.
*   **Circle Example:** Rotating a circle 270 degrees and then an additional 120 degrees results in the same effect as a single 30-degree rotation <a class="yt-timestamp" data-t="04:35:00">[04:35:00]</a>, <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>.

This collection of underlying relations—how pairs of actions combine to form an equivalent single action—is what defines a group <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>, <a class="yt-timestamp" data-t="05:35:00">[05:35:00]</a>.

## Numbers as Groups

Ordinary numbers can also be understood as groups, offering two distinct perspectives: one where combining actions resembles addition, and another where it resembles multiplication <a class="yt-timestamp" data-t="06:00:00">[06:00:00]</a>, <a class="yt-timestamp" data-t="06:09:00">[06:09:00]</a>.

### The Additive Group of Real Numbers

This group consists of all possible "sliding" actions of a number line along itself <a class="yt-timestamp" data-t="06:24:00">[06:24:00]</a>. Each sliding action can be associated with a unique real number by observing where the point at zero ends up <a class="yt-timestamp" data-t="06:38:00">[06:38:00]</a>, <a class="yt-timestamp" data-t="06:52:00">[06:52:00]</a>. For example, sliding right by 3 units is associated with the number 3, and sliding left by 2 units with -2 <a class="yt-timestamp" data-t="06:56:00">[06:56:00]</a>, <a class="yt-timestamp" data-t="07:03:00">[07:03:00]</a>. The number zero is associated with the "do nothing" action <a class="yt-timestamp" data-t="07:15:00">[07:15:00]</a>.

The group operation (applying one slide after another) directly corresponds to addition <a class="yt-timestamp" data-t="07:30:00">[07:30:00]</a>. Sliding right by 3 units and then by 2 units results in a total slide of 5 units (3 + 2) <a class="yt-timestamp" data-t="07:37:00">[07:37:00]</a>. This provides an alternative view of numbers as [[group_actions_in_mathematical_objects | groups of symmetries]], and addition as a form of group arithmetic <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>, <a class="yt-timestamp" data-t="08:04:00">[08:04:00]</a>.

### The Additive Group of Complex Numbers

This concept extends to the complex plane, where sliding actions can occur horizontally or vertically <a class="yt-timestamp" data-t="08:11:00">[08:11:00]</a>, <a class="yt-timestamp" data-t="08:14:00">[08:14:00]</a>. Numbers like `i`, `2i`, `3i` are associated with vertical sliding motions, while `3 + 2i` is associated with a diagonal slide <a class="yt-timestamp" data-t="08:19:00">[08:19:00]</a>, <a class="yt-timestamp" data-t="08:37:00">[08:37:00]</a>. Composing these sliding actions is analogous to adding complex numbers by adding their respective components <a class="yt-timestamp" data-t="09:04:00">[09:04:00]</a>, <a class="yt-timestamp" data-t="09:35:00">[09:35:00]</a>. This collection is known as the "additive group of complex numbers" <a class="yt-timestamp" data-t="09:43:00">[09:43:00]</a>.

### The Multiplicative Group of Positive Real Numbers

This group involves actions that stretch or squish the number line, keeping zero fixed <a class="yt-timestamp" data-t="10:11:00">[10:11:00]</a>, <a class="yt-timestamp" data-t="10:14:00">[10:14:00]</a>. Each action is uniquely associated with a positive number by tracking where the point at 1 lands <a class="yt-timestamp" data-t="10:21:00">[10:21:00]</a>, <a class="yt-timestamp" data-t="10:32:00">[10:32:00]</a>. For example, stretching by a factor of 3 is associated with the number 3, and squishing by a factor of 1/2 with 1/2 <a class="yt-timestamp" data-t="10:36:00">[10:36:00]</a>, <a class="yt-timestamp" data-t="10:45:00">[10:45:00]</a>.

Composing these stretching/squishing actions corresponds to multiplication <a class="yt-timestamp" data-t="11:17:00">[11:17:00]</a>. A stretch by 3 followed by a stretch by 2 results in a total stretch by 6 (3 x 2) <a class="yt-timestamp" data-t="11:21:00">[11:21:00]</a>, <a class="yt-timestamp" data-t="11:27:00">[11:27:00]</a>. This group is called the "multiplicative group of positive real numbers" <a class="yt-timestamp" data-t="11:45:00">[11:45:00]</a>.

### The Multiplicative Group of Complex Numbers

Extending this to the complex plane, fixing zero and dragging the point at 1 can involve not only stretching/squishing but also rotational components <a class="yt-timestamp" data-t="12:02:00">[12:02:00]</a>, <a class="yt-timestamp" data-t="12:05:00">[12:05:00]</a>, <a class="yt-timestamp" data-t="12:16:00">[12:16:00]</a>. For instance, dragging 1 to `i` (one unit above zero) requires a 90-degree rotation <a class="yt-timestamp" data-t="12:30:00">[12:30:00]</a>, <a class="yt-timestamp" data-t="12:37:00">[12:37:00]</a>. Applying this `i`-associated action twice in a row (a 90-degree rotation twice) results in a 180-degree flip, which maps 1 to -1. This illustrates how `i` times `i` equals -1 in this group context <a class="yt-timestamp" data-t="12:50:00">[12:50:00]</a>, <a class="yt-timestamp" data-t="13:04:00">[13:04:00]</a>.

Generally, every multiplicative action in the complex plane combines a stretch/squish (associated with a point on the positive real number line) and a pure rotation (associated with a point on the unit circle) <a class="yt-timestamp" data-t="13:37:00">[13:37:00]</a>, <a class="yt-timestamp" data-t="13:41:00">[13:41:00]</a>.

## Groups and Exponentiation

The understanding of numbers as groups provides a vivid interpretation of [[exponential_functions_and_group_theory | exponential functions]] <a class="yt-timestamp" data-t="15:22:00">[15:22:00]</a>, <a class="yt-timestamp" data-t="15:26:00">[15:26:00]</a>. The fundamental property of exponents, where `2^(x+y) = 2^x * 2^y` <a class="yt-timestamp" data-t="15:42:00">[15:42:00]</a>, can be reinterpreted in terms of group theory <a class="yt-timestamp" data-t="16:47:00">[16:47:00]</a>. This property suggests that adding inputs (members of an additive group of sliding actions) corresponds to multiplying outputs (members of a multiplicative group of stretching/squishing actions) <a class="yt-timestamp" data-t="16:54:00">[16:54:00]</a>, <a class="yt-timestamp" data-t="17:02:00">[17:02:00]</a>.

Functions that preserve the group structure in this way are called **homomorphisms** <a class="yt-timestamp" data-t="17:53:00">[17:53:00]</a>, <a class="yt-timestamp" data-t="18:11:00">[18:11:00]</a>. The exponential function `e^x` is a key example of such a function mapping from the additive group of complex numbers to the multiplicative group of complex numbers <a class="yt-timestamp" data-t="18:23:00">[18:23:00]</a>.

Specifically, `e^x` maps:
*   Purely horizontal slides (real numbers in the additive group) to pure stretching or squishing actions (positive real numbers in the multiplicative group) <a class="yt-timestamp" data-t="18:40:00">[18:40:00]</a>.
*   Purely vertical slides (imaginary numbers like `i` in the additive group) to pure rotations (points on the unit circle in the multiplicative group) <a class="yt-timestamp" data-t="18:56:00">[18:56:00]</a>, <a class="yt-timestamp" data-t="19:03:00">[19:03:00]</a>.

The special property of the number `e` is that when `e^x` maps vertical slides to rotations, a vertical slide of one unit (corresponding to `i`) maps to a rotation of exactly one radian <a class="yt-timestamp" data-t="20:08:00">[20:08:00]</a>, <a class="yt-timestamp" data-t="20:15:00">[20:15:00]</a>. Consequently, a vertical slide of `pi` units (corresponding to `pi*i`) maps to a rotation of exactly `pi` radians, which is a 180-degree rotation associated with the number negative one <a class="yt-timestamp" data-t="20:39:00">[20:39:00]</a>, <a class="yt-timestamp" data-t="20:46:00">[20:46:00]</a>. This group theoretic lens gives a vivid interpretation of Euler's formula, `e^(pi*i) = -1` <a class="yt-timestamp" data-t="21:31:00">[21:31:00]</a>.