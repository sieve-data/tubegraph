---
title: Factoring quadratic equations
videoId: 2ZzuZvz33X0
---

From: [[khanacademy]] <br/> 

[[solving_quadratic_equations | Solving a quadratic equation]] like `s^2 - 2s - 35 = 0` is best approached by [[factoring_polynomials | factoring]] the left-hand side, especially when the equation is explicitly set to zero <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. Once factored, the principle that if the product of two numbers is zero, then at least one of the numbers must be zero, can be applied <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

## Methods for Factoring Quadratic Equations

### 1. [[factoring_by_grouping | Factoring by Grouping]]

To factor a [[quadratic_equations | quadratic equation]] like `s^2 - 2s - 35 = 0` using [[factoring_by_grouping | factoring by grouping]]:
1.  **Find two numbers** whose sum is equal to the middle coefficient (-2) and whose product is equal to the constant term (-35) <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
    *   Let these numbers be `a` and `b`. So, `a + b = -2` and `a * b = -35` <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
    *   Since the product is negative, one number must be positive and the other negative <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
    *   The numbers are 5 and -7, because 5 + (-7) = -2 and 5 * (-7) = -35 <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
2.  **Split the middle term** using these two numbers <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
    *   Rewrite `s^2 - 2s - 35` as `s^2 + 5s - 7s - 35` <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
3.  **Group the terms** into two pairs <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
    *   `(s^2 + 5s)` and `(-7s - 35)`
4.  **Factor out the greatest common factor (GCF)** from each group <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
    *   `s(s + 5)` from the first group <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
    *   `-7(s + 5)` from the second group (note that factoring out a negative ensures the binomial matches) <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
5.  **Factor out the common binomial** `(s + 5)` <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
    *   This results in `(s + 5)(s - 7)` <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

### 2. Shortcut for Leading Coefficient of 1

When the leading coefficient of a [[quadratic_expressions | quadratic expression]] is 1 (e.g., `x^2 + Bx + C`), you can factor directly <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. If you have an expression of the form `x^2 + (a+b)x + ab`, it can be directly factored into `(x + a)(x + b)` <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

For `s^2 - 2s - 35 = 0`:
1.  Find two numbers that add up to -2 and multiply to -35 <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. As before, these are 5 and -7 <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
2.  Directly factor the expression as `(s + 5)(s - 7)` <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

## Solving the Factored Equation

Once the [[quadratic_equations | quadratic equation]] is factored into the form `(s + 5)(s - 7) = 0`, the solutions can be found:
1.  **Set each factor equal to zero** <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
    *   `s + 5 = 0`
    *   `s - 7 = 0`
2.  **Solve each linear equation for `s`** <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
    *   From `s + 5 = 0`, subtract 5 from both sides to get `s = -5` <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
    *   From `s - 7 = 0`, add 7 to both sides to get `s = 7` <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

Thus, the solutions for `s` are -5 and 7 <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

### Verification
You can verify these solutions by plugging them back into the original equation `s^2 - 2s - 35 = 0` <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   For `s = -5`: `(-5)^2 - 2(-5) - 35 = 25 + 10 - 35 = 35 - 35 = 0` <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   For `s = 7`: `(7)^2 - 2(7) - 35 = 49 - 14 - 35 = 35 - 35 = 0` <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

Both solutions satisfy the equation <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.