---
title: Connections between Gaussian distribution and the central limit theorem
videoId: cy8r7WSuT1I
---

From: [[3blue1brown]] <br/> 
The phrase "the unreasonable effectiveness of mathematics in the natural sciences" was the title of a paper by physicist Eugene Wigner <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Wigner opens his paper with an anecdote about a statistician explaining the [[gaussian_distribution_and_the_role_of_pi | Gaussian distribution]] to a former classmate <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. The classmate was incredulous upon learning that "pi," the ratio of a circle's circumference to its diameter, was part of the formula for population trends <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

This article explores why pi appears in the formula for a [[normal_distribution_and_its_characteristics | normal distribution]] and seeks to understand why the function `e^(-x^2)` is so central to statistics <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. The ultimate goal is to bridge the gap between pure mathematical proofs and the practical appearance of the [[normal_distribution_and_its_characteristics | normal distribution]] in phenomena like population statistics, especially its connection to the [[central_limit_theorem_basics_and_applications | Central Limit Theorem]] <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

## The Area Under the Bell Curve

The basic function describing the bell curve shape, after stripping away parameters and constants, is `e^(-x^2)` <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. Pi shows up in the final formula because the area underneath this curve works out to be the square root of pi <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. This area must be divided out to ensure the total area under the curve is one, a requirement for any [[integrals_and_probability_distributions | probability distribution]] <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

Calculating the area under a curve typically involves an [[integrals_and_probability_distributions | integral]] <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. For `e^(-x^2)` from negative infinity to infinity, the usual method of finding an antiderivative is not possible using standard mathematical tools <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. This necessitates a clever trick.

### The "Trick": Bumping to Higher Dimensions

The first step of this trick is to increase the problem by one dimension <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. Instead of finding the area under a 2D bell curve, we aim to find the volume underneath a 3D bell surface, defined by `e^(-(x^2+y^2))` <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. This function has circular symmetry because `x^2 + y^2` is the square of the distance (`r^2`) from the origin <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.

The volume under this surface can be calculated in two ways:

1.  **Using cylindrical shells (polar coordinates)**:
    By respecting the circular symmetry, we can integrate the volumes of infinitesimally thin cylindrical shells <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. The area of a shell is its circumference (`2πr`) times its height (`e^(-r^2)`) <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. When integrating this expression from `r = 0` to infinity, the `2r` term inside the integral makes finding an antiderivative possible <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. The [[application_of_limits_in_integral_calculus | integral]] evaluates to 1, leaving the volume as `pi` (which was factored out) <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. Thus, the volume underneath this bell surface is `pi` <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.

2.  **Using Cartesian slices**:
    Alternatively, the volume can be found by chopping the surface into slices parallel to one of the axes, e.g., the x-axis <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. The function `e^(-(x^2+y^2))` can be factored as `e^(-x^2) * e^(-y^2)` <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. Each slice, corresponding to a fixed `y` value, has the same basic `e^(-x^2)` bell curve shape, just scaled vertically by `e^(-y^2)` <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>. If `c` represents the unknown area under `e^(-x^2)`, then the area of each slice is `c * e^(-y^2)` <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. Integrating these slices with respect to `y` from negative infinity to infinity gives the total volume as `c` multiplied by another integral of `e^(-y^2)`, which is also `c` <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. Therefore, the volume is `c^2` <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.

By equating the two calculated volumes, `pi = c^2`, which means `c = sqrt(pi)` <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>. This elegantly explains the presence of `sqrt(pi)` in the normalization constant for the [[normal_distribution_and_its_characteristics | normal distribution]] <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

## Herschel's Derivation of the [[gaussian_distribution_and_the_role_of_pi | Gaussian Distribution]]

While beautiful, this proof might feel like a "trick" <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>. To address the statistician's friend's question about circles and population statistics, we turn to [[herschels_derivation_of_the_gaussian_distribution | John Herschel's derivation]] of the [[gaussian_distribution_and_the_role_of_pi | Gaussian distribution]] in 1850 <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.

Herschel showed that if a 2D [[integrals_and_probability_distributions | probability distribution]] (like hits on a dartboard) satisfies two reasonable properties, it *must* have the shape `e^(-(x^2+y^2))` <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>:

1.  **Radial Symmetry**: The probability density around any point depends only on its distance from the origin (`r`), not its direction <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>. Mathematically, `f(x,y)` can be expressed as `f(r)`, where `r = sqrt(x^2+y^2)` <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>. This property inherently involves circles.
2.  **Independence of Coordinates**: The `x` and `y` coordinates are independent of each other <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>. This means the 2D function can be factored into a function of `x` only and a function of `y` only: `f(x,y) = g(x) * h(y)` <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. Given radial symmetry, `g(x)` and `h(y)` must be the same function, say `g(x)` and `g(y)` <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.

Combining these properties leads to a functional equation: `f(sqrt(x^2+y^2)) = g(x) * g(y)` <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>. After some manipulation and assuming `f` and `g` are proportional (or the same, for simplicity in deduction), the equation becomes `f(sqrt(x^2+y^2)) = f(x) * f(y)` <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.

Solving this functional equation reveals that the only continuous function satisfying this property is an exponential function <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>. Specifically, it forces the function `f` to be of the form `e^(C*x^2)` for some constant `C` <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>. For the function to represent a valid [[integrals_and_probability_distributions | probability distribution]] (i.e., with a finite volume under the curve that can be normalized to one), the constant `C` must be negative <a class="yt-timestamp" data-t="00:21:18">[00:21:18]</a>.

This derivation, also independently discovered by James Clerk Maxwell for gas molecule velocities <a class="yt-timestamp" data-t="00:21:34">[00:21:34]</a>, explains why the [[gaussian_distribution_and_the_role_of_pi | Gaussian distribution]] naturally takes the `e^(-x^2)` form. Furthermore, it makes the "trick" of bumping the problem to 2D less arbitrary <a class="yt-timestamp" data-t="00:22:10">[00:22:10]</a>. The core of the proof leverages the very properties (radial symmetry and independence of axes) that define a [[gaussian_distribution_and_the_role_of_pi | Gaussian distribution]] according to Herschel-Maxwell <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a>.

## Connecting to the [[central_limit_theorem_basics_and_applications | Central Limit Theorem]]

Despite the elegance of Herschel's derivation, it still implicitly assumes a multi-dimensional or spatial context <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>. The [[normal_distribution_and_its_characteristics | normal distribution]] more commonly arises in practice through the [[central_limit_theorem_basics_and_applications | Central Limit Theorem]], which deals with the sum of many independent variables, a process that doesn't feel inherently spatial or geometric <a class="yt-timestamp" data-t="00:23:24">[00:23:24]</a>.

The final challenge, therefore, is to explain why the function characterized by the Herschel-Maxwell derivation (based on spatial properties) is the same function that forms the heart of the [[central_limit_theorem_basics_and_applications | Central Limit Theorem]] (based on sums of variables) <a class="yt-timestamp" data-t="00:23:30">[00:23:30]</a>. This deeper connection is a topic for further exploration <a class="yt-timestamp" data-t="00:23:46">[00:23:46]</a>.