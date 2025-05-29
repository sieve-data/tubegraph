---
title: Series and sums in relation to natural log
videoId: 4PDoT7jtxmw
---

From: [[3blue1brown]] <br/> 

The [[natural_logarithm_and_its_significance | natural logarithm]] (often denoted as `ln` or `log` with base `e`) appears in various seemingly unrelated mathematical contexts, from the distribution of prime numbers to the sums of infinite series. Its significance often stems from its unique relationship with rates of change in calculus [00:30:56].

## The Natural Logarithm Defined

The [[natural_logarithm_and_its_significance | natural logarithm]] of a number `X` (written as `ln(X)`) answers the question: "To what power must 'e' be raised to equal `X`?" [00:05:01]
Mathematically, `ln(X) = Y` is equivalent to `e^Y = X` [00:04:55]. The number `e` is an irrational constant approximately equal to 2.718. For example, `ln(10)` is approximately 2.3, meaning `e^2.3` is roughly 10 [00:05:08].

## Connection to Prime Number Density

One surprising appearance of the [[natural_logarithm_and_its_significance | natural logarithm]] is in the density of prime numbers [00:05:25]. The [[density_of_prime_numbers_and_natural_log | density of prime numbers]] near a given large value, such as a trillion (`10^12`), is approximately 1 divided by the [[natural_logarithm_and_its_significance | natural logarithm]] of that value [00:04:18].

For numbers around a trillion (`10^12`):
*   The [[natural_logarithm_and_its_significance | natural log]] of a trillion is approximately 27 [00:05:36].
*   This suggests that around 1 in 27 numbers in that range are prime [00:04:09].
*   For the range between 1 trillion and 1 trillion plus 1000, there are 37 primes [00:03:56], meaning the proportion is 37/1000, or about 1 in 27 [00:04:09]. This observation is a "cute fact" in mathematics [00:05:47].

## Natural Logarithms and Infinite Sums

The [[natural_logarithm_and_its_significance | natural logarithm]] also arises when considering various infinite sums.

### The Basel Problem: Sum of Reciprocals of Squares

The sum of the reciprocals of squares is a well-known result:
`1/1^2 + 1/2^2 + 1/3^2 + 1/4^2 + ...`
This [[infinite_sums_and_approximations | infinite sum]] was an open question in Europe for a time before Euler proved it converges to `π^2 / 6` [00:07:03]. This is notable for relating `π` to a sum of integers.

### Euler's Prime-Related Sums

Euler discovered an even stranger connection between primes and series:
By playing a "weird game" with the sum of reciprocals of squares, where terms corresponding to composite numbers are excluded and terms corresponding to powers of primes are scaled down, the resulting sum is the [[natural_logarithm_and_its_significance | natural logarithm]] of the original sum's result [00:09:22].

*   If `S = 1/1^2 + 1/2^2 + 1/3^2 + ... = π^2 / 6` [00:07:03]
*   A modified series (including `1/p^2` for primes `p`, `1/2 * 1/(p^2)^2` for `1/p^4`, etc.) sums to `ln(π^2 / 6)` [00:09:22].

A similar phenomenon occurs with the alternating sum of reciprocals of odd numbers:
*   `1 - 1/3 + 1/5 - 1/7 + ... = π / 4` [00:09:58]
*   If a similar "game" is played (keeping only prime-related odd numbers and scaling prime powers), the new sum equals `ln(π / 4)` [01:10:06].

These relationships demonstrate a profound connection between the [[natural_logarithm_and_its_significance | natural logarithm]] and prime number patterns [01:11:14].

### The Alternating Harmonic Series

The alternating harmonic series: `1 - 1/2 + 1/3 - 1/4 + 1/5 - ...`
This series converges to a value of approximately 0.69 [01:12:52]. More precisely, it converges to the [[natural_logarithm_and_its_significance | natural log]] of 2 (`ln(2)`) [01:03:09]. This can be derived by generalizing the series to a function of `x`, taking its derivative to obtain a geometric series, and then integrating the result [01:12:42].

### The Harmonic Series

The harmonic series: `1 + 1/2 + 1/3 + 1/4 + ...`
Unlike the sum of reciprocals of squares, this series does not converge to a finite value; it "gets bigger than any number you choose" [01:03:46]. This divergence can be shown by grouping terms, revealing that the sum is always greater than `1 + 1/2 + 1/2 + 1/2 + ...`, which clearly goes to infinity [01:02:10].

