---
title: Factoring quadratic polynomials
videoId: eF6zYNzlZKQ
---

From: [[khanacademy]] <br/> 

[[factoring_quadratic_equations | Factoring]] a second-degree [[factoring_polynomials | polynomial]], often called a [[quadratic_equations | quadratic]] or [[understanding_quadratic_expressions | quadratic expression]], involves expressing it as the product of two binomials <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. These expressions typically have a variable raised to the second power, such as `x` squared <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

## Understanding the Relationship Between Binomials and Quadratics

When two binomials of the form `(x + a)` and `(x + b)` are multiplied, the result is a [[quadratic_equations | quadratic]] expression:
`(x + a)(x + b) = x² + bx + ax + ab` <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
This can be simplified to `x² + (a + b)x + ab` <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

From this general form, we can observe key relationships:
*   The coefficient of the `x` term (the first-degree coefficient) is the sum of `a` and `b` (`a + b`) <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
*   The constant term is the product of `a` and `b` (`ab`) <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

Therefore, when [[factoring_quadratic_equations | factoring]] a [[quadratic_equations | quadratic]] expression like `x² + cx + d` (where `c` is the coefficient of `x` and `d` is the constant term), the goal is to find two numbers, `a` and `b`, such that their sum `(a + b)` equals `c`, and their product `(a * b)` equals `d` <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. This method is primarily used when the leading coefficient (the coefficient of `x²`) is 1 <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. It's important to ensure the expression is in standard form first <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

> [!INFO] Tip for [[working_with_positive_and_negative_factors_in_quadratics | Positive and Negative Factors]]
> When the constant term is positive, `a` and `b` must have the same sign <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>. If their sum is negative, both `a` and `b` must be negative <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
> When the constant term is negative, `a` and `b` must have opposite signs (one positive, one negative) <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

## Examples of Factoring Quadratic Expressions

### Example 1: All Positive Terms

Factor `x² + 10x + 9` <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

We need `a + b = 10` and `a * b = 9` <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
*   Factors of 9 are (1, 9) or (3, 3) <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
*   If `a=3, b=3`, then `a+b=6`, which is not 10 <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   If `a=1, b=9`, then `a*b=9` and `a+b=10` <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

> [!EXAMPLE]
> The factored form is `(x + 1)(x + 9)` <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

### Example 2: Larger Coefficients

Factor `x² + 15x + 50` <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

We need `a + b = 15` and `a * b = 50` <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
*   Factors of 50 include (1, 50), (2, 25), (5, 10) <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   `1 + 50 = 51` (not 15) <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   `2 + 25 = 27` (not 15) <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   `5 + 10 = 15` (this works) <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.

> [!EXAMPLE]
> The factored form is `(x + 5)(x + 10)` <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

### Example 3: Negative Middle Term, Positive Constant

Factor `x² - 11x + 24` <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

We need `a + b = -11` and `a * b = 24` <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
Since `a * b` is positive and `a + b` is negative, both `a` and `b` must be negative <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
*   Factors of 24 include (1, 24), (2, 12), (3, 8), (4, 6) <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
*   Consider their negative counterparts:
    *   `-3 + (-8) = -11` <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
    *   `-3 * (-8) = 24` <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.

> [!EXAMPLE]
> The factored form is `(x - 3)(x - 8)` <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

### Example 4: Positive Middle Term, Negative Constant

Factor `x² + 5x - 14` <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

We need `a + b = 5` and `a * b = -14` <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
Since `a * b` is negative, one number must be positive and the other negative <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
*   Factors of 14 are (1, 14), (2, 7) <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.
*   Test combinations for a sum of 5:
    *   `-1 + 14 = 13` (not 5) <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
    *   `1 + (-14) = -13` (not 5) <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.
    *   `-2 + 7 = 5` (this works) <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
    *   `-2 * 7 = -14` (this works) <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.

> [!EXAMPLE]
> The factored form is `(x - 2)(x + 7)` <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.

### Example 5: Negative Middle Term, Negative Constant

Factor `x² - x - 56` <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

We need `a + b = -1` (since `-x` is `-1x`) and `a * b = -56` <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
Since `a * b` is negative, one number must be positive and the other negative. The sum is negative, so the larger absolute value will be negative <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.
*   Factors of 56 include (1, 56), (2, 28), (4, 14), (7, 8) <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.
*   The pair (7, 8) is close, with a difference of 1 <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>.
*   If we use `-8` and `7`:
    *   `-8 * 7 = -56` <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.
    *   `-8 + 7 = -1` <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.

> [!EXAMPLE]
> The factored form is `(x - 8)(x + 7)` <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.

### Example 6: [[factoring_quadratics_with_negative_leading_coefficients | Negative Leading Coefficient]]

Factor `-x² - 5x + 24` <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.

The easiest approach for [[factoring_quadratics_with_negative_leading_coefficients | quadratics with a negative leading coefficient]] is to factor out -1 first <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>:
`-1 * (x² + 5x - 24)` <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.

Now, factor the inner [[quadratic_equations | quadratic]]: `x² + 5x - 24`.
We need `a + b = 5` and `a * b = -24` <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>.
One number is positive, one is negative.
*   Factors of 24: (1, 24), (2, 12), (3, 8), (4, 6) <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.
*   Consider (3, 8):
    *   If `-3` and `8`: `-3 + 8 = 5` <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.
    *   `-3 * 8 = -24` <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.

> [!EXAMPLE]
> The factored form is `-1 * (x - 3)(x + 8)` <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.

### Example 7: Another [[factoring_quadratics_with_negative_leading_coefficients | Negative Leading Coefficient]]

Factor `-x² + 18x - 72` <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.

Factor out -1: `-1 * (x² - 18x + 72)` <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.

Now, factor the inner [[quadratic_equations | quadratic]]: `x² - 18x + 72`.
We need `a + b = -18` and `a * b = 72` <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.
Since `a * b` is positive and `a + b` is negative, both numbers must be negative <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>.
*   Factors of 72: (1, 72), (2, 36), (3, 24), (4, 18), (6, 12), (8, 9) <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.
*   Consider (6, 12):
    *   `-6 + (-12) = -18` <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>.
    *   `-6 * (-12) = 72` <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>.

> [!EXAMPLE]
> The factored form is `-1 * (x - 6)(x - 12)` <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>.

[[factoring_quadratic_equations | Factoring quadratic polynomials]] is an art that requires practice with [[working_with_positive_and_negative_factors_in_quadratics | positive and negative factors]] and identifying factor pairs <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>. With repeated practice, this skill becomes second nature <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>.