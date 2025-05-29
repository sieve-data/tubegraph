---
title: Generating functions and subsets
videoId: bOXCLR3Wric
---

From: [[3blue1brown]] <br/> 

This article explores a challenging discrete math puzzle that can be solved using [[complex_functions_and_transformations | complex numbers]] and [[prime_numbers_and_generating_functions | generating functions]], an approach that might seem absurd for a question solely about whole numbers and their sums <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. This method is not unique; [[complex_functions_and_transformations | complex numbers]] are "unreasonably useful for discrete math" in various contexts <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. A more famous example is how mathematicians understand [[distribution_of_prime_numbers_and_dirichlets_theorem | prime numbers]] and their distribution by studying specially designed functions with [[complex_functions_and_transformations | complex number]] inputs and outputs, as seen in the Riemann hypothesis <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## The Puzzle

The puzzle is taken from a collection of problems used in training the USA team for the International Math Olympiad by Titu Andreescu and Zuming Feng <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

The specific question is:
> Find the number of subsets of the set 1 up to 2000, the sum of whose elements is divisible by 5 <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

For example, the set {2, 3, 5} is a subset whose sum (10) is divisible by 5 <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. The empty set, with a sum of 0, is also counted as its sum is considered a multiple of 5 <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

### Brute-Force Limitations

A brute-force approach would involve iterating through all possible subsets and checking their sums <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. However, the total number of subsets for a set with 2000 elements is 2 to the power of 2000 <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>, as each of the 2000 elements presents a binary choice (include or not include) <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. This number is astronomically large, making brute-force computation impossible <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

### Initial Approximation

One might guess that approximately one-fifth of all total subsets would have a sum divisible by 5, assuming a roughly even distribution of sums modulo 5 <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. While this is a decent approximation, the challenge lies in finding a precise integer answer <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

## Introducing Generating Functions

The solution involves a technique called a [[prime_numbers_and_generating_functions | generating function]] <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

### Simpler Example (1, 2, 3, 4, 5)

To understand the concept, consider a simpler set: {1, 2, 3, 4, 5} <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. There are 2 to the power of 5 (32) total subsets <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

The key insight is to consider the polynomial:
`(1 + x)(1 + x^2)(1 + x^3)(1 + x^4)(1 + x^5)` <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.

When this polynomial is algebraically expanded, each term in the expansion corresponds to a unique subset <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. The exponent of 'x' in each term equals the sum of the elements in the corresponding subset <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. For example, choosing `x^1` and `x^2` (and '1' from others) corresponds to the subset {1, 2} and results in an `x^3` term <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>. When like terms are collected (e.g., `3x^10`), the coefficient (3) represents the number of distinct subsets whose elements sum to that particular value (10) <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.

In this small example, there are 8 subsets whose sum is divisible by 5 <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. This is slightly larger than the heuristic guess of 6.4 (1/5 of 32) <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

### Applying to the Main Puzzle

For the problem with the set 1 up to 2000, the corresponding [[prime_numbers_and_generating_functions | generating function]] is:
`f(x) = (1 + x)(1 + x^2)(1 + x^3) ... (1 + x^2000)` <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.

If `f(x)` is expanded as `sum(c_n * x^n)`, then each coefficient `c_n` represents the number of subsets whose elements sum to `n` <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. The goal is to deduce information about these coefficients without actually expanding the expression <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.

[[prime_numbers_and_generating_functions | Generating functions]] are widely applicable, for instance, in studying Fibonacci numbers where coefficients of a power series can be Fibonacci numbers <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

## Manipulating the Generating Function

We treat `f(x)` as an actual function, plugging in values for `x` to gain insight into its coefficients <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>.

### Evaluating at x = 0

`f(0) = (1+0)(1+0)...(1+0) = 1` <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.
In the expanded form, `f(0)` only leaves the `c_0` term <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>. This simply tells us `c_0 = 1`, corresponding to the single empty set <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.

### Evaluating at x = 1

