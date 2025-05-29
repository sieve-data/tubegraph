---
title: Constructing Taylor polynomials
videoId: 3d6DsjIBzJ4
---

From: [[3blue1brown]] <br/> 

[[importance_of_taylor_series | Taylor series]] are considered one of the most powerful tools in mathematics for [[approximation_of_functions_using_taylor_series | approximating functions]] <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. They frequently appear in various fields, including mathematics, physics, and engineering <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Why Approximate Functions with Polynomials?

The primary motive behind using Taylor polynomials is that [[generating_functions_and_polynomials | polynomials]] are generally much easier to manipulate than other types of functions <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. They are simpler to compute, differentiate, and integrate, making them "all around more friendly" <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

### Practical Application: The Pendulum Problem
A classic example of the utility of Taylor polynomials in [[applications_of_taylor_polynomials_in_physics | physics]] involves analyzing the potential energy of a pendulum <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. The expression for the pendulum's height above its lowest point is proportional to `1 - cos(theta)` <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. The `cosine` function makes the problem complex and obscures the relationship between pendulums and other oscillating phenomena <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

However, by approximating `cos(theta)` as `1 - (theta^2)/2`, the problem becomes significantly simpler <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. Graphing `cos(theta)` alongside `1 - (theta^2)/2` shows they are quite close, especially for small angles near 0 <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. The study of Taylor series focuses on finding polynomials that approximate non-polynomial functions near a specific input <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

## Step-by-Step Construction of a Taylor Polynomial

Let's construct a quadratic approximation for `cos(x)` near `x = 0`, in the form `c0 + c1*x + c2*x^2` <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. The goal is to find `c0`, `c1`, and `c2` such that the polynomial closely resembles `cos(x)` around `x = 0` <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

### 1. Matching the Function Value (c0)
At `x = 0`, `cos(x)` is `1` <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. For the approximation to be effective, it should also equal `1` at `x = 0` <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. Plugging `x = 0` into `c0 + c1*x + c2*x^2` yields `c0` <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
Thus, we set `c0 = 1` <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

### 2. Matching the First Derivative (c1)
To prevent the approximation from drifting too quickly from the original function, its tangent slope should match that of `cos(x)` at `x = 0` <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
*   The [[derivative_of_polynomial_functions_using_geometric_visualization | derivative]] of `cos(x)` is `-sin(x)`, which is `0` at `x = 0` (a flat tangent line) <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   The derivative of the polynomial `1 + c1*x + c2*x^2` is `c1 + 2*c2*x` <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. At `x = 0`, this is `c1` <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
Therefore, we set `c1 = 0` <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

### 3. Matching the Second Derivative (c2)
To ensure the curves bend at the same rate, their second derivatives should match <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   The second derivative of `cos(x)` (derivative of `-sin(x)`) is `-cos(x)`, which is `-1` at `x = 0` <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   The second derivative of the polynomial `1 + 0x + c2*x^2` (derivative of `0 + 2*c2*x`) is `2*c2` <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
Thus, `2*c2 = -1`, meaning `c2 = -1/2` <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

### Resulting Quadratic Approximation
The quadratic approximation for `cos(x)` near `x = 0` is `1 + 0x - (1/2)x^2`, or simply `1 - (1/2)x^2` <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. This approximation is highly accurate for small values, e.g., for `cos(0.1)`, it estimates `0.995`, which is very close to the true value <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

In summary:
*   `c0` ensures the value of the polynomial matches the function's value at `x = 0` <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   `c1` ensures the first derivatives (slopes) match at `x = 0` <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
*   `c2` ensures the second derivatives match, controlling the rate of change of the slope <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

### Extending to Higher Order Terms
To achieve even greater accuracy, more terms can be added to the polynomial, matching higher-order derivatives <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

*   **Third-order term (`c3*x^3`)**: The third derivative of `cos(x)` is `sin(x)`, which is `0` at `x = 0` <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. The third derivative of `c3*x^3` is `1*2*3*c3` <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. Setting them equal means `c3 = 0` <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. This implies `1 - (1/2)x^2` is also the best possible cubic approximation <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   **Fourth-order term (`c4*x^4`)**: The fourth derivative of `cos(x)` is `cos(x)`, which is `1` at `x = 0` <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. The fourth derivative of `c4*x^4` is `1*2*3*4*c4`, or `24*c4` <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. Setting them equal yields `24*c4 = 1`, so `c4 = 1/24` <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

The fourth-order approximation for `cos(x)` is `1 - (1/2)x^2 + (1/24)x^4` <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>. This polynomial is an even closer approximation for `cos(x)` around `x = 0` <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.

### Key Observations in the Process
1.  **Factorial Terms**: When taking `n` successive derivatives of `x^n`, the result is `n!` (n factorial) <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. Therefore, the coefficient of each `x^n` term is the `n`-th derivative of the function, divided by `n!` to cancel out this effect <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
2.  **Independence of Coefficients**: Adding higher-order terms to the polynomial does not change the values of the previously determined lower-order coefficients (e.g., `c0`, `c1`, `c2`) <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. This is because at `x = 0`, the derivatives of all higher-order terms become zero, isolating the control of each derivative to a single coefficient <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

