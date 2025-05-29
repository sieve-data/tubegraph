---
title: Approximation of functions using Taylor series
videoId: 3d6DsjIBzJ4
---

From: [[3blue1brown]] <br/> 

[[importance_of_taylor_series | Taylor series]] are considered one of the most powerful tools in mathematics for [[approximating_solutions_using_calculus | approximating functions]] <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. They frequently appear in mathematics, physics, and various engineering fields <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Motivation for Approximating Functions
The usefulness of [[importance_of_taylor_series | Taylor series]] often becomes clear in practical applications, such as physics problems <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. For instance, when studying the potential energy of a pendulum, the required expression for its height is proportional to `1 - cosine(angle)` <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. The cosine function can make such problems awkward and unwieldy, obscuring the relationship between pendulums and other oscillating phenomena <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. However, approximating `cosine(theta)` as `1 - theta^2 / 2` simplifies the problem significantly <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This approximation is visually close to `cosine(theta)` for small angles near 0 <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

The primary goal of [[importance_of_taylor_series | Taylor series]] is to transform non-polynomial functions into polynomials that approximate them near a specific input <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. Polynomials are generally easier to work with, compute, differentiate, and integrate compared to other functions <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

## [[constructing_taylor_polynomials | Constructing Taylor Polynomials]]
To construct a polynomial approximation, such as a quadratic `c0 + c1*x + c2*x^2` for `cosine(x)` near `x = 0`, the goal is to make its graph "spoon" with the original function's graph at that point <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

The process involves matching the function's value and its [[derivatives_of_simple_functions_and_their_intuition | derivatives]] at the point of approximation:
1.  **Matching the Value**: At `x = 0`, `cosine(x)` is 1 <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. For the approximation `c0 + c1*x + c2*x^2` to match, plugging in `x = 0` yields `c0` <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. Therefore, `c0` must be 1 <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
2.  **Matching the First Derivative (Slope)**: The derivative of `cosine(x)` is `negative sine(x)` <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. At `x = 0`, `negative sine(0)` is 0, indicating a flat tangent line <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. The derivative of the quadratic approximation is `c1 + 2*c2*x` <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. At `x = 0`, this is `c1` <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. Thus, `c1` must be 0 to match the slope <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
3.  **Matching the Second Derivative (Curvature)**: The second derivative of `cosine(x)` is `negative cosine(x)` <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. At `x = 0`, this equals `negative 1` <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. This ensures the approximation curves at the same rate as the original function <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. The second derivative of the quadratic approximation (`c1 + 2*c2*x`) is `2*c2` <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. To match, `2*c2` must be `negative 1`, so `c2` is `negative 1/2` <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

This process yields the quadratic approximation `1 - (1/2)x^2` for `cosine(x)` near `x = 0` <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. This approximation is very accurate for small values, e.g., `cosine(0.1)` is estimated as `0.995` <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.

### Generalizing to Higher Order Terms
To improve the approximation, more terms can be added to the polynomial, matching higher-order derivatives <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

*   **Third-order term (`c3*x^3`)**: The third derivative of `cosine(x)` is `sine(x)`, which is 0 at `x = 0` <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. The third derivative of `c3*x^3` is `1*2*3*c3` (or `3!*c3`) <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. Matching these means `c3` must be 0 <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
*   **Fourth-order term (`c4*x^4`)**: The fourth derivative of `cosine(x)` is `cosine(x)`, which is 1 at `x = 0` <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. The fourth derivative of `c4*x^4` is `1*2*3*4*c4` (or `4!*c4`), which is `24*c4` <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. Matching these means `c4` must be `1/24` <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

This leads to the improved approximation `1 - (1/2)x^2 + (1/24)x^4` <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>, which is a very close approximation for `cosine(x)` around `x = 0` <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. In physics problems with small angles, substituting this polynomial for `cosine(x)` yields almost unnoticeably different predictions <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.

### The Role of Factorials
When taking `n` successive [[derivatives_of_simple_functions_and_their_intuition | derivatives]] of `x^n`, the power rule repeatedly brings down the exponent, resulting in `n!` (n factorial) <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. Therefore, to ensure the polynomial's `nth` derivative matches the function's `nth` derivative, the coefficient of `x^n` must be the function's `nth` derivative (evaluated at the approximation point) *divided by* `n!` <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. This division by the factorial cancels out the cascading effect of the power rule applications <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.

### Approximating Near a Non-Zero Input
If approximating near an input other than 0, such as `x = a`, the polynomial is written in terms of powers of `(x - a)` <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>. All derivatives of the function are then evaluated at `a` <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. This effectively shifts the reference point so that plugging in `x = a` simplifies the polynomial to a single constant <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

