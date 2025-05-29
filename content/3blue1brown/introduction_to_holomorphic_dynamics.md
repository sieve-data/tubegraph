---
title: Introduction to Holomorphic Dynamics
videoId: LqbZpur38nw
---

From: [[3blue1brown]] <br/> 

[[introduction_to_partial_differential_equations | Holomorphic dynamics]] is a field of mathematics that studies phenomena such as the Mandelbrot set <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. A primary goal in studying this field is to demonstrate how iconic shapes, like the Mandelbrot set, emerge in a more general way than their initial definitions might suggest <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This field is closely related to concepts like Newton's fractal, discussed previously <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Defining Holomorphic Dynamics

The term "holomorphic" refers to functions that take [[introduction_to_complex_numbers | complex number]] inputs and produce [[introduction_to_complex_numbers | complex number]] outputs <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>, and for which one can also take a [[introduction_to_derivatives_and_calculus_concepts | derivative]] <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. In this context, having a [[introduction_to_derivatives_and_calculus_concepts | derivative]] means that when zooming in on the function's behavior near a given point, it appears roughly as a scaling and rotating operation, like multiplying by some [[introduction_to_complex_numbers | complex constant]] <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. Most common functions, such as polynomials, exponentials, and trigonometric functions, are included in this category <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

The "dynamics" aspect of the title refers to repeatedly applying one of these functions over and over <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>, by evaluating the function on an input, then on its output, and so on <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. The patterns of points emerging from this iteration can exhibit several behaviors:
*   Becoming trapped in a cycle <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   Approaching a limiting point <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
*   Growing infinitely large (approaching the "point at infinity") <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
*   Behaving chaotically with no discernible pattern <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

A surprising outcome is that for many functions, visualizing these behaviors often results in intricate fractal patterns <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

## Notable Examples

### Newton's Fractal
Newton's method is an algorithm for finding the roots of a polynomial *p* <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. It works by repeatedly iterating the expression `x - p(x) / p'(x)`, where `p'` is the [[introduction_to_derivatives_and_calculus_concepts | derivative]] of *p* <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. When the initial seed value is near a root, this procedure rapidly converges to that root <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

When Newton's method is applied in the [[introduction_to_complex_numbers | complex plane]], different initial seed values are colored based on which root they converge to <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. The resulting images are highly intricate, featuring rough fractal boundaries between the colored regions <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

The function iterated in Newton's method (e.g., for `z^3 - 1`) can be rewritten as one polynomial divided by another, which mathematicians call rational functions <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. Mathematicians Pierre Fatou and Gaston Julia studied the iteration of such rational functions in the years following World War I <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

### The Mandelbrot Set
The most widely known example of a rational function studied for its fractal dynamics is `z^2 + c`, where `c` is a constant <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. For the Mandelbrot set, the process always begins with an initial value of `z = 0` <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. The behavior of the iterated sequence `0, c, c^2 + c, (c^2+c)^2 + c, ...` is observed <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

*   If the process remains bounded (e.g., stays within a visible range), the corresponding point `c` is colored black <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   If the sequence diverges to infinity (e.g., gets larger than 2), the point `c` is colored with a gradient based on its divergence speed <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.

This coloring scheme produces the iconic Mandelbrot set <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. The Mandelbrot set is a "parameter space" because `c` (the parameter) is varied while the initial `z` is fixed <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. Different parts of the Mandelbrot set correspond to different types of stable behavior:
*   The largest cardioid represents values of `c` where the process converges to a limit <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
*   The large circle on the left indicates values where the process enters a two-value cycle <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
*   Smaller circles represent cycles of three values, and so on <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

### Julia Sets
In contrast to the Mandelbrot set, Julia sets are generated by fixing the parameter `c` and varying the initial seed value `z_0` across the complex plane <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. Each pixel corresponds to a different initial value, and the function (`z^2 + c` for a fixed `c`) remains constant <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. Pixels are colored black if the process remains bounded, and with a gradient if they diverge <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.

While often used to refer to the black region for `z^2 + c`, the term "Julia set" has a more general definition, referring specifically to the boundaries of these regions, not their interiors <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

## Understanding the Dynamics: Fixed Points and Stability

To understand complex systems like these, mathematicians often start by identifying parts with simple behavior <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

### Fixed Points
A fixed point of a function `f(z)` is a value where `f(z) = z` <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
For Newton's method functions, the roots of the polynomial are fixed points <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. Any rational function will have fixed points, as finding them can be rearranged into finding the roots of a polynomial, which are guaranteed by the fundamental theorem of algebra <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

### Stability
A crucial concept for understanding the full dynamics is stability <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>:
*   An attracting fixed point draws nearby points towards it <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.
*   A repelling fixed point pushes nearby points away <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.

This stability can be computed using the [[introduction_to_derivatives_and_calculus_concepts | derivative]] of the function <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. For complex functions, computing [[introduction_to_derivatives_and_calculus_concepts | derivatives]] is symbolically similar to real functions <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>. Geometrically, the [[introduction_to_derivatives_and_calculus_concepts | derivative]] `f'(z)` at a point `z` indicates how a small neighborhood around `z` scales and rotates when `f(z)` is applied <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.

