---
title: Eulers formula
videoId: mvmuCPvRoWQ
---

From: [[3blue1brown]] <br/> 

Two years after its initial exploration, the idea of [[eulers_formula_and_mathematical_proofs | Euler's formula]], `e` to the pi `i` equals negative one, is revisited to offer a richer interpretation through the lens of [[exponentiation_in_group_theory | group theory]] <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. While a quick explanation of [[eulers_formula_and_mathematical_proofs | Euler's formula]] exists for those comfortable with vector calculus <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>, the group theory approach aims to change how numbers and algebra are perceived <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

## Introduction to Group Theory

[[exponentiation_in_group_theory | Group theory]] is fundamentally about studying the nature of symmetry <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. A "symmetry" refers to an action taken on an object that leaves it looking indistinguishable from its original state <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Symmetries of a Square
A square is a highly symmetric shape <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. Examples of symmetries include:
*   Rotating it 90 degrees counterclockwise <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
*   Flipping it around its vertical line <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

Each of these actions is a symmetry, and all symmetries together form a "group of symmetries," or simply a "group" <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. The group of symmetries for a square consists of 8 symmetries: doing nothing, three different rotations, and four ways to flip it <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. This specific group is known as the *dihedral group of order 8* <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. This is an example of a finite group <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

### Symmetries of a Circle
Unlike the square, a circle has infinitely many symmetries, such as all possible rotations of any angle <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. This group acts on a circle and captures symmetries that don't involve flipping <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. Each action in this group can be associated with a unique point on the circle itself by tracking where a chosen arbitrary point ends up after the rotation <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

### Arithmetic within Groups
The core of [[exponentiation_in_group_theory | group theory]] lies in understanding how symmetries interact when composed <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
*   **Square example:** Rotating a square 90 degrees and then flipping it vertically has the same overall effect as flipping it over a specific diagonal line <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
*   **Circle example:** Rotating a circle 270 degrees and then 120 degrees results in the same effect as a single 30-degree rotation <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

In any group, there is an "arithmetic" where two actions can be combined by applying one after the other to yield a third action within the group <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. This collection of underlying relations between pairs of actions and their composition defines a group <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

## Numbers as Groups

Numbers themselves can be understood in two ways through the lens of [[exponentiation_in_group_theory | group theory]]: one involving addition, and another involving multiplication <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

### Additive Group of Real Numbers
Consider the actions of sliding a number line left or right <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. This collection of sliding actions forms a group <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. Each sliding action can be uniquely associated with a real number by observing where the point at zero ends up <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. For instance, sliding right by 3 units is associated with the number 3 <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. Sliding by zero (doing nothing) is associated with the number zero <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.

This group is called the "additive group of real numbers" because the group operation (applying one slide after another) corresponds to ordinary addition <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. For example, sliding right by 3 and then by 2 results in a slide of 3 plus 2, or 5 units <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

### Additive Group of Complex Numbers
This idea extends to the complex plane. Sliding actions on the complex plane can be associated with complex numbers <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. Vertical slides correspond to imaginary numbers like `i`, `2i`, etc. <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. A diagonal slide, such as one associated with `3 + 2i`, is the same as first sliding right by 3 units and then vertically by 2 units <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. Composing these sliding actions on the complex plane corresponds to adding complex numbers by adding their components <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. This collection is known as the "additive group of complex numbers" <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.

### Multiplicative Group of Positive Real Numbers
Another type of group action on the number line involves stretching or squishing it while keeping zero fixed <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. Each stretching action can be associated with a unique positive real number by observing where the point at 1 goes <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>. For example, stretching by a factor of 3 maps 1 to 3 <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>, and squishing by a factor of 1/2 maps 1 to 1/2 <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.

When composing these actions, applying a stretch by 3 and then a stretch by 2 results in a stretch by 6 (the product of 3 and 2) <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>. This group is called the "multiplicative group of positive real numbers" <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.

