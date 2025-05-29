---
title: Approximating functions using Taylor series
videoId: 3d6DsjIBzJ4
---

From: [[3blue1brown]] <br/> 

[[importance_of_taylor_series_in_mathematics | Taylor series]] are considered one of the most powerful mathematical tools for [[using_taylor_polynomials_for_function_approximation | approximating functions]] <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. They frequently appear across various fields, including mathematics, physics, and engineering <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. The primary purpose of [[using_taylor_polynomials_for_function_approximation | Taylor series]] is to find polynomials that approximate non-polynomial functions near a specific input <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. Polynomials are generally easier to work with than other functions, being simpler to compute, differentiate, and integrate <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

## Motivation through a Physics Problem

The utility of function approximation becomes clear in problems where complex functions make calculations unwieldy <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. For instance, when studying the potential energy of a pendulum, the height of the pendulum's weight above its lowest point is proportional to `1 - cos(θ)`, where `θ` is the angle between the pendulum and the vertical <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. The `cos(θ)` term can complicate the problem and obscure relationships with other oscillating phenomena <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

By approximating `cos(θ)` as `1 - θ²/2`, the problem significantly simplifies <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. Graphing `cos(θ)` alongside `1 - θ²/2` shows they are very close for small angles near zero <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. The question then becomes how to systematically find such a polynomial approximation <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

## Constructing a Quadratic Approximation for cos(x) near x=0

To construct a polynomial approximation, such as `c₀ + c₁x + c₂x²`, that resembles `cos(x)` near `x=0`, we match the function's value and its derivatives at that point <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

1.  **Matching the Value (c₀)**:
    *   At `x=0`, `cos(x)` is `1` <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
    *   For the polynomial, plugging in `x=0` yields `c₀` <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
    *   Therefore, `c₀` must be `1` to ensure the approximation equals `1` at `x=0` <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
    *   `c₀` is responsible for matching the output of the approximation with `cos(x)` at `x=0` <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

2.  **Matching the First Derivative (c₁)**:
    *   The derivative of `cos(x)` is `-sin(x)`, which is `0` at `x=0`, indicating a flat tangent line <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
    *   The derivative of the quadratic `c₀ + c₁x + c₂x²` is `c₁ + 2c₂x` <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
    *   At `x=0`, this derivative is `c₁` <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
    *   Setting `c₁` to `0` ensures the approximation has the same flat tangent line at `x=0` <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
    *   `c₁` is in charge of making sure the derivatives match at `x=0` <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

3.  **Matching the Second Derivative (c₂)**:
    *   `cos(x)` curves downward around `x=0`, indicating a negative second derivative <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
    *   The second derivative of `cos(x)` (`-cos(x)`) is `-1` at `x=0` <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
    *   The second derivative of the polynomial `c₀ + c₁x + c₂x²` is `2c₂` <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
    *   Setting `2c₂ = -1` means `c₂` should be `-1/2` <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
    *   This ensures the polynomial's slope changes at the same rate as `cos(x)`'s <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
    *   `c₂` is responsible for making sure the second derivatives match up <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

This process yields the quadratic approximation `1 + 0x - ½x²`, or `1 - ½x²` <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. For example, `cos(0.1)` is estimated as `0.995`, which is very close to the true value <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. The constants `c₀`, `c₁`, and `c₂` control the approximation's value, slope, and curvature, respectively <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.

## Extending to Higher Order Terms

To improve the approximation, one can add more terms to the polynomial and match higher-order derivatives <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

*   **Third-order term (c₃x³)**: The third derivative of `cos(x)` is `sin(x)`, which is `0` at `x=0` <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. The third derivative of `c₃x³` is `1 * 2 * 3 * c₃` <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. Thus, `c₃` must be `0` <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
*   **Fourth-order term (c₄x⁴)**: The fourth derivative of `cos(x)` is `cos(x)` itself, which is `1` at `x=0` <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. The fourth derivative of `c₄x⁴` is `1 * 2 * 3 * 4 * c₄`, or `24c₄` <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. So, `c₄` must be `1/24` <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

The resulting fourth-order approximation `1 - ½x² + 1/24x⁴` is a very close approximation for `cos(x)` around `x=0` <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.

### Key Observations:
*   **Factorials**: When taking `n` successive derivatives of `xⁿ`, the result is `n!` (n factorial) <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. Therefore, the coefficient of each `xⁿ` term is the nth derivative of the function divided by `n!` to cancel out this effect <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
*   **Independence of Coefficients**: Adding new higher-order terms does not change the values of previously determined lower-order coefficients <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. This is because when evaluating derivatives at `x=0`, any term with an `x` factor will "wash away" <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.
*   **Approximation Around a Point 'a'**: If approximating near an input `a` other than `0`, the polynomial should be written in terms of powers of `(x-a)` <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>. All derivatives of the function would then be evaluated at `a` <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.

