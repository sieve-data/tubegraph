---
title: Importance of Taylor series
videoId: 3d6DsjIBzJ4
---

From: [[3blue1brown]] <br/> 

Taylor series are a fundamental and powerful tool in mathematics, physics, and various fields of engineering <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. They are primarily used for [[approximation_of_functions_using_taylor_series | approximating functions]] <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. The core idea behind Taylor series is to approximate non-polynomial functions using polynomials <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. This is highly advantageous because polynomials are generally much easier to work with; they are simpler to compute, differentiate, and integrate <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

## Applications in Physics

The utility of Taylor series often becomes clear in practical applications, such as in physics <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. For instance, when analyzing the potential energy of a pendulum, an expression involving the cosine of the angle arises <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. This cosine function can make problems awkward and unwieldy, obscuring connections to other oscillating phenomena <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. However, by approximating `cosine(θ)` as `1 - θ²/2`, the problem simplifies significantly, allowing for easier solutions <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. For small angles, this polynomial substitution yields predictions that are almost unnoticeably different from using the exact cosine function <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.

## [[constructing_taylor_polynomials | Constructing Taylor Polynomials]]

The process of constructing Taylor polynomials involves matching the derivatives of a given function at a specific point. For a quadratic approximation of a function like `cosine(x)` near `x = 0`, a polynomial of the form `c₀ + c₁x + c₂x²` is used <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

*   **Matching Value (c₀)**: At `x = 0`, `cosine(0) = 1`. To ensure the approximation is accurate at this point, the polynomial must also equal `1` at `x = 0`. Plugging in `0` into the polynomial reveals that `c₀` must be `1` <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
*   **Matching First Derivative (c₁)**: To prevent the approximation from drifting quickly, its tangent slope should match that of `cosine(x)` at `x = 0` <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. The derivative of `cosine(x)` is `-sine(x)`, which is `0` at `x = 0` <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. The derivative of the polynomial `c₀ + c₁x + c₂x²` is `c₁ + 2c₂x`. At `x = 0`, this equals `c₁`. Therefore, `c₁` is set to `0` <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Matching Second Derivative (c₂)**: To ensure the polynomial curves at the same rate as the function, their second derivatives must match <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. The second derivative of `cosine(x)` is `-cosine(x)`, which is `-1` at `x = 0` <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. The second derivative of the polynomial is `2c₂`. Setting `2c₂ = -1` means `c₂ = -1/2` <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

This yields the quadratic approximation `1 - (1/2)x²` for `cosine(x)` near `x = 0` <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. This method ensures that the polynomial's value, slope, and rate of slope change align with the original function, maximizing accuracy given the number of terms <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

### Generalization

By adding more terms (e.g., `c₃x³`, `c₄x⁴`), higher-order derivatives can be matched <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. For `cosine(x)`:
*   The third derivative is `sine(x)`, which is `0` at `x = 0`, so `c₃ = 0` <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
*   The fourth derivative is `cosine(x)`, which is `1` at `x = 0` <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. To match, the coefficient `c₄` must be `1/(4!) = 1/24` <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

The resulting polynomial `1 - (1/2)x² + (1/24)x⁴` provides an even closer approximation <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>. This process naturally introduces factorial terms in the denominators of the coefficients, which cancel out the cascading effect of repeated applications of the power rule <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. Crucially, adding higher-order terms does not change the coefficients of lower-order terms when approximating around `x = 0`, because derivatives of higher-order terms become zero when `x = 0` is plugged in <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

For approximation near an input `a` (not `0`), the polynomial is expressed in terms of powers of `(x - a)`, and all derivatives are evaluated at `a` <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>. The general formula for a Taylor polynomial is:
`f(a) + f'(a)(x-a) + f''(a)/2!(x-a)² + f'''(a)/3!(x-a)³ + ...` <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>

### Example: Taylor Polynomials for e^x

The function `e^x` is particularly well-suited for Taylor series because its derivatives are all `e^x` itself <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>. At `x = 0`, all derivatives of `e^x` are `1` <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>. Thus, its Taylor polynomials around `x = 0` look like:
`1 + 1x + (1/2!)x² + (1/3!)x³ + ...` <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>

## Geometric Intuition

Taylor polynomials can also be understood geometrically, particularly in connection with the [[introduction_to_calculus_series | Fundamental Theorem of Calculus]] <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>. If `f(x)` represents the derivative of an area function `A(x)`, then approximating `A(x)` near `x = a` involves:
*   The area up to `a` (`A(a)`).
*   The rectangular area `f(a)(x-a)`.
*   The triangular area `(1/2)f'(a)(x-a)²` <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>.
This geometric interpretation clearly shows how the terms of a Taylor polynomial correspond to progressively more accurate approximations of the area under a curve, reflecting the value, slope, and curvature of the area function.

## Taylor Series vs. Taylor Polynomials

While Taylor polynomials involve a finite number of terms, an infinite sum of all terms is called a Taylor series <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>.

### [[convergence_and_divergence_of_taylor_series | Convergence and Divergence]]

The concept of an infinite sum requires careful definition: a series [[convergence_and_divergence_of_taylor_series | converges]] if adding more terms gets increasingly close to a specific value <a class="yt-timestamp" data-t="00:17:57">[00:17:57]</a>. For example, the Taylor series for `e^x` at `x = 1` converges to the value `e` <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>. Remarkably, for `e^x`, its Taylor series converges to `e^x` for *any* input `x`, even though it's constructed from derivative information at a single point (`x = 0`) <a class="yt-timestamp" data-t="00:19:04">[00:19:04]</a>. Similarly, Taylor series for `sine` and `cosine` also converge across their entire domains <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.

However, not all Taylor series converge for all inputs. The Taylor series for the natural logarithm `ln(x)` around `x = 1` only converges for inputs between `0` and `2` <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>. Outside this range, the series [[convergence_and_divergence_of_taylor_series | diverges]], meaning the sum of terms does not approach a specific value <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>. The maximum distance from the approximation point within which the series converges is called the radius of convergence <a class="yt-timestamp" data-t="00:20:44">[00:20:44]</a>.

## Conclusion

Taylor series offer a profound way to translate information about a function's higher-order derivatives at a single point into an accurate approximation of the function's behavior around that point <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>. This core intuition is crucial for understanding their wide-ranging utility and significance in various scientific and engineering disciplines <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a>.