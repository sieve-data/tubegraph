---
title: Attracing and repelling cycles in dynamical systems
videoId: LqbZpur38nw
---

From: [[3blue1brown]] <br/> 

This article explores [[holomorphic_dynamics|holomorphic dynamics]], a field that studies concepts like the Mandelbrot set <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. A primary goal is to demonstrate how the Mandelbrot set appears more generally than its initial definition suggests <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. This field is closely related to the concepts discussed in the previous video regarding Newton's fractal <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Holomorphic Functions
The term "holomorphic" refers to functions that accept complex number inputs and produce complex number outputs, and for which a derivative can be taken <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. In this context, having a derivative means that when one zooms in on how the function behaves near a point and its neighbors, it appears roughly as a scaling and rotation, similar to multiplying by a complex constant <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. Most ordinary functions, such as polynomials, exponentials, and trigonometric functions, fall into this category <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

## Dynamics of Iterated Functions
The "dynamics" aspect of the title refers to the study of what happens when a function is repeatedly applied <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This involves evaluating the function on an input, then on its output, and so on <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. The resulting sequence of points can exhibit several behaviors:
*   **Cycles:** The pattern of points gets trapped in a cycle <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   **Limiting Point:** The sequence approaches a specific limit point <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
*   **Infinity:** The sequence grows indefinitely, flying off to infinity, which mathematicians consider a limit point <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
*   **Chaos:** The sequence has no discernible pattern and behaves chaotically <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

Surprisingly, visualizing when these different behaviors arise for various functions often results in intricate [[numerical_methods_and_chaos_theory_in_differential_equations | fractal patterns]] <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

### Newton's Fractal as an Example
Newton's method is an algorithm for finding the root of a polynomial `p` <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. It works by repeatedly iterating the expression `x - p(x) / p'(x)` <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. When the initial seed value is near a root (where `p(x) = 0`), this process quickly converges to that root <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

When applied in the complex plane, by coloring pixels based on which root a seed value converges to, the results are intricate pictures with rough fractal boundaries between colors <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. The iterated function in Newton's method can be rewritten as one polynomial divided by another, which mathematicians call rational functions <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

Mathematicians Pierre Fatou and Gaston Julia extensively studied the iteration of rational functions after World War I, developing a rich theory without the aid of computers <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

### The Mandelbrot Set and Julia Sets
One of the most widely known examples of studying rational functions and their resulting fractals is the simple function `z^2 + c`, where `c` is a constant <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. For the Mandelbrot set, `c` is varied, and the initial value `z` is always zero <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. The process then involves repeatedly applying `z^2 + c` <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

If the sequence of values remains bounded, the point `c` is colored black; otherwise, it's colored based on how quickly it diverges to infinity <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. This visualization yields the iconic Mandelbrot set <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   The largest cardioid section contains values of `c` where the process converges to a limit <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
*   The large circle on the left indicates values where the process enters a 2-cycle <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
*   Other circles represent higher-period cycles <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

The Mandelbrot set is a **parameter space** because `c` (a parameter of the function) is tweaked, while the initial seed value is consistent <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.

In contrast, **Julia sets** are constructed by fixing the parameter `c` and letting the pixels represent different possible initial values (`z_naught`) <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. Pixels are colored black if the process remains bounded, and with a gradient if they diverge <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. The term "Julia set" specifically refers to the boundaries of these regions, not their interiors <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

## Fixed Points and Stability
To understand the full dynamics of these systems, it's crucial to analyze the stability of points <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

### Fixed Points
A **fixed point** of a function `f(z)` is a value `z` where `f(z) = z` <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. For Newton's method, the roots of the polynomial `p` are fixed points of the iteration function <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. Any rational function will always have fixed points, as finding them boils down to finding the roots of a polynomial equation, which are guaranteed by the fundamental theorem of algebra <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

### Stability (Attracting and Repelling)
A fixed point is **attracting** if nearby points tend to be drawn towards it, and **repelling** if they are pushed away <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>. This property can be computed using the derivative of the function <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

For complex functions, the derivative `f'(z)` can be interpreted geometrically as a scaling and rotation <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. For stability analysis, only the scaling (absolute value) matters <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>:
*   If `|f'(z)| < 1` at a fixed point, it is **attracting** <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.
*   If `|f'(z)| > 1` at a fixed point, it is **repelling** <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.

For Newton's map, the derivative at a fixed point (a root) is 0 <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. These are called **super-attracting fixed points**, meaning nearby points shrink significantly towards them <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>. This is by design, as Newton's method aims for rapid convergence to roots <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>. The main cardioid of the Mandelbrot set corresponds to `c` values where at least one of its fixed points is attracting <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.

