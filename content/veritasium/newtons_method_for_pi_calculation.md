---
title: Newtons method for Pi calculation
videoId: gMlf1ELvRzc
---

From: [[veritasium]] <br/> 

For approximately 2000 years, the most successful method for calculating Pi was incredibly slow and tedious <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. This changed with the arrival of [[development_of_calculus_by_isaac_newton | Isaac Newton]], who revolutionized the process <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Understanding Pi

Pi (π) represents the ratio of a circle's circumference to its diameter <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. It is roughly 3.14 times the diameter <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. Pi is also intrinsically linked to a circle's area, given by the formula πr² <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

### Why Area is Pi R Squared

To understand why the area of a circle is πr², imagine cutting a pizza into many thin slices and rearranging them into a rectangle <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
The length of this rectangle would be half the pizza's circumference (πr) <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>, as half the crust forms one side and the other half forms the other <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. The width of the rectangle would be the length of a pizza slice, which is the radius (r) of the original circle <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. Therefore, the area of the rectangle (and thus the circle) is length (πr) times width (r), resulting in πr² <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. For a unit circle (radius = 1), its area is simply Pi <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

## Traditional Methods of Calculating Pi

For millennia, the approach to calculating Pi was to approximate a circle's circumference or area using polygons <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

### Basic Polygon Approximation
It's easy to demonstrate that Pi must be between three and four <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
*   **Lower Bound**: Inscribe a regular hexagon with side lengths of one unit inside a circle <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. If the hexagon is made of six equilateral triangles, the circle's diameter is two <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. The hexagon's perimeter is six <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. Since the circle's circumference must be larger, Pi (circumference/diameter) must be greater than 6/2, meaning Pi > 3 <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **Upper Bound**: Draw a square around the circle <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. The square's perimeter is eight <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. As this is larger than the circle's circumference, Pi must be less than 8/2, meaning Pi < 4 <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

### [[archimedes_method_of_calculating_pi | Archimedes' Method]] and Historical Progression
In 250 BC, [[archimedes_method_of_calculating_pi | Archimedes]] significantly improved this method <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. He started with a hexagon and then repeatedly bisected it, calculating the perimeters of inscribed and circumscribed polygons to get increasingly tighter bounds for Pi <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. This involved complex calculations requiring the extraction of square roots and converting them to fractions <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. By the time he reached a 96-sided polygon, [[archimedes_method_of_calculating_pi | Archimedes]] had determined Pi to be between 3.1408 and 3.1429 <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

For the next 2000 years, mathematicians from Chinese, Indian, Persian, and Arab cultures continued this polygon-bisection approach, extending the precision <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   In the late 16th century, Frenchman Francois Viete computed the perimeter of a polygon with 393,216 sides <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
*   At the turn of the 17th century, the Dutch Ludolph van Ceulen spent 25 years <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a> calculating the perimeter of a polygon with 2^62 sides (over 4 quintillion sides), achieving 35 correct decimal places of Pi <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. These digits were inscribed on his tombstone <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
*   Twenty years later, Christoph Grienberger surpassed this, reaching 38 correct decimal places <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
This method was incredibly laborious, highlighting a desire to demonstrate mathematical prowess rather than simply achieving practical precision <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

## Newton's Breakthrough: The Binomial Theorem

The "ridiculous" polygon method became obsolete with the arrival of [[development_of_calculus_by_isaac_newton | Sir Isaac Newton]] <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. In 1666, while quarantining at home due to the bubonic plague, 23-year-old Newton was experimenting with algebraic expressions <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