## General Form of Taylor Polynomials

[[using_taylor_polynomials_for_function_approximation | Taylor polynomials]] translate derivative information at a single point into approximation information around that point <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.

For a function `f(x)` approximated near `x=0` (also known as a Maclaurin polynomial), the coefficient of each `xⁿ` term is the value of the nth derivative of the function evaluated at `0`, divided by `n!` <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>. This ensures:
*   The constant term matches the function's value <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.
*   The `x` term matches the function's slope <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.
*   The `x²` term matches how the slope changes <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.
*   And so on for higher terms <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.

The more terms chosen, the closer the approximation, but the polynomial becomes more complicated <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.

In full generality, for an approximation near an input `a`, [[using_taylor_polynomials_for_function_approximation | Taylor polynomials]] are written in terms of powers of `(x-a)`, and all derivatives of `f` are evaluated at `a` <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>. Changing `a` shifts where the approximation "hugs" the original function <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.

### Example: Taylor Polynomials for e^x near x=0

The function `e^x` provides a simple example <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.
*   All derivatives of `e^x` are `e^x` <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.
*   At `x=0`, all derivatives evaluate to `1` <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.
*   Therefore, the Taylor polynomial approximation for `e^x` near `x=0` looks like: `1 + 1x + 1/2! x² + 1/3! x³ + ...` <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.

## Geometric Understanding of Taylor Polynomials (Second Order Term)

A geometric interpretation of the second-order term can be derived from the [[visualizing_integration_and_approximations | Fundamental Theorem of Calculus]] <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>. Consider a function `f(x)` that represents the area under some graph from a fixed left point to a variable right point `x` <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>. The graph itself represents the derivative of this area function <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>.

To approximate the change in this area function `f(x)` from `a` to `x`:
*   The first-order term corresponds to the area of a rectangle with height `f'(a)` (the value of the graph at `a`) and width `(x-a)` <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>. This matches `f'(a)(x-a)`.
*   The second-order term approximates the "triangular" portion of the area above this rectangle <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>. The base of this "triangle" is `(x-a)`, and its height is the change in the graph's value over that interval, approximately `f''(a)(x-a)` (slope of the graph times the base) <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>.
*   The area of this approximate triangle is `½ * base * height = ½ * (x-a) * f''(a)(x-a) = ½ * f''(a) * (x-a)²` <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>. This exactly matches the second-order term in a Taylor polynomial <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.

This geometric interpretation clearly shows how each term in a Taylor polynomial accounts for different aspects of the function's behavior around the point of approximation <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.

## From Taylor Polynomials to Taylor Series

While [[using_taylor_polynomials_for_function_approximation | Taylor polynomials]] use a finite number of terms, an [[understanding_taylor_series_convergence | infinite sum]] of terms is called a [[understanding_taylor_series_convergence | Taylor series]] <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>. An infinite sum doesn't literally mean adding infinitely many things, but rather considering whether the sum of more and more terms approaches a specific value <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>.

### Series Convergence and Divergence
*   **Convergence**: If adding more terms gets increasingly close to a specific value, the series is said to converge to that value <a class="yt-timestamp" data-t="00:17:57">[00:17:57]</a>. In such cases, the infinite series is considered equal to the value it converges to <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.
    *   For example, plugging `x=1` into the Taylor polynomial for `e^x` and adding more terms causes the sum to converge towards `e` <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>. Similarly, for any `x`, the Taylor series for `e^x` converges to `e^x` <a class="yt-timestamp" data-t="00:18:47">[00:18:47]</a>. This is also true for `sin(x)` and `cos(x)` <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.
*   **Divergence**: Sometimes, the series only converges within a specific range around the input where the derivative information was gathered <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>. Outside this range, the series might fail to approach anything, with the sum bouncing wildly as more terms are added <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>. In this case, the series diverges <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>.
    *   For instance, the Taylor series for `ln(x)` around `x=1` converges for `x` values between `0` and `2`, but diverges outside this range <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>.
*   **Radius of Convergence**: The maximum distance between the approximation point and where the series converges is called the radius of convergence <a class="yt-timestamp" data-t="00:20:44">[00:20:44]</a>.

The fundamental intuition behind [[using_taylor_polynomials_for_function_approximation | Taylor series]] is that they translate derivative information at a single point into approximation information around that point <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a>.