---
title: Holomorphic dynamics and complex functions
videoId: LqbZpur38nw
---

From: [[3blue1brown]] <br/> 

Holomorphic dynamics is a field of mathematics that studies the repeated application of certain types of functions, often leading to intricate fractal patterns <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This field is intimately tied to concepts like the [[mandelbrot_set | Mandelbrot set]] and [[newtons_fractal | Newton's fractal]] <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Holomorphic Functions

The term "holomorphic" refers to functions that take [[complex_plane_and_exponential_functions | complex number]] inputs and produce [[complex_plane_and_exponential_functions | complex number]] outputs <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>, and for which a derivative can be taken <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Geometrically, having a derivative in this context means that when zoomed in near a point, the function's behavior looks approximately like scaling and rotating, similar to multiplying by a complex constant <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. This category includes most ordinary functions such as polynomials, exponentials, and [[trigonometry_and_complex_numbers | trig functions]] <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

## Dynamics: Repeated Application

The "dynamics" in the title refers to repeatedly applying one of these functions: evaluating on an input, then evaluating the same function on the output, and so on <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. The sequence of points generated can exhibit various behaviors:
*   **Cycles**: The pattern of points gets trapped in a cycle <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   **Limiting points**: The sequence approaches a specific point <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>, including "infinity" as a limit point <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
*   **Chaos**: The sequence has no pattern and behaves chaotically <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

What's surprising is that visualizing these different behaviors often results in intricate fractal patterns <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

## Newton's Fractal Example

An example of this is [[newtons_fractal | Newton's method]], an algorithm for finding the roots of a polynomial *p* <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. The method repeatedly iterates the expression `x - p(x) / p'(x)` <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. When applied in the [[complex_plane_and_exponential_functions | complex plane]], by coloring points based on which root they converge to, the results are intricate pictures with rough fractal boundaries <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. The function iterated in Newton's method is a [[complex_functions_and_transformations | rational function]] (one polynomial divided by another) <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. Mathematicians Pierre Fatou and Gaston Julia extensively studied the iteration of these rational functions in the early 20th century <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

## The Mandelbrot Set

The most well-known example of iterating a [[complex_functions_and_transformations | rational function]] is `z^2 + c`, where *c* is a constant <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. For the [[mandelbrot_set | Mandelbrot set]], the initial value of *z* is always zero, and the constant *c* is varied <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. Points in the [[complex_plane_and_exponential_functions | complex plane]] corresponding to *c* are colored black if the iteration `z_new = z_old^2 + c` remains bounded (i.e., doesn't "blow up" to infinity) <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. Different colors can be used to indicate how quickly divergent values rush off to infinity <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

The [[mandelbrot_set | Mandelbrot set]] is a *parameter space* <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>, meaning each pixel represents a different function (defined by *c*). Different sections of the [[mandelbrot_set | Mandelbrot set]] correspond to specific dynamic behaviors:
*   The largest cardioid section contains *c* values where the process converges to a limit <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
*   The large circle on the left represents *c* values where the process gets trapped in a 2-cycle <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
*   Smaller circles represent cycles of higher periods <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

## Julia Sets

In contrast to the [[mandelbrot_set | Mandelbrot set]], [[julia_sets | Julia sets]] are constructed by fixing *c* and varying the initial value *z_0* <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. Each [[julia_sets | Julia set]] image corresponds to a single function <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. The term "Julia set" specifically refers to the boundaries of these regions, not their interior <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

## Fixed Points and Stability

To understand the dynamics, mathematicians first look for simple behaviors, such as **fixed points** where `f(z) = z` <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. For [[newtons_fractal | Newton's method]], the roots of the polynomial are fixed points <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. Any [[complex_functions_and_transformations | rational function]] will have fixed points, as finding them is equivalent to finding the roots of a polynomial expression <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

A crucial concept is **stability**:
*   A fixed point is **attracting** if nearby points converge towards it <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.
*   A fixed point is **repelling** if nearby points are pushed away <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.

The stability of a fixed point can be determined by the absolute value of the function's derivative at that point <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
*   If `|f'(z)| < 1`, the fixed point is attracting <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.
*   If `|f'(z)| > 1`, the fixed point is repelling <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.

The derivative of complex functions has a lovely [[geometric_representation_of_complex_numbers | geometric interpretation]]: it describes how a small neighborhood around an input scales and rotates when the function is applied <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. For [[newtons_fractal | Newton's method]], the derivative at a root is 0, making roots **super-attracting fixed points** <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a> because neighborhoods shrink significantly around them, reflecting the algorithm's goal of rapid convergence <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.

## Cycles

Beyond fixed points, dynamics can involve **cycles**, where `f(f(...f(z)...)) = z` after *n* iterations, forming an n-cycle <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>. The number of such periodic points grows exponentially with *n* <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>. These cycles can also be attracting or repelling. An **attracting cycle** means a neighborhood of points around a value in the cycle is pulled into it <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>. For [[newtons_fractal | Newton's method]], the existence of an attracting cycle means there's a non-zero chance that an initial guess gets trapped and never finds a root <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>. An example is `z^3 - 2z + 2`, which has an attracting 2-cycle between 0 and 1 <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>.

## The Mandelbrot Set Appears in Other Contexts

A fascinating aspect of holomorphic dynamics is the reappearance of the [[mandelbrot_set | Mandelbrot set]] in different contexts. For [[newtons_fractal | Newton's method]] applied to cubic polynomials, one can visualize which polynomials have attracting cycles <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>.

This relies on **Fatou's theorem**, which states that if a [[complex_functions_and_transformations | rational map]] has an attracting cycle, then at least one value where the derivative of the iterated function is zero must fall into that cycle <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>. For cubic polynomials, this means checking only the "center of mass" (average of the three roots) of the polynomial is sufficient to determine if an attracting cycle exists <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>.

By fixing two roots (e.g., at -1 and 1) and varying the third root (lambda) in the [[complex_plane_and_exponential_functions | complex plane]], a *parameter space* can be created <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>. Coloring pixels based on whether this "center of mass" point results in an attracting cycle reveals a shape identical to the [[mandelbrot_set | Mandelbrot set]] <a class="yt-timestamp" data-t="00:20:43">[00:20:43]</a>. This suggests the [[mandelbrot_set | Mandelbrot set]] relates to a more general and universal property of parameter spaces in iterative processes <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>.

## Why Fractals? Julia Sets and Chaos

The intricate fractal nature of these diagrams is linked to the concept of chaos.
*   The **Fatou set** of an iterated function comprises points that eventually fall into some stable, predictable pattern <a class="yt-timestamp" data-t="00:22:29">[00:22:29]</a>.
*   The **Julia set** is everything else: the rough boundaries between colored regions <a class="yt-timestamp" data-t="00:22:41">[00:22:41]</a>. It includes all repelling cycles and fixed points <a class="yt-timestamp" data-t="00:22:53">[00:22:53]</a>. Points in the [[julia_sets | Julia set]] typically behave chaotically, meaning nearby neighbors eventually diverge into qualitatively different behaviors <a class="yt-timestamp" data-t="00:23:35">[00:23:35]</a>.

A surprising result, a corollary to Montel's theorem, is the "stuff-goes-everywhere principle" <a class="yt-timestamp" data-t="00:24:02">[00:24:02]</a>. If a small disk is drawn around a point on the [[julia_sets | Julia set]], as the process plays out, that disk eventually expands to cover nearly every point on the [[complex_plane_and_exponential_functions | complex plane]] (with at most two exceptions) <a class="yt-timestamp" data-t="00:23:53">[00:23:53]</a>. This means that if there are multiple attractive behaviors (like roots or cycles), points from any tiny disk on the [[julia_sets | Julia set]] will eventually fall into *all* of them <a class="yt-timestamp" data-t="00:25:04">[00:25:04]</a>.

This property explains why the boundaries of these diagrams are not smooth <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>. If a boundary were smooth, a small circle could touch only two colors; however, if there are three or more attractive behaviors, the "stuff-goes-everywhere" principle dictates that any point on the boundary must be arbitrarily close to points leading to *all* possible behaviors, implying a rough, fractal shape <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>. While the [[julia_sets | Julia set]] often has an area of zero, there are cases where it can be the entire plane, meaning everything behaves chaotically <a class="yt-timestamp" data-t="00:26:06">[00:26:06]</a>.

The connection between chaos and fractal geometry is fundamental in holomorphic dynamics <a class="yt-timestamp" data-t="00:26:20">[00:26:20]</a>. The quantification of chaotic behavior directly leads to an explanation for the rough, fractal shape of these mathematical objects <a class="yt-timestamp" data-t="00:26:45">[00:26:45]</a>.