### Attracting and Repelling Cycles
A **cycle of period n** occurs when iterating `f` n times returns to the starting point, i.e., `f^n(z) = z` <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. These can be found by solving `f^n(z) = z`, which for `z^2 + c` leads to polynomials of exponentially growing degrees (e.g., `2^n`) <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.

While infinitely many points fall into cycles for such processes <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>, these are usually on the boundary of regions and unlikely to be hit in practice <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>. What matters is if a cycle is **attracting**, meaning a neighborhood of points around values in that cycle tends to be pulled in <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>. This is determined by checking if the derivative of `f^n(z)` at any point in the cycle has a magnitude less than one <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>.

A relevant question for [[numerical_methods_and_chaos_theory_in_differential_equations | numerical methods]] is whether Newton's map ever has an attracting cycle, as this would mean an initial guess could get trapped and never find a root <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>. The answer is yes <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>. For example, when finding the roots of `z^3 - 2z + 2` using Newton's method, a cluster of points around zero can get trapped in a 2-cycle between zero and one <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>.

### Fatou's Theorem and its Implications
A key theorem by Fatou states that if a rational map has an attracting cycle, then at least one point where the derivative of the iterated function (`f'(z)`) equals zero (a critical point) must fall into that cycle <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>. The intuition is that for a cycle to be attracting, at least one of its values should have a very small derivative, near a point where the derivative is zero <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>.

This theorem justifies why, for the Mandelbrot set, checking only the seed value `z = 0` (which is a critical point for `z^2 + c`) is sufficient to gain a full picture; if a stable cycle exists, this seed value will find it <a class="yt-timestamp" data-t="00:18:26">[00:18:26]</a>.

This principle extends to Newton's method for cubic polynomials. By fixing two roots and moving a third (`lambda`), a diagram can be generated where each pixel corresponds to a unique polynomial (a parameter space) <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>. A pixel is colored black if Newton's method for the corresponding polynomial produces an attracting cycle <a class="yt-timestamp" data-t="00:20:13">[00:20:13]</a>. When zoomed in, this black region strikingly resembles the Mandelbrot set, demonstrating its broader significance beyond just `z^2 + c` <a class="yt-timestamp" data-t="00:20:43">[00:20:43]</a>.

## Chaos and the Nature of Fractals
The fractal nature of these diagrams is linked to chaos. A peculiar property of Newton's method diagrams (and generally for any rational map) is that if one draws a small circle around the boundary of a colored region, that circle must include all available colors from the picture <a class="yt-timestamp" data-t="00:21:16">[00:21:16]</a>. If there are at least three colors (representing different limiting behaviors), this property implies that the boundary can never be smooth <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>.

This leads to the formal definitions of:
*   **Fatou Set:** The set of points that eventually fall into some stable, predictable pattern (e.g., attracting fixed point or cycle) <a class="yt-timestamp" data-t="00:22:29">[00:22:29]</a>.
*   **Julia Set:** Everything else; the rough boundaries between colored regions <a class="yt-timestamp" data-t="00:22:41">[00:22:41]</a>. The Julia set includes all repelling cycles and repelling fixed points <a class="yt-timestamp" data-t="00:22:53">[00:22:53]</a>.

Points in the Julia set tend to behave chaotically, meaning their nearby neighbors, even very close ones, will eventually fall into qualitatively different behaviors <a class="yt-timestamp" data-t="00:23:35">[00:23:35]</a>. A surprising result, related to Montel's theorem, is that if a small disk is drawn around a point on the Julia set, upon iteration, it tends to expand to hit every single point on the complex plane (with at most two exceptions) <a class="yt-timestamp" data-t="00:23:49">[00:23:49]</a>. This "stuff-goes-everywhere principle" implies that Julia set points are as chaotic as possible <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>.

This means if there's any attractive behavior (like an attracting fixed point or cycle), values from that tiny disk around a Julia set point will eventually fall into that behavior <a class="yt-timestamp" data-t="00:25:04">[00:25:04]</a>. In cases with three or more attracting behaviors, this explains why the Julia set is not smooth and must be complicated <a class="yt-timestamp" data-t="00:25:20">[00:25:20]</a>.

While Julia sets often have zero area, some examples exist where the Julia set is the entire complex plane, meaning everything behaves chaotically <a class="yt-timestamp" data-t="00:26:06">[00:26:06]</a>. The connection between chaos and fractal shapes is not merely metaphorical; quantifying the chaotic behavior of some points directly explains the rough fractal shape through this boundary property <a class="yt-timestamp" data-t="00:26:20">[00:26:20]</a>. This provides a logical link between these two phenomena that often coincide in mathematics <a class="yt-timestamp" data-t="00:27:01">[00:27:01]</a>.