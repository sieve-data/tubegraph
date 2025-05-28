---
title: Mathematical series expansion
videoId: gMlf1ELvRzc
---

From: [[veritasium]] <br/> 

For 2000 years, the calculation of [[history_of_pi_calculation_methods | Pi]] was a painstakingly slow and tedious process <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This changed with Isaac Newton's introduction of mathematical series expansion, which significantly sped up the process <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Understanding Pi

[[history_of_pi_calculation_methods | Pi]] is the ratio of a circle's circumference to its diameter, approximately 3.14 <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. It is also related to a circle's area by the formula Pi R squared <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. The area of a unit circle (radius R=1) is simply Pi <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

### Traditional Pi Calculation Methods

The most obvious method for calculating [[history_of_pi_calculation_methods | Pi]] involved inscribing and circumscribing polygons around a circle <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
It was known for thousands of years that [[history_of_pi_calculation_methods | Pi]] must be between three and four <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>:
*   An inscribed hexagon with sides of length one (diameter two) has a perimeter of six, meaning the circle's circumference is greater than six, so [[history_of_pi_calculation_methods | Pi]] (circumference/diameter) is greater than three <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   A circumscribed square around a circle with diameter two has a perimeter of eight, meaning the circle's circumference is less than eight, so [[history_of_pi_calculation_methods | Pi]] is less than four <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

In 250 BC, Archimedes improved this method <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>:
*   He started with a hexagon and bisected it to create polygons with more sides (12-gon, 24-gon, 48-gon, up to a 96-gon) <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   By calculating the perimeters of both inscribed and circumscribed polygons, he established upper and lower bounds for [[history_of_pi_calculation_methods | Pi]] <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
*   His calculations involved extracting square roots and converting them into fractions <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   Archimedes ultimately found [[history_of_pi_calculation_methods | Pi]] to be between 3.1408 and 3.1429 <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

For the next two millennia, mathematicians from Chinese, Indian, Persian, and Arab cultures continued this method, bisecting polygons to dizzying heights <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>:
*   **Francois Viete (late 16th century)**: Doubled Archimedes' efforts a dozen more times, computing the perimeter of a polygon with 393,216 sides <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
*   **Ludolph van Ceulen (early 17th century)**: Spent 25 years calculating the perimeter of a polygon with 2^62 sides (over 4 quintillion sides), achieving 35 correct decimal places of [[history_of_pi_calculation_methods | Pi]] <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. These digits were inscribed on his tombstone <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
*   **Christoph Grienberger**: Surpassed Van Ceulen's record 20 years later, reaching 38 correct decimal places <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

This polygon bisection method was extremely laborious, requiring immense mathematical effort for minimal gains in precision <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

## Newton's Revolution in Series Expansion

In 1666, at just 23 years old, Isaac Newton revolutionized the calculation of [[history_of_pi_calculation_methods | Pi]] while quarantining during a bubonic plague outbreak <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

### The [[binomial_theorem_and_its_applications | Binomial Theorem]]

Newton explored simple algebraic expansions like (1+X)^2 or (1+X)^3 <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. He recognized that the coefficients of these expansions correspond to numbers in Pascal's Triangle <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>. Pascal's Triangle was known across many ancient cultures, including Greeks, Indians, Chinese, and Persians <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. Its construction is simple: each number is the sum of the two numbers directly above it <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. This pattern in [[mathematical_principles_in_origami | mathematics]] transcends cultures and time <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

Over time, a general formula for the numbers in Pascal's Triangle was developed, allowing calculation of coefficients in any row without computing previous rows. This formula is the [[binomial_theorem_and_its_applications | Binomial Theorem]] <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>:
(1+X)^N = 1 + NX + N(N-1)/2! X^2 + N(N-1)(N-2)/3! X^3 + ... <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
This theorem was well-known in Newton's time and rigorously provable <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.

### Extending the [[binomial_theorem_and_its_applications | Binomial Theorem]]

The standard [[binomial_theorem_and_its_applications | Binomial Theorem]] was understood to apply only when N is a positive integer <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. Newton, however, decided to "break the formula" by applying it to values of N that were not positive integers <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>. He believed that [[mathematical_principles_in_origami | mathematics]] is about finding patterns and extending them to see where they might still hold <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.

#### Negative Integer Powers
Newton tried N = -1, which corresponds to (1+X)^-1 = 1/(1+X) <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. Blindly plugging N=-1 into the [[binomial_theorem_and_its_applications | Binomial Theorem]] yields an infinite series: 1 - X + X^2 - X^3 + X^4 - ... <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.
This becomes an infinite series because for non-positive integers, the N-N term in the coefficient never becomes zero, unlike with positive integers where the series terminates <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. Newton justified this by multiplying the infinite series by (1+X) and observed that all terms cancelled except the leading one, confirming the series equals 1/(1+X) <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

This implies an extension of Pascal's Triangle "above" the zero-th row, where values for negative integers of N would consist of alternating plus and minus ones that sum to zero in the row beneath them <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>. Interestingly, ignoring the negative signs, these numbers are arranged in the same pattern as the main triangle, effectively a rotation <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

#### Fractional Powers
Newton then applied the [[binomial_theorem_and_its_applications | Binomial Theorem]] to fractional powers, such as N = 1/2, corresponding to (1+X)^0.5, or the square root of (1+X) <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>. This also results in an infinite series <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>. This extension suggests a "continuum" of Pascal's Triangles, with fractions existing in their own planes <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>.

Newton could use this to efficiently calculate values like the square root of three <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>. By writing 3 as (4-1) and factoring out 4, it becomes 2 * (1 - 1/4)^0.5 <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>. Substituting -1/4 for X in the binomial series for N=1/2 provides a rapidly converging series expansion for the square root of three <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

## Calculating Pi with Series Expansion and Calculus

Newton applied this extended [[binomial_theorem_and_its_applications | Binomial Theorem]] to the equation of a unit circle <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>. The top half of a unit circle is given by Y = (1 - X^2)^0.5 <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>. This is the same form as (1+X)^0.5, by simply replacing X with -X^2 in the series expansion <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>. This yields an infinite series for Y, where each term is a rational number multiplied by X raised to some power <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>.

Newton then used his newly invented calculus (which he called the "theory of Fluxions") <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>. He realized that integrating the series for Y from X=0 to X=1 would give the area of a quarter unit circle <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>. Since the area of a unit circle is Pi, the area of a quarter circle is Pi/4 <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.
Integrating each term of the series (increasing the power of X by one and dividing by the new power) yields an infinite series of terms involving simple arithmetic with fractions, which can be evaluated at X=1 to calculate Pi to arbitrarily high precision <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.

### Optimization for Faster Convergence

Newton further optimized his method by integrating not from 0 to 1, but from 0 to 0.5 <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>. The goal with infinite series is to make the terms decrease in size as fast as possible to achieve high accuracy with fewer calculations <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>. By substituting X=0.5, each term in the series shrinks by an additional factor of X squared (which is a quarter) <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>.

Integrating from 0 to 0.5 calculates a specific part of the circle's area, which can be broken down into a 30-degree sector (area Pi/12) and a right triangle <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>. This allows for a more rapidly converging series for Pi <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>. Evaluating only the first five terms of this optimized series yields Pi = 3.14161, which is off by only two parts in 100,000 <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>. To match Van Ceulen's 35 decimal places (achieved with 4 quintillion sides), Newton's method would only require computing about 50 terms <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>. What previously took years could now be done in days <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.

This new technology rendered the polygon bisection method obsolete, demonstrating how insight and extending mathematical patterns beyond their expected bounds can lead to vastly more efficient solutions <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>.