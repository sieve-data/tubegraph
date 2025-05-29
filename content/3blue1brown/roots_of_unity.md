---
title: Roots of unity
videoId: bOXCLR3Wric
---

From: [[3blue1brown]] <br/> 

Roots of unity are complex numbers that, when raised to a specific integer power, result in the number one <a class="yt-timestamp" data-t="00:18:39">[00:18:39]</a>. They are special values located on the [[unit_circle_and_rational_points_in_relation_to_pythagorean_triples | unit circle]] in the complex plane <a class="yt-timestamp" data-t="00:17:33">[00:17:33]</a>.

## Definition and Properties

For a given integer `n`, the `n`-th roots of unity are the solutions to the equation `z^n = 1` <a class="yt-timestamp" data-t="00:18:39">[00:18:39]</a>. While `z = 1` is always a solution, there are `n-1` other solutions in the complex plane <a class="yt-timestamp" data-t="00:18:55">[00:18:55]</a>.

A specific example is the fifth root of unity, often labeled as `zeta` (ζ). This number sits a fifth of a turn around the [[unit_circle_and_rational_points_in_relation_to_pythagorean_triples | unit circle]] <a class="yt-timestamp" data-t="00:17:33">[00:17:33]</a>. Its angle is `2π/5` radians (or 72 degrees), and its magnitude is one <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>. Using Euler's formula notation, it can be explicitly written as `e^(2πi/5)` <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>.

A key property of roots of unity is their cyclical nature when raised to successive powers <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>. For the fifth root of unity:
*   `ζ^0 = 1`
*   `ζ^1 = ζ`
*   `ζ^2` rotates two-fifths of a turn around the [[unit_circle_and_rational_points_in_relation_to_pythagorean_triples | unit circle]] <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.
*   `ζ^3` rotates three-fifths of a turn <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>.
*   `ζ^4` rotates four-fifths of a turn <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>.
*   `ζ^5` rotates back to one, which is the same as `ζ^0` <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>.
This property means that powers of a root of unity cycle every `n` terms <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>.

## Application in the Subset Sum Puzzle

Roots of unity prove "unreasonably useful" in discrete mathematics, including the solution of a puzzle to find the number of subsets of the set {1, ..., 2000} whose elements sum to a number divisible by 5 <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

### Generating Functions

The puzzle can be approached using a *generating function* <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. For the set {1, 2, 3, 4, 5}, the generating function is the polynomial:
`f(x) = (1 + x)(1 + x^2)(1 + x^3)(1 + x^4)(1 + x^5)` <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.

When expanded, the coefficient of `x^k` in this polynomial represents the number of subsets whose elements sum to `k` <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. For the problem with elements up to 2000, the generating function becomes a product of 2000 binomial terms: `f(x) = (1 + x)(1 + x^2)...(1 + x^2000)` <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. The goal is to find the sum of coefficients `c_n` where `n` is a multiple of 5 <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.

### Filtering Coefficients with Roots of Unity

Evaluating the generating function at specific complex numbers, particularly the roots of unity, allows for filtering these coefficients <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.

Consider the sum of `f(x)` evaluated at the five fifth roots of unity (ζ^0, ζ^1, ζ^2, ζ^3, ζ^4) <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>:
`f(ζ^0) + f(ζ^1) + f(ζ^2) + f(ζ^3) + f(ζ^4)` <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>.

When the generating function is expressed as `f(x) = Σ c_n x^n`, evaluating `f(ζ^k)` and summing them results in a powerful cancellation effect:
*   For terms `c_j x^j` where `j` is *not* a multiple of 5, the sum of `ζ^(kj)` for `k` from 0 to 4 (i.e., `ζ^0j + ζ^1j + ζ^2j + ζ^3j + ζ^4j`) will cancel to zero <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>. This can be visualized as the vectors of the roots of unity summing to zero through [[vector_spaces_and_axioms | vector addition]] on the complex plane <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>.
*   For terms `c_j x^j` where `j` *is* a multiple of 5, `ζ^(kj)` will always reduce to 1 (since `ζ^5 = 1`) <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>. Thus, the sum `ζ^0j + ζ^1j + ζ^2j + ζ^3j + ζ^4j` will constructively interfere, summing to 5 <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>.

Therefore, `Σ f(ζ^k) = 5 * Σ c_n` where `n` is a multiple of 5 <a class="yt-timestamp" data-t="00:22:52">[00:22:52]</a>. To find the desired sum of coefficients, one simply divides this total by 5 <a class="yt-timestamp" data-t="00:23:24">[00:23:24]</a>.

### Calculation of `f(ζ^k)`

