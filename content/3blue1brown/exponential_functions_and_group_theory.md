---
title: Exponential functions and group theory
videoId: mvmuCPvRoWQ
---

From: [[3blue1brown]] <br/> 

The field of [[introduction_to_group_theory|group theory]] offers a significantly richer interpretation of Euler's formula, which states e^(πi) = -1 <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>, beyond a simple association between numbers <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. Understanding this perspective requires an [[introduction_to_group_theory|introduction to the basics of group theory]] <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This approach can fundamentally alter one's perception of numbers and algebra <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

## What is Group Theory?

At its core, [[group theory and symmetries|group theory is the study of symmetry]] <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. This involves identifying all actions that can be performed on an object, such as a square, that leave it appearing indistinguishable from its original state <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. Examples include rotating a square 90 degrees counterclockwise or flipping it across a vertical line <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. Each such action is termed a "symmetry" of the object <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

A "group" is a collection of these symmetries <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
*   **Finite Groups**: For instance, the symmetries of a square form the "dihedral group of order 8", consisting of 8 symmetries: doing nothing, three rotations, and four flips <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   **Infinite Groups**: An example is the group of all possible rotations of a circle, which includes an infinite continuum of angles between 0 and 2π radians <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. In some cases, each action in a group can be associated with a unique point on the object itself, as seen with circle rotations mapping to points on the circle <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

The essence of [[introduction_to_group_theory|group theory]] lies in understanding how these symmetries interact <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. When two actions are performed sequentially (e.g., rotating a square and then flipping it), their combined effect is equivalent to a single other action from the group <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. This sequential application of actions defines an "arithmetic" within the group, whether thought of as addition or multiplication of actions <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. The underlying collection of these compositional relations is what fundamentally constitutes a group <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. This concept is foundational to much of modern mathematics <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

## Numbers as Groups

Numbers, both real and complex, can be understood as examples of groups themselves, acting in different ways:

### The Additive Group of Real Numbers
Consider all possible sliding actions (translations) on a number line, moving it left or right along itself <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. This collection forms a group. Each sliding action can be uniquely associated with a real number by observing where the point at zero ends up <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. For example, sliding right by 3 units is associated with the number 3 <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>, and sliding left by 2 units with -2 <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. The "doing nothing" action corresponds to 0 <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.

This is called the **additive group of real numbers** because composing these actions mirrors arithmetic addition <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. Sliding right by 3 units and then by 2 units has the same overall effect as sliding right by 5 units (3 + 2) <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. This perspective views numbers as a specific instance within the broader category of symmetry groups, where addition is the group's internal arithmetic <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

### The Additive Group of Complex Numbers
This concept extends to the complex plane by considering sliding actions in two dimensions <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. Vertical slides correspond to imaginary numbers (e.g., 2i for a slide of 2 units vertically) <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. A diagonal slide, like the one associated with 3 + 2i, is equivalent to a horizontal slide of 3 units followed by a vertical slide of 2 units <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. Composing these sliding actions on the complex plane aligns with the addition of complex numbers (e.g., (3 + 2i) + (1 - 3i) results in (3+1) + (2-3)i) <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. This collection of all 2D sliding actions forms the **additive group of complex numbers** <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.

### The Multiplicative Group of Positive Real Numbers
A different kind of group is formed by stretching or squishing actions on the number line, keeping 0 fixed <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. Each action is associated with a unique positive real number by observing where the point at 1 lands <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>. For example, stretching by a factor of 3 takes 1 to 3 <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.

Composing these actions corresponds to multiplication <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>. Stretching by 3 and then by 2 has the same effect as stretching by 6 (3 × 2) <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. This is known as the **multiplicative group of positive real numbers** <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.

### The Multiplicative Group of Complex Numbers
Extending this to the complex plane, fixing 0 and dragging 1 around allows for not only stretching/squishing but also rotational actions <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>. The action associated with the complex number *i* (dragging 1 to *i*) is a 90-degree rotation <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>. Applying this action twice (i.e., *i* × *i*) results in a 180-degree rotation, which is the action associated with -1 <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.

