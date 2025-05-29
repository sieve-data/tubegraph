---
title: Applications of Taylor polynomials in physics
videoId: 3d6DsjIBzJ4
---

From: [[3blue1brown]] <br/> 

[[importance_of_taylor_series | Taylor series]] are a fundamental tool in mathematics, physics, and various fields of engineering due to their power in [[approximation_of_functions_using_taylor_series | approximating functions]] <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. Polynomials are generally easier to compute, differentiate, and integrate, making them more manageable than other types of functions <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. The study of [[constructing_taylor_polynomials | Taylor series]] focuses on transforming non-polynomial functions into polynomials that approximate them closely around a specific input <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

## Pendulum Problem Example

A key illustration of their utility comes from physics, specifically when dealing with the potential energy of a pendulum <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. The expression for the pendulum's height above its lowest point is proportional to `1 - cosine(angle)` <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. The cosine function in this context made the problem "awkward and unwieldy," obscuring the relationship between pendulums and other oscillating phenomena <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

By approximating `cosine(theta)` as `1 - theta^2 / 2`, the problem became significantly simpler and "fell into place much more easily" <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This quadratic approximation for cosine is particularly effective for small angles near 0 <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. In any physics problem involving the cosine of a small angle, substituting this polynomial for `cosine(x)` yields predictions that are "almost unnoticeably different" <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.

### Why this Approximation Works

The construction of such an approximation, known as a [[constructing_taylor_polynomials | Taylor polynomial]], involves matching the function's value and its derivatives at a specific point (e.g., `x = 0` for `cosine(x)`) <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>:

*   The constant term `c0` ensures the polynomial's value matches the function's value at `x = 0` <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. For `cosine(x)`, `c0 = 1`.
*   The `c1` term ensures the polynomial's slope matches the function's slope at `x = 0` <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. For `cosine(x)`, `c1 = 0`.
*   The `c2` term ensures the polynomial's second derivative matches the function's second derivative at `x = 0` <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. For `cosine(x)`, `c2 = -1/2`, leading to the term `-1/2 x^2` <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

This matching of derivatives means that the polynomial's change and its rate of change (and higher-order changes) are as similar as possible to the original function's behavior around that point <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. Adding more terms to the polynomial allows for matching higher-order derivatives, leading to even closer approximations <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. For example, for `cosine(x)`, adding a fourth-order term `(1/24)x^4` results in a very close approximation `1 - (1/2)x^2 + (1/24)x^4` <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

## General Significance

Taylor polynomials provide a powerful method for approximating complex functions using simpler polynomials, which is invaluable in fields like physics where exact solutions to equations involving non-polynomial functions can be challenging <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. They translate derivative information of a function at a single point into information about the function's value near that point <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>. This allows physicists to simplify models and gain insights into system behavior, especially for small perturbations or oscillations.