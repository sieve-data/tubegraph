---
title: Understanding quadratic expressions
videoId: eF6zYNzlZKQ
---

From: [[khanacademy]] <br/> 

A quadratic expression is defined as a second-degree polynomial, meaning it contains a variable raised to the second power <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. This is often referred to as a quadratic polynomial or simply a quadratic <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. In typical examples, the variable used is `x` <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## Factoring Quadratic Expressions

The goal when [[factoring_quadratic_polynomials | factoring a second degree polynomial]] is to express it as the product of two binomials <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

### The Product of Two Binomials

Consider the product of two simple binomials, such as `(x + a)` and `(x + b)`:
`(x + a)(x + b) = x * x + x * b + a * x + a * b` <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>
This simplifies to `x² + (a + b)x + ab` <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

From this general form, we can observe that:
*   The coefficient of the `x` term (first-degree coefficient) is the sum of `a` and `b` (`a + b`) <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
*   The constant term is the product of `a` and `b` (`ab`) <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

When the leading coefficient of the `x²` term is 1, the strategy is to find two numbers that add up to the `x` coefficient and multiply to the constant term <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. Ensure the quadratic expression is in standard form before applying this method <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

### Examples of Factoring

#### Example 1: All Positive Terms

To factor `x² + 10x + 9`:
1.  Identify that `a + b = 10` and `ab = 9` <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
2.  Consider the factors of 9: (1, 9) and (3, 3) <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
3.  Check which pair sums to 10:
    *   3 + 3 = 6 (Does not equal 10) <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>
    *   1 + 9 = 10 (Matches) <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>
4.  Therefore, `a = 1` and `b = 9` <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
5.  The factored form is `(x + 1)(x + 9)` <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

To factor `x² + 15x + 50`:
1.  Identify that `a + b = 15` and `ab = 50` <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
2.  Consider the factors of 50: (1, 50), (2, 25), (5, 10) <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
3.  Check which pair sums to 15:
    *   1 + 50 = 51 (Does not equal 15) <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>
    *   2 + 25 = 27 (Does not equal 15) <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>
    *   5 + 10 = 15 (Matches) <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>
4.  The factored form is `(x + 5)(x + 10)` <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

#### Example 2: Incorporating Negative Signs

The [[working_with_positive_and_negative_factors_in_quadratics | positive and negative factors]] play a crucial role in factoring.

**Case: Positive Product, Negative Sum**
If `ab` is positive and `a + b` is negative, then both `a` and `b` must be negative <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

To factor `x² - 11x + 24`:
1.  Identify that `a + b = -11` and `ab = 24` <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
2.  Since the product is positive and the sum is negative, both `a` and `b` must be negative <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
3.  Consider factors of 24: (1, 24), (2, 12), (3, 8), (4, 6) <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
4.  We need two *negative* numbers from these factors that sum to -11. The pair (3, 8) sums to 11 <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
5.  So, -3 and -8:
    *   (-3) * (-8) = 24 <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>
    *   (-3) + (-8) = -11 <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>
6.  The factored form is `(x - 3)(x - 8)` <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.

**Case: Negative Product**
If `ab` is negative, then one number is positive and the other is negative <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

To factor `x² + 5x - 14`:
1.  Identify that `a + b = 5` and `ab = -14` <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
2.  Since the product is negative, one factor is positive and one is negative <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
3.  Consider factors of 14: (1, 14), (2, 7) <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
4.  We need a pair where the sum is 5.
    *   -2 + 7 = 5 (Matches) <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>
    *   -2 * 7 = -14 <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>
5.  The factored form is `(x - 2)(x + 7)` <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.

To factor `x² - x - 56`:
1.  Identify that `a + b = -1` and `ab = -56` <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
2.  Since the product is negative, one factor is positive and one is negative <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. Since the sum is negative, the number with the larger absolute value must be negative <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.
3.  Consider factors of 56. The pair (7, 8) is a good candidate because they are close in value <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.
4.  We need a pair that sums to -1.
    *   -8 + 7 = -1 (Matches) <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>
    *   -8 * 7 = -56 <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>
5.  The factored form is `(x - 8)(x + 7)` <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.

#### Example 3: Negative Leading Coefficient

If the quadratic expression has a negative coefficient on the `x²` term, the easiest approach is to factor out a -1 first <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.

To factor `-x² - 5x + 24`:
1.  Factor out -1: `-1(x² + 5x - 24)` <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.
2.  Now factor the inner quadratic: `x² + 5x - 24`.
    *   Need `a + b = 5` and `ab = -24` <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>.
    *   Since the product is negative, one factor is positive, one is negative <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.
    *   Consider factors of 24. The pair (3, 8) seems promising <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.
    *   To sum to positive 5, it must be -3 and 8:
        *   -3 + 8 = 5 <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>
        *   -3 * 8 = -24 <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>
3.  The factored form is `-1(x - 3)(x + 8)` <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.

To factor `-x² + 18x - 72`:
1.  Factor out -1: `-1(x² - 18x + 72)` <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.
2.  Now factor the inner quadratic: `x² - 18x + 72`.
    *   Need `a + b = -18` and `ab = 72` <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.
    *   Since the product is positive and the sum is negative, both factors must be negative <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.
    *   Consider factors of 72. The pair (6, 12) sums to 18.
    *   So, -6 and -12:
        *   -6 + (-12) = -18 <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>
        *   -6 * -12 = 72
3.  The factored form is `-1(x - 6)(x - 12)` <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>.

Factoring quadratic expressions is an art that becomes second nature with practice, requiring examination of factors and strategic use of [[working_with_positive_and_negative_factors_in_quadratics | positive and negative signs]] <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.