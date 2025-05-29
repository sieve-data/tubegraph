---
title: The complexity and unpredictability of root finding algorithms
videoId: -RdOwhmqP5s
---

From: [[3blue1brown]] <br/> 

The study of fractals, often seen as intricately detailed shapes with infinite complexity <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>, surprisingly connects to the practical application of algorithms used in engineering <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This connection is particularly evident in the behavior of root-finding algorithms for polynomials, which can reveal unexpected levels of chaos and unpredictability.

## The Problem of Finding Polynomial Roots

A fundamental challenge in mathematics and engineering is determining when a polynomial equals zero; these values are known as its roots <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>, <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. While seemingly academic, this problem arises frequently in real-world applications <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

### Real-World Applications

One significant area where polynomials are ubiquitous is computer graphics <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. For instance, displaying text on a screen involves fonts defined by polynomial curves, specifically Bezier curves <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>, <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. To render these, a computer must decide which pixels to color in <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. This often boils down to calculating the distance of a pixel from the mathematical curve, a task that involves finding the minimum of a polynomial function <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>, <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. Finding this minimum requires solving for the roots of the function's derivative <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>, <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>, <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

### Limitations of Direct Formulas

While specific formulas exist for lower-degree polynomials:
*   **Quadratic Formula:** Provides exact solutions for degree 2 polynomials <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. This formula is incredibly prevalent, used trillions of times in productions like Pixar's *Coco* for per-pixel calculations <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>, <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **Cubic and Quartic Formulas:** Formulas exist for degree 3 and 4 polynomials, but they are increasingly complex and rarely used in practice due to their "god-awful nightmare" nature <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>, <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>, <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.

A profound result in mathematics is the [[unsolvability_of_the_quintic | unsolvability of the quintic]] <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>, which states that no general algebraic formula exists for finding the roots of polynomials of degree 5 or higher using standard functions <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>, <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. This means that for higher-degree polynomials, approximation algorithms are necessary <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

## Newton's Method: A Pragmatic Approach

