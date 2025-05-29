---
title: Eulers formula and its significance
videoId: mvmuCPvRoWQ
---

From: [[3blue1brown]] <br/> 

[[eulers_formula_and_unit_circle|Euler's formula]], expressed as `e^(pi * i) = -1`, is a foundational concept in mathematics <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This formula can be given a richer interpretation by viewing it through the lens of group theory <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>, which studies the nature of symmetry <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## Introduction to Group Theory

Group theory centers on understanding collections of symmetric actions, or "symmetries," on a mathematical object <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. Each action leaves the object indistinguishable from its starting state <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. All symmetries of an object together form a "group" <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

For example:
*   **Symmetries of a Square**: This is a finite group consisting of 8 symmetries, including doing nothing, three rotations (90, 180, 270 degrees), and four flips <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. This specific group is called the dihedral group of order 8 <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   **Symmetries of a Circle**: This group consists of infinitely many rotations, capturing all symmetries that don't involve flipping <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. Each rotation can be associated with a unique point on the circle <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

The core of group theory lies in how these symmetries "play with each other" <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. When two actions are applied sequentially, their overall effect is equivalent to another single action within the group <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. This composition defines an "arithmetic" within the group <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

## Numbers as Groups

Numbers themselves can be understood as groups, illustrating two distinct forms of group arithmetic:

### Additive Group of Numbers

*   **Real Numbers**: This group consists of all possible "sliding" actions on a number line (moving it left or right) <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. Each slide can be associated with a unique real number by tracking where the point at zero ends up <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>. For instance, sliding right by 3 units is associated with the number 3 <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. The number zero is associated with the "doing nothing" action <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>. Composing these sliding actions corresponds to ordinary addition of numbers <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. This is known as the "additive group of real numbers" <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.
*   **Complex Numbers**: Extending this to the complex plane, vertical sliding motions are associated with imaginary numbers like `i`, `2i`, etc. <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. A number like `3 + 2i` is associated with a diagonal slide that moves zero to that point <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. Composing these slides on the complex plane aligns with complex number addition, where components are added together <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. This is the "additive group of complex numbers" <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.

### Multiplicative Group of Numbers

*   **Positive Real Numbers**: This group involves "stretching or squishing" actions on the number line, keeping zero fixed <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. Each action is uniquely associated with a positive real number by tracking where the point at 1 goes <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. For example, stretching by a factor of 3 brings the point at 1 to 3 <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. Composing these actions corresponds to ordinary multiplication of numbers <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. This is the "multiplicative group of positive real numbers" <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.
*   **Non-Zero Complex Numbers**: On the complex plane, with zero fixed, dragging the point at 1 to various locations shows that this group includes not only stretching/squishing but also rotational components <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>. For example, dragging 1 to `i` requires a 90-degree rotation <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>. Applying this `i` action twice (i.e., `i * i`) results in a 180-degree flip, which maps 1 to -1 <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>. Every multiplicative action is a combination of a stretch/squish (associated with positive real numbers) and a pure rotation (associated with points on the unit circle) <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.

## Exponentiation and Homomorphisms

Traditionally, exponentiation (e.g., `2^3`) is understood as repeated multiplication <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. However, this definition doesn't apply to fractional or negative exponents, let alone complex ones <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>. The definition is extended to ensure the "exponential property" holds: `b^(x + y) = b^x * b^y` <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>.

From a group theory perspective, this property is profound:
*   **Inputs (exponents)** are members of the additive group of sliding actions <a class="yt-timestamp" data-t="00:16:58">[00:16:58]</a>.
*   **Outputs (results of exponentiation)** are members of the multiplicative group of stretching and squishing actions <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>.

This means that adding inputs (composing sliding actions) corresponds to multiplying outputs (composing stretching/rotating actions) <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>. Functions that preserve this "group structure" (arithmetic) are called **homomorphisms** <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.

## [[eulers_formula_and_unit_circle|Euler's Formula]] through Group Theory

When applying an exponential function like `b^x` to complex numbers:
*   A purely horizontal slide (real number input) maps to a pure stretching or squishing action (positive real number output) <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a>.
*   It is intuitive that purely vertical slides (imaginary number inputs) would map to pure rotations (outputs on the unit circle) <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>.

For any base `b`, the input `i` (a vertical slide of one unit) maps to a rotation of a specific number of radians <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>. For example, `2^i` maps to about 0.693 radians of rotation, and `5^i` maps to about 1.609 radians <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.

## The Significance of [[importance_of_eulers_number_e_in_calculus|Euler's Number e]]

What makes the number [[importance_of_eulers_number_e_in_calculus|e]] special is that when the exponential function `e^x` maps vertical slides to rotations, a vertical slide of exactly one unit (corresponding to `i`) maps to a rotation of exactly one radian <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>.

This direct proportionality means:
*   A two-unit vertical slide maps to a two-radian rotation <a class="yt-timestamp" data-t="00:20:27">[00:20:27]</a>.
*   A three-unit vertical slide maps to a three-radian rotation <a class="yt-timestamp" data-t="00:20:35">[00:20:35]</a>.
*   Crucially, a vertical slide of `pi` units (corresponding to `pi * i`) maps to a rotation of exactly `pi` radians <a class="yt-timestamp" data-t="00:20:39">[00:20:39]</a>. A `pi`-radian rotation is equivalent to a 180-degree rotation, which is the multiplicative action associated with the number -1 <a class="yt-timestamp" data-t="00:20:46">[00:20:46]</a>.

Thus, `e^(pi * i) = -1` <a class="yt-timestamp" data-t="00:20:51">[00:20:51]</a>.

The fundamental reason for [[importance_of_eulers_number_e_in_calculus|e]]'s uniqueness in this context lies in calculus: `e^x` is the only exponential function that is equal to its own derivative <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>.

This group theory perspective provides a vivid interpretation of [[eulers_formula_and_unit_circle|Euler's formula]]: it demonstrates how `e^x` maps purely vertical additive slides (perpendicular to the real number line) into pure rotations (perpendicular to real number stretching actions), with `e` being the unique base where a vertical slide of `pi` units results in a rotation of exactly `pi` radians, equating to -1 <a class="yt-timestamp" data-t="00:21:45">[00:21:45]</a>.

## Visualizing e^x as a Transformation

One way to visualize the transformation of the complex plane by `e^x` is to imagine:
1.  Rolling the complex plane into a cylinder, such that all vertical lines become circles <a class="yt-timestamp" data-t="00:23:51">[00:23:51]</a>.
2.  Then, "smooshing" that cylinder onto the plane around zero, where each of the exponentially spaced concentric circles corresponds to what were originally vertical lines <a class="yt-timestamp" data-t="00:23:57">[00:23:57]</a>.