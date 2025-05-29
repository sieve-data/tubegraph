---
title: Factoring by grouping
videoId: 2ZzuZvz33X0
---

From: [[khanacademy]] <br/> 

[[factoring_quadratic_equations|Factoring by grouping]] is a technique used to solve [[factoring_quadratic_equations|quadratic equations]], especially when they are explicitly set equal to zero <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. The primary goal is to factor the quadratic expression on the left-hand side into a product of binomials <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. This method is particularly effective for [[factoring_quadratics|factoring quadratics]] in the form of `ax² + bx + c = 0`.

## The Core Idea

When [[using_grouping_methods_to_factor_expressions|factoring by grouping]], the objective is to find two numbers (let's call them 'a' and 'b') that satisfy two conditions for a quadratic equation in the form `x² + Bx + C = 0` <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>:

1.  Their sum (`a + b`) must be equal to the coefficient of the middle term (B) <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
2.  Their product (`a * b`) must be equal to the constant term (C) <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

If the product (C) is a negative number, one of the two numbers (a or b) must be positive, and the other must be negative <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

## Step-by-Step Example

Let's solve the equation `s² - 2s - 35 = 0` using [[using_grouping_methods_to_factor_expressions|factoring by grouping]] <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>:

1.  **Find the two numbers**:
    *   We need two numbers that sum to -2 and multiply to -35 <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
    *   Considering factors of 35 that are two apart, and knowing one must be positive and one negative (due to the negative product), we find 5 and -7 <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
    *   Check: `5 + (-7) = -2` and `5 * (-7) = -35` <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

2.  **Split the middle term**:
    *   Rewrite the middle term (`-2s`) using the two numbers found: `+5s - 7s` <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
    *   The equation becomes: `s² + 5s - 7s - 35 = 0` <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

3.  **Group the terms**:
    *   Group the first two terms and the last two terms: `(s² + 5s) + (-7s - 35) = 0` <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

4.  **Factor out common factors from each group**:
    *   From `(s² + 5s)`, factor out `s`: `s(s + 5)` <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
    *   From `(-7s - 35)`, factor out `-7`: `-7(s + 5)` <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
    *   The expression is now: `s(s + 5) - 7(s + 5) = 0` <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

5.  **Factor out the common binomial**:
    *   Notice that `(s + 5)` is a common factor in both terms <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
    *   Factor it out: `(s + 5)(s - 7) = 0` <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

## Solving the Factored Equation

Once the expression is factored, we use the principle that if the product of two numbers is zero, then at least one of them must be zero <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>:

*   `s + 5 = 0` OR `s - 7 = 0` <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>

Solve each simple equation:

*   For `s + 5 = 0`: Subtract 5 from both sides, so `s = -5` <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   For `s - 7 = 0`: Add 7 to both sides, so `s = 7` <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

Thus, the solutions for `s` are -5 and 7 <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

### Verification
*   If `s = -5`: `(-5)² - 2(-5) - 35 = 25 + 10 - 35 = 0` <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   If `s = 7`: `(7)² - 2(7) - 35 = 49 - 14 - 35 = 0` <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

Both solutions are correct.

## Shortcut for Leading Coefficient 1

When the leading coefficient of a quadratic equation (the coefficient of `x²`) is 1, a shortcut can be used after finding the two numbers (a and b) that sum to the middle term and multiply to the constant term <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

For a quadratic `x² + Bx + C = 0`, if you find `a` and `b` such that `a + b = B` and `a * b = C`, then the factored form is directly `(x + a)(x + b) = 0` <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

In our example (`s² - 2s - 35 = 0`), since the leading coefficient is 1, once we found 5 and -7, we could have directly factored it as `(s + 5)(s - 7) = 0` <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>. This shortcut skips the explicit "splitting the middle term" and "grouping" steps, but [[using_grouping_methods_to_factor_expressions|factoring by grouping]] is a perfectly valid and appropriate method <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.