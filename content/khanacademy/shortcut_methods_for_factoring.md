---
title: Shortcut methods for factoring
videoId: 2ZzuZvz33X0
---

From: [[khanacademy]] <br/> 

When solving a [[factoring_quadratic_equations | quadratic equation]] that is explicitly equal to zero, such as `s^2 - 2s - 35 = 0`, a common method is to [[factoring_polynomials | factor]] the left-hand side [00:00:19]. While [[factoring_by_grouping | factoring by grouping]] is a valid approach, there is also a shortcut, especially when the leading coefficient of the quadratic expression is 1 [00:03:38], [00:04:40].

## When to Use the Shortcut

This shortcut is applicable when the quadratic expression has a leading coefficient of 1 [00:04:40], [00:05:19], [00:05:22]. In such cases, a "two-step factoring" process like [[factoring_by_grouping | factoring by grouping]] can be bypassed [00:04:47].

## Derivation of the Shortcut

Consider the product of two binomials in the form `(x + a)` and `(x + b)` [00:04:50]:
`x + a` multiplied by `x + b` is equal to:
* `x * x = x^2` <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>
* `x * b = bx` <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>
* `a * x = ax` <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>
* `a * b = ab` <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>

Combining these terms yields:
`x^2 + bx + ax + ab` <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>
This simplifies to:
`x^2 + (a + b)x + ab` <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>

This expansion reveals a pattern:
* The coefficient of the middle term (`x`) is the sum of `a` and `b` (`a + b`) [00:05:13].
* The constant term is the product of `a` and `b` (`ab`) [00:05:17].

This pattern aligns with [[factoring_quadratic_polynomials | quadratic polynomials]] where the leading coefficient is 1 [00:05:17], [00:05:19].

## Applying the Shortcut

To apply the shortcut, identify two numbers whose sum equals the coefficient of the middle term and whose product equals the constant term [00:00:44], [00:00:49], [00:05:27], [00:05:33].

### Example: Solving `s^2 - 2s - 35 = 0`

1.  **Identify desired sum and product:** For the equation `s^2 - 2s - 35 = 0`, we need two numbers (`a` and `b`) such that:
    *   `a + b = -2` <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>, <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>
    *   `a * b = -35` <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>, <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>

2.  **Find the numbers:** Since the product is negative, one number must be positive and the other negative [00:00:59], [00:01:02]. Considering pairs of factors of 35 that are 2 apart, 5 and -7 fit the criteria [00:01:05]:
    *   `5 + (-7) = -2` <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
    *   `5 * (-7) = -35` <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>

3.  **Directly factor:** Once these numbers are found, the expression can be directly factored into the product of two binomials using these numbers [00:05:38]:
    `(s + 5)(s - 7) = 0` <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>, <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>

4.  **Solve for s:** If the product of two numbers is zero, at least one of them must be zero [00:03:02], [00:03:13]:
    *   `s + 5 = 0` implies `s = -5` <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>, <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>
    *   `s - 7 = 0` implies `s = 7` <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>, <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>

Thus, the solutions for `s` are -5 or 7 [00:04:19]. Both [[factoring_by_grouping | factoring by grouping]] and this shortcut method are appropriate for solving such equations [00:06:14], [00:06:19].