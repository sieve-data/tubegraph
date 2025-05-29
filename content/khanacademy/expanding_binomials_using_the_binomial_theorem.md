---
title: Expanding binomials using the binomial theorem
videoId: iPwrDWQ7hPc
---

From: [[khanacademy]] <br/> 

Expanding higher powers of binomials can become a challenging and time-consuming task if done manually <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## Initial Binomial Expansions

Let's observe how quickly the process becomes painful:

*   **` (a + b)^0 `**: Any non-zero base raised to the 0 power equals 1 <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.
    ` (a + b)^0 = 1 ` <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>
*   **` (a + b)^1 `**: This simply equals ` a + b ` <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.
*   **` (a + b)^2 `**: It is incorrect to assume this is ` a^2 + b^2 ` <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. Instead, it is ` (a + b) * (a + b) ` <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
    Applying multiplication:
    *   ` a * a = a^2 ` <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
    *   ` a * b = ab ` <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>
    *   ` b * a = ab ` <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>
    *   ` b * b = b^2 ` <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>
    Combining like terms, we get: ` a^2 + 2ab + b^2 ` <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. This concept is part of [[understanding_binomials_and_their_products | understanding binomials and their products]].
*   **` (a + b)^3 `**: This can be calculated by multiplying ` (a + b)^2 ` by another ` (a + b) ` <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
    Starting with ` a^2 + 2ab + b^2 ` and multiplying by ` a + b `:
    *   Multiply by `b`: ` b^3 + 2ab^2 + a^2b ` <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>
    *   Multiply by `a`: ` ab^2 + 2a^2b + a^3 ` <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>
    Adding these results yields: ` a^3 + 3a^2b + 3ab^2 + b^3 ` <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

Manually expanding to the third power already takes a reasonable amount of time <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>, making higher powers like the 10th or 20th incredibly painful <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. This is where the [[introduction_to_the_binomial_theorem | binomial theorem]] becomes useful <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

## The Binomial Theorem

The [[introduction_to_the_binomial_theorem | binomial theorem]] provides a formula for expanding ` (a + b)^n ` <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>:

` (a + b)^n = Σ (from k=0 to n) of (n choose k) * a^(n-k) * b^k ` <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>

### Binomial Coefficients (`n choose k`)

The term ` (n choose k) `, which comes from [[binomial_coefficients_and_combinatorics | combinatorics]], is calculated using factorials <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>:

` (n choose k) = n! / (k! * (n - k)!) ` <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>

By definition, ` 0! = 1 ` <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.

## Application of the Binomial Theorem: ` (a + b)^4 `

Let's apply the binomial theorem to expand ` (a + b)^4 ` <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. In this case, ` n = 4 ` <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

The expansion will be the sum from ` k = 0 ` to ` 4 ` of ` (4 choose k) * a^(4-k) * b^k ` <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.

Let's break down each term:

*   **k = 0**:
    *   Coefficient: ` (4 choose 0) = 4! / (0! * 4!) = 1 ` <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>
    *   Variables: ` a^(4-0) * b^0 = a^4 * 1 = a^4 ` <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>
    *   Term: ` 1a^4 ` <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>
*   **k = 1**:
    *   Coefficient: ` (4 choose 1) = 4! / (1! * 3!) = (4 * 3 * 2 * 1) / (1 * 3 * 2 * 1) = 4 ` <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>
    *   Variables: ` a^(4-1) * b^1 = a^3b ` <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>
    *   Term: ` 4a^3b ` <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>
*   **k = 2**:
    *   Coefficient: ` (4 choose 2) = 4! / (2! * 2!) = (4 * 3 * 2 * 1) / ((2 * 1) * (2 * 1)) = 6 ` <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>
    *   Variables: ` a^(4-2) * b^2 = a^2b^2 ` <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>
    *   Term: ` 6a^2b^2 ` <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>
*   **k = 3**:
    *   Coefficient: ` (4 choose 3) = 4! / (3! * 1!) = 4 ` <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>
    *   Variables: ` a^(4-3) * b^3 = ab^3 ` <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>
    *   Term: ` 4ab^3 ` <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>
*   **k = 4**:
    *   Coefficient: ` (4 choose 4) = 4! / (4! * 0!) = 1 ` <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>
    *   Variables: ` a^(4-4) * b^4 = a^0b^4 = b^4 ` <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>
    *   Term: ` 1b^4 ` <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>

Adding all these terms together gives the full expansion of ` (a + b)^4 ` <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>:

` (a + b)^4 = a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4 ` <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. This is an [[application_of_binomial_theorem_to_a_plus_b_to_the_4th_power | application of the binomial theorem to a plus b to the 4th power]].

## Patterns and Symmetry

The expansion of ` (a + b)^4 ` reveals clear [[patterns_and_symmetry_in_binomial_expansions | patterns and symmetry]] <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>:

*   **Coefficients**: The coefficients display symmetry, following a sequence of 1, 4, 6, 4, 1 <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   **Exponents of `a`**: The power of `a` starts at `n` (4 in this case) and decreases by one in each subsequent term: ` a^4, a^3, a^2, a^1, a^0 ` <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>.
*   **Exponents of `b`**: The power of `b` starts at `0` and increases by one in each subsequent term: ` b^0, b^1, b^2, b^3, b^4 ` <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
*   **Sum of Exponents**: For each term, the sum of the exponents of `a` and `b` always equals `n` (4 in this case) <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.