---
title: Symmetries and group actions
videoId: mvmuCPvRoWQ
---

From: [[3blue1brown]] <br/> 

[[introduction_to_group_theory | Group theory]] is a field of mathematics that primarily studies the nature of [[group_theory_and_the_idea_of_symmetry | symmetry]] <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. It provides a richer interpretation for concepts like Euler's formula <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Defining Symmetry

A symmetry of an object refers to any action that can be performed on the object that leaves it looking indistinguishable from its original state <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

For example, a square is a symmetric shape <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>:
*   Rotating it 90 degrees counterclockwise leaves it looking the same <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
*   Flipping it around its vertical line also leaves it identical <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

Each such action is called a symmetry of the object, and all of these symmetries collectively form a "group of symmetries," or simply a group <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

## Examples of Groups

### Finite Groups
*   **Symmetries of a Square**: This particular group consists of 8 symmetries <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. These include:
    *   The action of doing nothing <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
    *   Three different rotations <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
    *   Four ways to flip it over <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
*   This specific group is known as the [[the_concept_of_simple_groups_and_permutation_groups | dihedral group]] of order 8, and it is an example of a finite group because it consists of a limited number of actions <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

### Infinite Groups
Many groups contain infinitely many actions.
*   **Rotations of a Circle**: Consider all possible rotations of any angle <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. This can be viewed as a group that acts on a circle, capturing all of its symmetries that do not involve flipping it <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. Every action in this group of rotation lies somewhere on the infinite continuum between 0 and 2π radians <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. Each rotation can be associated with a single point on the circle itself <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

## Group Arithmetic: Composing Actions

The core of [[introduction_to_group_theory | group theory]] lies in understanding how these symmetries interact with each other <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
*   **Composition**: If you apply one symmetric action followed by another, the overall effect is equivalent to a third action within the same group <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. This is often thought of as "adding" or "multiplying" actions <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
    *   **Example (Square)**: Rotating a square 90 degrees and then flipping it around the vertical axis results in the same overall effect as if it had been flipped over a diagonal line <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
    *   **Example (Circle)**: Rotating a circle 270 degrees and then 120 degrees results in the same effect as a 30-degree rotation <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

This collection of underlying relations—the associations between pairs of actions and the single action equivalent to their [[composition of linear transformations | composition]]—is what defines a group <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

## Numbers as Groups

Numbers themselves can be understood as groups in two distinct ways, where composing actions resembles either addition or multiplication <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

### Additive Group of Real Numbers
*   Consider all possible ways to slide a number line left or right along itself <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. This collection of sliding actions is a group, representing the symmetries on an infinite line <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
*   Each action can be associated with a unique real number by observing where the point at zero ends up <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
    *   Sliding right by 3 units is associated with the number 3 <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
    *   Sliding left by 2 units is associated with the number -2 <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
    *   Doing nothing is associated with zero <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
*   **Group Operation**: Applying one sliding action followed by another corresponds to adding the associated numbers <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. For instance, sliding right by 3 units and then by 2 units is equivalent to sliding right by 5 units (3+2) <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. This is why it's called the "additive group of real numbers" <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.

### Additive Group of Complex Numbers
*   This concept can be extended to the complex plane, considering sliding actions across it <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
    *   Numbers like `i`, `2i`, `3i` are associated with vertical sliding motions <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.
    *   A point like `3 + 2i` is associated with an action that slides the plane such that zero moves to `3 + 2i` <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. This diagonal slide is equivalent to sliding right by 3, then vertically by 2i <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
*   **Group Operation**: Composing these sliding actions on the complex plane involves adding their components <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. For example, a slide by `3 + 2i` followed by a slide by `1 - 3i` results in a slide equivalent to `(3+1) + (2-3)i` <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. This group is called the "additive group of complex numbers" <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.

### Multiplicative Group of Positive Real Numbers
*   Consider actions on the number line that stretch or squish it, keeping zero fixed <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
*   Each action is associated with a unique positive real number by observing where the point at one goes <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.
    *   A stretch by a factor of 3 brings 1 to 3 <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
    *   A squish by a factor of 1/2 brings 1 to 1/2 <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.
*   **Group Operation**: Applying one stretching/squishing action followed by another corresponds to multiplying the associated numbers <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. For example, stretching by 3 then by 2 results in a stretch by 6 (3 * 2) <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. This is known as the "multiplicative group of positive real numbers" <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.

### Multiplicative Group of Complex Numbers
*   Extending this idea to the complex plane, fixing zero and dragging the point at one, introduces actions that include not only stretching and squishing but also rotational components <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.
    *   The action associated with `i` (dragging 1 to `i`) is a 90-degree rotation <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.
    *   Applying the `i` action twice (i.e., `i * i`) results in a 180-degree flip, which brings 1 to -1 <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>. This illustrates `i * i = -1` in terms of action composition <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.
*   Every multiplicative action on the complex plane is a combination of a stretch/squish (associated with a point on the positive real number line) and a pure rotation (associated with a point on the unit circle) <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. This is analogous to how additive actions break down into horizontal and vertical slides <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>.

## Exponentiation in Group Theory

Exponentiation, traditionally understood as repeated multiplication, can be reinterpreted through the lens of group theory <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. The fundamental property of exponents, `b^(x+y) = b^x * b^y`, suggests a connection between the additive group (inputs `x` and `y`) and the multiplicative group (outputs `b^x` and `b^y`) <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>.

This property implies that adding inputs (actions from an additive group, like sliding) corresponds to multiplying outputs (actions from a multiplicative group, like stretching/rotating) <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>. Such functions, which preserve the group structure by mapping the arithmetic of one group to another, are called **homomorphisms** <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>.

For the exponential function `e^x`:
*   Purely horizontal slides (real number inputs) are mapped to pure stretching or squishing actions (positive real number outputs) <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a>.
*   Purely vertical slides (imaginary number inputs, multiples of `i`) map into pure rotations (points on the unit circle) <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>. This is an example of [[role_of_circular_symmetry_in_statistical_distributions | circular symmetry]].
*   Specifically, `e^x` maps a vertical slide of `pi` units (corresponding to `pi * i`) to a rotation of exactly `pi` radians, which is a 180-degree rotation associated with the number -1 <a class="yt-timestamp" data-t="00:20:39">[00:20:39]</a>. This is the essence of Euler's formula, `e^(i*pi) = -1` <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

From a group theory perspective, this highlights how exponentials map additive actions perpendicular to the real number line (vertical slides) into multiplicative actions perpendicular to the real number stretching actions (pure rotations) <a class="yt-timestamp" data-t="00:21:45">[00:21:45]</a>.

The transformation of the complex plane by `e^x` can be visualized as first rolling the plane into a cylinder (wrapping vertical lines into circles), then "smooshing" that cylinder onto the plane around zero, where concentric circles correspond to the original vertical lines <a class="yt-timestamp" data-t="00:23:51">[00:23:51]</a>.