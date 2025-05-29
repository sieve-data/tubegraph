---
title: Using negative factors in quadratic expressions
videoId: eF6zYNzlZKQ
---

From: [[khanacademy]] <br/> 

A quadratic expression is a second-degree polynomial, meaning it contains a variable raised to the second power <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. When [[factoring_quadratic_expressions | factoring]] a quadratic expression of the form `x² + Bx + C` into the product of two binomials `(x + a)(x + b)`, there's a direct relationship between the coefficients and the factors:
*   The sum of the factors `a` and `b` (`a + b`) equals the coefficient of the x-term (`B`) <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
*   The product of the factors `a` and `b` (`a * b`) equals the constant term (`C`) <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

This method is primarily used when the leading coefficient (the coefficient of the x² term) is 1 <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

## Factoring Quadratics with Negative Coefficients

When dealing with negative coefficients in a quadratic expression, the same principles apply, but careful consideration of the signs of the factors is necessary.

### Case 1: Positive Constant Term, Negative Middle Term (e.g., `x² - 11x + 24`)

In an expression like `x² - 11x + 24`:
*   The product of the two factors (`a * b`) must be positive (24) <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
*   The sum of the two factors (`a + b`) must be negative (-11) <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

For the product to be positive, both `a` and `b` must be either both positive or both negative <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. Since their sum is negative, it indicates that both factors must be negative <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

To find the factors:
1.  List pairs of factors of 24: (1, 24), (2, 12), (3, 8), (4, 6) <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
2.  Test the sums:
    *   3 + 8 = 11 <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.
    *   Since we need a sum of -11, consider -3 and -8.
    *   (-3) * (-8) = 24 (correct product) <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
    *   (-3) + (-8) = -11 (correct sum) <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
Therefore, `x² - 11x + 24` factors to `(x - 3)(x - 8)` <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.

### Case 2: Negative Constant Term (e.g., `x² + 5x - 14`)

In an expression like `x² + 5x - 14`:
*   The product of the two factors (`a * b`) must be negative (-14) <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
*   The sum of the two factors (`a + b`) must be positive (5) <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.

For the product to be negative, one factor must be positive and the other must be negative <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. The fact that their sum is positive means the factor with the larger absolute value must be positive.

To find the factors:
1.  List pairs of factors of 14: (1, 14), (2, 7) <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
2.  Test combinations with one negative factor:
    *   -1 + 14 = 13 (not 5) <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.
    *   -2 + 7 = 5 (correct sum!) <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
    *   (-2) * 7 = -14 (correct product) <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
Therefore, `x² + 5x - 14` factors to `(x - 2)(x + 7)` <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.

Another example: `x² - x - 56` <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.
*   Product is -56, so one factor is positive, one is negative <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
*   Sum is -1, so the factor with the larger absolute value must be negative <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.
Factors of 56 are 7 and 8 <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>. Since the sum is -1, we need -8 and 7.
*   (-8) * 7 = -56 <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.
*   (-8) + 7 = -1 <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.
Thus, `x² - x - 56` factors to `(x - 8)(x + 7)` <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.

### Case 3: Negative Leading Coefficient (e.g., `-x² - 5x + 24`)

When the coefficient of the x² term is negative, the easiest approach is to [[factoring_quadratic_expressions | factor out]] a negative 1 from the entire expression <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>. This converts the problem into one with a positive leading coefficient, similar to the [[factoring_quadratics_with_a_leading_coefficient_of_1 | examples above]] <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.

For `-x² - 5x + 24`:
1.  Factor out -1: `-1(x² + 5x - 24)` <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.
2.  Now, factor the inner quadratic `x² + 5x - 24`.
    *   Product is -24 (one positive, one negative factor) <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>.
    *   Sum is 5 (positive, so the larger factor must be positive).
    *   Factors of 24 include (3, 8).
    *   Consider -3 and 8: (-3) * 8 = -24 and (-3) + 8 = 5 <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.
3.  Substitute the factored form back: `-1(x - 3)(x + 8)` <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>.

Another example: `-x² + 18x - 72` <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.
1.  Factor out -1: `-1(x² - 18x + 72)` <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.
2.  Factor `x² - 18x + 72`.
    *   Product is 72 (both factors same sign) <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>.
    *   Sum is -18 (negative, so both factors must be negative) <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.
    *   Factors of 72 include (6, 12) <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>.
    *   Consider -6 and -12: (-6) * (-12) = 72 and (-6) + (-12) = -18 <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>.
3.  Substitute back: `-1(x - 6)(x - 12)` <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>.

> [!NOTE]
> [[factoring_quadratic_expressions | Factoring]] quadratics, especially with negative terms, requires practice and developing an "art" for identifying the correct factors <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. Consider factors of the constant term first, then test their sums while paying close attention to the signs <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>.