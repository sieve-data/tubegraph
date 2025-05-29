---
title: Complex numbers in discrete math
videoId: bOXCLR3Wric
---

From: [[3blue1brown]] <br/> 

While mathematics often compartmentalizes into distinct fields, [[complex_numbers|complex numbers]] surprisingly appear in areas seemingly unrelated to their continuous, geometric nature, such as discrete math problems involving whole numbers and sums <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. This unexpected utility is a recurring theme in mathematics <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

## Applications

### Prime Number Distribution
A prominent example of [[complex_numbers|complex numbers]]' application in discrete math is in the modern understanding of prime numbers <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. Questions about prime distribution and density are studied by analyzing specially designed functions whose inputs and outputs are [[complex_numbers|complex numbers]] <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. This is central to the famous Riemann Hypothesis, where a smooth, [[complex_numbers_as_a_foundation_for_understanding_quaternions|complex-valued]] function encodes information about discrete prime numbers, making certain questions about primes easier to answer through its analysis than by direct examination <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

### The Subset Sum Puzzle
A simpler "toy problem" demonstrates a similar principle <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. The puzzle asks to find the number of subsets of the set {1, ..., 2000} whose elements sum to a multiple of 5 <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

For example:
*   The set {3, 1, 4} has a sum of 8, which is not divisible by 5 <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   The set {2, 3, 5} has a sum of 10, which *is* divisible by 5, so it is counted <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
*   The empty set is counted, as its sum is 0, which is a multiple of 5 <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

There are 2^2000 total possible subsets <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>, making brute-force enumeration impossible <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. A heuristic guess might be one-fifth of the total subsets, but the challenge is to find the precise integer answer <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

#### Solving with Generating Functions

The solution involves a "generating function" <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. For the set {1, 2, 3, 4, 5}, the generating function is the polynomial:
`(1 + x)(1 + x^2)(1 + x^3)(1 + x^4)(1 + x^5)` <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>

When this polynomial is expanded, each term corresponds to a subset <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. The exponent of `x` in a term equals the sum of the elements in the corresponding subset <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. For example, `x^3` can come from `x^1 * x^2` (subset {1, 2}) or just `x^3` (subset {3}) <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>. When like terms are collected, the coefficient of `x^n` (`c_n`) indicates the number of subsets that sum to `n` <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

For the full puzzle (set {1, ..., 2000}), the generating function is:
`f(x) = (1 + x)(1 + x^2)...(1 + x^2000)` <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>

Evaluating this function at specific real values provides some initial insights:
*   `f(0) = c_0 = 1`: There is one subset (the empty set) with a sum of 0 <a class="yt=" data-t="00:12:17">[00:12:17]</a>.
*   `f(1) = 2^2000`: This is the sum of all coefficients (`Σc_n`), representing the total number of subsets <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.
*   `f(-1) = 0`: This implies that the sum of coefficients for even-sum subsets equals the sum of coefficients for odd-sum subsets (`Σc_even - Σc_odd = 0`), meaning half of all subsets have an even sum and half have an odd sum <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. This can be used to isolate even coefficients: `(f(1) + f(-1))/2 = Σc_even` <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>.

#### Complex Numbers as a Filtering Mechanism

To find subsets whose sum is divisible by 5, a similar filtering approach is needed, but this time with a period of 5 <a class="yt-timestamp" data-t="00:15:57">[00:15:57]</a>. This is where [[complex_numbers|complex numbers]] provide a "trick" by extending evaluation into the [[complex_numbers_introduction|complex plane]] <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>.

The key is to use the "fifth roots of unity" <a class="yt-timestamp" data-t="00:18:39">[00:18:39]</a>. These are [[complex_numbers|complex numbers]] that, when raised to the fifth power, equal 1 <a class="yt-timestamp" data-t="00:18:49">[00:18:49]</a>. Geometrically, they are points evenly spaced around the unit circle <a class="yt-timestamp" data-t="00:17:33">[00:17:33]</a>. Let `zeta` be `e^(i * 2π/5)` (a fifth of a turn around the unit circle) <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>. The five roots are `zeta^0, zeta^1, zeta^2, zeta^3, zeta^4` <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.

When these roots of unity are summed: `Σ(zeta^k)^m` for k=0 to 4:
*   If `m` is *not* a multiple of 5, the sum is 0 (due to cancellation, as the vectors representing the powers sum to zero) <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.
*   If `m` *is* a multiple of 5, each term `(zeta^k)^m` equals 1 (since `(zeta^k)^5 = 1`), so the sum is 5 (constructive interference) <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>.

This property acts as a filter <a class="yt-timestamp" data-t="00:22:25">[00:22:25]</a>. By evaluating the generating function `f(x)` at each of the five fifth roots of unity and summing the results, we can isolate the coefficients `c_n` where `n` is a multiple of 5 <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a>:

`Σ(f(zeta^k)) for k=0 to 4 = 5 * (c_0 + c_5 + c_10 + ...)` <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a>

