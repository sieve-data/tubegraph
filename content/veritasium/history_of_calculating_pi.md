---
title: History of calculating Pi
videoId: gMlf1ELvRzc
---

From: [[veritasium]] <br/> 

Pi (π) is a fundamental mathematical constant representing the ratio of a circle's circumference to its diameter <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. For over 2000 years, calculating Pi was a painstakingly slow and tedious process <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. This changed with the contributions of [[development_of_calculus_by_isaac_newton | Isaac Newton]], who introduced a significantly faster method <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Understanding Pi

Pi is approximately 3.14 times a circle's diameter <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. It is also related to a circle's area, given by the formula Pi R squared <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. This formula can be visualized by cutting a circle into thin slices and rearranging them into a rectangle <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. The length of this rectangle is half the circumference (Pi R), and its width is the radius (R), resulting in an area of Pi R squared <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. For a unit circle (radius of 1), the area is simply Pi <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

## Early Methods: Polygon Approximation

The most obvious initial approach to calculating Pi was to bound it between simple geometric shapes <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. It's easy to demonstrate that Pi must be between three and four <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>:
*   An inscribed hexagon with side length one (and thus diameter two) has a perimeter of six, meaning the circle's circumference must be greater than six, so Pi is greater than three <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   A circumscribed square has a perimeter of eight, which is larger than the circle's circumference, meaning Pi is less than four <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

This basic understanding was known for thousands of years <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

### [[archimedes_method_of_calculating_pi | Archimedes' Method]]

In 250 BC, [[archimedes_method_of_calculating_pi | Archimedes]] significantly improved upon this method <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. He started with an inscribed hexagon and successively bisected its sides to create polygons with more sides, like a dodecagon (12-sided shape) <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. He calculated the perimeter of these polygons to find a lower bound for Pi <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. He did the same for circumscribed polygons to find an upper bound <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

These calculations were complex, involving square roots and converting results to fractions <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. By the time he reached a 96-gon, [[archimedes_method_of_calculating_pi | Archimedes]] had found Pi to be between 3.1408 and 3.1429 <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. This level of precision was remarkable for its time and went beyond any practical purpose, serving as a demonstration of mathematical power <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

### Continued Refinements of the Polygon Method

For the next 2000 years, mathematicians continued to use and refine [[archimedes_method_of_calculating_pi | Archimedes']] method of bisecting polygons <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. Contributions came from:
*   Chinese, Indian, Persian, and Arab mathematicians <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
*   In the late 16th century, Frenchman Francois Viete doubled the polygon sides many more times than [[archimedes_method_of_calculating_pi | Archimedes]], computing the perimeter of a polygon with 393,216 sides <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
*   At the turn of the 17th century, the Dutch Ludolph van Ceulen spent 25 years computing Pi to high accuracy using a polygon with 2^62 sides (over four quintillion sides) <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. His reward was just 35 correct decimal places of Pi, which were inscribed on his tombstone <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   Twenty years later, Christoph Grienberger surpassed this record, achieving 38 correct decimal places <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

This method was ultimately superseded by the arrival of [[development_of_calculus_by_Isaac_Newton | Isaac Newton]] <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

## [[newtons_method_for_pi_calculation | Newton's Method]] for Pi Calculation

In 1666, at just 23 years old, [[development_of_calculus_by_Isaac_Newton | Isaac Newton]] developed a revolutionary method for calculating Pi while quarantining at home during an outbreak of bubonic plague <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

### Pascal's Triangle and the Binomial Theorem

Newton's work built upon existing mathematical knowledge, including Pascal's Triangle. This triangular array of numbers, where each number is the sum of the two directly above it, was known by various ancient cultures including Greeks, Indians, Chinese, and Persians <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. It provides the coefficients for the expansion of expressions like (1 + X)^n <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.

Over time, a general formula for the numbers in Pascal's Triangle, known as the Binomial Theorem, was developed <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. For an expression (1 + X)^n, the theorem states:
1 + nX + [n(n-1)/2!]X^2 + [n(n-1)(n-2)/3!]X^3 + ... <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

This theorem was well-known in Newton's day <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.

### Newton's Innovation: Breaking the Binomial Theorem

The standard Binomial Theorem was traditionally applied only when 'n' was a positive integer <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. Newton's groundbreaking insight was to apply the theorem beyond this boundary <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

*   **Negative Powers**: He experimented with (1 + X)^-1 (or 1/(1+X)) by blindly plugging n = -1 into the formula <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. This resulted in an infinite series with alternating signs: 1 - X + X^2 - X^3 + X^4 - ... <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. Newton justified this by showing that multiplying the series by (1 + X) resulted in 1, proving its validity <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. This implies an extension of Pascal's Triangle for negative integers, where the alternating signs allow terms to sum to zero in rows below, fitting the pattern <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
*   **Fractional Powers**: Newton then applied the theorem to fractional powers, specifically (1 + X)^(1/2), which is the square root of (1 + X) <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>. Plugging n = 1/2 into the binomial theorem also yielded an infinite series <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>. This concept suggests a "continuum" of Pascal's triangles for all possible powers <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. He showed this could be used to quickly and efficiently calculate values like the square root of three <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.

### Calculating Pi with Newton's Method

Newton's particular interest in n = 1/2 stemmed from its connection to the equation of a unit circle: X^2 + Y^2 = 1 <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>. Solving for Y, the top half of the circle is Y = (1 - X^2)^(1/2) <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>. This is essentially the same expression as (1 + X)^(1/2), just with X replaced by -X^2 <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.

Newton, having recently invented [[development_of_calculus_by_Isaac_Newton | calculus]] (which he called the "theory of Fluxions"), realized he could integrate the series expansion of (1 - X^2)^(1/2) <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.
*   Integrating Y = (1 - X^2)^(1/2) from X=0 to X=1 yields the area of a quarter unit circle <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.
*   Since the area of a unit circle is Pi (Pi R^2 where R=1), the area of a quarter circle is Pi/4 <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>.
*   By integrating the infinite series term by term (increasing each power of X by one and dividing by the new power), Newton obtained an infinite series of terms involving simple arithmetic with fractions, which could be evaluated at X=1 to calculate Pi to arbitrarily high precision <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.

### Newton's Final Tweak for Efficiency

Newton further refined his method by integrating from X=0 to X=0.5 instead of X=0 to X=1 <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>. This was done to make the terms in the infinite series decrease in size as fast as possible, requiring fewer terms for a good approximation <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>. When X=0.5, each term shrinks by an additional factor of X^2 (which is 1/4 in this case) <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.

Integrating from 0 to 0.5 calculates the area of a specific part of the circle, which can be broken down into a 30-degree sector (area Pi/12) and a right triangle <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>. Rearranging the resulting equation for Pi leads to a very rapidly converging series <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>.
*   Using only the first five terms of this series, Newton could get Pi = 3.14161, which was off by only two parts in 100,000 <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>.
*   To match the computational power of Van Ceulen's four quintillion-sided polygon (which took 25 years for 35 digits), Newton's series would only require computing 50 terms, taking mere days instead of years <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>.

Newton's method marked a profound shift in the [[history_of_physics_and_mathematics_discoveries | history of mathematics]], rendering the laborious polygon bisection method obsolete <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>. It demonstrated that insight and pushing the boundaries of known mathematical patterns can lead to vastly superior approaches <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>.