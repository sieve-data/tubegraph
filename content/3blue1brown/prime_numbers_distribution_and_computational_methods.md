---
title: Prime numbers distribution and computational methods
videoId: 4PDoT7jtxmw
---

From: [[3blue1brown]] <br/> 

The [[distribution_of_prime_numbers | distribution of prime numbers]] becomes sparser as numbers get larger. This is because larger numbers have more potential factors they could be divided by <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. For instance, to determine if a number like 143 is prime, one only needs to check factors up to its square root <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. However, for a number around a trillion, checking for primality involves considering on the order of a million potential prime factors <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

## Estimating Prime Density at High Values

When considering a range of numbers like those between one trillion (10^12) and one trillion plus one thousand, a significant amount of number crunching is required to identify the [[prime_numbers_and_their_regularities | prime numbers]] within it <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. For example, a simple Python program, though not the most efficient, can perform this task <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

In a range of 1000 integers starting at one trillion, there are approximately 37 [[prime_numbers_and_their_regularities | prime numbers]] <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. This yields a proportion of about 0.037, or roughly one prime for every 27 numbers <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

Mathematicians can quickly estimate this proportion without extensive computation. The density of [[prime_numbers_and_their_regularities | prime numbers]] near a given value, such as a trillion, is approximately related to the [[density_of_prime_numbers_and_natural_log | natural logarithm]] of that value <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. The natural logarithm of one trillion (ln(10^12)) is approximately 27 <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>, which aligns closely with the observed proportion of 1 in 27 <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. This connection between the [[density_of_prime_numbers_and_natural_log | natural logarithm]] (base *e*) and [[prime_numbers_and_their_regularities | prime numbers]] is considered a fascinating mathematical fact <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

## Relation between Pi and Prime Numbers

There are surprising connections between [[relation_between_pi_and_prime_numbers | pi and prime numbers]] through infinite series manipulations:

*   **Basel Problem:** The sum of the reciprocals of all natural numbers squared (1/1² + 1/2² + 1/3² + ...) converges to pi squared divided by 6 (π²/6) <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
*   **Prime-Filtered Series (Sum of Squares):** If a "weird game" is played with the sum of reciprocals of squares, where only terms corresponding to prime numbers or powers of primes are kept, and terms corresponding to prime powers are scaled down by their exponent (e.g., 1/4² scaled by 1/2, 1/8² scaled by 1/3), the resulting sum equals the [[density_of_prime_numbers_and_natural_log | natural logarithm]] of π²/6 <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. Non-prime, non-prime-power terms are excluded (e.g., 6, 10) <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
*   **Leibniz Formula for Pi:** The alternating sum of reciprocals of odd numbers (1 - 1/3 + 1/5 - 1/7 + ...) converges to pi divided by 4 (π/4) <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
*   **Prime-Filtered Series (Alternating Odd Numbers):** Applying a similar "prime game" to the Leibniz formula (keeping primes and scaling down prime powers while maintaining the alternating signs), the sum evaluates to the [[density_of_prime_numbers_and_natural_log | natural logarithm]] of π/4 <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

These relationships indicate that when *e* is raised to the power of these prime-filtered sums, the result is something directly related to [[relation_between_pi_and_prime_numbers | pi]] <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.

## Natural Logarithm and Divergent Series

The harmonic series (1 + 1/2 + 1/3 + 1/4 + ...) is a divergent series, meaning its sum eventually exceeds any chosen number, no matter how large <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>. This can be demonstrated by grouping terms; for instance, grouping terms in powers of two (1/3 + 1/4, 1/5 + ... + 1/8, etc.), each group sums to a value greater than or equal to 1/2 <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>.

The sum of the first *n* terms of the harmonic series is approximately equal to the [[density_of_prime_numbers_and_natural_log | natural logarithm]] of *n* (ln(*n*)) <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>. To make the sum exceed one million, *n* would need to be approximately *e* raised to the power of one million (e^1,000,000), which is roughly 10^400,000 <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>.

The integral of 1/*x* from 1 to *n* is equal to ln(*n*) <a class="yt-timestamp" data-t="01:01:39">[01:01:39]</a>. Graphically, the sum of rectangles approximating the harmonic series (where each rectangle's upper-left corner touches the 1/*x* curve) is slightly larger than the area under the curve (the integral) <a class="yt-timestamp" data-t="00:58:13">[00:58:13]</a>. The constant difference between the harmonic sum and ln(*n*) as *n* approaches infinity is known as the Euler-Mascheroni constant (approximately 0.577) <a class="yt-timestamp" data-t="01:02:10">[01:02:10]</a>.

The alternating harmonic series (1 - 1/2 + 1/3 - 1/4 + ...) converges to the [[density_of_prime_numbers_and_natural_log | natural logarithm]] of 2 (ln(2)) <a class="yt-timestamp" data-t="01:03:03">[01:03:03]</a>. This can be shown by generalizing the series into a function f(*x*) = x - x²/2 + x³/3 - ... <a class="yt-timestamp" data-t="01:05:04">[01:05:04]</a>. The derivative of this function, f'(*x*) = 1 - x + x² - ..., is a geometric series that sums to 1/(1+x) <a class="yt-timestamp" data-t="01:05:35">[01:05:35]</a>. Integrating 1/(1+x) from 0 to 1 yields ln(1+x) evaluated from 0 to 1, which results in ln(2) - ln(1) = ln(2) <a class="yt-timestamp" data-t="01:09:46">[01:09:46]</a>.
