---
title: Solving difficult quadratic equations
videoId: bNQY0z76M5A
---

From: [[khanacademy]] <br/> 

When faced with [[quadratic_equations | quadratic equations]] that are challenging to solve by [[factoring_quadratic_equations | factoring]], a powerful and universally applicable technique is **completing the square** <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. This method can solve any [[quadratic_equations | quadratic equation]] and forms the basis for the quadratic formula <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. It builds upon the idea of [[solving_quadratic_equations | solving quadratics]] using perfect squares <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## Understanding Completing the Square

The essence of completing the square involves transforming a [[quadratic_equations | quadratic equation]] into a perfect square by strategically adding and subtracting values from both sides of the equation <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

### Example 1: Basic Application

Consider the [[quadratic_equations | quadratic equation]]: `x² - 4x = 5` <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

1.  **Identify the required term:** To make the left-hand side a perfect square (in the form `(x - a)²`), we need to find a constant `a²` such that `-2a` equals the coefficient of the `x` term <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
    *   In this case, the coefficient of `x` is -4. So, `-2a = -4`, which means `a = 2` <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
    *   The term to add is `a²`, which is `(-2)² = 4` <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. This is found by taking half of the x-coefficient (-4/2 = -2) and squaring it <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

2.  **Add the term to both sides:** To maintain equality, add 4 to both sides of the equation <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
    `x² - 4x + 4 = 5 + 4` <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>
    `x² - 4x + 4 = 9` <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>

3.  **Rewrite as a perfect square:** The left side is now `(x - 2)²` <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
    `(x - 2)² = 9` <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>

4.  **Solve for x:** Take the square root of both sides, remembering both positive and negative roots <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
    `x - 2 = ±√9` <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>
    `x - 2 = ±3` <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>

5.  **Isolate x:** Add 2 to both sides <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
    `x = 2 ± 3` <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>

    This yields two solutions:
    *   `x = 2 + 3 = 5` <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>
    *   `x = 2 - 3 = -1` <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>

While this specific example could have been solved faster by [[factoring_quadratic_equations | factoring]] `x² - 4x - 5 = 0` into `(x - 5)(x + 1) = 0` <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>, completing the square is advantageous because it consistently works, regardless of the complexity of the coefficients <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.

### Example 2: Solving a Difficult Quadratic Equation

Let's solve `10x² - 30x - 8 = 0` using completing the square <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>. This problem would be painful to solve using [[factoring_quadratic_polynomials | factoring by grouping]] <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.

1.  **Simplify by dividing by a common factor:** Divide all terms by 2 <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
    `5x² - 15x - 4 = 0` <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>

2.  **Make the leading coefficient 1:** Divide all terms by the leading coefficient, 5 <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
    `x² - 3x - 4/5 = 0` <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>
    This step often introduces fractions, which makes direct [[factoring_quadratic_equations | factoring]] very difficult <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.

3.  **Move the constant term to the right side:** Add 4/5 to both sides <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.
    `x² - 3x = 4/5` <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>

4.  **Complete the square:**
    *   Take half of the x-coefficient (-3) and square it: `(-3/2)² = 9/4` <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.
    *   Add 9/4 to both sides of the equation <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
    `x² - 3x + 9/4 = 4/5 + 9/4` <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>

5.  **Simplify the right side:** Find a common denominator for the fractions on the right side (20) <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
    `4/5 = 16/20` <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>
    `9/4 = 45/20` <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>
    `16/20 + 45/20 = 61/20` <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>

    So, the equation becomes:
    `x² - 3x + 9/4 = 61/20` <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>

6.  **Rewrite as a perfect square:**
    `(x - 3/2)² = 61/20` <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>

7.  **Solve for x:**
    *   Take the square root of both sides: `x - 3/2 = ±√(61/20)` <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>
    *   Add 3/2 to both sides: `x = 3/2 ± √(61/20)` <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>

This exact form is the solution. Using a calculator, the approximate decimal values are:
*   `x ≈ 3.246` <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>
*   `x ≈ -0.246` <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>

Completing the square proves invaluable for solving [[quadratic_equations | quadratic equations]] that are not easily factorable, especially those with fractional or irrational solutions <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.