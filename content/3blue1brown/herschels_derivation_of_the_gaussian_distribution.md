---
title: Herschels derivation of the Gaussian distribution
videoId: cy8r7WSuT1I
---

From: [[3blue1brown]] <br/> 

The effectiveness of mathematics in natural sciences, as observed by physicist Eugene Wigner, often leads to surprising connections. One notable anecdote involves a statistician explaining the [[gaussian_distribution_and_the_role_of_pi | Gaussian distribution]] to a former classmate who questions the appearance of pi, the ratio of a circle's circumference to its diameter, in population trends <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The statistician's friend expressed incredulity, asking, "Surely the population has nothing to do with the circumference of a circle?" <a class="yt-timestamp" data-t="00:54:00">[00:54:00]</a> This question highlights a fundamental curiosity about the presence of pi in the formula for a normal (or Gaussian) distribution.

While a classic proof exists to explain the origin of pi (stemming from the integral of e to the negative x squared, which equals the square root of pi) <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>, this doesn't fully address the underlying "why" from a conceptual standpoint <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>. The function e to the negative x squared is the core shape of the bell curve <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>, and its area is normalized to one for a [[applications_of_probability_density | probability distribution]] <a class="yt-timestamp" data-t="02:43:00">[02:43:00]</a>. The challenge is not just to prove the integral value, but to understand why this specific function is so crucial to statistics and how it relates to concepts like the [[central_limit_theorem | central limit theorem]] <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a>.

## The Classic Integral Proof and Its Limitations

To find the area under the curve of e to the negative x squared, the standard tool is an [[integrals_and_probability_distributions | integral]] <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>. However, this particular function does not have an antiderivative that can be expressed using standard mathematical functions <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>.

A common "trick" to solve this involves elevating the problem to two dimensions. Instead of finding the area under a 2D bell curve, one seeks the volume under a 3D bell surface, defined by e to the negative (x squared plus y squared) <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>. This function exhibits [[using_geometry_for_understanding_probability | circular symmetry]] about the z-axis, as its value depends on the distance `r` from the origin (where `r^2 = x^2 + y^2`) <a class="yt-timestamp" data-t="06:08:00">[06:08:00]</a>.

By integrating in polar coordinates (using thin cylindrical shells), the volume is calculated as an integral of `2 * pi * r * e^(-r^2) dr` <a class="yt-timestamp" data-t="06:49:00">[06:49:00]</a>. This integral simplifies because `2r * e^(-r^2)` has an antiderivative of `-e^(-r^2)` <a class="yt-timestamp" data-t="08:18:00">[08:18:00]</a>. Evaluating this integral from 0 to infinity yields a volume of `pi` <a class="yt-timestamp" data-t="08:40:00">[08:40:00]</a>.

Alternatively, by integrating in Cartesian coordinates, the volume can be expressed as the square of the original 2D integral (letting `c` be the unknown area) <a class="yt-timestamp" data-t="09:31:00">[09:31:00]</a>. Since both methods calculate the same volume, setting `c^2 = pi` implies `c = sqrt(pi)` <a class="yt-timestamp" data-t="11:48:00">[11:48:00]</a>. While elegant, this proof can feel arbitrary and doesn't directly connect to the statistical interpretation <a class="yt-timestamp" data-t="12:10:00">[12:10:00]</a>.

## Herschel's Derivation of the Gaussian Shape

To address the conceptual "why," we turn to John Herschel, a 19th-century polymath, who in 1850 provided an elegant derivation for the [[gaussian_distribution_and_the_role_of_pi | Gaussian distribution]] <a class="yt-timestamp" data-t="12:51:00">[12:51:00]</a>. His approach models a probability distribution in a two-dimensional space, such as the spread of hits on a dartboard <a class="yt-timestamp" data-t="13:15:00">[13:15:00]</a>. Herschel showed that if a distribution satisfies two reasonable properties, its form is uniquely determined as e to the negative (x squared plus y squared), up to a constant <a class="yt-timestamp" data-t="13:25:00">[13:25:00]</a>.

### Property 1: Radial Symmetry

The first property states that the [[applications_of_probability_density | probability density]] around each point depends solely on its distance from the origin, not its direction <a class="yt-timestamp" data-t="13:53:00">[13:53:00]</a>.
*   This means the probability function `f2(x, y)` can be expressed as a single-variable function `f(r)`, where `r = sqrt(x^2 + y^2)` <a class="yt-timestamp" data-t="14:12:00">[14:12:00]</a>.
*   For example, on a dartboard, rotating the board makes no difference to the distribution of hits if aiming for the bullseye <a class="yt-timestamp" data-t="14:05:00">[14:05:00]</a>.

