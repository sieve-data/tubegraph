---
title: Role of circular symmetry in statistical distributions
videoId: cy8r7WSuT1I
---

From: [[3blue1brown]] <br/> 

The pervasive presence of mathematics in the natural sciences is a topic explored by physicist Eugene Wigner in his paper, "The unreasonable effectiveness of mathematics in the natural sciences" <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Wigner opens his paper with an anecdote about a statistician explaining the [[Normal distribution and its properties | Gaussian distribution]] to a former classmate <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. The statistician explains the symbols, including `pi`, which is described as the ratio of a circle's circumference to its diameter <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. The classmate expresses incredulity, questioning what population trends have to do with the circumference of a circle <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

This article delves into this very question, exploring the elegant connection between circular symmetry and the [[Normal distribution and its properties | normal distribution]] <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

## Pi in the Normal Distribution Formula

The core function describing the bell curve shape of a [[Normal distribution and its properties | normal distribution]] (or [[Normal distribution and its properties | Gaussian distribution]]) is `e` to the negative `x` squared (`e^(-x^2)`) <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. The appearance of `pi` in the final formula for this distribution stems from the fact that the area underneath this curve is exactly the square root of `pi` <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. To ensure the area under the curve is one—a requirement for a [[Connection between Gaussian distribution and probability | probability density]] [[Probability density and distribution | distribution]]—this square root of `pi` must be divided out <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

The challenge lies in explaining not just *that* the area is the square root of `pi`, but *why* this specific function (`e^(-x^2)`) is so fundamental in statistics, especially given its non-obvious connection to circles <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. The goal is to connect the proof involving `pi` with the [[Assumptions and limitations of the Central Limit Theorem | Central Limit Theorem]], which explains when a [[Normal distribution and its properties | normal distribution]] arises in nature <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

## The Classic Proof: Integration by Bumping Up a Dimension

Finding the area under a curve typically involves an integral <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. However, for `e^(-x^2)`, it is provably impossible to find an antiderivative using standard mathematical tools <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. This necessitates a clever trick <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

The first step of this trick is to "bump things up one dimension" <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. Instead of finding the area under a 1D bell curve, we seek the volume under a 2D "bell surface" <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. This 2D function is defined as `e` to the negative `r` squared (`e^(-r^2)`), where `r` is the distance from a point `(x, y)` to the origin, meaning `r^2 = x^2 + y^2` by the Pythagorean theorem <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. So the function is `e^(-(x^2 + y^2))` <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.

### Leveraging Circular Symmetry

This 2D function exhibits a profound [[Symmetries and group actions | circular symmetry]] <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>. All inputs `(x, y)` that lie on a given circle (i.e., have the same distance `r` from the origin) produce the same output value <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. This results in a rotational symmetry about the z-axis when graphed <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

