---
title: Binomial theorem and Pascals triangle
videoId: gMlf1ELvRzc
---

From: [[veritasium]] <br/> 

Pascal's triangle is a mathematical structure that has been discovered by many different cultures, including ancient Greeks, Indians, Chinese, and Persians <a class="yt-timestamp" data-t="06:03:00">[06:03:00]</a>. It is easy to construct: each number in a row is the sum of the two numbers directly above it <a class="yt-timestamp" data-t="06:12:00">[06:12:00]</a>.

The numbers in Pascal's triangle represent the coefficients when expanding simple algebraic expressions like (1 + X) raised to a power <a class="yt-timestamp" data-t="05:45:00">[05:45:00]</a>. For example:
*   (1 + X)² = 1 + 2X + X² <a class="yt-timestamp" data-t="05:19:00">[05:19:00]</a>
*   (1 + X)³ = 1 + 3X + 3X² + X³ <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>
The coefficients (1, 2, 1) and (1, 3, 3, 1) correspond to rows in Pascal's triangle <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a>. The power that (1 + X) is raised to corresponds to the row of the triangle <a class="yt-timestamp" data-t="05:55:00">[05:55:00]</a>.

## The Binomial Theorem

Over time, a general formula for the numbers in Pascal's triangle was developed, allowing calculation of numbers in any row without computing all preceding rows <a class="yt-timestamp" data-t="06:57:00">[06:57:00]</a>. This is known as the binomial theorem <a class="yt-timestamp" data-t="07:26:00">[07:26:00]</a>, which states that for any expression (1 + X)ⁿ:

1 + nX + [n(n-1)/2!]X² + [n(n-1)(n-2)/3!]X³ + ... <a class="yt-timestamp" data-t="07:12:00">[07:12:00]</a>

This formula can be rigorously proven <a class="yt-timestamp" data-t="07:34:00">[07:34:00]</a>. For positive integer values of `n`, the series is finite because terms eventually become zero (e.g., n-n = 0) <a class="yt-timestamp" data-t="09:06:00">[09:06:00]</a>.

## Newton's Extension

In 1666, at just 23 years old and quarantining due to the bubonic plague <a class="yt-timestamp" data-t="05:04:00">[05:04:00]</a>, [[newtons_method_for_pi_calculation | Isaac Newton]] revolutionized the use of the binomial theorem by applying it in situations where it was not traditionally deemed applicable <a class="yt-timestamp" data-t="07:50:00">[07:50:00]</a>. He extended the theorem to negative values of `n` and even fractional powers <a class="yt-timestamp" data-t="11:31:00">[11:31:00]</a>.

### Negative Integer Powers
When `n` is a negative integer, [[newtons_method_for_pi_calculation | Newton]] found that the binomial theorem results in an infinite series <a class="yt-timestamp" data-t="08:51:00">[08:51:00]</a>. For example, for (1 + X)⁻¹ (which is 1/(1+X)), the formula yields an alternating series of 1 - X + X² - X³ + X⁴ - X⁵... <a class="yt-timestamp" data-t="08:30:00">[08:30:00]</a>. [[newtons_method_for_pi_calculation | Newton]] justified this by showing that multiplying this infinite series by (1 + X) results in 1, thus confirming its validity <a class="yt-timestamp" data-t="09:56:00">[09:56:00]</a>.

This extension implies that Pascal's triangle can be conceptually extended above its traditional 'zeroeth' row, with alternating plus and minus signs, where pairs of numbers still sum to make the number below them <a class="yt-timestamp" data-t="10:29:00">[10:29:00]</a>. When negative signs are ignored, these numbers mirror the pattern of the main triangle, as if rotated on its side <a class="yt-timestamp" data-t="11:11:00">[11:11:00]</a>.

### Fractional Powers
[[newtons_method_for_pi_calculation | Newton]] further extended the theorem to fractional powers, such as (1 + X)½, which represents the square root of (1 + X) <a class="yt-timestamp" data-t="11:31:00">[11:31:00]</a>. Plugging `n = ½` into the binomial theorem also generates an infinite series <a class="yt-timestamp" data-t="11:45:00">[11:45:00]</a>. This concept suggests a "continuum" of Pascal's triangles existing between integer rows <a class="yt-timestamp" data-t="11:59:00">[11:59:00]</a>.

This groundbreaking extension allowed for the rapid and efficient calculation of values like the square root of three <a class="yt-timestamp" data-t="12:30:00">[12:30:00]</a>. More significantly, it provided a new method for calculating Pi, which was far more efficient than the previous [[archimedes_method_of_calculating_pi | Archimedes]] polygon bisection method <a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>. [[newtons_method_for_pi_calculation | Newton]] used this extended binomial theorem in conjunction with his newly invented calculus (theory of Fluxions) to integrate the equation for a unit circle and derive an infinite series for Pi <a class="yt-timestamp" data-t="13:42:00">[13:42:00]</a>.