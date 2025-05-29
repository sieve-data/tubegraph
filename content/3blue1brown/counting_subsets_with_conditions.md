---
title: Counting subsets with conditions
videoId: bOXCLR3Wric
---

From: [[3blue1brown]] <br/> 

This article explores a challenging discrete math puzzle that unexpectedly leverages [[Julia Sets and Fatou Sets | complex numbers]] and generating functions to arrive at an exact solution <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. The problem involves counting subsets of a given set whose elements sum up to a number divisible by a specific integer.

## The Puzzle

The puzzle, originating from a book by Titu Andreescu and Zuming Feng used for training the USA International Math Olympiad team, asks:

> Find the number of subsets of the set 1 up to 2000, the sum of whose elements is divisible by 5 <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>.

For example, for the set {1, 2, 3, 4, 5}:
*   The subset {3, 1, 4} sums to 8, which is not divisible by 5 <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>.
*   The subset {2, 3, 5} sums to 10, which *is* divisible by 5 and would be counted <a class="yt-timestamp" data-t="02:13:00">[02:13:00]</a>.
*   The empty set is included, with a sum of 0, which is considered a multiple of 5 <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>.

A brute-force approach, iterating through all possible subsets, is infeasible as there are 2 to the power of 2,000 total subsets—an astronomically large number <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>. While one might initially guess that roughly a fifth of all subsets would have a sum divisible by 5 due to an even distribution, the challenge lies in finding the precise integer answer <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.

### A Simpler Example

Consider the problem for the set {1, 2, 3, 4, 5}. There are 2 to the power of 5 (32) total subsets <a class="yt-timestamp" data-t="04:38:00">[04:38:00]</a>. By listing and summing them, it is found that 8 subsets have a sum divisible by 5 <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>. This is slightly more than the expected 6.4 (a fifth of 32) <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>.

## Generating Functions: The First Twist

The first "unreasonably useful" technique for this discrete problem is the use of a generating function <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>. For the set {1, 2, 3, 4, 5}, the corresponding polynomial is:

`f(x) = (1 + x)(1 + x^2)(1 + x^3)(1 + x^4)(1 + x^5)` <a class="yt-timestamp" data-t="07:08:00">[07:08:00]</a>

When this polynomial is algebraically expanded, each term in the expansion corresponds to a unique subset. The exponent of `x` in each term represents the sum of the elements in that subset <a class="yt-timestamp" data-t="08:44:00">[08:44:00]</a>. For example:
*   Choosing `1` from each parenthetical corresponds to the empty set (`x^0`) <a class="yt-timestamp" data-t="07:46:00">[07:46:00]</a>.
*   Choosing `x` from `(1+x)` and `1` from others corresponds to the subset {1} (`x^1`) <a class="yt-timestamp" data-t="07:53:00">[07:53:00]</a>.
*   Choosing `x` from `(1+x)` and `x^2` from `(1+x^2)` (and `1` from others) corresponds to {1, 2}, yielding `x^3` <a class="yt-timestamp" data-t="08:13:00">[08:13:00]</a>.
*   The coefficient of `x^k` in the fully expanded polynomial represents the number of subsets whose elements sum to `k` <a class="yt-timestamp" data-t="09:24:00">[09:24:00]</a>.

For the original puzzle with the set {1, ..., 2000}, the generating function is:

`f(x) = (1 + x)(1 + x^2)...(1 + x^2000)` <a class="yt-timestamp" data-t="11:00:00">[0:11:00]</a>

The goal is to determine properties of the coefficients `c_n` in the expanded form `f(x) = c_0 + c_1x + c_2x^2 + ... + c_Nx^N` without actually expanding it <a class="yt-timestamp" data-t="11:16:00">[0:11:16]</a>.

### Evaluating the Generating Function at Specific Values

Treating `f(x)` as a function allows for deductions about its coefficients:

*   **`f(0) = c_0 = 1`**: This represents the single empty set <a class="yt-timestamp" data-t="12:17:00">[0:12:17]</a>.
*   **`f(1) = 2^2000`**: Plugging `x=1` into the factored form yields `2^2000` <a class="yt-timestamp" data-t="12:50:00">[0:12:50]</a>. Plugging `x=1` into the expanded form sums all coefficients (`c_0 + c_1 + ...`), which is the total number of subsets <a class="yt-timestamp" data-t="13:00:00">[0:13:00]</a>.
*   **`f(-1) = 0`**: Plugging `x=-1` into the factored form yields `(1-1)(1+(-1)^2)... = 0` because the `(1+x)` term becomes `0` <a class="yt-timestamp" data-t="13:36:00">[0:13:36]</a>. In the expanded form, this creates an alternating sum of coefficients: `c_0 - c_1 + c_2 - c_3 + ... = 0` <a class="yt-timestamp" data-t="13:58:00">[0:13:58]</a>. This implies that the sum of coefficients for even-sum subsets equals the sum of coefficients for odd-sum subsets <a class="yt-timestamp" data-t="14:53:00">[0:14:53]</a>.