Therefore, the number of subsets whose sum is divisible by 5 is:
`1/5 * [f(zeta^0) + f(zeta^1) + f(zeta^2) + f(zeta^3) + f(zeta^4)]` <a class="yt-timestamp" data-t="00:23:18">[00:23:18]</a>

#### Evaluating the Expression

`f(zeta^0)` is `f(1) = 2^2000` <a class="yt-timestamp" data-t="00:29:06">[00:29:06]</a>.

For `f(zeta)`, `f(zeta^2)`, `f(zeta^3)`, and `f(zeta^4)`, the calculation is more involved.
`f(zeta) = (1 + zeta)(1 + zeta^2)...(1 + zeta^2000)` <a class="yt-timestamp" data-t="00:24:31">[00:24:31]</a>.
Since `zeta` powers cycle every 5 terms, this product effectively becomes `((1 + zeta)(1 + zeta^2)(1 + zeta^3)(1 + zeta^4)(1 + zeta^5))^400` <a class="yt-timestamp" data-t="00:24:37">[00:24:37]</a>.

The key to evaluating `(1 + zeta)(1 + zeta^2)(1 + zeta^3)(1 + zeta^4)(1 + zeta^5)` comes from the factorization of `z^5 - 1`:
`z^5 - 1 = (z - zeta^0)(z - zeta^1)(z - zeta^2)(z - zeta^3)(z - zeta^4)` <a class="yt-timestamp" data-t="00:27:36">[00:27:36]</a>.
We know `zeta^0 = 1`, so `z^5 - 1 = (z - 1)(z - zeta)(z - zeta^2)(z - zeta^3)(z - zeta^4)` <a class="yt-timestamp" data-t="00:27:41">[00:27:41]</a>.
Dividing by `(z-1)`:
`z^4 + z^3 + z^2 + z + 1 = (z - zeta)(z - zeta^2)(z - zeta^3)(z - zeta^4)` <a class="yt-timestamp" data-t="00:27:36">[00:27:36]</a>.

To get `(1 + zeta)...`, we substitute `z = -1` into the equation <a class="yt-timestamp" data-t="00:28:07">[00:28:07]</a>:
`(-1)^4 + (-1)^3 + (-1)^2 + (-1) + 1 = (-1 - zeta)(-1 - zeta^2)(-1 - zeta^3)(-1 - zeta^4)`
`1 - 1 + 1 - 1 + 1 = (-1)^4 (1 + zeta)(1 + zeta^2)(1 + zeta^3)(1 + zeta^4)`
`1 = (1 + zeta)(1 + zeta^2)(1 + zeta^3)(1 + zeta^4)`

Therefore, `(1 + zeta)(1 + zeta^2)(1 + zeta^3)(1 + zeta^4)(1 + zeta^5)` becomes `1 * (1 + 1) = 2` <a class="yt-timestamp" data-t="00:28:30">[00:28:30]</a>.
So, `f(zeta)` (and `f(zeta^2)`, `f(zeta^3)`, `f(zeta^4)`) evaluates to `2^400` <a class="yt-timestamp" data-t="00:28:47">[00:28:47]</a>.

Combining these:
The number of subsets with sum divisible by 5 is:
`1/5 * [2^2000 + 2^400 + 2^400 + 2^400 + 2^400]`
`= 1/5 * [2^2000 + 4 * 2^400]` <a class="yt-timestamp" data-t="00:29:35">[00:29:35]</a>.

This can be verified with the smaller example (set {1, 2, 3, 4, 5}). The formula yields `1/5 * [2^5 + 4 * 2^1] = 1/5 * [32 + 8] = 1/5 * 40 = 8` <a class="yt-timestamp" data-t="00:29:50">[00:29:50]</a>, which matches the manual count <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

## Broader Mathematical Context

This approach of using [[complex_numbers|complex numbers]] to extract information about coefficients from a polynomial (or series) is a powerful and general technique <a class="yt-timestamp" data-t="00:30:43">[00:30:43]</a>. The idea of evaluating functions on a richer space of numbers like the [[complex_numbers_introduction|complex plane]] offers mathematicians significant power <a class="yt-timestamp" data-t="00:32:18">[00:32:18]</a>.

The specific use of [[geometric_representation_of_complex_numbers|complex numbers]] on the unit circle (roots of unity) to detect frequency information is extremely fruitful <a class="yt-timestamp" data-t="00:33:17">[00:33:17]</a>. This core idea underpins:
*   **Fourier Transforms and Series:** Fundamental tools for analyzing and synthesizing functions based on their frequency components <a class="yt-timestamp" data-t="00:33:49">[00:33:49]</a>.
*   **Shor's Algorithm:** A quantum computing algorithm for factoring large numbers, which leverages roots of unity to detect frequency information <a class="yt-timestamp" data-t="00:33:51">[00:33:51]</a>.

This demonstrates how [[uses_of_complex_numbers_in_mathematics_and_engineering|complex numbers]], particularly roots of unity, provide a unique capability to "suss out" frequency-related properties from discrete sequences, connecting seemingly disparate areas of mathematics <a class="yt-timestamp" data-t="00:33:20">[00:33:20]</a>.