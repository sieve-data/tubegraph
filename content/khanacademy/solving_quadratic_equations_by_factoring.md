---
title: Solving quadratic equations by factoring
videoId: 2ZzuZvz33X0
---

From: [[khanacademy]] <br/> 

When presented with a quadratic equation like `s² - 2s - 35 = 0` <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>, the most effective way to solve for the variable (in this case, 's'), especially when the equation is explicitly set to zero, is to [[factoring_in_algebra | factor]] the quadratic expression <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. This approach differs from [[solving_algebraic_equations | traditional algebraic means]] used for simpler equations <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Factoring by Grouping

This is a standard method for [[factoring_quadratic_expressions | factoring quadratic expressions]] <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

1.  **Identify Coefficients**: For a quadratic equation in the form `ax² + bx + c = 0`, identify 'b' and 'c'. In `s² - 2s - 35 = 0`, `b = -2` and `c = -35` <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.
2.  **Find Two Numbers**: Find two numbers (let's call them `a` and `b`) whose sum is equal to the middle coefficient (`-2`) and whose product is equal to the constant term (`-35`) <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
    *   `a + b = -2` <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>
    *   `a * b = -35` <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>
    *   Since the product is negative, one number must be positive and the other negative <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
    *   The numbers are `5` and `-7` because `5 + (-7) = -2` <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a> and `5 * (-7) = -35` <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
3.  **Split the Middle Term**: Rewrite the middle term (`-2s`) using the two numbers found: `5s - 7s` <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
    *   `s² + 5s - 7s - 35 = 0` <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>
4.  **Group Terms**: Group the first two terms and the last two terms <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
    *   `(s² + 5s) + (-7s - 35) = 0`
5.  **Factor Out Common Factors**: Factor out the greatest common factor from each group.
    *   From `(s² + 5s)`, factor out `s`: `s(s + 5)` <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
    *   From `(-7s - 35)`, factor out `-7` (note: [[using_negative_factors_in_quadratic_expressions | factoring out a negative number]] often helps align the binomials): `-7(s + 5)` <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
    *   This results in `s(s + 5) - 7(s + 5) = 0` <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
6.  **Factor Out the Common Binomial**: Notice that `(s + 5)` is a common factor in both terms <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. Factor it out.
    *   `(s + 5)(s - 7) = 0` <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>

## Applying the Zero Product Property

Once the quadratic equation is factored into the product of two binomials equal to zero, apply the Zero Product Property <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **Zero Product Property**: If the product of two or more numbers is zero, then at least one of those numbers must be zero <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

Therefore, for `(s + 5)(s - 7) = 0`:
*   Either `s + 5 = 0` <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>
*   Or `s - 7 = 0` <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>

## Solving for 's'

Solve each of the resulting linear equations:

1.  For `s + 5 = 0`:
    *   Subtract `5` from both sides <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
    *   `s = -5` <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>

2.  For `s - 7 = 0`:
    *   Add `7` to both sides <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
    *   `s = 7` <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>

Thus, the solutions for `s` are `-5` and `7` <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. These solutions can be verified by substituting them back into the original equation <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

## Shortcut Method for Leading Coefficient of 1

When the quadratic equation has a leading coefficient of `1` (i.e., `x² + bx + c = 0`), there is a [[shortcut_methods_for_factoring_quadratics | shortcut method]] for [[factoring_quadratics_with_a_leading_coefficient_of_1 | factoring quadratics with a leading coefficient of 1]] <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

Consider the product of two binomials: `(x + a)(x + b)`.
Expanding this gives:
`x * x = x²` <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>
`x * b = bx` <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>
`a * x = ax` <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>
`a * b = ab` <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>

Combining like terms results in `x² + (a + b)x + ab` <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

This pattern directly corresponds to the form `s² - 2s - 35 = 0` <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. If you can find two numbers that sum to the middle coefficient (`-2`) and multiply to the constant term (`-35`), you can directly write the factored form.

As identified before, the numbers are `5` and `-7` <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   `5 + (-7) = -2` <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>
*   `5 * (-7) = -35` <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>

Therefore, the equation can be immediately factored as `(s + 5)(s - 7) = 0` <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. This [[comparisons_of_methods_completing_the_square_vs_factoring | shortcut]] leads directly to the same solutions as [[examples_of_solving_quadratic_equations_by_completing_the_square | factoring by grouping]] <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

> [!NOTE] While the [[shortcut_methods_for_factoring_quadratics | shortcut]] is efficient when the leading coefficient is 1, [[factoring_quadratic_expressions | factoring by grouping]] is a universally applicable method for [[factoring_quadratic_expressions | factoring quadratic expressions]] <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>, making it a robust technique in [[solving_quadratic_equations_using_the_quadratic_formula | solving quadratic equations]].