---
title: Completing the square as a technique for solving quadratic equations
videoId: bNQY0z76M5A
---

From: [[khanacademy]] <br/> 

[[completing_the_square_and_derivation_of_the_quadratic_formula | Completing the square]] is a powerful technique used to solve any [[introduction_to_the_quadratic_formula | quadratic equation]] <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. It forms the basis for the [[completing_the_square_and_derivation_of_the_quadratic_formula | derivation of the quadratic formula]] <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. The core idea is to transform a quadratic equation into a perfect square, making it straightforward to solve <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

## Core Concept: Converting to a Perfect Square

The method builds upon the principle of [[converting_a_quadratic_equation_into_a_perfect_square | solving quadratic equations using perfect squares]] <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. The goal is to manipulate a quadratic expression `x^2 + bx` by adding a specific constant term to make it a perfect square in the form `(x + a)^2` or `(x - a)^2` <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

For an expression `x^2 - 2ax + a^2`, it factors into `(x - a)^2` <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. To find the constant term `a^2` needed to complete the square from `x^2 + bx`, you take half of the coefficient `b` and square it <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a> <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

## Examples of Solving Quadratic Equations by Completing the Square

### Example 1: A Simple Case

Let's solve the quadratic equation `x^2 - 4x = 5` <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

1.  **Identify the term to complete the square**:
    *   Take half of the coefficient of `x` (which is -4): `(-4) / 2 = -2` <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
    *   Square this value: `(-2)^2 = 4` <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. This is the number needed to complete the square.
2.  **Add the term to both sides of the equation**:
    *   Add 4 to the left side to create a perfect square <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
    *   To maintain equality, add 4 to the right side as well <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
    *   `x^2 - 4x + 4 = 5 + 4` <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>
    *   `x^2 - 4x + 4 = 9` <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>
3.  **Rewrite the left side as a perfect square**:
    *   The expression `x^2 - 4x + 4` is `(x - 2)^2` <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
    *   So, `(x - 2)^2 = 9` <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
4.  **Solve for x**:
    *   Take the square root of both sides, remembering both positive and negative roots <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
    *   `x - 2 = ±√9` <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>
    *   `x - 2 = ±3` <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>
    *   Add 2 to both sides: `x = 2 ± 3` <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>
    *   This yields two solutions:
        *   `x = 2 + 3 = 5` <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>
        *   `x = 2 - 3 = -1` <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>

### Comparison with Factoring

For simple cases like the one above, [[comparisons_of_methods_completing_the_square_vs_factoring | factoring]] can be a faster method <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. If we rearrange `x^2 - 4x = 5` to `x^2 - 4x - 5 = 0`, we can factor it into `(x - 5)(x + 1) = 0`, leading to the solutions `x = 5` or `x = -1` <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. However, [[completing_the_square_and_derivation_of_the_quadratic_formula | completing the square]] is a universal technique that will always work, regardless of the coefficients or complexity of the problem <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.

### Example 2: A More Complex Case with Fractions

Consider the equation `10x^2 - 30x - 8 = 0` <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

1.  **Simplify the equation (optional but recommended)**:
    *   Divide all terms by the greatest common factor (2): `5x^2 - 15x - 4 = 0` <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
2.  **Make the leading coefficient 1**:
    *   Divide all terms by the coefficient of `x^2` (which is 5): `x^2 - 3x - 4/5 = 0` <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a> <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
    *   This equation would be very difficult to solve by [[factoring_quadratic_expressions | factoring]] due to the fraction <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.
3.  **Move the constant term to the right side**:
    *   Add `4/5` to both sides: `x^2 - 3x = 4/5` <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a> <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.
4.  **Complete the square on the left side**:
    *   Take half of the coefficient of `x` (which is -3): `(-3) / 2 = -3/2` <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
    *   Square this value: `(-3/2)^2 = 9/4` <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a> <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
5.  **Add this term to both sides**:
    *   `x^2 - 3x + 9/4 = 4/5 + 9/4` <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>
6.  **Simplify the right side (find a common denominator)**:
    *   `4/5 = 16/20` <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>
    *   `9/4 = 45/20` <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>
    *   `16/20 + 45/20 = 61/20` <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>
    *   So, `x^2 - 3x + 9/4 = 61/20` <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.
7.  **Rewrite the left side as a perfect square**:
    *   `x^2 - 3x + 9/4` is `(x - 3/2)^2` <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.
    *   So, `(x - 3/2)^2 = 61/20` <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.
8.  **Solve for x**:
    *   Take the square root of both sides: `x - 3/2 = ±√(61/20)` <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
    *   Add `3/2` to both sides: `x = 3/2 ± √(61/20)` <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.

This provides the exact solutions, which are often irrational and difficult to find by [[solving_quadratic_equations_by_factoring | factoring]] <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. Using a calculator, the approximate values are `x ≈ 3.246` and `x ≈ -0.246` <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a> <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>.

The ability of [[completing_the_square_and_derivation_of_the_quadratic_formula | completing the square]] to solve any quadratic equation, regardless of complexity, highlights its importance and its [[relation_between_completing_the_square_and_the_quadratic_formula | relation between completing the square and the quadratic formula]] <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a> <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.