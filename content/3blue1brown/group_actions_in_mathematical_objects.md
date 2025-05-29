---
title: Group actions in mathematical objects
videoId: mvmuCPvRoWQ
---

From: [[3blue1brown]] <br/> 

[[introduction_to_group_theory | Group theory]] provides a framework for understanding the nature of [[group_theory_and_symmetries | symmetry]] <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. It offers a richer interpretation of mathematical concepts, such as Euler's formula <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. At its core, [[introduction_to_group_theory | group theory]] studies collections of actions—called symmetries—that can be performed on a mathematical object, leaving it looking indistinguishable <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. All of the symmetries of an object together form a "group of symmetries," or simply a "group" <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

## Symmetries and Group Actions

Groups can consist of a finite number of symmetries or infinitely many <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

### Finite Groups: The Square
A classic example is the symmetries of a square <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. These actions include rotating it 90 degrees counterclockwise or flipping it around a vertical line, both of which leave the square looking identical to its starting state <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. The group of symmetries for a square consists of 8 distinct actions:
*   Doing nothing <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>
*   Three different rotations <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>
*   Four different ways to flip it over <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>

This specific group is known as the dihedral group of order 8 <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

### Infinite Groups: The Circle
An example of an infinite group is the collection of all possible rotations of a circle <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. These rotations capture all the symmetries of the circle that don't involve flipping it <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. Each action in this group can be associated with a single point on the circle itself; for instance, a specific rotation can be uniquely identified by where it moves an arbitrary starting point on the circle <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. This provides a way to label and conceptualize the actions <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

## Group Arithmetic: Composing Actions
The core of [[introduction_to_group_theory | group theory]] lies in understanding how these symmetries "play with each other" <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. Any two actions within a group can be combined by applying one after the other, resulting in a third action that is also part of the group <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. This forms a kind of "arithmetic" for the group <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

*   **Example (Square)**: A 90-degree rotation followed by a vertical flip might have the same overall effect as a single diagonal flip <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
*   **Example (Circle)**: A 270-degree rotation followed by a 120-degree rotation results in an overall 30-degree rotation <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

This collection of underlying relations—how pairs of actions combine to yield a single equivalent action—is what defines a group's structure <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. Much of modern mathematics is rooted in understanding how these collections of actions are organized by this relational composition <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

## Numbers as Group Actions
Groups are incredibly general, and many different ideas, including ordinary numbers, can be framed in terms of symmetries and their composition <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. Numbers can be viewed as groups in two distinct ways: one where combining actions resembles addition, and another where it resembles multiplication <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

### Additive Group of Real Numbers
Consider all the ways to slide a number line left or right along itself <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. Each sliding action can be uniquely associated with a real number by observing where the point originally at zero ends up <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>:
*   Sliding right by 3 units is associated with the number 3 <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
*   Sliding left by 2 units is associated with the number -2 <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
*   Doing nothing is associated with zero <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.

This collection is called the additive group of real numbers <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. The group operation, applying one slide after another, directly corresponds to addition <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>: sliding right by 3 units then by 2 units results in a total slide of 5 units (3+2) <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

### Additive Group of Complex Numbers
This idea extends to the complex plane <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. Vertical slides correspond to imaginary numbers (e.g., 2i is a slide of 2 units vertically) <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. A diagonal slide, like the one associated with 3 + 2i, is equivalent to a horizontal slide of 3 units followed by a vertical slide of 2 units <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. Composing these sliding actions on the complex plane is equivalent to adding complex numbers <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. This is known as the additive group of complex numbers <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.

### Multiplicative Group of Positive Real Numbers
Numbers can also form a different kind of group. Consider actions that stretch or squish a number line, keeping zero fixed <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. Each such action can be associated with a unique positive real number by observing where the point originally at 1 lands <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>:
*   Stretching by a factor of 3 maps 1 to 3 <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
*   Squishing by a factor of 1/2 maps 1 to 1/2 <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.

When these actions are composed, the corresponding numbers are multiplied <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>. For example, a stretch by 3 followed by a stretch by 2 results in an overall stretch by 6 (3 * 2) <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. This is the multiplicative group of positive real numbers <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.

### Multiplicative Group of Complex Numbers
Extending this to the complex plane, fixing 0 and dragging 1 around introduces not only stretching and squishing but also rotational components <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.
*   The action associated with the number *i* (dragging 1 to *i*) is a 90-degree rotation <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.
*   Applying this action twice (*i* times *i*) results in a 180-degree rotation, which is the action associated with -1 <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>. Thus, *i* * *i* = -1 within this group framework <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.

Every multiplicative action on the complex plane is a combination of a stretch/squish (associated with a point on the positive real number line) and a pure rotation (associated with a point on the unit circle) <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. This is analogous to how additive actions can be broken down into horizontal and vertical slides <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>.

## Exponentiation and Group Structures
Viewing numbers through the lens of [[introduction_to_group_theory | group theory]] provides a vivid interpretation of exponential functions <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a>. The fundamental exponential property, $B^{x+y} = B^x \times B^y$, indicates that adding inputs (members of an additive group of sliding actions) corresponds to multiplying outputs (members of a multiplicative group of stretching/rotating actions) <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>.

Exponential functions map purely vertical slides (additive actions perpendicular to the real number line) into pure rotations (multiplicative actions perpendicular to real number stretching actions) <a class="yt-timestamp" data-t="00:21:45">[00:21:45]</a>. The special property of the number *e* is that for $e^x$, a vertical slide of one unit (corresponding to *i*) maps to a rotation of exactly one radian <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>. Therefore, a vertical slide of $\pi$ units (input $\pi i$) corresponds to a rotation of exactly $\pi$ radians, which is the 180-degree rotation associated with the number -1 <a class="yt-timestamp" data-t="00:20:39">[00:20:39]</a>. This group theory perspective helps illuminate Euler's formula, $e^{\pi i} = -1$ <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.