---
title: Real and imaginary numbers in quadratics
videoId: i7idZfS8t8w
---

From: [[khanacademy]] <br/> 

The [[quadratic_formula_introduction | quadratic formula]] is one of the most useful formulas in mathematics for [[solving_quadratic_equations | solving quadratic equations]] <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. It is used to solve for the roots, or zeroes, of [[quadratic_equations | quadratic equations]] <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. While memorization is generally not encouraged, it is recommended to memorize the [[quadratic_formula_introduction | quadratic formula]] with the understanding of its proof <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. The formula itself is derived by completing the square on a general [[quadratic_equations | quadratic equation]] <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

## The Quadratic Formula

For a general [[quadratic_equations | quadratic equation]] in the form **ax² + bx + c = 0** <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>:
*   `a` is the coefficient of the x² term <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   `b` is the coefficient of the x term <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
*   `c` is the constant term <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

The solutions for x are given by the [[quadratic_formula_introduction | quadratic formula]]:
> x = -b ± √(b² - 4ac) / 2a <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>

## Applying the Quadratic Formula

### Example 1: Verifying with a Factorable Quadratic
Consider the equation x² + 4x - 21 = 0 <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
Here, a = 1, b = 4, and c = -21 <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

Plugging these values into the [[quadratic_formula_introduction | quadratic formula]]:
x = -4 ± √(4² - 4 * 1 * -21) / (2 * 1) <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>
x = -4 ± √(16 + 84) / 2 <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>
x = -4 ± √100 / 2 <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>
x = -4 ± 10 / 2 <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>
x = -2 ± 5 <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>

This yields two solutions:
*   x = -2 + 5 = 3 <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>
*   x = -2 - 5 = -7 <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>

These results match those obtained by factoring the original equation (x + 7)(x - 3) = 0, which gives x = -7 or x = 3 <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

### Example 2: Quadratic with No Real Solutions
Consider the equation 3x² + 6x = -10 <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
First, rewrite it in the standard form ax² + bx + c = 0 by adding 10 to both sides:
3x² + 6x + 10 = 0 <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>

Here, a = 3, b = 6, and c = 10 <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

Applying the [[quadratic_formula_introduction | quadratic formula]]:
x = -6 ± √(6² - 4 * 3 * 10) / (2 * 3) <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>
x = -6 ± √(36 - 120) / 6 <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>
x = -6 ± √(-84) / 6 <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>

When the term under the square root (b² - 4ac) is negative, the equation has **no real solutions** <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a> <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. This means that if you were to graph the corresponding [[understanding_quadratic_expressions | quadratic expression]], it would not intersect the x-axis <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. In the future, the concept of **imaginary numbers** will be introduced to express these solutions <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

### Example 3: Quadratic with Non-Integer Real Solutions
Consider the equation -3x² + 12x + 1 = 0 <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.
Here, a = -3, b = 12, and c = 1 <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.

Applying the [[quadratic_formula_introduction | quadratic formula]]:
x = -12 ± √(12² - 4 * -3 * 1) / (2 * -3) <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>
x = -12 ± √(144 + 12) / -6 <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>
x = -12 ± √156 / -6 <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>

To simplify √156, perform a prime factorization:
156 = 2 * 78 = 2 * 2 * 39 <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>
So, √156 = √(2² * 39) = 2√39 <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.

Substitute back into the formula:
x = -12 ± 2√39 / -6 <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>

Divide both numerator terms and the denominator by 2:
x = (-6 ± √39) / -3 <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>

This can be further simplified:
x = -6/-3 ± √39/-3 <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>
x = 2 ± (-√39/3) <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>

Since "plus or minus" already accounts for both positive and negative possibilities, the final form is:
x = 2 ± √39/3 <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>

These solutions are real numbers, meaning the graph of y = -3x² + 12x + 1 will intersect the x-axis at two distinct points <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>.