---
title: Relationship between natural logs and prime numbers
videoId: 4PDoT7jtxmw
---

From: [[3blue1brown]] <br/> 

A surprising connection exists between the seemingly unrelated concepts of [[Natural logarithms and exponential growth | natural logarithms]] and [[prime_numbers_and_their_regularities | prime numbers]]. This relationship becomes apparent when examining the density of primes and certain infinite series.

## Estimating Prime Density

Consider the numbers between one trillion (10^12) and one trillion plus a thousand <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. While performing a painstaking calculation would be difficult, a simple Python program can identify the primes within this range <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. It's observed that [[Prime numbers and density | prime numbers get sparser]] as they increase in value <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

For the range between 1 trillion and 1 trillion plus a thousand, there are 37 primes <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. This means the proportion of primes in this range is 0.037, or approximately 1 in 27 <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>, <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

Mathematicians can estimate this proportion quickly because the density of [[Prime numbers and density | prime numbers]] near a given value, like a trillion, is approximately the reciprocal of the [[Natural logarithms and exponential growth | natural logarithm]] of that number <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>, <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

The natural logarithm (ln) of a number 'X' answers the question "e to what power equals X?" <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. For example, ln(10) is approximately 2.3, meaning e^2.3 ≈ 10 <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>, <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

Calculating the natural logarithm of one trillion (10^12) yields approximately 27 <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>, <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. This aligns remarkably well with the observed density of 1 in 27, highlighting a profound [[Connection between zeta function and prime numbers | connection between natural logarithms and prime numbers]] <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>, <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

## Natural Logarithms and Series Involving Primes

The appearance of [[Natural logarithms and exponential growth | natural logarithms]] is not limited to prime density. They also arise in surprising manipulations of infinite series that involve [[Pi and its formulas involving primes | pi and primes]].

### Euler's Basel Problem and a "Prime Game"

Euler famously solved the Basel problem, showing that the sum of the reciprocals of all natural numbers squared (1/1^2 + 1/2^2 + 1/3^2 + ...) equals π^2/6 <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>, <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>, <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.

A peculiar "game" can be played with this series:
*   Exclude 1.
*   Keep terms corresponding to [[prime_numbers_and_their_regularities | prime numbers]] as they are (e.g., 1/2^2, 1/3^2, 1/5^2, 1/7^2...).
*   For terms that are powers of primes (e.g., 4=2^2, 8=2^3, 9=3^2), keep the term but scale it down by the inverse of its exponent (e.g., 1/4^2 scaled by 1/2, 1/8^2 scaled by 1/3, 1/9^2 scaled by 1/2) <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>, <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
*   Exclude all other composite numbers (e.g., 6, 10, 12, 14, 15) <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>, <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.

Despite its seemingly chaotic manipulation, this new series sums to the natural logarithm of the original result: ln(π^2/6) <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>, <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.

### Leibniz Formula for Pi and Primes

Another example is the Leibniz formula for π/4, an alternating series of the reciprocals of odd numbers: 1 - 1/3 + 1/5 - 1/7 + ... = π/4 <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>, <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>, <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

If the same "prime game" is applied to this series (excluding 1, keeping primes, scaling down prime powers, excluding other composites), the resulting sum is ln(π/4) <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>, <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. This suggests a deep and consistent relationship between natural logarithms and [[Prime numbers and their regularities | prime patterns]] <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

## Natural Logarithms and Series of Reciprocals

The [[Natural logarithms and exponential growth | natural logarithm]] also describes the behavior of harmonic series.

### The Diverging Harmonic Series

The sum of the reciprocals of all natural numbers (1 + 1/2 + 1/3 + 1/4 + ...) is known as the harmonic series <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>. Unlike the sum of squares, this series does not converge to a finite number; it *diverges* <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>, <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>. This can be proven by grouping terms, showing that the sum can always exceed any chosen number <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>, <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>.

The sum of the harmonic series up to 'n' terms (S_n) is approximately equal to ln(n) <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>, <a class="yt-timestamp" data-t="00:16:58">[00:16:58]</a>. More precisely, S_n ≈ ln(n) + γ, where γ (gamma) is the Euler–Mascheroni constant (approximately 0.577) <a class="yt-timestamp" data-t="01:02:10">[01:02:10]</a>, <a class="yt-timestamp" data-t="01:02:21">[01:02:21]</a>. This constant quantifies the difference between the harmonic sum and the natural logarithm <a class="yt-timestamp" data-t="01:02:31">[01:02:31]</a>.

The derivative of ln(x) is 1/x <a class="yt-timestamp" data-t="00:53:59">[00:53:59]</a>. Conversely, the integral of 1/x from 1 to n is ln(n) <a class="yt-timestamp" data-t="00:55:21">[00:55:21]</a>, <a class="yt-timestamp" data-t="01:01:32">[01:01:32]</a>. The harmonic series sum can be visualized as a sum of rectangles whose total area is slightly larger than the area under the curve of 1/x <a class="yt-timestamp" data-t="00:58:13">[00:58:13]</a>, <a class="yt-timestamp" data-t="00:59:06">[00:59:06]</a>.

### The Alternating Harmonic Series

The alternating harmonic series (1 - 1/2 + 1/3 - 1/4 + ...) converges to ln(2) <a class="yt-timestamp" data-t="01:03:03">[01:03:03]</a>, <a class="yt-timestamp" data-t="01:03:05">[01:03:05]</a>, <a class="yt-timestamp" data-t="01:03:09">[01:03:09]</a>.

This can be understood by generalizing the series into a function: f(x) = x/1 - x^2/2 + x^3/3 - x^4/4 + ... <a class="yt-timestamp" data-t="01:05:04">[01:05:04]</a>. Taking the derivative of this series simplifies it to a [[Prime numbers and generating functions | geometric series]]: f'(x) = 1 - x + x^2 - x^3 + ... <a class="yt-timestamp" data-t="01:05:35">[01:05:35]</a>, <a class="yt-timestamp" data-t="01:05:41">[01:05:41]</a>.

A geometric series of the form 1 + r + r^2 + ... sums to 1/(1-r) <a class="yt-timestamp" data-t="01:06:44">[01:06:44]</a>, <a class="yt-timestamp" data-t="01:06:49">[01:06:49]</a>. In this case, r = -x, so f'(x) = 1/(1 - (-x)) = 1/(1 + x) <a class="yt-timestamp" data-t="01:06:52">[01:06:52]</a>, <a class="yt-timestamp" data-t="01:08:11">[01:08:11]</a>.

To find the sum of the original alternating series (which is f(1)), one can integrate f'(x) from 0 to 1 <a class="yt-timestamp" data-t="01:08:17">[01:08:17]</a>, <a class="yt-timestamp" data-t="01:08:21">[01:08:21]</a>. The integral of 1/(1+x) is ln(1+x) <a class="yt-timestamp" data-t="01:09:54">[01:09:54]</a>. Evaluating this from 0 to 1 gives ln(1+1) - ln(1+0) = ln(2) - ln(1) = ln(2) - 0 = ln(2) <a class="yt-timestamp" data-t="01:10:23">[01:10:23]</a>, <a class="yt-timestamp" data-t="01:10:39">[01:10:39]</a>, <a class="yt-timestamp" data-t="01:10:47">[01:10:47]</a>.

This sequence of manipulations demonstrates how [[Natural logarithms and exponential growth | natural logarithms]] emerge from seemingly unrelated series, further emphasizing their fundamental role in mathematics, particularly in relation to the behavior and [[Distribution of prime numbers and Dirichlets theorem | distribution of prime numbers]].