[[newtons_fractal_and_roots_of_polynomial_equations | Newton's method]] (also known as the Newton-Raphson method) is a widely used iterative algorithm to approximate polynomial roots to any desired precision <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>, <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

### The Algorithm

1.  **Initial Guess (x0):** Start with an arbitrary initial guess <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
2.  **Linear Approximation:** Calculate the value of the polynomial and its derivative at the current guess <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>, <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
3.  **New Guess (x1):** Determine where the tangent line (linear approximation) at the current guess intersects the x-axis <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>, <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. This intersection point becomes the next, improved guess <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>, <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>, <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
4.  **Iteration:** Repeat the process with the new guess until the desired precision is achieved <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>, <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

The step size is calculated using the function's value and its derivative: `step size = P(x) / P'(x)` <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>, <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. Intuitively, a larger `P(x)` (higher graph) requires a bigger step, but a larger `P'(x)` (steeper graph) means a smaller adjustment <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>, <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.

## The Unexpected Complexity: Fractals in the Complex Plane

While Newton's method converges quickly when starting near a root <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>, its behavior becomes unpredictable when the initial guess is far from a root <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. This is particularly evident when applying the method in the complex plane.

### Behavior with Real vs. Complex Numbers

For real-valued functions, an initial guess far from a root can lead to the sequence of guesses bouncing around or "getting lost" in areas where the linear approximation is not useful, eventually only converging to a true root by chance <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>, <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>, <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

However, polynomials always have roots in the complex plane, as stated by the fundamental theorem of algebra <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>, <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. When extending Newton's method to complex inputs, the visual intuition of tangent lines is lost <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>, <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>, but the algebraic formula still applies <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.

### The Emergence of Newton's Fractal

When applying Newton's method to a grid of initial complex guesses, most points converge quickly to one of the true roots <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>, <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>. However, some points, particularly those on the real number line previously identified as problematic, bounce around for longer <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>, <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.

By coloring each initial guess based on which root it ultimately converges to, and then reverting the points to their starting positions, a stunning fractal pattern emerges <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>, <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>, <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. This image, known as [[newtons_fractal_and_roots_of_polynomial_equations | Newton's fractal]], displays infinite detail <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>, <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>, <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>.

The fractal reveals regions where a minuscule adjustment to the initial guess can completely alter which root it converges to <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>. This highlights the inherent unpredictability of the root-finding algorithm and the existence of vast areas of initial values that lead to such chaotic behavior <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.

Changing the polynomial (by moving its roots) alters the resulting fractal pattern <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>, <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>. The regions immediately around a root consistently show the same color, indicating stable convergence <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>, <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>. All the chaos occurs at the boundaries between these regions <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>, and these fractal boundaries appear to be a general characteristic for any polynomial with three or more roots <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>, <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>, <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>.

The intricacy of the fractal increases with the number of iterations of Newton's method <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>, <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>, <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>. The true fractal is the limit as the number of iterations approaches infinity <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.

## The Boundary Property and its Implications

A key property of these fractals is that the boundary of any one colored region (i.e., the set of points that converge to a specific root) is precisely the same as the boundary of all other colored regions <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>, <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>, <a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>.

A point is on the boundary of a set if any tiny circle drawn around it contains points both inside and outside the set <a class="yt-timestamp" data-t="00:18:36">[00:18:36]</a>, <a class="yt-timestamp" data-t="00:18:39">[00:18:39]</a>, <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>. This means that at any boundary point, a small circle will contain points converging to *all* possible roots, not just two <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>, <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>, <a class="yt-timestamp" data-t="00:19:30">[00:19:30]</a>.

This "all or nothing" boundary property implies that the boundaries cannot be smooth, or even partially smooth <a class="yt-timestamp" data-t="00:21:06">[00:21:06]</a>, <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>. Any smooth segment would only touch two colors, which is forbidden by the property <a class="yt-timestamp" data-t="00:21:15">[00:21:15]</a>. Instead, the boundary must consist entirely of sharp corners and exhibit a "blobs on blobs on blobs" pattern, explaining its endless roughness when zoomed in <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>, <a class="yt-timestamp" data-t="00:20:53">[00:20:53]</a>, <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>, <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>.

This implies that if you're near a sensitive point where seed values could go to one root, they could, in fact, access *any* of the possible roots from that small neighborhood <a class="yt-timestamp" data-t="00:21:48">[00:21:48]</a>, <a class="yt-timestamp" data-t="00:21:56">[00:21:56]</a>, <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>.

### Why Three Roots Make a Difference

The fractal boundary complexity appears when there are three or more roots <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>. For quadratic polynomials (with only two roots), the boundary is a single line of points equidistant from each root, and the resulting diagram is much simpler, resembling a Voronoi Diagram with straight-line boundaries <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>, <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>, <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>, <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>. This aligns with the boundary property, as a smooth boundary is permissible when only two colors (roots) are involved <a class="yt-timestamp" data-t="00:22:48">[00:22:48]</a>, <a class="yt-timestamp" data-t="00:22:51">[00:22:51]</a>.

The field of holomorphic dynamics studies these kinds of questions, delving into why such complex behaviors arise from seemingly simple iterative processes <a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a>, <a class="yt-timestamp" data-t="00:23:26">[00:23:26]</a>.

## Enduring Relevance

Despite being named "Newton's fractal," Isaac Newton himself could not have conceived of these images with the technology of his time <a class="yt-timestamp" data-t="00:23:38">[00:23:38]</a>, <a class="yt-timestamp" data-t="00:23:41">[00:23:41]</a>. This highlights a recurring theme in mathematics: simple ideas discovered centuries ago often contain new angles or domains of relevance that await future discovery <a class="yt-timestamp" data-t="00:24:10">[00:24:10]</a>, <a class="yt-timestamp" data-t="00:24:14">[00:24:14]</a>. Unasked questions about seemingly "old news" mathematics, like whether Newton's method can get trapped in a [[cycling_behaviors_using_roots_of_unity | cycle]], continue to reveal surprising connections, such as with the Mandelbrot set <a class="yt-timestamp" data-t="00:24:25">[00:24:25]</a>, <a class="yt-timestamp" data-t="00:24:42">[00:24:42]</a>, <a class="yt-timestamp" data-t="00:24:46">[00:24:46]</a>, <a class="yt-timestamp" data-t="00:24:50">[00:24:50]</a>.