To perform the calculation, it's necessary to evaluate `f(ζ^k)` using its factored form: `f(x) = Π (1 + x^i)`.
The product `(1 + ζ)(1 + ζ^2)(1 + ζ^3)(1 + ζ^4)(1 + ζ^5)` is key for calculating `f(ζ)` <a class="yt-timestamp" data-t="00:24:43">[00:24:43]</a>.

This product can be evaluated using the polynomial factorization of `z^5 - 1` <a class="yt-timestamp" data-t="00:27:36">[00:27:36]</a>:
`z^5 - 1 = (z - ζ^0)(z - ζ^1)(z - ζ^2)(z - ζ^3)(z - ζ^4)` <a class="yt-timestamp" data-t="00:27:41">[00:27:41]</a>.
By setting `z = -1`, the left side becomes `(-1)^5 - 1 = -2` <a class="yt-timestamp" data-t="00:28:10">[00:28:10]</a>.
The right side becomes `(-1 - ζ^0)(-1 - ζ^1)(-1 - ζ^2)(-1 - ζ^3)(-1 - ζ^4)`.
Factoring out `-1` from each term, this simplifies to `(-1)^5 * (1 + ζ^0)(1 + ζ^1)(1 + ζ^2)(1 + ζ^3)(1 + ζ^4)` <a class="yt-timestamp" data-t="00:28:13">[00:28:13]</a>.
Thus, `-2 = -1 * (1 + ζ^0)(1 + ζ^1)(1 + ζ^2)(1 + ζ^3)(1 + ζ^4)`.
This implies that `(1 + ζ^0)(1 + ζ^1)(1 + ζ^2)(1 + ζ^3)(1 + ζ^4) = 2` <a class="yt-timestamp" data-t="00:28:30">[00:28:30]</a>.

Given that `f(x) = (1 + x)(1 + x^2)...(1 + x^2000)`, and the powers of `x` in the factors (`x^i`) cycle with respect to `ζ^k` every 5 terms, `f(ζ)` can be written as `((1 + ζ^0)(1 + ζ^1)(1 + ζ^2)(1 + ζ^3)(1 + ζ^4))^400` <a class="yt-timestamp" data-t="00:24:43">[00:24:43]</a>.
Since the base product is 2, `f(ζ) = 2^400` <a class="yt-timestamp" data-t="00:28:47">[00:28:47]</a>.
Similarly, `f(ζ^2) = f(ζ^3) = f(ζ^4) = 2^400` due to the shuffling effect of powers of roots of unity <a class="yt-timestamp" data-t="00:28:51">[00:28:51]</a>.

The final term needed is `f(ζ^0) = f(1)`. This is `(1 + 1)(1 + 1^2)...(1 + 1^2000) = 2^2000` <a class="yt-timestamp" data-t="00:29:06">[00:29:06]</a>.

The total sum of coefficients `c_n` where `n` is a multiple of 5 is:
`(1/5) * [f(1) + f(ζ) + f(ζ^2) + f(ζ^3) + f(ζ^4)]` <a class="yt-timestamp" data-t="00:29:35">[00:29:35]</a>
`= (1/5) * [2^2000 + 2^400 + 2^400 + 2^400 + 2^400]` <a class="yt-timestamp" data-t="00:29:38">[00:29:38]</a>
`= (1/5) * [2^2000 + 4 * 2^400]` <a class="yt-timestamp" data-t="00:29:42">[00:29:42]</a>.

This specific calculation demonstrates how complex numbers can solve a seemingly purely discrete problem <a class="yt-timestamp" data-t="00:23:30">[00:23:30]</a>.

## Broader Significance

The application of roots of unity extends far beyond toy problems:
*   **Discrete Math:** The technique is similar in spirit to how prime numbers are studied in relation to the Riemann hypothesis <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. The [[role_of_invariants_in_mathematics | concept of invariants]] and analysis of functions with complex inputs provides insights into discrete sequences (e.g., coefficients) <a class="yt-timestamp" data-t="00:31:02">[00:31:02]</a>.
*   **Frequency Detection:** The ability of roots of unity to capture cycling behavior makes them extremely fruitful for detecting frequency information <a class="yt-timestamp" data-t="00:33:17">[00:33:17]</a>. This is the core idea underlying [[applications_of_polynomial_rootfinding_in_computer_graphics | Fourier transforms]] and Fourier series <a class="yt-timestamp" data-t="00:33:49">[00:33:49]</a>.
*   **Quantum Computing:** Peter Shor's algorithm for quantum computers, which can factor large numbers significantly faster than classical computers, relies on the use of roots of unity to detect frequency information <a class="yt-timestamp" data-t="00:33:59">[00:33:59]</a>.