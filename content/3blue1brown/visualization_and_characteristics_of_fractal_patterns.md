---
title: Visualization and characteristics of fractal patterns
videoId: -RdOwhmqP5s
---

From: [[3blue1brown]] <br/> 

Fractal patterns are complex, intricate shapes that exhibit infinite detail upon zooming in <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. The patterns discussed here relate to an infinite family of [[newtons_fractal_and_its_relation_to_polynomials | fractals]] derived from [[mathematical_concepts_related_to_newtons_fractal | Newton's method]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Unlike many [[benoit_mandelbrot_and_the_pragmatic_origins_of_fractal_geometry | other fractals]], these patterns have a pragmatic starting point <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>, reflecting the complexity of an algorithm widely used in engineering <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Solving Polynomial Equations: A Pragmatic Origin

The core problem leading to these [[fractal geometry | fractals]] is finding when a polynomial equals zero, also known as finding its roots <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. This question is fundamental in engineering <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>, particularly in computer graphics <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. For instance, rendering text on screen involves solving equations based on polynomial curves known as Bezier curves <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. Determining whether a pixel should be colored requires calculating its distance from these curves, which itself can be expressed as a polynomial <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. Finding the minimum of this distance involves setting its derivative (another polynomial) to zero <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. Thus, a systematic way to find polynomial roots is highly valuable <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

While quadratic, cubic, and quartic polynomials have exact formulas for their roots <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>, polynomials of degree five or more generally do not have analogous formulas using standard functions <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. This is known as the unsolvability of the quintic <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. In practice, algorithms are used to approximate these solutions <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

## [[mathematical_concepts_related_to_newtons_fractal | Newton's Method]]

[[mathematical_concepts_related_to_newtons_fractal | Newton's method]] (also known as the [[mathematical_concepts_related_to_newtons_fractal | Newton-Raphson method]]) is a common algorithm for approximating polynomial roots <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

The algorithm proceeds as follows:
1.  **Initial Guess** Begin with a random guess, `x0` <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
2.  **Linear Approximation** Draw a tangent line to the polynomial's graph at `x0` <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
3.  **New Guess** The point where this tangent line crosses the x-axis becomes the next guess, `x1` <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. This is calculated by `x1 = x0 - P(x0)/P'(x0)` where `P(x)` is the polynomial and `P'(x)` is its derivative <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
4.  **Iteration** Repeat the process, using the new guess as the starting point <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.

The method converges quickly if the initial guess is near a root <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. However, if the initial guess is far from a root, the sequence of guesses can bounce around or behave unpredictably before, if ever, converging to a root <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.

## [[newtons_fractal_and_its_relation_to_polynomials | Newton's Fractal]] in the Complex Plane

The fascinating visual patterns emerge when [[mathematical_concepts_related_to_newtons_fractal | Newton's method]] is applied to polynomials with complex number inputs and outputs <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>. While the visual interpretation of tangent lines no longer applies, the underlying formula for the next guess remains valid in the complex plane <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

When many different initial complex guesses are subjected to [[mathematical_concepts_related_to_newtons_fractal | Newton's method]], most quickly converge to one of the polynomial's true (complex) roots <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>. However, some initial guesses, called "stragglers," bounce around for a while <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.

To visualize this, each starting point (pixel) in the complex plane is colored based on which of the polynomial's roots it ultimately converges to <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>. The resulting image, known as [[newtons_fractal_and_its_relation_to_polynomials | Newton's fractal]], reveals an endlessly complex pattern with infinite detail as more iterations are allowed <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>.

### Characteristics of [[newtons_fractal_and_its_relation_to_polynomials | Newton's Fractal]]

*   **Infinite Detail and Complexity** The fine details of the shape continue with endless complexity, meaning any resolution is insufficient to capture its full intricacy <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>. This complexity arises from the simple rule of repeatedly solving linear approximations <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>.
*   **Unpredictability and Sensitivity** The fractal demonstrates that in certain regions of the complex plane, a minuscule adjustment to the initial guess can completely change which root the method converges to <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>. This highlights the unpredictable nature of the root-finding algorithm in specific initial value ranges <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.
*   **The "All or Nothing" Boundary Property** A peculiar property of these [[fractal geometry | fractal]] diagrams (for polynomials with three or more roots) is that the boundary of any one colored region is precisely the same set as the boundary of all other colored regions <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a> <a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>.
    *   A point is on the boundary of a set if any arbitrarily small circle drawn around it contains points both inside and outside the set <a class="yt-timestamp" data-t="00:18:36">[00:18:36]</a>.
    *   This implies that any small circle either contains all colors (if it encompasses part of the shared boundary) or just one color (if it's in the interior of a region) <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>. It's impossible to find a circle containing only two colors <a class="yt-timestamp" data-t="00:19:30">[00:19:30]</a>.
    *   This property forces the boundary to consist entirely of sharp corners, explaining why it remains rough regardless of zoom level <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a> <a class="yt-timestamp" data-t="00:21:23">[00:21:23]</a>.
    *   The [[fractal_dimension_and_its_implications | fractal dimension]] of such a boundary can be measured (e.g., around 1.44 for the shown example) <a class="yt-timestamp" data-t="00:21:30">[00:21:30]</a> <a class="yt-timestamp" data-t="00:21:33">[00:21:33]</a>.
*   **Comparison to Voronoi Diagrams** If the coloring were simply based on the closest root without applying [[mathematical_concepts_related_to_newtons_fractal | Newton's method]], the result would be a Voronoi Diagram with straight-line boundaries <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>. The [[newtons_fractal_and_its_relation_to_polynomials | Newton's fractal]] dramatically deviates from this simple expectation.
*   **Impact of Polynomial Degree**
    *   **Cubic (3+ roots):** Similar to quintic polynomials, cubic polynomials also produce [[fractal geometry | fractal]] patterns with infinite detail when [[mathematical_concepts_related_to_newtons_fractal | Newton's method]] is applied in the complex plane <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>.
    *   **Quadratic (2 roots):** Quadratic polynomials behave differently. Each initial guess tends to the closest root, resulting in a diagram with a decidedly simpler, less complex boundary (a single line of points at equal distance from each root) <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a> <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a>. This is because a smooth boundary between two colors is permissible, unlike the three-color case <a class="yt-timestamp" data-t="00:22:48">[00:22:48]</a>. The complexity appears to arise when transitioning from two to three roots <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>.

## Historical Context and Future Questions

Although the method is named after Newton, he had no knowledge of these complex [[fractal geometry | fractal]] images that can be generated with modern technology <a class="yt-timestamp" data-t="00:23:38">[00:23:38]</a>. This phenomenon highlights how simple ideas, discovered centuries ago, can contain new angles or domains of relevance that await discovery much later <a class="yt-timestamp" data-t="00:24:10">[00:24:10]</a>.

The study of such dynamics falls under the field of holomorphic dynamics <a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a> <a class="yt-timestamp" data-t="00:23:26">[00:23:26]</a>. Further exploration into whether the process gets trapped in a cycle reveals surprising connections with the [[benoit_mandelbrot_and_the_pragmatic_origins_of_fractal_geometry | Mandelbrot set]] <a class="yt-timestamp" data-t="00:24:46">[00:24:46]</a> <a class="yt-timestamp" data-t="00:24:50">[00:24:50]</a>.