`f(1) = (1+1)(1+1)...(1+1)` (2000 times) `= 2^2000` <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.
In the expanded form, `f(1)` equals the sum of all coefficients (`c_0 + c_1 + ... + c_N`) <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>. This confirms that the total number of subsets is `2^2000` <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.

### Evaluating at x = -1

`f(-1) = (1 + (-1))(1 + (-1)^2)...(1 + (-1)^2000)` <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>.
Since the first term `(1 + (-1))` is 0, the entire expression `f(-1)` is 0 <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.
When `x = -1` is plugged into the expanded polynomial `sum(c_n * x^n)`, terms alternate in sign: `c_0 - c_1 + c_2 - c_3 + ...` <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.
Since `f(-1) = 0`, this means `(c_0 + c_2 + c_4 + ...) - (c_1 + c_3 + c_5 + ...) = 0` <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>. This implies that the sum of coefficients for even-sum subsets equals the sum of coefficients for odd-sum subsets <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>, meaning half of all subsets have an even sum and half have an odd sum <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>.

Combining `f(1)` and `f(-1)`:
`(f(1) + f(-1)) / 2 = (sum(c_n) + sum(c_n * (-1)^n)) / 2`
This sum filters out odd coefficients and leaves only the even coefficients: `c_0 + c_2 + c_4 + ...` <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>.
So, `(2^2000 + 0) / 2 = 2^1999` is the total number of subsets with an even sum <a class="yt-timestamp" data-t="00:15:48">[00:15:48]</a>. This is tantalizingly close to the problem's goal of finding sums divisible by 5 <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.

## Generalizing with Complex Numbers

To filter for coefficients whose indices are multiples of 5, we need inputs that exhibit a cycling behavior with a period of 5 <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>. This is where [[complex_functions_and_transformations | complex numbers]] become essential <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>.

We use the **fifth roots of unity**. These are [[complex_functions_and_transformations | complex numbers]] `z` such that `z^5 = 1` <a class="yt-timestamp" data-t="00:18:43">[00:18:43]</a>. Graphically, they are points equally spaced around the unit circle in the complex plane <a class="yt-timestamp" data-t="00:17:33">[00:17:33]</a>. Let `zeta` be the principal fifth root of unity, `e^(2*pi*i/5)` (or `cos(72°) + i*sin(72°)`), which sits at 1/5 of a turn around the unit circle <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>.

The powers of `zeta` are:
*   `zeta^0 = 1`
*   `zeta^1 = zeta` (1/5 turn)
*   `zeta^2` (2/5 turn)
*   `zeta^3` (3/5 turn)
*   `zeta^4` (4/5 turn)
*   `zeta^5 = 1` (back to 0/5 turn) <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>

This cycling property is crucial <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>.

### Filtering with Roots of Unity

When we sum `f(x)` evaluated at all five roots of unity (`zeta^0, zeta^1, zeta^2, zeta^3, zeta^4`), a powerful cancellation occurs <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>.
Consider a single term `c_n * x^n` from the expanded `f(x)`:
`c_n * (zeta^0)^n + c_n * (zeta^1)^n + c_n * (zeta^2)^n + c_n * (zeta^3)^n + c_n * (zeta^4)^n`

*   If `n` is *not* divisible by 5, the sum of `(zeta^k)^n` for `k=0,1,2,3,4` will be 0 <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>. (e.g., for `x^1`, the sum `1 + zeta + zeta^2 + zeta^3 + zeta^4 = 0`) <a class="yt-timestamp" data-t="00:19:30">[00:19:30]</a>.
*   If `n` *is* divisible by 5, then `(zeta^k)^n` will always equal 1 for any `k` <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>. (e.g., for `x^5`, the sum `1^5 + zeta^5 + (zeta^2)^5 + (zeta^3)^5 + (zeta^4)^5 = 1 + 1 + 1 + 1 + 1 = 5`) <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>.

Therefore, summing `f(x)` at all five roots of unity yields:
`f(zeta^0) + f(zeta^1) + f(zeta^2) + f(zeta^3) + f(zeta^4) = 5 * (c_0 + c_5 + c_10 + ...)` <a class="yt-timestamp" data-t="00:22:41">[00:22:41]</a>.

