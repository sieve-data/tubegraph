---
title: Solving quadratic equations
videoId: 2ZzuZvz33X0
---

From: [[khanacademy]] <br/> 

When tasked with [[solving_techniques_for_quadratic_equations | solving]] a quadratic equation, such as `s^2 - 2s - 35 = 0` <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>, the most effective [[methods_for_solving_quadratic_equations | method]], especially when the equation is explicitly set to zero, is to [[factoring_quadratic_equations | factor]] the non-zero side <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This approach leverages the property that if the product of two numbers is zero, at least one of them must be zero <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

## Factoring by Grouping

One common [[factoring_quadratics | factoring]] technique is **factoring by grouping** <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This method is particularly useful when the leading coefficient (the coefficient of the `s^2` term) is 1, as is the case in `s^2 - 2s - 35 = 0` <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

### Steps for Factoring by Grouping

1.  **Identify two numbers** <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>:
    *   Find two numbers (let's call them `a` and `b`) whose sum (`a + b`) equals the coefficient of the middle term (`-2`) <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a> <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
    *   Their product (`a * b`) must equal the constant term (`-35`) <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a> <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
    *   If the product is negative, one number must be positive and the other negative <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
    *   For `s^2 - 2s - 35 = 0`, the numbers are `5` and `-7` <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
        *   `5 + (-7) = -2` <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
        *   `5 * (-7) = -35` <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>

2.  **Split the middle term**: Rewrite the quadratic equation by splitting the middle term (`-2s`) using the identified numbers <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
    *   `s^2 - 2s - 35 = 0` becomes `s^2 + 5s - 7s - 35 = 0` <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a> <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

3.  **Group and factor**:
    *   Group the first two terms and factor out their common factor: `(s^2 + 5s)` becomes `s(s + 5)` <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a> <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
    *   Group the last two terms and factor out their common factor: `(-7s - 35)` becomes `-7(s + 5)` <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a> <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
    *   The equation now is `s(s + 5) - 7(s + 5) = 0` <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

4.  **Factor out the common binomial**: Notice that `(s + 5)` is a common factor in both terms <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. Factor it out:
    *   `(s + 5)(s - 7) = 0` <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

### Solving the Factored Equation

Once factored, the equation `(s + 5)(s - 7) = 0` represents the product of two numbers equal to zero <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. This means at least one of the factors must be zero <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

Set each factor equal to zero and solve for `s`:
1.  `s + 5 = 0`
    *   Subtract 5 from both sides: `s = -5` <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a> <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
2.  `s - 7 = 0`
    *   Add 7 to both sides: `s = 7` <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a> <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

Therefore, the solutions for `s` are `-5` and `7` <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

### Verification

You can verify the solutions by plugging them back into the original equation:
*   For `s = -5`: `(-5)^2 - 2(-5) - 35 = 25 + 10 - 35 = 0` <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   For `s = 7`: `(7)^2 - 2(7) - 35 = 49 - 14 - 35 = 0` <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

Both solutions satisfy the equation <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

## Shortcut for Factoring Quadratics with a Leading Coefficient of 1

When the [[understanding_components_of_a_quadratic_equation | quadratic equation]] is in the form `x^2 + Bx + C = 0` (where `B` is `a+b` and `C` is `ab`) <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>, and the leading coefficient is 1 <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>, you can directly factor it into `(x + a)(x + b) = 0` once `a` and `b` are identified <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.

In our example, once we found `5` and `-7` as the two numbers that sum to `-2` and multiply to `-35` <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>, we could have immediately written the factored form as `(s + 5)(s - 7) = 0` <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. This provides a shortcut compared to the full factoring by grouping process <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.