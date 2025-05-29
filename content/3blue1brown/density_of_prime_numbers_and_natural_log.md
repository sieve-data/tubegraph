---
title: Density of prime numbers and natural log
videoId: 4PDoT7jtxmw
---

From: [[3blue1brown]] <br/> 

The density of [[prime_numbers_and_their_regularities|prime numbers]] within a given range can be estimated using the [[natural_logarithm_and_its_significance|natural logarithm]] <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>. This mathematical relationship provides a surprisingly accurate approximation, even for very large numbers <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>.

## Estimating Prime Density at High Values

When considering a range of numbers, such as those between 1 trillion and 1 trillion plus a thousand, the proportion of [[prime_numbers_and_their_regularities|prime numbers]] decreases as the numbers get larger <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>. This is because larger numbers have more potential factors <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>. For instance, in the range of 1,000 integers starting from 1 trillion (10^12), there are 37 prime numbers, yielding a proportion of 0.037 or approximately one in every 27 numbers <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>.

Mathematicians can quickly estimate this proportion by using the [[natural_logarithm_and_proportionality_constants|natural logarithm]] <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>. The density of [[prime_numbers_and_their_regularities|prime numbers]] near a given value, like a trillion, is roughly one divided by the [[natural_logarithm_and_proportionality_constants|natural log]] of that value <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>. For a trillion (10^12), the natural log (log base `e`) is approximately 27 <a class="yt-timestamp" data-t="05:36:00">[05:36:00]</a>. This means the proportion of primes is close to one in 27, a significantly higher density than many might intuitively guess <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>.

### What is a Natural Logarithm?
The [[natural_logarithm_and_its_significance|natural logarithm]] of a number `X`, denoted as `ln(X)` or `log_e(X)`, answers the question: `e` to what power equals `X`? <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a> For example, `ln(10)` is approximately 2.3, meaning `e^2.3` is roughly 10 <a class="yt-timestamp" data-t="05:04:00">[05:04:00]</a>.

## The "Naturalness" of the Natural Logarithm

The term "natural" for the [[natural_logarithm_and_its_significance|natural logarithm]] stems from its frequent appearance in various natural phenomena and mathematical relationships <a class="yt-timestamp" data-t="06:10:00">[06:10:10]</a>. Beyond [[prime_numbers_and_their_regularities|prime numbers]], it is deeply connected to infinite [[series_and_sums_in_relation_to_natural_log|series and sums]].

### Connection to Pi and Prime Numbers
A bizarre connection exists between [[relation_between_pi_and_prime_numbers|Pi]] and [[prime_numbers_and_their_regularities|prime numbers]] through series manipulated by specific rules <a class="yt-timestamp" data-t="07:12:00">[07:12:00]</a>.
Consider Euler's solution to the Basel problem, where the sum of the reciprocals of squares (`1/1^2 + 1/2^2 + 1/3^2 + ...`) equals `pi^2 / 6` <a class="yt-timestamp" data-t="06:34:00">[06:34:00]</a>. A peculiar manipulation of this series, which selectively keeps or scales terms based on their relation to primes, results in the [[natural_logarithm_and_proportionality_constants|natural log]] of `pi^2 / 6` <a class="yt-timestamp" data-t="09:19:00">[09:19:00]</a>.

The rule for manipulating the series:
> Keep terms where the denominator is a [[prime_numbers_and_their_regularities|prime number]]. For terms where the denominator is a power of a [[prime_numbers_and_their_regularities|prime number]] (e.g., `n = p^k`), keep the term but scale it down by `1/k`. Kick out all other terms (composite numbers not powers of a prime) <a class="yt-timestamp" data-t="07:27:00">[07:27:00]</a>.

For example, `1/4^2` (where 4 is `2^2`) is scaled down by `1/2` to become `(1/2) * (1/4^2)` <a class="yt-timestamp" data-t="07:41:00">[07:41:00]</a>. `1/8^2` (where 8 is `2^3`) is scaled down by `1/3` <a class="yt-timestamp" data-t="08:18:00">[08:18:00]</a>. This "weird game" consistently yields a result equal to the [[natural_logarithm_and_proportionality_constants|natural log]] of the original series' sum, showcasing an unexpected link between `e`, [[relation_between_pi_and_prime_numbers|pi]], and [[prime_numbers_and_their_regularities|prime numbers]] <a class="yt-timestamp" data-t="09:43:00">[09:43:00]</a>.

### The Harmonic Series and Logarithmic Growth
The harmonic series (`1 + 1/2 + 1/3 + 1/4 + ... + 1/n`) is another example of a [[series_and_sums_in_relation_to_natural_log|series]] connected to the [[natural_logarithm_and_its_significance|natural logarithm]] <a class="yt-timestamp" data-t="13:39:00">[13:39:00]</a>. Unlike the sum of reciprocals of squares, the harmonic series does not converge to a finite value; it grows indefinitely <a class="yt-timestamp" data-t="13:46:00">[13:46:00]</a>. However, its growth is logarithmic <a class="yt-timestamp" data-t="16:39:00">[16:39:00]</a>. The sum up to `1/n` is approximately equal to `ln(n)` <a class="yt-timestamp" data-t="16:54:00">[16:54:00]</a>. More precisely, it's `ln(n)` plus a constant known as the Euler-Mascheroni constant (approximately 0.577) <a class="yt-timestamp" data-t="17:02:00">[17:02:00]</a>.

