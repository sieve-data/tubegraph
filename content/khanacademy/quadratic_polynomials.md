---
title: Quadratic polynomials
videoId: eF6zYNzlZKQ
---

From: [[khanacademy]] <br/> 

A **quadratic polynomial** is a second-degree polynomial, meaning it is an expression where the variable is raised to the second power <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. Often called a "quadratic expression" or simply a "quadratic" <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. In the examples discussed, the variable used is `x` <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## Factoring Quadratic Polynomials

The goal of [[Factoring quadratics | factoring a quadratic polynomial]] is to break it down into the product of two binomials <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

### Understanding the Components

Consider the product of two binomials: `(x + a)` multiplied by `(x + b)` <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

Expanding this product results in:
`x * x = x²` <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>
`x * b = bx` <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>
`a * x = ax` <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>
`a * b = ab` <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>

Combining the `x` terms, the general form of a quadratic polynomial in standard form derived from `(x + a)(x + b)` is:
`x² + (a + b)x + ab` <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>

This reveals key relationships for [[Understanding components of a quadratic equation | understanding the components of a quadratic equation]]:
*   The coefficient of the `x` term (the first-degree coefficient) is the **sum** of `a` and `b` (`a + b`) <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
*   The constant term is the **product** of `a` and `b` (`ab`) <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

When the leading coefficient (the coefficient of the `x²` term) is 1, the process involves finding two numbers that satisfy these sum and product conditions <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. If the quadratic is not in standard form, it should be converted to apply this method <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

### Factoring Examples (Leading Coefficient of 1)

#### Example 1: All Positive Terms
> `x² + 10x + 9` <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>

We need to find two numbers, `a` and `b`, such that:
*   `a + b = 10` <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>
*   `a * b = 9` <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>

Considering integer factors of 9: (1, 9) or (3, 3) <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
*   1 + 9 = 10 (Matches) <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>
*   3 + 3 = 6 (Does not match) <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>

Therefore, `a = 1` and `b = 9` (or vice-versa) <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
**Factored form:** `(x + 1)(x + 9)` <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>

#### Example 2: Larger Numbers
> `x² + 15x + 50` <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>

We need `a + b = 15` and `a * b = 50` <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
Factors of 50: (1, 50), (2, 25), (5, 10) <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   1 + 50 = 51 (No) <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>
*   2 + 25 = 27 (No) <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>
*   5 + 10 = 15 (Yes) <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>

**Factored form:** `(x + 5)(x + 10)` <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>

#### Example 3: Negative `x` term, Positive Constant
> `x² - 11x + 24` <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>

We need `a + b = -11` and `a * b = 24` <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   Since the product (`ab`) is positive, `a` and `b` must have the same sign (both positive or both negative) <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
*   Since the sum (`a + b`) is negative, both `a` and `b` must be negative <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

Factors of 24: (1, 24), (2, 12), (3, 8), (4, 6) <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
We need a pair that sums to -11 when both are negative.
*   -3 + (-8) = -11 (Yes) <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>

**Factored form:** `(x - 3)(x - 8)` <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>

#### Example 4: Positive `x` term, Negative Constant
> `x² + 5x - 14` <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>

We need `a + b = 5` and `a * b = -14` <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
*   Since the product (`ab`) is negative, one number must be positive and the other negative <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

Factors of 14: (1, 14), (2, 7) <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
We need a pair that sums to 5, with one negative.
*   -1 + 14 = 13 (No) <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>
*   1 + (-14) = -13 (No) <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>
*   -2 + 7 = 5 (Yes) <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>

**Factored form:** `(x - 2)(x + 7)` <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>

#### Example 5: Negative `x` term, Negative Constant
> `x² - x - 56` <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>

We need `a + b = -1` (since -x is -1x) and `a * b = -56` <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
*   Since the product is negative, one number is positive and the other is negative <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   Since the sum is negative, the larger absolute value of the two numbers should be negative <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.

Factors of 56: (1, 56), (2, 28), (4, 14), (7, 8) <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.
The pair (7, 8) are close to each other, which is typical for a sum of -1 <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>.
*   -8 + 7 = -1 (Yes) <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>

**Factored form:** `(x - 8)(x + 7)` <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>

### Factoring Examples (Leading Coefficient of -1)

When the `x²` term has a negative coefficient, the easiest approach is to factor out -1 first <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.

#### Example 6:
> `-x² - 5x + 24` <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>

1.  Factor out -1: `-1(x² + 5x - 24)` <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>
2.  Now factor the inner quadratic `(x² + 5x - 24)`.
    *   Need `a + b = 5` and `a * b = -24` <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>.
    *   One positive, one negative, sum is positive (so the positive number has a larger absolute value) <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.
    *   Factors of 24: (1, 24), (2, 12), (3, 8), (4, 6) <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.
    *   Using (3, 8): -3 + 8 = 5 (Yes) <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.

**Factored form:** `-1(x - 3)(x + 8)` <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>

#### Example 7:
> `-x² + 18x - 72` <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>

1.  Factor out -1: `-1(x² - 18x + 72)` <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>
2.  Now factor the inner quadratic `(x² - 18x + 72)`.
    *   Need `a + b = -18` and `a * b = 72` <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.
    *   Product is positive, sum is negative, so both numbers must be negative <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.
    *   Factors of 72: (1, 72), (2, 36), (3, 24), (4, 18), (6, 12), (8, 9) <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.
    *   Using (6, 12): -6 + (-12) = -18 (Yes) <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>.

**Factored form:** `-1(x - 6)(x - 12)` <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>

> [!tip] Practice is Key
> Factoring quadratics can be "a bit of an art" <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>. It requires looking at factors, experimenting with positive and negative signs, and checking their sums and products <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>. With more practice, it becomes second nature <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>.