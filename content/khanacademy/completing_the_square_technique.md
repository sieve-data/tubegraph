---
title: Completing the square technique
videoId: bNQY0z76M5A
---

From: [[khanacademy]] <br/> 

[[completing_the_square | Completing the square]] is an algebraic technique used primarily to [[solving_quadratic_equations | solve quadratic equations]] <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. This method is universal, meaning it works for any [[understanding_quadratic_expressions | quadratic equation]], and it forms the fundamental basis for the [[quadratic_formula_introduction | quadratic formula]] <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. It can be used to [[using_completing_the_square_to_derive_the_quadratic_formula | derive the quadratic formula]] itself <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

The technique builds on the concept of [[perfect_squares_in_algebra | perfect squares]] previously used in [[solving_quadratic_equations | solving quadratics]] <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. The core idea is to manipulate a [[understanding_quadratic_expressions | quadratic equation]] so that one side becomes a [[perfect_squares_in_algebra | perfect square]] <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. This is achieved by adding and subtracting specific values from both sides of the equation <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

## How to Complete the Square

The process involves transforming the standard form of a quadratic expression (`ax^2 + bx + c`) into a [[perfect_squares_in_algebra | perfect square]] trinomial, typically `(x + h)^2` or `(x - h)^2`.

### Example 1: Simple Case

Consider the [[understanding_quadratic_expressions | quadratic equation]]:
`x^2 - 4x = 5` <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>

1.  **Identify the goal**: The aim is to make the left-hand side (`x^2 - 4x`) a [[perfect_squares_in_algebra | perfect square]] <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. A [[perfect_squares_in_algebra | perfect square]] trinomial in the form `x^2 - 2ax + a^2` can be factored as `(x - a)^2` <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
2.  **Find the constant term**:
    *   Compare `x^2 - 4x` to `x^2 - 2ax`. This means `-4x` must be equal to `-2ax` <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
    *   Divide the coefficient of the `x` term (`-4`) by 2 to find `a`: `-4 / 2 = -2` <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. So, `a = -2` <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
    *   Square this value of `a` to find the constant term needed: `(-2)^2 = 4` <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
    *   *Rule of thumb*: Take half of the `x` coefficient and then square it <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
3.  **Add the constant to both sides**: Add `4` to both sides of the equation to maintain equality <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
    `x^2 - 4x + 4 = 5 + 4` <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>
    `x^2 - 4x + 4 = 9` <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>
4.  **Rewrite the left side as a perfect square**: The left side is now `(x - 2)^2` <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
    `(x - 2)^2 = 9` <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>
5.  **Solve by taking the square root**:
    `x - 2 = ±√9` <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>
    `x - 2 = ±3` <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>
6.  **Isolate x**:
    `x = 2 ± 3` <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>
    This yields two solutions:
    *   `x = 2 + 3 = 5` <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>
    *   `x = 2 - 3 = -1` <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>

While this problem could also be solved by [[factoring_quadratic_equations | factoring]] <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>, [[completing_the_square | completing the square]] is a method that will always work, regardless of the coefficients <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.

### Example 2: More Complex Case (with fractions)

Consider the equation:
`10x^2 - 30x - 8 = 0` <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>

1.  **Ensure the leading coefficient is 1**:
    *   First, simplify by dividing by the greatest common factor, if any (e.g., divide by 2):
        `5x^2 - 15x - 4 = 0` <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>
    *   Then, divide the entire equation by the leading coefficient (e.g., 5) to make the `x^2` term have a coefficient of 1 <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>:
        `x^2 - 3x - 4/5 = 0` <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>
    *   This equation is difficult to [[factoring_quadratic_equations | factor]] due to the fraction <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.
2.  **Move the constant term to the right side**:
    `x^2 - 3x = 4/5` <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>
3.  **Find the constant term to complete the square**:
    *   Take half of the `x` coefficient (`-3`): `-3 / 2 = -3/2` <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
    *   Square this value: `(-3/2)^2 = 9/4` <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
4.  **Add the constant to both sides**:
    `x^2 - 3x + 9/4 = 4/5 + 9/4` <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>
5.  **Simplify the right side**: Find a common denominator (20) for `4/5` and `9/4` <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.
    `4/5 = 16/20` <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>
    `9/4 = 45/20` <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>
    `x^2 - 3x + 9/4 = 16/20 + 45/20` <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>
    `x^2 - 3x + 9/4 = 61/20` <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>
6.  **Rewrite the left side as a perfect square**:
    `(x - 3/2)^2 = 61/20` <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>
7.  **Solve by taking the square root**:
    `x - 3/2 = ±√(61/20)` <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>
8.  **Isolate x**:
    `x = 3/2 ± √(61/20)` <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>

The solutions in decimal form are approximately:
*   `x ≈ 3.246` <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>
*   `x ≈ -0.246` <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>

Completing the square is a robust method for [[solving_quadratic_equations | solving any quadratic equation]], particularly useful when [[factoring_quadratic_equations | factoring]] is not straightforward or impossible with integers/simple fractions <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.