This leads to a powerful filtering technique:
`Sum of even coefficients = (f(1) + f(-1)) / 2` <a class="yt-timestamp" data-t="15:27:00">[0:15:27]</a>
`Sum of odd coefficients = (f(1) - f(-1)) / 2`

This method provides the number of subsets with even or odd sums. The puzzle, however, requires finding the number of subsets whose sum is divisible by 5 <a class="yt-timestamp" data-t="15:52:00">[0:15:52]</a>.

## Complex Numbers: The Second Twist

To filter for coefficients divisible by 5, the strategy is to generalize the "alternating sum" idea using [[Julia Sets and Fatou Sets | complex numbers]] <a class="yt-timestamp" data-t="16:31:00">[0:16:31]</a>.

The key lies in using the *fifth roots of unity*. These are [[Julia Sets and Fatou Sets | complex numbers]] on the unit circle that, when raised to the fifth power, equal 1 <a class="yt-timestamp" data-t="18:39:00">[0:18:39]</a>. They are `z_k = e^(i * 2πk / 5)` for `k = 0, 1, 2, 3, 4` <a class="yt-timestamp" data-t="17:42:00">[0:17:42]</a>. Let `ζ = e^(i * 2π / 5)` be the primitive fifth root of unity <a class="yt-timestamp" data-t="17:33:00">[0:17:33]</a>. The roots are `ζ^0 = 1`, `ζ^1`, `ζ^2`, `ζ^3`, `ζ^4`.

### Properties of Roots of Unity

When summed, powers of roots of unity exhibit cancellation or constructive interference:

*   For `k` not a multiple of 5: `ζ^0 + (ζ^k)^1 + (ζ^k)^2 + (ζ^k)^3 + (ζ^k)^4 = 0` <a class="yt-timestamp" data-t="20:00:00">[0:20:00]</a>.
    *   Visually, the vectors representing these complex numbers add up to zero, forming a closed polygon <a class="yt-timestamp" data-t="19:38:00">[0:19:38]</a>.
*   For `k` a multiple of 5 (e.g., `ζ^5 = 1`): `(ζ^5)^0 + (ζ^5)^1 + (ζ^5)^2 + (ζ^5)^3 + (ζ^5)^4 = 1 + 1 + 1 + 1 + 1 = 5` <a class="yt-timestamp" data-t="21:41:00">[0:21:41]</a>.

This property provides the exact filter needed. If we sum the generating function evaluated at each of the five roots of unity:

`f(1) + f(ζ) + f(ζ^2) + f(ζ^3) + f(ζ^4)` <a class="yt-timestamp" data-t="22:29:00">[0:22:29]</a>

Each term `c_n * x^n` in the expansion will be part of this sum. When `n` is *not* a multiple of 5, the sum of `c_n * (1^n + ζ^n + (ζ^2)^n + (ζ^3)^n + (ζ^4)^n)` will be `c_n * 0 = 0`, thus canceling out these terms <a class="yt-timestamp" data-t="22:48:00">[0:22:48]</a>. When `n` *is* a multiple of 5, the sum will be `c_n * (1 + 1 + 1 + 1 + 1) = 5 * c_n`, leading to constructive interference <a class="yt-timestamp" data-t="22:52:00">[0:22:52]</a>.

Therefore, the sum `f(1) + f(ζ) + f(ζ^2) + f(ζ^3) + f(ζ^4)` is equal to `5` times the sum of coefficients `c_n` where `n` is a multiple of 5 <a class="yt-timestamp" data-t="23:02:00">[0:23:02]</a>. To find the desired count, we just need to calculate this sum and divide by 5 <a class="yt-timestamp" data-t="23:24:00">[0:23:24]</a>.

## Calculating `f(ζ^k)`

We already know `f(1) = 2^2000` <a class="yt-timestamp" data-t="29:06:00">[0:29:06]</a>. Now, we need to evaluate `f(ζ)`, `f(ζ^2)`, `f(ζ^3)`, and `f(ζ^4)`.
For `f(ζ)`:
`f(ζ) = (1 + ζ)(1 + ζ^2)...(1 + ζ^2000)` <a class="yt-timestamp" data-t="24:31:00">[0:24:31]</a>

Since powers of `ζ` repeat every 5 terms (`ζ^5 = 1`, `ζ^6 = ζ`, etc.), the product `(1 + ζ^k)` also repeats every 5 terms <a class="yt-timestamp" data-t="24:39:00">[0:24:39]</a>. The entire 2000-term product is effectively 400 copies of the first five terms:
`P = (1 + ζ)(1 + ζ^2)(1 + ζ^3)(1 + ζ^4)(1 + ζ^5)` <a class="yt-timestamp" data-t="24:46:00">[0:24:46]</a>
So, `f(ζ) = P^400`.

The final trick is to realize that the fifth roots of unity are the roots of the polynomial `z^5 - 1 = 0` <a class="yt-timestamp" data-t="18:49:00">[0:18:49]</a>. This means `z^5 - 1` can be factored as:
`z^5 - 1 = (z - 1)(z - ζ)(z - ζ^2)(z - ζ^3)(z - ζ^4)` <a class="yt-timestamp" data-t="27:31:00">[0:27:31]</a>