### General Taylor Polynomial Formula
For a function `f(x)` approximated near `x = a`, the coefficient of each `(x - a)^n` term is the value of the `nth` derivative of `f` evaluated at `a`, divided by `n!` <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.

```markdown
$$
P_n(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + \dots + \frac{f^{(n)}(a)}{n!}(x-a)^n
$$
```
This formula ensures that:
*   The constant term matches the function's value at `a` <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.
*   The next term matches the slope (first derivative) at `a` <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.
*   Subsequent terms match the higher-order derivatives (rate of change of slope, etc.) at `a` <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.

The more terms included, the closer the approximation, but the polynomial becomes more complex <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.

## Geometric Intuition for the Second-Order Term
A geometric understanding of the second-order term relates to the [[derivative_of_polynomial_functions_using_geometric_visualization | fundamental theorem of calculus]] <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>. Consider an area function whose graph represents its derivative. If a slight nudge `dx` is applied to the right bound of the area, the new bit of area is approximately `height * dx` <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>. For more accuracy, especially for a change `x - a` that isn't infinitesimal, the triangular portion above the rectangle must be considered <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>.

The base of this triangle is `x - a`, and its height is `(slope of the graph) * (x - a)` <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>. Since the graph is the first derivative of the area function, its slope is the second derivative of the area function, evaluated at `a` <a class="yt-timestamp" data-t="00:16:08">[00:16:08]</a>. The area of this triangle (1/2 base * height) then becomes `(1/2) * (second derivative of area function at a) * (x - a)^2` <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>. This precisely matches the form of the second-order term in a [[constructing_taylor_polynomials | Taylor polynomial]] <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.

<div class="callout is-info">
The approximation of the area at `x` (given its derivatives at `a`) is:
*   The area up to `a` (`f(a)`) <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>.
*   Plus the area of the rectangle (`first derivative * (x - a)`) <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.
*   Plus the area of the triangle (`(1/2) * second derivative * (x - a)^2`) <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>.
</div>

## [[infinite_sums_and_approximations | Infinite Sums and Approximations]]: Taylor Series
While [[constructing_taylor_polynomials | Taylor polynomials]] involve a finite number of terms, an [[infinite_sums_and_approximations | infinite sum]] of terms is called a [[importance_of_taylor_series | Taylor series]] <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>. Adding infinitely many terms doesn't make sense in a direct computational way <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>. However, if adding more terms leads incrementally closer to a specific value, the series is said to [[convergence_and_divergence_of_taylor_series | converge]] to that value <a class="yt-timestamp" data-t="00:17:57">[00:17:57]</a>.

### Examples of Convergence
*   **e^x Taylor Series**: For `e^x` around `x = 0`, all its [[derivatives_of_simple_functions_and_their_intuition | derivatives]] are `e^x`, which equals 1 at `x = 0` <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>. Thus, its [[importance_of_taylor_series | Taylor series]] is `1 + x + x^2/2! + x^3/3! + ...` <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>. If `x = 1` is plugged in, the sum `1 + 1 + 1/2! + 1/3! + ...` converges to the value `e` <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>. For any `x`, the Taylor series for `e^x` converges to `e^x` <a class="yt-timestamp" data-t="00:18:53">[00:18:53]</a>. This is also true for `sine(x)` and `cosine(x)` <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.

### [[convergence_and_divergence_of_taylor_series | Divergence]] and Radius of Convergence
Sometimes, a [[importance_of_taylor_series | Taylor series]] only [[convergence_and_divergence_of_taylor_series | converges]] within a specific range around the input point used for derivative information <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>.
*   **Natural Logarithm Taylor Series**: The [[importance_of_taylor_series | Taylor series]] for `ln(x)` around `x = 1` converges for inputs between 0 and 2 <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>. Outside this range, the series fails to approach a specific value; it [[convergence_and_divergence_of_taylor_series | diverges]] <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>. Even if `ln(x)` is well-defined beyond this range, the derivative information at `x = 1` does not "propagate" that far <a class="yt-timestamp" data-t="00:20:28">[00:20:28]</a>.

The maximum distance between the approximation point and points where the polynomial outputs actually converge is called the **radius of convergence** for the [[importance_of_taylor_series | Taylor series]] <a class="yt-timestamp" data-t="00:20:44">[00:20:44]</a>.

## Conclusion
The fundamental intuition behind [[importance_of_taylor_series | Taylor series]] is their ability to translate information about a function's higher-order [[derivatives_of_simple_functions_and_their_intuition | derivatives]] at a single point into approximation information for the function near that point <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. This allows for powerful approximations of complex functions using simpler polynomials.