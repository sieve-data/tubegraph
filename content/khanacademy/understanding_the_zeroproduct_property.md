---
title: Understanding the zeroproduct property
videoId: 2ZzuZvz33X0
---

From: [[khanacademy]] <br/> 

The zero-product property is a fundamental concept in algebra, particularly useful when [[product_and_sum_relationships_in_factoring | factoring]] and solving equations that are set equal to zero <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>. It simplifies the process of finding solutions to equations like quadratic equations, which might otherwise seem complex <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

## Core Principle

The property states that if the product of two or more numbers is zero, then at least one of those numbers must be zero <a class="yt-timestamp" data-t="03:13:13">[03:13:13]</a>.

Consider two numbers, `a` and `b`. If `a` multiplied by `b` equals zero (`a * b = 0`), then it logically follows that either `a` must be zero, or `b` must be zero, or both must be zero <a class="yt-timestamp" data-t="03:02:02">[03:02:02]</a>. This is an essential [[properties_of_multiplication_with_zero_and_one | property of multiplication with zero]] <a class="yt-timestamp" data-t="02:55:55">[02:55:55]</a>.

## Application in Solving Equations

The zero-product property is most effectively applied after an algebraic expression has been factored into a product of binomials or other terms, and the entire expression is set equal to zero <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>.

### Example: Solving a Quadratic Equation

Let's consider the equation `s² - 2s - 35 = 0` <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. The best way to solve this is to [[product_and_sum_relationships_in_factoring | factor the left-hand side]] of the equation <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>.

1.  **Factoring by Grouping**: To factor `s² - 2s - 35`, we look for two numbers whose sum is -2 and whose product is -35 <a class="yt-timestamp" data-t="00:44:44">[00:44:44]</a>. These numbers are 5 and -7, because 5 + (-7) = -2 and 5 * (-7) = -35 <a class="yt-timestamp" data-t="01:08:08">[01:08:08]</a>.
    *   Rewrite the middle term: `s² + 5s - 7s - 35 = 0` <a class="yt-timestamp" data-t="01:23:23">[01:23:23]</a>.
    *   Group terms: `(s² + 5s) + (-7s - 35) = 0` <a class="yt-timestamp" data-t="01:45:45">[01:45:45]</a>.
    *   Factor out common terms from each group: `s(s + 5) - 7(s + 5) = 0` <a class="yt-timestamp" data-t="01:51:51">[01:51:51]</a>.
    *   Factor out the common binomial `(s + 5)`: `(s + 5)(s - 7) = 0` <a class="yt-timestamp" data-t="02:26:26">[02:26:26]</a>.

2.  **Applying the Zero-Product Property**: Now that the equation is in the form `(s + 5)(s - 7) = 0`, we can apply the zero-product property <a class="yt-timestamp" data-t="02:51:51">[02:51:51]</a>. This means that either `s + 5` must be equal to zero, or `s - 7` must be equal to zero (or both) <a class="yt-timestamp" data-t="03:22:22">[03:22:22]</a>.

    *   Set the first factor to zero:
        `s + 5 = 0` <a class="yt-timestamp" data-t="03:22:22">[03:22:22]</a>
        Subtract 5 from both sides using the rules of [[understanding_the_concept_of_equality_in_algebra | equality in algebra]] <a class="yt-timestamp" data-t="03:52:52">[03:52:52]</a>:
        `s = -5` <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>

    *   Set the second factor to zero:
        `s - 7 = 0` <a class="yt-timestamp" data-t="03:30:30">[03:30:30]</a>
        Add 7 to both sides <a class="yt-timestamp" data-t="04:07:07">[04:07:07]</a>:
        `s = 7` <a class="yt-timestamp" data-t="04:13:13">[04:13:13]</a>

### Solutions

The solutions to the equation `s² - 2s - 35 = 0` are `s = -5` or `s = 7` <a class="yt-timestamp" data-t="04:13:13">[04:13:13]</a>.

### Verification

These solutions can be verified by substituting them back into the original equation:
*   For `s = -5`: `(-5)² - 2(-5) - 35 = 25 + 10 - 35 = 0` <a class="yt-timestamp" data-t="04:22:22">[04:22:22]</a>.
*   For `s = 7`: `(7)² - 2(7) - 35 = 49 - 14 - 35 = 0` <a class="yt-timestamp" data-t="04:30:30">[04:30:30]</a>.
Both solutions satisfy the equation <a class="yt-timestamp" data-t="04:36:36">[04:36:36]</a>.

> [!TIP] Shortcut for Factoring
> When the leading coefficient of a quadratic equation (e.g., the coefficient of `s²`) is 1, you can directly factor it into binomials `(x + a)(x + b)` where `a + b` is the coefficient of the middle term and `a * b` is the constant term <a class="yt-timestamp" data-t="05:17:17">[05:17:17]</a>. In the example `s² - 2s - 35 = 0`, since 5 + (-7) = -2 and 5 * (-7) = -35, it could be directly factored as `(s + 5)(s - 7) = 0` <a class="yt-timestamp" data-t="05:54:54">[05:54:54]</a>.