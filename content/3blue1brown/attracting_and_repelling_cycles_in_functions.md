---
title: Attracting and Repelling Cycles in Functions
videoId: LqbZpur38nw
---

From: [[3blue1brown]] <br/> 

[[Holomorphic dynamics]] is a field of mathematics that studies the behavior of functions with complex number inputs and outputs when they are repeatedly applied <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This field is intimately tied to concepts like the [[lorenz_attractor_and_chaos_theory | Mandelbrot set]] and [[mathematical_functions_and_graphs | Newton's fractal]] <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Iterating Functions

The "dynamics" aspect of [[holomorphic dynamics]] involves asking what happens when a function is repeatedly applied, meaning the output of one application becomes the input for the next <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This iterative process can lead to several outcomes:
*   **Cycles:** The sequence of points gets trapped in a repeating pattern <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   **Limit Points:** The sequence approaches a specific point, potentially even infinity <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
*   **Chaos:** The sequence exhibits no discernible pattern <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

When visualizing these behaviors for various functions, intricate [[lorenz_attractor_and_chaos_theory | fractal patterns]] often emerge <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

## Fixed Points

The simplest behavior in an iterative system is when the process stays fixed in place <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. A value `z` is a **fixed point** of a function `f` if `f(z) = z` <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
*   For functions arising from [[mathematical_functions_and_graphs | Newton's method]], the roots of the polynomial `p` (where `p(z) = 0`) are fixed points of the iterative expression `x - p(x) / p'(x)` <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.
*   Any rational function will always have fixed points, as finding them can be rearranged into finding the roots of a polynomial expression <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

### Stability of Fixed Points

[[Understanding function behavior beyond graphs | Understanding the stability]] of fixed points is crucial for understanding the overall dynamics <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   A fixed point is **attracting** if nearby points are drawn towards it <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.
*   A fixed point is **repelling** if nearby points are pushed away from it <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.

This stability can be computed using the [[derivatives_of_simple_functions_and_their_intuition | derivative]] of the function at the fixed point <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>:
*   If the absolute value of the derivative `|f'(z)|` at the fixed point `z` is less than 1, the fixed point is attracting <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.
*   If `|f'(z)|` is greater than 1, the fixed point is repelling <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.
*   If the derivative is exactly 0, it's a **super-attracting** fixed point, meaning nearby points shrink significantly towards it <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>. This is by design for [[mathematical_functions_and_graphs | Newton's method]] to quickly converge to roots <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>.

## Cycles (Periodic Points)

Beyond fixed points, an iterative process can fall into **cycles**, where `f(z)` is not `z` but some other value `w`, and `f(w)` eventually returns to `z` <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.
*   A "two-cycle" occurs if `f(f(z)) = z` (and `f(z)` is not `z`) <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.
*   **n-cycles** can be found by evaluating `f` composed with itself `n` times and setting it equal to `z` <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>.
*   The explicit expressions for higher-order cycles become very complex, but the number of periodic points grows exponentially with `n` <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.

### Attracting Cycles

For practical applications, such as [[mathematical_functions_and_graphs | Newton's method]], the key question is whether a cycle is **attracting** <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>. An attracting cycle means that a neighborhood of points around a value from that cycle will be pulled towards it <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.
*   If [[mathematical_functions_and_graphs | Newton's method]] has an attracting cycle, an initial guess might get trapped in that cycle instead of finding a root <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>.
*   An example is finding the roots of `z^3 - 2z + 2` using Newton's method, where a starting cluster around `z=0` can get trapped in a 2-cycle between `0` and `1` <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>.
*   To verify if a cycle is attracting, compute the derivative of the `n`-times composed function (`f(f(...f(z)...))`) at a point in the cycle. If its magnitude is less than one, the cycle is attracting <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>.

### Fatou's Theorem and Critical Points

Mathematician Pierre Fatou showed a significant result: if a rational map has an attracting cycle, then at least one **critical point** (a value where the [[derivatives_of_simple_functions_and_their_intuition | derivative]] of the iterated function equals zero) must fall into that cycle <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>.
*   This implies that if a cycle is attracting, at least one of its values should have a very small derivative, drawing points towards it <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>.
*   This theorem explains why, for the [[lorenz_attractor_and_chaos_theory | Mandelbrot set]] (`z^2 + c`), using a single seed value of `z=0` (which is a critical point) is sufficient to generate a comprehensive picture of attracting cycles <a class="yt-timestamp" data-t="00:18:26">[00:18:26]</a>.
*   For cubic polynomials in [[mathematical_functions_and_graphs | Newton's method]], it's been shown that if an attracting cycle exists, the seed value at the average of the three roots will fall into that cycle <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>. This allows for visualizing which cubic polynomials have attracting cycles by simply checking this midpoint <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>.

## Fatou and Julia Sets

The terms **Fatou set** and **Julia set** are fundamental in [[holomorphic dynamics]] <a class="yt-timestamp" data-t="00:22:24">[00:22:24]</a>.
*   The **Fatou set** consists of points that eventually fall into some stable, predictable pattern (e.g., an attracting fixed point or cycle) <a class="yt-timestamp" data-t="00:22:29">[00:22:29]</a>. If a small disc is drawn around a point in the Fatou set, it will eventually shrink as it falls into stable behavior <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>.
*   The **Julia set** comprises all other points, typically forming the rough boundaries between regions of different stable behaviors <a class="yt-timestamp" data-t="00:22:41">[00:22:41]</a>. This set includes all repelling cycles and repelling fixed points <a class="yt-timestamp" data-t="00:22:53">[00:22:53]</a>. Points in the Julia set tend to behave [[lorenz_attractor_and_chaos_theory | chaotically]] <a class="yt-timestamp" data-t="00:23:35">[00:23:35]</a>.

### The "Stuff-Goes-Everywhere" Principle

A surprising result related to Julia sets is that if a small disc is drawn around any point on the Julia set, as the function is iterated, that disc will eventually expand to cover almost every single point on the complex plane (with at most two exceptions) <a class="yt-timestamp" data-t="00:23:49">[00:23:49]</a>. This is a corollary to Montel's theorem <a class="yt-timestamp" data-t="00:24:09">[00:24:09]</a>.
*   This principle implies that points on the Julia set are as [[lorenz_attractor_and_chaos_theory | chaotic]] as possible <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>.
*   If there are three or more attracting behaviors in a system, this principle explains why the Julia set boundary must be non-smooth and [[lorenz_attractor_and_chaos_theory | fractal]] <a class="yt-timestamp" data-t="00:25:23">[00:25:23]</a>. Any small circle touching a smooth boundary would only contain points leading to two behaviors, but the "stuff-goes-everywhere" principle requires all behaviors to be present in any small disc around a Julia set point <a class="yt-timestamp" data-t="00:21:49">[00:21:49]</a>.
*   This establishes a logical link between chaos and the fractal shapes observed in [[holomorphic dynamics]] <a class="yt-timestamp" data-t="00:26:18">[00:26:18]</a>.