To illustrate the slow growth, reaching a sum greater than 1 million requires `n` to be an enormous number, approximately `e` to the power of 1 million (10^400,000) <a class="yt-timestamp" data-t="19:23:00">[19:23:00]</a>. This is because `ln(n) ≈ 1,000,000` implies `n ≈ e^(1,000,000)` <a class="yt-timestamp" data-t="20:13:00">[20:13:00]</a>. Using the approximation `ln(10) ≈ 2.3`, `e^(1,000,000)` can be converted to `(e^ln(10))^(1,000,000/ln(10))` which is approximately `10^(1,000,000/2.3) ≈ 10^434,782` <a class="yt-timestamp" data-t="21:19:00">[21:19:00]</a>.

### Exponential Functions and 'e'

The number `e` (approximately 2.718) is the preferred base for exponential functions in mathematics, physics, and engineering due to its unique relationship with rates of change <a class="yt-timestamp" data-t="24:15:00">[24:15:00]</a>.

The defining characteristic of `e^t` is that its derivative with respect to `t` is equal to itself: `d/dt (e^t) = e^t` <a class="yt-timestamp" data-t="31:00:00">[31:00:00]</a>. This means the rate of change of an exponential function with base `e` is directly proportional to its current value, with a proportionality constant of 1 <a class="yt-timestamp" data-t="31:42:00">[31:42:00]</a>. For any other base `a`, the derivative of `a^t` is `ln(a) * a^t` <a class="yt-timestamp" data-t="36:12:00">[36:12:00]</a>. This demonstrates why `e` is chosen as the "natural" base: it simplifies the expression of growth rates by making the proportionality constant explicit within the exponent <a class="yt-timestamp" data-t="33:06:00">[33:06:00]</a>.

This property is crucial in understanding:
*   **Bell curves (Normal Distribution)**: These are often written using `e` because the parameters in the exponent directly relate to statistical properties like standard deviation <a class="yt-timestamp" data-t="25:50:00">[25:50:00]</a>.
*   **Complex Exponentials (Euler's Formula)**: `e^(it)` describes points moving around the unit circle in the complex plane, where `t` directly represents the distance walked (in radians) <a class="yt-timestamp" data-t="29:05:00">[29:05:00]</a>. For other bases like `2^(it)`, the rate of movement is scaled by `ln(2)` <a class="yt-timestamp" data-t="30:26:00">[30:26:00]</a>.

## Derivatives and Integrals of the Natural Logarithm

The [[natural_logarithm_and_its_significance|natural logarithm]]'s derivative and integral also highlight its fundamental role in calculus.

### Derivative of `ln(x)`
If `y = ln(x)`, then by the definition of the natural logarithm, `x = e^y` <a class="yt-timestamp" data-t="51:55:00">[51:55:00]</a>. Using implicit differentiation, `dx/dy = e^y` <a class="yt-timestamp" data-t="52:28:00">[52:28:00]</a>. Since `dy/dx` is the reciprocal of `dx/dy`, we get `dy/dx = 1/e^y` <a class="yt-timestamp" data-t="52:52:00">[52:52:00]</a>. Substituting `e^y = x`, the derivative of `ln(x)` is `1/x` <a class="yt-timestamp" data-t="53:24:00">[53:24:00]</a>.

### Integral of `1/x`
Since the derivative of `ln(x)` is `1/x`, it follows that the antiderivative (or integral) of `1/x` is `ln(x)` <a class="yt-timestamp" data-t="59:50:00">[59:50:00]</a>. The integral of `1/x` from 1 to `n` is `ln(n) - ln(1) = ln(n) - 0 = ln(n)` <a class="yt-timestamp" data-t="01:01:04">[01:01:04]</a>.

This integral provides a continuous approximation of the harmonic series <a class="yt-timestamp" data-t="55:32:00">[55:32:00]</a>. Graphically, the sum of rectangles representing `1/n` terms (starting at `n=1`) will always be slightly larger than the area under the curve of `1/x` from 1 to `n` <a class="yt-timestamp" data-t="58:54:00">[58:54:00]</a>. The difference between the sum and the integral converges to the Euler-Mascheroni constant <a class="yt-timestamp" data-t="01:02:07">[01:02:07]</a>.

### Alternating Harmonic Series
The alternating harmonic series (`1 - 1/2 + 1/3 - 1/4 + ...`) converges to `ln(2)` <a class="yt-timestamp" data-t="01:03:03">[01:03:03]</a>. This can be shown by generalizing the series to a function `f(x) = x - x^2/2 + x^3/3 - x^4/4 + ...` <a class="yt-timestamp" data-t="01:04:59">[01:04:59]</a>. Taking the derivative of this series results in a geometric series `1 - x + x^2 - x^3 + ...` <a class="yt-timestamp" data-t="01:05:35">[01:05:35]</a>, which sums to `1/(1+x)` <a class="yt-timestamp" data-t="01:08:11">[01:08:11]</a>. Integrating `1/(1+x)` from 0 to 1 yields `ln(1+x)` evaluated from 0 to 1, which simplifies to `ln(2) - ln(1) = ln(2)` <a class="yt-timestamp" data-t="01:09:46">[01:09:46]</a>. Since `f(1)` is the alternating harmonic series and the integral of its derivative is `ln(2)`, it proves the relationship.