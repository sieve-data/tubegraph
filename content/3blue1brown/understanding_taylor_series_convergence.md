---
title: Understanding Taylor series convergence
videoId: 3d6DsjIBzJ4
---

From: [[3blue1brown]] <br/> 

Taylor series are one of mathematics' most powerful tools for [[approximating_functions_using_taylor_series | approximating functions]] <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. They frequently appear in [[applications_of_taylor_series_in_physics_and_engineering | math, physics, and engineering]] <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, despite their [[importance_of_taylor_series_in_mathematics | importance]] not always being immediately apparent <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Taylor Polynomials

The study of Taylor series primarily involves taking non-polynomial functions and finding polynomials that [[approximating_functions_using_taylor_series | approximate them]] near a specific input <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. Polynomials are generally easier to compute, differentiate, and integrate, making them "more friendly" to work with <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

[[using_taylor_polynomials_for_function_approximation | Taylor polynomials]] are constructed by ensuring that a polynomial approximation matches the function's value and its higher-order derivatives at a chosen point, often $x=0$ <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>:

*   **Matching Value**: The constant term ($c_0$) of the polynomial is set to match the function's value at the point of approximation <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Matching Slope**: The coefficient of the linear term ($c_1$) controls the polynomial's derivative at that point, ensuring it matches the function's slope <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   **Matching Curvature**: The coefficient of the quadratic term ($c_2$) controls the polynomial's second derivative, ensuring its curvature matches the function's <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   **Higher Order Terms**: Adding more terms (e.g., $c_3x^3$, $c_4x^4$) allows for matching higher-order derivatives, leading to a closer approximation <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

A key observation is that when taking successive derivatives of $x^n$, a factorial term ($n!$) naturally appears <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. Therefore, the coefficient of each $x^n$ term in the polynomial approximation is the $n^{th}$ derivative of the function (evaluated at the approximation point) divided by $n!$ <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. This means the general formula for a Taylor polynomial around $x=0$ is:

$P(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \dots + \frac{f^{(n)}(0)}{n!}x^n$ <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>

If approximating near an input 'a' instead of 0, the polynomial is expressed in terms of powers of $(x-a)$, and derivatives are evaluated at 'a' <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

## From Polynomials to Taylor Series

While [[using_taylor_polynomials_for_function_approximation | Taylor polynomials]] use a finite number of terms, one might consider if it makes sense to add [[concept_of_infinite_sums_in_mathematics | infinitely many terms]] <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>. In mathematics, an [[infinite_series_and_sum_computations | infinite sum]] is called a series <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>. Adding all infinitely many terms of a Taylor polynomial results in what is called a Taylor series <a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a>.

### The Concept of Convergence

The idea of adding infinitely many things does not directly make sense, as one can only perform a finite number of additions <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>. However, if a series behaves such that adding more and more terms gets "increasingly close to some specific value," the series is said to **converge** to that value <a class="yt-timestamp" data-t="00:17:57">[00:17:57]</a>. When a series converges, its infinite sum can be considered "equal" to the value it's converging to <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.

### Examples of Convergence

*   **$e^x$**: The Taylor polynomials for $e^x$ around $x=0$ are $1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots$ <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>. If you plug in any value for $x$, such as $x=1$, adding more and more terms of this series will get closer and closer to the value of $e$ <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>. This holds true for *any* input $x$; the series converges to $e^x$ for all $x$ <a class="yt-timestamp" data-t="00:18:47">[00:18:47]</a>. This is a "magical thing" because it means information gathered at a single point (x=0) allows for precise calculations far away <a class="yt-timestamp" data-t="00:19:08">[00:19:08]</a>.
*   **Sine and Cosine**: Similar to $e^x$, the Taylor series for sine and cosine also converge for all inputs $x$ <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.
*   **Natural Log of $x$ (ln x)**: The Taylor series for $\ln x$ around $x=1$ looks different. When plugging in an input between 0 and 2, adding more terms gets closer to $\ln x$ <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>. However, outside this range (e.g., for inputs above 2), the series fails to approach anything specific and the sum "bounces back and forth wildly" <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>. In such cases, the series is said to **diverge** <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>.

### Radius of Convergence

The maximum distance between the point of approximation and points where the Taylor series actually converges is called the **radius of convergence** <a class="yt-timestamp" data-t="00:20:44">[00:20:44]</a>. For $\ln x$ around $x=1$, the radius of convergence is 1, meaning it converges for $x$ in the interval $(0, 2)$ <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>. For $e^x$, sine, and cosine, the radius of convergence is infinite.

The fundamental intuition behind Taylor series is that they translate derivative information at a single point into approximation information around that point <a class="yt-timestamp" data-t="00:21:32">[00:21:32]</a>. Understanding when these infinite sums converge is crucial for their practical application.