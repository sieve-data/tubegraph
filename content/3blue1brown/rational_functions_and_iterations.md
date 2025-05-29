---
title: Rational functions and iterations
videoId: LqbZpur38nw
---

From: [[3blue1brown]] <br/> 

Holomorphic dynamics is a field of mathematics that studies the iteration of functions with complex number inputs and outputs <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. This field is particularly known for studying fractal shapes like the Mandelbrot set and Newton's fractal <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Holomorphic Functions
Holomorphic functions are functions that take complex number inputs and produce complex number outputs, and for which a derivative can be taken <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. Geometrically, having a derivative means that when zoomed in near a point, the function's behavior looks like scaling and rotating (multiplication by a complex constant) <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. Most common functions, such as polynomials, exponentials, and trigonometric functions, are holomorphic <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

## Dynamics of Iteration
The "dynamics" in holomorphic dynamics refers to what happens when a function is repeatedly applied <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This means evaluating the function on an input, then evaluating it on the output of the previous step, and repeating the process <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
Possible behaviors of the sequence of points produced include:
*   Becoming trapped in a cycle <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   Approaching a limiting point <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
*   Growing indefinitely and "flying off to infinity" (considered a limit point at infinity by mathematicians) <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
*   Behaving chaotically with no discernible pattern <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

Surprisingly, visualizing these different behaviors often results in intricate fractal patterns <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

### Newton's Fractal as an Example
An example of such a fractal is Newton's fractal, seen in the previous video <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. Newton's method is an algorithm for finding the roots of a polynomial p(x) by repeatedly iterating the expression x - p(x) / p'(x), where p'(x) is the derivative <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. If an initial "seed" value is near a root, the sequence of values quickly converges to that root <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

When this method is applied in the complex plane, different initial seed values can be colored based on which root they converge to <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. This process generates intricate pictures with rough fractal boundaries between the colors <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

The function iterated in Newton's method (e.g., for z³ - 1) can be rewritten as one polynomial divided by another <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. This type of function is called a [[complex_functions_and_transformations | rational function]] <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.

## Rational Functions and Their Iteration
[[complex_functions_and_transformations | Rational functions]] are functions expressed as the ratio of two polynomials <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. Mathematicians Pierre Fatou and Gaston Julia extensively studied the iteration of these functions in the years following World War I, developing a rich theory without the aid of computers <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

