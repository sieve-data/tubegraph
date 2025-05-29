---
title: Exponentiation in group theory
videoId: mvmuCPvRoWQ
---

From: [[3blue1brown]] <br/> 

Two years after the first video on [[eulers_formula_and_mathematical_proofs | Euler's formula]], `e`<sup>`pi`</sup>`i` = -1 <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>, this revisited explanation aims to provide a richer interpretation using concepts from [[introduction_to_group_theory | group theory]] <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. While a quick explanation of [[eulers_formula_and_mathematical_proofs | Euler's formula]] is possible for those comfortable with vector calculus <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>, the [[introduction_to_group_theory | group theory]] perspective offers an intuition that can change how one thinks about numbers and algebra <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

## What is a Group?

[[group_theory_and_the_idea_of_symmetry | Group theory]] is fundamentally about studying the nature of symmetry <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. A shape like a square is symmetric because there are actions (like rotations or flips) that leave it looking indistinguishable from its original state <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. Each of these actions is called a "symmetry" of the square <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>, and all of them together form a "group of symmetries," or simply a "group" <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

The dihedral group of order 8, for instance, consists of 8 symmetries of a square: doing nothing, three different rotations (e.g., 90 degrees counterclockwise), and four ways to flip it over <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. While this is a *finite group* <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>, many groups consist of infinitely many actions, such as all possible rotations of a circle <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. Each action in the circle group can be associated with a unique point on the circle itself <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

The core of [[introduction_to_group_theory | group theory]] lies in understanding how these symmetries interact <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. Applying one action after another (e.g., rotating a square 90 degrees then flipping it) results in an overall effect equivalent to a single action from the group <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. This means there's an "arithmetic" within any group where two actions can be combined to yield a third <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. This collection of underlying relations, defining how actions compose, is what defines a group <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

## Numbers as Groups

Numbers, both real and complex, can be understood as groups in two distinct ways <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

### Additive Group of Numbers

Consider the group of "sliding actions" on a number line (or complex plane) <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. Each sliding action corresponds to a unique number:
*   Sliding right by 3 units is associated with the number 3 <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
*   Sliding left by 2 units is associated with -2 <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
*   Doing nothing is associated with 0 <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
*   On the complex plane, 3 + 2i corresponds to sliding right by 3 units and then vertically by 2 units <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.

This is called the **additive group of real numbers** (or complex numbers) because combining sliding actions looks exactly like addition <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. Sliding right by 3 then by 2 results in a slide of 5 (3+2) <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. Similarly, combining slides in the complex plane involves adding their real and imaginary components <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.

### Multiplicative Group of Numbers

Another group involves "stretching or squishing" actions on the number line, keeping 0 fixed <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. Each action is associated with a positive number, determined by where the point at 1 lands:
*   Stretching by a factor of 3 maps 1 to 3 <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
*   Squishing by a factor of 1/2 maps 1 to 1/2 <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.

This is the **multiplicative group of positive real numbers** <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>. Combining actions here looks like multiplication: stretching by 3 then by 2 results in a stretch by 6 (3*2) <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.

Extending this to the complex plane, fixing 0 and dragging 1 around introduces actions with a rotational component <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. The action associated with `i` (dragging 1 to `i`) is a 90-degree rotation <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>. Applying this action twice (`i` * `i`) results in a 180-degree rotation, which maps 1 to -1 <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>, thus `i` * `i` = -1 <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>. Any multiplicative action on the complex plane can be seen as a combination of a stretch/squish and a pure rotation (associated with points on the unit circle) <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.

## Exponentiation Through Group Theory

Traditionally, [[exponential_functions_and_their_properties | exponents]] like 2<sup>3</sup> are understood as repeated multiplication <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. However, this definition doesn't make sense for fractional or negative [[exponential_functions_and_their_properties | exponents]], let alone complex ones like 2<sup>`i`</sup> <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>. The definition is extended to maintain the crucial "exponential property": `b`<sup>`x`+`y`</sup> = `b`<sup>`x`</sup> * `b`<sup>`y`</sup> <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>.

From a [[introduction_to_group_theory | group theory]] perspective, this property is profound <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>:
*   Adding inputs (`x` + `y`) corresponds to actions in the additive group (sliding).
*   Multiplying outputs (`b`<sup>`x`</sup> * `b`<sup>`y`</sup>) corresponds to actions in the multiplicative group (stretching/rotating).

Therefore, an [[exponential_functions_and_their_properties | exponential function]] can be seen as a function that takes actions from the additive group (inputs) and maps them to actions in the multiplicative group (outputs) <a class="yt-timestamp" data-t="00:16:58">[00:16:58]</a>. This kind of function, which preserves the group structure (i.e., the arithmetic within the groups), is called a **homomorphism** <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>.

The [[exponential_functions_and_their_properties | exponential function]] `b`<sup>`x`</sup> maps purely horizontal slides (real number inputs) to pure stretching or squishing actions (positive real number outputs) <a class="yt-timestamp" data-t="00:18:33">[00:18:33]</a>. This suggests that the "new dimension" of additive actions (vertical slides on the complex plane, i.e., imaginary numbers) should map to the "new dimension" of multiplicative actions (pure rotations on the unit circle) <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>.

### The Special Nature of 'e'

For any base `b`, the input `i` (a vertical slide of one unit) maps to a rotation of a specific radian value <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>. For `2`<sup>`x`</sup>, `i` maps to a rotation of approximately 0.693 radians <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>. For `5`<sup>`x`</sup>, `i` maps to about 1.609 radians <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>.

The number `e` is special because when `e`<sup>`x`</sup> maps vertical slides to rotations, a vertical slide of one unit (corresponding to `i`) maps to a rotation of *exactly one radian* <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>. Consequently:
*   A vertical slide of two units maps to a rotation of two radians <a class="yt-timestamp" data-t="00:20:27">[00:20:27]</a>.
*   A vertical slide of `pi` units (corresponding to `pi` * `i`) maps to a rotation of exactly `pi` radians <a class="yt-timestamp" data-t="00:20:39">[00:20:39]</a>.

This `pi`-radian rotation is equivalent to a 180-degree rotation, which is the multiplicative action associated with the number -1 <a class="yt-timestamp" data-t="00:20:46">[00:20:46]</a>. This directly leads to [[eulers_formula_and_mathematical_proofs | Euler's formula]]: `e`<sup>`pi`</sup>`i` = -1 <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

::info
The reason `e` is unique in this way is rooted in calculus, specifically because `e`<sup>`x`</sup> is equal to its own derivative <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>.
::

## Conclusion

Understanding [[exponentiation]] through the lens of [[introduction_to_group_theory | group theory]] provides a vivid interpretation <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a>. It reveals that [[exponential_functions_and_their_properties | exponentials]] map purely vertical slides (additive actions perpendicular to the real number line) into pure rotations (multiplicative actions perpendicular to real number stretching actions) <a class="yt-timestamp" data-t="00:21:45">[00:21:45]</a>. The base `e` performs this mapping in a special way, where a vertical slide of `pi` units precisely corresponds to a `pi`-radian rotation, leading to the elegant connection in [[eulers_formula_and_mathematical_proofs | Euler's formula]] <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>.

The function `e`<sup>`x`</sup> can be visualized as transforming the complex plane by first rolling it into a cylinder, wrapping vertical lines into circles, and then mapping that cylinder onto the plane around zero, where concentric circles correspond to the original vertical lines <a class="yt-timestamp" data-t="00:23:51">[00:23:51]</a>.