---
title: Introduction to binomials and calculating powers
videoId: iPwrDWQ7hPc
---

From: [[khanacademy]] <br/> 

A binomial is an algebraic expression consisting of two terms <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. Raising binomials to higher powers can quickly become a complex and time-consuming task <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>, <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

## Basic Binomial Expansions

Here are examples of binomial (a + b) raised to different powers:

*   **To the 0th Power:**
    Any non-zero expression raised to the 0 power equals 1 <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.
    (a + b)<sup>0</sup> = 1 <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>

*   **To the 1st Power:**
    (a + b)<sup>1</sup> = a + b <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>

*   **To the 2nd Power:**
    A common [[misconceptions_about_expanding_binomials | misconception about expanding binomials]] is to simply square each term (e.g., a<sup>2</sup> + b<sup>2</sup>), which is incorrect <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>, <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
    Instead, (a + b)<sup>2</sup> means (a + b) multiplied by (a + b) <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
    Using the distributive property:
    (a + b)(a + b) = a * a + a * b + b * a + b * b <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>
    = a<sup>2</sup> + ab + ab + b<sup>2</sup> <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
    = a<sup>2</sup> + 2ab + b<sup>2</sup> <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>

*   **To the 3rd Power:**
    To find (a + b)<sup>3</sup>, one can multiply (a + b)<sup>2</sup> by another (a + b) <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
    (a<sup>2</sup> + 2ab + b<sup>2</sup>)(a + b)
    Multiply each term by b:
    b * b<sup>2</sup> = b<sup>3</sup> <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>
    b * 2ab = 2ab<sup>2</sup> <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>
    b * a<sup>2</sup> = a<sup>2</sup>b <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>
    Multiply each term by a:
    a * b<sup>2</sup> = ab<sup>2</sup> <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>
    a * 2ab = 2a<sup>2</sup>b <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>
    a * a<sup>2</sup> = a<sup>3</sup> <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>
    Adding these terms together:
    a<sup>3</sup> + (a<sup>2</sup>b + 2a<sup>2</sup>b) + (2ab<sup>2</sup> + ab<sup>2</sup>) + b<sup>3</sup> <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>
    = a<sup>3</sup> + 3a<sup>2</sup>b + 3ab<sup>2</sup> + b<sup>3</sup> <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>, <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>

Calculating powers higher than 3, such as (a + b)<sup>10</sup> or (a + b)<sup>20</sup>, would be extremely tedious and time-consuming with this method <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>, <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. This is where the [[introduction_to_the_binomial_theorem | binomial theorem]] becomes useful <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

## The Binomial Theorem

The [[introduction_to_the_binomial_theorem | binomial theorem]] provides a formula for expanding any binomial (a + b) raised to the nth power <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>, <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>:

$\sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k$ <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>

### Binomial Coefficients (n choose k)

The notation $\binom{n}{k}$, pronounced "n choose k," comes from [[introduction_to_binomial_coefficients_and_combinatorics | combinatorics]] <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. It represents the number of ways to choose k items from a set of n distinct items. The formula for "n choose k" is <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>:

$\binom{n}{k} = \frac{n!}{k!(n-k)!}$ <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>

*   **n!** (n factorial) means n × (n-1) × ... × 1.
*   **0!** is defined as 1 for these calculations <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>, <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.

## Applying the Binomial Theorem: (a + b)<sup>4</sup>

Let's use the [[introduction_to_the_binomial_theorem | binomial theorem]] to expand (a + b)<sup>4</sup> <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. Here, n = 4 <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

The expansion will be the sum from k = 0 to 4 of $\binom{4}{k} a^{4-k} b^k$ <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>:

*   **k = 0:** $\binom{4}{0} a^{4-0} b^0$
    *   $\binom{4}{0} = \frac{4!}{0!(4-0)!} = \frac{4!}{1 \cdot 4!} = 1$ <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>, <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>
    *   Term: $1 \cdot a^4 \cdot 1 = a^4$ <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>, <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>

*   **k = 1:** $\binom{4}{1} a^{4-1} b^1$
    *   $\binom{4}{1} = \frac{4!}{1!(4-1)!} = \frac{4!}{1 \cdot 3!} = \frac{4 \cdot 3!}{1 \cdot 3!} = 4$ <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>, <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>
    *   Term: $4 a^3 b$ <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>, <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>

*   **k = 2:** $\binom{4}{2} a^{4-2} b^2$
    *   $\binom{4}{2} = \frac{4!}{2!(4-2)!} = \frac{4!}{2! \cdot 2!} = \frac{4 \cdot 3 \cdot 2 \cdot 1}{(2 \cdot 1)(2 \cdot 1)} = \frac{24}{4} = 6$ <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>, <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>
    *   Term: $6 a^2 b^2$ <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>, <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>

*   **k = 3:** $\binom{4}{3} a^{4-3} b^3$
    *   $\binom{4}{3} = \frac{4!}{3!(4-3)!} = \frac{4!}{3! \cdot 1!} = \frac{4 \cdot 3!}{3! \cdot 1} = 4$ <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>, <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>
    *   Term: $4 a b^3$ <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>, <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>

*   **k = 4:** $\binom{4}{4} a^{4-4} b^4$
    *   $\binom{4}{4} = \frac{4!}{4!(4-4)!} = \frac{4!}{4! \cdot 0!} = \frac{4!}{4! \cdot 1} = 1$ <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>, <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>
    *   Term: $1 \cdot a^0 \cdot b^4 = b^4$ <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>, <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>

Summing these terms gives the full expansion:
(a + b)<sup>4</sup> = a<sup>4</sup> + 4a<sup>3</sup>b + 6a<sup>2</sup>b<sup>2</sup> + 4ab<sup>3</sup> + b<sup>4</sup> <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>, <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>

### Patterns in Binomial Expansion

When expanding (a + b)<sup>n</sup>, several patterns emerge <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>:

*   **Coefficients:** The coefficients show [[understanding_binomial_distribution_and_symmetry_in_probability | symmetry]]. For (a + b)<sup>4</sup>, they are 1, 4, 6, 4, 1 <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.
*   **Powers of 'a':** The power of 'a' starts at 'n' and decreases by 1 in each subsequent term until it reaches 0 <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.
*   **Powers of 'b':** The power of 'b' starts at 0 (b<sup>0</sup> = 1) and increases by 1 in each subsequent term until it reaches 'n' <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
*   **Sum of Powers:** In each term, the sum of the exponents of 'a' and 'b' always equals 'n' (e.g., for a<sup>2</sup>b<sup>2</sup>, 2+2=4).