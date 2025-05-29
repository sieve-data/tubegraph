---
title: Convergence and divergence of Taylor series
videoId: 3d6DsjIBzJ4
---

From: [[3blue1brown]] <br/> 

When first learning about [[importance_of_taylor_series | Taylor series]], their significance may not be immediately apparent <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. However, they are a powerful mathematical tool for [[approximation_of_functions_using_taylor_series | approximating functions]] and frequently appear in mathematics, [[applications_of_taylor_polynomials_in_physics | physics]], and various fields of engineering <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## From Taylor Polynomials to Taylor Series

The study of [[constructing_taylor_polynomials | Taylor series]] primarily involves taking non-polynomial functions and finding polynomials that approximate them near a specific input <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. Polynomials are generally easier to compute, derive, and [[evaluating_integrals_and_the_role_of_the_convergence_point | integrate]] than other functions <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

[[constructing_taylor_polynomials | Taylor polynomials]] are approximations that stop at a finite number of terms <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. This process of creating an approximation involves matching the function's value, slope, and higher-order derivatives at a specific point, often `x = 0` <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>. More terms in the polynomial generally lead to a closer approximation, but also a more complicated polynomial <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.

However, a fundamental question in mathematics arises: does it make sense to add infinitely many terms to a polynomial approximation <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>?

## Concept of Infinite Sums and Convergence

An infinite sum in mathematics is called a series <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>. While [[constructing_taylor_polynomials | Taylor polynomials]] have finitely many terms, adding all infinitely many terms creates what is known as a Taylor series <a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a>.

It is critical to be careful with the idea of an infinite series, as one cannot physically add infinitely many numbers <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a>.

> [!NOTE] Convergence
> If a series is such that adding more and more terms progressively gets closer to some specific value, the series is said to **converge** to that value <a class="yt-timestamp" data-t="00:17:57">[00:17:57]</a>. If comfortable, one can extend the definition of equality to say that the infinite sum equals the value it is converging to <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.

For instance, consider the [[constructing_taylor_polynomials | Taylor polynomial]] for *e<sup>x</sup>* <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>. When an input like `x = 1` is plugged in, as more polynomial terms are added, the sum gets increasingly closer to the value of *e* <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>. Therefore, this infinite series for *e<sup>x</sup>* converges to *e* <a class="yt-timestamp" data-t="00:18:36">[00:18:36]</a>. This holds true for any input `x`; the higher-order [[constructing_taylor_polynomials | Taylor polynomials]] will converge towards *e<sup>x</sup>* <a class="yt-timestamp" data-t="00:18:47">[00:18:47]</a>. Thus, *e<sup>x</sup>* equals its own [[importance_of_taylor_series | Taylor series]] for all inputs `x` <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>. The same is true for functions like sine and cosine <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.

## Divergence of Taylor Series and Radius of Convergence

Sometimes, however, [[importance_of_taylor_series | Taylor series]] only converge within a specific range around the input point whose derivative information is used <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>.

> [!WARNING] Divergence
> In cases where adding more terms of the series does not approach any specific value, the series is said to **diverge** <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>.

For example, the [[importance_of_taylor_series | Taylor series]] for the natural logarithm of *x* around the input `x = 1` looks like this <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>:
When an input between 0 and 2 is used, adding more terms of this series will approach the natural logarithm of that input <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>. However, outside of this range, the series fails to approach anything; the sum bounces wildly as more terms are added <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>. This happens even though the natural log of *x* is well-defined for inputs above 2 <a class="yt-timestamp" data-t="00:20:22">[00:20:22]</a>. In such a scenario, the derivative information of ln(*x*) at `x = 1` does not propagate out indefinitely <a class="yt-timestamp" data-t="00:20:28">[00:20:28]</a>.

The maximum distance between the input point of approximation and the points where the outputs of these polynomials actually converge is called the **radius of convergence** for the [[importance_of_taylor_series | Taylor series]] <a class="yt-timestamp" data-t="00:20:44">[00:20:44]</a>.

## Further Learning
There are many more aspects to [[importance_of_taylor_series | Taylor series]], including various use cases, methods for bounding approximation errors, and tests to determine when series converge or diverge <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>. The fundamental intuition to remember is that [[importance_of_taylor_series | Taylor series]] translate derivative information at a single point into approximation information around that point <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a>. This topic is part of a broader [[introduction_to_calculus_series | calculus series]] <a class="yt-timestamp" data-t="00:21:07">[00:21:07]</a>.