In general, every multiplicative action on the complex plane combines a stretch/squish (associated with a point on the positive real line) with a pure rotation (associated with a point on the unit circle) <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.

## Exponential Functions and Homomorphisms

[[Exponential growth and decay|Exponential functions]] are typically introduced as repeated multiplication <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a> (e.g., 2³ = 2 × 2 × 2) <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>. A key [[properties of the exponential function|property of the exponential function]] is that adding inputs corresponds to multiplying outputs: 2^(x+y) = 2^x * 2^y <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>. This property is crucial for extending the definition beyond counting numbers to fractional, negative, or complex exponents, as these latter forms cannot be understood as "repeated multiplication" <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>. The extended definition ensures this fundamental property remains consistent <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>.

From a [[introduction to group theory|group theory]] perspective, this property hints at a special relationship: [[exponential functions and group theory|exponential functions]] map elements from the additive group (inputs) to elements of the multiplicative group (outputs) <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>. Specifically, adding sliding actions (inputs) corresponds to multiplying stretching/rotating actions (outputs) <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>.

Functions that preserve the group structure in this way—where composing actions in the input group corresponds to composing the mapped actions in the output group—are called **homomorphisms** <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>. This concept is fundamental throughout [[introduction to group theory|group theory]] <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>.

### Euler's Formula through Group Homomorphism
Consider the [[exponential functions and group theory|exponential function]] e^x as a homomorphism from the additive group of complex numbers to the multiplicative group of complex numbers.
*   Purely real inputs (horizontal slides) map to positive real outputs (pure stretching or squishing actions) <a class="yt-timestamp" data-t="00:18:33">[00:18:33]</a>.
*   The "new dimension" of additive actions, i.e., purely vertical slides (multiples of *i*), naturally maps to the "new dimension" of multiplicative actions, i.e., pure rotations (points on the unit circle) <a class="yt-timestamp" data-t="00:18:53">[00:18:53]</a>.

For a general base like 2^x, the input *i* (a vertical slide of one unit) maps to a rotation of approximately 0.693 radians on the unit circle <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>. For 5^x, *i* maps to a rotation of about 1.609 radians <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.

What makes the number *e* special is that the [[exponential functions and group theory|exponential function]] e^x maps a vertical slide of exactly one unit (corresponding to the input *i*) to a rotation of precisely one radian on the unit circle <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>. Consequently, a vertical slide of two units (2i) maps to a rotation of two radians, and so on <a class="yt-timestamp" data-t="00:20:27">[00:20:27]</a>.

This leads directly to Euler's formula: a vertical slide of π units (πi) maps to a rotation of exactly π radians <a class="yt-timestamp" data-t="00:20:39">[00:20:39]</a>. A π-radian rotation is a 180-degree rotation, which is the multiplicative action associated with the number -1 <a class="yt-timestamp" data-t="00:20:46">[00:20:46]</a>. Thus, e^(πi) = -1 <a class="yt-timestamp" data-t="00:20:51">[00:20:51]</a>.

The reason *e* exhibits this particular mapping behavior is rooted in [[calculus and exponential functions|calculus]], where *e* is defined. While all [[derivatives of exponential functions|exponential functions]] are proportional to their own [[derivatives of exponential functions|derivative]], e^x is uniquely equal to its own [[derivatives of exponential functions|derivative]] <a class="yt-timestamp" data-t="00:21:13">[00:21:13]</a>.

Viewing [[exponential functions and group theory|exponential functions]] through the lens of [[introduction to group theory|group theory]] offers a vivid interpretation: they map purely vertical additive slides (perpendicular to the real number line) into pure rotations (perpendicular to real number stretching actions) <a class="yt-timestamp" data-t="00:21:45">[00:21:45]</a>. The base *e* ensures that a vertical slide of π units precisely corresponds to a rotation of π radians, yielding -1 <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>.

Visually, the [[exponential functions and group theory|function e^x]] transforms the complex plane by first "rolling" it into a cylinder (where vertical lines become circles) and then "smooshing" that cylinder onto the plane around zero, such that exponentially spaced concentric circles correspond to the original vertical lines <a class="yt-timestamp" data-t="00:23:51">[00:23:51]</a>.