This sum acts as a filter, multiplying only the coefficients corresponding to subset sums divisible by 5 by a factor of 5 <a class="yt-timestamp" data-t="00:22:52">[00:22:52]</a>. To get the desired count (the sum of `c_n` where `n` is a multiple of 5), we simply divide this result by 5 <a class="yt-timestamp" data-t="00:23:18">[00:23:18]</a>.

## Evaluating the Function at Roots of Unity

We need to evaluate `f(zeta^k)` using its factored form:
`f(x) = (1 + x)(1 + x^2)...(1 + x^2000)` <a class="yt-timestamp" data-t="00:23:58">[00:23:58]</a>.

Consider `f(zeta)`:
`f(zeta) = (1 + zeta)(1 + zeta^2)(1 + zeta^3)...(1 + zeta^2000)` <a class="yt-timestamp" data-t="00:24:31">[00:24:31]</a>.
Because powers of `zeta` repeat every 5 terms (`zeta^6 = zeta`, `zeta^7 = zeta^2`, etc.), the product consists of 400 repetitions of `(1 + zeta)(1 + zeta^2)(1 + zeta^3)(1 + zeta^4)(1 + zeta^5)` <a class="yt-timestamp" data-t="00:24:43">[00:24:43]</a>.
So, `f(zeta) = [(1 + zeta)(1 + zeta^2)(1 + zeta^3)(1 + zeta^4)(1 + zeta^5)]^400`.

### The "Final Trick"

The product `(1 + zeta)(1 + zeta^2)(1 + zeta^3)(1 + zeta^4)(1 + zeta^5)` can be evaluated using a property of roots of unity <a class="yt-timestamp" data-t="00:27:20">[00:27:20]</a>.
The fifth roots of unity are the roots of the polynomial `z^5 - 1 = 0` <a class="yt-timestamp" data-t="00:27:28">[00:27:28]</a>.
This polynomial can be factored in terms of its roots:
`z^5 - 1 = (z - zeta^0)(z - zeta^1)(z - zeta^2)(z - zeta^3)(z - zeta^4)` <a class="yt-timestamp" data-t="00:27:36">[00:27:36]</a>.
Since `zeta^0 = 1`, we can rewrite this as:
`z^5 - 1 = (z - 1)(z - zeta)(z - zeta^2)(z - zeta^3)(z - zeta^4)` <a class="yt-timestamp" data-t="00:27:41">[00:27:41]</a>.

Dividing both sides by `(z - 1)` (for `z != 1`):
`z^4 + z^3 + z^2 + z + 1 = (z - zeta)(z - zeta^2)(z - zeta^3)(z - zeta^4)` <a class="yt-timestamp" data-t="00:27:56">[00:27:56]</a>.

To get the desired `(1 + zeta)` form, we substitute `z = -1` into the equation:
`(-1)^4 + (-1)^3 + (-1)^2 + (-1) + 1 = (-1 - zeta)(-1 - zeta^2)(-1 - zeta^3)(-1 - zeta^4)` <a class="yt-timestamp" data-t="00:28:07">[00:28:07]</a>.
`1 - 1 + 1 - 1 + 1 = (-1)^4 * (1 + zeta)(1 + zeta^2)(1 + zeta^3)(1 + zeta^4)`
`1 = (1 + zeta)(1 + zeta^2)(1 + zeta^3)(1 + zeta^4)` <a class="yt-timestamp" data-t="00:28:30">[00:28:30]</a>.

So, the product `(1 + zeta)(1 + zeta^2)(1 + zeta^3)(1 + zeta^4)` equals 1.
Remember that `(1 + zeta^5)` is `(1 + 1) = 2`.
Therefore, `(1 + zeta)(1 + zeta^2)(1 + zeta^3)(1 + zeta^4)(1 + zeta^5) = 1 * 2 = 2` <a class="yt-timestamp" data-t="00:28:36">[00:28:36]</a>.