### [[binomial_theorem_and_pascals_triangle | Pascal's Triangle]] and the [[binomial_theorem_and_pascals_triangle | Binomial Theorem]]
Newton recognized a pattern in the expansion of (1+x) raised to a positive integer power, such as (1+x)² = 1 + 2x + x² <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a> or (1+x)³ = 1 + 3x + 3x² + x³ <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. The coefficients of these expansions correspond directly to the numbers in [[binomial_theorem_and_pascals_triangle | Pascal's triangle]] <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.

[[binomial_theorem_and_pascals_triangle | Pascal's triangle]] is easy to construct by adding two neighbors in a row to get the value in the row below <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. This pattern was known across various ancient cultures <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. Over time, a general formula, known as the [[binomial_theorem_and_pascals_triangle | binomial theorem]], was developed for the coefficients in any row:
For (1+x)^n, the expansion is:
1 + nx + (n(n-1)/2!)x² + (n(n-1)(n-2)/3!)x³ + ... <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>

### Newton's Generalization
The standard [[binomial_theorem_and_pascals_triangle | binomial theorem]] was understood to apply only when 'n' is a positive integer <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. However, Newton boldly decided to "break the formula" by applying it to non-integer values of 'n' <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. He reasoned that mathematics often involves finding patterns and extending them to see where they might still hold true <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.

1.  **Negative Powers**: Newton first tried n = -1, expanding (1+x)^-1 (or 1/(1+x)) <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. Blindly plugging n=-1 into the formula yielded an infinite series where terms alternate between plus and minus signs: 1 - x + x² - x³ + x⁴ - x⁵ + ... <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. This infinite series is justified because if you multiply it by (1+x), all terms cancel out except for the leading one, resulting in 1 <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. This means the infinite series indeed equals 1/(1+x) <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. For positive integers, the series is finite because at some point, the (n-n) term becomes zero, making all subsequent coefficients zero <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. For non-integers, this never happens, leading to an infinite series <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.
2.  **Fractional Powers**: Newton then extended the [[binomial_theorem_and_pascals_triangle | binomial theorem]] to fractional powers, such as n = 1/2, meaning (1+x)^(1/2) or √√(1+x) <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>. This also results in an infinite series <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>. This generalized [[binomial_theorem_and_pascals_triangle | binomial theorem]] implied a continuum of [[binomial_theorem_and_pascals_triangle | Pascal's triangles]] for any real number 'n', not just integers <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. This breakthrough allowed Newton to calculate values like √3 efficiently by writing it as 2 * √(1 - 1/4) and plugging x = -1/4 into the series for √(1+x) <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.

## Connecting to Pi Calculation

Newton applied his generalized [[binomial_theorem_and_pascals_triangle | binomial theorem]] to the equation of a unit circle <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.
The equation for a unit circle is x² + y² = 1 <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>. Solving for y (the top half of the circle) gives y = √(1 - x²) <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>, which can be written as (1 - x²)^(1/2). This expression is similar to (1+x)^(1/2), just with 'x' replaced by '-x²' <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>. Expanding this using the generalized binomial theorem, Newton obtained an infinite series for the circle's equation, where each term was an irrational number multiplied by x raised to some power <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>.

### Integrating with [[development_of_calculus_by_isaac_newton | Calculus]]
Having recently invented [[development_of_calculus_by_iac_newton | calculus]] (which he called the theory of Fluxions) <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>, Newton realized that integrating the series for y = (1 - x²)^(1/2) from x=0 to x=1 would give the area under a quarter of the unit circle <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>. Since the area of a unit circle is Pi, a quarter of its area is Pi/4 <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>.

Newton knew how to integrate x to a power: increase the power by one and divide by the new power <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>. This allowed him to integrate the infinite series term by term, resulting in another infinite series that involved only simple arithmetic with fractions <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>. By plugging in x=1, this series could calculate Pi to an arbitrarily high precision <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.

### Optimization: Integrating to Half
Newton added a final optimization <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>. To make the infinite series converge faster, he chose to integrate from x=0 to x=0.5 instead of x=1 <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>. When substituting x=0.5, each term in the series would shrink by an additional factor of x² (which is 0.25) <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>.

Integrating to 0.5 computes a specific area under the circle's curve <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>. This area can be geometrically broken down into a 30-degree sector of the circle (area = π/12) and a right triangle <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>. By equating the integral to this geometric sum and rearranging, Newton derived a formula for Pi <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>. Evaluating just the first five terms of this series yielded Pi = 3.14161, which was off by only two parts in 100,000 <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>. To match van Ceulen's 35 decimal places, Newton's series would only require computing 50 terms, a task that would take days instead of years <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>.

## Impact
Newton's method rendered the centuries-old polygon bisection approach obsolete <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>. It demonstrated that insight and the courage to push mathematical boundaries could lead to vastly superior methods, fundamentally changing how constants like Pi could be calculated <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>.