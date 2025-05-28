---
title: Isaac Newtons approach to estimating Pi
videoId: gMlf1ELvRzc
---

From: [[veritasium]] <br/> 

For 2000 years, the most successful method for calculating Pi was painstakingly slow and tedious <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. However, Isaac Newton "speed-ran Pi" by introducing a revolutionary new method <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Understanding Pi

Pi (π) represents the ratio of a circle's circumference to its diameter, approximately 3.14 <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. It is also fundamentally related to a circle's area, given by the formula Pi R squared (πr²) <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. This formula can be visualized by cutting a circle into thin slices and rearranging them to form a rectangle, where the length is half the circumference (πR) and the width is the radius (R) <a class="yt-timestamp" data-t="00:00:48">[00:01:10]</a>. Therefore, the area of a unit circle (radius = 1) is simply Pi <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

## Traditional Methods of Calculating Pi

The most obvious initial approach to calculating Pi involved approximating a circle with polygons <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. It was known for thousands of years that Pi must be between three and four, by comparing the perimeter of an inscribed hexagon and a circumscribed square to a circle's circumference <a class="yt-timestamp" data-t="00:01:33">[00:02:16]</a>.

### Archimedes' Method
Around 250 BC, [[archimedes_method_for_calculating_pi | Archimedes]] significantly improved upon this by repeatedly bisecting polygons <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. He started with a hexagon, then bisected it to a 12-sided polygon (dodecagon), calculating its perimeter to find a lower bound for Pi <a class="yt-timestamp" data-t="00:02:27">[00:02:40]</a>. He did the same for a circumscribed 12-gon to find an upper bound <a class="yt-timestamp" data-t="00:02:41">[00:02:45]</a>. These calculations were complex, involving square roots and fractions <a class="yt-timestamp" data-t="00:02:48">[00:02:54]</a>. By the time he reached a 96-gon, [[archimedes_method_for_calculating_pi | Archimedes]] had Pi between 3.1408 and 3.1429 <a class="yt-timestamp" data-t="00:03:01">[00:03:11]</a>.

### Continuation of Polygon Bisection Methods
For the next 2000 years, mathematicians from various cultures, including Chinese, Indian, Persian, and Arab scholars, continued to bisect polygons to achieve greater precision, contributing to the [[history_of_pi_calculation_methods | history of Pi calculation methods]] <a class="yt-timestamp" data-t="00:03:33">[00:03:48]</a>.
Notable figures in the [[contributions_of_renaissance_mathematicians | Renaissance]] period included:
*   **Francois Viete** (late 16th century): Doubled [[archimedes_method_for_calculating_pi | Archimedes]]' polygon bisections a dozen more times, computing the perimeter of a polygon with 393,216 sides <a class="yt-timestamp" data-t="00:03:50">[00:04:03]</a>.
*   **Ludolph van Ceulen** (turn of 17th century): Spent 25 years on the effort, computing the perimeter of a polygon with 2^62 sides (over 4 quintillion sides), achieving 35 correct decimal places of Pi <a class="yt-timestamp" data-t="00:04:03">[00:04:33]</a>. His digits were inscribed on his tombstone <a class="yt-timestamp" data-t="00:04:38">[00:04:42]</a>.
*   **Christoph Grienberger**: Surpassed van Ceulen's record 20 years later, achieving 38 correct decimal places <a class="yt-timestamp" data-t="00:04:42">[00:04:49]</a>.

This method was mathematically sound but extraordinarily tedious, representing a "flexing of mathematical muscles" rather than practical necessity <a class="yt-timestamp" data-t="00:03:22">[00:03:32]</a>.

## Isaac Newton's Revolutionary Approach

The year was 1666, and Isaac Newton, at just 23 years old, was quarantining at home due to the bubonic plague <a class="yt-timestamp" data-t="00:05:04">[00:05:10]</a>. During this time, he revolutionized the calculation of Pi.

### The Binomial Theorem
Newton built upon the known concept of Pascal's Triangle, which provides the coefficients for the expansion of expressions like (1 + X)^N <a class="yt-timestamp" data-t="00:05:13">[00:05:52]</a>. Pascal's Triangle was known across many ancient cultures <a class="yt-timestamp" data-t="00:06:03">[00:06:07]</a>. The general formula for these numbers, known as the Binomial Theorem, was also established <a class="yt-timestamp" data-t="00:06:57">[00:07:26]</a>. This theorem states that for (1 + X)^N, the expansion is 1 + NX + [N(N-1)/2!]X² + [N(N-1)(N-2)/3!]X³ + ... <a class="yt-timestamp" data-t="00:07:09">[00:07:25]</a>. For positive integer values of N, the series is finite because terms eventually become zero <a class="yt-timestamp" data-t="00:09:06">[00:09:24]</a>.

