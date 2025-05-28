---
title: History of Pi calculation methods
videoId: gMlf1ELvRzc
---

From: [[veritasium]] <br/> 

For approximately 2000 years, the most successful method for calculating Pi was painstakingly slow and tedious <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. However, [[Isaac Newtons approach to estimating Pi | Isaac Newton]] later revolutionized this process <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Understanding Pi

Pi (π) is a fundamental mathematical constant.
*   The circumference of a circle is roughly 3.14 times its diameter <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.
*   Pi is also related to a circle's area, given by the formula "Area = Pi R squared" <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
    *   This can be visualized by cutting a pizza into very thin slices and arranging them into a rectangle <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. The length of this rectangle is half the circumference (πR), and its width is the radius (R) of the original circle, thus the area is (πR) * R = πR² <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   The area of a unit circle (radius R=1) is simply Pi <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

## Ancient Methods: Inscribing and Circumscribing Polygons

The earliest method for calculating Pi involved geometric approximation <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. It was known for thousands of years that Pi must be between 3 and 4 <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
*   By drawing a regular hexagon inside a circle with a diameter of two, its perimeter is six, showing Pi (circumference/diameter) must be greater than three <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   By drawing a square around the circle, its perimeter is eight, showing Pi must be less than four <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

### [[archimedes_method_for_calculating_pi | Archimedes' Method]]

Around 250 BC, [[archimedes_method_for_calculating_pi | Archimedes]] significantly improved this method <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
*   He started with a hexagon and progressively bisected it, creating regular polygons with more sides (12-gon, 24-gon, 48-gon) <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   He calculated the perimeters of both inscribed and circumscribed polygons to find increasingly tighter bounds for Pi <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
*   These calculations were complex, requiring the extraction of square roots and converting them into fractions <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   By the time he reached a 96-gon, he determined Pi to be between 3.1408 and 3.1429 <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. This level of precision, over 2000 years ago, was remarkable <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
*   The pursuit of such high precision was driven more by demonstrating mathematical prowess than practical necessity <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

### Continuation of the Polygon Method

For the next two millennia, mathematicians continued to use and refine [[archimedes_method_for_calculating_pi | Archimedes' method]] of bisecting polygons <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   Contributions came from Chinese, Indian, Persian, and Arab mathematicians, each pushing the bounds of Pi further <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
*   In the late 16th century, Frenchman Francois Viete computed the perimeter of a polygon with 393,216 sides <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
*   At the turn of the 17th century, the Dutch mathematician Ludolph van Ceulen spent 25 years on this effort <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. He calculated the perimeter of a polygon with 2^62 sides (over four quintillion sides) <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>, achieving 35 correct decimal places of Pi <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. These digits were famously inscribed on his tombstone <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
*   Twenty years later, Christoph Grienberger surpassed this record with 38 correct decimal places <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

This era of bisecting n-gons effectively ended shortly thereafter <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

## [[Isaac Newtons approach to estimating Pi | Isaac Newton]]'s Breakthrough: The Binomial Theorem

In 1666, at just 23 years old, [[Isaac Newtons approach to estimating Pi | Isaac Newton]], while quarantining due to the bubonic plague, developed a revolutionary method for calculating Pi <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

### Pascal's Triangle and the Binomial Theorem
*   Newton was exploring expressions like (1+X)² and (1+X)³, noticing a pattern in the coefficients that correspond to Pascal's triangle <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
*   Pascal's triangle, known across many ancient cultures, provides a quick way to compute coefficients for (1+X)^N by adding the two numbers above <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. Mathematics' beauty lies in its transcendence of culture and time <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.
*   Over time, a general formula for these coefficients was developed, known as the binomial theorem <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. This formula allows calculating coefficients for any row without computing previous ones <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. The binomial theorem states that for any expression (1+X)^N, it equals:
    1 + NX + N(N-1)/2! X² + N(N-1)(N-2)/3! X³ + ... <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>

### Newton's Extension: Breaking the Formula
*   While the standard binomial theorem applied only when N is a positive integer (resulting in a finite sum because terms eventually become zero) <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>, Newton dared to apply it beyond these bounds <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
*   He experimented with negative powers, like (1+X)^(-1) (which is 1/(1+X)) <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. By blindly plugging N=-1 into the formula, he derived an infinite series: 1 - X + X² - X³ + X⁴ - X⁵ + ... <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.
*   He justified this by showing that multiplying the infinite series by (1+X) resulted in 1, proving its validity <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
*   This implied an extension of Pascal's triangle to negative integer rows <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

### Fractional Powers and Calculus
*   Newton further extended the binomial theorem to fractional powers, such as (1+X)^(1/2) (square root of 1+X) <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.
*   This allowed him to quickly and efficiently calculate values like the square root of three by transforming it into an expression that could be expanded using the series <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.
*   Newton realized that the equation for a unit circle, X² + Y² = 1, could be expressed as Y = (1 - X²)^(1/2) for the top half of the circle <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>. He could then substitute -X² for X in his binomial series expansion <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.
*   By integrating this series under the curve from X=0 to X=1, he calculated the area of a quarter unit circle, which is Pi/4 <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>. This was possible due to his invention of calculus, or "theory of Fluxions" <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.
*   Integrating each term of the series yielded an infinite series of terms involving simple arithmetic with fractions <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>, allowing Pi to be calculated to arbitrarily high precision <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.

### Optimizing the Calculation
*   Newton added a final tweak: instead of integrating from 0 to 1, he integrated from 0 to 0.5 <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>. This made the terms in the infinite series decrease in size much faster, requiring fewer terms for a good answer <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>.
*   Integrating from 0 to 0.5 computes the area of a segment of the circle, which can be broken down into a 30-degree sector (Pi/12) and a right triangle <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>.
*   Using only the first five terms of this optimized series, Newton could calculate Pi to 3.14161 <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>.
*   To match the precision of van Ceulen's 35 decimal places (which took 25 years), Newton's method would only require computing 50 terms, taking mere days instead of years <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>.

This technological leap rendered the polygon bisection method obsolete <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>, demonstrating how pushing mathematical patterns beyond expected bounds can lead to profound insights and vastly improved methods <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>.