To compute the volume under this surface, this symmetry is respected by integrating using thin cylindrical shells <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.
*   The area of a cylindrical shell is its circumference (`2 * pi * r`) multiplied by its height (the function's value, `e^(-r^2)`) <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.
*   Giving the cylinder a small thickness `dr`, its volume is approximately `(2 * pi * r * e^(-r^2)) * dr` <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
*   Integrating these volumes from `r = 0` to infinity:
    *   `Integral[0 to infinity] (2 * pi * r * e^(-r^2)) dr`
    *   The `pi` can be factored out: `pi * Integral[0 to infinity] (2 * r * e^(-r^2)) dr` <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
    *   The term `(2 * r * e^(-r^2))` has an antiderivative: `-e^(-r^2)` <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
    *   Evaluating the antiderivative at the bounds (infinity and 0) yields `0 - (-1) = 1` <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
    *   Therefore, the total volume under the bell surface is `pi * 1 = pi` <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

This derivation inherently involves `pi` because of the intrinsic [[Symmetries and group actions | circular symmetry]] of the problem setup <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

### Relating 2D and 3D Volumes

The utility of bumping up a dimension becomes apparent when the volume is analyzed in a second, different way <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. We can chop the 3D volume into slices parallel to one of the axes, say the x-axis <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.

The function `e^(-(x^2 + y^2))` can be factored as `e^(-x^2) * e^(-y^2)` <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.
*   Consider a slice where `y` is a constant (e.g., `y=0`) <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. The slice's shape is `e^(-x^2)` multiplied by `e^(-y^2)` (which is a constant for that slice) <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
*   The area of such a slice is the "mystery constant" `c` (the area under `e^(-x^2)`) multiplied by `e^(-y^2)` <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
*   To find the total volume, we integrate these slice areas with respect to `y` from negative infinity to infinity:
    *   `Integral[-infinity to infinity] (c * e^(-y^2)) dy` <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
    *   Factoring out `c`, we get `c * Integral[-infinity to infinity] e^(-y^2) dy` <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.
    *   The remaining integral is exactly the mystery constant `c` again <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.
    *   Thus, the volume under the bell surface is `c * c = c^2` <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.

Since we established through polar integration that the volume is `pi`, we can equate the two results: `c^2 = pi` <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>. Therefore, the mystery constant `c` (the area under `e^(-x^2)`) is the square root of `pi` <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.

## Herschel-Maxwell Derivation: The Inevitability of Circular Symmetry

While elegant, the proof above feels like a "trick" <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>. To address the statistician's friend's question about circles and population statistics, we turn to a derivation by John Herschel in 1850, independently discovered by James Clerk Maxwell years later <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.

Herschel considered a 2D probability [[Probability density and distribution | distribution]], such as the distribution of hits on a dartboard <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>. He showed that if this distribution satisfies two "reasonable" properties, it is *forced* to take the shape `e^(-(x^2 + y^2))` (or `e^(-c*(x^2 + y^2))` allowing for a spread parameter) <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>.

### Property 1: Radial Symmetry

The first property states that the probability density around each point depends *only* on its distance from the origin (`r`), not on its direction <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>. This means the probability function `f2(x, y)` can be expressed as a single-variable function `f(r)` <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>. This is the explicit embrace of [[Symmetries and group actions | circular symmetry]] in the distribution <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.

### Property 2: Independence of Coordinates

The second property is that the `x` and `y` coordinates of each point are independent of each other <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>. Mathematically, this means the 2D probability function `f2(x, y)` can be factored into two separate functions: `g(x) * h(y)` <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. Due to the radial symmetry, the behavior along each axis must be the same, so `g(x)` and `h(y)` are essentially the same function, `g(x) * g(y)` <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.

### The Functional Equation

Combining these properties leads to a functional equation: `f(sqrt(x^2 + y^2)) = g(x) * g(y)` <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>. Assuming `f` and `g` are proportional (or, for simplicity, the same function after normalization), we get `f(sqrt(x^2 + y^2)) = f(x) * f(y)` <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.

Let `h(x) = f(sqrt(x))` <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>. The functional equation then becomes `h(x^2 + y^2) = h(x^2) * h(y^2)` <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>. This is a form of Cauchy's functional equation, which implies that `h(z)` must be an exponential function of the form `b^z` (or `e^(c*z)` for some constant `c`) for all positive real `z` <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.

Substituting back, `f(x)` must be `e^(c*x^2)` <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>. For the function to represent a probability distribution that can be normalized (i.e., its integral converges), the constant `c` must be negative <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>. This derivation shows that the specific `e^(-x^2)` form of the [[Normal distribution and its properties | Gaussian distribution]] arises naturally from these two simple and intuitive assumptions about its shape.

### Synthesis of Concepts

This derivation makes the appearance of `pi` in the [[Normal distribution and its properties | normal distribution]] formula less mysterious <a class="yt-timestamp" data-t="00:21:55">[00:21:55]</a>. The [[Symmetries and group actions | circular symmetry]] is explicitly part of the defining properties of the distribution itself <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>. The "trick" of bumping up a dimension and using polar coordinates in the integral proof is no longer arbitrary; it is a direct application of these defining symmetries <a class="yt-timestamp" data-t="00:22:10">[00:22:10]</a>. The proof's reliance on both radial symmetry (for polar coordinates) and the ability to factor the function (for Cartesian slices) directly mirrors the two properties defining the Gaussian distribution in the Herschel-Maxwell derivation <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a>.

## Conclusion and Further Connections

While the Herschel-Maxwell derivation sheds light on the role of circular symmetry, it still leaves a gap for those who primarily encounter the [[Normal distribution and its properties | normal distribution]] via the [[Assumptions and limitations of the Central Limit Theorem | Central Limit Theorem]], which does not inherently feel spatial or geometric <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>. The next step is to bridge the understanding between the Herschel-Maxwell characterization and the [[Assumptions and limitations of the Central Limit Theorem | Central Limit Theorem]] <a class="yt-timestamp" data-t="00:23:30">[00:23:30]</a>.

### Footnote: Higher-Dimensional Spheres
Interestingly, applying the integration trick (bumping up dimensions) to other functions can also be used to derive formulas for the volumes of higher-dimensional spheres <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>. This demonstrates the broader applicability of leveraging symmetry in complex mathematical problems.