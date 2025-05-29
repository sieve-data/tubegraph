---
title: Using Taylor polynomials for function approximation
videoId: 3d6DsjIBzJ4
---

From: [[3blue1brown]] <br/> 

[[Importance of Taylor series in mathematics | Taylor series]] are a powerful mathematical tool for [[approximating_functions_using_taylor_series | approximating functions]] <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. They are widely used in mathematics, physics, and many fields of engineering <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Why Approximate Functions? A Pendulum Example

The utility of [[approximating_functions_using_taylor_series | approximating functions]] often becomes clear in practical problems <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. For instance, when studying the potential energy of a pendulum, the expression involves `1 - cos(theta)` <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. The cosine function can make the problem awkward, but by approximating `cos(theta)` as `1 - (theta^2)/2`, the problem becomes much simpler <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This approximation might seem arbitrary at first <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>, but when graphed, `cos(theta)` and `1 - (theta^2)/2` are quite close for small angles near 0 <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

The study of Taylor series primarily focuses on taking non-polynomial functions and finding polynomials that [[approximating_functions_using_taylor_series | approximate them]] near a specific input <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. Polynomials are generally easier to work with: they are simpler to compute, [[computing_derivatives_of_functions | differentiate]], and integrate <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

## Constructing a Taylor Polynomial for `cos(x)`

To construct a polynomial approximation, such as `c0 + c1*x + c2*x^2`, for a function like `cos(x)` near `x = 0`, the goal is to make its graph "spoon" with the function's graph at that point <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

1.  **Matching the Function Value**:
    *   At `x = 0`, `cos(x)` equals `1` <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
    *   For the polynomial to match, `c0` must be `1` (since plugging in `x = 0` yields `c0`) <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

2.  **Matching the First Derivative (Slope)**:
    *   The derivative of `cos(x)` is `-sin(x)`, which is `0` at `x = 0` (a flat tangent line) <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
    *   The derivative of the polynomial `c0 + c1*x + c2*x^2` is `c1 + 2*c2*x` <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
    *   At `x = 0`, this derivative is `c1` <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
    *   Therefore, `c1` must be `0` to match the slope <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. This prevents the approximation from drifting away too quickly <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

3.  **Matching the Second Derivative (Curvature)**:
    *   The second derivative of `cos(x)` is `-cos(x)`, which is `-1` at `x = 0` <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. This indicates a downward curve <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
    *   The second derivative of the polynomial is `2*c2` <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
    *   Thus, `2*c2` must be `-1`, meaning `c2 = -1/2` <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. Matching the second derivative ensures the polynomial curves at the same rate <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

The resulting quadratic approximation is `1 + 0x - (1/2)x^2`, or `1 - (1/2)x^2` <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. This provides a very good approximation, for example, `cos(0.1)` is estimated as `0.995` <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.

### Extending to Higher Order Terms

*   **Third Order (`c3*x^3`)**: The third derivative of `cos(x)` is `sin(x)`, which is `0` at `x = 0` <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. The third derivative of `c3*x^3` is `1*2*3*c3` <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. Thus, `c3` must be `0` <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. This means `1 - (1/2)x^2` is also the best cubic approximation <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   **Fourth Order (`c4*x^4`)**: The fourth derivative of `cos(x)` is `cos(x)` itself, which is `1` at `x = 0` <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. The fourth derivative of `c4*x^4` is `1*2*3*4*c4`, or `24*c4` <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. For these to match, `c4` must be `1/24` <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
    *   The approximation becomes `1 - (1/2)x^2 + (1/24)x^4` <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>, which is very close to `cos(x)` around `x = 0` <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.

### Key Observations

*   **Factorial Terms**: When taking `n` successive derivatives of `x^n`, the result is `n!` (n factorial) <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. To compensate for this, coefficients must be divided by the appropriate factorial <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. For example, the `x^4` coefficient was `1` (fourth derivative) divided by `4!` (`24`) <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.
*   **Independence of Terms**: Adding new higher-order terms does not change the values of previously determined lower-order coefficients <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. This is because when evaluating derivatives at `x = 0`, any term with an `x` factor will "wash away" <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. Each derivative at `x = 0` is controlled by one unique coefficient <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.
*   **Approximating Near Other Inputs**: If approximating near an input `a` (other than 0), the polynomial must be written in terms of powers of `(x - a)` <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>. This ensures that plugging in `x = a` results in similar cancellations <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.
*   **Philosophical Insight**: This process translates information about a function's higher-order derivatives at a single point into an approximation of the function's value near that point <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.

