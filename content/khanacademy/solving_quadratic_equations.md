---
title: Solving quadratic equations
videoId: 2ZzuZvz33X0
---

From: [[khanacademy]] <br/> 

To solve for a variable in a [[quadratic_equations | quadratic equation]], such as `s^2 - 2s - 35 = 0` <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>, especially when it's explicitly set to zero, the most effective method is often to [[factoring_quadratic_equations | factor]] the expression on the left-hand side <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. Once factored into binomials, the principle that their product must equal zero can be applied <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## Factoring by Grouping

One standard method for [[factoring_quadratic_polynomials | factoring a quadratic expression]] is by grouping <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

1.  **Find Two Numbers**: Identify two numbers, `a` and `b`, such that their sum (`a + b`) is equal to the coefficient of the middle term, and their product (`a * b`) is equal to the constant term <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
    *   For `s^2 - 2s - 35 = 0`:
        *   The sum `a + b` must be -2 <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
        *   The product `a * b` must be -35 <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
    *   Since the product is negative, one number must be positive and the other negative <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
    *   The numbers 5 and -7 satisfy these conditions: 5 + (-7) = -2, and 5 * (-7) = -35 <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

2.  **Split the Middle Term**: Rewrite the middle term of the quadratic equation using the two numbers found <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
    *   `s^2 - 2s - 35 = 0` becomes `s^2 + 5s - 7s - 35 = 0` <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

3.  **Group and Factor**: Group the first two terms and the last two terms, then factor out the greatest common factor from each group <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
    *   Group 1: `s^2 + 5s` - common factor is `s` <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
        *   `s(s + 5)` <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>
    *   Group 2: `-7s - 35` - common factor is -7 <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
        *   `-7(s + 5)` <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>
    *   Combine: `s(s + 5) - 7(s + 5) = 0` <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

4.  **Factor Out the Common Binomial**: Notice that `(s + 5)` is a common factor in both terms. Factor it out <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
    *   `(s + 5)(s - 7) = 0` <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>

## Zero Product Property

Once the quadratic equation is factored into two binomials, the Zero Product Property can be applied <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. This property states that if the product of two numbers is zero, then at least one of those numbers must be zero <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

1.  **Set Each Factor to Zero**: Since `(s + 5)(s - 7) = 0`, either `s + 5 = 0` or `s - 7 = 0` (or both) <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

2.  **[[Solving simple linear equations | Solve]] for the Variable**: [[solving_equations_with_variables | Solve]] each resulting [[solving_simple_linear_equations | linear equation]]:
    *   For `s + 5 = 0`: Subtract 5 from both sides to get `s = -5` <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
    *   For `s - 7 = 0`: Add 7 to both sides to get `s = 7` <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

Thus, the solutions for `s` are -5 and 7 <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. These solutions can be verified by substituting them back into the original equation <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

## Shortcut for Specific Quadratics

When the leading coefficient of a quadratic expression (the coefficient of the `s^2` term) is 1, a shortcut for [[factoring_quadratic_equations | factoring]] can be used <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. If `x^2 + (a + b)x + ab` is the form, it can be directly factored into `(x + a)(x + b)` <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

This means that once the two numbers (`a` and `b`) are found whose sum is the middle coefficient and product is the constant term, the quadratic can be immediately written in factored form <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
*   For `s^2 - 2s - 35 = 0`, with `a = 5` and `b = -7`, it can be directly factored as `(s + 5)(s - 7) = 0` <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

Both [[factoring_quadratic_equations | factoring by grouping]] and this shortcut are appropriate ways to [[solving_difficult_quadratic_equations | solve quadratic equations]] <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.