By plugging in `z = -1` into this equation:
`(-1)^5 - 1 = (-1 - 1)(-1 - ζ)(-1 - ζ^2)(-1 - ζ^3)(-1 - ζ^4)` <a class="yt-timestamp" data-t="28:07:00">[0:28:07]</a>
`-2 = (-1)^5 (1 + 1)(1 + ζ)(1 + ζ^2)(1 + ζ^3)(1 + ζ^4)` <a class="yt-timestamp" data-t="28:13:00">[0:28:13]</a>
`-2 = (-1) * 2 * (1 + ζ)(1 + ζ^2)(1 + ζ^3)(1 + ζ^4)`
`1 = (1 + ζ)(1 + ζ^2)(1 + ζ^3)(1 + ζ^4)`

This product of four terms equals 1. Therefore, the full product `P`:
`P = (1 + ζ)(1 + ζ^2)(1 + ζ^3)(1 + ζ^4)(1 + ζ^5)`
`P = (1) * (1 + 1)` (since `ζ^5 = 1`) <a class="yt-timestamp" data-t="25:27:00">[0:25:27]</a>
`P = 2` <a class="yt-timestamp" data-t="28:30:00">[0:28:30]</a>

So, `f(ζ) = 2^400` <a class="yt-timestamp" data-t="28:47:00">[0:28:47]</a>. Due to the cyclic nature of powers of roots of unity, `f(ζ^2)`, `f(ζ^3)`, and `f(ζ^4)` also equal `2^400` <a class="yt-timestamp" data-t="28:52:00">[0:28:52]</a>.

## The Final Answer

The total number of subsets whose sum is divisible by 5 is:

` (f(1) + f(ζ) + f(ζ^2) + f(ζ^3) + f(ζ^4)) / 5` <a class="yt-timestamp" data-t="29:26:00">[0:29:26]</a>

Plugging in the calculated values:
` (2^2000 + 2^400 + 2^400 + 2^400 + 2^400) / 5` <a class="yt-timestamp" data-t="29:38:00">[0:29:38]</a>
`= (2^2000 + 4 * 2^400) / 5` <a class="yt-timestamp" data-t="29:42:00">[0:29:42]</a>

### Sanity Check with Small Example

For the set {1, 2, 3, 4, 5}, the number of elements is 5, so the powers would be 2^5 and 2^1:
` (2^5 + 4 * 2^1) / 5`
`= (32 + 8) / 5`
`= 40 / 5 = 8` <a class="yt-timestamp" data-t="29:50:00">[0:29:50]</a>
This matches the result from the direct counting for the smaller example <a class="yt-timestamp" data-t="30:08:00">[0:30:08]</a>.

## Reflection and Broader Implications

The solution to this puzzle exemplifies powerful mathematical techniques:

1.  **Generating Functions**: Representing a discrete counting problem as coefficients of a polynomial <a class="yt-timestamp" data-t="30:48:00">[0:30:48]</a>. This concept is widely used in combinatorics, probability, and other areas. For instance, [[infinite_sums_and_approximations | Fibonacci numbers]] can be studied using generating functions <a class="yt-timestamp" data-t="10:02:00">[0:10:02]</a>.
2.  **[[Julia Sets and Fatou Sets | Complex Numbers]]**: Utilizing the properties of roots of unity in the [[Julia Sets and Fatou Sets | complex plane]] to "filter" information about coefficients related to specific frequencies or divisibility rules <a class="yt-timestamp" data-t="30:52:00">[0:30:52]</a>.

This approach is not unique to this toy problem. It shares a "spiritual" similarity with how [[prime_numbers_and_their_regularities | mathematicians understand prime numbers]] and their [[Distribution of prime numbers | distribution]], particularly in the context of the [[Distribution of prime numbers | Riemann hypothesis]] <a class="yt-timestamp" data-t="00:34:00">[0:34:00]</a>. Riemann's work involved a Dirichlet series (a type of generating function) whose coefficients encode information about primes, and insights are gained by analyzing this function with [[Julia Sets and Fatou Sets | complex-valued inputs]] <a class="yt-timestamp" data-t="31:39:00">[0:31:39]</a>.

The "unreasonable effectiveness" of [[Julia Sets and Fatou Sets | complex numbers]] in discrete problems often stems from their ability to represent and detect cyclical or frequency-based information, as seen with the roots of unity <a class="yt-timestamp" data-t="33:00:00">[0:33:00]</a>. This fundamental idea underlies many critical concepts, including Fourier transforms and Fourier series, which are essential in signal processing and many other scientific fields <a class="yt-timestamp" data-t="33:49:00">[0:33:49]</a>. Shor's algorithm for quantum computers, for example, leverages the use of roots of unity to detect frequency information for factoring large numbers <a class="yt-timestamp" data-t="33:31:00">[0:33:31]</a>.