---
title: Why the number e is special in calculus
videoId: 4PDoT7jtxmw
---

From: [[3blue1brown]] <br/> 

The mathematical constant *e*, approximately 2.71828, often appears in various mathematical contexts, from prime number distributions to compound interest, leading to the question of why it is considered "special" or "natural" <a class="yt-timestamp" data-t="06:10:11">[06:10:11]</a>. Its significance is deeply rooted in [[Fundamental concepts of calculus | calculus]] and the concept of rates of change <a class="yt-timestamp" data-t="05:54:52">[05:54:52]</a>, <a class="yt-timestamp" data-t="05:59:59">[05:59:59]</a>.

## e and Prime Number Density

One surprising appearance of *e* is in the density of prime numbers. The proportion of prime numbers near a very large value, such as a trillion, is approximately one divided by the natural logarithm of that number <a class="yt-timestamp" data-t="03:18:18">[03:18:18]</a>, <a class="yt-timestamp" data-t="04:15:24">[04:15:24]</a>. For numbers around a trillion (10^12), the natural logarithm is approximately 27 <a class="yt-timestamp" data-t="05:32:04">[05:32:04]</a>, which aligns closely with the observed density of primes in that range (about one in 27) <a class="yt-timestamp" data-t="04:09:12">[04:09:12]</a>, <a class="yt-timestamp" data-t="05:38:00">[05:38:00]</a>.

This connection extends to other mathematical series. For instance, the sum of the reciprocals of squares (1/1² + 1/2² + 1/3² + ...) famously converges to π²/6 <a class="yt-timestamp" data-t="06:34:00">[06:34:00]</a>, <a class="yt-timestamp" data-t="07:03:00">[07:03:00]</a>. Even more remarkably, if this series is manipulated by keeping only terms whose denominators are primes or powers of primes (scaling down terms for prime powers), the resulting sum equals the natural logarithm of π²/6 <a class="yt-timestamp" data-t="09:22:00">[09:22:00]</a>, <a class="yt-timestamp" data-t="09:29:34">[09:29:34]</a>. Similar patterns appear in other series involving π, where applying this "prime game" results in the natural logarithm of the original sum <a class="yt-timestamp" data-t="09:34:00">[09:34:00]</a>, <a class="yt-timestamp" data-t="11:09:00">[11:09:00]</a>. These unexpected connections highlight the "natural" presence of *e* and its logarithm in areas seemingly unrelated to exponential growth <a class="yt-timestamp" data-t="09:59:00">[09:59:00]</a>, <a class="yt-timestamp" data-t="11:14:00">[11:14:00]</a>.

## The Role of e in Exponential Functions

Exponential functions, represented as `a^x` (where `a` is the base), describe phenomena of growth or decay. While any positive number `a` can serve as a base, *e* is almost universally chosen in fields like physics, engineering, and advanced mathematics <a class="yt-timestamp" data-t="23:37:00">[23:37:00]</a>, <a class="yt-timestamp" data-t="24:19:00">[24:19:00]</a>. This is because any exponential function `a^x` can be rewritten in terms of *e* as `e^(ln(a) * x)` <a class="yt-timestamp" data-t="27:14:00">[27:14:00]</a>.

For example, the bell curve, critical in probability and statistics, is typically written as `e^(-x^2)` (often with additional parameters) <a class="yt-timestamp" data-t="24:41:00">[24:41:00]</a>. While it *could* be written with a different base, such as `a^(-x^2)`, using *e* allows the parameters in the exponent to directly correspond to meaningful statistical measures like the standard deviation <a class="yt-timestamp" data-t="25:38:00">[25:38:00]</a>, <a class="yt-timestamp" data-t="33:50:00">[33:50:00]</a>.