## General Form of Taylor Polynomials

For any function `f(x)`, its Taylor polynomial approximation near `x = a` is given by:

![[P_n(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + \dots + \frac{f^{(n)}(a)}{n!}(x-a)^n]]

*   The constant term `f(a)` ensures the polynomial's value matches `f(a)` <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.
*   The `(x-a)` term ensures the slope matches `f'(a)` <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.
*   The `(x-a)^2` term ensures the rate of change of the slope matches `f''(a)` <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.
*   Each subsequent term matches a higher-order derivative <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.

The more terms chosen, the closer the approximation, though the polynomial becomes more complex <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.

### Example: Taylor Polynomials for `e^x`

For `f(x) = e^x` approximated near `x = 0`:
*   The derivative of `e^x` is always `e^x` <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.
*   At `x = 0`, all derivatives are `e^0 = 1` <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.
*   Thus, the Taylor polynomial for `e^x` is `1 + 1x + (1/2!)x^2 + (1/3!)x^3 + ...` <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.

## Geometric Understanding of the Second Order Term

The [[concept_of_sample_approximation_in_integration | concept of sample approximation in integration]] and the [[fundamental_theorem_of_calculus | Fundamental Theorem of Calculus]] offer a geometric interpretation <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>.
Consider an area function `A(x)` whose derivative is the graph `f(x)` <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>.
*   The change in area `A(x) - A(a)` can be approximated by a rectangle (height `f(a)`, width `x-a`) and a triangle <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>.
*   The rectangle's area is `f(a) * (x-a)`, which is the first derivative term in the Taylor polynomial for the area function <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.
*   The triangle's base is `(x-a)` <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>. Its height is the slope of `f(x)` multiplied by `(x-a)` <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>. Since `f(x)` is the first derivative of the area function, its slope is the second derivative of the area function, `A''(a)` <a class="yt-timestamp" data-t="00:16:08">[00:16:08]</a>.
*   The triangle's area is `(1/2) * (base) * (height) = (1/2) * (x-a) * (A''(a)*(x-a))` which simplifies to `(1/2) * A''(a) * (x-a)^2` <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>. This is precisely the second-order term of the Taylor polynomial for the area function <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.

This [[visualizing_integration_and_approximations | visualization]] shows how each term in the Taylor polynomial corresponds to a geometric component of the area change <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.

## Taylor Series: Infinite Sums and Convergence

An infinite sum in mathematics is called a series <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>. While Taylor polynomials involve finitely many terms, adding all infinitely many terms results in a Taylor series <a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a>.

*   A series **converges** if adding more and more terms gets increasingly close to a specific value <a class="yt-timestamp" data-t="00:17:57">[00:17:57]</a>. If this happens, the series is said to [[understanding_taylor_series_convergence | converge]] to that value <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.
*   For `e^x`, its Taylor series (for `x=1`) converges to the number `e` <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>. In fact, `e^x` equals its own Taylor series for any input `x`, regardless of distance from 0 <a class="yt-timestamp" data-t="00:18:47">[00:18:47]</a>. This is also true for sine and cosine <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.

### Radius of Convergence

Sometimes, a Taylor series only [[understanding_taylor_series_convergence | converges]] within a certain range around the input used for derivative information <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>.
*   For example, the Taylor series for `ln(x)` around `x = 1` converges only for inputs between `0` and `2` <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>. Outside this range, the series **diverges**, meaning the sum bounces wildly and doesn't approach a specific value <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>.
*   The maximum distance between the approximation point and where the series converges is called the [[understanding_taylor_series_convergence | radius of convergence]] <a class="yt-timestamp" data-t="00:20:44">[00:20:44]</a>.

Taylor series have numerous [[applications_of_taylor_series_in_physics_and_engineering | applications in physics and engineering]] and mathematics <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>. The fundamental intuition to remember is that they translate derivative information at a single point into approximation information around that point <a class="yt-timestamp" data-t="00:21:32">[00:21:32]</a>.