*   If the absolute value of the [[introduction_to_derivatives_and_calculus_concepts | derivative]] at a fixed point is less than 1, the fixed point is attracting <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.
*   If the absolute value is greater than 1, the fixed point is repelling <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.

For Newton's map, at a root (fixed point), the [[introduction_to_derivatives_and_calculus_concepts | derivative]] is 0 <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>. These are called "super-attracting" fixed points because nearby neighborhoods shrink significantly <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>, consistent with Newton's method's goal of rapid convergence to roots <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>. The main cardioid of the Mandelbrot set corresponds to values of `c` where at least one fixed point of `z^2 + c` is attracting <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.

### Cycles
Beyond fixed points, one can analyze cycles where `f(f(z)) = z` (two-cycle) or `f_n(z) = z` (n-cycle), where `f_n` is `f` composed with itself `n` times <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>. While explicit expressions for higher-order cycles become complex, the number of such periodic points grows exponentially with `n` <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.

An attracting cycle means that a neighborhood of points around values in that cycle will be pulled in <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>. For Newton's method, attracting cycles are possible, meaning an initial guess might get trapped in a cycle instead of finding a root <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>. For example, for `z^3 - 2z + 2`, a two-cycle between 0 and 1 is attracting <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>.

## Fatou's Theorem and the Universal Mandelbrot Set
A key result by Fatou states that if a rational map has an attracting cycle, at least one of the values where the [[introduction_to_derivatives_and_calculus_concepts | derivative]] of the iterated function equals zero must fall into that cycle <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>. This implies that if a stable cycle exists, a specific "critical point" (where the [[introduction_to_derivatives_and_calculus_concepts | derivative]] is zero) will find it <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>. This justifies why the Mandelbrot set uses a single seed value (`z = 0`), as it is sufficient to capture all stable cycles <a class="yt-timestamp" data-t="00:18:26">[00:18:26]</a>.

For Newton's method applied to cubic polynomials (with two roots fixed at -1 and 1), there's a "magical fact" that if an attracting cycle exists, the seed value at the center of mass of the three roots (which is the critical point in this case) will fall into that cycle <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>. By coloring a parameter space (where the third root, lambda, varies) based on whether this specific midpoint yields an attracting cycle, the Mandelbrot set re-emerges <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>. This appearance of the Mandelbrot set in such a different context suggests it relates to something more general and universal about parameter spaces in iterative processes <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>.

## Chaos and Fractal Boundaries
A central question is why these processes result in fractals at all <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>.
For Newton's method, any small circle drawn around the boundary of a colored region must contain all available colors from the picture <a class="yt-timestamp" data-t="00:21:16">[00:21:16]</a>. This "all colors" property is true more generally for any rational map: tiny circles either contain points with only one limiting behavior, or all of them <a class="yt-timestamp" data-t="00:21:30">[00:21:30]</a>. If there are at least three colors, this implies the boundary cannot be smooth, as a smooth segment would allow for a small circle touching only two colors <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>.

### Fatou Sets vs. Julia Sets
Two important terms clarify the behavior of points:
*   **[[analytic_continuation_and_complex_analysis | Fatou set]]**: Points that eventually fall into some stable, predictable pattern <a class="yt-timestamp" data-t="00:22:29">[00:22:29]</a>. Small discs around points in the [[analytic_continuation_and_complex_analysis | Fatou set]] tend to shrink under iteration <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>.
*   **Julia set**: Everything else, corresponding to the rough boundaries between colored regions in the pictures <a class="yt-timestamp" data-t="00:22:41">[00:22:41]</a>. This includes repelling cycles and fixed points <a class="yt-timestamp" data-t="00:22:53">[00:22:53]</a>. A typical point in the Julia set bounces chaotically with no clear pattern <a class="yt-timestamp" data-t="00:22:58">[00:22:58]</a>.

A key result is that if a small disc is drawn around a point on the Julia set, it tends to expand over time as the points within it diverge and behave chaotically <a class="yt-timestamp" data-t="00:23:24">[00:23:24]</a>. This expansion is extreme: the disc eventually covers nearly every point on the [[introduction_to_complex_numbers | complex plane]], with at most two exceptions <a class="yt-timestamp" data-t="00:23:49">[00:23:49]</a>. This is sometimes called the "stuff-goes-everywhere principle" (a corollary to Montel's theorem) <a class="yt-timestamp" data-t="00:24:02">[00:24:02]</a>.

This principle means that if an attractive behavior (like an attracting fixed point or cycle) exists, values from any tiny disc around a Julia set point will eventually fall into that behavior <a class="yt-timestamp" data-t="00:25:04">[00:25:04]</a>. For cases with three or more attracting behaviors, this explains why the Julia set must be complicated and non-smooth <a class="yt-timestamp" data-t="00:25:20">[00:25:20]</a>.

While many Julia sets have zero area (being just boundaries), there are examples where the Julia set is the entire plane, meaning everything behaves chaotically <a class="yt-timestamp" data-t="00:26:02">[00:26:02]</a>. The connection between chaos and fractals in this field is not merely metaphorical; quantifying the chaotic behavior of points directly explains the rough fractal shapes of the boundaries <a class="yt-timestamp" data-t="00:26:20">[00:26:20]</a>.