Similarly, in the context of [[Complex numbers in mathematics | complex numbers]], expressions like `e^(it)` (Euler's formula) describe movement around the unit circle <a class="yt-timestamp" data-t="28:52:00">[28:52:00]</a>, <a class="yt-timestamp" data-t="29:05:00">[29:05:00]</a>. While `2^(it)` or any `a^(it)` would also describe circular motion, `e^(it)` is chosen because the variable `t` directly represents the distance walked along the unit circle in radians <a class="yt-timestamp" data-t="30:33:00">[30:33:00]</a>, <a class="yt-timestamp" data-t="34:04:00">[34:04:00]</a>.

> [!INFO] Why e is Preferred
> The choice of *e* as the base for exponential functions makes the constants involved in their derivatives and integrals "more readable" <a class="yt-timestamp" data-t="33:06:00">[33:06:00]</a>, <a class="yt-timestamp" data-t="33:09:00">[33:09:00]</a>, <a class="yt-timestamp" data-t="33:53:00">[33:53:00]</a>, <a class="yt-timestamp" data-t="36:09:00">[36:09:00]</a>.

## The Unique Derivative Property

The fundamental reason *e* is special in [[Introduction to calculus series | calculus]] is its unique derivative property: the derivative of `e^t` with respect to `t` is `e^t` itself <a class="yt-timestamp" data-t="31:00:00">[31:00:00]</a>, <a class="yt-timestamp" data-t="31:12:00">[31:12:00]</a>.

> [!EXAMPLE]
> `d/dt (e^t) = e^t` <a class="yt-timestamp" data-t="31:00:00">[31:00:00]</a>

This means that at any point on the graph of `y = e^t`, the slope of the tangent line is equal to the height of the function at that point <a class="yt-timestamp" data-t="31:25:00">[31:25:00]</a>. This property is crucial for modeling continuous compound growth, where the rate of growth is always proportional to the current amount <a class="yt-timestamp" data-t="31:37:00">[31:37:00]</a>.

For a more general exponential function `e^(rt)`, its derivative is `r * e^(rt)` <a class="yt-timestamp" data-t="31:57:00">[31:57:00]</a>. Here, `r` directly represents the proportionality constant for the rate of change <a class="yt-timestamp" data-t="32:56:00">[32:56:00]</a>. In contrast, for an exponential `a^t`, its derivative is `ln(a) * a^t` <a class="yt-timestamp" data-t="36:12:00">[36:12:00]</a>. While mathematically equivalent, the natural logarithm of the base `a` appears as a constant, making the rate of change less directly interpretable <a class="yt-timestamp" data-t="37:09:00">[37:09:00]</a>.

In the complex plane, for `e^(it)`, its derivative is `i * e^(it)` <a class="yt-timestamp" data-t="34:17:00">[34:17:00]</a>. This means the rate of change (velocity vector) at any point is the current position vector multiplied by `i`, which is a 90-degree rotation <a class="yt-timestamp" data-t="34:31:00">[34:31:00]</a>, <a class="yt-timestamp" data-t="34:43:00">[34:43:00]</a>. This explains why `e^(it)` traces a circle at a speed of one unit per second (radian per unit time) <a class="yt-timestamp" data-t="35:15:00">[35:15:00]</a>, <a class="yt-timestamp" data-t="35:17:00">[35:17:00]</a>. For `2^(it)`, the derivative involves `ln(2)`, causing the rotation to be scaled and thus traverse the circle at a different rate <a class="yt-timestamp" data-t="35:26:00">[35:26:00]</a>, <a class="yt-timestamp" data-t="35:46:00">[35:46:00]</a>.

### Defining e

The number *e* can be defined in several ways, often linked to its unique derivative property or as the sum of an infinite series:

*   **As the base where the derivative equals itself**: *e* is the unique number such that the derivative of `e^x` is `e^x` <a class="yt-timestamp" data-t="37:43:00">[37:43:00]</a>, <a class="yt-timestamp" data-t="45:35:00">[45:35:00]</a>. This implies that the limit `(a^h - 1) / h` as `h` approaches zero must be equal to 1 for `a=e` <a class="yt-timestamp" data-t="45:38:00">[45:38:00]</a>. For `a=2`, this limit is approximately 0.69 <a class="yt-timestamp" data-t="44:10:00">[44:10:00]</a>, which is `ln(2)` <a class="yt-timestamp" data-t="45:17:00">[45:17:00]</a>.
*   **As the sum of an infinite series**: The exponential function, often denoted `exp(x)`, is defined by the infinite series:
    `exp(x) = 1 + x + x²/2! + x³/3! + ...` <a class="yt-timestamp" data-t="46:04:00">[46:04:00]</a>, <a class="yt-timestamp" data-t="46:09:00">[46:09:00]</a>.
    If this series is taken as the fundamental definition, it can then be shown that `exp(x)` behaves like an exponential (i.e., `exp(a+b) = exp(a) * exp(b)`) <a class="yt-timestamp" data-t="47:52:00">[47:52:00]</a>. The number *e* is then defined as `exp(1)` <a class="yt-timestamp" data-t="48:05:00">[48:05:00]</a>. A beautiful consequence of this definition is that the derivative of `exp(x)` (term by term using the [[Power rule in calculus and its geometric significance | power rule]]) is `exp(x)` itself <a class="yt-timestamp" data-t="48:48:00">[48:48:00]</a>, <a class="yt-timestamp" data-t="49:59:00">[49:59:00]</a>.

## The Natural Logarithm: Derivative and Integral

The natural logarithm `ln(x)` is the inverse function of `e^x`. Its derivative is elegantly simple: `d/dx (ln(x)) = 1/x` <a class="yt-timestamp" data-t="53:59:00">[53:59:00]</a>. This can be derived using implicit differentiation from `y = ln(x)` (which implies `x = e^y`) <a class="yt-timestamp" data-t="51:55:00">[51:55:00]</a>, <a class="yt-timestamp" data-t="52:07:00">[52:07:00]</a>, <a class="yt-timestamp" data-t="53:17:00">[53:17:00]</a>. The graph of `ln(x)` becomes shallower as `x` increases, which is consistent with its derivative `1/x` getting smaller <a class="yt-timestamp" data-t="54:03:00">[54:03:00]</a>, <a class="yt-timestamp" data-t="54:14:00">[54:14:00]</a>.

Conversely, the integral of `1/x` is the natural logarithm: `∫(1/x)dx = ln(x) + C` <a class="yt-timestamp" data-t="01:00:55">[01:00:55]</a>. This connection is fundamental to the [[Fundamental theorem of calculus | Fundamental Theorem of Calculus]] <a class="yt-timestamp" data-t="01:00:41">[01:00:41]</a>.

### Harmonic Series and Euler's Constant

The sum of the reciprocals of integers, `1 + 1/2 + 1/3 + ... + 1/n`, known as the harmonic series, does not converge; it grows infinitely large <a class="yt-timestamp" data-t="01:39:46">[01:39:46]</a>. However, its growth is approximately described by the natural logarithm: `S_n ≈ ln(n)` <a class="yt-timestamp" data-t="01:54:54">[01:54:54]</a>.

More precisely, the sum `S_n` is approximately `ln(n) + γ`, where `γ` (gamma) is the Euler-Mascheroni constant (approximately 0.577) <a class="yt-timestamp" data-t="01:02:10">[01:02:10]</a>. This constant represents the limiting difference between the harmonic series and the natural logarithm of `n` as `n` approaches infinity <a class="yt-timestamp" data-t="01:02:16">[01:02:16]</a>. [[Visualization in calculus | Visualizing]] this, the sum of rectangles of height `1/n` and width `1` (representing the harmonic series) is always slightly larger than the area under the curve `1/x` (representing the integral `ln(x)`) <a class="yt-timestamp" data-t="00:57:48">[00:57:48]</a>, <a class="yt-timestamp" data-t="00:59:06">[00:59:06]</a>.

### Alternating Harmonic Series

Another series, `1 - 1/2 + 1/3 - 1/4 + ...`, known as the alternating harmonic series, surprisingly converges to `ln(2)` <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>, <a class="yt-timestamp" data-t="01:03:09">[01:03:09]</a>. This can be demonstrated by considering a more general function `f(x) = x - x²/2 + x³/3 - x⁴/4 + ...` <a class="yt-timestamp" data-t="01:05:04">[01:05:04]</a>. Taking its derivative yields `f'(x) = 1 - x + x² - x³ + ...` <a class="yt-timestamp" data-t="01:05:39">[01:05:39]</a>, which is a geometric series sum `1/(1+x)` <a class="yt-timestamp" data-t="01:08:11">[01:08:11]</a>. Integrating `1/(1+x)` from 0 to `x` gives `ln(1+x)` <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>. Therefore, `f(x) = ln(1+x)`. Plugging in `x=1` into `f(x)` gives the alternating harmonic series, and plugging `x=1` into `ln(1+x)` gives `ln(2)` <a class="yt-timestamp" data-t="01:12:35">[01:12:35]</a>.

These examples illustrate that *e* and its natural logarithm are not merely arbitrary constants, but fundamental mathematical objects that naturally emerge in the description of continuous processes, rates of change, and even unexpected areas like the distribution of prime numbers. This prevalence makes `e` truly special in the landscape of mathematics.