Thus, `f(zeta) = 2^400`.
Similarly, `f(zeta^2)`, `f(zeta^3)`, and `f(zeta^4)` will also equal `2^400` because multiplying `zeta^k` by itself (squaring, cubing, etc.) just shuffles the order of the terms in the product `(1 + x^j)` but doesn't change the overall value <a class="yt-timestamp" data-t="00:28:51">[00:28:51]</a>.

The only remaining term to evaluate is `f(zeta^0)`, which is `f(1)` <a class="yt-timestamp" data-t="00:29:02">[00:29:02]</a>. As established earlier, `f(1) = 2^2000` <a class="yt-timestamp" data-t="00:29:13">[00:29:13]</a>.

## Final Calculation

The total sum of coefficients whose indices are multiples of 5 is:
`(1/5) * [f(zeta^0) + f(zeta^1) + f(zeta^2) + f(zeta^3) + f(zeta^4)]` <a class="yt-timestamp" data-t="00:29:26">[00:29:26]</a>
`= (1/5) * [2^2000 + 2^400 + 2^400 + 2^400 + 2^400]` <a class="yt-timestamp" data-t="00:29:38">[00:29:38]</a>
`= (1/5) * [2^2000 + 4 * 2^400]` <a class="yt-timestamp" data-t="00:29:42">[00:29:42]</a>

This is the precise number of subsets of {1, ..., 2000} whose sum is divisible by 5.

### Sanity Check (Small Example)

For the set {1, 2, 3, 4, 5}, the formula yields:
`(1/5) * [2^5 + 4 * 2^1]` <a class="yt-timestamp" data-t="00:30:01">[00:30:01]</a>
`= (1/5) * [32 + 4 * 2]`
`= (1/5) * [32 + 8]`
`= (1/5) * 40 = 8` <a class="yt-timestamp" data-t="00:30:08">[00:30:08]</a>.
This matches the result found by explicit enumeration for the small example <a class="yt-timestamp" data-t="00:30:08">[00:30:08]</a>.

## Reflection and Broader Implications

The solution highlights the power of transforming a discrete counting problem into one solvable by manipulating [[prime_numbers_and_generating_functions | polynomials]] and evaluating them on [[complex_functions_and_transformations | complex numbers]] <a class="yt-timestamp" data-t="00:30:43">[00:30:43]</a>.

### Connection to Prime Numbers and Riemann Hypothesis

The technique used for this puzzle is similar in spirit to how [[distribution_of_prime_numbers_and_dirichlets_theorem | prime numbers]] are studied, particularly in relation to the Riemann hypothesis <a class="yt-timestamp" data-t="00:31:08">[00:31:08]</a>. In that field, a discrete sequence related to primes is encoded as coefficients in a Dirichlet series (similar to a [[prime_numbers_and_generating_functions | polynomial]]), and information about these coefficients is extracted by studying the function's behavior with [[complex_functions_and_transformations | complex-valued inputs]] <a class="yt-timestamp" data-t="00:31:39">[00:31:39]</a>. Extending the domain to [[complex_functions_and_transformations | complex numbers]] offers significant mathematical power for deductions <a class="yt-timestamp" data-t="00:32:18">[00:32:18]</a>.

### Why Complex Numbers?

[[Complex numbers]] are uniquely suited for problems involving frequency or cycling behavior because operations like multiplication by roots of unity correspond to rotations on the complex plane <a class="yt-timestamp" data-t="00:33:04">[00:33:04]</a>. This property allows for the "filtering" or "constructive interference" seen in the puzzle's solution. This idea is foundational to:
*   **Fourier transforms and Fourier series**: Used extensively in signal processing and analysis to decompose functions into their constituent frequencies <a class="yt-timestamp" data-t="00:33:49">[00:33:49]</a>.
*   **Shor's Algorithm**: A quantum computing algorithm for factoring large numbers, which relies on using roots of unity to detect frequency information in a quantum state <a class="yt-timestamp" data-t="00:33:59">[00:33:59]</a>.

For those interested in learning more about [[prime_numbers_and_generating_functions | generating functions]], "GeneratingFunctionology" by Herbert Wilf is highly recommended <a class="yt-timestamp" data-t="00:34:01">[00:34:01]</a>.