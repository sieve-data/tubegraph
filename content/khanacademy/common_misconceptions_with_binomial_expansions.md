---
title: Common misconceptions with binomial expansions
videoId: iPwrDWQ7hPc
---

From: [[khanacademy]] <br/> 

Expanding binomials to higher powers can quickly become challenging and lead to errors if not approached carefully <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Basic Binomial Expansions

*   **(a + b)<sup>0</sup>**: Any non-zero expression raised to the 0 power is equal to 1 <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.
*   **(a + b)<sup>1</sup>**: This simply equals a + b <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## The Common Misconception: (a + b)<sup>2</sup>

A frequent mistake when [[calculating_powers_of_binomials|calculating powers of binomials]] is assuming that (a + b)<sup>2</sup> is equal to a<sup>2</sup> + b<sup>2</sup> <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. This is incorrect <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

The correct way to expand (a + b)<sup>2</sup> involves multiplying the [[binomial_products|binomial product]] (a + b) by itself:
(a + b)<sup>2</sup> = (a + b) * (a + b) <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>

By applying distribution:
*   a * a = a<sup>2</sup> <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   a * b = ab <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>
*   b * a = ab <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>
*   b * b = b<sup>2</sup> <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>

Combining the like terms (ab + ab), the full expansion is:
(a + b)<sup>2</sup> = a<sup>2</sup> + 2ab + b<sup>2</sup> <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>

## Expanding to Higher Powers

Manually expanding binomials to higher powers, such as (a + b)<sup>3</sup> or (a + b)<sup>4</sup>, becomes progressively more "painful" and time-consuming <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

For example, to find (a + b)<sup>3</sup>:
(a + b)<sup>3</sup> = (a + b)<sup>2</sup> * (a + b) <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>
Substituting the expansion of (a + b)<sup>2</sup>:
(a<sup>2</sup> + 2ab + b<sup>2</sup>) * (a + b) <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>

This multiplication yields:
a<sup>3</sup> + 3a<sup>2</sup>b + 3ab<sup>2</sup> + b<sup>3</sup> <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>

Trying to calculate (a + b)<sup>10</sup> or (a + b)<sup>20</sup> manually would be incredibly painful and time-consuming <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. This is where the [[using_the_binomial_theorem_for_higher_powers|binomial theorem]] becomes a valuable tool <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

### The Binomial Theorem

The [[using_the_binomial_theorem_for_higher_powers|binomial theorem]] provides a formula for expanding (a + b)<sup>n</sup>:

> (a + b)<sup>n</sup> = Σ<sub>k=0</sub><sup>n</sup> (n choose k) * a<sup>(n-k)</sup> * b<sup>k</sup> <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>

Where (n choose k) is a [[combinatorics_and_factorials|combinatorial]] term defined as:
(n choose k) = n! / (k! * (n-k)!) <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>

Using the binomial theorem, the expansion for (a + b)<sup>4</sup> can be found much more efficiently than manual multiplication:
(a + b)<sup>4</sup> = 1a<sup>4</sup> + 4a<sup>3</sup>b + 6a<sup>2</sup>b<sup>2</sup> + 4ab<sup>3</sup> + 1b<sup>4</sup> <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>

The [[patterns_in_binomial_expansions|patterns in binomial expansions]] are evident in the coefficients (1, 4, 6, 4, 1, exhibiting [[symmetry_in_binomial_probabilities|symmetry]]) and the exponents (a's exponent decreases from n to 0, while b's exponent increases from 0 to n) <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.