However, the sum of the first `n` terms of the harmonic series (`1 + 1/2 + ... + 1/n`) is approximately equal to the [[natural_logarithm_and_its_significance | natural log]] of `n` (`ln(n)`) [01:01:56].
More accurately, the sum `S_n = 1 + 1/2 + ... + 1/n` is approximately `ln(n) + γ`, where `γ` (gamma) is the Euler-Mascheroni constant (approximately 0.577) [01:02:16]. This constant represents the difference between the harmonic sum and the [[natural_logarithm_and_its_significance | natural log]] as `n` approaches infinity [01:02:31].

> [!NOTE] Example Calculation
> To find `n` such that `1 + 1/2 + ... + 1/n` is greater than a million:
> `ln(n) ≈ 1,000,000` [01:13:09]
> This implies `n ≈ e^(1,000,000)` [01:13:21]
> Since `e ≈ 10^0.434` (because `ln(10) ≈ 2.3`, so `1/ln(10) ≈ 1/2.3 ≈ 0.434`), `n ≈ (10^0.434)^(1,000,000) = 10^(434,000)` [01:14:02]. This is an incredibly large number, vastly exceeding the estimated number of atoms in the universe (10^80) [01:13:30].

## Why 'e' is "Natural": Its Calculus Properties

The term "[[natural_logarithm_and_its_significance | natural logarithm]]" comes from the prevalence of `e` in describing natural phenomena, particularly those involving rates of change. While any exponential function `a^x` can be written as `e^(ln(a) * x)` [01:14:47], `e` is special because its derivative is itself [01:15:58]:
`d/dx (e^x) = e^x` [01:16:00]

This unique property means that for an exponential function `e^(rt)`, its rate of change is `r` times its current value [01:17:02]. This simplifies proportionality constants in various applications:
*   **Exponential Growth/Decay:** If `e^(rt)` represents a quantity, `r` directly represents the continuous growth rate [01:17:02].
*   **Bell Curves:** The standard form of a bell curve uses `e` (`e^(-x^2/s^2)`) because the parameter `s` directly relates to the standard deviation [01:19:50].
*   **Complex Exponentials:** `e^(it)` (where `i` is the imaginary unit) describes circular motion in the complex plane, where `t` directly represents the distance walked in radians [01:20:10]. The derivative `d/dt (e^(it)) = i * e^(it)` means the velocity vector is always 90 degrees rotated from the position vector, and its speed is 1 unit per second if the magnitude of the position vector is 1 [01:21:15].

## Derivative and Integral of Natural Logarithm

The fundamental relationship between `e^x` and `ln(x)` allows us to derive the derivative of `ln(x)`.
If `y = ln(x)`, then `x = e^y` [01:22:07].
Using implicit differentiation (differentiating both sides with respect to `x`):
`dx/dx = d/dx (e^y)`
`1 = e^y * dy/dx` [01:22:42] (using the chain rule, as `e^y` is its own derivative, multiplied by `dy/dx`)
`dy/dx = 1 / e^y` [01:22:52]
Since `x = e^y`, we can substitute `x` back in:
`d/dx (ln(x)) = 1/x` [01:23:28]

This result is significant because it connects the [[natural_logarithm_and_its_significance | natural logarithm]] to the function `1/x`.
The integral of `1/x` from 1 to `n` is `ln(n)` [01:25:04]. This means the area under the curve `1/x` from 1 to `n` is exactly `ln(n)` [01:26:04].

Comparing the harmonic series (`S = 1 + 1/2 + 1/3 + ... + 1/N`) with the integral of `1/x` (`I = ∫(1 to N) (1/x) dx`):
*   The sum `S` represents the sum of areas of rectangles of width 1 and height `1/n` [01:28:50].
*   The integral `I` represents the area under the curve `1/x` [01:29:18].
*   By visualizing these on a graph, it's clear that the sum of the rectangles (using the left endpoint for height) will always be larger than the area under the curve [01:28:50]. Thus, the sum `S` is greater than the integral `I` [01:27:54]. This visual insight reinforces why `ln(n)` serves as a good approximation for the harmonic sum.

These connections illustrate why the [[natural_logarithm_and_its_significance | natural logarithm]] is considered "natural" and fundamental across various branches of mathematics, from [[density_of_prime_numbers_and_natural_log | number theory]] to calculus and [[natural_logarithm_and_proportionality_constants | probability]].