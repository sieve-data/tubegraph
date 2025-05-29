---
title: Importance of Taylor series in mathematics
videoId: 3d6DsjIBzJ4
---

From: [[3blue1brown]] <br/> 

Taylor series are considered one of the most powerful tools mathematics offers for [[approximating_functions_using_taylor_series | approximating functions]] <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. They frequently appear in mathematics, physics, and various engineering fields <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Approximating Functions with Polynomials

The study of Taylor series primarily involves transforming non-polynomial functions into polynomials that closely approximate them near a specific input <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. Polynomials are generally preferred in [[the_importance_of_calculations_in_mathematics | mathematical calculations]] because they are much simpler to work with: they are easier to compute, differentiate, and integrate <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

### Practical Application: Pendulum Potential Energy

An early practical illustration of Taylor series' utility can be found in physics, particularly when dealing with the potential energy of a pendulum <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. The potential energy is proportional to `1 - cos(theta)`, where `theta` is the angle between the pendulum and the vertical <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. The cosine function can make such problems awkward and unwieldy, obscuring the relationship between pendulums and other oscillating phenomena <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

By [[using_taylor_polynomials_for_function_approximation | approximating cosine of theta]] as `1 - theta^2 / 2` for small angles near 0, the problem becomes much simpler to solve <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This approximation is visually close to `cos(theta)` on a graph, especially for small angles <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

### Constructing a Polynomial Approximation (Taylor Polynomials)

To find such a polynomial approximation, like `1 - x^2 / 2` for `cos(x)` near `x = 0`, the process involves matching the function's value and its successive derivatives at the point of interest <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

Consider a quadratic polynomial `P(x) = c0 + c1*x + c2*x^2` to approximate `cos(x)` near `x = 0`:

1.  **Matching Function Value (`c0`)**:
    *   At `x = 0`, `cos(x) = 1` <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
    *   The polynomial `P(0) = c0` <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
    *   Therefore, `c0` must be `1` to ensure the approximation matches the function's value at `x = 0` <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

2.  **Matching First Derivative (Slope, `c1`)**:
    *   The derivative of `cos(x)` is `-sin(x)`, which is `0` at `x = 0` (a flat tangent line) <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
    *   The derivative of `P(x)` is `c1 + 2*c2*x` <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
    *   At `x = 0`, `P'(0) = c1` <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
    *   Setting `c1 = 0` ensures the polynomial's tangent line matches `cos(x)` at `x = 0` <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

3.  **Matching Second Derivative (Curvature, `c2`)**:
    *   The second derivative of `cos(x)` is `-cos(x)`, which is `-1` at `x = 0` (curves downward) <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
    *   The second derivative of `P(x)` is `2*c2` <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
    *   Setting `2*c2 = -1` means `c2 = -1/2` <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

This leads to the quadratic approximation `P(x) = 1 + 0x - (1/2)x^2 = 1 - (1/2)x^2` <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. This approximation is highly accurate for values close to `x = 0`, for example, `cos(0.1)` is approximated as `0.995` <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

### Extending to Higher Order Terms

*   **Third Order (`c3*x^3`)**: The third derivative of `cos(x)` is `sin(x)`, which is `0` at `x = 0` <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. The third derivative of `c3*x^3` is `1*2*3*c3` <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. Thus, `c3` must be `0` <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. This means `1 - (1/2)x^2` is also the best possible cubic approximation <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   **Fourth Order (`c4*x^4`)**: The fourth derivative of `cos(x)` is `cos(x)` again, which is `1` at `x = 0` <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. The fourth derivative of `c4*x^4` is `1*2*3*4*c4` (or `4!*c4`) <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. To match, `c4` must be `1/24` <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
    *   This leads to the improved approximation `1 - (1/2)x^2 + (1/24)x^4` <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.

This iterative process of matching derivatives ensures that the polynomial's behavior (value, slope, curvature, and higher-order changes) closely mirrors that of the original function near the chosen point <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. Each coefficient `cn` of an `x^n` term is responsible for matching the nth derivative of the function at `x=0` <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.

### The Role of Factorials

