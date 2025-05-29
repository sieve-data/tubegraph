---
title: Understanding binomials and their products
videoId: 2ZzuZvz33X0
---

From: [[khanacademy]] <br/> 

When solving a [[factoring_quadratic_polynomials | quadratic equation]] such as s² - 2s - 35 = 0 <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>, a common and effective approach, especially when the equation is explicitly set to zero, is to [[factoring_polynomials | factor]] the left-hand side <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. This method relies on the principle that if the product of two [[introduction_to_the_binomial_theorem | binomials]] equals zero, then at least one of those [[introduction_to_the_binomial_theorem | binomials]] must be zero <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

## Factoring by Grouping

One standard method for [[factoring_polynomials | factoring]] a [[factoring_quadratic_polynomials | quadratic equation]] is by [[factoring_polynomials | grouping]] <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. This involves finding two numbers whose sum equals the coefficient of the middle term (the 's' term) and whose product equals the constant term <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

For the equation s² - 2s - 35 = 0 <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>:
*   We need two numbers (let's call them *a* and *b*) such that *a* + *b* = -2 <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
*   And *a* × *b* = -35 <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

Since the product is a negative number, one number must be positive and the other negative <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. The numbers 5 and -7 satisfy these conditions:
*   5 + (-7) = -2 <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
*   5 × (-7) = -35 <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>

Once these numbers are found, the middle term of the [[factoring_quadratic_polynomials | quadratic equation]] is split using these numbers <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>:
s² + 5s - 7s - 35 = 0 <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>

Then, the terms are [[factoring_polynomials | grouped]]:
1.  Group the first two terms: s² + 5s <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>
    [[factoring_polynomials | Factor]] out the common term, `s`: s(s + 5) <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>
2.  Group the last two terms: -7s - 35 <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>
    [[factoring_polynomials | Factor]] out the common term, `-7`: -7(s + 5) <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>

Combining these results:
s(s + 5) - 7(s + 5) = 0 <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>

Notice that `(s + 5)` is a common factor in both terms. [[factoring_polynomials | Factor]] it out:
(s + 5)(s - 7) = 0 <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>

## The Zero Product Property

The product of two numbers (or [[introduction_to_the_binomial_theorem | binomials]]) is zero if and only if at least one of the numbers is zero <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
Given (s + 5)(s - 7) = 0 <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>, this means:
*   s + 5 = 0 OR <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>
*   s - 7 = 0 <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>

Solving these simple linear equations:
*   s + 5 = 0 ⇒ s = -5 <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>
*   s - 7 = 0 ⇒ s = 7 <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>

Thus, the solutions for *s* are -5 and 7 <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

## Shortcut for Factoring Binomial Products

When a [[factoring_quadratic_polynomials | quadratic equation]] has a leading coefficient of 1 (i.e., the coefficient of the s² term is 1), there's a direct shortcut <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

Consider the product of two [[expanding_binomials_using_the_binomial_theorem | binomials]]: (x + a)(x + b) <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
[[expanding_binomials_using_the_binomial_theorem | Expanding]] this product gives:
x * x = x² <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>
x * b = bx <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>
a * x = ax <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>
a * b = ab <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>

Combining these terms:
x² + bx + ax + ab = x² + (a + b)x + ab <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>

This pattern shows that when a [[factoring_quadratic_polynomials | quadratic equation]] (with a leading coefficient of 1) is factored into the product of two [[expanding_binomials_using_the_binomial_theorem | binomials]], the constant term of the quadratic (ab) is the product of the two numbers (a and b), and the coefficient of the middle term (a + b) is the sum of the two numbers <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

In the example s² - 2s - 35 = 0 <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>, once the numbers 5 and -7 were identified (sum to -2, product to -35) <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>, the equation could be immediately [[factoring_polynomials | factored]] as (s + 5)(s - 7) = 0 <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. While [[factoring_polynomials | factoring by grouping]] is a valid method, this shortcut provides a quicker way to reach the factored form.