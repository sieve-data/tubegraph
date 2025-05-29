---
title: Gaussian distribution and the role of pi
videoId: cy8r7WSuT1I
---

From: [[3blue1brown]] <br/> 

The phrase "the unreasonable effectiveness of mathematics in the natural sciences" was coined by physicist Eugene Wigner <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Wigner opens his paper with an anecdote about two high school classmates discussing their jobs <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. One became a statistician working on population trends, and showed a reprint of their work to the former classmate <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. The reprint began with the [[connections_between_gaussian_distribution_and_the_central_limit_theorem | Gaussian distribution]] <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. When the statistician explained the symbols, the classmate, incredulous, asked about a specific symbol <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. Upon learning it was pi, the ratio of a circle's circumference to its diameter, the classmate exclaimed, "Surely the population has nothing to do with the circumference of a circle" <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

This article delves into why pi appears in the formula for a normal (or [[connections_between_gaussian_distribution_and_the_central_limit_theorem | Gaussian]]) distribution, addressing the statistician's friend's disbelief <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The goal is to explain this connection and ultimately link it to the [[connections_between_gaussian_distribution_and_the_central_limit_theorem | central limit theorem]] <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

## Pi's Origin in the Gaussian Formula

The basic function describing the bell curve shape of a normal distribution, when stripped of parameters and constants, is `e` to the negative `x` squared (`e^(-x^2)`) <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. Pi appears in the final formula because the area underneath this curve is the square root of pi (`sqrt(π)`) <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. To interpret the curve as a [[integrals_and_probability_distributions | probability distribution]], its area must be one, requiring division by `sqrt(π)` <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. Thus, pi originates from the area under this specific curve <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

## The Classic Proof: Finding the Area Under e^(-x^2)

Calculating the area under `e^(-x^2)` requires an integral <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. However, it is provably impossible to find a standard antiderivative for this function using typical mathematical tools <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. A clever trick is needed.

### The "Trick": Bumping Up a Dimension

The first step of the trick involves moving from a 2D bell curve to a 3D bell surface <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. The function for this surface is `e^(-(x^2+y^2))` <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. This function has circular symmetry, meaning inputs on a given circle have the same output, resulting in rotational symmetry about the z-axis when graphed <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.

#### Volume Calculation using Cylindrical Shells

Respecting the circular symmetry, the volume under this surface can be computed by integrating thin cylindrical shells <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   The circumference of a shell is `2πr` <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
*   The height is `e^(-r^2)` <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
*   The volume of a thin shell is `(2πr * e^(-r^2)) dr` <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.

Integrating this expression from `r = 0` to `infinity`:
`∫[0,∞] (2πr * e^(-r^2)) dr` <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>
Factoring out pi: `π ∫[0,∞] (2r * e^(-r^2)) dr` <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>
The antiderivative of `2r * e^(-r^2)` is `-e^(-r^2)` <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.
Evaluating the definite integral gives `0 - (-1) = 1` <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
Therefore, the volume under the bell surface is `π * 1 = π` <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.

#### Volume Calculation using Cartesian Slices

Alternatively, the volume can be approached by chopping the surface into slices parallel to one of the axes, e.g., the x-axis <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
The function `e^(-(x^2+y^2))` can be factored as `e^(-x^2) * e^(-y^2)` <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.
Each slice at a given `y` value is `e^(-x^2)` scaled by `e^(-y^2)` <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
The area of a slice (e.g., at `y=0`) is the mystery constant, `c = ∫[-∞,∞] e^(-x^2) dx` <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.
The area of any slice at `y` is `c * e^(-y^2)` <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.

Integrating these slice areas to find the total volume:
`Volume = ∫[-∞,∞] (c * e^(-y^2)) dy` <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>
Factoring out `c`: `c * ∫[-∞,∞] e^(-y^2) dy` <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>
Since `∫[-∞,∞] e^(-y^2) dy` is also `c`, the volume is `c * c = c^2` <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.

Since both methods calculate the same volume, we have `c^2 = π` <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.
Therefore, the area underneath the bell curve, `c`, is `sqrt(π)` <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.

## Why is e^(-x^2) Special? The Herschel-Maxwell Derivation

While the integral trick is elegant, it doesn't explain *why* `e^(-x^2)` is the special function for statistics, nor why circles are involved <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>. The [[herschels_derivation_of_the_gaussian_distribution | Herschel's derivation of the Gaussian distribution]] from 1850 provides insight <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.

