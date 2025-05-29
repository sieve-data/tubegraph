---
title: Introduction to group theory
videoId: mvmuCPvRoWQ
---

From: [[3blue1brown]] <br/> 

[[group_theory_and_the_idea_of_symmetry | Group theory]] is a field in mathematics dedicated to studying the nature of [[symmetries and group actions | symmetry]] <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. It provides a richer interpretation of mathematical concepts, such as Euler's formula <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. The study focuses on how collections of symmetric actions are organized by their relations <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

## Defining a Group

A group is a collection of symmetric actions on some mathematical object <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>. The "[[symmetries and group actions | symmetry]]" of an object can be understood by identifying all actions that leave it looking indistinguishable from its original state <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Examples of Groups

*   **Symmetries of a Square**: Actions like rotating 90 degrees counterclockwise or flipping along a vertical line are considered [[symmetries and group actions | symmetries]] of the square <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. All eight [[symmetries and group actions | symmetries]] of a square (including doing nothing, three rotations, and four flips) form a group called the dihedral group of order 8 <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. This is an example of a finite group <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
*   **Symmetries of a Circle**: The collection of all possible rotations of any angle on a circle forms a group <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. This group consists of infinitely many actions <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>, where each rotation can be associated with a point on the circle <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

### Group Arithmetic (Composition)

The core of [[group_theory_and_the_idea_of_symmetry | group theory]] is understanding how [[symmetries and group actions | symmetries]] interact <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. By applying one action after another, a "kind of arithmetic" emerges within any group <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. This allows two actions to be "added together" (or multiplied) to result in a third action <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. This collection of underlying relations—how pairs of actions combine to an equivalent single action—is what defines a group <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

## Numbers as Groups

Ordinary numbers can be framed as groups in two distinct ways: where composition looks like addition, and where it looks like multiplication <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. This perspective views numbers as actions rather than just counting entities <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.

### The Additive Group of Real Numbers

This group consists of all possible "sliding" actions (left or right) on a number line <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. Each sliding action can be associated with a unique real number, determined by where the point at zero ends up <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. For example, sliding right by 3 units is associated with the number 3 <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>, and sliding left by 2 units with -2 <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. The number zero is associated with the action of doing nothing <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.

The group operation in this context is addition: sliding right by 3 units and then by 2 units results in the same effect as sliding right by 5 units (3 + 2) <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. This redefines what numbers are—examples within a larger category of groups—and addition as one example of group arithmetic <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

### The Additive Group of [[introduction_to_complex_numbers | Complex Numbers]]

This extends the concept of sliding actions to the [[introduction_to_complex_numbers | complex plane]] <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
*   Numbers like `i`, `2i`, `3i` on the vertical line are associated with vertical sliding motions <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.
*   A number like `3 + 2i` is associated with a diagonal slide that moves zero to that point <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. This diagonal slide can be broken down into a horizontal slide of 3 units and a vertical slide of 2 units <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.

Composing two sliding actions in the [[introduction_to_complex_numbers | complex plane]] means adding their respective horizontal and vertical components <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. This "composing" of sliding actions is equivalent to the addition of [[introduction_to_complex_numbers | complex numbers]] <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.

### The Multiplicative Group of Positive Real Numbers

This group involves actions of "stretching or squishing" a number line while keeping zero fixed <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. Each action is associated with a unique positive number by tracking where the point at '1' goes <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.
*   Stretching by a factor of 3 brings '1' to '3' <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
*   Squishing by a factor of 1/2 brings '1' to '1/2' <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.

Composing these actions means multiplying the associated numbers <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>. For example, a stretch by 3 followed by a stretch by 2 is equivalent to a stretch by 6 (3 * 2) <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. This shows how ordinary multiplication is an example of group arithmetic <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.

### The Multiplicative Group of [[introduction_to_complex_numbers | Complex Numbers]]

Extending stretching/squishing actions to the [[introduction_to_complex_numbers | complex plane]] introduces rotational components <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.
*   Dragging the point '1' to 'i' corresponds to a 90-degree rotation <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.
*   Applying this action twice (i * i) results in a 180-degree flip, associated with -1 <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.

In general, every multiplicative action on the [[introduction_to_complex_numbers | complex plane]] is a combination of a stretch/squish (associated with positive real numbers) and a pure rotation (associated with points on the unit circle) <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.

## Connection to [[exponentiation_in_group_theory | Exponentiation]]

From a [[group_theory_and_the_idea_of_symmetry | group theory]] perspective, the exponential property (e.g., `2^(x+y) = 2^x * 2^y`) suggests a function mapping inputs from the additive group (sliding actions) to outputs in the multiplicative group (stretching/rotating actions) <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>. Such a function "preserves the group structure" because composing input actions corresponds to composing output actions <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>. Functions that preserve this arithmetic between groups are called homomorphisms <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.

Specifically, the exponential function `e^x` maps purely vertical slides (additive actions on the imaginary axis) into pure rotations (multiplicative actions on the unit circle) <a class="yt-timestamp" data-t="00:18:49">[00:18:49]</a>. A vertical slide of `i` (one unit) maps to a rotation of exactly one radian <a class="yt-timestamp" data-t="00:20:15">[00:20:15]</a>. This means a vertical slide of `pi` units (input `pi*i`) maps to a rotation of `pi` radians (180 degrees), which is the multiplicative action associated with the number -1 <a class="yt-timestamp" data-t="00:20:39">[00:20:39]</a>.

### Visualization of `e^x` as a Transformation

The function `e^x` can be visualized as a transformation of the [[introduction_to_complex_numbers | complex plane]] <a class="yt-timestamp" data-t="00:22:18">[00:22:18]</a>. Imagine rolling the [[introduction_to_complex_numbers | complex plane]] into a cylinder, where vertical lines become circles <a class="yt-timestamp" data-t="00:23:51">[00:23:51]</a>. Then, this cylinder is "smooshed" onto the plane around zero, with concentric circles (exponentially spaced) corresponding to the original vertical lines <a class="yt-timestamp" data-t="00:23:57">[00:23:57]</a>.

---
### Summary of Group Theory Concepts

*   **Group**: A collection of symmetric actions on a mathematical object <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>.
*   **Group Arithmetic**: The method of combining two actions by applying one after the other to get an equivalent third action <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.
*   **Numbers as Groups**: Real and [[introduction_to_complex_numbers | complex numbers]] can be understood as groups under either addition (sliding actions) or multiplication (stretching/squishing/rotating actions) <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.
*   **Homomorphisms**: Functions between groups that preserve their underlying arithmetic structure <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>. [[exponentiation_in_group_theory | Exponentiation]] is a key example in relating additive and multiplicative groups of numbers <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.