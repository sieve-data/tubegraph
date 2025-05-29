---
title: Factoring polynomials
videoId: 7Uos1ED3KHI
---

From: [[khanacademy]] <br/> 

[[canceling_common_factors_in_expressions | Canceling common factors in expressions]] is a key concept when simplifying rational expressions, similar to how we simplify fractions (rational numbers) to their lowest terms <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

For example, to simplify 3/6, we recognize that 3 and 6 share a common factor of 3 <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. Since 6 can be written as 2 times 3 <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>, the 3s can [[canceling_common_factors_in_expressions | cancel out]], resulting in 1/2 in lowest terms <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. The same principle applies to rational expressions <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## What are Rational Expressions?

Rational expressions are similar to rational numbers, but instead of the numerator and denominator being actual numbers, they are expressions involving variables <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

## Simplifying Rational Expressions

The process involves [[factoring quadratic polynomials | factoring]] both the numerator and the denominator to identify and [[canceling_common_factors_in_expressions | cancel out]] common factors <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

### Example 1: Factoring out a common numerical factor

Consider the expression:
```
(9x + 3) / (12x + 4) <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>
```
1.  **Factor the numerator:** Factor out the common factor of 3:
    `3(3x + 1)` <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>
2.  **Factor the denominator:** Factor out the common factor of 4:
    `4(3x + 1)` <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>
3.  **Identify and cancel common factors:** Both the numerator and denominator share the common factor `(3x + 1)` <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. These can [[canceling_common_factors_in_expressions | cancel out]] <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
    The expression simplifies to `3/4` <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

### Example 2: Factoring a Difference of Squares

Consider the expression:
```
(x² - 9) / (5x + 15) <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>
```
1.  **Factor the numerator:** This is a [[factoring_quadratic_equations | difference of squares]] `(a² - b² = (a+b)(a-b))` <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>:
    `(x + 3)(x - 3)` <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>
2.  **Factor the denominator:** Factor out the common factor of 5:
    `5(x + 3)` <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>
3.  **Identify and cancel common factors:** The common factor `(x + 3)` can be [[canceling_common_factors_in_expressions | canceled out]] <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
    The simplified expression is `(x - 3) / 5` <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

### Important Note on Excluded Values

When simplifying rational expressions by [[canceling_common_factors_in_expressions | canceling common factors]] that contain variables, it's crucial to state the values of the variable that would have made the *original* denominator zero (undefined) <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

For `(x² - 9) / (5x + 15)`, the original denominator `5(x + 3)` would be zero if `x = -3` <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
Therefore, the simplified expression `(x - 3) / 5` is equivalent to the original *only if* we specify that `x ≠ -3` <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. Without this condition, the simplified expression is defined at `x = -3` while the original is not <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

Similarly, for `(9x + 3) / (12x + 4)`, the original denominator `12x + 4` would be zero if `x = -1/3` <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. So, `3/4` is equivalent to the original *only if* `x ≠ -1/3` <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

### Example 3: Factoring Quadratic Trinomials

Consider the expression:
```
(x² + 6x + 5) / (x² - x - 2) <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>
```
1.  **Factor the numerator:** Find two numbers that multiply to 5 and add to 6. These are 5 and 1 <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
    `(x + 5)(x + 1)` <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>
2.  **Factor the denominator:** Find two numbers that multiply to -2 and add to -1. These are -2 and 1 <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
    `(x - 2)(x + 1)` <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>
3.  **Identify and cancel common factors:** The common factor `(x + 1)` can be [[canceling_common_factors_in_expressions | canceled out]] <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
    The simplified expression is `(x + 5) / (x - 2)` <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
4.  **State the exclusion:** The original denominator would be zero if `x = -1` <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.
    So, the equivalence holds only if `x ≠ -1` <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

### Example 4: Factoring by Grouping (for leading coefficients not equal to 1)

Consider the expression:
```
(3x² + 3x - 18) / (2x² + 5x - 3) <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>
```
This requires [[factoring_by_grouping | factoring by grouping]] for both the numerator and denominator <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

#### Factoring the Numerator (3x² + 3x - 18)

1.  Find two numbers that multiply to `3 * -18 = -54` and add to `3` <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. These numbers are 9 and -6 <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
2.  Rewrite the middle term (`3x`) using these numbers:
    `3x² + 9x - 6x - 18` <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>
3.  Group terms and factor out common factors:
    `(3x² + 9x) + (-6x - 18)` <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>
    `3x(x + 3) - 6(x + 3)` <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>
4.  Factor out the common binomial `(x + 3)`:
    `(3x - 6)(x + 3)` <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>

#### Factoring the Denominator (2x² + 5x - 3)

1.  Find two numbers that multiply to `2 * -3 = -6` and add to `5` <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>. These numbers are 6 and -1 <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.
2.  Rewrite the middle term (`5x`) using these numbers:
    `2x² + 6x - x - 3` <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>
3.  Group terms and factor out common factors:
    `(2x² + 6x) + (-x - 3)` <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>
    `2x(x + 3) - 1(x + 3)` <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>
4.  Factor out the common binomial `(x + 3)`:
    `(2x - 1)(x + 3)` <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>

#### Simplification and Exclusion

Now, rewrite the original expression with the factored forms:
```
((3x - 6)(x + 3)) / ((2x - 1)(x + 3)) <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>
```
1.  **Identify and cancel common factors:** The common factor `(x + 3)` can be [[canceling_common_factors_in_expressions | canceled out]] <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.
    The simplified expression is `(3x - 6) / (2x - 1)` <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.
2.  **State the exclusion:** The original denominator would be zero if `x = -3` <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.
    So, the equivalence holds only if `x ≠ -3` <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.