Imagine a probability distribution in two-dimensional space, like hits on a dartboard <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>. Herschel showed that if this distribution satisfies two reasonable properties, it must take the form `e^(-(x^2+y^2))` (up to constants) <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>.

### Property 1: Radial Symmetry

The probability density depends *only* on the distance from the origin (`r`), not on direction <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>. Mathematically, the function `f2(x, y)` can be expressed as `f(r)`, where `r = sqrt(x^2 + y^2)` <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>.

### Property 2: Independence of Coordinates

The x and y coordinates are independent of each other <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>. This means the probability density `f2(x, y)` can be factored into a function purely of `x` and a function purely of `y`: `f2(x, y) = g(x) * h(y)` <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. Due to radial symmetry, `g` and `h` must be the same function, so `f2(x, y) = g(x) * g(y)` <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.

### The Functional Equation

Combining these properties and assuming `f` and `g` are proportional (or, for simplicity, the same function, up to a scaling constant that can be normalized later <a class="yt-timestamp" data-t="00:15:48">[00:15:48]</a>), we get the functional equation:
`f(sqrt(x^2 + y^2)) = f(x) * f(y)` <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>

To solve this, introduce a helper function `h(z) = f(sqrt(z))` <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>, so `f(x) = h(x^2)` <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>.
The equation becomes: `h(x^2 + y^2) = h(x^2) * h(y^2)` <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>.
Let `A = x^2` and `B = y^2`. Then `h(A + B) = h(A) * h(B)` <a class="yt-timestamp" data-t="00:18:18">[00:18:18]</a>.
This is a form of Cauchy's functional equation that turns addition into multiplication <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.

This equation implies that `h(n) = (h(1))^n` for any whole number `n` <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>. If we let `b = h(1)`, then `h(n) = b^n` <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>. This extends to rational inputs `p/q`, where `h(p/q) = b^(p/q)` <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>. Assuming `h` is continuous, this forces `h(x) = b^x` for all positive real `x` <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>.

Mathematicians often express exponential functions using `e` as the base: `h(x) = e^(c*x)` for some constant `c` <a class="yt-timestamp" data-t="00:20:02">[00:20:02]</a>.
Substituting back, `f(x) = h(x^2) = e^(c*x^2)` <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>.
For the function to represent a probability distribution (i.e., not blow up to infinity), the constant `c` must be negative <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>.

James Clerk Maxwell independently arrived at the same derivation ten years after Herschel, applying it in three dimensions to model the distribution of molecular velocities in a gas <a class="yt-timestamp" data-t="00:21:34">[00:21:34]</a>.

### Conclusion of the Derivation

This derivation shows that the `e^(-x^2)` form is not arbitrary but arises inevitably from the two simple properties of radial symmetry and independence of coordinates <a class="yt-timestamp" data-t="00:21:55">[00:21:55]</a>. Since circular symmetry is a defining property, it becomes less surprising that [[pis_relationship_to_circles_and_geometry | pi]] makes an appearance in its normalization <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>. The "trick" of moving to higher dimensions in the integral calculation now feels like an inevitable necessity, aligning with the function's inherent properties <a class="yt-timestamp" data-t="00:22:13">[00:22:13]</a>.

## The Unfinished Connection

Despite the clarity provided by the Herschel-Maxwell derivation, it still presumes a multi-dimensional spatial or geometric context <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>. Often, the normal distribution appears in non-geometric situations, primarily stemming from the [[connections_between_gaussian_distribution_and_the_central_limit_theorem | central limit theorem]], which deals with adding many independent variables <a class="yt-timestamp" data-t="00:23:24">[00:23:24]</a>. The final step to fully satisfy the statistician's friend requires explaining why the function derived by Herschel and Maxwell is the same as the one central to the [[connections_between_gaussian_distribution_and_the_central_limit_theorem | central limit theorem]] <a class="yt-timestamp" data-t="00:23:30">[00:23:30]</a>.

### Footnote: Higher-Dimensional Spheres

Applying this integration trick in higher dimensions allows for the derivation of formulas for volumes of higher-dimensional spheres <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>. This is a fun exercise for those comfortable with integration by parts <a class="yt-timestamp" data-t="00:24:09">[00:24:09]</a>.