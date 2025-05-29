---
title: Patterns and symmetry in binomial expansions
videoId: iPwrDWQ7hPc
---

From: [[khanacademy]] <br/> 

Expanding binomials to higher powers can quickly become a "painful" and time-consuming process <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. The [[introduction_to_the_binomial_theorem | binomial theorem]] provides a systematic way to perform these expansions and reveals interesting patterns and symmetries in the resulting terms <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

## Examples of Binomial Expansions

To illustrate the complexity and then the patterns, consider these lower-power expansions:

*   **(a + b)<sup>0</sup>**: Any non-zero base raised to the 0 power equals 1 <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.
*   **(a + b)<sup>1</sup>**: This simply equals a + b <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.
*   **(a + b)<sup>2</sup>**: This expands to a<sup>2</sup> + 2ab + b<sup>2</sup> <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. It is important to remember that (a + b)<sup>2</sup> is *not* a<sup>2</sup> + b<sup>2</sup> <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
*   **(a + b)<sup>3</sup>**: This expands to a<sup>3</sup> + 3a<sup>2</sup>b + 3ab<sup>2</sup> + b<sup>3</sup> <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

As the power increases, manual multiplication becomes incredibly painful <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. For instance, calculating (a + b)<sup>10</sup> or (a + b)<sup>20</sup> would take an extensive amount of time <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

## The Binomial Theorem

The [[introduction_to_the_binomial_theorem | binomial theorem]] provides a formula for expanding any binomial (a + b) to the n<sup>th</sup> power <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>:

$(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k$ <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>

Here, $\binom{n}{k}$ represents "n choose k," which is a concept from [[Binomial coefficients and combinatorics | combinatorics]] <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. It is calculated as:

$\binom{n}{k} = \frac{n!}{k!(n-k)!}$ <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>

## Expansion of (a + b)<sup>4</sup>

Applying the [[introduction_to_the_binomial_theorem | binomial theorem]] to [[application_of_the_binomial_theorem_to_a_plus_b_to_the_4th_power | (a + b)<sup>4</sup>]]:

$(a + b)^4 = \sum_{k=0}^{4} \binom{4}{k} a^{4-k} b^k$ <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>

This expands to:

*   When k = 0: $\binom{4}{0} a^{4-0} b^0 = 1 \cdot a^4 \cdot 1 = a^4$ <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>
*   When k = 1: $\binom{4}{1} a^{4-1} b^1 = 4 \cdot a^3 \cdot b = 4a^3b$ <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>
*   When k = 2: $\binom{4}{2} a^{4-2} b^2 = 6 \cdot a^2 \cdot b^2 = 6a^2b^2$ <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>
*   When k = 3: $\binom{4}{3} a^{4-3} b^3 = 4 \cdot a^1 \cdot b^3 = 4ab^3$ <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>
*   When k = 4: $\binom{4}{4} a^{4-4} b^4 = 1 \cdot a^0 \cdot b^4 = b^4$ <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>

Thus, (a + b)<sup>4</sup> = a<sup>4</sup> + 4a<sup>3</sup>b + 6a<sup>2</sup>b<sup>2</sup> + 4ab<sup>3</sup> + b<sup>4</sup> <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.

## Patterns and Symmetry

The expansion of (a + b)<sup>4</sup>, and binomial expansions in general, reveal distinct patterns and symmetries:

*   **Symmetry in Coefficients**: The coefficients of the terms are symmetrical <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>. For (a + b)<sup>4</sup>, the coefficients are 1, 4, 6, 4, 1. They increase to a middle term (or terms) and then decrease symmetrically <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.
*   **Pattern in Exponents**:
    *   The exponent of the first term ('a') starts at 'n' (the power of the binomial) and decreases by one in each subsequent term until it reaches 0 <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>. (e.g., a<sup>4</sup>, a<sup>3</sup>, a<sup>2</sup>, a<sup>1</sup>, a<sup>0</sup>).
    *   The exponent of the second term ('b') starts at 0 and increases by one in each subsequent term until it reaches 'n' <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>. (e.g., b<sup>0</sup>, b<sup>1</sup>, b<sup>2</sup>, b<sup>3</sup>, b<sup>4</sup>).
    *   The sum of the exponents in each term always equals 'n' <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. For example, in 4a<sup>3</sup>b, 3 + 1 = 4.

These patterns and symmetries are fundamental to understanding the [[binomial distribution | binomial distribution]] and other areas of mathematics.