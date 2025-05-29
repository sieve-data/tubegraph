---
title: Converting a quadratic equation into a perfect square
videoId: bNQY0z76M5A
---

From: [[khanacademy]] <br/> 

[[completing_the_square_as_a_technique_for_solving_quadratic_equations|Completing the square]] is a technique used to transform a quadratic equation into a perfect square, making it easier to solve <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. This method is universal, working for any quadratic equation <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>, and forms the basis for the [[introduction_to_the_quadratic_formula|quadratic formula]] <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. The [[completing_the_square_and_derivation_of_the_quadratic_formula|derivation of the quadratic formula]] itself can be achieved using [[completing_the_square_as_a_technique_for_solving_quadratic_equations|completing the square]] <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

The core idea behind [[completing_the_square_as_a_technique_for_solving_quadratic_equations|completing the square]] is to engineer a quadratic equation, by adding and subtracting terms from both sides, so that one side becomes a perfect square <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. This builds upon methods of [[solving_quadratic_equations_by_factoring|solving quadratics]] using perfect squares <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## How to Convert to a Perfect Square

To convert an expression like `x² + bx` into a perfect square, you need to add a specific number to it. This number is found by taking half of the coefficient of the `x` term (`b/2`) and then squaring it `(b/2)²` <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

For example, if you have `x² - 2ax + a²`, this is equivalent to `(x - a)²` <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. In this form, the coefficient of the `x` term is `-2a`, and the constant term is `a²`. Thus, `a` is half of `-2a` <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>, and `a²` is the square of `a` <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

Remember, whatever you add to one side of an equation, you must add to the other side to maintain equality <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

## Examples of Converting to a Perfect Square

### Example 1: Simple Case

Consider the quadratic equation:
`x² - 4x = 5` <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>

1.  **Identify the `b` term**: The coefficient of `x` is -4 <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
2.  **Calculate the constant to add**: Take half of -4, which is -2 <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. Then square it: `(-2)² = 4` <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
3.  **Add the constant to both sides**:
    `x² - 4x + 4 = 5 + 4` <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>
4.  **Rewrite the left side as a perfect square**: The left side, `x² - 4x + 4`, is equivalent to `(x - 2)²` <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
    ` (x - 2)² = 9` <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>
5.  **Solve for x**:
    *   Take the square root of both sides: `x - 2 = ±3` <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>
    *   Add 2 to both sides: `x = 2 ± 3` <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>
    *   This yields two solutions: `x = 5` (from 2+3) and `x = -1` (from 2-3) <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

Although this problem could also be solved by [[factoring_quadratic_expressions|factoring]] <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>, [[completing_the_square_as_a_technique_for_solving_quadratic_equations|completing the square]] provides a method that will always work, regardless of the coefficients <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.

### Example 2: More Complex Case with Leading Coefficient > 1

Consider the equation:
`10x² - 30x - 8 = 0` <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>

1.  **Simplify by dividing by a common factor (optional but recommended)**: Divide all terms by 2 <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
    `5x² - 15x - 4 = 0` <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>
2.  **Ensure a leading coefficient of 1**: Divide all terms by the leading coefficient, 5 <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
    `x² - 3x - 4/5 = 0` <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>
    This step often introduces fractions <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>, making [[factoring_quadratic_expressions|factoring]] very difficult <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.
3.  **Isolate the `x²` and `x` terms**: Add 4/5 to both sides <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.
    `x² - 3x = 4/5` <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>
4.  **Calculate the constant to add**: Take half of -3, which is -3/2 <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. Then square it: `(-3/2)² = 9/4` <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
5.  **Add the constant to both sides**:
    `x² - 3x + 9/4 = 4/5 + 9/4` <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>
6.  **Find a common denominator for the right side**: The common denominator for 5 and 4 is 20 <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
    *   `4/5 = 16/20` <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>
    *   `9/4 = 45/20` <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>
    *   Right side sum: `16/20 + 45/20 = 61/20` <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>
7.  **Rewrite the left side as a perfect square**: The left side, `x² - 3x + 9/4`, is equivalent to `(x - 3/2)²` <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
    ` (x - 3/2)² = 61/20` <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>
8.  **Solve for x**:
    *   Take the square root of both sides: `x - 3/2 = ±√(61/20)` <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>
    *   Add 3/2 to both sides: `x = 3/2 ± √(61/20)` <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>
    *   This provides the exact solutions, which would be extremely difficult to find by [[factoring_quadratic_expressions|factoring]] <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>. Approximate decimal values can be found using a calculator <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.

[[completing_the_square_as_a_technique_for_solving_quadratic_equations|Completing the square]] is a powerful and reliable method for [[solving_quadratic_equations_using_the_quadratic_formula|solving any quadratic equation]] <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>. It provides the foundation for understanding and deriving the [[introduction_to_the_quadratic_formula|quadratic formula]] <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.