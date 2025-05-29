---
title: Examples of solving quadratic equations by completing the square
videoId: bNQY0z76M5A
---

From: [[khanacademy]] <br/> 

[[completing_the_square_as_a_technique_for_solving_quadratic_equations | Completing the square]] is a technique used to solve any [[examples_and_applications_of_the_quadratic_formula | quadratic equation]] <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. It forms the basis for the [[relation_between_completing_the_square_and_the_quadratic_formula | quadratic formula]] itself <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>, which can be derived using this method <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. The core idea behind [[completing_the_square_as_a_technique_for_solving_quadratic_equations | completing the square]] is to transform a quadratic equation into a "perfect square" form, similar to methods used for [[solving_quadratic_equations_using_the_quadratic_formula | solving quadratics]] that are already perfect squares <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. This is achieved by adding and subtracting terms from both sides of the equation to "engineer" a perfect square <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

## Example 1: Simple Quadratic Equation

Let's solve the quadratic equation `x² - 4x = 5` <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. The goal is to make the left-hand side a perfect square <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

1.  **Identify the target form**: A perfect square binomial like `(x - a)²` expands to `x² - 2ax + a²` <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. We want `x² - 4x + ?` to equal `(x - a)²` <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
2.  **Determine the constant to add**: Comparing `x² - 4x` to `x² - 2ax`, we see that `-2a` must equal `-4` <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. This means `a = 2` <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. Therefore, the term needed to [[converting_a_quadratic_equation_into_a_perfect_square | complete the square]] is `a²`, which is `(-2)² = 4` <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. This can be found by taking half of the coefficient of the x-term (`-4`), which is `-2`, and then squaring it to get `4` <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
3.  **Add the constant to both sides**: Since we added `4` to the left side, we must also add `4` to the right side to maintain equality <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
    `x² - 4x + 4 = 5 + 4` <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>
    `x² - 4x + 4 = 9` <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>
4.  **Rewrite the left side as a perfect square**: The left side is now `(x - 2)²` <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
    `(x - 2)² = 9` <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>
5.  **Solve by taking the square root**:
    `x - 2 = ±√9` <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>
    `x - 2 = ±3` <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>
6.  **Isolate x**: Add `2` to both sides.
    `x = 2 ± 3` <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>
    This yields two solutions:
    *   `x = 2 + 3 = 5` <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>
    *   `x = 2 - 3 = -1` <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>

### Comparison with Factoring

For this particular equation, [[solving_quadratic_equations_by_factoring | factoring]] would have been faster <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. By moving all terms to one side, `x² - 4x - 5 = 0` <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>, it can be factored into `(x - 5)(x + 1) = 0` <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>, giving `x = 5` or `x = -1` <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. However, [[completing_the_square_as_a_technique_for_solving_quadratic_equations | completing the square]] always works, regardless of the coefficients or complexity of the problem <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

## Example 2: More Complex Quadratic Equation

Let's solve `10x² - 30x - 8 = 0` <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

1.  **Simplify the equation**: Divide the entire equation by a common factor to reduce coefficients. Dividing by `2` gives `5x² - 15x - 4 = 0` <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
2.  **Make the leading coefficient 1**: For [[completing_the_square_as_a_technique_for_solving_quadratic_equations | completing the square]], it's easiest when the `x²` term has a coefficient of `1` <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>. Divide the entire equation by `5`:
    `x² - 3x - 4/5 = 0` <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>
    > [!NOTE]
    > This step often introduces fractions, making [[factoring_quadratic_expressions | factoring]] very difficult <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.

3.  **Move the constant term to the right side**: Add `4/5` to both sides:
    `x² - 3x = 4/5` <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>
4.  **Determine the constant to add**: Take half of the x-term coefficient (`-3`), which is `-3/2` <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. Square this value: `(-3/2)² = 9/4` <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
5.  **Add the constant to both sides**: Add `9/4` to both sides of the equation.
    `x² - 3x + 9/4 = 4/5 + 9/4` <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>
6.  **Combine terms on the right side**: Find a common denominator for `4/5` and `9/4`, which is `20` <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.
    `4/5 = 16/20` <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>
    `9/4 = 45/20` <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>
    `x² - 3x + 9/4 = 16/20 + 45/20` <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>
    `x² - 3x + 9/4 = 61/20` <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>
7.  **Rewrite the left side as a perfect square**: The left side is `(x - 3/2)²` <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
    `(x - 3/2)² = 61/20` <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>
8.  **Solve by taking the square root**:
    `x - 3/2 = ±√(61/20)` <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>
9.  **Isolate x**: Add `3/2` to both sides.
    `x = 3/2 ± √(61/20)` <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>

The solutions involve a radical, making it clear that [[factoring_quadratic_expressions | factoring]] would not have been a straightforward method for this problem <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. Approximate values can be found using a calculator:
*   `x ≈ 3.246` (for `3/2 + √(61/20)`) <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>
*   `x ≈ -0.246` (for `3/2 - √(61/20)`) <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>

These examples illustrate that [[completing_the_square_as_a_technique_for_solving_quadratic_equations | completing the square]] is a universally applicable method for [[solving_quadratic_equations_using_the_quadratic_formula | solving quadratic equations]] <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>, and it serves as the foundation for the [[completing_the_square_and_derivation_of_the_quadratic_formula | quadratic formula]] itself <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>.