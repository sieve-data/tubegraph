---
title: Pattern matching in algebra
videoId: eF6zYNzlZKQ
---

From: [[khanacademy]] <br/> 

Factoring a second-degree polynomial, commonly known as a quadratic, involves breaking it down into the product of two binomials <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. This process often relies on recognizing and applying a specific pattern.

## Understanding the Pattern

A quadratic polynomial contains a variable raised to the second power, typically `x²` <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. The general form of a quadratic expression when factored into two binomials is `(x + a)(x + b)` <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

When you multiply these binomials using the distributive property, the result is:
`x * x = x²` <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>
`x * b = bx` <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>
`a * x = ax` <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>
`a * b = ab` <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>

[[combining_like_terms_in_algebra | Combining like terms]], this expands to:
`x² + bx + ax + ab` <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>
`x² + (a + b)x + ab` <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>

This expansion reveals a crucial pattern for [[pattern_matching_in_algebra | pattern matching]]:
*   The coefficient of the `x` term (first degree coefficient) is the **sum** of `a` and `b` (`a + b`) <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
*   The constant term is the **product** of `a` and `b` (`ab`) <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

This pattern is especially useful when the leading coefficient of the quadratic (the coefficient of the `x²` term) is 1 <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

## Applying the Pattern: Examples

The goal is to find two integer numbers (`a` and `b`) that satisfy these conditions <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

### Example 1: All Positive Terms

Consider the quadratic expression `x² + 10x + 9` <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.
We need to find two numbers whose product is 9 and whose sum is 10 <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
Factors of 9 are 1, 3, and 9 <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
*   If `a = 3`, `b = 3`: `3 + 3 = 6` (not 10) <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>
*   If `a = 1`, `b = 9`: `1 * 9 = 9` and `1 + 9 = 10` <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>

Thus, `a = 1` and `b = 9` (or vice-versa). The factored form is `(x + 1)(x + 9)` <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

### Example 2: Larger Numbers

Factor `x² + 15x + 50` <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
We need two numbers that multiply to 50 and add to 15 <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
Factors of 50:
*   `1 * 50`: `1 + 50 = 51` (no) <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>
*   `2 * 25`: `2 + 25 = 27` (no) <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>
*   `5 * 10`: `5 + 10 = 15` (yes) <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>

The factored form is `(x + 5)(x + 10)` <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

### Example 3: Negative Middle Term, Positive Constant

Factor `x² - 11x + 24` <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
We need two numbers whose product is 24 and sum is -11 <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
Since the product is positive, both numbers must be either positive or negative <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>. Since the sum is negative, both numbers must be negative <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
Factors of 24:
*   `1, 24`
*   `2, 12`
*   `3, 8`
*   `4, 6` <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>

Let's test negative pairs:
*   `-3 * -8 = 24`
*   `-3 + -8 = -11` (yes) <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>

The factored form is `(x - 3)(x - 8)` <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

### Example 4: Positive Middle Term, Negative Constant

Factor `x² + 5x - 14` <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
We need two numbers whose product is -14 and sum is 5 <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
Since the product is negative, one number must be positive and the other negative <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
Factors of 14:
*   `1, 14`
*   `2, 7` <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>

Test combinations:
*   `-1 + 14 = 13` (no) <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>
*   `1 + -14 = -13` (no) <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>
*   `-2 + 7 = 5` (yes!) <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>

The factored form is `(x - 2)(x + 7)` <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.

### Example 5: Negative Middle Term, Negative Constant

Factor `x² - x - 56` <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.
We need two numbers whose product is -56 and sum is -1 <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
Again, one positive, one negative. Since the sum is negative, the larger absolute value factor should be negative <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.
Factors of 56 that are close to each other:
*   `7 * 8 = 56` <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>

Test negative 8 and positive 7:
*   `-8 * 7 = -56`
*   `-8 + 7 = -1` (yes) <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>

The factored form is `(x - 8)(x + 7)` <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.

### Example 6: Factoring Out a Negative Leading Coefficient

Factor `-x² - 5x + 24` <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.
When the `x²` term has a negative coefficient, it's easiest to first factor out -1 <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.
`-1(x² + 5x - 24)` <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.
Now, factor the trinomial inside the parentheses. We need two numbers that multiply to -24 and add to 5 <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>.
Factors of 24 that have a difference of 5:
*   `3, 8` <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>
    *   Since the sum is positive, the larger factor should be positive.
*   `-3 * 8 = -24`
*   `-3 + 8 = 5` (yes) <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>

The factored form is `-1(x - 3)(x + 8)` <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.

### Example 7: Another Negative Leading Coefficient

Factor `-x² + 18x - 72` <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.
Factor out -1: `-1(x² - 18x + 72)` <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.
Now, find two numbers that multiply to 72 and add to -18 <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.
Since the product is positive and the sum is negative, both numbers must be negative <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.
Factors of 72 to consider:
*   `8, 9`: `-8 + -9 = -17` (close, but no) <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>
*   `6, 12`: `-6 + -12 = -18` (yes) <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>

The factored form is `-1(x - 6)(x - 12)` <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>.

> [!NOTE] Factoring as an Art
> Factoring polynomials like these can be seen as an "art" because it requires practice to quickly identify the correct factors and their signs <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>. With sufficient practice, this skill becomes second nature <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>.