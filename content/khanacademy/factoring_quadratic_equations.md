---
title: Factoring quadratic equations
videoId: 2ZzuZvz33X0
---

From: [[khanacademy]] <br/> 

[[factoring_quadratics | Factoring quadratic equations]] is a common method used to [[solving_quadratic_equations | solve for the variable]] in a [[quadratic_polynomials | quadratic equation]], especially when the equation is set equal to zero <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. This method is considered a best way to [[solving_techniques_for_quadratic_equations | solve this type of equation]] <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Understanding a Quadratic Equation
A quadratic equation typically takes the form of a [[quadratic_polynomials | quadratic polynomial]] set to zero <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. For example, `s² - 2s - 35 = 0` is a quadratic equation where `s` is the variable <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. When [[understanding_components_of_a_quadratic_equation | understanding components of a quadratic equation]] in this form, the goal is to find the values of the variable `s` that satisfy the equation <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## [[methods_for_solving_quadratic_equations | Methods for Solving Quadratic Equations]]: Factoring by Grouping
One standard way to factor a quadratic equation is by [[factoring_by_grouping | factoring by grouping]] <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This method is particularly useful when the leading coefficient (the coefficient of the squared term) is not 1.

### Steps for Factoring by Grouping

1.  **Identify Key Numbers**: For a quadratic equation in the form `ax² + bx + c = 0`, you need to find two numbers whose sum is equal to the middle coefficient (`b`) and whose product is equal to the constant term (`c`) <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
    *   *Example*: For `s² - 2s - 35 = 0`, we need two numbers that sum to -2 and multiply to -35 <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. Since the product is negative, one number must be positive and the other negative <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. The numbers 5 and -7 fit these criteria (5 + (-7) = -2 and 5 * (-7) = -35) <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

2.  **Split the Middle Term**: Rewrite the middle term (`bx`) using the two numbers found in the previous step <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
    *   *Example*: `s² - 2s - 35 = 0` becomes `s² + 5s - 7s - 35 = 0` <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

3.  **Group and Factor**: Group the first two terms and the last two terms, then factor out the greatest common factor from each group <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
    *   *Example*:
        *   Group 1: `s² + 5s`. Factor out `s`: `s(s + 5)` <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
        *   Group 2: `-7s - 35`. Factor out `-7`: `-7(s + 5)` <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
        *   The equation now is `s(s + 5) - 7(s + 5) = 0` <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

4.  **Factor the Common Binomial**: Notice that both terms now share a common binomial factor (e.g., `s + 5`). Factor this binomial out <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
    *   *Example*: `(s + 5)(s - 7) = 0` <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

## Applying the Zero Product Property
Once the quadratic equation is factored into the product of two binomials equal to zero, you can use the zero product property <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. This property states that if the product of two numbers (or expressions) is zero, then at least one of those numbers must be zero <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

*   *Example*: From `(s + 5)(s - 7) = 0`, either `s + 5 = 0` or `s - 7 = 0` (or both) <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
    *   Solving `s + 5 = 0` gives `s = -5` <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
    *   Solving `s - 7 = 0` gives `s = 7` <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
    *   Thus, the solutions for `s` are -5 and 7 <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

### Verification
You can verify the solutions by plugging them back into the original equation <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   If `s = -5`: `(-5)² - 2(-5) - 35 = 25 + 10 - 35 = 0` <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   If `s = 7`: `(7)² - 2(7) - 35 = 49 - 14 - 35 = 0` <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

## Shortcut for Leading Coefficient of 1
When a quadratic equation has a leading coefficient of 1 (e.g., `x² + bx + c = 0`), there's a shortcut for [[factoring_quadratics | factoring quadratics]] <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. If `(x + a)(x + b)` is expanded, it results in `x² + (a + b)x + ab` <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. This means if you can find two numbers `a` and `b` that add up to the middle coefficient and multiply to the constant term, you can directly factor the quadratic into `(x + a)(x + b)` <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

*   *Example*: For `s² - 2s - 35 = 0`, we found the numbers 5 and -7 <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
    *   5 + (-7) = -2 (middle coefficient) <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
    *   5 * (-7) = -35 (constant term) <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
    *   Therefore, the equation can be directly factored as `(s + 5)(s - 7) = 0` <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

While this shortcut exists, [[factoring_by_grouping | factoring by grouping]] remains a perfectly valid and appropriate method for [[solving_quadratic_equations | solving quadratic equations]] <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.