When taking `n` successive derivatives of `x^n`, the result is `n!` (n factorial) <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. To ensure the polynomial's `n`-th derivative matches the function's `n`-th derivative at `x = 0`, the coefficient of `x^n` is not simply the `n`-th derivative value, but that value *divided by* `n!` <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. This cancels out the cascading effect of the power rule applications <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.

### Approximating Near a Non-Zero Input

If approximating near an input `a` other than `0`, the polynomial is written in terms of powers of `(x - a)`, and all derivatives are evaluated at `a` <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

### The General Taylor Polynomial Formula

The general formula for a Taylor polynomial approximation for a function `f(x)` around `x = a` is:

> `P(x) = f(a) + f'(a)(x-a) + (f''(a)/2!)(x-a)^2 + (f'''(a)/3!)(x-a)^3 + ... + (f^(n)(a)/n!)(x-a)^n` <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a> <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>

Here:
*   The constant term `f(a)` matches the value of `f` at `a` <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.
*   The `(x-a)` term matches the slope <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.
*   The `(x-a)^2` term matches the rate at which the slope changes (curvature) <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.
*   And so on for higher terms <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.

The more terms chosen, the closer the approximation, but the polynomial becomes more complex <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.

### Example: Taylor Polynomials for `e^x`

For the function `e^x` around `x = 0`, all its derivatives are `e^x`, which evaluate to `1` at `x = 0` <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.
The Taylor polynomials for `e^x` therefore look like:

> `1 + 1*x + (1/2!)*x^2 + (1/3!)*x^3 + ...` <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>

## Geometric Understanding of the Second Order Term

The second-order term of Taylor polynomials can also be understood geometrically, relating to the [[mathematical_analysis_of_fourier_series | Fundamental Theorem of Calculus]] and area approximation <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>.

Consider a function representing the area under a graph, from a fixed left point to a variable right point `x` <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>. The graph itself is the derivative of this area function <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>.

If `a` is the starting input and `x` is the nudged input (`x-a` being the change):
*   The initial area up to `a` is `f(a)` <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>.
*   The area of the main rectangle is `f'(a) * (x-a)` <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.
*   The additional triangular area for increased accuracy is `(1/2) * f''(a) * (x-a)^2` <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>.

This geometric interpretation clearly shows how the terms correspond to the function's value, its rate of change (slope), and the rate of change of its slope (curvature) in the context of approximating the area function <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.

## Taylor Series: Infinite Sums and Convergence

While Taylor polynomials involve a finite number of terms, an [[infinite_series_and_sum_computations | infinite sum]] of terms is called a Taylor series <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>.

### Understanding Convergence

An infinite series converges to a specific value if adding more and more terms gets increasingly close to that value <a class="yt-timestamp" data-t="00:17:57">[00:17:57]</a>. If a series converges, it can be said that the series "equals" the value it converges to <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.

For example, when `x = 1` is plugged into the Taylor polynomial for `e^x`, as more terms are added, the sum approaches the value of [[importance_of_eulers_number_e_in_calculus | Euler's number e]] <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>. For `e^x`, its Taylor series converges to `e^x` for *any* input `x`, regardless of how far it is from `0` <a class="yt-timestamp" data-t="00:18:47">[00:18:47]</a>. This is also true for `sin(x)` and `cos(x)` <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.

### Radius of Convergence

However, for some functions, Taylor series only converge within a specific range around the input where the derivative information was gathered <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>.

For example, the Taylor series for `ln(x)` around `x = 1` converges only for inputs between `0` and `2` <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>. Outside this range, the series *diverges*, meaning adding more terms does not approach a specific value <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>. The maximum distance from the approximation point where the series converges is called the [[understanding_taylor_series_convergence | radius of convergence]] <a class="yt-timestamp" data-t="00:20:44">[00:20:44]</a>.

## Core Intuition of Taylor Series

The fundamental intuition behind Taylor series is that they translate derivative information from a single point of a function into approximation information about the function's behavior around that point <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a>. This means a lot can be learned about a function's behavior in an interval by knowing its value and the values of its derivatives at just one point <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.

## Further Study

[[applications_of_taylor_series_in_physics_and_engineering | Taylor series]] have numerous use cases, including error bounding for approximations and tests to determine series convergence or divergence <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>.