### Multiplicative Group of Complex Numbers
Extending this to the complex plane, fixing zero and dragging the point at 1 allows for not only stretching/squishing but also rotational components <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>. The action associated with `i` (dragging 1 to `i`) is a 90-degree rotation <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>. Applying this action twice (i.e., `i * i`) results in a 180-degree flip, which maps 1 to -1 <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>. Therefore, `i * i = -1` can be understood as composing these multiplicative actions <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.

Generally, any multiplicative action on the complex plane is a combination of a stretch/squish (associated with a point on the positive real line) and a pure rotation (associated with a point on the unit circle) <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.

## Exponentiation and Homomorphisms

Traditionally, [[exponentiation_in_group_theory | exponentiation]] (e.g., `2^3`) is understood as repeated multiplication <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. This definition becomes problematic for fractional or negative exponents (e.g., `2^(1/2)`, `2^(-1)`) and especially for complex exponents like `2^i` <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>. The definition is extended to ensure the "exponential property" holds: `b^(x+y) = b^x * b^y` <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.

From a group theory perspective, this property is crucial: adding inputs corresponds to multiplying outputs <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>. This suggests treating inputs as members of the additive group of sliding actions and outputs as members of the multiplicative group of stretching/squishing actions <a class="yt-timestamp" data-t="00:16:58">[00:16:58]</a>.

Such functions that preserve the group structure (i.e., composing inputs corresponds to composing outputs) are called **homomorphisms** <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>.

### The Role of Euler's Number `e`
When a real number is plugged into `b^x`, a positive real number (a pure stretching/squishing action) is produced <a class="yt-timestamp" data-t="00:18:33">[00:18:33]</a>. It's logical then for the "new dimension" of additive actions (vertical slides) to map to the "new dimension" of multiplicative actions (pure rotations) <a class="yt-timestamp" data-t="00:18:49">[00:18:49]</a>. This means complex numbers on the vertical imaginary axis (multiples of `i`) should map to complex numbers on the unit circle <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>.

*   For `2^x`, the input `i` (a vertical slide of one unit) maps to a rotation of approximately 0.693 radians around the unit circle <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.
*   For `5^x`, the input `i` maps to a rotation of approximately 1.609 radians <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.

[[properties_of_eulers_number_e | What makes the number `e` special]] is that when the exponential `e^x` maps vertical slides to rotations, a vertical slide of one unit (corresponding to `i`) maps to a rotation of *exactly one radian* <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>. Consequently, a vertical slide of `pi` units (corresponding to `pi * i`) maps to a rotation of exactly `pi` radians <a class="yt-timestamp" data-t="00:20:39">[00:20:39]</a>. This 180-degree rotation is the multiplicative action associated with the number negative one <a class="yt-timestamp" data-t="00:20:51">[00:20:51]</a>. This is the essence of [[eulers_formula_and_mathematical_proofs | Euler's formula]]: `e^(pi*i) = -1` <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

The special nature of `e` is deeply rooted in calculus, specifically because `e^x` is the only exponential function that is equal to its own derivative <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>.

## Conclusion

Viewing [[eulers_formula_and_mathematical_proofs | Euler's formula]] through the lens of [[exponentiation_in_group_theory | group theory]] provides a vivid interpretation:
*   Exponential functions map purely vertical slides (additive actions perpendicular to the real number line) into pure rotations (multiplicative actions perpendicular to the real number stretching actions) <a class="yt-timestamp" data-t="00:21:45">[00:21:45]</a>.
*   `e^x` performs this mapping in a unique way, ensuring that a vertical slide of `pi` units corresponds precisely to a `pi`-radian rotation, which is the 180-degree rotation associated with negative 1 <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>.

The function `e^x` can also be visualized as a transformation of the complex plane, rolling the plane into a cylinder and then "smooshing" it onto the plane around zero, where vertical lines become concentric circles <a class="yt-timestamp" data-t="00:23:51">[00:23:51]</a>.