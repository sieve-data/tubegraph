---
title: Mathematical concepts related to Newtons fractal
videoId: -RdOwhmqP5s
---

From: [[3blue1brown]] <br/> 

Newton's fractal is not just an intricate shape with infinite detail <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>; it represents a pragmatic starting point in mathematics, reflecting the complexity of an algorithm used widely in engineering <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This fractal illustrates the behavior of [[understanding_newtons_method_and_its_applications | Newton's method]] when applied to finding roots of polynomials in the complex plane <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## The Quest for Polynomial Roots

The primary objective that leads to Newton's fractal is determining when a polynomial equals zero, also known as finding its roots <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. This seemingly academic question is crucial in engineering, particularly in computer graphics <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

### Applications in Computer Graphics
Polynomials are extensively used in computer graphics <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. For instance, rendering text on a screen involves fonts defined by polynomial curves, specifically Bezier curves <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. Displaying these curves requires determining which pixels should be colored in <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. This involves calculating the distance from a pixel to the mathematical curve, where the square of that distance is itself a polynomial <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. Finding the minimum of this distance function, a classic calculus problem, leads to solving for the zeros of its derivative (which is also a polynomial) <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

### Limitations of Direct Formulas
While quadratic functions have a well-known formula for their roots <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a> (used trillions of times in films like *Coco* <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>), higher-order polynomials become much trickier <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. Cubic and quartic polynomials also have formulas, though the quartic formula is rarely used in practice due to its complexity <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. However, for polynomials of degree five or more, no analogous general formula exists that combines standard functions to always yield a root, a concept known as the unsolvability of the quintic <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. In practice, algorithms are used to approximate solutions <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

## [[understanding_newtons_method_and_its_applications | Newton's Method]]

[[understanding_newtons_method_and_its_applications | Newton's method]] is a common algorithm for approximating solutions to equations <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

### The Algorithm
The procedure starts with an initial guess, x₀ <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. To improve the guess, the method asks where a linear approximation (a tangent line) to the function at the current guess crosses the x-axis <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. This intersection point becomes the next guess <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

The step size for the next guess is calculated by dividing the polynomial's value at the current guess (P(x)) by its derivative at that point (P'(x)) <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. The next guess, x₁, is the previous guess adjusted by this step size: x₁ = x₀ - P(x₀)/P'(x₀) <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>. This process is repeated iteratively until the guess is extremely close to a true root <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

### History
Originally developed by Isaac Newton, the method was simplified and published by Joseph Raphson, leading to its common name, the Newton-Raphson method <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

### Challenges in the Real Plane
While generally effective, [[understanding_newtons_method_and_its_applications | Newton's method]] can be sensitive to the initial guess <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. If an initial guess is far from a root, the sequence of guesses might bounce around without converging to a root, or only doing so by chance <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

## [[newtons_fractal_and_roots_of_polynomial_equations | Newton's Method in the Complex Plane]] and Fractals

The true complexity of [[understanding_newtons_method_and_its_applications | Newton's method]] emerges when applied to finding roots in the complex plane <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. According to the fundamental theorem of algebra, any polynomial can be factored into terms corresponding to its roots if complex numbers are allowed <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

In the complex plane, the visual analogy of tangent lines and graphs no longer applies <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>. However, the algebraic formula for [[understanding_newtons_method_and_its_applications | Newton's method]] remains valid <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>. When applied to many different initial guesses in the complex plane, most points quickly converge to one of the true roots <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>. However, some "stragglers" bounce around chaotically before eventually converging <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.

### [[newtons_fractal_and_roots_of_polynomial_equations | Newton's Fractal]] Generation
To visualize this, each initial guess (represented as a dot or pixel in the complex plane) is colored based on which of the polynomial's roots it ultimately converges to <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>. When this process is applied to every pixel at high resolution, the result is [[newtons_fractal_and_its_relation_to_polynomials | Newton's fractal]] <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>.

This fractal reveals regions where a tiny adjustment to an initial guess can drastically change which root it converges to <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>. This highlights the unpredictable nature of the root-finding algorithm, with "whole swaths of initial values" exhibiting this unpredictability <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.

## [[visualization_and_characteristics_of_fractal_patterns | Characteristics of Newton's Fractal]]

### Dynamic Nature
The appearance of [[newtons_fractal_and_its_relation_to_polynomials | Newton's fractal]] changes based on the specific polynomial (i.e., the placement of its roots) <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>. Regions close to a root consistently converge to that root, appearing as solid color areas <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>. The chaos and intricate patterns are concentrated at the boundaries between these regions <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>. These fractal boundaries are a general characteristic for any given polynomial <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>.

### Effect of Iterations
The number of steps (iterations) in [[understanding_newtons_method_and_its_applications | Newton's method]] affects the intricacy of the generated image <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>:
*   **Zero steps**: Each point is colored based on the closest root, forming a Voronoi Diagram with straight-line boundaries <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.
*   **More steps**: As more iterations are allowed, the image becomes progressively more intricate, approaching the full fractal in the limit of an arbitrarily large number of iterations <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>.

### The "Shared Boundary" Property
A peculiar property of [[newtons_fractal_and_its_relation_to_polynomials | Newton's fractal]] with three or more roots is that the boundary of any one color region is precisely the same set as the boundary of all other color regions <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>. This means if you draw a small circle anywhere on the boundary, it will always contain points belonging to *all* the colors <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a>. It is impossible to find a circle that contains only two of the colors <a class="yt-timestamp" data-t="00:19:30">[00:19:30]</a>. This property mandates that the boundary cannot be smooth, or even partially smooth; it must consist entirely of "sharp corners," explaining its rough, infinitely detailed nature <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>.

The [[the_application_and_computation_of_fractal_dimensions_in_nature | fractal dimension]] of such a boundary can be measured; for a specific example, it was found to be around 1.44 <a class="yt-timestamp" data-t="00:21:30">[00:21:30]</a>. This "shared boundary" implies that if a point is in a sensitive region where nearby initial values diverge to different roots, then *every* possible root must be accessible from within that small neighborhood <a class="yt-timestamp" data-t="00:21:48">[00:21:48]</a>.

### The Quadratic Exception
For quadratic polynomials, which have only two roots, the behavior is different <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>. Each initial guess tends towards whichever root it's closest to, resulting in a simple, non-fractal diagram with a straight-line boundary <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>. This is because a smooth boundary is permissible with only two colors, as the shared boundary property does not force the complexity <a class="yt-timestamp" data-t="00:22:48">[00:22:48]</a>. The fractal complexity arises when the number of roots jumps from two to three or more <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>.

## Further Exploration

The field of mathematics that studies these kinds of questions is called holomorphic dynamics <a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a>. Exploring whether the iterative process of [[understanding_newtons_method_and_its_applications | Newton's method]] can get trapped in a cycle leads to a surprising connection with the [[Benoit Mandelbrot and the pragmatic origins of fractal geometry | Mandelbrot set]] <a class="yt-timestamp" data-t="00:24:42">[00:24:42]</a>.

It is notable that Newton himself had no knowledge of [[newtons_fractal_and_its_relation_to_polynomials | Newton's fractal]] and could not have visualized these images with his technology <a class="yt-timestamp" data-t="00:23:38">[00:23:38]</a>. This "overextension of nomenclature" is common in mathematics, where simple ideas discovered centuries ago often contain hidden complexities or new domains of relevance that are only discovered much later <a class="yt-timestamp" data-t="00:24:04">[00:24:04]</a>.