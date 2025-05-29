---
title: Natural logarithms and exponential growth
videoId: 4PDoT7jtxmw
---

From: [[3blue1brown]] <br/> 

Natural logarithms and the mathematical constant 'e' are fundamental in understanding [[exponential growth and decay | exponential growth]] and various natural phenomena. They often appear in unexpected places, from the density of prime numbers to the behavior of infinite series and the rates of change in systems.

## The Natural Logarithm and Prime Numbers

A surprising relationship exists between the [[relationship_between_natural_logs_and_prime_numbers | natural logarithm]] and the distribution of [[relationship_between_natural_logs_and_prime_numbers | prime numbers]] <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>. As numbers increase, the density of [[relationship_between_natural_logs_and_prime_numbers | prime numbers]] generally decreases <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. For instance, while a list of primes between 0 and 50 includes many familiar numbers, a range of 1000 integers around a trillion (10^12) contains only 37 primes <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. This means the proportion of primes in that range is approximately 1 in 27 <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

Mathematicians can estimate this density using the [[relationship_between_natural_logs_and_prime_numbers | natural logarithm]] <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. The density of [[relationship_between_natural_logs_and_prime_numbers | prime numbers]] near a given value, like a trillion, is roughly inversely proportional to the [[natural_phenomena_and_their_relationship_with_exponentials | natural log]] of that number <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. The [[natural_phenomena_and_their_relationship_with_exponentials | natural log]] of a trillion (ln(10^12)) is approximately 27 <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>, which remarkably matches the observed density <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. This connection highlights why 'natural logarithm' is a fitting name, as it appears in fundamental aspects of number theory <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

### Natural Logarithms and Infinite Series

The [[natural_phenomena_and_their_relationship_with_exponentials | natural logarithm]] also appears in the sums of certain infinite series:

*   **Alternating Harmonic Series**: The sum of the series 1 - 1/2 + 1/3 - 1/4 + ... approaches the [[natural_phenomena_and_their_relationship_with_exponentials | natural log]] of 2 (approximately 0.69) <a class="yt-timestamp" data-t="01:03:05">[01:03:05]</a>. This can be derived by generalizing the series with a variable `x`, taking its derivative to reveal a geometric series, and then integrating the result <a class="yt-timestamp" data-t="01:05:04">[01:05:04]</a> <a class="yt-timestamp" data-t="01:05:35">[01:05:35]</a> <a class="yt-timestamp" data-t="01:06:20">[01:06:20]</a> <a class="yt-timestamp" data-t="01:09:54">[01:09:54]</a>.

*   **Harmonic Series**: The sum of the series 1 + 1/2 + 1/3 + 1/4 + ... does not converge to a specific value; it grows indefinitely <a class="yt-timestamp" data-t="01:00:02">[01:00:02]</a> <a class="yt-timestamp" data-t="01:13:43">[01:13:43]</a>. Each term becomes smaller, but the sum will eventually exceed any chosen number, however large <a class="yt-timestamp" data-t="01:00:02">[01:00:02]</a>.
    *   This divergence can be intuitively shown by grouping terms: (1/3 + 1/4) > 1/2, (1/5 + 1/6 + 1/7 + 1/8) > 1/2, and so on <a class="yt-timestamp" data-t="01:15:50">[01:15:50]</a>. Since there are infinitely many such groups, each summing to more than 1/2, the total sum is infinite <a class="yt-timestamp" data-t="01:15:56">[01:15:56]</a>.
    *   The sum up to `1/n` is approximately equal to the [[natural_phenomena_and_their_relationship_with_exponentials | natural log]] of `n` (ln(n)) <a class="yt-timestamp" data-t="01:16:54">[01:16:54]</a>. For example, to make the sum exceed one million, `n` must be roughly `e` to the power of one million (e^1,000,000) <a class="yt-timestamp" data-t="01:20:21">[01:20:21]</a>. This is an enormous number, approximately 10^400,000 <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>. The relationship is even more precise, being `ln(n) + γ`, where `γ` (Euler's constant) is approximately 0.577 <a class="yt-timestamp" data-t="01:02:16">[01:02:16]</a>.

## The Role of 'e' in Exponential Functions

The constant 'e' (approximately 2.718) is central to [[exponential growth | exponential functions]], often written as `e^x` or `e^(rt)` to describe [[exponential growth | exponential growth]] or decay <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. However, any [[exponential growth | exponential function]] `a^x` (where `a` is any positive base) can be expressed in terms of 'e' <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This is because `a^x = (e^(ln(a)))^x = e^((ln(a)) * x)` <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The number 'e' does not *produce* these families of curves, but rather serves as a convenient base for their representation <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

### Why 'e' is "Natural": Derivatives

The special significance of 'e' lies in its unique derivative [[calculus_and_exponential_functions | property]]: the derivative of `e^t` with respect to `t` is `e^t` itself <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This means the rate of change of the function at any point is equal to its current value <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This reflects continuous compound growth, where the growth rate is proportional to the current amount <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

For a general [[exponential growth | exponential function]] `a^t`, its [[derivatives_of_exponential_functions | derivative]] is `ln(a) * a^t` <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This `ln(a)` term is the proportionality constant. By choosing 'e' as the base (where `ln(e) = 1`), this constant becomes 1, simplifying calculations related to rates of change in [[calculus_and_exponential_functions | calculus]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This simplifies the interpretation of parameters in models, such as `r` in `e^(rt)`, which directly represents the continuous growth rate <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

The property `d/dx(e^x) = e^x` can be seen as the definition of 'e' itself, or it can be derived from the Taylor series definition of `e^x` (exp(x)) as `1 + x + x^2/2! + x^3/3! + ...` <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a> <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Taking the derivative of this polynomial term by term reproduces the original series <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

### Derivatives of Natural Logarithms

The derivative of the [[natural_phenomena_and_their_relationship_with_exponentials | natural log]] function `ln(x)` is `1/x` <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This can be derived using [[calculus_and_exponential_functions | implicit differentiation]]. If `y = ln(x)`, then by the definition of the [[natural_phenomena_and_their_relationship_with_exponentials | natural logarithm]], `e^y = x` <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Taking the derivative with respect to `x` on both sides: `d/dx(e^y) = d/dx(x)`. Using the chain rule, `e^y * dy/dx = 1`. Rearranging for `dy/dx` gives `dy/dx = 1/e^y`. Since `e^y = x`, the derivative `dy/dx = 1/x` <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This derivative intuitively makes sense as `ln(x)` becomes progressively shallower as `x` increases, just as `1/x` becomes smaller <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

### Integrals and Natural Logarithms

The inverse operation of differentiation is integration. The integral of `1/x` is the [[natural_phenomena_and_their_relationship_with_exponentials | natural log]] of `x` (plus a constant of integration) <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This integral directly links to the harmonic series, as the area under the curve `1/x` from 1 to `n` is `ln(n)` <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. While the integral approximates the sum of `1/n` terms, the sum is always slightly larger than the integral due to the way rectangles are drawn to represent the terms <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

The profound and frequent appearance of the [[natural_phenomena_and_their_relationship_with_exponentials | natural logarithm]] and 'e' in diverse mathematical contexts, from number theory to [[calculus_and_exponential_functions | calculus]], reinforces their fundamental significance.