### Newton's Generalization
Newton's genius lay in daring to apply the Binomial Theorem where it was traditionally not used: when N is not a positive integer <a class="yt-timestamp" data-t="00:07:50">[00:08:02]</a>.
*   **Negative Exponents:** He tried N = -1, for (1 + X)^(-1) = 1/(1 + X) <a class="yt-timestamp" data-t="00:08:19">[00:08:24]</a>. Blindly plugging N = -1 into the formula resulted in an infinite series: 1 - X + X² - X³ + X⁴ - X⁵... <a class="yt-timestamp" data-t="00:08:24">[00:08:50]</a>. Newton justified this by showing that multiplying this infinite series by (1 + X) resulted in 1, proving its validity <a class="yt-timestamp" data-t="00:09:56">[00:10:08]</a>. This implies an extension of Pascal's triangle to negative integer rows <a class="yt-timestamp" data-t="00:10:21">[00:11:01]</a>.
*   **Fractional Exponents:** Next, Newton experimented with fractional powers, such as N = 1/2, for (1 + X)^(1/2), which is equivalent to the square root of (1 + X) <a class="yt-timestamp" data-t="00:11:31">[00:11:42]</a>. Applying the binomial theorem with N = 1/2 generated another infinite series <a class="yt-timestamp" data-t="00:11:45">[00:11:50]</a>. This suggested a "continuum" of Pascal's triangles existing between integer rows <a class="yt-timestamp" data-t="00:11:59">[00:12:06]</a>. This method could be used to efficiently calculate square roots, for example, the square root of 3 <a class="yt-timestamp" data-t="00:12:30">[00:12:54]</a>.

### Calculating Pi with Calculus
Newton was particularly interested in N = 1/2 because the equation for a unit circle is X² + Y² = 1 <a class="yt-timestamp" data-t="00:12:56">[00:13:05]</a>. Solving for Y, the top half of the circle is Y = sqrt(1 - X²) = (1 - X²)^(1/2) <a class="yt-timestamp" data-t="00:13:05">[00:13:12]</a>. By replacing X with -X² in his binomial expansion for (1+X)^(1/2), he obtained an infinite series for the circle's equation, where each term was a rational number times X raised to some power <a class="yt-timestamp" data-t="00:13:12">[00:13:29]</a>.

At this point, Newton had just invented calculus, which he called the "theory of Fluxions" <a class="yt-timestamp" data-t="00:13:42">[00:13:48]</a>. He realized that integrating under the curve of the unit circle from X=0 to X=1 would yield the area of a quarter circle <a class="yt-timestamp" data-t="00:13:48">[00:13:54]</a>. Since the area of a unit circle is Pi (πr², with r=1), a quarter circle's area is Pi/4 <a class="yt-timestamp" data-t="00:13:57">[00:14:04]</a>.

He then integrated each term of the infinite series expansion for the circle's equation. The integral of X to some power is simply increasing the power by one and dividing by the new power <a class="yt-timestamp" data-t="00:14:07">[00:14:16]</a>. This produced an infinite series of terms involving simple arithmetic with fractions <a class="yt-timestamp" data-t="00:14:18">[00:14:24]</a>. By substituting X=1 into this series, he could calculate Pi to an arbitrarily high precision <a class="yt-timestamp" data-t="00:14:24">[00:14:31]</a>.

### Newton's Optimization for Convergence
Newton added a final tweak to optimize the calculation <a class="yt-timestamp" data-t="00:14:31">[00:14:35]</a>. Instead of integrating from zero to one, he chose to integrate from zero to a half <a class="yt-timestamp" data-t="00:14:50">[00:14:57]</a>. The goal with infinite series is to make the terms decrease in size as fast as possible to achieve accuracy with fewer calculations <a class="yt-timestamp" data-t="00:14:57">[00:15:06]</a>. By substituting X = 1/2, each term in the series would shrink by an additional factor of X² (which is 1/4), leading to much faster convergence <a class="yt-timestamp" data-t="00:15:08">[00:15:20]</a>.

Integrating from zero to a half yields a specific segment of the circle <a class="yt-timestamp" data-t="00:15:24">[00:15:30]</a>. This area can be broken down into a 30-degree sector of the circle (with an area of Pi/12) plus a right triangle <a class="yt-timestamp" data-t="00:15:30">[00:15:46]</a>. By equating this geometric sum to the result of the integrated series and rearranging, Newton derived a new formula for Pi <a class="yt-timestamp" data-t="00:15:46">[00:15:54]</a>.

## Impact
Using only the first five terms of this optimized series, Newton obtained Pi = 3.14161, which was off by only two parts in 100,000 <a class="yt-timestamp" data-t="00:15:54">[00:16:05]</a>. To match the precision achieved by Ludolph van Ceulen with his quadrillion-sided polygon, Newton would have only needed to compute 50 terms of his series <a class="yt-timestamp" data-t="00:16:07">[00:16:16]</a>. What previously took years of painstaking effort could now be done in days <a class="yt-timestamp" data-t="00:16:16">[00:16:21]</a>.

Newton's method rendered the traditional polygon bisection approach obsolete <a class="yt-timestamp" data-t="00:16:21">[00:16:26]</a>. This shift highlights how a little bit of insight and mathematical innovation can lead to vastly superior technology and efficiency, pushing beyond obvious methods and breaking conventional boundaries <a class="yt-timestamp" data-t="00:17:03">[00:17:19]</a>.