### Property 2: Independence of Coordinates

The second property asserts that the x and y coordinates of each point are independent <a class="yt-timestamp" data-t="14:33:00">[14:33:00]</a>.
*   Mathematically, this means the joint probability function `f2(x, y)` can be factored into two separate functions: `g(x)` (distribution of x) and `h(y)` (distribution of y) <a class="yt-timestamp" data-t="14:45:00">[14:45:00]</a>. So, `f2(x,y) = g(x) * h(y)` <a class="yt-timestamp" data-t="14:45:00">[14:45:00]</a>.
*   Due to radial symmetry, the behavior along both axes must be identical, implying `g(x) = h(x)` <a class="yt-timestamp" data-t="15:09:00">[15:09:00]</a>. Thus, `f2(x,y) = g(x) * g(y)` <a class="yt-timestamp" data-t="15:14:00">[15:14:00]</a>.
*   Furthermore, `f(r)` is proportional to `g(r)` (specifically, `f(r) = constant * g(r)`) <a class="yt-timestamp" data-t="15:18:00">[15:18:00]</a>. Assuming the constant is 1 for simplicity (as normalization can be applied later), we get `f(sqrt(x^2 + y^2)) = f(x) * f(y)` <a class="yt-timestamp" data-t="16:17:00">[16:17:00]</a>. This is a *functional equation*.

### Solving the Functional Equation

To solve `f(sqrt(x^2 + y^2)) = f(x) * f(y)`, a helper function `h(x) = f(sqrt(x))` is introduced <a class="yt-timestamp" data-t="17:44:00">[17:44:00]</a>. This transforms the equation into `h(x+y) = h(x) * h(y)` for positive x and y <a class="yt-timestamp" data-t="18:12:00">[18:12:00]</a>.

This specific functional equation forces `h(x)` to be an exponential function of the form `b^x` for some base `b` <a class="yt-timestamp" data-t="19:02:00">[19:02:00]</a>. For example, `h(5) = h(1+1+1+1+1) = h(1)^5` <a class="yt-timestamp" data-t="18:51:00">[18:51:00]</a>. By extending this reasoning to rational numbers and assuming continuity, `h(x) = b^x` for all positive real `x` <a class="yt-timestamp" data-t="19:38:00">[19:38:00]</a>.

It is conventional to write exponential functions with base `e`, so `h(x) = e^(c * x)` for some constant `c` <a class="yt-timestamp" data-t="20:02:00">[20:02:00]</a>. Substituting back `h(x^2) = f(x)`, we find that the function `f(x)` must be of the form `e^(c * x^2)` <a class="yt-timestamp" data-t="20:25:00">[20:25:00]</a>. For the distribution to be normalizable (i.e., its volume sums to one), the constant `c` must be negative <a class="yt-timestamp" data-t="21:12:00">[21:12:00]</a>. This leads directly to the core form of the [[gaussian_distribution_and_the_role_of_pi | Gaussian distribution]].

## Connection to the Classic Proof and the Central Limit Theorem

James Clerk Maxwell independently derived the same result ten years after Herschel, applying it to the distribution of velocities of molecules in a gas <a class="yt-timestamp" data-t="21:34:00">[21:34:00]</a>. Viewing the Gaussian as a function characterized by these properties (radial symmetry and independent coordinates) makes the appearance of pi in the integral proof less surprising, as circular symmetry is inherently part of its definition <a class="yt-timestamp" data-t="21:55:00">[21:55:00]</a>. The "trick" of bumping the problem to higher dimensions in the integral proof simply allows these defining properties to become visible <a class="yt-timestamp" data-t="22:30:00">[22:30:00]</a>.

However, even this derivation doesn't entirely satisfy the initial query about population statistics, as it presumes a multi-dimensional spatial scenario <a class="yt-timestamp" data-t="23:03:00">[23:03:00]</a>. More commonly, the normal distribution arises from the [[central_limit_theorem | central limit theorem]], which deals with the sum of many independent variables, not necessarily spatial ones <a class="yt-timestamp" data-t="23:24:00">[23:24:00]</a>. Bridging the gap between the Herschel-Maxwell derivation and the [[connections_between_gaussian_distribution_and_the_central_limit_theorem | Central Limit Theorem]] is the next step to fully address the statistician's friend's disbelief <a class="yt-timestamp" data-t="23:30:00">[23:30:00]</a>.

### Higher Dimensional Spheres
As a side note, the integration trick used in the classic proof can be extended to derive formulas for the volumes of higher dimensional spheres <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>. This demonstrates the broad applicability of these mathematical techniques beyond the context of probability. <a class="yt-timestamp" data-t="24:00:00">[24:00:00]</a>