### The Mandelbrot Set
The most famous example of iterating a [[complex_functions_and_transformations | rational function]] is `z² + c`, where `c` is a constant <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. The Mandelbrot set is constructed by:
1.  Always starting with an initial value of z = 0 <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
2.  Iterating the function `z² + c` for different values of `c` <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
3.  Coloring points black if the process remains bounded (e.g., doesn't exceed 2 in magnitude) <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
4.  Assigning a gradient of colors to divergent values based on how quickly they fly off to infinity <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

The resulting image is the iconic Mandelbrot set <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
Different parts of the Mandelbrot set represent specific dynamic behaviors for the chosen `c` value:
*   The largest cardioid section contains `c` values where the process eventually converges to a limit <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
*   The large circle on the left corresponds to `c` values where the process gets trapped in a cycle of two values <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
*   Other circles indicate cycles of three or more values <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

### Parameter Space vs. Dynamical Space (Julia Sets)
There's a key distinction in how the Mandelbrot set and Newton fractals are constructed:
*   **Mandelbrot Set (Parameter Space)**: Uses a consistent seed value (z=0) but tweaks the parameter `c`, changing the function itself <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. Each pixel corresponds to a unique function <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
*   **Julia Sets (Dynamical Space)**: Fixes `c` at some constant, and then the pixels represent different possible initial values (z naught) <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. Each image corresponds to a single function <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. The term "Julia set" typically refers to the rough boundaries between regions of different behaviors, rather than the interior regions themselves <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

## Understanding Stability in Dynamics

### Fixed Points
A fundamental concept in understanding dynamics is the **fixed point**, a value `z` where `f(z) = z` (the process stays fixed in place) <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. For functions arising from Newton's method, the roots of the polynomial are fixed points <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. Any [[complex_functions_and_transformations | rational function]] will always have fixed points, as finding them is equivalent to finding the roots of a polynomial expression, which always have solutions according to the [[complex_functions_and_transformations | Fundamental Theorem of Algebra]] <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

### Attracting and Repelling Fixed Points
**Stability** is crucial for understanding the overall dynamics <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>:
*   A fixed point is **attracting** if nearby points tend to get drawn towards it <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.
*   A fixed point is **repelling** if nearby points are pushed away <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.

Stability can be determined by computing the derivative of the function at the fixed point <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>:
*   If the absolute value of the derivative is less than 1, the fixed point is attracting <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.
*   If the absolute value of the derivative is greater than 1, the fixed point is repelling <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.

The derivative of a [[complex_functions_and_transformations | complex function]] geometrically describes local scaling and rotation <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. For Newton's map, the derivative at a fixed point (a root) is 0 <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. These are called **super-attracting fixed points** because nearby points shrink significantly towards them, ensuring rapid convergence to roots <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.

### Cycles and Attracting Cycles
Beyond fixed points, dynamics can involve **cycles**, where `f(z)` is not `z`, but `f(f(z))` returns to `z` (a two-cycle) or `f^n(z)` returns to `z` (an n-cycle) <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>. Finding these cycles involves solving higher-degree polynomial equations <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>. The number of periodic points (points that fall into a cycle) grows exponentially with the period `n` <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.

For numerical methods like Newton's method, the presence of **attracting cycles** is important <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>. If an initial guess falls into an attracting cycle, it will never find a root <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>. For example, when finding the roots of `z³ - 2z + 2` using Newton's method, a cluster of points around zero can get trapped in an attracting two-cycle between zero and one <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>.

## The Universal Nature of the Mandelbrot Set

### Fatou's Theorem and Critical Points
A crucial insight comes from a theorem by [[Pierre_Fatou_and_Gaston_Julia | Pierre Fatou]] <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>: if a [[complex_functions_and_transformations | rational map]] has an attracting cycle, then at least one of the values where the derivative of the iterated function equals zero (known as critical points) must fall into that cycle <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>. This implies that if an attracting cycle exists, a critical point will find it. This principle justifies why for the Mandelbrot set, using a single seed value of z=0 (which is a critical point for `z² + c`), is sufficient to reveal the full and interesting picture <a class="yt-timestamp" data-t="00:18:26">[00:18:26]</a>.

This theorem allows for the creation of a "parameter space" diagram for cubic polynomials, similar to the Mandelbrot set <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>. By fixing two roots (e.g., at -1 and 1) and varying a third root (lambda), a diagram can be generated where each pixel represents a unique polynomial <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>. Pixels are colored black if the Newton's method process for the corresponding polynomial produces an attracting cycle, which can be tested by checking the behavior of the average of the three roots (a critical point for Newton's map) <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>.

When zoomed in, this diagram reveals a black region that looks exactly like a Mandelbrot set <a class="yt-timestamp" data-t="00:20:43">[00:20:43]</a>. This suggests that the Mandelbrot shape is not unique to the `z² + c` example but represents something more general and universal about parameter spaces in iterative processes <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>.

## Why Fractals? Julia and Fatou Sets
The reason these diagrams are fractals is tied to the chaotic behavior of the system.
*   **Fatou Set**: Points that eventually fall into some stable, predictable pattern (e.g., an attracting fixed point or cycle) are part of the Fatou set <a class="yt-timestamp" data-t="00:22:29">[00:22:29]</a>. Small discs around points in the Fatou set tend to shrink upon iteration <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>.
*   **Julia Set**: The Julia set comprises all other points, typically the rough boundaries between colored regions in the pictures <a class="yt-timestamp" data-t="00:22:41">[00:22:41]</a>. It includes repelling cycles and fixed points <a class="yt-timestamp" data-t="00:22:53">[00:22:53]</a>. Points in the Julia set tend to behave chaotically, with nearby neighbors diverging to qualitatively different behaviors <a class="yt-timestamp" data-t="00:23:35">[00:23:35]</a>.

A surprising result related to Julia sets is the "stuff-goes-everywhere principle" (a corollary to Montel's theorem) <a class="yt-timestamp" data-t="00:23:49">[00:23:49]</a>. This principle states that if a small disc is drawn around a point on the Julia set, upon iteration, that disc will eventually expand to hit every single point on the complex plane (with at most two exceptions) <a class="yt-timestamp" data-t="00:23:53">[00:23:53]</a>. This means that if there are multiple attracting behaviors (three or more), any small region on the Julia set's boundary will inevitably contain points that lead to *all* possible attracting behaviors, preventing smooth boundaries and resulting in intricate fractal shapes <a class="yt-timestamp" data-t="00:24:25">[00:24:25]</a>.

While many Julia sets have an area of zero, there are examples where the Julia set is the entire plane, meaning everything behaves chaotically <a class="yt-timestamp" data-t="00:26:06">[00:26:06]</a>. This connection between chaos and the fractal nature of these shapes provides a logical link rather than just a coincidental analogy <a class="yt-timestamp" data-t="00:26:57">[00:26:57]</a>.