## General Form of a Taylor Polynomial (Centered at `a`)

If approximating near an input `a` (instead of `0`), the polynomial is written in terms of powers of `(x - a)` <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>. All derivatives of the function `f(x)` are evaluated at `a` <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.

The general formula for a Taylor polynomial of degree `N` for a function `f(x)` centered at `a` is:

$$ P_N(x) = \sum_{n=0}^{N} \frac{f^{(n)}(a)}{n!}(x-a)^n $$ <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>

Where:
*   `f^(n)(a)` is the `n`-th derivative of `f(x)` evaluated at `a`.
*   `n!` is `n` factorial.
*   `(x-a)^n` is the `n`-th power of `(x-a)`.

This formula ensures that:
*   The constant term (`n=0`) matches the value of the function at `a` <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.
*   The `n=1` term matches the slope (first derivative) at `a` <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.
*   The `n=2` term matches the rate at which the slope changes (second derivative) at `a`, and so on <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.

The more terms included, the closer the approximation becomes, but the polynomial also becomes more complicated <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.

### Example: Taylor Polynomials for `e^x`
For `f(x) = e^x` centered at `x = 0`:
*   The derivative of `e^x` is `e^x` itself <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.
*   Thus, all derivatives of `e^x` evaluated at `x = 0` are `e^0 = 1` <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.

The Taylor polynomial for `e^x` centered at `0` is:
$$ 1 + 1x + \frac{1}{2!}x^2 + \frac{1}{3!}x^3 + \dots $$ <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>

## Geometric Interpretation of the Second Order Term
The second-order term of a Taylor polynomial can be understood geometrically by considering a function `f(x)` representing the area under some graph from a fixed left point to a variable right point `x` <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>.

According to the Fundamental Theorem of Calculus, the graph itself represents the [[derivative_of_polynomial_functions_using_geometric_visualization | derivative]] of this area function <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>. A small change `dx` in the right bound adds an area approximately `height * dx` (a rectangle) <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.

For a more accurate change in area over a larger `(x-a)` interval, we must account for a triangular portion in addition to the rectangle <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>.
*   The base of this triangle is `(x-a)` <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>.
*   The height of the triangle is the slope of the graph (which is the second derivative of the area function) multiplied by `(x-a)` <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.
*   The area of this triangle is `(1/2) * base * height = (1/2) * f''(a) * (x-a)^2` <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>.

This `(1/2) * f''(a) * (x-a)^2` term precisely matches the second-order term in the Taylor polynomial, visually representing how the curvature (second derivative) contributes to the approximation of the area function <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.

## From Taylor Polynomials to Taylor Series

While Taylor polynomials involve a finite number of terms, an infinite sum of these terms is called a [[generating_functions_and_polynomials | Taylor series]] <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>.

The concept of [[convergence_and_divergence_of_taylor_series | infinite series]] requires careful consideration. A series is said to [[convergence_and_divergence_of_taylor_series | converge]] to a specific value if, as more and more terms are added, the sum gets increasingly close to that value <a class="yt-timestamp" data-t="00:17:57">[00:17:57]</a>.

### Examples of Convergence
*   For `e^x`, plugging in `x = 1` into its Taylor series (i.e., `1 + 1 + 1/2! + 1/3! + ...`) shows that as more terms are added, the sum converges to the value `e` <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>. In fact, `e^x` equals its own Taylor series for *all* inputs `x`, even though the series is constructed from derivative information at `x = 0` <a class="yt-timestamp" data-t="00:18:47">[00:18:47]</a>.
*   Similar behavior is observed for `sine` and `cosine` functions <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.

### Examples of Divergence and Radius of Convergence
Sometimes, a Taylor series only converges within a specific range around the input used for derivative information <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>.
*   For example, the Taylor series for `ln(x)` centered at `x = 1` looks like:
    $$ (x-1) - \frac{1}{2}(x-1)^2 + \frac{1}{3}(x-1)^3 - \dots $$ <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>
    This series converges to `ln(x)` only for inputs between `0` and `2` <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>. Outside this range, the series [[convergence_and_divergence_of_taylor_series | diverges]], meaning adding more terms does not lead to a stable value, even if `ln(x)` is well-defined <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>.
*   The maximum distance between the approximation point and where the series converges is called the **radius of convergence** <a class="yt-timestamp" data-t="00:20:44">[00:20:44]</a>.

## Core Intuition
The fundamental intuition behind Taylor series is their ability to translate derivative information of a function at a single point into approximation information about the function's behavior around that point <a class="yt-timestamp" data-t="00:21:32">[00:21:32]</a>. This leverages local properties to estimate global behavior.